"""Validation helpers for user/exchange - Auto-generated"""

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
    "server-name",  # MS Exchange server hostname.
    "domain-name",  # MS Exchange server fully qualified domain name.
    "username",  # User name used to sign in to the server. Must have proper permissions for service.
    "password",  # Password for the specified username.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "server-name": "",
    "domain-name": "",
    "username": "",
    "ip": "0.0.0.0",
    "connect-protocol": "rpc-over-https",
    "validate-server-certificate": "disable",
    "auth-type": "kerberos",
    "auth-level": "privacy",
    "http-auth-type": "ntlm",
    "ssl-min-proto-version": "default",
    "auto-discover-kdc": "enable",
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
    "name": "string",  # MS Exchange server entry name.
    "server-name": "string",  # MS Exchange server hostname.
    "domain-name": "string",  # MS Exchange server fully qualified domain name.
    "username": "string",  # User name used to sign in to the server. Must have proper pe
    "password": "password",  # Password for the specified username.
    "ip": "ipv4-address-any",  # Server IPv4 address.
    "connect-protocol": "option",  # Connection protocol used to connect to MS Exchange service.
    "validate-server-certificate": "option",  # Enable/disable exchange server certificate validation.
    "auth-type": "option",  # Authentication security type used for the RPC protocol layer
    "auth-level": "option",  # Authentication security level used for the RPC protocol laye
    "http-auth-type": "option",  # Authentication security type used for the HTTP transport.
    "ssl-min-proto-version": "option",  # Minimum SSL/TLS protocol version for HTTPS transport (defaul
    "auto-discover-kdc": "option",  # Enable/disable automatic discovery of KDC IP addresses.
    "kdc-ip": "string",  # KDC IPv4 addresses for Kerberos authentication.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "MS Exchange server entry name.",
    "server-name": "MS Exchange server hostname.",
    "domain-name": "MS Exchange server fully qualified domain name.",
    "username": "User name used to sign in to the server. Must have proper permissions for service.",
    "password": "Password for the specified username.",
    "ip": "Server IPv4 address.",
    "connect-protocol": "Connection protocol used to connect to MS Exchange service.",
    "validate-server-certificate": "Enable/disable exchange server certificate validation.",
    "auth-type": "Authentication security type used for the RPC protocol layer.",
    "auth-level": "Authentication security level used for the RPC protocol layer.",
    "http-auth-type": "Authentication security type used for the HTTP transport.",
    "ssl-min-proto-version": "Minimum SSL/TLS protocol version for HTTPS transport (default is to follow system global setting).",
    "auto-discover-kdc": "Enable/disable automatic discovery of KDC IP addresses.",
    "kdc-ip": "KDC IPv4 addresses for Kerberos authentication.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "server-name": {"type": "string", "max_length": 63},
    "domain-name": {"type": "string", "max_length": 79},
    "username": {"type": "string", "max_length": 64},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "kdc-ip": {
        "ipv4": {
            "type": "string",
            "help": "KDC IPv4 addresses for Kerberos authentication.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_CONNECT_PROTOCOL = [
    "rpc-over-tcp",  # Connect using RPC-over-TCP. Use for MS Exchange 2010 and earlier versions. Supported in MS Exchange 2013.
    "rpc-over-http",  # Connect using RPC-over-HTTP. Use for MS Exchange 2016 and later versions. Supported in MS Exchange 2013.
    "rpc-over-https",  # Connect using RPC-over-HTTPS. Use for MS Exchange 2016 and later versions. Supported in MS Exchange 2013.
]
VALID_BODY_VALIDATE_SERVER_CERTIFICATE = [
    "disable",  # Disable validation of server certificate.
    "enable",  # Enable validation of server certificate.
]
VALID_BODY_AUTH_TYPE = [
    "spnego",  # Negotiate authentication.
    "ntlm",  # NTLM authentication.
    "kerberos",  # Kerberos authentication.
]
VALID_BODY_AUTH_LEVEL = [
    "connect",  # RPC authentication level 'connect'.
    "call",  # RPC authentication level 'call'.
    "packet",  # RPC authentication level 'packet'.
    "integrity",  # RPC authentication level 'integrity'.
    "privacy",  # RPC authentication level 'privacy'.
]
VALID_BODY_HTTP_AUTH_TYPE = [
    "basic",  # Basic HTTP authentication.
    "ntlm",  # NTLM HTTP authentication.
]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",  # Follow system global setting.
    "SSLv3",  # SSLv3.
    "TLSv1",  # TLSv1.
    "TLSv1-1",  # TLSv1.1.
    "TLSv1-2",  # TLSv1.2.
    "TLSv1-3",  # TLSv1.3.
]
VALID_BODY_AUTO_DISCOVER_KDC = [
    "enable",  # Enable automatic discovery of KDC IP addresses.
    "disable",  # Disable automatic discovery of KDC IP addresses.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_exchange_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for user/exchange."""
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
    """Validate required fields for user/exchange."""
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


def validate_user_exchange_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new user/exchange object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "connect-protocol" in payload:
        value = payload["connect-protocol"]
        if value not in VALID_BODY_CONNECT_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("connect-protocol", "")
            error_msg = f"Invalid value for 'connect-protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CONNECT_PROTOCOL)}"
            error_msg += f"\n  → Example: connect-protocol='{{ VALID_BODY_CONNECT_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "validate-server-certificate" in payload:
        value = payload["validate-server-certificate"]
        if value not in VALID_BODY_VALIDATE_SERVER_CERTIFICATE:
            desc = FIELD_DESCRIPTIONS.get("validate-server-certificate", "")
            error_msg = f"Invalid value for 'validate-server-certificate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VALIDATE_SERVER_CERTIFICATE)}"
            error_msg += f"\n  → Example: validate-server-certificate='{{ VALID_BODY_VALIDATE_SERVER_CERTIFICATE[0] }}'"
            return (False, error_msg)
    if "auth-type" in payload:
        value = payload["auth-type"]
        if value not in VALID_BODY_AUTH_TYPE:
            desc = FIELD_DESCRIPTIONS.get("auth-type", "")
            error_msg = f"Invalid value for 'auth-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_TYPE)}"
            error_msg += f"\n  → Example: auth-type='{{ VALID_BODY_AUTH_TYPE[0] }}'"
            return (False, error_msg)
    if "auth-level" in payload:
        value = payload["auth-level"]
        if value not in VALID_BODY_AUTH_LEVEL:
            desc = FIELD_DESCRIPTIONS.get("auth-level", "")
            error_msg = f"Invalid value for 'auth-level': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_LEVEL)}"
            error_msg += f"\n  → Example: auth-level='{{ VALID_BODY_AUTH_LEVEL[0] }}'"
            return (False, error_msg)
    if "http-auth-type" in payload:
        value = payload["http-auth-type"]
        if value not in VALID_BODY_HTTP_AUTH_TYPE:
            desc = FIELD_DESCRIPTIONS.get("http-auth-type", "")
            error_msg = f"Invalid value for 'http-auth-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_AUTH_TYPE)}"
            error_msg += f"\n  → Example: http-auth-type='{{ VALID_BODY_HTTP_AUTH_TYPE[0] }}'"
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
    if "auto-discover-kdc" in payload:
        value = payload["auto-discover-kdc"]
        if value not in VALID_BODY_AUTO_DISCOVER_KDC:
            desc = FIELD_DESCRIPTIONS.get("auto-discover-kdc", "")
            error_msg = f"Invalid value for 'auto-discover-kdc': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_DISCOVER_KDC)}"
            error_msg += f"\n  → Example: auto-discover-kdc='{{ VALID_BODY_AUTO_DISCOVER_KDC[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_exchange_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update user/exchange."""
    # Step 1: Validate enum values
    if "connect-protocol" in payload:
        value = payload["connect-protocol"]
        if value not in VALID_BODY_CONNECT_PROTOCOL:
            return (
                False,
                f"Invalid value for 'connect-protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_CONNECT_PROTOCOL)}",
            )
    if "validate-server-certificate" in payload:
        value = payload["validate-server-certificate"]
        if value not in VALID_BODY_VALIDATE_SERVER_CERTIFICATE:
            return (
                False,
                f"Invalid value for 'validate-server-certificate'='{value}'. Must be one of: {', '.join(VALID_BODY_VALIDATE_SERVER_CERTIFICATE)}",
            )
    if "auth-type" in payload:
        value = payload["auth-type"]
        if value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid value for 'auth-type'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )
    if "auth-level" in payload:
        value = payload["auth-level"]
        if value not in VALID_BODY_AUTH_LEVEL:
            return (
                False,
                f"Invalid value for 'auth-level'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_LEVEL)}",
            )
    if "http-auth-type" in payload:
        value = payload["http-auth-type"]
        if value not in VALID_BODY_HTTP_AUTH_TYPE:
            return (
                False,
                f"Invalid value for 'http-auth-type'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_AUTH_TYPE)}",
            )
    if "ssl-min-proto-version" in payload:
        value = payload["ssl-min-proto-version"]
        if value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-min-proto-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )
    if "auto-discover-kdc" in payload:
        value = payload["auto-discover-kdc"]
        if value not in VALID_BODY_AUTO_DISCOVER_KDC:
            return (
                False,
                f"Invalid value for 'auto-discover-kdc'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_DISCOVER_KDC)}",
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
    "endpoint": "user/exchange",
    "category": "cmdb",
    "api_path": "user/exchange",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure MS Exchange server entries.",
    "total_fields": 14,
    "required_fields_count": 4,
    "fields_with_defaults_count": 12,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
