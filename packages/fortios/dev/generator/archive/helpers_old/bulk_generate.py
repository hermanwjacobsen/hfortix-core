#!/usr/bin/env python3
"""
Bulk Endpoint Generator - Generate multiple FortiOS API endpoints from JSON list.

This script provides convenient bulk generation with filtering, progress tracking,
and error handling for generating large numbers of endpoints.

Usage:
    # Generate all CMDB endpoints
    python bulk_generate.py --category cmdb
    
    # Generate all endpoints (CMDB, Monitor, Log, Service)
    python bulk_generate.py --all
    
    # Generate specific subcategory
    python bulk_generate.py --filter firewall
    
    # Generate with custom FortiGate
    python bulk_generate.py --category cmdb --host 192.168.1.99 --token YOUR_TOKEN
    
    # Dry run (show what would be generated)
    python bulk_generate.py --category cmdb --dry-run
"""

import argparse
import json
import sys
import time
from pathlib import Path
from typing import List, Dict

# Endpoints JSON file
ENDPOINTS_FILE = Path(__file__).parent.parent / ".dev" / "endpoints_all.json"


def load_endpoints() -> Dict:
    """Load endpoints from JSON file."""
    if not ENDPOINTS_FILE.exists():
        print(f"❌ Error: Endpoints file not found: {ENDPOINTS_FILE}")
        print("   Run: python .dev/extract_all_endpoints.py")
        sys.exit(1)
    
    with open(ENDPOINTS_FILE) as f:
        return json.load(f)


def filter_endpoints(
    data: Dict,
    category: str = None,
    subcategory: str = None,
    filter_text: str = None,
    limit: int = None
) -> List[Dict]:
    """
    Filter endpoints based on criteria.
    
    Args:
        data: Endpoints data from JSON
        category: Filter by category (cmdb, monitor, log, service)
        subcategory: Filter by subcategory (firewall, system, etc.)
        filter_text: Filter by text in endpoint path
        limit: Maximum number of endpoints
        
    Returns:
        List of filtered endpoint dictionaries
    """
    endpoints = data.get("flat_list", [])
    
    # Apply filters
    if category:
        endpoints = [e for e in endpoints if e["category"] == category]
    
    if subcategory:
        endpoints = [e for e in endpoints if e["subcategory"] == subcategory]
    
    if filter_text:
        endpoints = [
            e for e in endpoints
            if filter_text.lower() in e["endpoint"].lower()
        ]
    
    # Apply limit
    if limit:
        endpoints = endpoints[:limit]
    
    return endpoints


def generate_endpoint(endpoint_path: str, host: str, token: str, dry_run: bool = False) -> bool:
    """
    Generate a single endpoint using the generator.
    
    Args:
        endpoint_path: Full endpoint path (e.g., cmdb.firewall/policy)
        host: FortiGate host
        token: API token
        dry_run: If True, just print what would be done
        
    Returns:
        True if successful, False otherwise
    """
    if dry_run:
        print(f"    [DRY RUN] Would generate: {endpoint_path}")
        return True
    
    # Import here to avoid circular imports
    sys.path.insert(0, str(Path(__file__).parent))
    from generate import CodeGenerator
    
    try:
        generator = CodeGenerator(
            fortios_host=host,
            fortios_token=token,
            fortios_version="7.6",
            output_dir=Path(__file__).parent.parent / "packages" / "fortios" / "hfortix_fortios" / "api" / "v2",
            template_dir=Path(__file__).parent.parent / "templates",  # .dev/generator/templates
            schema_dir=Path(__file__).parent.parent / ".dev" / "schemas",
        )
        
        generator.generate_endpoint(endpoint_path)
        return True
    
    except Exception as e:
        print(f"    ❌ Error: {e}")
        return False


def main():
    """Main execution."""
    parser = argparse.ArgumentParser(
        description="Bulk generate FortiOS API endpoints",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all CMDB endpoints
  python bulk_generate.py --category cmdb
  
  # Generate all firewall endpoints
  python bulk_generate.py --filter firewall
  
  # Generate first 10 system endpoints (testing)
  python bulk_generate.py --subcategory system --limit 10
  
  # Dry run to see what would be generated
  python bulk_generate.py --category cmdb --dry-run
  
  # Generate all endpoints (1200+)
  python bulk_generate.py --all
        """,
    )
    
    # Filtering
    parser.add_argument(
        "--category",
        choices=["cmdb", "monitor", "log", "service"],
        help="Filter by category",
    )
    parser.add_argument(
        "--subcategory",
        help="Filter by subcategory (e.g., firewall, system, router)",
    )
    parser.add_argument(
        "--filter",
        help="Filter by text in endpoint path (case-insensitive)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Maximum number of endpoints to generate",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Generate all endpoints (no filtering)",
    )
    
    # FortiGate connection
    parser.add_argument(
        "--host",
        default="192.168.1.99",
        help="FortiGate host (default: 192.168.1.99)",
    )
    parser.add_argument(
        "--token",
        help="FortiGate API token (or set FORTIOS_TOKEN env var)",
    )
    
    # Options
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without actually generating",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue generating even if some endpoints fail",
    )
    
    args = parser.parse_args()
    
    # Get token
    import os
    token = args.token or os.environ.get("FORTIOS_TOKEN")
    if not token and not args.dry_run:
        print("❌ Error: FortiGate API token required")
        print("   Provide via --token or FORTIOS_TOKEN environment variable")
        sys.exit(1)
    
    # Load endpoints
    print("📋 Loading endpoints...")
    data = load_endpoints()
    
    # Apply filters
    endpoints = filter_endpoints(
        data,
        category=args.category,
        subcategory=args.subcategory,
        filter_text=args.filter,
        limit=args.limit if not args.all else None,
    )
    
    if not endpoints:
        print("❌ No endpoints match the filter criteria")
        sys.exit(1)
    
    # Show summary
    print(f"\n{'='*80}")
    print(f"Bulk Endpoint Generator")
    print(f"{'='*80}")
    print(f"Total endpoints to generate: {len(endpoints)}")
    
    if args.category:
        print(f"Category filter: {args.category}")
    if args.subcategory:
        print(f"Subcategory filter: {args.subcategory}")
    if args.filter:
        print(f"Text filter: {args.filter}")
    if args.dry_run:
        print(f"Mode: DRY RUN (no actual generation)")
    
    # Show first few endpoints
    print(f"\nFirst 5 endpoints:")
    for ep in endpoints[:5]:
        print(f"  - {ep['full_path']}")
    if len(endpoints) > 5:
        print(f"  ... and {len(endpoints) - 5} more")
    
    # Confirm
    if not args.dry_run:
        response = input(f"\n⚠️  Generate {len(endpoints)} endpoints? [y/N]: ")
        if response.lower() != 'y':
            print("Cancelled.")
            sys.exit(0)
    
    # Generate
    print(f"\n{'='*80}")
    print("Starting generation...")
    print(f"{'='*80}\n")
    
    successful = []
    failed = []
    start_time = time.time()
    
    for i, endpoint_data in enumerate(endpoints, 1):
        endpoint_path = endpoint_data["full_path"]
        
        print(f"[{i}/{len(endpoints)}] {endpoint_path}")
        
        success = generate_endpoint(endpoint_path, args.host, token, args.dry_run)
        
        if success:
            successful.append(endpoint_path)
        else:
            failed.append(endpoint_path)
            if not args.continue_on_error and not args.dry_run:
                print("\n❌ Stopping due to error (use --continue-on-error to continue)")
                break
    
    # Summary
    elapsed = time.time() - start_time
    print(f"\n{'='*80}")
    print(f"Generation Complete")
    print(f"{'='*80}")
    print(f"✅ Successful: {len(successful)}/{len(endpoints)}")
    if failed:
        print(f"❌ Failed: {len(failed)}/{len(endpoints)}")
    print(f"⏱️  Time: {elapsed:.1f} seconds ({elapsed/len(endpoints):.2f}s per endpoint)")
    
    if failed:
        print(f"\nFailed endpoints:")
        for ep in failed[:20]:
            print(f"  - {ep}")
        if len(failed) > 20:
            print(f"  ... and {len(failed) - 20} more")


if __name__ == "__main__":
    main()
