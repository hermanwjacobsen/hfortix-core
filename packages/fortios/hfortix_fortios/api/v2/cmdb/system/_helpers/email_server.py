"""Validation helpers for system/email_server - Auto-generated"""

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
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "type": "custom",
    "server": "",
    "port": 25,
    "source-ip": "0.0.0.0",
    "source-ip6": "::",
    "authenticate": "disable",
    "validate-server": "disable",
    "username": "",
    "security": "none",
    "ssl-min-proto-version": "default",
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
    "type": "option",  # Use FortiGuard Message service or custom email server.
    "server": "string",  # SMTP server IP address or hostname.
    "port": "integer",  # SMTP server port.
    "source-ip": "ipv4-address",  # SMTP server IPv4 source IP.
    "source-ip6": "ipv6-address",  # SMTP server IPv6 source IP.
    "authenticate": "option",  # Enable/disable authentication.
    "validate-server": "option",  # Enable/disable validation of server certificate.
    "username": "string",  # SMTP server user name for authentication.
    "password": "password",  # SMTP server user password for authentication.
    "security": "option",  # Connection security used by the email server.
    "ssl-min-proto-version": "option",  # Minimum supported protocol version for SSL/TLS connections (
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "type": "Use FortiGuard Message service or custom email server.",
    "server": "SMTP server IP address or hostname.",
    "port": "SMTP server port.",
    "source-ip": "SMTP server IPv4 source IP.",
    "source-ip6": "SMTP server IPv6 source IP.",
    "authenticate": "Enable/disable authentication.",
    "validate-server": "Enable/disable validation of server certificate.",
    "username": "SMTP server user name for authentication.",
    "password": "SMTP server user password for authentication.",
    "security": "Connection security used by the email server.",
    "ssl-min-proto-version": "Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "server": {"type": "string", "max_length": 63},
    "port": {"type": "integer", "min": 1, "max": 65535},
    "username": {"type": "string", "max_length": 255},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "custom",  # Use custom email server.
]
VALID_BODY_AUTHENTICATE = [
    "enable",  # Enable authentication.
    "disable",  # Disable authentication.
]
VALID_BODY_VALIDATE_SERVER = [
    "enable",  # Enable validation of server certificate.
    "disable",  # Disable validation of server certificate.
]
VALID_BODY_SECURITY = [
    "none",  # None.
    "starttls",  # STARTTLS.
    "smtps",  # SSL/TLS.
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


def validate_system_email_server_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/email_server."""
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
    """Validate required fields for system/email_server."""
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


def validate_system_email_server_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/email_server object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "authenticate" in payload:
        value = payload["authenticate"]
        if value not in VALID_BODY_AUTHENTICATE:
            desc = FIELD_DESCRIPTIONS.get("authenticate", "")
            error_msg = f"Invalid value for 'authenticate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHENTICATE)}"
            error_msg += f"\n  → Example: authenticate='{{ VALID_BODY_AUTHENTICATE[0] }}'"
            return (False, error_msg)
    if "validate-server" in payload:
        value = payload["validate-server"]
        if value not in VALID_BODY_VALIDATE_SERVER:
            desc = FIELD_DESCRIPTIONS.get("validate-server", "")
            error_msg = f"Invalid value for 'validate-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VALIDATE_SERVER)}"
            error_msg += f"\n  → Example: validate-server='{{ VALID_BODY_VALIDATE_SERVER[0] }}'"
            return (False, error_msg)
    if "security" in payload:
        value = payload["security"]
        if value not in VALID_BODY_SECURITY:
            desc = FIELD_DESCRIPTIONS.get("security", "")
            error_msg = f"Invalid value for 'security': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURITY)}"
            error_msg += f"\n  → Example: security='{{ VALID_BODY_SECURITY[0] }}'"
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


def validate_system_email_server_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/email_server."""
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "authenticate" in payload:
        value = payload["authenticate"]
        if value not in VALID_BODY_AUTHENTICATE:
            return (
                False,
                f"Invalid value for 'authenticate'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATE)}",
            )
    if "validate-server" in payload:
        value = payload["validate-server"]
        if value not in VALID_BODY_VALIDATE_SERVER:
            return (
                False,
                f"Invalid value for 'validate-server'='{value}'. Must be one of: {', '.join(VALID_BODY_VALIDATE_SERVER)}",
            )
    if "security" in payload:
        value = payload["security"]
        if value not in VALID_BODY_SECURITY:
            return (
                False,
                f"Invalid value for 'security'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY)}",
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
    "endpoint": "system/email_server",
    "category": "cmdb",
    "api_path": "system/email-server",
    "help": "Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.",
    "total_fields": 14,
    "required_fields_count": 1,
    "fields_with_defaults_count": 13,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
