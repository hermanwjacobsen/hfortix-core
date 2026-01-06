"""Validation helpers for switch_controller/system - Auto-generated"""

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
    "parallel-process-override": "disable",
    "parallel-process": 1,
    "data-sync-interval": 60,
    "iot-weight-threshold": 1,
    "iot-scan-interval": 60,
    "iot-holdoff": 5,
    "iot-mac-idle": 1440,
    "nac-periodic-interval": 60,
    "dynamic-periodic-interval": 60,
    "tunnel-mode": "compatible",
    "caputp-echo-interval": 30,
    "caputp-max-retransmit": 5,
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
    "parallel-process-override": "option",  # Enable/disable parallel process override.
    "parallel-process": "integer",  # Maximum number of parallel processes.
    "data-sync-interval": "integer",  # Time interval between collection of switch data (30 - 1800 s
    "iot-weight-threshold": "integer",  # MAC entry's confidence value. Value is re-queried when below
    "iot-scan-interval": "integer",  # IoT scan interval (2 - 10080 mins, default = 60 mins, 0 = di
    "iot-holdoff": "integer",  # MAC entry's creation time. Time must be greater than this va
    "iot-mac-idle": "integer",  # MAC entry's idle time. MAC entry is removed after this value
    "nac-periodic-interval": "integer",  # Periodic time interval to run NAC engine (5 - 180 sec, defau
    "dynamic-periodic-interval": "integer",  # Periodic time interval to run Dynamic port policy engine (5 
    "tunnel-mode": "option",  # Compatible/strict tunnel mode.
    "caputp-echo-interval": "integer",  # Echo interval for the caputp echo requests from swtp.
    "caputp-max-retransmit": "integer",  # Maximum retransmission count for the caputp tunnel packets.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "parallel-process-override": "Enable/disable parallel process override.",
    "parallel-process": "Maximum number of parallel processes.",
    "data-sync-interval": "Time interval between collection of switch data (30 - 1800 sec, default = 60, 0 = disable).",
    "iot-weight-threshold": "MAC entry's confidence value. Value is re-queried when below this value (default = 1, 0 = disable).",
    "iot-scan-interval": "IoT scan interval (2 - 10080 mins, default = 60 mins, 0 = disable).",
    "iot-holdoff": "MAC entry's creation time. Time must be greater than this value for an entry to be created (0 - 10080 mins, default = 5 mins).",
    "iot-mac-idle": "MAC entry's idle time. MAC entry is removed after this value (0 - 10080 mins, default = 1440 mins).",
    "nac-periodic-interval": "Periodic time interval to run NAC engine (5 - 180 sec, default = 60).",
    "dynamic-periodic-interval": "Periodic time interval to run Dynamic port policy engine (5 - 180 sec, default = 60).",
    "tunnel-mode": "Compatible/strict tunnel mode.",
    "caputp-echo-interval": "Echo interval for the caputp echo requests from swtp.",
    "caputp-max-retransmit": "Maximum retransmission count for the caputp tunnel packets.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "parallel-process": {"type": "integer", "min": 1, "max": 24},
    "data-sync-interval": {"type": "integer", "min": 30, "max": 1800},
    "iot-weight-threshold": {"type": "integer", "min": 0, "max": 255},
    "iot-scan-interval": {"type": "integer", "min": 2, "max": 10080},
    "iot-holdoff": {"type": "integer", "min": 0, "max": 10080},
    "iot-mac-idle": {"type": "integer", "min": 0, "max": 10080},
    "nac-periodic-interval": {"type": "integer", "min": 5, "max": 180},
    "dynamic-periodic-interval": {"type": "integer", "min": 5, "max": 180},
    "caputp-echo-interval": {"type": "integer", "min": 8, "max": 600},
    "caputp-max-retransmit": {"type": "integer", "min": 0, "max": 64},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_PARALLEL_PROCESS_OVERRIDE = [
    "disable",  # Disable maximum parallel process override.
    "enable",  # Enable maximum parallel process override.
]
VALID_BODY_TUNNEL_MODE = [
    "compatible",  # Least restrictive. Supports the lowest levels of security but highest compatibility between all FortiSwitch and FortiGate devices. 3rd party certificates permitted.
    "moderate",  # Moderate level of security. 3rd party certificates permitted.
    "strict",  # Highest level of security requirements. If enabled, the FortiGate device follows the same security mode requirements as in FIPS/CC mode.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_system_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/system."""
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
    """Validate required fields for switch_controller/system."""
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


def validate_switch_controller_system_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/system object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "parallel-process-override" in payload:
        value = payload["parallel-process-override"]
        if value not in VALID_BODY_PARALLEL_PROCESS_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("parallel-process-override", "")
            error_msg = f"Invalid value for 'parallel-process-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PARALLEL_PROCESS_OVERRIDE)}"
            error_msg += f"\n  → Example: parallel-process-override='{{ VALID_BODY_PARALLEL_PROCESS_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "tunnel-mode" in payload:
        value = payload["tunnel-mode"]
        if value not in VALID_BODY_TUNNEL_MODE:
            desc = FIELD_DESCRIPTIONS.get("tunnel-mode", "")
            error_msg = f"Invalid value for 'tunnel-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TUNNEL_MODE)}"
            error_msg += f"\n  → Example: tunnel-mode='{{ VALID_BODY_TUNNEL_MODE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_system_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/system."""
    # Step 1: Validate enum values
    if "parallel-process-override" in payload:
        value = payload["parallel-process-override"]
        if value not in VALID_BODY_PARALLEL_PROCESS_OVERRIDE:
            return (
                False,
                f"Invalid value for 'parallel-process-override'='{value}'. Must be one of: {', '.join(VALID_BODY_PARALLEL_PROCESS_OVERRIDE)}",
            )
    if "tunnel-mode" in payload:
        value = payload["tunnel-mode"]
        if value not in VALID_BODY_TUNNEL_MODE:
            return (
                False,
                f"Invalid value for 'tunnel-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_TUNNEL_MODE)}",
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
    "endpoint": "switch_controller/system",
    "category": "cmdb",
    "api_path": "switch-controller/system",
    "help": "Configure system-wide switch controller settings.",
    "total_fields": 12,
    "required_fields_count": 0,
    "fields_with_defaults_count": 12,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
