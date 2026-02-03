#!/usr/bin/env python3
"""
LOG Endpoint Generator (Template-Based)

Generates LOG category endpoints from schema files using Jinja2 templates.
Unlike CMDB/Monitor/Service endpoints, LOG endpoints use nested class hierarchy
to represent path parameters like:
  /log/disk/{type}/archive
  /log/disk/event/{subtype}/raw

This generator:
  - Uses Jinja2 templates for consistent code generation
  - Returns FortiObjectList instead of dict
  - Has explicit typed parameters (rows, filter, session_id, etc.)
  - Generates proper .pyi stubs with full type annotations

Example API usage:
  fgt.api.log.disk.ips.get(rows=100, filter='severity>=high')
  fgt.api.log.disk.event.vpn.get(rows=50)
"""

from pathlib import Path
from typing import Any
import json

from jinja2 import Environment, FileSystemLoader

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.naming import to_class_name, kebab_to_snake


class LogEndpointGenerator:
    """Template-based generator for LOG category endpoints."""
    
    def __init__(
        self, 
        schema_dir: Path | None = None, 
        output_dir: Path | None = None, 
        template_dir: Path | None = None,
        swagger_docs_dir: Path | None = None,
        stubs_dir: Path | None = None,
    ):
        """
        Initialize LOG endpoint generator.
        
        Args:
            schema_dir: Directory containing version schemas (e.g., schema/7.6.5)
            output_dir: Base output directory for generated files (api/v2)
            template_dir: Directory containing Jinja2 templates
            swagger_docs_dir: Swagger documentation directory (deprecated)
            stubs_dir: Directory for .pyi stub files (optional)
        """
        # Handle schema_dir - it should be the version directory (e.g., schema/7.6.5)
        # We need to append /log to get to the log schemas
        effective_schema_dir = schema_dir or swagger_docs_dir
        if effective_schema_dir is None:
            effective_schema_dir = Path(__file__).parent.parent.parent.parent / "schema" / "7.6.5"
        
        # Append /log if not already there
        if effective_schema_dir.name != "log":
            self.schema_dir = effective_schema_dir / "log"
        else:
            self.schema_dir = effective_schema_dir
            
        self.output_dir = output_dir or Path(__file__).parent.parent.parent.parent / "packages" / "fortios" / "hfortix_fortios" / "api" / "v2"
        self.log_dir = self.output_dir / "log"
        self.stubs_dir = stubs_dir
        
        # Set up Jinja2 environment
        if template_dir is None:
            template_dir = Path(__file__).parent.parent / "templates"
        
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        
        # Add custom filters
        self.env.filters["to_class_name"] = to_class_name
        self.env.filters["kebab_to_snake"] = kebab_to_snake
        
    def generate_all(self) -> dict[str, int]:
        """
        Generate all LOG endpoints from schema files.
        
        Returns:
            Dict with counts: {'disk': 15, 'memory': 12, ...}
        """
        print(f"\n🔄 LOG Endpoint Generator (Template-Based)")
        print(f"   Schema dir: {self.schema_dir}")
        print(f"   Output dir: {self.log_dir}")
        
        if not self.schema_dir.exists():
            print(f"⚠️  LOG schema directory not found: {self.schema_dir}")
            return {}
        
        # Clean up old files
        self._cleanup_old_files()
        
        # Ensure output directory exists
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # Group schemas by subcategory (disk, memory, fortianalyzer, forticloud, search)
        schemas_by_subcategory = self._group_schemas_by_subcategory()
        
        stats = {}
        subcategories = []
        
        for subcategory, schemas in sorted(schemas_by_subcategory.items()):
            print(f"\n📋 Generating {subcategory}...")
            count = self._generate_subcategory(subcategory, schemas)
            stats[subcategory] = count
            subcategories.append({
                "module": subcategory,
                "class_name": to_class_name(subcategory)
            })
        
        # Generate __init__.py and __init__.pyi
        print(f"\n📝 Generating __init__.py and __init__.pyi...")
        self._generate_init(subcategories)
        self._generate_init_pyi(subcategories)
        
        return stats
    
    def _cleanup_old_files(self):
        """Remove old generated LOG files."""
        import shutil
        
        if not self.log_dir.exists():
            return
        
        print(f"\n🧹 Cleaning up old LOG files...")
        
        # Remove all .py and .pyi files
        for pattern in ["*.py", "*.pyi"]:
            for file in self.log_dir.glob(pattern):
                if file.name != "__pycache__":
                    file.unlink()
                    print(f"  🗑️  Removed {file.name}")
    
    def _group_schemas_by_subcategory(self) -> dict[str, list[dict]]:
        """Group log schemas by subcategory (disk, memory, etc.)."""
        schemas_by_subcategory: dict[str, list[dict]] = {}
        
        for schema_file in sorted(self.schema_dir.glob("*.json")):
            # Parse filename: disk.ips.json, disk.event.vpn.json, etc.
            parts = schema_file.stem.split(".")
            if len(parts) < 2:
                continue
            
            subcategory = parts[0]  # disk, memory, fortianalyzer, forticloud, search
            
            # Load schema
            with open(schema_file) as f:
                schema = json.load(f)
            
            # Add parsed path info
            schema["_parts"] = parts[1:]  # Everything after subcategory
            schema["_filename"] = schema_file.stem
            
            if subcategory not in schemas_by_subcategory:
                schemas_by_subcategory[subcategory] = []
            
            schemas_by_subcategory[subcategory].append(schema)
        
        return schemas_by_subcategory
    
    def _generate_subcategory(self, subcategory: str, schemas: list[dict]) -> int:
        """Generate Python and stub files for a LOG subcategory."""
        class_name = to_class_name(subcategory)
        
        # Build the class hierarchy from schemas
        hierarchy = self._build_hierarchy(subcategory, schemas)
        
        # Prepare template context
        context = {
            "class_name": class_name,
            "subcategory": subcategory,
            "examples": self._get_examples(subcategory, hierarchy),
            "attributes": hierarchy["attributes"],
            "endpoint_classes": hierarchy["classes"],
        }
        
        # Render and write .py file
        py_template = self.env.get_template("log_endpoint.py.j2")
        py_content = py_template.render(**context)
        py_file = self.log_dir / f"{subcategory}.py"
        py_file.write_text(py_content)
        print(f"  ✅ Generated {py_file.name}")
        
        # Render and write .pyi file
        pyi_template = self.env.get_template("log_endpoint.pyi.j2")
        pyi_content = pyi_template.render(**context)
        pyi_file = self.log_dir / f"{subcategory}.pyi"
        pyi_file.write_text(pyi_content)
        print(f"  ✅ Generated {pyi_file.name}")
        
        return len(schemas)
    
    def _build_hierarchy(self, subcategory: str, schemas: list[dict]) -> dict:
        """
        Build nested class hierarchy from schemas.
        
        Example structure for disk:
        - DiskIps (has get())
        - DiskIpsArchive (has get())
        - DiskEvent (no get, has subtype attributes)
        - DiskEventVpn (has get())
        """
        # Track all endpoints and their properties
        endpoints: dict[str, dict] = {}
        
        for schema in schemas:
            parts = schema["_parts"]
            
            # Handle .raw variants as nested attributes under the main endpoint
            is_raw = parts and parts[-1] == "raw"
            
            # Build the class name from parts
            # e.g., ["ips"] -> DiskIps, ["event", "vpn"] -> DiskEventVpn
            # For raw: ["webfilter", "raw"] -> DiskWebfilterRaw
            class_suffix = "".join(to_class_name(p) for p in parts)
            full_class_name = f"{to_class_name(subcategory)}{class_suffix}"
            
            # Determine the API path (without /log/ prefix - that comes from api_type)
            api_path = f"{subcategory}/{'/'.join(p.replace('_', '-') for p in parts)}"
            
            # Create endpoint entry
            endpoints[full_class_name] = {
                "class_name": full_class_name,
                "parts": parts,
                "api_path": api_path,
                "has_get": True,
                "is_raw": is_raw,
                "log_type": " ".join(parts) if parts else subcategory,
                "example_path": ".".join(parts) if parts else "",
                "docstring": self._get_endpoint_docstring(subcategory, parts, schema),
                "schema": schema,
            }
            
            # Also ensure parent classes exist (for nested hierarchy)
            for i in range(len(parts) - 1):
                parent_parts = parts[:i + 1]
                parent_suffix = "".join(to_class_name(p) for p in parent_parts)
                parent_class_name = f"{to_class_name(subcategory)}{parent_suffix}"
                
                if parent_class_name not in endpoints:
                    # Parent class without its own get() - just a container
                    endpoints[parent_class_name] = {
                        "class_name": parent_class_name,
                        "parts": parent_parts,
                        "api_path": None,
                        "has_get": False,
                        "is_raw": False,
                        "log_type": " ".join(parent_parts),
                        "example_path": ".".join(parent_parts),
                        "docstring": f"{parent_class_name} log category.",
                        "schema": None,
                    }
        
        # Build attributes for each class
        for endpoint in endpoints.values():
            endpoint["attributes"] = []
            endpoint["init_params"] = ""
            endpoint["init_params_typed"] = ""
            endpoint["stored_params"] = []
            
            # Find direct children (one level deeper)
            my_parts = endpoint["parts"]
            my_depth = len(my_parts)
            
            for other_name, other in endpoints.items():
                other_parts = other["parts"]
                if len(other_parts) == my_depth + 1 and other_parts[:my_depth] == my_parts:
                    # This is a direct child
                    child_attr_name = kebab_to_snake(other_parts[-1])
                    endpoint["attributes"].append({
                        "name": child_attr_name,
                        "class_name": other_name,
                        "init_args": "",
                    })
        
        # Sort attributes alphabetically
        for endpoint in endpoints.values():
            endpoint["attributes"].sort(key=lambda x: x["name"])
        
        # Build main class attributes (top-level children)
        main_attributes = []
        for name, endpoint in endpoints.items():
            if len(endpoint["parts"]) == 1:
                attr_name = kebab_to_snake(endpoint["parts"][0])
                main_attributes.append({
                    "name": attr_name,
                    "class_name": name,
                })
        
        main_attributes.sort(key=lambda x: x["name"])
        
        # Sort classes for output (by depth, then name)
        sorted_classes = sorted(
            endpoints.values(),
            key=lambda x: (len(x["parts"]), x["class_name"])
        )
        
        return {
            "attributes": main_attributes,
            "classes": sorted_classes,
        }
    
    def _get_endpoint_docstring(self, subcategory: str, parts: list[str], schema: dict) -> str:
        """Generate docstring for an endpoint class."""
        if not parts:
            return f"{to_class_name(subcategory)} log operations."
        
        help_text = schema.get("help", "")
        if help_text:
            # Truncate and clean up help text
            help_text = help_text.split(".")[0] + "."
            return help_text
        
        log_type = " ".join(parts)
        return f"{to_class_name(subcategory)} {log_type} log operations."
    
    def _get_examples(self, subcategory: str, hierarchy: dict) -> list[str]:
        """Generate example usage for docstring."""
        examples = []
        
        # Find a few representative endpoints
        for cls in hierarchy["classes"][:3]:
            if cls["has_get"] and cls["example_path"]:
                examples.append(
                    f"fgt.api.log.{subcategory}.{cls['example_path']}.get(rows=100)"
                )
        
        if not examples:
            examples.append(f"fgt.api.log.{subcategory}.get()")
        
        return examples
    
    def _generate_init(self, subcategories: list[dict]):
        """Generate __init__.py for LOG category."""
        lines = [
            '"""LOG API - Auto-generated __init__ file."""',
            '',
            'from typing import TYPE_CHECKING',
            '',
        ]
        
        # Import all subcategory classes
        for subcat in subcategories:
            lines.append(f'from .{subcat["module"]} import {subcat["class_name"]}')
        
        lines.extend([
            '',
            'if TYPE_CHECKING:',
            '    from hfortix_core.http.interface import IHTTPClient',
            '',
            '',
            'class Log:',
            '    """Container for LOG endpoints.',
            '    ',
            '    Provides access to log query endpoints for different storage locations:',
            '    - disk: Logs stored on local disk',
            '    - memory: Logs stored in memory',
            '    - fortianalyzer: Logs from FortiAnalyzer',
            '    - forticloud: Logs from FortiCloud',
            '    - search: Log search operations',
            '    """',
            '',
            '    def __init__(self, client: "IHTTPClient"):',
            '        """Initialize LOG category."""',
        ])
        
        # Add all subcategory attributes
        for subcat in subcategories:
            lines.append(f'        self.{subcat["module"]} = {subcat["class_name"]}(client)')
        
        lines.append('')
        
        init_file = self.log_dir / "__init__.py"
        init_file.write_text('\n'.join(lines))
        print(f"  ✅ Generated __init__.py")
    
    def _generate_init_pyi(self, subcategories: list[dict]):
        """Generate __init__.pyi for LOG category."""
        template = self.env.get_template("log_init.pyi.j2")
        content = template.render(subcategories=subcategories)
        
        pyi_file = self.log_dir / "__init__.pyi"
        pyi_file.write_text(content)
        print(f"  ✅ Generated __init__.pyi")


def main():
    """Run the LOG endpoint generator."""
    base_dir = Path(__file__).parent.parent.parent.parent
    schema_dir = base_dir / "schema" / "7.6.5"
    output_dir = base_dir / "packages" / "fortios" / "hfortix_fortios" / "api" / "v2"
    template_dir = Path(__file__).parent.parent / "templates"
    
    generator = LogEndpointGenerator(schema_dir, output_dir, template_dir)
    stats = generator.generate_all()
    
    print("\n" + "=" * 60)
    print("LOG Generation Summary:")
    print("=" * 60)
    total = 0
    for subcategory, count in sorted(stats.items()):
        print(f"  {subcategory:20} : {count:3} schemas")
        total += count
    print("-" * 60)
    print(f"  {'Total':20} : {total:3} schemas")
    print("=" * 60)


if __name__ == "__main__":
    main()
