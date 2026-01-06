"""Validation helpers for switch_controller/remote_log - Auto-generated"""

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
    "name",  # Remote log name.
    "server",  # IPv4 address of the remote syslog server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "status": "disable",
    "server": "",
    "port": 514,
    "severity": "information",
    "csv": "disable",
    "facility": "local7",
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
    "name": "string",  # Remote log name.
    "status": "option",  # Enable/disable logging by FortiSwitch device to a remote sys
    "server": "string",  # IPv4 address of the remote syslog server.
    "port": "integer",  # Remote syslog server listening port.
    "severity": "option",  # Severity of logs to be transferred to remote log server.
    "csv": "option",  # Enable/disable comma-separated value (CSV) strings.
    "facility": "option",  # Facility to log to remote syslog server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Remote log name.",
    "status": "Enable/disable logging by FortiSwitch device to a remote syslog server.",
    "server": "IPv4 address of the remote syslog server.",
    "port": "Remote syslog server listening port.",
    "severity": "Severity of logs to be transferred to remote log server.",
    "csv": "Enable/disable comma-separated value (CSV) strings.",
    "facility": "Facility to log to remote syslog server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "server": {"type": "string", "max_length": 63},
    "port": {"type": "integer", "min": 0, "max": 65535},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable logging by FortiSwitch device to a remote syslog server.
    "disable",  # Disable logging by FortiSwitch device to a remote syslog server.
]
VALID_BODY_SEVERITY = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_BODY_CSV = [
    "enable",  # Enable comma-separated value (CSV) strings.
    "disable",  # Disable comma-separated value (CSV) strings.
]
VALID_BODY_FACILITY = [
    "kernel",  # Kernel messages.
    "user",  # Random user-level messages.
    "mail",  # Mail system.
    "daemon",  # System daemons.
    "auth",  # Security/authorization messages.
    "syslog",  # Messages generated internally by syslogd.
    "lpr",  # Line printer subsystem.
    "news",  # Network news subsystem.
    "uucp",  # UUCP server messages.
    "cron",  # Clock daemon.
    "authpriv",  # Security/authorization messages (private).
    "ftp",  # FTP daemon.
    "ntp",  # NTP daemon.
    "audit",  # Log audit.
    "alert",  # Log alert.
    "clock",  # Clock daemon.
    "local0",  # Reserved for local use.
    "local1",  # Reserved for local use.
    "local2",  # Reserved for local use.
    "local3",  # Reserved for local use.
    "local4",  # Reserved for local use.
    "local5",  # Reserved for local use.
    "local6",  # Reserved for local use.
    "local7",  # Reserved for local use.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_remote_log_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/remote_log."""
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
    """Validate required fields for switch_controller/remote_log."""
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


def validate_switch_controller_remote_log_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/remote_log object."""
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
    if "severity" in payload:
        value = payload["severity"]
        if value not in VALID_BODY_SEVERITY:
            desc = FIELD_DESCRIPTIONS.get("severity", "")
            error_msg = f"Invalid value for 'severity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SEVERITY)}"
            error_msg += f"\n  → Example: severity='{{ VALID_BODY_SEVERITY[0] }}'"
            return (False, error_msg)
    if "csv" in payload:
        value = payload["csv"]
        if value not in VALID_BODY_CSV:
            desc = FIELD_DESCRIPTIONS.get("csv", "")
            error_msg = f"Invalid value for 'csv': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CSV)}"
            error_msg += f"\n  → Example: csv='{{ VALID_BODY_CSV[0] }}'"
            return (False, error_msg)
    if "facility" in payload:
        value = payload["facility"]
        if value not in VALID_BODY_FACILITY:
            desc = FIELD_DESCRIPTIONS.get("facility", "")
            error_msg = f"Invalid value for 'facility': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FACILITY)}"
            error_msg += f"\n  → Example: facility='{{ VALID_BODY_FACILITY[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_remote_log_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/remote_log."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "severity" in payload:
        value = payload["severity"]
        if value not in VALID_BODY_SEVERITY:
            return (
                False,
                f"Invalid value for 'severity'='{value}'. Must be one of: {', '.join(VALID_BODY_SEVERITY)}",
            )
    if "csv" in payload:
        value = payload["csv"]
        if value not in VALID_BODY_CSV:
            return (
                False,
                f"Invalid value for 'csv'='{value}'. Must be one of: {', '.join(VALID_BODY_CSV)}",
            )
    if "facility" in payload:
        value = payload["facility"]
        if value not in VALID_BODY_FACILITY:
            return (
                False,
                f"Invalid value for 'facility'='{value}'. Must be one of: {', '.join(VALID_BODY_FACILITY)}",
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
    "endpoint": "switch_controller/remote_log",
    "category": "cmdb",
    "api_path": "switch-controller/remote-log",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure logging by FortiSwitch device to a remote syslog server.",
    "total_fields": 7,
    "required_fields_count": 2,
    "fields_with_defaults_count": 7,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
