#!/usr/bin/env python3
"""
Analyze schema files to automatically detect which fields need normalization.

This script scans all schema files and identifies:
1. Simple array fields (type='array') that should use normalize_to_string_list
2. Table/complex fields that contain a single 'name' subfield (should use normalize_to_name_list)
3. Multi-value option fields that are lists

The goal is to build intelligent, schema-driven normalization instead of hardcoded lists.
"""

import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, Set, Any


def analyze_field_normalization(schema_dir: Path) -> Dict[str, Any]:
    """
    Analyze all schema files to detect normalization patterns.
    
    Returns:
        Dictionary with:
        - simple_array_fields: Set of field names with type='array'
        - name_list_fields: Set of field names that are tables/complex with only 'name' subfield
        - multi_value_option_fields: Set of fields with options and is_list=True
        - field_examples: Dict mapping field_name to example schemas
    """
    simple_array_fields = set()
    name_list_fields = set()
    multi_value_option_fields = set()
    
    # Track examples for documentation
    field_examples = defaultdict(list)
    
    # Field type distribution
    field_type_stats = defaultdict(int)
    
    # Scan all schema files
    schema_files = list(schema_dir.rglob("*.json"))
    print(f"📊 Analyzing {len(schema_files)} schema files...\n")
    
    for schema_file in schema_files:
        try:
            with open(schema_file, 'r') as f:
                schema = json.load(f)
            
            # Check request_fields (for POST/PUT)
            if 'request_fields' in schema:
                for field_name, field_def in schema['request_fields'].items():
                    analyze_field(
                        field_name,
                        field_def,
                        schema,
                        simple_array_fields,
                        name_list_fields,
                        multi_value_option_fields,
                        field_examples,
                        field_type_stats
                    )
            
            # Check schema_fields (for GET responses)
            if 'schema_fields' in schema:
                for field_name, field_def in schema['schema_fields'].items():
                    analyze_field(
                        field_name,
                        field_def,
                        schema,
                        simple_array_fields,
                        name_list_fields,
                        multi_value_option_fields,
                        field_examples,
                        field_type_stats
                    )
                        
        except Exception as e:
            print(f"⚠️  Error processing {schema_file}: {e}")
    
    return {
        'simple_array_fields': simple_array_fields,
        'name_list_fields': name_list_fields,
        'multi_value_option_fields': multi_value_option_fields,
        'field_examples': dict(field_examples),
        'field_type_stats': dict(field_type_stats),
    }


def analyze_field(
    field_name: str,
    field_def: Dict[str, Any],
    schema: Dict[str, Any],
    simple_array_fields: Set[str],
    name_list_fields: Set[str],
    multi_value_option_fields: Set[str],
    field_examples: Dict[str, list],
    field_type_stats: Dict[str, int]
):
    """Analyze a single field and categorize it."""
    field_type = field_def.get('type', 'unknown')
    category = field_def.get('category', 'unknown')
    is_list = field_def.get('is_list', False)
    options = field_def.get('options', [])
    children = field_def.get('children', {})
    
    # Track stats
    field_type_stats[field_type] += 1
    
    # 1. Simple array fields (type='array')
    if field_type == 'array':
        simple_array_fields.add(field_name)
        if len(field_examples[field_name]) < 3:
            field_examples[field_name].append({
                'endpoint': schema.get('full_path', 'unknown'),
                'api_type': schema.get('api_type', 'unknown'),
                'summary': field_def.get('summary', ''),
                'type': field_type,
                'python_type': field_def.get('python_type', 'unknown'),
            })
    
    # 2. Table/complex fields with only 'name' subfield
    # These typically need [{'name': '...'}, ...] format
    elif category in ['table', 'complex'] and children:
        # Check if it only has 'name' field (or name + optional fields)
        has_name = 'name' in children
        total_fields = len(children)
        
        # If it has 'name' and only a few other optional fields, it's likely a name-list
        if has_name and total_fields <= 3:
            name_list_fields.add(field_name)
            if len(field_examples[field_name]) < 3:
                field_examples[field_name].append({
                    'endpoint': schema.get('full_path', 'unknown'),
                    'api_type': schema.get('api_type', 'unknown'),
                    'summary': field_def.get('summary', ''),
                    'category': category,
                    'children': list(children.keys()),
                })
    
    # 3. Multi-value option fields (e.g., day names)
    # These return space-separated strings but accept lists
    elif options and is_list:
        multi_value_option_fields.add(field_name)
        if len(field_examples[field_name]) < 3:
            field_examples[field_name].append({
                'endpoint': schema.get('full_path', 'unknown'),
                'api_type': schema.get('api_type', 'unknown'),
                'summary': field_def.get('summary', ''),
                'options': options[:5],  # First 5 options
                'is_list': is_list,
            })


def print_results(results: Dict[str, Any]):
    """Print analysis results in a readable format."""
    print("\n" + "="*80)
    print("SCHEMA-DRIVEN NORMALIZATION ANALYSIS")
    print("="*80 + "\n")
    
    # Simple array fields
    print(f"📋 SIMPLE ARRAY FIELDS (type='array'): {len(results['simple_array_fields'])}")
    print("-" * 80)
    for field_name in sorted(results['simple_array_fields']):
        examples = results['field_examples'].get(field_name, [])
        print(f"\n  {field_name}:")
        for ex in examples[:2]:  # Show first 2 examples
            print(f"    - {ex['api_type']}/{ex['endpoint']}")
            if ex.get('summary'):
                print(f"      {ex['summary']}")
    
    print("\n")
    print(f"📋 NAME-LIST FIELDS (table/complex with 'name' child): {len(results['name_list_fields'])}")
    print("-" * 80)
    for field_name in sorted(results['name_list_fields']):
        examples = results['field_examples'].get(field_name, [])
        print(f"\n  {field_name}:")
        for ex in examples[:2]:
            print(f"    - {ex['api_type']}/{ex['endpoint']}")
            print(f"      Children: {ex.get('children', [])}")
    
    print("\n")
    print(f"📋 MULTI-VALUE OPTION FIELDS: {len(results['multi_value_option_fields'])}")
    print("-" * 80)
    for field_name in sorted(results['multi_value_option_fields']):
        examples = results['field_examples'].get(field_name, [])
        print(f"\n  {field_name}:")
        for ex in examples[:2]:
            print(f"    - {ex['api_type']}/{ex['endpoint']}")
            print(f"      Options: {ex.get('options', [])}")
    
    print("\n")
    print("📊 FIELD TYPE STATISTICS:")
    print("-" * 80)
    for field_type, count in sorted(results['field_type_stats'].items(), key=lambda x: -x[1]):
        print(f"  {field_type:20s}: {count:6d}")
    
    print("\n")


def generate_python_code(results: Dict[str, Any]) -> str:
    """Generate Python code for the normalization constants."""
    code = '''"""
Auto-generated normalization field sets from schema analysis.

Generated by: .dev/scripts/analyze_normalizable_fields.py
"""

# Simple array fields that use plain list format (not [{'name': '...'}])
# These should use normalize_to_string_list()
SIMPLE_ARRAY_FIELDS = {
'''
    
    for field_name in sorted(results['simple_array_fields']):
        code += f'    "{field_name}",\n'
    
    code += '''}\n
# Table/complex fields with 'name' child that use [{'name': '...'}, ...] format
# These should use normalize_to_name_list()
NAME_LIST_FIELDS = {
'''
    
    for field_name in sorted(results['name_list_fields']):
        code += f'    "{field_name}",\n'
    
    code += '''}\n
# Multi-value option fields (space-separated strings)
# These should use normalize_day_field() or similar
MULTI_VALUE_OPTION_FIELDS = {
'''
    
    for field_name in sorted(results['multi_value_option_fields']):
        code += f'    "{field_name}",\n'
    
    code += '}\n'
    
    return code


def main():
    """Main entry point."""
    # Find schema directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    
    # Analyze both schema versions
    for version in ['7.4.8', '7.6.5']:
        schema_dir = repo_root / 'schema' / version
        
        if not schema_dir.exists():
            print(f"⚠️  Schema directory not found: {schema_dir}")
            continue
        
        print(f"\n{'='*80}")
        print(f"ANALYZING SCHEMA VERSION: {version}")
        print(f"{'='*80}\n")
        
        results = analyze_field_normalization(schema_dir)
        print_results(results)
        
        # Generate Python code
        output_file = repo_root / f'packages/fortios/hfortix_fortios/_helpers/schema_normalizable_fields_{version.replace(".", "_")}.py'
        python_code = generate_python_code(results)
        
        # Write to file
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(python_code)
        
        print(f"\n✅ Generated: {output_file.relative_to(repo_root)}")
        print(f"   - {len(results['simple_array_fields'])} simple array fields")
        print(f"   - {len(results['name_list_fields'])} name-list fields")
        print(f"   - {len(results['multi_value_option_fields'])} multi-value option fields")


if __name__ == '__main__':
    main()
