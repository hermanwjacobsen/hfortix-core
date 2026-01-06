"""Validation helpers for system/ptp - Auto-generated"""

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
    "interface",  # PTP client will reply through this interface.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "status": "disable",
    "mode": "multicast",
    "delay-mechanism": "E2E",
    "request-interval": 1,
    "interface": "",
    "server-mode": "disable",
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
    "status": "option",  # Enable/disable setting the FortiGate system time by synchron
    "mode": "option",  # Multicast transmission or hybrid transmission.
    "delay-mechanism": "option",  # End to end delay detection or peer to peer delay detection.
    "request-interval": "integer",  # The delay request value is the logarithmic mean interval in 
    "interface": "string",  # PTP client will reply through this interface.
    "server-mode": "option",  # Enable/disable FortiGate PTP server mode. Your FortiGate bec
    "server-interface": "string",  # FortiGate interface(s) with PTP server mode enabled. Devices
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable setting the FortiGate system time by synchronizing with an PTP Server.",
    "mode": "Multicast transmission or hybrid transmission.",
    "delay-mechanism": "End to end delay detection or peer to peer delay detection.",
    "request-interval": "The delay request value is the logarithmic mean interval in seconds between the delay request messages sent by the slave to the master.",
    "interface": "PTP client will reply through this interface.",
    "server-mode": "Enable/disable FortiGate PTP server mode. Your FortiGate becomes an PTP server for other devices on your network.",
    "server-interface": "FortiGate interface(s) with PTP server mode enabled. Devices on your network can contact these interfaces for PTP services.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "request-interval": {"type": "integer", "min": 1, "max": 6},
    "interface": {"type": "string", "max_length": 15},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "server-interface": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "server-interface-name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "delay-mechanism": {
            "type": "option",
            "help": "End to end delay detection or peer to peer delay detection.",
            "default": "E2E",
            "options": [{"help": "End to end delay detection.", "label": "E2E", "name": "E2E"}, {"help": "Peer to peer delay detection.", "label": "P2P", "name": "P2P"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable synchronization with PTP Server.
    "disable",  # Disable synchronization with PTP Server.
]
VALID_BODY_MODE = [
    "multicast",  # Send PTP packets with multicast.
    "hybrid",  # Send PTP packets with unicast and multicast.
]
VALID_BODY_DELAY_MECHANISM = [
    "E2E",  # End to end delay detection.
    "P2P",  # Peer to peer delay detection.
]
VALID_BODY_SERVER_MODE = [
    "enable",  # Enable FortiGate PTP server mode.
    "disable",  # Disable FortiGate PTP server mode.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_ptp_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/ptp."""
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
    """Validate required fields for system/ptp."""
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


def validate_system_ptp_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/ptp object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            desc = FIELD_DESCRIPTIONS.get("status", "")
            error_msg = f"Invalid value for 'status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STATUS)}"
            error_msg += f"\n  → Example: status='{{ VALID_BODY_STATUS[0] }}'"
            return (False, error_msg)
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            desc = FIELD_DESCRIPTIONS.get("mode", "")
            error_msg = f"Invalid value for 'mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MODE)}"
            error_msg += f"\n  → Example: mode='{{ VALID_BODY_MODE[0] }}'"
            return (False, error_msg)
    if "delay-mechanism" in payload:
        value = payload["delay-mechanism"]
        if value not in VALID_BODY_DELAY_MECHANISM:
            desc = FIELD_DESCRIPTIONS.get("delay-mechanism", "")
            error_msg = f"Invalid value for 'delay-mechanism': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DELAY_MECHANISM)}"
            error_msg += f"\n  → Example: delay-mechanism='{{ VALID_BODY_DELAY_MECHANISM[0] }}'"
            return (False, error_msg)
    if "server-mode" in payload:
        value = payload["server-mode"]
        if value not in VALID_BODY_SERVER_MODE:
            desc = FIELD_DESCRIPTIONS.get("server-mode", "")
            error_msg = f"Invalid value for 'server-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_MODE)}"
            error_msg += f"\n  → Example: server-mode='{{ VALID_BODY_SERVER_MODE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_ptp_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/ptp."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid value for 'mode'='{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )
    if "delay-mechanism" in payload:
        value = payload["delay-mechanism"]
        if value not in VALID_BODY_DELAY_MECHANISM:
            return (
                False,
                f"Invalid value for 'delay-mechanism'='{value}'. Must be one of: {', '.join(VALID_BODY_DELAY_MECHANISM)}",
            )
    if "server-mode" in payload:
        value = payload["server-mode"]
        if value not in VALID_BODY_SERVER_MODE:
            return (
                False,
                f"Invalid value for 'server-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_MODE)}",
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
    "endpoint": "system/ptp",
    "category": "cmdb",
    "api_path": "system/ptp",
    "help": "Configure system PTP information.",
    "total_fields": 7,
    "required_fields_count": 1,
    "fields_with_defaults_count": 6,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
