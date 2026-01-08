"""Validation helpers for switch_controller/ptp/profile - Auto-generated"""

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
    "name",  # Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "description": "",
    "mode": "transparent-e2e",
    "ptp-profile": "C37.238-2017",
    "transport": "l2-mcast",
    "domain": 254,
    "pdelay-req-interval": "1sec",
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
    "name": "string",  # Profile name.
    "description": "string",  # Description.
    "mode": "option",  # Select PTP mode.
    "ptp-profile": "option",  # Configure PTP power profile.
    "transport": "option",  # Configure PTP transport mode.
    "domain": "integer",  # Configure PTP domain value (0 - 255, default = 254).
    "pdelay-req-interval": "option",  # Configure PTP peer delay request interval.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "description": "Description.",
    "mode": "Select PTP mode.",
    "ptp-profile": "Configure PTP power profile.",
    "transport": "Configure PTP transport mode.",
    "domain": "Configure PTP domain value (0 - 255, default = 254).",
    "pdelay-req-interval": "Configure PTP peer delay request interval.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
    "description": {"type": "string", "max_length": 63},
    "domain": {"type": "integer", "min": 0, "max": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_MODE = [
    "transparent-e2e",
    "transparent-p2p",
]
VALID_BODY_PTP_PROFILE = [
    "C37.238-2017",
]
VALID_BODY_TRANSPORT = [
    "l2-mcast",
]
VALID_BODY_PDELAY_REQ_INTERVAL = [
    "1sec",
    "2sec",
    "4sec",
    "8sec",
    "16sec",
    "32sec",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_ptp_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/ptp/profile."""
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


def validate_switch_controller_ptp_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/ptp/profile object."""
    # Step 1: Validate required fields using central function
    is_valid, error = _validate_required_fields(
        payload,
        REQUIRED_FIELDS,
        FIELD_DESCRIPTIONS
    )
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values using central function
    if "mode" in payload:
        is_valid, error = _validate_enum_field(
            "mode",
            payload["mode"],
            VALID_BODY_MODE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "ptp-profile" in payload:
        is_valid, error = _validate_enum_field(
            "ptp-profile",
            payload["ptp-profile"],
            VALID_BODY_PTP_PROFILE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "transport" in payload:
        is_valid, error = _validate_enum_field(
            "transport",
            payload["transport"],
            VALID_BODY_TRANSPORT,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "pdelay-req-interval" in payload:
        is_valid, error = _validate_enum_field(
            "pdelay-req-interval",
            payload["pdelay-req-interval"],
            VALID_BODY_PDELAY_REQ_INTERVAL,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_ptp_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/ptp/profile."""
    # Validate enum values using central function
    if "mode" in payload:
        is_valid, error = _validate_enum_field(
            "mode",
            payload["mode"],
            VALID_BODY_MODE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "ptp-profile" in payload:
        is_valid, error = _validate_enum_field(
            "ptp-profile",
            payload["ptp-profile"],
            VALID_BODY_PTP_PROFILE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "transport" in payload:
        is_valid, error = _validate_enum_field(
            "transport",
            payload["transport"],
            VALID_BODY_TRANSPORT,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "pdelay-req-interval" in payload:
        is_valid, error = _validate_enum_field(
            "pdelay-req-interval",
            payload["pdelay-req-interval"],
            VALID_BODY_PDELAY_REQ_INTERVAL,
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
    "endpoint": "switch_controller/ptp/profile",
    "category": "cmdb",
    "api_path": "switch-controller.ptp/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Global PTP profile.",
    "total_fields": 7,
    "required_fields_count": 1,
    "fields_with_defaults_count": 7,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
