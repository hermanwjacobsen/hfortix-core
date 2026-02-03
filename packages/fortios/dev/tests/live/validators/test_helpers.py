"""
Tests for hfortix_fortios._helpers module functions.

This module tests:
- builders: build_cmdb_payload, build_api_payload, normalize_to_name_list
- converters: convert_boolean_to_str, filter_empty_values  
- normalizers: normalize_member_list, normalize_table_field
- response: is_success, get_results, get_name, get_mkey
- validation: validate_enum_field, validate_required_fields, validate_query_parameter

Run with: python -m pytest.validators.test_helpers
"""

import sys
from typing import Any, Type

import pytest


class TestResults:
    """Track test results."""
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []

    __test__ = False  # type: ignore[attr-defined]

    def add_pass(self, name: str):
        self.passed += 1
        print(f"  ✓ {name}")

    def add_fail(self, name: str, expected: Any, got: Any):
        self.failed += 1
        self.errors.append((name, expected, got))
        print(f"  ✗ {name}")
        print(f"    Expected: {expected!r}")
        print(f"    Got:      {got!r}")

    def add_error(self, name: str, error: Exception):
        self.failed += 1
        self.errors.append((name, "no error", str(error)))
        print(f"  ✗ {name}")
        print(f"    Error: {type(error).__name__}: {error}")


@pytest.fixture
def results():
    return TestResults()


def assert_eq(results: TestResults, name: str, got: Any, expected: Any):
    """Assert equality and record result."""
    if got == expected:
        results.add_pass(name)
    else:
        results.add_fail(name, expected, got)


def assert_true(results: TestResults, name: str, condition: bool, message: str = ""):
    """Assert condition is true."""
    if condition:
        results.add_pass(name)
    else:
        results.add_fail(name, True, f"False: {message}")


def assert_raises(results: TestResults, name: str, exception_type: Type[BaseException], func, *args, **kwargs):
    """Assert that function raises expected exception."""
    try:
        func(*args, **kwargs)
        results.add_fail(name, f"{exception_type.__name__} raised", "No exception raised")
    except exception_type:
        results.add_pass(name)
    except Exception as e:
        results.add_fail(name, f"{exception_type.__name__} raised", f"{type(e).__name__}: {e}")


# ============================================================================
# builders module tests
# ============================================================================

def test_normalize_to_name_list(results: TestResults):
    """Test normalize_to_name_list function."""
    print("\n=== Testing normalize_to_name_list ===")
    from hfortix_fortios._helpers.normalizers import normalize_to_name_list
    
    # Basic string input
    assert_eq(results, "string input", 
              normalize_to_name_list('test'), 
              [{'name': 'test'}])
    
    # List of strings
    assert_eq(results, "list of strings", 
              normalize_to_name_list(['a', 'b']), 
              [{'name': 'a'}, {'name': 'b'}])
    
    # Dict with name
    assert_eq(results, "dict with name", 
              normalize_to_name_list({'name': 'test'}), 
              [{'name': 'test'}])
    
    # List of dicts
    assert_eq(results, "list of dicts", 
              normalize_to_name_list([{'name': 'a'}, {'name': 'b'}]), 
              [{'name': 'a'}, {'name': 'b'}])
    
    # None input
    assert_eq(results, "None input", 
              normalize_to_name_list(None), 
              [])
    
    # Empty list
    assert_eq(results, "empty list", 
              normalize_to_name_list([]), 
              [])
    
    # Empty string - creates dict with empty name
    assert_eq(results, "empty string", 
              normalize_to_name_list(''), 
              [{'name': ''}])
    
    # Dict without 'name' key - returns empty (filters out non-matching)
    assert_eq(results, "dict without name key", 
              normalize_to_name_list({'foo': 'bar'}), 
              [])
    
    # BUG #7: Mixed list of strings and dicts - dict gets converted to string!
    # Expected: [{'name': 'a'}, {'name': 'b'}]
    # Actual:   [{'name': 'a'}, {'name': "{'name': 'b'}"}]  <- dict converted to string!
    result = normalize_to_name_list(['a', {'name': 'b'}])
    expected = [{'name': 'a'}, {'name': 'b'}]
    assert_eq(results, "BUG #7: mixed list of str and dict",
              result, expected)


def test_build_cmdb_payload(results: TestResults):
    """Test build_cmdb_payload function."""
    print("\n=== Testing build_cmdb_payload ===")
    from hfortix_fortios._helpers.builders import build_cmdb_payload
    
    # Basic payload
    assert_eq(results, "basic payload",
              build_cmdb_payload(name='test'),
              {'name': 'test'})
    
    # Filters out None values
    assert_eq(results, "filters None values",
              build_cmdb_payload(name='test', desc=None),
              {'name': 'test'})
    
    # Keeps empty strings
    assert_eq(results, "keeps empty strings",
              build_cmdb_payload(name='test', comment=''),
              {'name': 'test', 'comment': ''})
    
    # Converts underscore to hyphen in keys
    assert_eq(results, "converts underscore to hyphen",
              build_cmdb_payload(my_field='value'),
              {'my-field': 'value'})


def test_build_cmdb_payload_normalized(results: TestResults):
    """Test build_cmdb_payload_normalized function."""
    print("\n=== Testing build_cmdb_payload_normalized ===")
    from hfortix_fortios._helpers.builders import build_cmdb_payload_normalized
    
    # Normalizes member field
    assert_eq(results, "normalizes single string",
              build_cmdb_payload_normalized(member='test', normalize_fields={'member'}),
              {'member': [{'name': 'test'}]})
    
    # Normalizes list field
    assert_eq(results, "normalizes list",
              build_cmdb_payload_normalized(member=['a', 'b'], normalize_fields={'member'}),
              {'member': [{'name': 'a'}, {'name': 'b'}]})


def test_build_api_payload(results: TestResults):
    """Test build_api_payload function."""
    print("\n=== Testing build_api_payload ===")
    from hfortix_fortios._helpers.builders import build_api_payload
    
    # Basic with auto_normalize
    assert_eq(results, "basic with auto_normalize",
              build_api_payload(name='test', auto_normalize=True),
              {'name': 'test'})
    
    # Converts underscore to hyphen
    assert_eq(results, "converts underscore to hyphen",
              build_api_payload(my_field='value', auto_normalize=True),
              {'my-field': 'value'})


# ============================================================================
# converters module tests
# ============================================================================

def test_convert_boolean_to_str(results: TestResults):
    """Test convert_boolean_to_str function."""
    print("\n=== Testing convert_boolean_to_str ===")
    from hfortix_fortios._helpers.converters import convert_boolean_to_str
    
    # Boolean True -> 'enable'
    assert_eq(results, "True -> 'enable'",
              convert_boolean_to_str(True),
              'enable')
    
    # Boolean False -> 'disable'
    assert_eq(results, "False -> 'disable'",
              convert_boolean_to_str(False),
              'disable')
    
    # None passthrough
    assert_eq(results, "None passthrough",
              convert_boolean_to_str(None),
              None)
    
    # String 'enable' passthrough
    assert_eq(results, "'enable' passthrough",
              convert_boolean_to_str('enable'),
              'enable')
    
    # String 'disable' passthrough
    assert_eq(results, "'disable' passthrough",
              convert_boolean_to_str('disable'),
              'disable')
    
    # Other strings pass through unchanged
    assert_eq(results, "other strings passthrough",
              convert_boolean_to_str('yes'),
              'yes')
    
    # Integer gets converted to string
    assert_eq(results, "int converted to string",
              convert_boolean_to_str(1),
              '1')


def test_filter_empty_values(results: TestResults):
    """Test filter_empty_values function."""
    print("\n=== Testing filter_empty_values ===")
    from hfortix_fortios._helpers.converters import filter_empty_values
    
    # Empty dict
    assert_eq(results, "empty dict",
              filter_empty_values({}),
              {})
    
    # Non-empty values preserved
    assert_eq(results, "non-empty values preserved",
              filter_empty_values({'a': 1}),
              {'a': 1})
    
    # None filtered out
    assert_eq(results, "None filtered out",
              filter_empty_values({'a': None}),
              {})
    
    # Empty string NOT filtered
    assert_eq(results, "empty string NOT filtered",
              filter_empty_values({'a': ''}),
              {'a': ''})
    
    # Zero NOT filtered
    assert_eq(results, "zero NOT filtered",
              filter_empty_values({'a': 0}),
              {'a': 0})
    
    # False NOT filtered
    assert_eq(results, "False NOT filtered",
              filter_empty_values({'a': False}),
              {'a': False})
    
    # Empty list filtered out
    assert_eq(results, "empty list filtered out",
              filter_empty_values({'a': []}),
              {})
    
    # Empty dict filtered out
    assert_eq(results, "empty dict filtered out",
              filter_empty_values({'a': {}}),
              {})
    
    # Mixed - only None filtered
    assert_eq(results, "mixed filtering",
              filter_empty_values({'a': 1, 'b': None, 'c': 3}),
              {'a': 1, 'c': 3})


# ============================================================================
# normalizers module tests
# ============================================================================

def test_normalize_member_list(results: TestResults):
    """Test normalize_member_list function."""
    print("\n=== Testing normalize_member_list ===")
    from hfortix_fortios._helpers.normalizers import normalize_member_list
    
    # String input
    assert_eq(results, "string input",
              normalize_member_list('test'),
              [{'name': 'test'}])
    
    # List of strings
    assert_eq(results, "list of strings",
              normalize_member_list(['a', 'b']),
              [{'name': 'a'}, {'name': 'b'}])
    
    # None input
    assert_eq(results, "None input",
              normalize_member_list(None),
              [])
    
    # BUG #7 also affects normalize_member_list
    result = normalize_member_list(['a', {'name': 'b'}])
    expected = [{'name': 'a'}, {'name': 'b'}]
    assert_eq(results, "BUG #7: mixed list (normalize_member_list)",
              result, expected)


def test_normalize_table_field(results: TestResults):
    """Test normalize_table_field function."""
    print("\n=== Testing normalize_table_field ===")
    from hfortix_fortios._helpers.normalizers import normalize_table_field
    
    # String input with default mkey
    assert_eq(results, "string input default mkey",
              normalize_table_field('test'),
              [{'name': 'test'}])
    
    # String with custom mkey
    assert_eq(results, "string with custom mkey",
              normalize_table_field('test', mkey='q_origin_key'),
              [{'q_origin_key': 'test'}])
    
    # List of strings
    assert_eq(results, "list of strings",
              normalize_table_field(['a', 'b']),
              [{'name': 'a'}, {'name': 'b'}])
    
    # None input
    assert_eq(results, "None input",
              normalize_table_field(None),
              [])
    
    # Dict input preserved
    assert_eq(results, "dict input preserved",
              normalize_table_field({'name': 'test'}),
              [{'name': 'test'}])
    
    # BUG #7 also affects normalize_table_field
    result = normalize_table_field(['a', {'name': 'b'}])
    expected = [{'name': 'a'}, {'name': 'b'}]
    assert_eq(results, "BUG #7: mixed list (normalize_table_field)",
              result, expected)


# ============================================================================
# response module tests
# ============================================================================

def test_is_success(results: TestResults):
    """Test is_success function."""
    print("\n=== Testing is_success ===")
    from hfortix_fortios._helpers.response import is_success
    
    # Success status
    assert_eq(results, "status 'success' is success",
              is_success({'status': 'success'}),
              True)
    
    # Error status
    assert_eq(results, "status 'error' is not success",
              is_success({'status': 'error'}),
              False)
    
    # None input
    assert_eq(results, "None is not success",
              is_success(None),
              False)
    
    # Empty dict
    assert_eq(results, "empty dict is not success",
              is_success({}),
              False)
    
    # String 'success' (not dict) is not success
    assert_eq(results, "string 'success' is not success",
              is_success('success'),
              False)


def test_get_results(results: TestResults):
    """Test get_results function."""
    print("\n=== Testing get_results ===")
    from hfortix_fortios._helpers.response import get_results
    
    # List results
    assert_eq(results, "list results",
              get_results({'results': ['a', 'b']}),
              ['a', 'b'])
    
    # Dict results
    assert_eq(results, "dict results",
              get_results({'results': {'name': 'test'}}),
              {'name': 'test'})
    
    # No results key
    assert_eq(results, "no results key",
              get_results({}),
              None)
    
    # None input
    assert_eq(results, "None input",
              get_results(None),
              None)


def test_get_name_and_mkey(results: TestResults):
    """Test get_name and get_mkey functions."""
    print("\n=== Testing get_name and get_mkey ===")
    from hfortix_fortios._helpers.response import get_name, get_mkey
    
    # get_name extracts mkey field
    assert_eq(results, "get_name extracts mkey",
              get_name({'mkey': 'test-obj'}),
              'test-obj')
    
    # No mkey
    assert_eq(results, "get_name returns None without mkey",
              get_name({'status': 'success'}),
              None)
    
    # None input
    assert_eq(results, "get_name with None",
              get_name(None),
              None)
    
    # get_mkey is alias for get_name
    assert_eq(results, "get_mkey extracts mkey",
              get_mkey({'mkey': 'test-obj'}),
              'test-obj')


# ============================================================================
# validation module tests
# ============================================================================

def test_validate_enum_field(results: TestResults):
    """Test validate_enum_field function."""
    print("\n=== Testing validate_enum_field ===")
    from hfortix_fortios._helpers.validation import validate_enum_field
    
    # Valid value
    ok, msg = validate_enum_field('status', 'enable', ['enable', 'disable'], {'status': 'Status'})
    assert_eq(results, "valid value returns (True, None)", 
              (ok, msg), (True, None))
    
    # Invalid value
    ok, msg = validate_enum_field('status', 'active', ['enable', 'disable'], {'status': 'Status'})
    assert_eq(results, "invalid value returns (False, message)", 
              ok, False)
    assert_true(results, "error message contains field name", 
                'status' in msg if msg else False, msg or "")


def test_validate_required_fields(results: TestResults):
    """Test validate_required_fields function."""
    print("\n=== Testing validate_required_fields ===")
    from hfortix_fortios._helpers.validation import validate_required_fields
    
    # All present
    ok, msg = validate_required_fields(
        {'name': 'test', 'type': 'foo'}, 
        ['name', 'type'], 
        {'name': 'Name', 'type': 'Type'}
    )
    assert_eq(results, "all required present", (ok, msg), (True, None))
    
    # Missing field
    ok, msg = validate_required_fields(
        {'name': 'test'}, 
        ['name', 'type'], 
        {'name': 'Name', 'type': 'Type'}
    )
    assert_eq(results, "missing field returns False", ok, False)
    assert_true(results, "error mentions missing field", 
                'type' in msg.lower() if msg else False, msg or "")


def test_validate_query_parameter(results: TestResults):
    """Test validate_query_parameter function."""
    print("\n=== Testing validate_query_parameter ===")
    from hfortix_fortios._helpers.validation import validate_query_parameter
    
    # Valid
    ok, msg = validate_query_parameter('format', 'json', ['json', 'xml'])
    assert_eq(results, "valid param", (ok, msg), (True, None))
    
    # Invalid
    ok, msg = validate_query_parameter('format', 'csv', ['json', 'xml'])
    assert_eq(results, "invalid param returns False", ok, False)


# ============================================================================
# Main test runner
# ============================================================================

def main():
    """Run all tests."""
    print("=" * 60)
    print("hfortix_fortios._helpers module tests")
    print("=" * 60)
    
    results = TestResults()
    
    # Run all tests
    try:
        test_normalize_to_name_list(results)
        test_build_cmdb_payload(results)
        test_build_cmdb_payload_normalized(results)
        test_build_api_payload(results)
        test_convert_boolean_to_str(results)
        test_filter_empty_values(results)
        test_normalize_member_list(results)
        test_normalize_table_field(results)
        test_is_success(results)
        test_get_results(results)
        test_get_name_and_mkey(results)
        test_validate_enum_field(results)
        test_validate_required_fields(results)
        test_validate_query_parameter(results)
    except Exception as e:
        print(f"\n!!! Test suite error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        results.failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Results: {results.passed} passed, {results.failed} failed")
    print("=" * 60)
    
    if results.failed > 0:
        print("\nFailed tests:")
        for name, expected, got in results.errors:
            print(f"  - {name}")
        
        print("\n" + "-" * 60)
        print("BUG #7 FOUND:")
        print("-" * 60)
        print("""
normalize_to_name_list, normalize_member_list, and normalize_table_field
do not properly handle mixed lists of strings and dicts.

Location: hfortix_fortios._helpers.builders.normalize_to_name_list
         hfortix_fortios._helpers.normalizers.normalize_member_list
         hfortix_fortios._helpers.normalizers.normalize_table_field

Example:
  normalize_to_name_list(['a', {'name': 'b'}])
  
  Expected: [{'name': 'a'}, {'name': 'b'}]
  Actual:   [{'name': 'a'}, {'name': "{'name': 'b'}"}]

The issue is that when processing a list, if an item is already a dict
with the correct structure, it gets converted to string via str(item)
instead of being preserved.
""")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
