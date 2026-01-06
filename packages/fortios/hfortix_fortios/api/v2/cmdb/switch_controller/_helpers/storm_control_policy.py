"""Validation helpers for switch_controller/storm_control_policy - Auto-generated"""

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
    "name",  # Storm control policy name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "description": "",
    "storm-control-mode": "global",
    "rate": 500,
    "burst-size-level": 0,
    "unknown-unicast": "disable",
    "unknown-multicast": "disable",
    "broadcast": "disable",
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
    "name": "string",  # Storm control policy name.
    "description": "string",  # Description of the storm control policy.
    "storm-control-mode": "option",  # Set Storm control mode.
    "rate": "integer",  # Threshold rate in packets per second at which storm traffic 
    "burst-size-level": "integer",  # Increase level to handle bursty traffic (0 - 4, default = 0)
    "unknown-unicast": "option",  # Enable/disable storm control to drop/allow unknown unicast t
    "unknown-multicast": "option",  # Enable/disable storm control to drop/allow unknown multicast
    "broadcast": "option",  # Enable/disable storm control to drop/allow broadcast traffic
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Storm control policy name.",
    "description": "Description of the storm control policy.",
    "storm-control-mode": "Set Storm control mode.",
    "rate": "Threshold rate in packets per second at which storm traffic is controlled in override mode (default=500, 0 to drop all).",
    "burst-size-level": "Increase level to handle bursty traffic (0 - 4, default = 0).",
    "unknown-unicast": "Enable/disable storm control to drop/allow unknown unicast traffic in override mode.",
    "unknown-multicast": "Enable/disable storm control to drop/allow unknown multicast traffic in override mode.",
    "broadcast": "Enable/disable storm control to drop/allow broadcast traffic in override mode.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
    "description": {"type": "string", "max_length": 63},
    "rate": {"type": "integer", "min": 0, "max": 10000000},
    "burst-size-level": {"type": "integer", "min": 0, "max": 4},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_STORM_CONTROL_MODE = [
    "global",  # Apply Global or switch level storm control configuration.
    "override",  # Override global and switch level storm control to use port level configuration.
    "disabled",  # Disable storm control on the port entirely overriding global and switch level storm control.
]
VALID_BODY_UNKNOWN_UNICAST = [
    "enable",  # Enable storm control for unknown unicast traffic to drop packets which exceed configured rate limits.
    "disable",  # Disable storm control for unknown unicast traffic to allow all packets.
]
VALID_BODY_UNKNOWN_MULTICAST = [
    "enable",  # Enable storm control for unknown multicast traffic to drop packets which exceed configured rate limits.
    "disable",  # Disable storm control for unknown multicast traffic to allow all packets.
]
VALID_BODY_BROADCAST = [
    "enable",  # Enable storm control for broadcast traffic to drop packets which exceed configured rate limits.
    "disable",  # Disable storm control for broadcast traffic to allow all packets.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_storm_control_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/storm_control_policy."""
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
    """Validate required fields for switch_controller/storm_control_policy."""
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


def validate_switch_controller_storm_control_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/storm_control_policy object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "storm-control-mode" in payload:
        value = payload["storm-control-mode"]
        if value not in VALID_BODY_STORM_CONTROL_MODE:
            desc = FIELD_DESCRIPTIONS.get("storm-control-mode", "")
            error_msg = f"Invalid value for 'storm-control-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STORM_CONTROL_MODE)}"
            error_msg += f"\n  → Example: storm-control-mode='{{ VALID_BODY_STORM_CONTROL_MODE[0] }}'"
            return (False, error_msg)
    if "unknown-unicast" in payload:
        value = payload["unknown-unicast"]
        if value not in VALID_BODY_UNKNOWN_UNICAST:
            desc = FIELD_DESCRIPTIONS.get("unknown-unicast", "")
            error_msg = f"Invalid value for 'unknown-unicast': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UNKNOWN_UNICAST)}"
            error_msg += f"\n  → Example: unknown-unicast='{{ VALID_BODY_UNKNOWN_UNICAST[0] }}'"
            return (False, error_msg)
    if "unknown-multicast" in payload:
        value = payload["unknown-multicast"]
        if value not in VALID_BODY_UNKNOWN_MULTICAST:
            desc = FIELD_DESCRIPTIONS.get("unknown-multicast", "")
            error_msg = f"Invalid value for 'unknown-multicast': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UNKNOWN_MULTICAST)}"
            error_msg += f"\n  → Example: unknown-multicast='{{ VALID_BODY_UNKNOWN_MULTICAST[0] }}'"
            return (False, error_msg)
    if "broadcast" in payload:
        value = payload["broadcast"]
        if value not in VALID_BODY_BROADCAST:
            desc = FIELD_DESCRIPTIONS.get("broadcast", "")
            error_msg = f"Invalid value for 'broadcast': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BROADCAST)}"
            error_msg += f"\n  → Example: broadcast='{{ VALID_BODY_BROADCAST[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_storm_control_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/storm_control_policy."""
    # Step 1: Validate enum values
    if "storm-control-mode" in payload:
        value = payload["storm-control-mode"]
        if value not in VALID_BODY_STORM_CONTROL_MODE:
            return (
                False,
                f"Invalid value for 'storm-control-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_STORM_CONTROL_MODE)}",
            )
    if "unknown-unicast" in payload:
        value = payload["unknown-unicast"]
        if value not in VALID_BODY_UNKNOWN_UNICAST:
            return (
                False,
                f"Invalid value for 'unknown-unicast'='{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_UNICAST)}",
            )
    if "unknown-multicast" in payload:
        value = payload["unknown-multicast"]
        if value not in VALID_BODY_UNKNOWN_MULTICAST:
            return (
                False,
                f"Invalid value for 'unknown-multicast'='{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_MULTICAST)}",
            )
    if "broadcast" in payload:
        value = payload["broadcast"]
        if value not in VALID_BODY_BROADCAST:
            return (
                False,
                f"Invalid value for 'broadcast'='{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST)}",
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
    "endpoint": "switch_controller/storm_control_policy",
    "category": "cmdb",
    "api_path": "switch-controller/storm-control-policy",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure FortiSwitch storm control policy to be applied on managed-switch ports.",
    "total_fields": 8,
    "required_fields_count": 1,
    "fields_with_defaults_count": 8,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
