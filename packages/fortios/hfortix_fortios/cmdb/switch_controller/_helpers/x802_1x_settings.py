"""Validation helpers for switch_controller/x802_1x_settings - Auto-generated"""

from typing import Any, TypedDict, NotRequired, Literal

# Import common validators from central _helpers module
from hfortix_fortios._helpers import (
    validate_enable_disable,
    validate_integer_range,
    validate_string_length,
    validate_port_number,
    validate_ip_address,
    validate_ipv6_address,
    validate_mac_address,
)

# Import central validation functions (avoid duplication across 1,062 files)
from hfortix_fortios._helpers.validation import (
    validate_required_fields as _validate_required_fields,
    validate_enum_field as _validate_enum_field,
    validate_query_parameter as _validate_query_parameter,
)

# ============================================================================
# Required Fields Validation
# Auto-generated from schema
# ============================================================================

# ⚠️  IMPORTANT: FortiOS schemas have known issues with required field marking:

# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "link-down-auth": "set-unauth",
    "reauth-period": 60,
    "max-reauth-attempt": 3,
    "tx-period": 30,
    "mab-reauth": "disable",
    "mac-username-delimiter": "hyphen",
    "mac-password-delimiter": "hyphen",
    "mac-calling-station-delimiter": "hyphen",
    "mac-called-station-delimiter": "hyphen",
    "mac-case": "lowercase",
}

# ============================================================================
# Deprecated Fields
# Auto-generated from schema - warns users about deprecated fields
# ============================================================================

# Deprecated fields with migration guidance
DEPRECATED_FIELDS = {
}

# ============================================================================
# Field Metadata (Type Information & Descriptions)
# Auto-generated from schema - use for IDE autocomplete and documentation
# ============================================================================

# Field types mapping
FIELD_TYPES = {
    "link-down-auth": "option",  # Interface-reauthentication state to set if a link is down.
    "reauth-period": "integer",  # Period of time to allow for reauthentication (1 - 1440 sec, 
    "max-reauth-attempt": "integer",  # Maximum number of authentication attempts (0 - 15, default =
    "tx-period": "integer",  # 802.1X Tx period (seconds, default=30).
    "mab-reauth": "option",  # Enable/disable MAB re-authentication.
    "mac-username-delimiter": "option",  # MAC authentication username delimiter (default = hyphen).
    "mac-password-delimiter": "option",  # MAC authentication password delimiter (default = hyphen).
    "mac-calling-station-delimiter": "option",  # MAC calling station delimiter (default = hyphen).
    "mac-called-station-delimiter": "option",  # MAC called station delimiter (default = hyphen).
    "mac-case": "option",  # MAC case (default = lowercase).
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "link-down-auth": "Interface-reauthentication state to set if a link is down.",
    "reauth-period": "Period of time to allow for reauthentication (1 - 1440 sec, default = 60, 0 = disable reauthentication).",
    "max-reauth-attempt": "Maximum number of authentication attempts (0 - 15, default = 3).",
    "tx-period": "802.1X Tx period (seconds, default=30).",
    "mab-reauth": "Enable/disable MAB re-authentication.",
    "mac-username-delimiter": "MAC authentication username delimiter (default = hyphen).",
    "mac-password-delimiter": "MAC authentication password delimiter (default = hyphen).",
    "mac-calling-station-delimiter": "MAC calling station delimiter (default = hyphen).",
    "mac-called-station-delimiter": "MAC called station delimiter (default = hyphen).",
    "mac-case": "MAC case (default = lowercase).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "reauth-period": {"type": "integer", "min": 0, "max": 1440},
    "max-reauth-attempt": {"type": "integer", "min": 0, "max": 15},
    "tx-period": {"type": "integer", "min": 12, "max": 60},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_LINK_DOWN_AUTH = [
    "set-unauth",
    "no-action",
]
VALID_BODY_MAB_REAUTH = [
    "disable",
    "enable",
]
VALID_BODY_MAC_USERNAME_DELIMITER = [
    "colon",
    "hyphen",
    "none",
    "single-hyphen",
]
VALID_BODY_MAC_PASSWORD_DELIMITER = [
    "colon",
    "hyphen",
    "none",
    "single-hyphen",
]
VALID_BODY_MAC_CALLING_STATION_DELIMITER = [
    "colon",
    "hyphen",
    "none",
    "single-hyphen",
]
VALID_BODY_MAC_CALLED_STATION_DELIMITER = [
    "colon",
    "hyphen",
    "none",
    "single-hyphen",
]
VALID_BODY_MAC_CASE = [
    "lowercase",
    "uppercase",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_x802_1x_settings_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/x802_1x_settings."""
    # Validate query parameters using central function
    if "action" in params:
        is_valid, error = _validate_query_parameter(
            "action",
            params.get("action"),
            VALID_QUERY_ACTION
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_switch_controller_x802_1x_settings_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/x802_1x_settings object."""
    # Step 1: Validate required fields using central function
    is_valid, error = _validate_required_fields(
        payload,
        REQUIRED_FIELDS,
        FIELD_DESCRIPTIONS
    )
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values using central function
    if "link-down-auth" in payload:
        is_valid, error = _validate_enum_field(
            "link-down-auth",
            payload["link-down-auth"],
            VALID_BODY_LINK_DOWN_AUTH,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mab-reauth" in payload:
        is_valid, error = _validate_enum_field(
            "mab-reauth",
            payload["mab-reauth"],
            VALID_BODY_MAB_REAUTH,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mac-username-delimiter" in payload:
        is_valid, error = _validate_enum_field(
            "mac-username-delimiter",
            payload["mac-username-delimiter"],
            VALID_BODY_MAC_USERNAME_DELIMITER,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mac-password-delimiter" in payload:
        is_valid, error = _validate_enum_field(
            "mac-password-delimiter",
            payload["mac-password-delimiter"],
            VALID_BODY_MAC_PASSWORD_DELIMITER,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mac-calling-station-delimiter" in payload:
        is_valid, error = _validate_enum_field(
            "mac-calling-station-delimiter",
            payload["mac-calling-station-delimiter"],
            VALID_BODY_MAC_CALLING_STATION_DELIMITER,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mac-called-station-delimiter" in payload:
        is_valid, error = _validate_enum_field(
            "mac-called-station-delimiter",
            payload["mac-called-station-delimiter"],
            VALID_BODY_MAC_CALLED_STATION_DELIMITER,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mac-case" in payload:
        is_valid, error = _validate_enum_field(
            "mac-case",
            payload["mac-case"],
            VALID_BODY_MAC_CASE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_x802_1x_settings_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/x802_1x_settings."""
    # Validate enum values using central function
    if "link-down-auth" in payload:
        is_valid, error = _validate_enum_field(
            "link-down-auth",
            payload["link-down-auth"],
            VALID_BODY_LINK_DOWN_AUTH,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mab-reauth" in payload:
        is_valid, error = _validate_enum_field(
            "mab-reauth",
            payload["mab-reauth"],
            VALID_BODY_MAB_REAUTH,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mac-username-delimiter" in payload:
        is_valid, error = _validate_enum_field(
            "mac-username-delimiter",
            payload["mac-username-delimiter"],
            VALID_BODY_MAC_USERNAME_DELIMITER,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mac-password-delimiter" in payload:
        is_valid, error = _validate_enum_field(
            "mac-password-delimiter",
            payload["mac-password-delimiter"],
            VALID_BODY_MAC_PASSWORD_DELIMITER,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mac-calling-station-delimiter" in payload:
        is_valid, error = _validate_enum_field(
            "mac-calling-station-delimiter",
            payload["mac-calling-station-delimiter"],
            VALID_BODY_MAC_CALLING_STATION_DELIMITER,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mac-called-station-delimiter" in payload:
        is_valid, error = _validate_enum_field(
            "mac-called-station-delimiter",
            payload["mac-called-station-delimiter"],
            VALID_BODY_MAC_CALLED_STATION_DELIMITER,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "mac-case" in payload:
        is_valid, error = _validate_enum_field(
            "mac-case",
            payload["mac-case"],
            VALID_BODY_MAC_CASE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Imported from central module to avoid duplication across 1,062 files
# ============================================================================

from hfortix_fortios._helpers.metadata import (
    get_field_description as _get_field_description,
    get_field_type as _get_field_type,
    get_field_constraints as _get_field_constraints,
    get_field_default as _get_field_default,
    get_field_options as _get_field_options,
    get_nested_schema as _get_nested_schema,
    get_all_fields as _get_all_fields,
    get_field_metadata as _get_field_metadata,
    validate_field_value as _validate_field_value,
)

# Wrapper functions that bind module-specific data to central functions
def get_field_description(field_name: str) -> str | None:
    """Get description/help text for a field."""
    return _get_field_description(FIELD_DESCRIPTIONS, field_name)

def get_field_type(field_name: str) -> str | None:
    """Get the type of a field."""
    return _get_field_type(FIELD_TYPES, field_name)

def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """Get constraints for a field (min/max values, string length)."""
    return _get_field_constraints(FIELD_CONSTRAINTS, field_name)

def get_field_default(field_name: str) -> Any | None:
    """Get default value for a field."""
    return _get_field_default(FIELDS_WITH_DEFAULTS, field_name)

def get_field_options(field_name: str) -> list[str] | None:
    """Get valid enum options for a field."""
    return _get_field_options(globals(), field_name)

def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """Get schema for nested table/list fields."""
    return _get_nested_schema(NESTED_SCHEMAS, field_name)

def get_all_fields() -> list[str]:
    """Get list of all field names."""
    return _get_all_fields(FIELD_TYPES)

def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """Get complete metadata for a field (type, description, constraints, defaults, options)."""
    return _get_field_metadata(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS, REQUIRED_FIELDS, NESTED_SCHEMAS,
        globals(), field_name
    )

def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """Validate a single field value against its constraints."""
    return _validate_field_value(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        globals(), field_name, value
    )


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "switch_controller/x802_1x_settings",
    "category": "cmdb",
    "api_path": "switch-controller/802-1X-settings",
    "help": "Configure global 802.1X settings.",
    "total_fields": 10,
    "required_fields_count": 0,
    "fields_with_defaults_count": 10,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
