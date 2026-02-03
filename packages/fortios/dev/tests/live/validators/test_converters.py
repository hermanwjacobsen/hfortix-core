"""
Tests for hfortix_fortios converters.

Tests convert_boolean_to_str and filter_empty_values functions.
"""

from hfortix_fortios._helpers.converters import (
    convert_boolean_to_str,
    filter_empty_values,
)


def test_convert_boolean_true():
    """Test converting True to 'enable'."""
    result = convert_boolean_to_str(True)
    assert result == "enable"
    print("✅ convert_boolean_to_str - True -> 'enable'")


def test_convert_boolean_false():
    """Test converting False to 'disable'."""
    result = convert_boolean_to_str(False)
    assert result == "disable"
    print("✅ convert_boolean_to_str - False -> 'disable'")


def test_convert_boolean_none():
    """Test converting None returns None."""
    result = convert_boolean_to_str(None)
    assert result is None
    print("✅ convert_boolean_to_str - None -> None")


def test_convert_boolean_string_passthrough():
    """Test string values are passed through."""
    result = convert_boolean_to_str("enable")
    assert result == "enable"
    print("✅ convert_boolean_to_str - string passthrough")


def test_convert_boolean_string_other():
    """Test other string values are passed through."""
    result = convert_boolean_to_str("custom")
    assert result == "custom"
    print("✅ convert_boolean_to_str - other string passthrough")


def test_convert_boolean_int_to_str():
    """Test integer is converted to string."""
    result = convert_boolean_to_str(123)  # type: ignore
    assert result == "123"
    print("✅ convert_boolean_to_str - int to str")


# ============================================================================
# filter_empty_values tests
# ============================================================================

def test_filter_empty_values_removes_none():
    """Test that None values are removed."""
    payload = {"name": "test", "comment": None, "status": "enable"}
    result = filter_empty_values(payload)
    assert result == {"name": "test", "status": "enable"}
    print("✅ filter_empty_values - removes None")


def test_filter_empty_values_removes_empty_list():
    """Test that empty lists are removed."""
    payload = {"name": "test", "members": [], "status": "enable"}
    result = filter_empty_values(payload)
    assert result == {"name": "test", "status": "enable"}
    print("✅ filter_empty_values - removes empty list")


def test_filter_empty_values_removes_empty_dict():
    """Test that empty dicts are removed."""
    payload = {"name": "test", "config": {}, "status": "enable"}
    result = filter_empty_values(payload)
    assert result == {"name": "test", "status": "enable"}
    print("✅ filter_empty_values - removes empty dict")


def test_filter_empty_values_keeps_non_empty_list():
    """Test that non-empty lists are kept."""
    payload = {"name": "test", "members": [{"name": "addr1"}]}
    result = filter_empty_values(payload)
    assert result == {"name": "test", "members": [{"name": "addr1"}]}
    print("✅ filter_empty_values - keeps non-empty list")


def test_filter_empty_values_keeps_non_empty_dict():
    """Test that non-empty dicts are kept."""
    payload = {"name": "test", "config": {"key": "value"}}
    result = filter_empty_values(payload)
    assert result == {"name": "test", "config": {"key": "value"}}
    print("✅ filter_empty_values - keeps non-empty dict")


def test_filter_empty_values_keeps_zero():
    """Test that zero values are kept."""
    payload = {"name": "test", "count": 0, "priority": 0}
    result = filter_empty_values(payload)
    assert result == {"name": "test", "count": 0, "priority": 0}
    print("✅ filter_empty_values - keeps zero values")


def test_filter_empty_values_keeps_empty_string():
    """Test that empty strings are kept (not filtered)."""
    payload = {"name": "test", "comment": ""}
    result = filter_empty_values(payload)
    assert result == {"name": "test", "comment": ""}
    print("✅ filter_empty_values - keeps empty string")


def test_filter_empty_values_keeps_false():
    """Test that False values are kept."""
    payload = {"name": "test", "enabled": False}
    result = filter_empty_values(payload)
    assert result == {"name": "test", "enabled": False}
    print("✅ filter_empty_values - keeps False")


def test_filter_empty_values_all_none():
    """Test filtering payload with all None values."""
    payload = {"a": None, "b": None, "c": None}
    result = filter_empty_values(payload)
    assert result == {}
    print("✅ filter_empty_values - all None values")


def test_filter_empty_values_mixed():
    """Test filtering payload with mixed values."""
    payload = {
        "name": "test",
        "comment": None,
        "members": [],
        "config": {},
        "status": "enable",
        "count": 0,
        "valid": [{"name": "a"}],
    }
    result = filter_empty_values(payload)
    assert result == {
        "name": "test",
        "status": "enable",
        "count": 0,
        "valid": [{"name": "a"}],
    }
    print("✅ filter_empty_values - mixed values")


def test_filter_empty_values_empty_payload():
    """Test filtering empty payload."""
    result = filter_empty_values({})
    assert result == {}
    print("✅ filter_empty_values - empty payload")


def run_all_tests():
    """Run all converter tests."""
    print("\n" + "=" * 60)
    print("CONVERTER TESTS")
    print("=" * 60 + "\n")

    # convert_boolean_to_str tests
    test_convert_boolean_true()
    test_convert_boolean_false()
    test_convert_boolean_none()
    test_convert_boolean_string_passthrough()
    test_convert_boolean_string_other()
    test_convert_boolean_int_to_str()

    # filter_empty_values tests
    test_filter_empty_values_removes_none()
    test_filter_empty_values_removes_empty_list()
    test_filter_empty_values_removes_empty_dict()
    test_filter_empty_values_keeps_non_empty_list()
    test_filter_empty_values_keeps_non_empty_dict()
    test_filter_empty_values_keeps_zero()
    test_filter_empty_values_keeps_empty_string()
    test_filter_empty_values_keeps_false()
    test_filter_empty_values_all_none()
    test_filter_empty_values_mixed()
    test_filter_empty_values_empty_payload()

    print("\n" + "=" * 60)
    print("ALL CONVERTER TESTS PASSED!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_tests()
