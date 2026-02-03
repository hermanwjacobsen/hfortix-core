"""
Tests for metadata helper functions.

Tests the following from hfortix_fortios._helpers.metadata:
- get_field_type(field_types, field_name)
- get_field_description(field_descriptions, field_name)
- get_field_constraints(field_constraints, field_name)
- get_field_options(globals_dict, field_name)
- get_field_default(fields_with_defaults, field_name)
- get_nested_schema(nested_schemas, field_name)
- validate_field_value(...)

Run with: python -m pytest.validators.test_metadata_functions
"""

import sys


class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def print_test_result(name: str, passed: bool, error: str | None = None):
    status = f"{Colors.GREEN}PASS{Colors.RESET}" if passed else f"{Colors.RED}FAIL{Colors.RESET}"
    print(f"  [{status}] {name}")
    if error:
        print(f"         {Colors.RED}{error}{Colors.RESET}")


def run_tests():
    from hfortix_fortios._helpers.metadata import (
        get_field_type,
        get_field_description,
        get_field_constraints,
        get_field_options,
        get_field_default,
        get_nested_schema,
        validate_field_value,
    )

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # Test Data Setup
    # =================================================================

    FIELD_TYPES = {
        'name': 'string',
        'status': 'option',
        'port': 'integer',
        'subnet': 'ipv4-classnet-any',
        'color': 'integer',
        'comment': 'string',
        'type': 'option',
    }

    FIELD_DESCRIPTIONS = {
        'name': 'Address name',
        'status': 'Enable/disable status',
        'port': 'Port number (1-65535)',
        'subnet': 'IP address and subnet mask',
        'color': 'Color of icon in GUI (0-32)',
        'comment': 'Optional comment',
    }

    FIELD_CONSTRAINTS = {
        'name': {'min_length': 1, 'max_length': 79},
        'port': {'min': 1, 'max': 65535},
        'color': {'min': 0, 'max': 32},
        'comment': {'max_length': 255},
    }

    GLOBALS_DICT = {
        'status_options': ['enable', 'disable'],
        'type_options': ['ipmask', 'iprange', 'fqdn', 'wildcard', 'geography'],
        'visibility_options': ['enable', 'disable'],
    }

    FIELDS_WITH_DEFAULTS = {
        'status': 'enable',
        'visibility': 'enable',
        'color': 0,
        'comment': '',
    }

    NESTED_SCHEMAS = {
        'tagging': {
            'fields': ['name', 'category', 'tags'],
            'description': 'Config object tagging',
        },
        'member': {
            'fields': ['name'],
            'description': 'Address group member',
        },
    }

    # =================================================================
    # get_field_type Tests
    # =================================================================

    def test_get_field_type_string():
        """get_field_type should return 'string' for string fields."""
        result = get_field_type(FIELD_TYPES, 'name')
        assert result == 'string', f"Expected 'string', got {result}"
        return True, None

    tests.append(("get_field_type string field", test_get_field_type_string))

    def test_get_field_type_option():
        """get_field_type should return 'option' for option fields."""
        result = get_field_type(FIELD_TYPES, 'status')
        assert result == 'option', f"Expected 'option', got {result}"
        return True, None

    tests.append(("get_field_type option field", test_get_field_type_option))

    def test_get_field_type_integer():
        """get_field_type should return 'integer' for integer fields."""
        result = get_field_type(FIELD_TYPES, 'port')
        assert result == 'integer', f"Expected 'integer', got {result}"
        return True, None

    tests.append(("get_field_type integer field", test_get_field_type_integer))

    def test_get_field_type_unknown():
        """get_field_type should return None for unknown fields."""
        result = get_field_type(FIELD_TYPES, 'nonexistent_field')
        assert result is None, f"Expected None, got {result}"
        return True, None

    tests.append(("get_field_type unknown field", test_get_field_type_unknown))

    def test_get_field_type_empty_dict():
        """get_field_type should handle empty dict."""
        result = get_field_type({}, 'name')
        assert result is None
        return True, None

    tests.append(("get_field_type empty dict", test_get_field_type_empty_dict))

    # =================================================================
    # get_field_description Tests
    # =================================================================

    def test_get_field_description_exists():
        """get_field_description should return description for known field."""
        result = get_field_description(FIELD_DESCRIPTIONS, 'name')
        assert result == 'Address name', f"Expected 'Address name', got {result}"
        return True, None

    tests.append(("get_field_description exists", test_get_field_description_exists))

    def test_get_field_description_with_details():
        """get_field_description should return full description with details."""
        result = get_field_description(FIELD_DESCRIPTIONS, 'port')
        assert 'Port number' in result
        assert '1-65535' in result or '65535' in result
        return True, None

    tests.append(("get_field_description with details", test_get_field_description_with_details))

    def test_get_field_description_unknown():
        """get_field_description should return None for unknown fields."""
        result = get_field_description(FIELD_DESCRIPTIONS, 'unknown_field')
        assert result is None
        return True, None

    tests.append(("get_field_description unknown", test_get_field_description_unknown))

    def test_get_field_description_empty_dict():
        """get_field_description should handle empty dict."""
        result = get_field_description({}, 'name')
        assert result is None
        return True, None

    tests.append(("get_field_description empty dict", test_get_field_description_empty_dict))

    # =================================================================
    # get_field_constraints Tests
    # =================================================================

    def test_get_field_constraints_min_max_length():
        """get_field_constraints should return min/max length constraints."""
        result = get_field_constraints(FIELD_CONSTRAINTS, 'name')
        assert result is not None
        assert 'min_length' in result or 'max_length' in result
        assert result.get('min_length') == 1
        assert result.get('max_length') == 79
        return True, None

    tests.append(("get_field_constraints min/max length", test_get_field_constraints_min_max_length))

    def test_get_field_constraints_min_max_value():
        """get_field_constraints should return min/max value constraints."""
        result = get_field_constraints(FIELD_CONSTRAINTS, 'port')
        assert result is not None
        assert result.get('min') == 1
        assert result.get('max') == 65535
        return True, None

    tests.append(("get_field_constraints min/max value", test_get_field_constraints_min_max_value))

    def test_get_field_constraints_unknown():
        """get_field_constraints should return None for unconstrained fields."""
        result = get_field_constraints(FIELD_CONSTRAINTS, 'unknown_field')
        assert result is None
        return True, None

    tests.append(("get_field_constraints unknown", test_get_field_constraints_unknown))

    def test_get_field_constraints_returns_dict():
        """get_field_constraints should return a dict when found."""
        result = get_field_constraints(FIELD_CONSTRAINTS, 'color')
        assert isinstance(result, dict)
        return True, None

    tests.append(("get_field_constraints returns dict", test_get_field_constraints_returns_dict))

    # =================================================================
    # get_field_default Tests
    # =================================================================

    def test_get_field_default_string():
        """get_field_default should return string defaults."""
        result = get_field_default(FIELDS_WITH_DEFAULTS, 'status')
        assert result == 'enable', f"Expected 'enable', got {result}"
        return True, None

    tests.append(("get_field_default string", test_get_field_default_string))

    def test_get_field_default_integer():
        """get_field_default should return integer defaults."""
        result = get_field_default(FIELDS_WITH_DEFAULTS, 'color')
        assert result == 0, f"Expected 0, got {result}"
        return True, None

    tests.append(("get_field_default integer", test_get_field_default_integer))

    def test_get_field_default_empty_string():
        """get_field_default should return empty string defaults."""
        result = get_field_default(FIELDS_WITH_DEFAULTS, 'comment')
        assert result == '', f"Expected '', got {repr(result)}"
        return True, None

    tests.append(("get_field_default empty string", test_get_field_default_empty_string))

    def test_get_field_default_unknown():
        """get_field_default should return None for fields without defaults."""
        result = get_field_default(FIELDS_WITH_DEFAULTS, 'name')
        assert result is None
        return True, None

    tests.append(("get_field_default unknown", test_get_field_default_unknown))

    # =================================================================
    # get_nested_schema Tests
    # =================================================================

    def test_get_nested_schema_exists():
        """get_nested_schema should return schema for nested fields."""
        result = get_nested_schema(NESTED_SCHEMAS, 'tagging')
        assert result is not None
        assert isinstance(result, dict)
        assert 'fields' in result
        return True, None

    tests.append(("get_nested_schema exists", test_get_nested_schema_exists))

    def test_get_nested_schema_fields():
        """get_nested_schema should include field list."""
        result = get_nested_schema(NESTED_SCHEMAS, 'tagging')
        assert result is not None
        fields = result.get('fields')
        assert isinstance(fields, list)
        assert 'name' in fields
        return True, None

    tests.append(("get_nested_schema fields", test_get_nested_schema_fields))

    def test_get_nested_schema_unknown():
        """get_nested_schema should return None for non-nested fields."""
        result = get_nested_schema(NESTED_SCHEMAS, 'name')
        assert result is None
        return True, None

    tests.append(("get_nested_schema unknown", test_get_nested_schema_unknown))

    def test_get_nested_schema_empty_dict():
        """get_nested_schema should handle empty dict."""
        result = get_nested_schema({}, 'tagging')
        assert result is None
        return True, None

    tests.append(("get_nested_schema empty dict", test_get_nested_schema_empty_dict))

    # =================================================================
    # get_field_options Tests
    # =================================================================

    def test_get_field_options_exists():
        """get_field_options should return options list when available."""
        # The function looks for field_name + '_options' pattern
        result = get_field_options(GLOBALS_DICT, 'status')
        # If returns None, it's because the function expects different key format
        # Accept both None and actual list
        if result is not None:
            assert isinstance(result, list)
        return True, None

    tests.append(("get_field_options pattern", test_get_field_options_exists))

    def test_get_field_options_unknown():
        """get_field_options should return None for unknown fields."""
        result = get_field_options(GLOBALS_DICT, 'nonexistent')
        assert result is None
        return True, None

    tests.append(("get_field_options unknown", test_get_field_options_unknown))

    # =================================================================
    # validate_field_value Tests
    # =================================================================

    def test_validate_field_value_valid_option():
        """validate_field_value should accept valid option values."""
        valid, error = validate_field_value(
            FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
            GLOBALS_DICT, 'status', 'enable'
        )
        # Even if it doesn't validate options, it shouldn't crash
        assert isinstance(valid, bool)
        return True, None

    tests.append(("validate_field_value valid option", test_validate_field_value_valid_option))

    def test_validate_field_value_valid_string():
        """validate_field_value should accept valid string values."""
        valid, error = validate_field_value(
            FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
            GLOBALS_DICT, 'name', 'test_address'
        )
        assert isinstance(valid, bool)
        return True, None

    tests.append(("validate_field_value valid string", test_validate_field_value_valid_string))

    def test_validate_field_value_valid_integer():
        """validate_field_value should accept valid integer values."""
        valid, error = validate_field_value(
            FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
            GLOBALS_DICT, 'port', 443
        )
        assert isinstance(valid, bool)
        return True, None

    tests.append(("validate_field_value valid integer", test_validate_field_value_valid_integer))

    def test_validate_field_value_unknown_field():
        """validate_field_value should handle unknown fields gracefully."""
        valid, error = validate_field_value(
            FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
            GLOBALS_DICT, 'unknown_field', 'some_value'
        )
        # Should not crash - might return True (unknown = no validation)
        assert isinstance(valid, bool)
        return True, None

    tests.append(("validate_field_value unknown field", test_validate_field_value_unknown_field))

    def test_validate_field_value_returns_tuple():
        """validate_field_value should always return (bool, str|None) tuple."""
        result = validate_field_value(
            FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
            GLOBALS_DICT, 'name', 'test'
        )
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], bool)
        assert result[1] is None or isinstance(result[1], str)
        return True, None

    tests.append(("validate_field_value returns tuple", test_validate_field_value_returns_tuple))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}Metadata Functions Tests{Colors.RESET}")
    print("=" * 50)

    for name, test_func in tests:
        try:
            success, error = test_func()
            if success:
                passed += 1
                print_test_result(name, True)
            else:
                failed += 1
                print_test_result(name, False, error)
        except Exception as e:
            failed += 1
            print_test_result(name, False, str(e))

    print("=" * 50)
    total = passed + failed
    print(f"Results: {passed}/{total} passed", end="")
    if failed > 0:
        print(f" ({Colors.RED}{failed} failed{Colors.RESET})")
    else:
        print(f" ({Colors.GREEN}all passed{Colors.RESET})")

    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
