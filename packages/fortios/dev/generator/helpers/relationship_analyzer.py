"""
Relationship analyzer for FortiOS API endpoints.

Builds reverse dependency maps showing which endpoints reference each endpoint.
"""

import json
import logging
from collections import defaultdict
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class RelationshipAnalyzer:
    """Analyzes endpoint relationships from schema files."""
    
    def __init__(self, schema_dir: Path):
        """
        Initialize analyzer.
        
        Args:
            schema_dir: Directory containing schema JSON files (e.g., schema/7.6.5/)
        """
        self.schema_dir = schema_dir
        self.reverse_dependencies: dict[str, list[dict[str, Any]]] = defaultdict(list)
        
    def analyze_all_schemas(self) -> dict[str, list[dict[str, Any]]]:
        """
        Analyze all schemas to build reverse dependency map.
        
        Returns:
            Map of {endpoint: [{"endpoint": "referencing_endpoint", "fields": ["field1", "field2"]}]}
            
        Example:
            {
                "firewall/address": [
                    {"endpoint": "firewall/policy", "fields": ["srcaddr", "dstaddr"]},
                    {"endpoint": "vpn.ipsec/phase2", "fields": ["src-name", "dst-name"]}
                ]
            }
        """
        logger.info(f"Analyzing schemas in {self.schema_dir}")
        
        # Only analyze CMDB endpoints (monitor/log don't have relationships yet)
        cmdb_dir = self.schema_dir / 'cmdb'
        if not cmdb_dir.exists():
            logger.warning(f"CMDB directory not found: {cmdb_dir}")
            return {}
        
        # Find all schema files
        schema_files = list(cmdb_dir.glob('*.json'))
        logger.info(f"Found {len(schema_files)} CMDB schemas to analyze")
        
        # Build reverse dependency map
        for schema_file in schema_files:
            self._process_schema_file(schema_file)
        
        logger.info(f"Built reverse dependencies for {len(self.reverse_dependencies)} endpoints")
        return dict(self.reverse_dependencies)
    
    def _process_schema_file(self, schema_file: Path) -> None:
        """
        Process a single schema file to extract dependencies.
        
        Args:
            schema_file: Path to schema JSON file
        """
        try:
            with open(schema_file) as f:
                schema = json.load(f)
        except Exception as e:
            logger.warning(f"Failed to load schema {schema_file}: {e}")
            return
        
        # Get the endpoint path for this schema
        source_endpoint = schema.get('full_path')
        if not source_endpoint:
            return
        
        # Get relationships from schema
        relationships = schema.get('relationships', {})
        if not isinstance(relationships, dict):
            return
        
        # Process datasources to get field-level mappings
        datasources = relationships.get('datasources', {})
        if not isinstance(datasources, dict):
            return
        
        # Build field mapping per target endpoint
        endpoint_fields: dict[str, list[str]] = defaultdict(list)
        
        for field_name, ds_list in datasources.items():
            if not isinstance(ds_list, list):
                continue
            
            for ds in ds_list:
                if not isinstance(ds, dict):
                    continue
                
                target_endpoint = ds.get('endpoint')
                if target_endpoint:
                    endpoint_fields[target_endpoint].append(field_name)
        
        # Add to reverse dependency map
        for target_endpoint, fields in endpoint_fields.items():
            self.reverse_dependencies[target_endpoint].append({
                'endpoint': source_endpoint,
                'fields': sorted(set(fields))  # Remove duplicates
            })
    
    def get_reverse_deps(self, endpoint: str) -> list[dict[str, Any]]:
        """
        Get reverse dependencies for a specific endpoint.
        
        Args:
            endpoint: Endpoint path (e.g., 'firewall/address')
            
        Returns:
            List of endpoints that reference this one, with fields
        """
        return self.reverse_dependencies.get(endpoint, [])
    
    def export_to_json(self, output_path: Path) -> None:
        """
        Export reverse dependency map to JSON file.
        
        Args:
            output_path: Path to output JSON file
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(dict(self.reverse_dependencies), f, indent=2)
        
        logger.info(f"Exported reverse dependencies to {output_path}")
    
    def print_summary(self, top_n: int = 20) -> None:
        """
        Print summary of most referenced endpoints.
        
        Args:
            top_n: Number of top endpoints to show
        """
        print("\n" + "=" * 80)
        print("REVERSE DEPENDENCY ANALYSIS")
        print("=" * 80)
        
        # Sort by number of references
        sorted_endpoints = sorted(
            self.reverse_dependencies.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )
        
        print(f"\nTop {top_n} Most Referenced Endpoints:")
        print("-" * 80)
        
        for i, (endpoint, refs) in enumerate(sorted_endpoints[:top_n], 1):
            ref_count = len(refs)
            print(f"{i:2}. {endpoint:<50} ({ref_count} references)")
            
            # Show first few references
            if i <= 5:
                for ref in refs[:3]:
                    referencing_endpoint = ref.get('endpoint', 'unknown')
                    fields = ref.get('fields', [])
                    fields_str = ', '.join(fields[:2])
                    if len(fields) > 2:
                        fields_str += f', +{len(fields) - 2} more'
                    print(f"     ← {referencing_endpoint} (via: {fields_str})")
                
                if len(refs) > 3:
                    print(f"     ... and {len(refs) - 3} more")
        
        print(f"\nTotal endpoints with reverse dependencies: {len(self.reverse_dependencies)}")


def main():
    """Test the analyzer."""
    import sys
    from pathlib import Path
    
    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    # Find schema directory
    script_dir = Path(__file__).parent
    schema_dir = script_dir.parent.parent.parent / 'schema' / '7.6.5'
    
    if not schema_dir.exists():
        print(f"Schema directory not found: {schema_dir}")
        sys.exit(1)
    
    # Analyze
    analyzer = RelationshipAnalyzer(schema_dir)
    reverse_deps = analyzer.analyze_all_schemas()
    
    # Print summary
    analyzer.print_summary(top_n=25)
    
    # Test specific endpoint
    print("\n" + "=" * 80)
    print("EXAMPLE: firewall/address reverse dependencies")
    print("=" * 80)
    
    addr_deps = analyzer.get_reverse_deps('firewall/address')
    print(f"\nfirewall/address is referenced by {len(addr_deps)} endpoints:\n")
    
    for dep in addr_deps[:10]:
        endpoint = dep.get('endpoint', 'unknown')
        fields = dep.get('fields', [])
        print(f"  - {endpoint}")
        print(f"    Fields: {', '.join(fields)}")
    
    if len(addr_deps) > 10:
        print(f"\n  ... and {len(addr_deps) - 10} more")
    
    # Export
    output_path = script_dir / 'reverse_dependencies.json'
    analyzer.export_to_json(output_path)


if __name__ == '__main__':
    main()
