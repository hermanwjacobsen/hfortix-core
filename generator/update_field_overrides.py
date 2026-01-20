#!/usr/bin/env python3
"""
Generator Integration: Update field overrides from schemas

This script is designed to be called during the code generation process.
It scans all schema files and automatically updates the field_overrides.py
file with the correct lists of fields that must preserve underscores.

Usage:
    # Standalone
    python3 scripts/update_field_overrides.py
    
    # From generator (pseudo-code)
    from scripts.update_field_overrides import update_from_schemas
    update_from_schemas(schema_base_path='schema/7.6.5')

Integration Points:
    1. After schema files are downloaded/generated
    2. Before generating Python API code
    3. As part of the build/regeneration process

This ensures that field name conversion is always in sync with the schemas.
"""

from pathlib import Path
import sys

# Add parent to path to import the scanner
sys.path.insert(0, str(Path(__file__).parent))

from scan_underscore_fields import (
    scan_schema_file,
    update_field_overrides_file,
)


def update_from_schemas(schema_base_path: str | Path | None = None,
                       field_overrides_path: str | Path | None = None,
                       verbose: bool = True) -> bool:
    """
    Scan schemas and update field_overrides.py automatically.
    
    This is the main entry point for generator integration.
    
    Args:
        schema_base_path: Path to schema directory (e.g., 'schema/7.6.5')
                         If None, auto-detects from script location
        field_overrides_path: Path to field_overrides.py
                             If None, auto-detects from script location
        verbose: Print progress messages
    
    Returns:
        True if successful, False otherwise
    
    Example:
        # From generator code
        from scripts.update_field_overrides import update_from_schemas
        
        # Update before generating API code
        success = update_from_schemas(
            schema_base_path='schema/7.6.5',
            verbose=True
        )
        
        if success:
            # Continue with API code generation
            generate_api_code()
    """
    # Auto-detect paths if not provided
    if schema_base_path is None:
        schema_base_path = Path(__file__).parent.parent / 'schema' / '7.6.5'
    else:
        schema_base_path = Path(schema_base_path)
    
    if field_overrides_path is None:
        field_overrides_path = (
            Path(__file__).parent.parent / 
            'packages' / 'fortios' / 'hfortix_fortios' / '_helpers' / 'field_overrides.py'
        )
    else:
        field_overrides_path = Path(field_overrides_path)
    
    if verbose:
        print("=" * 80)
        print("UPDATING FIELD OVERRIDES FROM SCHEMAS")
        print("=" * 80)
        print(f"Schema path: {schema_base_path}")
        print(f"Target file: {field_overrides_path}")
        print()
    
    # Validate paths
    if not schema_base_path.exists():
        print(f"❌ Error: Schema directory not found: {schema_base_path}")
        return False
    
    if not field_overrides_path.exists():
        print(f"❌ Error: field_overrides.py not found: {field_overrides_path}")
        return False
    
    # Scan schemas
    api_types = {
        'cmdb': {'request_fields': set(), 'response_fields': set(), 'fields': set()},
        'monitor': {'request_fields': set(), 'response_fields': set(), 'fields': set()},
        'log': {'request_fields': set(), 'response_fields': set(), 'fields': set()},
        'service': {'request_fields': set(), 'response_fields': set(), 'fields': set()},
    }
    
    total_schemas = 0
    for api_type in ['cmdb', 'monitor', 'log', 'service']:
        api_dir = schema_base_path / api_type
        if not api_dir.exists():
            continue
        
        for schema_file in api_dir.glob('**/*.json'):
            if schema_file.name == 'index.json':
                continue
            
            file_results = scan_schema_file(schema_file, api_type)
            api_types[api_type]['request_fields'].update(file_results['request_fields'])
            api_types[api_type]['response_fields'].update(file_results['response_fields'])
            api_types[api_type]['fields'].update(file_results['fields'])
            total_schemas += 1
    
    if verbose:
        print(f"Scanned {total_schemas} schema files")
        print()
        print("Found fields with underscores:")
        for api_type in ['cmdb', 'monitor', 'log', 'service']:
            data = api_types[api_type]
            body_count = len(data['fields']) if api_type == 'cmdb' else len(data['request_fields'])
            if body_count > 0:
                print(f"  {api_type.upper()}: {body_count} body fields")
        print()
    
    # Update file
    success = update_field_overrides_file(api_types, field_overrides_path)
    
    if verbose and success:
        print()
        print("✅ Field overrides successfully updated!")
        print()
        print("Next steps:")
        print("  1. Review changes in field_overrides.py")
        print("  2. Run tests to verify: python3 test_underscore_preservation.py")
        print("  3. Commit the updated file")
    
    return success


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Update field_overrides.py from schema files'
    )
    parser.add_argument(
        '--schema-path',
        type=str,
        help='Path to schema directory (default: auto-detect)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Path to field_overrides.py (default: auto-detect)'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress progress messages'
    )
    
    args = parser.parse_args()
    
    success = update_from_schemas(
        schema_base_path=args.schema_path,
        field_overrides_path=args.output,
        verbose=not args.quiet
    )
    
    sys.exit(0 if success else 1)
