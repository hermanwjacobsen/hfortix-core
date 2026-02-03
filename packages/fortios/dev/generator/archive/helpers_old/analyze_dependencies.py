#!/usr/bin/env python3
"""
Analyze endpoint dependencies from datasource fields.

Parses all schemas to build a dependency graph showing which endpoints
reference which other endpoints.
"""

import json
from pathlib import Path
from collections import defaultdict
from typing import Any


def extract_datasources(schema_data: dict[str, Any]) -> dict[str, list[str]]:
    """
    Extract datasource fields from schema.
    
    Args:
        schema_data: Parsed schema JSON
        
    Returns:
        Dict mapping field name to list of datasource endpoints
    """
    datasources = {}
    
    if 'results' in schema_data and 'children' in schema_data['results']:
        for field_name, field_data in schema_data['results']['children'].items():
            if 'datasource' in field_data:
                datasources[field_name] = field_data['datasource']
    
    return datasources


def parse_datasource_path(datasource: str) -> tuple[str, str] | None:
    """
    Parse datasource string to extract category and path.
    
    Args:
        datasource: e.g., 'firewall.address.name' or 'system.interface.name'
        
    Returns:
        Tuple of (category, path) or None if can't parse
        
    Examples:
        'firewall.address.name' -> ('firewall', 'address')
        'system.interface.name' -> ('system', 'interface')
        'firewall.schedule.onetime.name' -> ('firewall', 'schedule/onetime')
    """
    parts = datasource.split('.')
    if len(parts) < 2:
        return None
    
    # Last part is the field name (e.g., 'name', 'id')
    # Everything before that is the endpoint path
    category = parts[0]
    
    # Handle nested paths (e.g., firewall.schedule.onetime.name)
    if len(parts) > 2:
        path_parts = parts[1:-1]  # Exclude category and field name
        path = '/'.join(path_parts)
    else:
        path = parts[1].replace('-', '_')  # firewall.address.name -> address
    
    return (category, path)


def analyze_dependencies(schema_dir: Path) -> dict[str, dict]:
    """
    Analyze all schemas to build dependency graph.
    
    Args:
        schema_dir: Directory containing schema JSON files
        
    Returns:
        Dict with dependency information
    """
    dependencies = defaultdict(lambda: {
        'depends_on': set(),  # Endpoints this endpoint depends on
        'depended_by': set(),  # Endpoints that depend on this one
        'fields': defaultdict(list),  # Which fields reference which endpoints
    })
    
    # Find all schema files
    schema_files = list(schema_dir.rglob('*.json'))
    print(f"📊 Analyzing {len(schema_files)} schemas...")
    
    for schema_file in schema_files:
        # Parse endpoint path from file
        # e.g., .dev/schemas/v7.6/cmdb/firewall/policy.json -> cmdb/firewall/policy
        rel_path = schema_file.relative_to(schema_dir)
        parts = rel_path.parts
        
        if len(parts) < 2:
            continue
        
        category = parts[0]  # cmdb, monitor, etc.
        endpoint_parts = parts[1:]
        endpoint_path = '/'.join(p.replace('.json', '') for p in endpoint_parts)
        endpoint_full = f"{category}/{endpoint_path}"
        
        # Load schema
        try:
            with open(schema_file) as f:
                schema_data = json.load(f)
        except Exception as e:
            print(f"⚠️  Error loading {schema_file}: {e}")
            continue
        
        # Extract datasources
        datasources = extract_datasources(schema_data)
        
        if not datasources:
            continue
        
        # Process each datasource
        for field_name, ds_list in datasources.items():
            for datasource in ds_list:
                parsed = parse_datasource_path(datasource)
                if not parsed:
                    continue
                
                ds_category, ds_path = parsed
                referenced_endpoint = f"{ds_category}/{ds_path}"
                
                # Record dependency
                dependencies[endpoint_full]['depends_on'].add(referenced_endpoint)
                dependencies[endpoint_full]['fields'][referenced_endpoint].append(field_name)
                dependencies[referenced_endpoint]['depended_by'].add(endpoint_full)
    
    return dependencies


def print_dependency_report(dependencies: dict, top_n: int = 20):
    """Print dependency analysis report."""
    
    print("\n" + "=" * 80)
    print("DEPENDENCY ANALYSIS REPORT")
    print("=" * 80)
    
    # Most depended-on endpoints
    print(f"\n📌 Top {top_n} Most Referenced Endpoints:")
    print("-" * 80)
    
    sorted_by_refs = sorted(
        dependencies.items(),
        key=lambda x: len(x[1]['depended_by']),
        reverse=True
    )
    
    for i, (endpoint, data) in enumerate(sorted_by_refs[:top_n], 1):
        ref_count = len(data['depended_by'])
        if ref_count == 0:
            break
        print(f"{i:2}. {endpoint:<50} ({ref_count} references)")
        if i <= 5:  # Show details for top 5
            for dep in list(data['depended_by'])[:3]:
                print(f"     ← {dep}")
            if len(data['depended_by']) > 3:
                print(f"     ... and {len(data['depended_by']) - 3} more")
    
    # Most dependent endpoints
    print(f"\n🔗 Top {top_n} Endpoints with Most Dependencies:")
    print("-" * 80)
    
    sorted_by_deps = sorted(
        dependencies.items(),
        key=lambda x: len(x[1]['depends_on']),
        reverse=True
    )
    
    for i, (endpoint, data) in enumerate(sorted_by_deps[:top_n], 1):
        dep_count = len(data['depends_on'])
        if dep_count == 0:
            break
        print(f"{i:2}. {endpoint:<50} ({dep_count} dependencies)")
        if i <= 5:  # Show details for top 5
            for dep in list(data['depends_on'])[:3]:
                fields = data['fields'][dep]
                print(f"     → {dep} (via: {', '.join(fields[:2])})")
            if len(data['depends_on']) > 3:
                print(f"     ... and {len(data['depends_on']) - 3} more")
    
    # Statistics
    print("\n📈 Statistics:")
    print("-" * 80)
    
    endpoints_with_deps = sum(1 for d in dependencies.values() if d['depends_on'])
    endpoints_referenced = sum(1 for d in dependencies.values() if d['depended_by'])
    total_refs = sum(len(d['depended_by']) for d in dependencies.values())
    total_deps = sum(len(d['depends_on']) for d in dependencies.values())
    
    print(f"Total endpoints analyzed: {len(dependencies)}")
    print(f"Endpoints with dependencies: {endpoints_with_deps}")
    print(f"Endpoints being referenced: {endpoints_referenced}")
    print(f"Total dependency relationships: {total_deps}")
    print(f"Average dependencies per endpoint: {total_deps / max(endpoints_with_deps, 1):.1f}")


def export_dependency_graph(dependencies: dict, output_file: Path):
    """Export dependency graph as JSON."""
    
    # Convert sets to lists for JSON serialization
    export_data = {}
    for endpoint, data in dependencies.items():
        export_data[endpoint] = {
            'depends_on': sorted(list(data['depends_on'])),
            'depended_by': sorted(list(data['depended_by'])),
            'fields': {k: v for k, v in data['fields'].items()},
        }
    
    with open(output_file, 'w') as f:
        json.dump(export_data, f, indent=2)
    
    print(f"\n💾 Dependency graph exported to: {output_file}")


def main():
    """Main analysis function."""
    
    # Schema directory  
    schema_dir = Path(__file__).parent.parent.parent / '.dev/schemas/v7.6/cmdb'
    
    if not schema_dir.exists():
        print(f"❌ Schema directory not found: {schema_dir}")
        return
    
    # Analyze dependencies
    dependencies = analyze_dependencies(schema_dir)
    
    # Print report
    print_dependency_report(dependencies, top_n=25)
    
    # Export to JSON
    output_file = Path(__file__).parent.parent.parent / '.dev/dependency_graph.json'
    export_dependency_graph(dependencies, output_file)


if __name__ == '__main__':
    main()
