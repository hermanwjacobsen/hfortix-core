"""
Tests for hfortix_fortios metadata functions.

Tests all metadata accessor functions and validate_field_value.
"""

from typing import Any

from hfortix_fortios._helpers.metadata import (
    get_field_description,
    get_field_type,
    get_field_constraints,
    get_field_default,
    get_field_options,
    get_nested_schema,
    get_all_fields,
    get_field_metadata,
    validate_field_value,
)


# Sample test data mimicking what would be in a helper module
FIELD_DESCRIPTIONS = {
    "name": "Object name",
    "status": "Enable or disable this feature",
    "comment": "Optional comment for this object",
    "priority": "Processing priority (0-255)",
}

FIELD_TYPES = {
    "name": "string",
    "status": "option",
    "comment": "string",
    "priority": "integer",
    "members": "table",
}

FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
    "comment": {"type": "string", "max_length": 255},
    "priority": {"type": "integer", "min": 0, "max": 255},
}

FIELDS_WITH_DEFAULTS = {
    "status": "enable",
    "priority": 0,
}

REQUIRED_FIELDS = ["name"]

NESTED_SCHEMAS = {
    "members": {
        "name": {"type": "string", "required": True},
        "status": {"type": "option", "options": ["enable", "disable"]},
    }
}

# Valid enum options (simulating globals())
VALID_BODY_STATUS = ["enable", "disable"]


def get_test_globals() -> dict[str, Any]:
    """Get a mock globals dict for testing."""
    return {
        "VALID_BODY_STATUS": VALID_BODY_STATUS,
    }


# ============================================================================
# get_field_description tests
# ============================================================================

def test_get_field_description_exists():
    """Test getting description for existing field."""
    result = get_field_description(FIELD_DESCRIPTIONS, "name")
    assert result == "Object name"
    print("✅ get_field_description - existing field")


def test_get_field_description_not_exists():
    """Test getting description for non-existing field."""
    result = get_field_description(FIELD_DESCRIPTIONS, "unknown")
    assert result is None
    print("✅ get_field_description - non-existing field")


# ============================================================================
# get_field_type tests
# ============================================================================

def test_get_field_type_string():
    """Test getting string field type."""
    result = get_field_type(FIELD_TYPES, "name")
    assert result == "string"
    print("✅ get_field_type - string")


def test_get_field_type_option():
    """Test getting option field type."""
    result = get_field_type(FIELD_TYPES, "status")
    assert result == "option"
    print("✅ get_field_type - option")


def test_get_field_type_integer():
    """Test getting integer field type."""
    result = get_field_type(FIELD_TYPES, "priority")
    assert result == "integer"
    print("✅ get_field_type - integer")


def test_get_field_type_table():
    """Test getting table field type."""
    result = get_field_type(FIELD_TYPES, "members")
    assert result == "table"
    print("✅ get_field_type - table")


def test_get_field_type_not_exists():
    """Test getting type for non-existing field."""
    result = get_field_type(FIELD_TYPES, "unknown")
    assert result is None
    print("✅ get_field_type - non-existing field")


# ============================================================================
# get_field_constraints tests
# ============================================================================

def test_get_field_constraints_string():
    """Test getting string field constraints."""
    result = get_field_constraints(FIELD_CONSTRAINTS, "name")
    assert result is not None
    assert result["type"] == "string"
    assert result["max_length"] == 63
    print("✅ get_field_constraints - string constraints")


def test_get_field_constraints_integer():
    """Test getting integer field constraints."""
    result = get_field_constraints(FIELD_CONSTRAINTS, "priority")
    assert result is not None
    assert result["type"] == "integer"
    assert result["min"] == 0
    assert result["max"] == 255
    print("✅ get_field_constraints - integer constraints")


def test_get_field_constraints_not_exists():
    """Test getting constraints for field without constraints."""
    result = get_field_constraints(FIELD_CONSTRAINTS, "status")
    assert result is None
    print("✅ get_field_constraints - no constraints")


# ============================================================================
# get_field_default tests
# ============================================================================

def test_get_field_default_exists():
    """Test getting default for field with default."""
    result = get_field_default(FIELDS_WITH_DEFAULTS, "status")
    assert result == "enable"
    print("✅ get_field_default - with default")


def test_get_field_default_zero():
    """Test getting zero default."""
    result = get_field_default(FIELDS_WITH_DEFAULTS, "priority")
    assert result == 0
    print("✅ get_field_default - zero default")


def test_get_field_default_not_exists():
    """Test getting default for field without default."""
    result = get_field_default(FIELDS_WITH_DEFAULTS, "name")
    assert result is None
    print("✅ get_field_default - no default")


# ============================================================================
# get_field_options tests
# ============================================================================

def test_get_field_options_exists():
    """Test getting options for enum field."""
    globals_dict = get_test_globals()
    result = get_field_options(globals_dict, "status")
    assert result == ["enable", "disable"]
    print("✅ get_field_options - with options")


def test_get_field_options_not_exists():
    """Test getting options for non-enum field."""
    globals_dict = get_test_globals()
    result = get_field_options(globals_dict, "name")
    assert result is None
    print("✅ get_field_options - no options")


def test_get_field_options_with_special_chars():
    """Test getting options for field with special characters."""
    globals_dict = {"VALID_BODY_MACHINE_LEARNING_DETECTION": ["enable", "disable", "monitor"]}
    result = get_field_options(globals_dict, "machine-learning-detection")
    assert result == ["enable", "disable", "monitor"]
    print("✅ get_field_options - field with special chars")


# ============================================================================
# get_nested_schema tests
# ============================================================================

def test_get_nested_schema_exists():
    """Test getting nested schema."""
    result = get_nested_schema(NESTED_SCHEMAS, "members")
    assert result is not None
    assert "name" in result
    assert "status" in result
    print("✅ get_nested_schema - exists")


def test_get_nested_schema_not_exists():
    """Test getting nested schema for non-table field."""
    result = get_nested_schema(NESTED_SCHEMAS, "name")
    assert result is None
    print("✅ get_nested_schema - not exists")


# ============================================================================
# get_all_fields tests
# ============================================================================

def test_get_all_fields():
    """Test getting all field names."""
    result = get_all_fields(FIELD_TYPES)
    assert isinstance(result, list)
    assert "name" in result
    assert "status" in result
    assert "comment" in result
    assert "priority" in result
    assert "members" in result
    assert len(result) == 5
    print("✅ get_all_fields - basic")


def test_get_all_fields_empty():
    """Test getting fields from empty dict."""
    result = get_all_fields({})
    assert result == []
    print("✅ get_all_fields - empty")


# ============================================================================
# get_field_metadata tests
# ============================================================================

def test_get_field_metadata_complete():
    """Test getting complete field metadata."""
    globals_dict = get_test_globals()
    result = get_field_metadata(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS,
        REQUIRED_FIELDS,
        NESTED_SCHEMAS,
        globals_dict,
        "status"
    )
    assert result is not None
    assert result["name"] == "status"
    assert result["type"] == "option"
    assert result["description"] == "Enable or disable this feature"
    assert result["default"] == "enable"
    assert result["options"] == ["enable", "disable"]
    assert result["required"] is False
    print("✅ get_field_metadata - complete")


def test_get_field_metadata_required_field():
    """Test getting metadata for required field."""
    globals_dict = get_test_globals()
    result = get_field_metadata(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS,
        REQUIRED_FIELDS,
        NESTED_SCHEMAS,
        globals_dict,
        "name"
    )
    assert result is not None
    assert result["required"] is True
    assert "constraints" in result
    print("✅ get_field_metadata - required field")


def test_get_field_metadata_with_nested():
    """Test getting metadata for table field with nested schema."""
    globals_dict = get_test_globals()
    result = get_field_metadata(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS,
        REQUIRED_FIELDS,
        NESTED_SCHEMAS,
        globals_dict,
        "members"
    )
    assert result is not None
    assert result["type"] == "table"
    assert "nested_schema" in result
    print("✅ get_field_metadata - with nested schema")


def test_get_field_metadata_not_exists():
    """Test getting metadata for non-existing field."""
    globals_dict = get_test_globals()
    result = get_field_metadata(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS,
        REQUIRED_FIELDS,
        NESTED_SCHEMAS,
        globals_dict,
        "unknown"
    )
    assert result is None
    print("✅ get_field_metadata - non-existing field")


# ============================================================================
# validate_field_value tests
# ============================================================================

def test_validate_field_value_enum_valid():
    """Test validating valid enum value."""
    globals_dict = get_test_globals()
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "status",
        "enable"
    )
    assert is_valid is True
    assert error is None
    print("✅ validate_field_value - valid enum")


def test_validate_field_value_enum_invalid():
    """Test validating invalid enum value."""
    globals_dict = get_test_globals()
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "status",
        "invalid"
    )
    assert is_valid is False
    assert error is not None
    assert "Invalid value" in error
    assert "enable" in error
    assert "disable" in error
    print("✅ validate_field_value - invalid enum")


def test_validate_field_value_integer_valid():
    """Test validating valid integer value."""
    globals_dict = get_test_globals()
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "priority",
        100
    )
    assert is_valid is True
    assert error is None
    print("✅ validate_field_value - valid integer")


def test_validate_field_value_integer_below_min():
    """Test validating integer below minimum."""
    globals_dict = get_test_globals()
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "priority",
        -1
    )
    assert is_valid is False
    assert error is not None
    assert "below minimum" in error
    print("✅ validate_field_value - integer below min")


def test_validate_field_value_integer_above_max():
    """Test validating integer above maximum."""
    globals_dict = get_test_globals()
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "priority",
        300
    )
    assert is_valid is False
    assert error is not None
    assert "exceeds maximum" in error
    print("✅ validate_field_value - integer above max")


def test_validate_field_value_integer_wrong_type():
    """Test validating non-integer for integer field."""
    globals_dict = get_test_globals()
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "priority",
        "not an int"
    )
    assert is_valid is False
    assert error is not None
    assert "must be an integer" in error
    print("✅ validate_field_value - integer wrong type")


def test_validate_field_value_string_valid():
    """Test validating valid string value."""
    globals_dict = get_test_globals()
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "name",
        "valid-name"
    )
    assert is_valid is True
    assert error is None
    print("✅ validate_field_value - valid string")


def test_validate_field_value_string_too_long():
    """Test validating string exceeding max length."""
    globals_dict = get_test_globals()
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "name",
        "x" * 100  # Exceeds 63 char limit
    )
    assert is_valid is False
    assert error is not None
    assert "exceeds maximum" in error
    print("✅ validate_field_value - string too long")


def test_validate_field_value_string_wrong_type():
    """Test validating non-string for string field."""
    globals_dict = get_test_globals()
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "name",
        12345
    )
    assert is_valid is False
    assert error is not None
    assert "must be a string" in error
    print("✅ validate_field_value - string wrong type")


def test_validate_field_value_unknown_field():
    """Test validating value for unknown field."""
    globals_dict = get_test_globals()
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "unknown_field",
        "value"
    )
    assert is_valid is False
    assert error is not None
    assert "Unknown field" in error
    print("✅ validate_field_value - unknown field")


def test_validate_field_value_no_constraints():
    """Test validating field without constraints."""
    # members field has no constraints
    globals_dict = get_test_globals()
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "members",
        [{"name": "test"}]
    )
    assert is_valid is True
    assert error is None
    print("✅ validate_field_value - no constraints")


def test_validate_field_value_integer_at_boundary():
    """Test validating integer at boundary values."""
    globals_dict = get_test_globals()
    
    # Test min boundary
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "priority",
        0
    )
    assert is_valid is True
    
    # Test max boundary
    is_valid, error = validate_field_value(
        FIELD_TYPES,
        FIELD_DESCRIPTIONS,
        FIELD_CONSTRAINTS,
        globals_dict,
        "priority",
        255
    )
    assert is_valid is True
    print("✅ validate_field_value - integer at boundaries")


def run_all_tests():
    """Run all metadata tests."""
    print("\n" + "=" * 60)
    print("METADATA FUNCTION TESTS")
    print("=" * 60 + "\n")

    # get_field_description tests
    test_get_field_description_exists()
    test_get_field_description_not_exists()

    # get_field_type tests
    test_get_field_type_string()
    test_get_field_type_option()
    test_get_field_type_integer()
    test_get_field_type_table()
    test_get_field_type_not_exists()

    # get_field_constraints tests
    test_get_field_constraints_string()
    test_get_field_constraints_integer()
    test_get_field_constraints_not_exists()

    # get_field_default tests
    test_get_field_default_exists()
    test_get_field_default_zero()
    test_get_field_default_not_exists()

    # get_field_options tests
    test_get_field_options_exists()
    test_get_field_options_not_exists()
    test_get_field_options_with_special_chars()

    # get_nested_schema tests
    test_get_nested_schema_exists()
    test_get_nested_schema_not_exists()

    # get_all_fields tests
    test_get_all_fields()
    test_get_all_fields_empty()

    # get_field_metadata tests
    test_get_field_metadata_complete()
    test_get_field_metadata_required_field()
    test_get_field_metadata_with_nested()
    test_get_field_metadata_not_exists()

    # validate_field_value tests
    test_validate_field_value_enum_valid()
    test_validate_field_value_enum_invalid()
    test_validate_field_value_integer_valid()
    test_validate_field_value_integer_below_min()
    test_validate_field_value_integer_above_max()
    test_validate_field_value_integer_wrong_type()
    test_validate_field_value_string_valid()
    test_validate_field_value_string_too_long()
    test_validate_field_value_string_wrong_type()
    test_validate_field_value_unknown_field()
    test_validate_field_value_no_constraints()
    test_validate_field_value_integer_at_boundary()

    print("\n" + "=" * 60)
    print("ALL METADATA TESTS PASSED!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_tests()
