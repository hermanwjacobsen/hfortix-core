#!/usr/bin/env python3
"""
FortiOS Schema Downloader

Downloads API schemas from FortiGate devices for code generation.

Usage:
    # Download all schemas from FortiGate
    python download_schemas.py --host 192.168.1.99 --token YOUR_TOKEN --version 7.6 --all
    
    # Download specific category
    python download_schemas.py --host 192.168.1.99 --token YOUR_TOKEN --version 7.6 --category cmdb
    
    # Download single endpoint
    python download_schemas.py --host 192.168.1.99 --token YOUR_TOKEN --version 7.6 --endpoint cmdb.firewall.address
    
    # Force re-download (overwrite existing)
    python download_schemas.py --host 192.168.1.99 --token YOUR_TOKEN --version 7.6 --all --force
"""

import argparse
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

# Add parent directory to path for local imports
sys.path.insert(0, str(Path(__file__).parent))
from swagger_parser import SwaggerParser


def _utc_timestamp() -> str:
    """Return an ISO 8601 UTC timestamp with trailing Z."""
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


@dataclass
class EndpointInfo:
    """Information about an API endpoint."""
    category: str  # cmdb, monitor, log, service
    path: str      # firewall/address
    name: str      # address
    full_path: str # firewall.address


@dataclass
class DownloadResult:
    """Result of a schema download operation."""
    endpoint: str
    success: bool
    error: str | None = None
    schema_path: Path | None = None
    schema_hash: str | None = None


class SchemaDownloader:
    """Downloads schemas from FortiOS devices."""
    
    def __init__(
        self,
        host: str,
        token: str,
        version: str,
        output_dir: Path,
        verify_ssl: bool = False,
        timeout: float = 30.0,
        vdom: str = "root",
        swagger_docs_dir: Path | None = None,
    ):
        """
        Initialize schema downloader.
        
        Args:
            host: FortiGate IP/hostname
            token: API token for authentication
            version: Version tag for storage (e.g., "7.6")
            output_dir: Base directory for schema storage
            verify_ssl: Whether to verify SSL certificates
            timeout: Request timeout in seconds
            vdom: VDOM to query (default: root)
            swagger_docs_dir: Directory containing Swagger docs (optional, used as fallback)
        """
        self.host = host.rstrip("/")
        self.token = token
        self.version = version
        # New schema uses flat structure: VERSION/category/endpoint.name.json
        # Old used: vVERSION/category/module/endpoint.json
        self.output_dir = output_dir / version
        self.verify_ssl = verify_ssl
        self.timeout = timeout
        self.vdom = vdom
        
        # Initialize Swagger parser if docs directory provided
        self.swagger_parser = None
        if swagger_docs_dir:
            swagger_path = Path(swagger_docs_dir)
            if swagger_path.exists():
                self.swagger_parser = SwaggerParser(swagger_path)
                print(f"📚 Swagger docs loaded from {swagger_path}")
        
        # Create HTTP client
        self.client = httpx.Client(
            base_url=f"https://{self.host}",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=verify_ssl,
            timeout=timeout,
        )
        
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Track downloaded schemas
        self.results: list[DownloadResult] = []
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
    
    def download_schema(
        self,
        category: str,
        endpoint_path: str,
        force: bool = False,
    ) -> DownloadResult:
        """
        Download schema for a single endpoint.
        
        Args:
            category: API category (cmdb, monitor, log, service)
            endpoint_path: Endpoint path (e.g., "firewall/address")
            force: Force re-download even if schema exists
            
        Returns:
            DownloadResult with success status and details
        """
        endpoint_name = endpoint_path.replace("/", ".")
        full_endpoint = f"{category}.{endpoint_name}"
        
        # Build output path - flat structure (e.g., cmdb/firewall.policy.json)
        # New schema uses flat files with dots, not nested directories
        category_dir = self.output_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)
        
        endpoint_file = category_dir / f"{endpoint_name}.json"
        
        # Check if already exists
        if endpoint_file.exists() and not force:
            print(f"⏭️  Skipping {full_endpoint} (already exists)")
            return DownloadResult(
                endpoint=full_endpoint,
                success=True,
                schema_path=endpoint_file,
                error="Already exists (use --force to re-download)"
            )
        
        # Build API URL
        # Handle dot notation for CMDB subcategories
        # FortiGate API uses dots for many CMDB subcategories with 3+ path segments:
        #   /api/v2/cmdb/firewall.schedule/group (not firewall/schedule/group)
        #   /api/v2/cmdb/log.disk/filter (not log/disk/filter)
        #   /api/v2/cmdb/switch-controller.auto-config/default (not switch-controller/auto-config/default)
        #   /api/v2/cmdb/system.autoupdate/schedule (not system/autoupdate/schedule)
        # BUT: Some 2-part endpoints keep slash notation (e.g., log/custom-field, system/modem)
        api_endpoint_path = endpoint_path
        if category == "cmdb":
            parts = endpoint_path.split("/")
            if len(parts) >= 3:
                # Convert to dot notation for 3+ part paths
                # Examples:
                #   firewall/schedule/group -> firewall.schedule/group
                #   log/disk/filter -> log.disk/filter  
                #   switch-controller/auto-config/default -> switch-controller.auto-config/default
                #   system/autoupdate/schedule -> system.autoupdate/schedule
                api_endpoint_path = f"{parts[0]}.{parts[1]}/{'/'.join(parts[2:])}"
            # Note: 2-part endpoints (like log/custom-field, system/modem) keep slash notation
        
        url = f"/api/v2/{category}/{api_endpoint_path}"
        params = {
            "action": "schema",
            "vdom": self.vdom,
        }
        
        try:
            print(f"📥 Downloading {full_endpoint}...")
            try:
                base = str(self.client.base_url)
            except Exception:
                base = f"https://{self.host}"
            print(f"    Request: GET {base}{url} params={params}")
            response = self.client.get(url, params=params)
            response.raise_for_status()
            
            schema_data = response.json()
            
            # Add metadata
            schema_data["_metadata"] = {
                "downloaded_at": _utc_timestamp(),
                "source_host": self.host,
                "source_vdom": self.vdom,
                "category": category,
                "endpoint_path": endpoint_path,
                "full_endpoint": full_endpoint,
            }
            
            # Calculate hash
            schema_json = json.dumps(schema_data, sort_keys=True)
            schema_hash = hashlib.sha256(schema_json.encode()).hexdigest()[:16]
            
            # Write to file
            with open(endpoint_file, "w") as f:
                json.dump(schema_data, f, indent=2)
            
            print(f"✅ Downloaded {full_endpoint} → {endpoint_file}")
            
            return DownloadResult(
                endpoint=full_endpoint,
                success=True,
                schema_path=endpoint_file,
                schema_hash=schema_hash,
            )
            
        except httpx.HTTPStatusError as e:
            # Include the response URL and truncated body for easier debugging
            resp = e.response
            error_msg = f"HTTP {resp.status_code}: {resp.url} - {resp.text[:200]}"
            
            # Try Swagger fallback for various error codes:
            # - 400 (Bad Request): Endpoint doesn't support ?action=schema
            # - 404 (Not Found): Endpoint/feature not available on this device
            # - 405 (Method Not Allowed): Method not supported
            # - 424 (Failed Dependency): Required feature/service not configured
            # - 500 (Internal Server Error): FortiGate error processing request
            # - 503 (Service Unavailable): Service temporarily unavailable
            if resp.status_code in (400, 404, 405, 424, 500, 503) and self.swagger_parser:
                print(f"⚠️  {full_endpoint} returned HTTP {resp.status_code} (no schema support)")
                print(f"    Trying Swagger docs as fallback...")
                
                try:
                    # Get endpoint info from Swagger
                    # Use api_endpoint_path for Swagger lookup (with dot notation)
                    endpoint_info = self.swagger_parser.get_endpoint_info(category, api_endpoint_path)
                    
                    if endpoint_info:
                        # Create minimal schema from Swagger
                        # Use original endpoint_path for schema metadata (to match file structure)
                        schema_data = self.swagger_parser.create_minimal_schema(
                            category, endpoint_path, endpoint_info
                        )
                        
                        # Add metadata
                        schema_data["_metadata"].update({
                            "downloaded_at": _utc_timestamp(),
                            "source_host": self.host,
                            "source_vdom": self.vdom,
                            "fallback_reason": f"HTTP {resp.status_code} from API, used Swagger docs",
                        })
                        
                        # Write minimal schema
                        with open(endpoint_file, "w") as f:
                            json.dump(schema_data, f, indent=2)
                        
                        schema_json = json.dumps(schema_data, sort_keys=True)
                        schema_hash = hashlib.sha256(schema_json.encode()).hexdigest()[:16]
                        
                        print(f"✅ Created from Swagger: {full_endpoint} → {endpoint_file}")
                        
                        return DownloadResult(
                            endpoint=full_endpoint,
                            success=True,
                            schema_path=endpoint_file,
                            schema_hash=schema_hash,
                            error=f"HTTP {resp.status_code} - created from Swagger docs"
                        )
                    else:
                        print(f"    ❌ Endpoint not found in Swagger docs either")
                
                except Exception as swagger_error:
                    print(f"    ❌ Swagger fallback failed: {swagger_error}")
            
            # Other HTTP errors or Swagger fallback failed
            print(f"❌ Failed {full_endpoint}: {error_msg}")
            return DownloadResult(
                endpoint=full_endpoint,
                success=False,
                error=error_msg,
            )
        except Exception as e:
            error_msg = str(e)
            # Try to include the attempted URL in the generic exception
            try:
                attempted = f"{str(self.client.base_url)}{url}"
            except Exception:
                attempted = f"https://{self.host}{url}"
            error_msg = f"{error_msg} (request: {attempted})"
            
            # Try Swagger fallback for JSON parse errors (likely binary/download endpoints)
            if ('JSONDecodeError' in str(type(e)) or 'Expecting value' in error_msg or 'Extra data' in error_msg) and self.swagger_parser:
                print(f"⚠️  {full_endpoint} returned non-JSON response (likely download/action endpoint)")
                print(f"    Trying Swagger docs as fallback...")
                
                try:
                    # Get endpoint info from Swagger
                    endpoint_info = self.swagger_parser.get_endpoint_info(category, api_endpoint_path)
                    
                    if endpoint_info:
                        # Create minimal schema from Swagger
                        schema_data = self.swagger_parser.create_minimal_schema(
                            category, endpoint_path, endpoint_info
                        )
                        
                        # Add metadata
                        schema_data["_metadata"].update({
                            "downloaded_at": _utc_timestamp(),
                            "source_host": self.host,
                            "source_vdom": self.vdom,
                            "fallback_reason": f"JSON parse error - used Swagger docs",
                        })
                        
                        # Write minimal schema
                        with open(endpoint_file, "w") as f:
                            json.dump(schema_data, f, indent=2)
                        
                        schema_json = json.dumps(schema_data, sort_keys=True)
                        schema_hash = hashlib.sha256(schema_json.encode()).hexdigest()[:16]
                        
                        print(f"✅ Created from Swagger: {full_endpoint} → {endpoint_file}")
                        
                        return DownloadResult(
                            endpoint=full_endpoint,
                            success=True,
                            schema_path=endpoint_file,
                            schema_hash=schema_hash,
                            error=f"JSON parse error - created from Swagger docs"
                        )
                    else:
                        print(f"    ❌ Endpoint not found in Swagger docs either")
                
                except Exception as swagger_error:
                    print(f"    ❌ Swagger fallback failed: {swagger_error}")
            
            print(f"❌ Failed {full_endpoint}: {error_msg}")
            return DownloadResult(
                endpoint=full_endpoint,
                success=False,
                error=error_msg,
            )
    
    def discover_endpoints(self, category: str) -> list[str]:
        """
        Discover available endpoints in a category.
        
        Reads existing schema files from the output directory to discover all endpoints.
        
        Args:
            category: API category to discover
            
        Returns:
            List of endpoint paths
        """
        # Check if we have existing schemas for this category
        category_dir = self.output_dir / category
        if not category_dir.exists():
            # No existing schemas, return empty list
            return []
        
        # Find all .json files recursively
        schema_files = list(category_dir.rglob('*.json'))
        
        # Extract endpoint paths from schema files
        endpoints = []
        for schema_file in schema_files:
            # Get relative path from category dir
            # e.g., firewall/address.json -> firewall/address
            rel_path = schema_file.relative_to(category_dir)
            endpoint_path = str(rel_path.with_suffix(''))
            endpoints.append(endpoint_path)
        
        print(f"  📋 Found {len(endpoints)} existing schemas in {category}")
        return sorted(endpoints)
    
    def download_all(
        self,
        categories: list[str] | None = None,
        endpoints: list[str] | None = None,
        force: bool = False,
        max_workers: int = 10,
    ) -> dict[str, Any]:
        """
        Download schemas with parallel processing.
        
        Args:
            categories: Specific categories to download (None = all)
            endpoints: Specific endpoints to download
            force: Force re-download
            max_workers: Concurrent download workers
            
        Returns:
            Summary dictionary with statistics
        """
        if categories is None:
            categories = ["cmdb", "monitor", "log", "service"]
        
        # Build list of endpoints to download
        tasks: list[tuple[str, str]] = []
        
        if endpoints:
            # Download specific endpoints
            for endpoint in endpoints:
                parts = endpoint.split(".", 1)
                if len(parts) == 2:
                    category, path = parts
                    # Skip log category - handled by specialized log_generator
                    if category.lower() == "log":
                        continue
                    tasks.append((category, path.replace(".", "/")))
        else:
            # Download all endpoints in categories
            for category in categories:
                endpoint_list = self.discover_endpoints(category)
                for endpoint_path in endpoint_list:
                    tasks.append((category, endpoint_path))
        
        # Download in parallel
        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self.download_schema, cat, path, force): (cat, path)
                for cat, path in tasks
            }
            
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
        
        self.results = results
        
        # Create summary
        successful = [r for r in results if r.success]
        failed = [r for r in results if not r.success]
        
        summary = {
            "total": len(results),
            "successful": len(successful),
            "failed": len(failed),
            "version": self.version,
            "host": self.host,
            "downloaded_at": _utc_timestamp(),
        }
        
        # Save summary metadata (with .meta.json extension to distinguish from schemas)
        summary_file = self.output_dir / ".download_metadata.json"
        with open(summary_file, "w") as f:
            json.dump(summary, f, indent=2)
        
        # Create index (with .meta.json extension to distinguish from schemas)
        self.create_index()
        
        return summary
    
    def create_index(self):
        """Create index of all downloaded schemas."""
        index = {}
        
        for result in self.results:
            if result.success and result.schema_path:
                index[result.endpoint] = {
                    "schema_path": str(result.schema_path.relative_to(self.output_dir)),
                    "schema_hash": result.schema_hash,
                }
        
        # Use .schema_index.json to distinguish from API schemas
        index_file = self.output_dir / ".schema_index.json"
        with open(index_file, "w") as f:
            json.dump(index, f, indent=2, sort_keys=True)
        
        print(f"\n📋 Created index: {index_file}")
        print(f"   Total endpoints: {len(index)}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Download FortiOS API schemas for code generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    
    # Connection arguments
    parser.add_argument("--host", required=True, help="FortiGate IP/hostname")
    parser.add_argument("--token", required=True, help="API token")
    parser.add_argument("--version", required=True, help="FortiOS version (e.g., 7.6)")
    parser.add_argument("--vdom", default="root", help="VDOM to query (default: root)")
    parser.add_argument("--no-verify-ssl", action="store_true", help="Disable SSL verification")
    parser.add_argument("--timeout", type=float, default=30.0, help="Request timeout (seconds)")
    
    # Download scope
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true", help="Download all schemas")
    group.add_argument("--category", help="Download specific category (cmdb, monitor, log, service)")
    group.add_argument("--endpoint", help="Download specific endpoint (e.g., cmdb.firewall.address)")
    
    # Options
    parser.add_argument("--force", action="store_true", help="Force re-download (overwrite existing)")
    parser.add_argument("--max-workers", type=int, default=10, help="Parallel download workers")
    parser.add_argument("--output-dir", type=Path, default=Path(".dev/generator/schemas"), help="Output directory")
    
    args = parser.parse_args()
    
    # Determine what to download
    categories = None
    endpoints = None
    
    if args.all:
        categories = None  # Download all
    elif args.category:
        categories = [args.category]
    elif args.endpoint:
        endpoints = [args.endpoint]
    
    # Download schemas
    print(f"🚀 FortiOS Schema Downloader")
    print(f"   Host: {args.host}")
    print(f"   Version: {args.version}")
    print(f"   Output: {args.output_dir}/v{args.version}/")
    print()
    
    with SchemaDownloader(
        host=args.host,
        token=args.token,
        version=args.version,
        output_dir=args.output_dir,
        verify_ssl=not args.no_verify_ssl,
        timeout=args.timeout,
        vdom=args.vdom,
    ) as downloader:
        summary = downloader.download_all(
            categories=categories,
            endpoints=endpoints,
            force=args.force,
            max_workers=args.max_workers,
        )
        
        # Print summary
        print(f"\n📊 Download Summary")
        print(f"   ✅ Successful: {summary['successful']}")
        print(f"   ❌ Failed: {summary['failed']}")
        print(f"   📁 Total: {summary['total']}")
        
        if summary['failed'] > 0:
            sys.exit(1)


if __name__ == "__main__":
    main()
