"""Validation helpers for log/syslogd2/setting - Auto-generated"""

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
    "server",  # Address of remote syslog server.
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "status": "disable",
    "server": "",
    "mode": "udp",
    "port": 514,
    "facility": "local7",
    "source-ip-interface": "",
    "source-ip": "",
    "format": "default",
    "priority": "default",
    "max-log-rate": 0,
    "enc-algorithm": "disable",
    "ssl-min-proto-version": "default",
    "certificate": "",
    "interface-select-method": "auto",
    "interface": "",
    "vrf-select": 0,
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
    "status": "option",  # Enable/disable remote syslog logging.
    "server": "string",  # Address of remote syslog server.
    "mode": "option",  # Remote syslog logging over UDP/Reliable TCP.
    "port": "integer",  # Server listen port.
    "facility": "option",  # Remote syslog facility.
    "source-ip-interface": "string",  # Source interface of syslog.
    "source-ip": "string",  # Source IP address of syslog.
    "format": "option",  # Log format.
    "priority": "option",  # Set log transmission priority.
    "max-log-rate": "integer",  # Syslog maximum log rate in MBps (0 = unlimited).
    "enc-algorithm": "option",  # Enable/disable reliable syslogging with TLS encryption.
    "ssl-min-proto-version": "option",  # Minimum supported protocol version for SSL/TLS connections (
    "certificate": "string",  # Certificate used to communicate with Syslog server.
    "custom-field-name": "string",  # Custom field name for CEF format logging.
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable remote syslog logging.",
    "server": "Address of remote syslog server.",
    "mode": "Remote syslog logging over UDP/Reliable TCP.",
    "port": "Server listen port.",
    "facility": "Remote syslog facility.",
    "source-ip-interface": "Source interface of syslog.",
    "source-ip": "Source IP address of syslog.",
    "format": "Log format.",
    "priority": "Set log transmission priority.",
    "max-log-rate": "Syslog maximum log rate in MBps (0 = unlimited).",
    "enc-algorithm": "Enable/disable reliable syslogging with TLS encryption.",
    "ssl-min-proto-version": "Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).",
    "certificate": "Certificate used to communicate with Syslog server.",
    "custom-field-name": "Custom field name for CEF format logging.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "server": {"type": "string", "max_length": 127},
    "port": {"type": "integer", "min": 0, "max": 65535},
    "source-ip-interface": {"type": "string", "max_length": 15},
    "source-ip": {"type": "string", "max_length": 63},
    "max-log-rate": {"type": "integer", "min": 0, "max": 100000},
    "certificate": {"type": "string", "max_length": 35},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "custom-field-name": {
        "id": {
            "type": "integer",
            "help": "Entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "name": {
            "type": "string",
            "help": "Field name [A-Za-z0-9_].",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "custom": {
            "type": "string",
            "help": "Field custom name [A-Za-z0-9_].",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Log to remote syslog server.
    "disable",  # Do not log to remote syslog server.
]
VALID_BODY_MODE = [
    "udp",  # Enable syslogging over UDP.
    "legacy-reliable",  # Enable legacy reliable syslogging by RFC3195 (Reliable Delivery for Syslog).
    "reliable",  # Enable reliable syslogging by RFC6587 (Transmission of Syslog Messages over TCP).
]
VALID_BODY_FACILITY = [
    "kernel",  # Kernel messages.
    "user",  # Random user-level messages.
    "mail",  # Mail system.
    "daemon",  # System daemons.
    "auth",  # Security/authorization messages.
    "syslog",  # Messages generated internally by syslog.
    "lpr",  # Line printer subsystem.
    "news",  # Network news subsystem.
    "uucp",  # Network news subsystem.
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
VALID_BODY_FORMAT = [
    "default",  # Syslog format.
    "csv",  # CSV (Comma Separated Values) format.
    "cef",  # CEF (Common Event Format) format.
    "rfc5424",  # Syslog RFC5424 format.
    "json",  # JSON (JavaScript Object Notation) format.
]
VALID_BODY_PRIORITY = [
    "default",  # Set Syslog transmission priority to default.
    "low",  # Set Syslog transmission priority to low.
]
VALID_BODY_ENC_ALGORITHM = [
    "high-medium",  # SSL communication with high and medium encryption algorithms.
    "high",  # SSL communication with high encryption algorithms.
    "low",  # SSL communication with low encryption algorithms.
    "disable",  # Disable SSL communication.
]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",  # Follow system global setting.
    "SSLv3",  # SSLv3.
    "TLSv1",  # TLSv1.
    "TLSv1-1",  # TLSv1.1.
    "TLSv1-2",  # TLSv1.2.
    "TLSv1-3",  # TLSv1.3.
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",  # Set outgoing interface automatically.
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_log_syslogd2_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for log/syslogd2/setting."""
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
    """Validate required fields for log/syslogd2/setting."""
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


def validate_log_syslogd2_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new log/syslogd2/setting object."""
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
    if "format" in payload:
        value = payload["format"]
        if value not in VALID_BODY_FORMAT:
            desc = FIELD_DESCRIPTIONS.get("format", "")
            error_msg = f"Invalid value for 'format': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORMAT)}"
            error_msg += f"\n  → Example: format='{{ VALID_BODY_FORMAT[0] }}'"
            return (False, error_msg)
    if "priority" in payload:
        value = payload["priority"]
        if value not in VALID_BODY_PRIORITY:
            desc = FIELD_DESCRIPTIONS.get("priority", "")
            error_msg = f"Invalid value for 'priority': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY)}"
            error_msg += f"\n  → Example: priority='{{ VALID_BODY_PRIORITY[0] }}'"
            return (False, error_msg)
    if "enc-algorithm" in payload:
        value = payload["enc-algorithm"]
        if value not in VALID_BODY_ENC_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("enc-algorithm", "")
            error_msg = f"Invalid value for 'enc-algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENC_ALGORITHM)}"
            error_msg += f"\n  → Example: enc-algorithm='{{ VALID_BODY_ENC_ALGORITHM[0] }}'"
            return (False, error_msg)
    if "ssl-min-proto-version" in payload:
        value = payload["ssl-min-proto-version"]
        if value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-min-proto-version", "")
            error_msg = f"Invalid value for 'ssl-min-proto-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MIN_PROTO_VERSION)}"
            error_msg += f"\n  → Example: ssl-min-proto-version='{{ VALID_BODY_SSL_MIN_PROTO_VERSION[0] }}'"
            return (False, error_msg)
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("interface-select-method", "")
            error_msg = f"Invalid value for 'interface-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERFACE_SELECT_METHOD)}"
            error_msg += f"\n  → Example: interface-select-method='{{ VALID_BODY_INTERFACE_SELECT_METHOD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_syslogd2_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update log/syslogd2/setting."""
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
    if "facility" in payload:
        value = payload["facility"]
        if value not in VALID_BODY_FACILITY:
            return (
                False,
                f"Invalid value for 'facility'='{value}'. Must be one of: {', '.join(VALID_BODY_FACILITY)}",
            )
    if "format" in payload:
        value = payload["format"]
        if value not in VALID_BODY_FORMAT:
            return (
                False,
                f"Invalid value for 'format'='{value}'. Must be one of: {', '.join(VALID_BODY_FORMAT)}",
            )
    if "priority" in payload:
        value = payload["priority"]
        if value not in VALID_BODY_PRIORITY:
            return (
                False,
                f"Invalid value for 'priority'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY)}",
            )
    if "enc-algorithm" in payload:
        value = payload["enc-algorithm"]
        if value not in VALID_BODY_ENC_ALGORITHM:
            return (
                False,
                f"Invalid value for 'enc-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_ENC_ALGORITHM)}",
            )
    if "ssl-min-proto-version" in payload:
        value = payload["ssl-min-proto-version"]
        if value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-min-proto-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
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
    "endpoint": "log/syslogd2/setting",
    "category": "cmdb",
    "api_path": "log.syslogd2/setting",
    "help": "Global settings for remote syslog server.",
    "total_fields": 17,
    "required_fields_count": 2,
    "fields_with_defaults_count": 16,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
