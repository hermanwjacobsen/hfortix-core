#!/usr/bin/env python3
"""
Scan all schema files to find fields where the API expects underscores (not hyphens).

This script identifies fields where:
- The original API field name contains underscores
- The python_name also contains underscores
- These fields should NOT be converted from snake_case to kebab-case

Output is grouped by API type (cmdb, monitor, log, service) to populate
the *_BODY_FIELD_NO_HYPHEN sets in field_overrides.py

This script can be run standalone or integrated into the code generator.
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, Set

def scan_schema_file(schema_path: Path, api_type: str) -> dict[str, set[str]]:
    """
    Scan a single schema file for fields with underscores.
    
    Returns dict with keys: 'request_fields', 'response_fields', 'fields'
    """
    result = {
        'request_fields': set(),
        'response_fields': set(),
        'fields': set()  # CMDB body fields
    }
    
    try:
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        
        # Check request_fields (Monitor/Service endpoints - POST/PUT bodies)
        if 'request_fields' in schema:
            for field_name, field_info in schema['request_fields'].items():
                if '_' in field_name:  # Has underscore in API name
                    result['request_fields'].add(field_name)
        
        # Check response_fields (Monitor/Service endpoints - GET responses)
        if 'response_fields' in schema:
            for field_name, field_info in schema['response_fields'].items():
                if '_' in field_name:  # Has underscore in API name
                    result['response_fields'].add(field_name)
        
        # Check fields (CMDB endpoints - body fields)
        if 'fields' in schema:
            for field_key, field_info in schema['fields'].items():
                api_name = field_info.get('name', field_key)
                if '_' in api_name:  # Has underscore in API name
                    python_name = field_info.get('python_name', api_name)
                    result['fields'].add(python_name)
    
    except Exception as e:
        print(f"Error reading {schema_path}: {e}")
    
    return result

def main():
    """Scan all schemas and generate field override lists."""
    schema_base = Path(__file__).parent.parent / 'schema' / '7.6.5'
    
    # Results grouped by API type
    api_types = {
        'cmdb': {'request_fields': set(), 'response_fields': set(), 'fields': set()},
        'monitor': {'request_fields': set(), 'response_fields': set(), 'fields': set()},
        'log': {'request_fields': set(), 'response_fields': set(), 'fields': set()},
        'service': {'request_fields': set(), 'response_fields': set(), 'fields': set()},
    }
    
    # Scan each API type directory
    for api_type in ['cmdb', 'monitor', 'log', 'service']:
        api_dir = schema_base / api_type
        if not api_dir.exists():
            continue
        
        # Scan all JSON files
        for schema_file in api_dir.glob('**/*.json'):
            if schema_file.name == 'index.json':
                continue
            
            file_results = scan_schema_file(schema_file, api_type)
            
            # Merge results
            api_types[api_type]['request_fields'].update(file_results['request_fields'])
            api_types[api_type]['response_fields'].update(file_results['response_fields'])
            api_types[api_type]['fields'].update(file_results['fields'])
    
    # Print results in format ready for field_overrides.py
    print("=" * 80)
    print("FIELDS WITH UNDERSCORES IN API (DO NOT CONVERT TO HYPHENS)")
    print("=" * 80)
    print()
    
    for api_type in ['cmdb', 'monitor', 'log', 'service']:
        data = api_types[api_type]
        
        # For CMDB, we care about body fields
        if api_type == 'cmdb' and data['fields']:
            print(f"# {api_type.upper()} body fields that must preserve underscores")
            print(f"# Auto-generated from schema analysis - {len(data['fields'])} fields")
            print(f"{api_type.upper()}_BODY_FIELD_NO_HYPHEN = {{")
            for field in sorted(data['fields']):
                print(f'    "{field}",')
            print("}")
            print()
        
        # For Monitor/Log/Service, we care about request fields (POST/PUT bodies)
        if api_type in ['monitor', 'log', 'service'] and data['request_fields']:
            print(f"# {api_type.upper()} body fields that must preserve underscores")
            print(f"# Auto-generated from schema analysis - {len(data['request_fields'])} fields")
            print(f"{api_type.upper()}_BODY_FIELD_NO_HYPHEN = {{")
            for field in sorted(data['request_fields']):
                print(f'    "{field}",')
            print("}")
            print()
    
    # Summary statistics
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    for api_type in ['cmdb', 'monitor', 'log', 'service']:
        data = api_types[api_type]
        print(f"{api_type.upper()}:")
        print(f"  Body fields with underscores: {len(data['fields'])} (CMDB)")
        print(f"  Request fields with underscores: {len(data['request_fields'])} (Monitor/Service)")
        print(f"  Response fields with underscores: {len(data['response_fields'])} (info only)")
        print()
    
    return api_types


def update_field_overrides_file(api_types: Dict[str, Dict[str, Set[str]]], 
                                 field_overrides_path: Path | None = None) -> bool:
    """
    Update the field_overrides.py file with scanned results.
    
    Args:
        api_types: Dictionary with scanned field data
        field_overrides_path: Path to field_overrides.py (auto-detected if None)
    
    Returns:
        True if file was updated successfully
    """
    if field_overrides_path is None:
        # Auto-detect path
        field_overrides_path = (
            Path(__file__).parent.parent / 
            'packages' / 'fortios' / 'hfortix_fortios' / '_helpers' / 'field_overrides.py'
        )
    
    if not field_overrides_path.exists():
        print(f"Error: field_overrides.py not found at {field_overrides_path}")
        return False
    
    # Read current file
    with open(field_overrides_path, 'r') as f:
        content = f.read()
    
    # Update each BODY_FIELD_NO_HYPHEN set
    for api_type in ['cmdb', 'monitor', 'log', 'service']:
        data = api_types[api_type]
        
        # Determine which field set to use
        if api_type == 'cmdb':
            fields = data['fields']
        else:
            fields = data['request_fields']
        
        if not fields:
            continue
        
        var_name = f"{api_type.upper()}_BODY_FIELD_NO_HYPHEN"
        
        # Generate new set definition
        new_set = f"{var_name} = {{\n"
        for field in sorted(fields):
            new_set += f'    "{field}",\n'
        new_set += "}"
        
        # Find and replace the existing set using regex
        pattern = rf'{var_name}\s*=\s*\{{[^}}]*\}}'
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, new_set, content, flags=re.DOTALL)
            print(f"✓ Updated {var_name} with {len(fields)} fields")
        else:
            print(f"⚠ Warning: Could not find {var_name} in file")
    
    # Write updated content
    with open(field_overrides_path, 'w') as f:
        f.write(content)
    
    print(f"\n✅ Successfully updated {field_overrides_path}")
    return True


if __name__ == '__main__':
    import sys
    
    # Run scanner
    api_types = main()
    
    # Ask user if they want to update the file
    if len(sys.argv) > 1 and sys.argv[1] == '--update':
        print("\n" + "=" * 80)
        print("UPDATING field_overrides.py")
        print("=" * 80)
        update_field_overrides_file(api_types)
    else:
        print("\nTo automatically update field_overrides.py, run:")
        print("  python3 scripts/scan_underscore_fields.py --update")
