#!/usr/bin/env python3
"""
Test Helper Integration - Validate Template Changes

This script tests that the updated templates correctly use helper functions
from the central _helpers module.
"""

import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent))

from schema_parser import EndpointSchema, FieldMetadata


def test_endpoint_template():
    """Test endpoint class template uses helpers."""
    print("🧪 Testing endpoint_class.py.j2 template...")
    
    # Setup Jinja2
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    
    # Add filters
    env.filters["kebab_to_snake"] = lambda x: x.replace("-", "_").replace("/", "_")
    env.filters["to_python_type"] = lambda x: "str"
    env.filters["api_path_fix"] = lambda x: x  # Identity function for test
    
    # Load template
    template = env.get_template("endpoint_class.py.j2")
    
    # Create mock schema
    schema = EndpointSchema(
        category="cmdb",
        path="firewall/address",
        api_path="firewall/address",
        name="address",
        full_path="firewall.address",
        mkey="name",
        mkey_type="string",
        help="Address configuration",
        fields={
            "name": FieldMetadata(
                name="name",
                type="string",
                required=True,
                help="Address name",
                is_list=False,
                options=None,
                default=None,
            ),
            "subnet": FieldMetadata(
                name="subnet",
                type="string",
                required=False,
                help="IP subnet",
                is_list=False,
                options=None,
                default=None,
            ),
        },
    )
    
    # Render template
    rendered = template.render(schema=schema)
    
    # Validate imports
    assert "from hfortix_fortios._helpers import" in rendered, "❌ Missing _helpers import"
    assert "build_cmdb_payload" in rendered, "❌ Missing build_cmdb_payload import"
    assert "is_success" in rendered, "❌ Missing is_success import"
    
    # Validate PUT method uses build_cmdb_payload
    assert "data = build_cmdb_payload(" in rendered, "❌ PUT doesn't use build_cmdb_payload()"
    
    # Validate POST method uses build_cmdb_payload
    post_section = rendered.split("def post(")[1].split("def delete(")[0]
    assert "data = build_cmdb_payload(" in post_section, "❌ POST doesn't use build_cmdb_payload()"
    
    # Validate exists() uses is_success
    exists_section = rendered.split("def exists(")[1].split("def set(")[0]
    assert "is_success(response)" in exists_section, "❌ exists() doesn't use is_success()"
    
    print("✅ Endpoint template validation passed!")
    print("   ✓ Imports _helpers module")
    print("   ✓ PUT uses build_cmdb_payload()")
    print("   ✓ POST uses build_cmdb_payload()")
    print("   ✓ exists() uses is_success()")


def test_validator_template():
    """Test validator template has helper imports."""
    print("\n🧪 Testing validator.py.j2 template...")
    
    # Setup Jinja2
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    
    # Add filters
    env.filters["kebab_to_snake"] = lambda x: x.replace("-", "_").replace("/", "_")
    
    # Load template
    template = env.get_template("validator.py.j2")
    
    # Create mock schema
    schema = EndpointSchema(
        category="cmdb",
        path="firewall/address",
        api_path="firewall/address",
        name="address",
        full_path="firewall.address",
        mkey="name",
        mkey_type="string",
        help="Address configuration",
        fields={},
    )
    
    # Render template
    context = {
        "schema": schema,
        "required_fields": [],
        "fields_with_defaults": {},
        "enum_constants": [],
        "deprecated_fields": {},  # Add deprecated_fields context
        "all_fields": [],
    }
    rendered = template.render(**context)
    
    # Validate imports
    assert "from hfortix_fortios._helpers import" in rendered, "❌ Missing _helpers import"
    assert "validate_enable_disable" in rendered, "❌ Missing validate_enable_disable"
    assert "validate_integer_range" in rendered, "❌ Missing validate_integer_range"
    assert "validate_string_length" in rendered, "❌ Missing validate_string_length"
    assert "validate_ip_address" in rendered, "❌ Missing validate_ip_address"
    
    print("✅ Validator template validation passed!")
    print("   ✓ Imports _helpers module")
    print("   ✓ Imports common validators")

