"""Validation helpers for switch_controller/snmp_community - Auto-generated"""

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
    "name",  # SNMP community name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "name": "",
    "status": "enable",
    "query-v1-status": "enable",
    "query-v1-port": 161,
    "query-v2c-status": "enable",
    "query-v2c-port": 161,
    "trap-v1-status": "enable",
    "trap-v1-lport": 162,
    "trap-v1-rport": 162,
    "trap-v2c-status": "enable",
    "trap-v2c-lport": 162,
    "trap-v2c-rport": 162,
    "events": "cpu-high mem-low log-full intf-ip ent-conf-change l2mac",
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
    "id": "integer",  # SNMP community ID.
    "name": "string",  # SNMP community name.
    "status": "option",  # Enable/disable this SNMP community.
    "hosts": "string",  # Configure IPv4 SNMP managers (hosts).
    "query-v1-status": "option",  # Enable/disable SNMP v1 queries.
    "query-v1-port": "integer",  # SNMP v1 query port (default = 161).
    "query-v2c-status": "option",  # Enable/disable SNMP v2c queries.
    "query-v2c-port": "integer",  # SNMP v2c query port (default = 161).
    "trap-v1-status": "option",  # Enable/disable SNMP v1 traps.
    "trap-v1-lport": "integer",  # SNMP v2c trap local port (default = 162).
    "trap-v1-rport": "integer",  # SNMP v2c trap remote port (default = 162).
    "trap-v2c-status": "option",  # Enable/disable SNMP v2c traps.
    "trap-v2c-lport": "integer",  # SNMP v2c trap local port (default = 162).
    "trap-v2c-rport": "integer",  # SNMP v2c trap remote port (default = 162).
    "events": "option",  # SNMP notifications (traps) to send.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "SNMP community ID.",
    "name": "SNMP community name.",
    "status": "Enable/disable this SNMP community.",
    "hosts": "Configure IPv4 SNMP managers (hosts).",
    "query-v1-status": "Enable/disable SNMP v1 queries.",
    "query-v1-port": "SNMP v1 query port (default = 161).",
    "query-v2c-status": "Enable/disable SNMP v2c queries.",
    "query-v2c-port": "SNMP v2c query port (default = 161).",
    "trap-v1-status": "Enable/disable SNMP v1 traps.",
    "trap-v1-lport": "SNMP v2c trap local port (default = 162).",
    "trap-v1-rport": "SNMP v2c trap remote port (default = 162).",
    "trap-v2c-status": "Enable/disable SNMP v2c traps.",
    "trap-v2c-lport": "SNMP v2c trap local port (default = 162).",
    "trap-v2c-rport": "SNMP v2c trap remote port (default = 162).",
    "events": "SNMP notifications (traps) to send.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "name": {"type": "string", "max_length": 35},
    "query-v1-port": {"type": "integer", "min": 0, "max": 65535},
    "query-v2c-port": {"type": "integer", "min": 0, "max": 65535},
    "trap-v1-lport": {"type": "integer", "min": 0, "max": 65535},
    "trap-v1-rport": {"type": "integer", "min": 0, "max": 65535},
    "trap-v2c-lport": {"type": "integer", "min": 0, "max": 65535},
    "trap-v2c-rport": {"type": "integer", "min": 0, "max": 65535},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "hosts": {
        "id": {
            "type": "integer",
            "help": "Host entry ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ip": {
            "type": "user",
            "help": "IPv4 address of the SNMP manager (host).",
            "required": True,
            "default": "",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "disable",  # Disable SNMP community.
    "enable",  # Enable SNMP community.
]
VALID_BODY_QUERY_V1_STATUS = [
    "disable",  # Disable SNMP v1 queries.
    "enable",  # Enable SNMP v1 queries.
]
VALID_BODY_QUERY_V2C_STATUS = [
    "disable",  # Disable SNMP v2c queries.
    "enable",  # Enable SNMP v2c queries.
]
VALID_BODY_TRAP_V1_STATUS = [
    "disable",  # Disable SNMP v1 traps.
    "enable",  # Enable SNMP v1 traps.
]
VALID_BODY_TRAP_V2C_STATUS = [
    "disable",  # Disable SNMP v2c traps.
    "enable",  # Enable SNMP v2c traps.
]
VALID_BODY_EVENTS = [
    "cpu-high",  # Send a trap when CPU usage too high.
    "mem-low",  # Send a trap when available memory is low.
    "log-full",  # Send a trap when log disk space becomes low.
    "intf-ip",  # Send a trap when an interface IP address is changed.
    "ent-conf-change",  # Send a trap when an entity MIB change occurs (RFC4133).
    "l2mac",  # Send a trap for Learning event (add/delete/movefrom/moveto).
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_snmp_community_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/snmp_community."""
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
    """Validate required fields for switch_controller/snmp_community."""
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


def validate_switch_controller_snmp_community_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/snmp_community object."""
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
    if "query-v1-status" in payload:
        value = payload["query-v1-status"]
        if value not in VALID_BODY_QUERY_V1_STATUS:
            desc = FIELD_DESCRIPTIONS.get("query-v1-status", "")
            error_msg = f"Invalid value for 'query-v1-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QUERY_V1_STATUS)}"
            error_msg += f"\n  → Example: query-v1-status='{{ VALID_BODY_QUERY_V1_STATUS[0] }}'"
            return (False, error_msg)
    if "query-v2c-status" in payload:
        value = payload["query-v2c-status"]
        if value not in VALID_BODY_QUERY_V2C_STATUS:
            desc = FIELD_DESCRIPTIONS.get("query-v2c-status", "")
            error_msg = f"Invalid value for 'query-v2c-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QUERY_V2C_STATUS)}"
            error_msg += f"\n  → Example: query-v2c-status='{{ VALID_BODY_QUERY_V2C_STATUS[0] }}'"
            return (False, error_msg)
    if "trap-v1-status" in payload:
        value = payload["trap-v1-status"]
        if value not in VALID_BODY_TRAP_V1_STATUS:
            desc = FIELD_DESCRIPTIONS.get("trap-v1-status", "")
            error_msg = f"Invalid value for 'trap-v1-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRAP_V1_STATUS)}"
            error_msg += f"\n  → Example: trap-v1-status='{{ VALID_BODY_TRAP_V1_STATUS[0] }}'"
            return (False, error_msg)
    if "trap-v2c-status" in payload:
        value = payload["trap-v2c-status"]
        if value not in VALID_BODY_TRAP_V2C_STATUS:
            desc = FIELD_DESCRIPTIONS.get("trap-v2c-status", "")
            error_msg = f"Invalid value for 'trap-v2c-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRAP_V2C_STATUS)}"
            error_msg += f"\n  → Example: trap-v2c-status='{{ VALID_BODY_TRAP_V2C_STATUS[0] }}'"
            return (False, error_msg)
    if "events" in payload:
        value = payload["events"]
        if value not in VALID_BODY_EVENTS:
            desc = FIELD_DESCRIPTIONS.get("events", "")
            error_msg = f"Invalid value for 'events': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EVENTS)}"
            error_msg += f"\n  → Example: events='{{ VALID_BODY_EVENTS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_snmp_community_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/snmp_community."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "query-v1-status" in payload:
        value = payload["query-v1-status"]
        if value not in VALID_BODY_QUERY_V1_STATUS:
            return (
                False,
                f"Invalid value for 'query-v1-status'='{value}'. Must be one of: {', '.join(VALID_BODY_QUERY_V1_STATUS)}",
            )
    if "query-v2c-status" in payload:
        value = payload["query-v2c-status"]
        if value not in VALID_BODY_QUERY_V2C_STATUS:
            return (
                False,
                f"Invalid value for 'query-v2c-status'='{value}'. Must be one of: {', '.join(VALID_BODY_QUERY_V2C_STATUS)}",
            )
    if "trap-v1-status" in payload:
        value = payload["trap-v1-status"]
        if value not in VALID_BODY_TRAP_V1_STATUS:
            return (
                False,
                f"Invalid value for 'trap-v1-status'='{value}'. Must be one of: {', '.join(VALID_BODY_TRAP_V1_STATUS)}",
            )
    if "trap-v2c-status" in payload:
        value = payload["trap-v2c-status"]
        if value not in VALID_BODY_TRAP_V2C_STATUS:
            return (
                False,
                f"Invalid value for 'trap-v2c-status'='{value}'. Must be one of: {', '.join(VALID_BODY_TRAP_V2C_STATUS)}",
            )
    if "events" in payload:
        value = payload["events"]
        if value not in VALID_BODY_EVENTS:
            return (
                False,
                f"Invalid value for 'events'='{value}'. Must be one of: {', '.join(VALID_BODY_EVENTS)}",
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
    "endpoint": "switch_controller/snmp_community",
    "category": "cmdb",
    "api_path": "switch-controller/snmp-community",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure FortiSwitch SNMP v1/v2c communities globally.",
    "total_fields": 15,
    "required_fields_count": 1,
    "fields_with_defaults_count": 14,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
