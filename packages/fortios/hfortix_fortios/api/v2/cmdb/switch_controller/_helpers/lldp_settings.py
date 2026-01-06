"""Validation helpers for switch_controller/lldp_settings - Auto-generated"""

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
    "tx-hold": 4,
    "tx-interval": 30,
    "fast-start-interval": 2,
    "management-interface": "internal",
    "device-detection": "enable",
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
    "tx-hold": "integer",  # Number of tx-intervals before local LLDP data expires (1 - 1
    "tx-interval": "integer",  # Frequency of LLDP PDU transmission from FortiSwitch (5 - 409
    "fast-start-interval": "integer",  # Frequency of LLDP PDU transmission from FortiSwitch for the 
    "management-interface": "option",  # Primary management interface to be advertised in LLDP and CD
    "device-detection": "option",  # Enable/disable dynamic detection of LLDP neighbor devices fo
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "tx-hold": "Number of tx-intervals before local LLDP data expires (1 - 16, default = 4). Packet TTL is tx-hold * tx-interval.",
    "tx-interval": "Frequency of LLDP PDU transmission from FortiSwitch (5 - 4095 sec, default = 30). Packet TTL is tx-hold * tx-interval.",
    "fast-start-interval": "Frequency of LLDP PDU transmission from FortiSwitch for the first 4 packets when the link is up (2 - 5 sec, default = 2, 0 = disable fast start).",
    "management-interface": "Primary management interface to be advertised in LLDP and CDP PDUs.",
    "device-detection": "Enable/disable dynamic detection of LLDP neighbor devices for VLAN assignment.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "tx-hold": {"type": "integer", "min": 1, "max": 16},
    "tx-interval": {"type": "integer", "min": 5, "max": 4095},
    "fast-start-interval": {"type": "integer", "min": 0, "max": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_MANAGEMENT_INTERFACE = [
    "internal",  # Use internal interface.
    "mgmt",  # Use management interface.
]
VALID_BODY_DEVICE_DETECTION = [
    "disable",  # Disable dynamic detection of LLDP neighbor devices.
    "enable",  # Enable dynamic detection of LLDP neighbor devices.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_lldp_settings_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/lldp_settings."""
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
    """Validate required fields for switch_controller/lldp_settings."""
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


def validate_switch_controller_lldp_settings_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/lldp_settings object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "management-interface" in payload:
        value = payload["management-interface"]
        if value not in VALID_BODY_MANAGEMENT_INTERFACE:
            desc = FIELD_DESCRIPTIONS.get("management-interface", "")
            error_msg = f"Invalid value for 'management-interface': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MANAGEMENT_INTERFACE)}"
            error_msg += f"\n  → Example: management-interface='{{ VALID_BODY_MANAGEMENT_INTERFACE[0] }}'"
            return (False, error_msg)
    if "device-detection" in payload:
        value = payload["device-detection"]
        if value not in VALID_BODY_DEVICE_DETECTION:
            desc = FIELD_DESCRIPTIONS.get("device-detection", "")
            error_msg = f"Invalid value for 'device-detection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEVICE_DETECTION)}"
            error_msg += f"\n  → Example: device-detection='{{ VALID_BODY_DEVICE_DETECTION[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_lldp_settings_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/lldp_settings."""
    # Step 1: Validate enum values
    if "management-interface" in payload:
        value = payload["management-interface"]
        if value not in VALID_BODY_MANAGEMENT_INTERFACE:
            return (
                False,
                f"Invalid value for 'management-interface'='{value}'. Must be one of: {', '.join(VALID_BODY_MANAGEMENT_INTERFACE)}",
            )
    if "device-detection" in payload:
        value = payload["device-detection"]
        if value not in VALID_BODY_DEVICE_DETECTION:
            return (
                False,
                f"Invalid value for 'device-detection'='{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_DETECTION)}",
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
    "endpoint": "switch_controller/lldp_settings",
    "category": "cmdb",
    "api_path": "switch-controller/lldp-settings",
    "help": "Configure FortiSwitch LLDP settings.",
    "total_fields": 5,
    "required_fields_count": 0,
    "fields_with_defaults_count": 5,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
