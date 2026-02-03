"""
Tests for hfortix_fortios normalizers.

Tests normalize_to_name_list, normalize_member_list, and normalize_table_field functions.
"""

from hfortix_fortios._helpers.normalizers import (
    normalize_to_name_list,
    normalize_member_list,
    normalize_table_field,
)


def test_normalize_to_name_list_string():
    """Test normalizing a single string."""
    result = normalize_to_name_list("port1")
    assert result == [{"name": "port1"}]
    print("✅ normalize_to_name_list - single string")


def test_normalize_to_name_list_string_with_whitespace():
    """Test that whitespace is trimmed from strings."""
    result = normalize_to_name_list("  port1  ")
    assert result == [{"name": "port1"}]
    print("✅ normalize_to_name_list - string with whitespace trimmed")


def test_normalize_to_name_list_list_of_strings():
    """Test normalizing a list of strings."""
    result = normalize_to_name_list(["port1", "port2", "port3"])
    assert result == [{"name": "port1"}, {"name": "port2"}, {"name": "port3"}]
    print("✅ normalize_to_name_list - list of strings")


def test_normalize_to_name_list_list_of_strings_with_whitespace():
    """Test that whitespace is trimmed from list items."""
    result = normalize_to_name_list(["  port1  ", " port2", "port3 "])
    assert result == [{"name": "port1"}, {"name": "port2"}, {"name": "port3"}]
    print("✅ normalize_to_name_list - list of strings with whitespace")


def test_normalize_to_name_list_dict():
    """Test normalizing a single dict."""
    result = normalize_to_name_list({"name": "port1"})
    assert result == [{"name": "port1"}]
    print("✅ normalize_to_name_list - single dict")


def test_normalize_to_name_list_list_of_dicts():
    """Test normalizing a list of dicts (passthrough)."""
    input_list = [{"name": "port1"}, {"name": "port2"}]
    result = normalize_to_name_list(input_list)
    assert result == [{"name": "port1"}, {"name": "port2"}]
    print("✅ normalize_to_name_list - list of dicts")


def test_normalize_to_name_list_none():
    """Test normalizing None returns empty list."""
    result = normalize_to_name_list(None)
    assert result == []
    print("✅ normalize_to_name_list - None")


def test_normalize_to_name_list_empty_list():
    """Test normalizing empty list returns empty list."""
    result = normalize_to_name_list([])
    assert result == []
    print("✅ normalize_to_name_list - empty list")


def test_normalize_to_name_list_empty_dict():
    """Test normalizing empty dict returns empty list."""
    result = normalize_to_name_list({})
    assert result == []
    print("✅ normalize_to_name_list - empty dict")


def test_normalize_to_name_list_dict_without_name():
    """Test dict without 'name' key returns empty list."""
    result = normalize_to_name_list({"other": "value"})
    assert result == []
    print("✅ normalize_to_name_list - dict without name key")


def test_normalize_to_name_list_filters_empty_dicts():
    """Test that empty dicts in list are filtered out."""
    result = normalize_to_name_list([{"name": "port1"}, {}, {"name": "port2"}])
    assert result == [{"name": "port1"}, {"name": "port2"}]
    print("✅ normalize_to_name_list - filters empty dicts")


# ============================================================================
# normalize_member_list tests (should behave same as normalize_to_name_list)
# ============================================================================

def test_normalize_member_list_string():
    """Test normalize_member_list with string."""
    result = normalize_member_list("addr1")
    assert result == [{"name": "addr1"}]
    print("✅ normalize_member_list - single string")


def test_normalize_member_list_list():
    """Test normalize_member_list with list."""
    result = normalize_member_list(["addr1", "addr2"])
    assert result == [{"name": "addr1"}, {"name": "addr2"}]
    print("✅ normalize_member_list - list of strings")


def test_normalize_member_list_none():
    """Test normalize_member_list with None."""
    result = normalize_member_list(None)
    assert result == []
    print("✅ normalize_member_list - None")


# ============================================================================
# normalize_table_field tests
# ============================================================================

def test_normalize_table_field_string_default_mkey():
    """Test normalize_table_field with string and default mkey."""
    result = normalize_table_field("value1")
    assert result == [{"name": "value1"}]
    print("✅ normalize_table_field - string with default mkey")


def test_normalize_table_field_string_custom_mkey():
    """Test normalize_table_field with custom mkey."""
    result = normalize_table_field("eth0", mkey="interface-name")
    assert result == [{"interface-name": "eth0"}]
    print("✅ normalize_table_field - string with custom mkey")


def test_normalize_table_field_string_with_whitespace():
    """Test that whitespace is trimmed."""
    result = normalize_table_field("  value1  ", mkey="id")
    assert result == [{"id": "value1"}]
    print("✅ normalize_table_field - whitespace trimmed")


def test_normalize_table_field_list_of_strings():
    """Test normalize_table_field with list of strings."""
    result = normalize_table_field(["a", "b", "c"])
    assert result == [{"name": "a"}, {"name": "b"}, {"name": "c"}]
    print("✅ normalize_table_field - list of strings")


def test_normalize_table_field_list_of_dicts():
    """Test normalize_table_field with list of dicts (passthrough)."""
    input_list = [{"id": 1, "value": "a"}, {"id": 2, "value": "b"}]
    result = normalize_table_field(input_list)
    assert result == input_list
    print("✅ normalize_table_field - list of dicts passthrough")


def test_normalize_table_field_single_dict():
    """Test normalize_table_field with single dict."""
    result = normalize_table_field({"id": 1, "value": "test"})
    assert result == [{"id": 1, "value": "test"}]
    print("✅ normalize_table_field - single dict")


def test_normalize_table_field_none():
    """Test normalize_table_field with None."""
    result = normalize_table_field(None)
    assert result == []
    print("✅ normalize_table_field - None")


def test_normalize_table_field_empty_list():
    """Test normalize_table_field with empty list."""
    result = normalize_table_field([])
    assert result == []
    print("✅ normalize_table_field - empty list")


def test_normalize_table_field_multi_field_requires_dict():
    """Test that multi-field objects require dict format."""
    # With more than 1 required field, string format should raise ValueError
    try:
        normalize_table_field(
            "simple_string",
            required_fields=["id", "name", "value"],
            field_name="test_field"
        )
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "requires dict format" in str(e)
        print("✅ normalize_table_field - multi-field rejects string")


def test_normalize_table_field_multi_field_list_of_strings_rejected():
    """Test that list of strings is rejected for multi-field objects."""
    try:
        normalize_table_field(
            ["a", "b", "c"],
            required_fields=["id", "name"],
            field_name="members"
        )
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "requires dict format" in str(e)
        print("✅ normalize_table_field - multi-field rejects list of strings")


def test_normalize_table_field_single_required_field_accepts_string():
    """Test that single required field accepts string format."""
    result = normalize_table_field(
        "value1",
        required_fields=["name"]
    )
    assert result == [{"name": "value1"}]
    print("✅ normalize_table_field - single required field accepts string")


def test_normalize_table_field_error_message_includes_example():
    """Test that error message includes auto-generated example."""
    try:
        normalize_table_field(
            "invalid",
            required_fields=["id", "port"],
            field_name="servers"
        )
        assert False, "Should have raised ValueError"
    except ValueError as e:
        error_msg = str(e)
        assert "servers" in error_msg
        assert "id" in error_msg
        assert "port" in error_msg
        print("✅ normalize_table_field - error includes example")


def run_all_tests():
    """Run all normalizer tests."""
    print("\n" + "=" * 60)
    print("NORMALIZER TESTS")
    print("=" * 60 + "\n")

    # normalize_to_name_list tests
    test_normalize_to_name_list_string()
    test_normalize_to_name_list_string_with_whitespace()
    test_normalize_to_name_list_list_of_strings()
    test_normalize_to_name_list_list_of_strings_with_whitespace()
    test_normalize_to_name_list_dict()
    test_normalize_to_name_list_list_of_dicts()
    test_normalize_to_name_list_none()
    test_normalize_to_name_list_empty_list()
    test_normalize_to_name_list_empty_dict()
    test_normalize_to_name_list_dict_without_name()
    test_normalize_to_name_list_filters_empty_dicts()

    # normalize_member_list tests
    test_normalize_member_list_string()
    test_normalize_member_list_list()
    test_normalize_member_list_none()

    # normalize_table_field tests
    test_normalize_table_field_string_default_mkey()
    test_normalize_table_field_string_custom_mkey()
    test_normalize_table_field_string_with_whitespace()
    test_normalize_table_field_list_of_strings()
    test_normalize_table_field_list_of_dicts()
    test_normalize_table_field_single_dict()
    test_normalize_table_field_none()
    test_normalize_table_field_empty_list()
    test_normalize_table_field_multi_field_requires_dict()
    test_normalize_table_field_multi_field_list_of_strings_rejected()
    test_normalize_table_field_single_required_field_accepts_string()
    test_normalize_table_field_error_message_includes_example()

    print("\n" + "=" * 60)
    print("ALL NORMALIZER TESTS PASSED!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_tests()
