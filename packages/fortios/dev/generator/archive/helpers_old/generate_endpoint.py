#!/usr/bin/env python3
"""
Generic Endpoint Generator

Generates FortiOS endpoints by downloading schemas from FortiGate.

Supported Categories:
    - cmdb:    Configuration endpoints (full CRUD)
    - monitor: Monitoring endpoints (GET/POST)
    - service: Service endpoints

NOT Supported:
    - log: Log endpoints use composition pattern, manually implemented
           (see api/v2/log/ for manual implementation)

Usage:
    python generate_endpoint.py cmdb firewall.service/custom
    python generate_endpoint.py cmdb firewall/policy
    python generate_endpoint.py monitor casb/saas-application
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from schema_parser import SchemaParser
from generators.endpoint_generator import EndpointGenerator
from generators.validator_generator import ValidatorGenerator


def download_schema(host: str, token: str, category: str, endpoint_path: str) -> dict:
    """
    Download schema from FortiGate.
    
    Args:
        host: FortiGate hostname/IP
        token: API token
        category: API category (cmdb, monitor, log, service)
        endpoint_path: Endpoint path (e.g., "firewall/policy" or "firewall.service/custom")
        
    Returns:
        Schema dictionary
    """
    import requests
    from urllib3 import disable_warnings
    from urllib3.exceptions import InsecureRequestWarning
    
    disable_warnings(InsecureRequestWarning)
    
    # Build URL - use original endpoint path for API call
    url = f"https://{host}/api/v2/{category}/{endpoint_path}?action=schema"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    print(f"  📥 Downloading schema from {host}...")
    print(f"     URL: {url}")
    
    response = requests.get(url, headers=headers, verify=False, timeout=30)
    response.raise_for_status()
    
    data = response.json()
    
    # Wrap with metadata
    wrapped = {
        "_metadata": {
            "category": category,
            "endpoint_path": endpoint_path,
            "downloaded_at": "2026-01-03T12:00:00Z",
            "fortigate_host": host,
        },
        "results": data.get("results", {})
    }
    
    return wrapped


def main():
    parser = argparse.ArgumentParser(
        description="Generate FortiOS endpoint from schema",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Normal endpoint
  python generate_endpoint.py cmdb firewall/policy
  
  # Edge case (dot in name)
  python generate_endpoint.py cmdb firewall.service/custom
  python generate_endpoint.py cmdb firewall.ssh/setting
  
  # With custom FortiGate
  python generate_endpoint.py cmdb firewall/address --host 192.168.1.99 --token YOUR_TOKEN
        """
    )
    
    parser.add_argument("category", help="API category (cmdb, monitor, log, service)")
    parser.add_argument("endpoint", help="Endpoint path (e.g., firewall/policy or firewall.service/custom)")
    parser.add_argument("--host", default="192.168.1.99", help="FortiGate hostname/IP")
    parser.add_argument("--token-file", default=".env", help="File containing API token")
    parser.add_argument("--token", help="API token (overrides --token-file)")
    parser.add_argument("--skip-download", action="store_true", help="Skip schema download (use cached)")
    parser.add_argument("--output-dir", help="Custom output directory")
    
    args = parser.parse_args()
    
    # Get API token
    if args.token:
        api_token = args.token
    else:
        # Try to read from .env file
        env_file = Path(args.token_file)
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("FORTIGATE_TOKEN="):
                    api_token = line.split("=", 1)[1].strip().strip('"\'')
                    break
            else:
                print(f"❌ No FORTIGATE_TOKEN found in {args.token_file}")
                sys.exit(1)
        else:
            print(f"❌ Token file not found: {args.token_file}")
            print("   Use --token or create .env with FORTIGATE_TOKEN=your_token")
            sys.exit(1)
    
    print(f"🚀 Generating {args.category}.{args.endpoint}\n")
    
    # Paths
    base_dir = Path(__file__).parent
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = base_dir.parent.parent / "packages" / "fortios" / "hfortix_fortios" / "api" / "v2"
    template_dir = base_dir / "templates"
    
    print(f"📂 Output: {output_dir}")
    print(f"📂 Templates: {template_dir}")
    print()
    
    # Download or load schema
    if not args.skip_download:
        try:
            schema_dict = download_schema(args.host, api_token, args.category, args.endpoint)
        except Exception as e:
            print(f"❌ Failed to download schema: {e}")
            sys.exit(1)
    else:
        print("⏭️  Skipping download (using cached schema)")
        # You'd need to implement schema caching
        print("❌ Schema caching not yet implemented")
        sys.exit(1)
    
    # Parse schema
    print("  🔍 Parsing schema...")
    schema = SchemaParser.parse(schema_dict, source_file=f"{args.category}_{args.endpoint}")
    
    print(f"     Category: {schema.category}")
    print(f"     Path: {schema.path}")
    print(f"     API path: {schema.api_path}")
    print(f"     File name: {schema.file_name}")
    print(f"     Class name: {schema.class_name}")
    print(f"     Fields: {len(schema.fields)}")
    print(f"     Required: {len(schema.required_fields)}")
    print()
    
    # Generate endpoint
    print("  ✨ Generating endpoint class...")
    endpoint_gen = EndpointGenerator(template_dir)
    endpoint_file = endpoint_gen.generate(schema, output_dir)
    print(f"     ✅ {endpoint_file}")
    
    # Generate validator
    print("  ✨ Generating validator...")
    validator_gen = ValidatorGenerator(template_dir)
    validator_file = validator_gen.generate(schema, output_dir)
    print(f"     ✅ {validator_file}")
    
    print("\n✅ Generation complete!")
    print(f"\n📄 Generated files:")
    print(f"   Endpoint:  {endpoint_file}")
    print(f"   Validator: {validator_file}")
    
    # Show file sizes
    print(f"\n📏 File sizes:")
    print(f"   Endpoint:  {endpoint_file.stat().st_size:,} bytes")
    print(f"   Validator: {validator_file.stat().st_size:,} bytes")
    
    # Show usage example
    print(f"\n💡 Usage example:")
    endpoint_access = f"fgt.api.{args.category}.{args.endpoint.replace('/', '.').replace('.', '.')}"
    print(f"   from hfortix_fortios import FortiOS")
    print(f"   fgt = FortiOS(host='{args.host}', token='...')")
    print(f"   items = {endpoint_access}.get()")


if __name__ == "__main__":
    main()
