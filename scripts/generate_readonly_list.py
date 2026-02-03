#!/usr/bin/env python3
"""
Generate list of read-only endpoints from schema files.

This script scans all schema JSON files and creates a markdown document
listing all endpoints marked as readonly=true.
"""

import json
from pathlib import Path
from datetime import datetime

def scan_schemas_for_readonly(schema_dir: Path) -> list[dict]:
    """
    Scan schema directory for readonly endpoints.
    
    Args:
        schema_dir: Directory containing schema JSON files
        
    Returns:
        List of dicts with endpoint info (path, help, category, etc.)
    """
    readonly_endpoints = []
    
    # Find all JSON files
    for json_file in sorted(schema_dir.rglob("*.json")):
        # Skip index files
        if json_file.name == "index.json":
            continue
            
        try:
            with open(json_file, 'r') as f:
                schema = json.load(f)
            
            # Check if endpoint is readonly
            if schema.get("readonly", False):
                readonly_endpoints.append({
                    "path": schema.get("path", schema.get("full_path", "unknown")),
                    "help": schema.get("help", "No description available"),
                    "category": schema.get("api_type", schema.get("category", "unknown")),
                    "mkey": schema.get("mkey", None),
                    "class_name": schema.get("class_name", ""),
                })
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Warning: Could not parse {json_file}: {e}")
            continue
    
    return readonly_endpoints


def generate_markdown(endpoints: list[dict], output_file: Path) -> None:
    """
    Generate markdown documentation for readonly endpoints.
    
    Args:
        endpoints: List of endpoint info dicts
        output_file: Output markdown file path
    """
    # Sort by category and path
    endpoints.sort(key=lambda x: (x['category'], x['path']))
    
    # Group by category
    by_category = {}
    for ep in endpoints:
        category = ep['category']
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(ep)
    
    # Generate markdown
    lines = [
        "# Read-Only Endpoints",
        "",
        "This document lists all FortiOS API endpoints that are marked as read-only.",
        "These endpoints provide reference data and do not support POST, PUT, or DELETE operations.",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}  ",
        f"**Total Read-Only Endpoints:** {len(endpoints)}",
        "",
        "---",
        "",
    ]
    
    # Add table of contents
    lines.extend([
        "## Table of Contents",
        "",
    ])
    for category in sorted(by_category.keys()):
        lines.append(f"- [{category.upper()}](#{category})")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Add sections by category
    for category in sorted(by_category.keys()):
        eps = by_category[category]
        lines.extend([
            f"## {category.upper()}",
            "",
            f"**Count:** {len(eps)} endpoints",
            "",
            "| Path | Description | Primary Key |",
            "|------|-------------|-------------|",
        ])
        
        for ep in eps:
            path = ep['path']
            help_text = ep['help'].replace("|", "\\|").replace("\n", " ")
            mkey = ep['mkey'] if ep['mkey'] else "—"
            lines.append(f"| `{path}` | {help_text} | `{mkey}` |")
        
        lines.append("")
    
    # Add usage notes
    lines.extend([
        "---",
        "",
        "## Usage Notes",
        "",
        "### Read-Only Endpoints",
        "",
        "Read-only endpoints provide reference data that cannot be modified through the API:",
        "",
        "- ✅ **GET** operations are supported",
        "- ❌ **POST** operations are not supported (cannot create)",
        "- ❌ **PUT** operations are not supported (cannot update)",
        "- ❌ **DELETE** operations are not supported (cannot delete)",
        "",
        "### Common Read-Only Endpoint Types",
        "",
        "1. **Internet Service Tables**: FortiGuard-managed service definitions",
        "   - `firewall/internet-service`",
        "   - `firewall/internet-service-botnet`",
        "   - `firewall/internet-service-reputation`",
        "",
        "2. **Geographic Reference Data**: Country, city, and region information",
        "   - `firewall/country`",
        "   - `firewall/city`",
        "   - `firewall/region`",
        "",
        "3. **Vendor/Product References**: MAC address vendor lookups, etc.",
        "   - `firewall/vendor-mac`",
        "   - `firewall/vendor-mac-summary`",
        "",
        "### Example Usage",
        "",
        "```python",
        "from hfortix_fortios import FortiOS",
        "",
        "# Connect to FortiGate",
        "fgt = FortiOS(host='192.168.1.99', token='your-token')",
        "",
        "# Query read-only reference data",
        "internet_services = fgt.api.cmdb.firewall.internet_service.get()",
        "",
        "# Filter results",
        "google_services = fgt.api.cmdb.firewall.internet_service.get(",
        "    filter='name=@Google'",
        ")",
        "",
        "# These operations will fail (read-only):",
        "# fgt.api.cmdb.firewall.internet_service.post(...)  # Not supported",
        "# fgt.api.cmdb.firewall.internet_service.put(...)   # Not supported",
        "```",
        "",
    ])
    
    # Write file
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"✅ Generated {output_file}")
    print(f"   Found {len(endpoints)} read-only endpoints")


def main():
    """Main entry point."""
    # Get project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    # Schema directory
    schema_dir = project_root / "schema" / "7.6.5" / "cmdb"
    
    # Output file
    output_file = project_root / "docs" / "fortios" / "READONLY_ENDPOINTS.md"
    
    print(f"Scanning schemas in: {schema_dir}")
    
    # Scan for readonly endpoints
    endpoints = scan_schemas_for_readonly(schema_dir)
    
    # Generate markdown
    generate_markdown(endpoints, output_file)


if __name__ == "__main__":
    main()
