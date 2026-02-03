#!/usr/bin/env python3
"""
Test the generator with existing schema files (no FortiGate required).
"""

import json
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent))

from schema_parser import SchemaParser
from generators.endpoint_generator import EndpointGenerator
from generators.validator_generator import ValidatorGenerator


def test_firewall_policy():
    """Test generating firewall policy endpoint."""
    
    print("🧪 Testing Generator with firewall policy schema\n")
    
    # Paths - use actual schema from v7.6
    schema_file = Path(__file__).parent.parent / "schemas/v7.6/cmdb/firewall/policy.json"
    template_dir = Path(__file__).parent / "templates"
    output_dir = Path(__file__).parent / "test_output"
    
    # Ensure output dir exists
    output_dir.mkdir(exist_ok=True)
    
    print(f"📂 Schema file: {schema_file}")
    print(f"📂 Template dir: {template_dir}")
    print(f"📂 Output dir: {output_dir}\n")
    
    # Load schema
    print("📖 Loading schema...")
    with open(schema_file) as f:
        schema_json = json.load(f)
    
    # Schema structure has results.children, not top-level children
    num_fields = len(schema_json.get('results', {}).get('children', {}))
    print(f"   Found {num_fields} fields\n")
    
    # Parse schema
    print("🔍 Parsing schema...")
    schema = SchemaParser.parse(schema_json, str(schema_file))
    
    print(f"   Category: {schema.category}")
    print(f"   Path: {schema.path}")
    print(f"   Name: {schema.name}")
    print(f"   Class name: {schema.class_name}")
    print(f"   Mkey: {schema.mkey} ({schema.mkey_type})")
    print(f"   Fields: {len(schema.fields)}")
    print(f"   Required fields: {len(schema.required_fields)}")
    print(f"   Fields with defaults: {len(schema.defaults)}\n")
    
    # Show some field details
    print("📋 Sample fields:")
    for i, (name, field) in enumerate(list(schema.fields.items())[:5]):
        print(f"   - {name}: {field.type} {'(required)' if field.required else ''}")
        if field.options:
            print(f"     Options: {', '.join(field.options[:3])}{'...' if len(field.options) > 3 else ''}")
    print()
    
    # Generate endpoint
    print("✨ Generating endpoint class...")
    endpoint_gen = EndpointGenerator(template_dir)
    endpoint_file = endpoint_gen.generate(schema, output_dir)
    print(f"   ✅ {endpoint_file}")
    print(f"   📏 {endpoint_file.stat().st_size:,} bytes\n")
    
    # Generate validator
    print("✨ Generating validator...")
    validator_gen = ValidatorGenerator(template_dir)
    validator_file = validator_gen.generate(schema, output_dir)
    print(f"   ✅ {validator_file}")
    print(f"   📏 {validator_file.stat().st_size:,} bytes\n")
    
    # Show generated file structure
    print("📁 Generated file structure:")
    for path in sorted(output_dir.rglob("*.py")):
        rel_path = path.relative_to(output_dir)
        print(f"   {rel_path}")
    print()
    
    # Read and show sample of generated code
    print("📄 Sample of generated endpoint class:")
    print("-" * 60)
    with open(endpoint_file) as f:
        lines = f.readlines()
        for line in lines[:30]:
            print(line.rstrip())
    print("   ...")
    print("-" * 60)
    print()
    
    print("✅ Test complete!")
    print(f"\n💡 Check generated files in: {output_dir}")


if __name__ == "__main__":
    test_firewall_policy()
