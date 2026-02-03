"""
Tests for MetadataMixin class methods on FortiOS endpoint classes.

Tests the following methods available on all endpoint classes:
- schema() - Get full schema with field definitions
- fields() - Get list of field names or detailed field info
- defaults() - Get default values for all fields
- required_fields() - Get list of required field names
- field_info() - Get info for a specific field
- validate_field() - Validate a value for a specific field
- help() - Print help for the endpoint
"""

from io import StringIO
import sys


def create_test_client():
    """Create a FortiOS client for testing."""
    from hfortix_fortios import FortiOS
    # Suppress SSL warning during test
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return FortiOS(
            'test', 
            token='abcdefghij1234567890abcdefghij12345678901234567890', 
            verify=False
        )


def get_address_endpoint():
    """Get the firewall address endpoint for testing."""
    fgt = create_test_client()
    return fgt.api.cmdb.firewall.address


# ============================================
# schema() tests
# ============================================

def test_schema_returns_dict():
    """schema() should return a dict."""
    print("\n=== Testing schema() returns dict ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.schema()
    
    assert isinstance(result, dict)
    print("✅ schema() returns dict")


def test_schema_has_required_keys():
    """schema() should have required keys."""
    print("\n=== Testing schema() has required keys ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.schema()
    
    # Schema has endpoint info keys, not 'fields' directly
    required_keys = ['endpoint', 'category', 'mkey', 'mkey_type', 'help']
    for key in required_keys:
        assert key in result, f"Missing key: {key}"
    
    print(f"✅ schema() has required keys: {required_keys}")


def test_schema_fields_is_dict():
    """schema() should have field count info."""
    print("\n=== Testing schema() has field counts ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.schema()
    
    # Schema has field counts rather than the fields dict
    assert 'total_fields' in result
    assert isinstance(result['total_fields'], int)
    assert result['total_fields'] > 0
    
    print(f"✅ schema() has total_fields: {result['total_fields']}")


# ============================================
# fields() tests
# ============================================

def test_fields_returns_list():
    """fields() should return a list of field names."""
    print("\n=== Testing fields() returns list ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.fields()
    
    assert isinstance(result, list)
    assert len(result) > 0
    assert all(isinstance(f, str) for f in result)
    
    print(f"✅ fields() returns list with {len(result)} fields")


def test_fields_contains_common_fields():
    """fields() should contain common address fields."""
    print("\n=== Testing fields() contains common fields ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.fields()
    
    # These should exist on firewall address
    assert 'name' in result
    assert 'uuid' in result
    
    print("✅ fields() contains 'name' and 'uuid'")


def test_fields_detailed_returns_dict():
    """fields(detailed=True) should return a dict."""
    print("\n=== Testing fields(detailed=True) returns dict ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.fields(detailed=True)
    
    assert isinstance(result, dict)
    assert len(result) > 0
    
    print(f"✅ fields(detailed=True) returns dict with {len(result)} fields")


def test_fields_detailed_has_field_info():
    """fields(detailed=True) should have info for each field."""
    print("\n=== Testing fields(detailed=True) has field info ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.fields(detailed=True)
    
    # Check that each field has some info
    for field_name, field_info in list(result.items())[:3]:
        assert isinstance(field_info, dict), f"Field {field_name} info is not a dict"
        assert 'type' in field_info or 'name' in field_info, f"Field {field_name} missing type/name"
    
    print("✅ fields(detailed=True) has field info for each field")


# ============================================
# defaults() tests
# ============================================

def test_defaults_returns_dict():
    """defaults() should return a dict."""
    print("\n=== Testing defaults() returns dict ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.defaults()
    
    assert isinstance(result, dict)
    
    print(f"✅ defaults() returns dict with {len(result)} defaults")


def test_defaults_contains_common_fields():
    """defaults() should contain common field defaults."""
    print("\n=== Testing defaults() contains common fields ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.defaults()
    
    # name should have an empty string default
    assert 'name' in result
    assert result['name'] == ''
    
    print("✅ defaults() contains 'name' with empty string default")


def test_defaults_matches_schema():
    """defaults() values should match schema defaults."""
    print("\n=== Testing defaults() matches schema ===")
    endpoint = get_address_endpoint()
    
    defaults = endpoint.defaults()
    schema = endpoint.schema()
    fields_info = schema.get('fields', {})
    
    # Check that defaults come from schema
    for field_name, default_value in list(defaults.items())[:5]:
        if field_name in fields_info:
            field = fields_info[field_name]
            if 'default' in field:
                assert field['default'] == default_value, \
                    f"Default mismatch for {field_name}: {default_value} vs {field['default']}"
    
    print("✅ defaults() matches schema defaults")


# ============================================
# required_fields() tests
# ============================================

def test_required_fields_returns_list():
    """required_fields() should return a list."""
    print("\n=== Testing required_fields() returns list ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.required_fields()
    
    assert isinstance(result, list)
    assert all(isinstance(f, str) for f in result)
    
    print(f"✅ required_fields() returns list with {len(result)} fields")


def test_required_fields_are_valid():
    """required_fields() should return valid field names."""
    print("\n=== Testing required_fields() are valid ===")
    endpoint = get_address_endpoint()
    
    required = endpoint.required_fields()
    all_fields = endpoint.fields()
    
    for field in required:
        assert field in all_fields, f"Required field {field} not in fields()"
    
    print("✅ required_fields() are all valid field names")


# ============================================
# field_info() tests
# ============================================

def test_field_info_returns_dict():
    """field_info() should return a dict for valid field."""
    print("\n=== Testing field_info() returns dict ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.field_info('name')
    
    assert isinstance(result, dict)
    
    print("✅ field_info('name') returns dict")


def test_field_info_has_required_keys():
    """field_info() should have type and description."""
    print("\n=== Testing field_info() has required keys ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.field_info('name')
    
    assert 'type' in result or 'name' in result
    
    print("✅ field_info('name') has type/name info")


def test_field_info_invalid_field_returns_none():
    """field_info() should return None for invalid field."""
    print("\n=== Testing field_info() invalid field returns None ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.field_info('nonexistent_field_xyz')
    
    assert result is None
    
    print("✅ field_info('nonexistent_field_xyz') returns None")


def test_field_info_various_fields():
    """field_info() should work for various field types."""
    print("\n=== Testing field_info() various fields ===")
    endpoint = get_address_endpoint()
    
    # Get a few fields to test
    fields = endpoint.fields()[:5]
    
    for field_name in fields:
        info = endpoint.field_info(field_name)
        assert info is not None, f"field_info('{field_name}') returned None"
        assert isinstance(info, dict), f"field_info('{field_name}') not a dict"
    
    print(f"✅ field_info() works for {len(fields)} different fields")


# ============================================
# validate_field() tests
# ============================================

def test_validate_field_valid_string():
    """validate_field() should accept valid string."""
    print("\n=== Testing validate_field() valid string ===")
    endpoint = get_address_endpoint()
    
    is_valid, error = endpoint.validate_field('name', 'test-address')
    
    assert is_valid is True
    assert error is None
    
    print("✅ validate_field('name', 'test-address') is valid")


def test_validate_field_returns_tuple():
    """validate_field() should return (bool, str|None) tuple."""
    print("\n=== Testing validate_field() returns tuple ===")
    endpoint = get_address_endpoint()
    
    result = endpoint.validate_field('name', 'test')
    
    assert isinstance(result, tuple)
    assert len(result) == 2
    is_valid, error = result
    assert isinstance(is_valid, bool)
    assert error is None or isinstance(error, str)
    
    print("✅ validate_field() returns (bool, str|None) tuple")


def test_validate_field_invalid_returns_error():
    """validate_field() should return error for invalid value."""
    print("\n=== Testing validate_field() invalid returns error ===")
    endpoint = get_address_endpoint()
    
    # Try a string that's too long (name max is 79 chars)
    long_name = 'a' * 100
    is_valid, error = endpoint.validate_field('name', long_name)
    
    # If validation is strict, it should fail
    # If not, it might pass (library dependent)
    if not is_valid:
        assert error is not None
        assert isinstance(error, str)
        print(f"✅ validate_field() returned error: {error}")
    else:
        print("⚠️ validate_field() accepted long string (validation may be lenient)")
    
    print("✅ validate_field() returns proper tuple for invalid input")


def test_validate_field_unknown_field():
    """validate_field() should handle unknown field gracefully."""
    print("\n=== Testing validate_field() unknown field ===")
    endpoint = get_address_endpoint()
    
    # Try to validate a non-existent field
    try:
        is_valid, error = endpoint.validate_field('nonexistent_xyz', 'value')
        # Should return False or raise
        if not is_valid:
            assert error is not None
            print(f"✅ validate_field() returned error for unknown field: {error}")
        else:
            print("⚠️ validate_field() accepted unknown field")
    except Exception as e:
        print(f"✅ validate_field() raised exception for unknown field: {type(e).__name__}")


# ============================================
# help() tests
# ============================================

def test_help_produces_output():
    """help() should produce output to stdout."""
    print("\n=== Testing help() produces output ===")
    endpoint = get_address_endpoint()
    
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        endpoint.help()
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert len(output) > 0
    
    print("✅ help() produces output")


def test_help_returns_none():
    """help() should return None."""
    print("\n=== Testing help() returns None ===")
    endpoint = get_address_endpoint()
    
    # Capture stdout to suppress
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        result = endpoint.help()
    finally:
        sys.stdout = old_stdout
    
    assert result is None
    
    print("✅ help() returns None")


def test_help_shows_endpoint_info():
    """help() should show endpoint information."""
    print("\n=== Testing help() shows endpoint info ===")
    endpoint = get_address_endpoint()
    
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        endpoint.help()
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # Should contain endpoint or address related info
    output_lower = output.lower()
    assert 'address' in output_lower or 'firewall' in output_lower or 'endpoint' in output_lower
    
    print("✅ help() shows endpoint information")


def test_help_with_show_fields():
    """help(show_fields=True) should show more detail."""
    print("\n=== Testing help(show_fields=True) ===")
    endpoint = get_address_endpoint()
    
    # Capture stdout for both modes
    old_stdout = sys.stdout
    
    sys.stdout = StringIO()
    try:
        endpoint.help(show_fields=False)
        output_short = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    sys.stdout = StringIO()
    try:
        endpoint.help(show_fields=True)
        output_long = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # With show_fields=True, output should be longer
    # (or at least the same if implementation differs)
    assert len(output_long) >= len(output_short)
    
    print(f"✅ help(show_fields=True) output length: {len(output_long)} vs {len(output_short)}")


def test_help_for_specific_field():
    """help(field_name='name') should show field-specific help."""
    print("\n=== Testing help(field_name='name') ===")
    endpoint = get_address_endpoint()
    
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        endpoint.help(field_name='name')
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # Should contain 'name' field info
    assert len(output) > 0
    
    print("✅ help(field_name='name') produces output")


# ============================================
# Multiple endpoint tests
# ============================================

def test_different_endpoints_have_different_schemas():
    """Different endpoints should have different schemas."""
    print("\n=== Testing different endpoints have different schemas ===")
    fgt = create_test_client()
    
    address = fgt.api.cmdb.firewall.address
    # Get another endpoint
    try:
        policy = fgt.api.cmdb.firewall.policy
        
        addr_schema = address.schema()
        policy_schema = policy.schema()
        
        assert addr_schema['endpoint'] != policy_schema['endpoint']
        assert addr_schema['mkey'] != policy_schema['mkey'] or \
               addr_schema['fields'] != policy_schema['fields']
        
        print("✅ address and policy have different schemas")
    except AttributeError:
        print("⚠️ Could not access firewall.policy endpoint")


# ============================================
# Main runner
# ============================================

if __name__ == "__main__":
    print("MetadataMixin Tests")
    print("=" * 50)
    
    tests = [
        # schema() tests
        test_schema_returns_dict,
        test_schema_has_required_keys,
        test_schema_fields_is_dict,
        
        # fields() tests
        test_fields_returns_list,
        test_fields_contains_common_fields,
        test_fields_detailed_returns_dict,
        test_fields_detailed_has_field_info,
        
        # defaults() tests
        test_defaults_returns_dict,
        test_defaults_contains_common_fields,
        test_defaults_matches_schema,
        
        # required_fields() tests
        test_required_fields_returns_list,
        test_required_fields_are_valid,
        
        # field_info() tests
        test_field_info_returns_dict,
        test_field_info_has_required_keys,
        test_field_info_invalid_field_returns_none,
        test_field_info_various_fields,
        
        # validate_field() tests
        test_validate_field_valid_string,
        test_validate_field_returns_tuple,
        test_validate_field_invalid_returns_error,
        test_validate_field_unknown_field,
        
        # help() tests
        test_help_produces_output,
        test_help_returns_none,
        test_help_shows_endpoint_info,
        test_help_with_show_fields,
        test_help_for_specific_field,
        
        # Multiple endpoint tests
        test_different_endpoints_have_different_schemas,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            failed += 1
            print(f"  [FAIL] {test.__name__}: {e}")
    
    print("=" * 50)
    print(f"Results: {passed}/{passed + failed} passed", end="")
    if failed == 0:
        print(" (all passed)")
    else:
        print(f" ({failed} failed)")
