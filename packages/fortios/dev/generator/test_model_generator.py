#!/usr/bin/env python3
"""
Test Pydantic Model Generator

Quick test of the new model generator with firewall.policy schema.
"""

import sys
from pathlib import Path

# Add generator to path
sys.path.insert(0, str(Path(__file__).parent))

from generators.model_generator import ModelGenerator
from schema_management.schema_parser import SchemaParser
import json


def main():
    """Test model generation."""
    print("🧪 Testing Pydantic Model Generator\n")
    print("=" * 70)
    
    # Paths
    schema_file = Path("/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.policy.json")
    template_dir = Path(__file__).parent / "templates"
    output_dir = Path(__file__).parent / "test_output" / "models"
    
    # Load schema
    print(f"\n📖 Loading schema: {schema_file.name}")
    with open(schema_file) as f:
        schema_json = json.load(f)
    schema = SchemaParser.parse(schema_json, str(schema_file))
    print(f"   ✅ Loaded: {schema.class_name}")
    print(f"   📊 Fields: {len(schema.fields)}")
    if hasattr(schema, 'child_tables'):
        print(f"   📦 Child tables: {len(schema.child_tables) if schema.child_tables else 0}")
    
    # Initialize generator
    print(f"\n🏗️  Initializing model generator...")
    generator = ModelGenerator(template_dir)
    print("   ✅ Generator ready")
    
    # Generate model
    print(f"\n⚙️  Generating Pydantic model...")
    try:
        output_file = generator.generate(schema, output_dir)
        print(f"   ✅ Generated: {output_file}")
        print(f"   📏 Size: {output_file.stat().st_size:,} bytes")
        
        # Show first 50 lines
        print(f"\n📄 Preview (first 50 lines):")
        print("=" * 70)
        with open(output_file) as f:
            lines = f.readlines()
            for i, line in enumerate(lines[:50], 1):
                print(f"{i:3d} | {line}", end='')
        
        if len(lines) > 50:
            print(f"\n... ({len(lines) - 50} more lines)")
        
        print("=" * 70)
        print(f"\n✅ Success! Model generated at:")
        print(f"   {output_file}")
        
        # Try to import and validate
        print(f"\n🧪 Testing import...")
        spec = __import__('importlib.util').util.spec_from_file_location("test_model", output_file)
        if spec and spec.loader:
            module = __import__('importlib.util').util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            model_class = getattr(module, schema.pydantic_class_name)
            print(f"   ✅ Successfully imported {schema.pydantic_class_name}")
            print(f"   📋 Model fields: {len(model_class.model_fields)}")
            
            # Try creating an instance
            print(f"\n🧪 Testing model instantiation...")
            try:
                if schema.mkey:
                    instance = model_class(**{schema.mkey: 1, "name": "test-policy"})
                else:
                    instance = model_class(name="test-policy")
                print(f"   ✅ Created instance: {instance}")
            except Exception as e:
                print(f"   ⚠️  Could not create instance: {e}")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error generating model:")
        print(f"   {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
