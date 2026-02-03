#!/usr/bin/env python3
"""
Bulk Test Generator for FortiOS API Endpoints

Generates pytest tests for all schemas that already exist in .dev/schemas/

Usage:
    python bulk_generate_tests.py                    # Generate all tests
    python bulk_generate_tests.py --category cmdb    # Only CMDB tests
    python bulk_generate_tests.py --from-file .dev/endpoints_cmdb.txt  # From file
"""

import argparse
import json
import sys
import time
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from schema_parser import SchemaParser
from generate_tests import TestGenerator


def find_schema_files(schema_dir: Path, category: str = None) -> list[Path]:
    """Find all schema JSON files."""
    if category:
        search_path = schema_dir / category
    else:
        search_path = schema_dir
    
    return list(search_path.rglob("*.json"))


def main():
    parser = argparse.ArgumentParser(
        description="Bulk generate pytest tests from existing schemas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all tests
  python bulk_generate_tests.py
  
  # Only CMDB tests
  python bulk_generate_tests.py --category cmdb
  
  # From endpoint list file
  python bulk_generate_tests.py --from-file .dev/endpoints_cmdb.txt
        """
    )
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--category",
        help="Only generate tests for this category (cmdb, monitor, log, service)"
    )
    group.add_argument(
        "--from-file",
        type=Path,
        help="Generate from endpoint list file (.txt)"
    )
    
    parser.add_argument(
        "--schema-dir",
        type=Path,
        default=Path(__file__).parent.parent / "schemas",
        help="Directory containing schemas (default: .dev/schemas)"
    )
    
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent.parent.parent / "packages" / "fortios",
        help="Base output directory (default: packages/fortios)"
    )
    
    args = parser.parse_args()
    
    # Paths
    schema_dir = args.schema_dir
    output_dir = args.output_dir
    template_dir = Path(__file__).parent.parent / "templates"  # .dev/generator/templates
    
    if not schema_dir.exists():
        print(f"❌ Schema directory not found: {schema_dir}")
        print("   Run download_schemas.py first to generate schemas")
        sys.exit(1)
    
    # Gather schema files
    schema_files = []
    
    if args.from_file:
        # Load endpoints from file - but just find all schemas instead
        print(f"📋 Generating from: {args.from_file}")
        print(f"🔍 Finding all schemas in: {schema_dir}\n")
        schema_files = find_schema_files(schema_dir, args.category)
    else:
        # Find all schemas
        print(f"🔍 Finding schema files in: {schema_dir}")
        schema_files = find_schema_files(schema_dir, args.category)
        print(f"   Found {len(schema_files)} schemas\n")
    
    if not schema_files:
        print("❌ No schema files found")
        sys.exit(1)
    
    print(f"🧪 Generating tests for {len(schema_files)} endpoints...\n")
    
    # Initialize test generator
    test_gen = TestGenerator(template_dir)
    
    # Generate tests
    generated = []
    failed = []
    
    for i, schema_file in enumerate(schema_files, 1):
        try:
            # Parse schema
            schema_dict = json.loads(schema_file.read_text())
            schema = SchemaParser.parse(schema_dict, str(schema_file))
            
            # Generate test
            test_file = test_gen.generate(schema, output_dir)
            
            # Skip if no test generated (category-only endpoints)
            if test_file is None:
                continue
            
            print(f"  [{i:3}/{len(schema_files)}] ✅ {schema.category}.{schema.path}")
            print(f"           → {test_file.relative_to(output_dir)}")
            
            generated.append(test_file)
            
            # Small delay to be nice
            time.sleep(0.01)
            
        except Exception as e:
            print(f"  [{i:3}/{len(schema_files)}] ❌ {schema_file.name}: {e}")
            failed.append((schema_file, str(e)))
    
    # Summary
    print("\n" + "="*80)
    print(f"✅ Successfully generated: {len(generated)}/{len(schema_files)} tests")
    
    if failed:
        print(f"❌ Failed: {len(failed)} tests\n")
        print("Failed schemas:")
        for schema_file, error in failed[:10]:
            print(f"  - {schema_file.name}: {error}")
        if len(failed) > 10:
            print(f"  ... and {len(failed) - 10} more")
    
    print(f"\n📁 Tests generated in: {output_dir / '.tests'}")
    print(f"\n🧪 Run tests:")
    print(f"   cd {output_dir}")
    print(f"   pytest .tests/ -v")


if __name__ == "__main__":
    main()
