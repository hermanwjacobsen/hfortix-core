#!/usr/bin/env python3
"""
Regenerate all pytest test files from schemas.

This script iterates through all schemas and regenerates their corresponding test files.
"""

import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from schema_management.schema_parser import SchemaParser
from helpers.generate_tests import TestGenerator


def main():
    """Regenerate all tests."""
    # Paths
    script_dir = Path(__file__).parent
    schema_base = script_dir.parent.parent / "schema" / "7.6.5"
    output_dir = script_dir.parent.parent
    template_dir = script_dir / "templates"
    
    print(f"📂 Schema directory: {schema_base}")
    print(f"📂 Output directory: {output_dir}")
    print(f"📂 Template directory: {template_dir}")
    print()
    
    # Initialize test generator
    test_gen = TestGenerator(template_dir)
    
    # Track statistics
    stats = {
        "generated": 0,
        "skipped": 0,
        "errors": 0,
    }
    
    # Iterate through all schema files
    for schema_file in sorted(schema_base.rglob("*.json")):
        # Skip index files
        if schema_file.name == "index.json":
            continue
        
        # Get category from path
        relative_path = schema_file.relative_to(schema_base)
        category = relative_path.parts[0]
        
        print(f"  Processing {category}/{schema_file.stem}...", end=" ")
        
        try:
            # Load schema
            schema_dict = json.loads(schema_file.read_text())
            
            # Parse schema
            schema = SchemaParser.parse(schema_dict, str(schema_file))
            
            # Generate test
            test_file = test_gen.generate(schema, output_dir)
            
            if test_file:
                stats["generated"] += 1
                print(f"✅ Generated {test_file.name}")
            else:
                stats["skipped"] += 1
                print("⏭️  Skipped")
                
        except Exception as e:
            stats["errors"] += 1
            print(f"❌ Error: {e}")
    
    # Print summary
    print()
    print("=" * 60)
    print("📊 Test Generation Summary")
    print("=" * 60)
    print(f"  ✅ Generated: {stats['generated']}")
    print(f"  ⏭️  Skipped:   {stats['skipped']}")
    print(f"  ❌ Errors:    {stats['errors']}")
    print(f"  📝 Total:     {stats['generated'] + stats['skipped'] + stats['errors']}")
    print("=" * 60)
    
    if stats["errors"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
