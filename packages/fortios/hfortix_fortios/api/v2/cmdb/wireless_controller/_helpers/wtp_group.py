"""Validation helpers for wireless_controller/wtp_group - Auto-generated"""

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
    "name": "",
    "platform-type": "",
    "ble-major-id": 0,
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
    "name": "string",  # WTP group name.
    "platform-type": "option",  # FortiAP models to define the WTP group platform type.
    "ble-major-id": "integer",  # Override BLE Major ID.
    "wtps": "string",  # WTP list.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "WTP group name.",
    "platform-type": "FortiAP models to define the WTP group platform type.",
    "ble-major-id": "Override BLE Major ID.",
    "wtps": "WTP list.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "ble-major-id": {"type": "integer", "min": 0, "max": 65535},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "wtps": {
        "wtp-id": {
            "type": "string",
            "help": "WTP ID.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_PLATFORM_TYPE = [
    "AP-11N",  # Default 11n AP.
    "C24JE",  # FAPC24JE.
    "421E",  # FAP421E.
    "423E",  # FAP423E.
    "221E",  # FAP221E.
    "222E",  # FAP222E.
    "223E",  # FAP223E.
    "224E",  # FAP224E.
    "231E",  # FAP231E.
    "321E",  # FAP321E.
    "431F",  # FAP431F.
    "431FL",  # FAP431FL.
    "432F",  # FAP432F.
    "432FR",  # FAP432FR.
    "433F",  # FAP433F.
    "433FL",  # FAP433FL.
    "231F",  # FAP231F.
    "231FL",  # FAP231FL.
    "234F",  # FAP234F.
    "23JF",  # FAP23JF.
    "831F",  # FAP831F.
    "231G",  # FAP231G.
    "233G",  # FAP233G.
    "234G",  # FAP234G.
    "431G",  # FAP431G.
    "432G",  # FAP432G.
    "433G",  # FAP433G.
    "231K",  # FAP231K.
    "231KD",  # FAP231KD.
    "23JK",  # FAP23JK.
    "222KL",  # FAP222KL.
    "241K",  # FAP241K.
    "243K",  # FAP243K.
    "244K",  # FAP244K.
    "441K",  # FAP441K.
    "432K",  # FAP432K.
    "443K",  # FAP443K.
    "U421E",  # FAPU421EV.
    "U422EV",  # FAPU422EV.
    "U423E",  # FAPU423EV.
    "U221EV",  # FAPU221EV.
    "U223EV",  # FAPU223EV.
    "U24JEV",  # FAPU24JEV.
    "U321EV",  # FAPU321EV.
    "U323EV",  # FAPU323EV.
    "U431F",  # FAPU431F.
    "U433F",  # FAPU433F.
    "U231F",  # FAPU231F.
    "U234F",  # FAPU234F.
    "U432F",  # FAPU432F.
    "U231G",  # FAPU231G.
    "MVP",  # FAP MVP.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_wtp_group_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for wireless_controller/wtp_group."""
    # Validate query parameters if present
    if "action" in params:
        value = params.get("action")
        if value and value not in VALID_QUERY_ACTION:
            return (
                False,
                f"Invalid query parameter 'action'='{value}'. Must be one of: {', '.join(VALID_QUERY_ACTION)}",
            )

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_required_fields(payload: dict) -> tuple[bool, str | None]:
    """Validate required fields for wireless_controller/wtp_group."""
    # Check always-required fields
    missing_fields = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            missing_fields.append(field)
    
    if missing_fields:
        # Build enhanced error message
        error_parts = [f"Missing required field(s): {', '.join(missing_fields)}"]
        
        # Add descriptions for first few missing fields
        for field in missing_fields[:3]:
            desc = FIELD_DESCRIPTIONS.get(field)
            if desc:
                error_parts.append(f"  • {field}: {desc}")
        
        if len(missing_fields) > 3:
            error_parts.append(f"  ... and {len(missing_fields) - 3} more")
        
        return (False, "\n".join(error_parts))

    return (True, None)


def validate_wireless_controller_wtp_group_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new wireless_controller/wtp_group object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "platform-type" in payload:
        value = payload["platform-type"]
        if value not in VALID_BODY_PLATFORM_TYPE:
            desc = FIELD_DESCRIPTIONS.get("platform-type", "")
            error_msg = f"Invalid value for 'platform-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PLATFORM_TYPE)}"
            error_msg += f"\n  → Example: platform-type='{{ VALID_BODY_PLATFORM_TYPE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_wtp_group_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update wireless_controller/wtp_group."""
    # Step 1: Validate enum values
    if "platform-type" in payload:
        value = payload["platform-type"]
        if value not in VALID_BODY_PLATFORM_TYPE:
            return (
                False,
                f"Invalid value for 'platform-type'='{value}'. Must be one of: {', '.join(VALID_BODY_PLATFORM_TYPE)}",
            )

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
    "endpoint": "wireless_controller/wtp_group",
    "category": "cmdb",
    "api_path": "wireless-controller/wtp-group",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure WTP groups.",
    "total_fields": 4,
    "required_fields_count": 0,
    "fields_with_defaults_count": 3,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
