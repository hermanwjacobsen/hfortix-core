"""
Validation helpers for user/exchange endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification
Customize as needed for endpoint-specific business logic.
"""

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
#
# 1. FALSE POSITIVES: Some fields marked "required" have default values,
#    meaning they're optional (filtered out by generator)
#
# 2. CONDITIONAL REQUIREMENTS: Many endpoints require EITHER field A OR field B:
#    - firewall.policy: requires (srcaddr + dstaddr) OR (srcaddr6 + dstaddr6)
#    - These conditional requirements cannot be expressed in a simple list
#
# 3. SPECIALIZED FEATURES: Fields for WAN optimization, VPN, NAT64, etc.
#    are marked "required" but only apply when using those features
#
# The REQUIRED_FIELDS list below is INFORMATIONAL ONLY and shows fields that:
# - Are marked required in the schema
# - Don't have non-empty default values
# - Aren't specialized feature fields
#
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
    "rpc-over-tcp",
    "rpc-over-http",
    "rpc-over-https",
]
VALID_BODY_VALIDATE_SERVER_CERTIFICATE = [
    "disable",
    "enable",
]
VALID_BODY_AUTH_TYPE = [
    "spnego",
    "ntlm",
    "kerberos",
]
VALID_BODY_AUTH_LEVEL = [
    "connect",
    "call",
    "packet",
    "integrity",
    "privacy",
]
VALID_BODY_HTTP_AUTH_TYPE = [
    "basic",
    "ntlm",
]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_AUTO_DISCOVER_KDC = [
    "enable",
    "disable",
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
    """
    Validate GET request parameters for user/exchange.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_user_exchange_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_user_exchange_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_user_exchange_get(
        ...     filters={"format": "name|type"}
        ... )
        >>> assert is_valid == True
    """
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
    """
    Validate required fields for user/exchange.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "test"}
        >>> is_valid, error = validate_required_fields(payload)
    """
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
    """
    Validate POST request to create new user/exchange object.

    This validator performs two-stage validation:
    1. Required fields check (schema-based)
    2. Field value validation (enums, ranges, formats)

    Args:
        payload: Request body data with configuration
        **params: Query parameters (vdom, etc.)

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if payload is valid, False otherwise
        - error_message: None if valid, detailed error string if invalid

    Examples:
        >>> # ✅ Valid - Minimal required fields
        >>> payload = {
        ...     "server-name": True,  # MS Exchange server hostname.
        ...     "domain-name": True,  # MS Exchange server fully qualified domain name.
        ... }
        >>> is_valid, error = validate_user_exchange_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "server-name": True,
        ...     "connect-protocol": "rpc-over-tcp",  # Valid enum value
        ... }
        >>> is_valid, error = validate_user_exchange_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["connect-protocol"] = "invalid-value"
        >>> is_valid, error = validate_user_exchange_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_user_exchange_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
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
    """
    Validate PUT request to update user/exchange.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_user_exchange_put(payload)
    """
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
# Provide programmatic access to field metadata for IDE autocomplete,
# documentation generation, and dynamic validation
# ============================================================================


def get_field_description(field_name: str) -> str | None:
    """
    Get description/help text for a field.

    Args:
        field_name: Name of the field

    Returns:
        Description text or None if field doesn't exist

    Example:
        >>> desc = get_field_description("name")
        >>> print(desc)
    """
    return FIELD_DESCRIPTIONS.get(field_name)


def get_field_type(field_name: str) -> str | None:
    """
    Get the type of a field.

    Args:
        field_name: Name of the field

    Returns:
        Field type (e.g., "string", "integer", "option") or None

    Example:
        >>> field_type = get_field_type("status")
        >>> print(field_type)  # "option"
    """
    return FIELD_TYPES.get(field_name)


def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """
    Get constraints for a field (min/max values, string length).

    Args:
        field_name: Name of the field

    Returns:
        Constraint dict or None

    Example:
        >>> constraints = get_field_constraints("port")
        >>> print(constraints)  # {"type": "integer", "min": 1, "max": 65535}
    """
    return FIELD_CONSTRAINTS.get(field_name)


def get_field_default(field_name: str) -> Any | None:
    """
    Get default value for a field.

    Args:
        field_name: Name of the field

    Returns:
        Default value or None if no default

    Example:
        >>> default = get_field_default("status")
        >>> print(default)  # "enable"
    """
    return FIELDS_WITH_DEFAULTS.get(field_name)


def get_field_options(field_name: str) -> list[str] | None:
    """
    Get valid enum options for a field.

    Args:
        field_name: Name of the field

    Returns:
        List of valid values or None if not an enum field

    Example:
        >>> options = get_field_options("status")
        >>> print(options)  # ["enable", "disable"]
    """
    # Construct the constant name from field name
    constant_name = f"VALID_BODY_{field_name.replace('-', '_').upper()}"
    return globals().get(constant_name)


def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """
    Get schema for nested table/list fields.

    Args:
        field_name: Name of the parent field

    Returns:
        Dict mapping child field names to their metadata

    Example:
        >>> nested = get_nested_schema("members")
        >>> if nested:
        ...     for child_field, child_meta in nested.items():
        ...         print(f"{child_field}: {child_meta['type']}")
    """
    return NESTED_SCHEMAS.get(field_name)


def get_all_fields() -> list[str]:
    """
    Get list of all field names.

    Returns:
        List of all field names in the schema

    Example:
        >>> fields = get_all_fields()
        >>> print(len(fields))
    """
    return list(FIELD_TYPES.keys())


def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """
    Get complete metadata for a field (type, description, constraints, defaults, options).

    Args:
        field_name: Name of the field

    Returns:
        Dict with all available metadata or None if field doesn't exist

    Example:
        >>> meta = get_field_metadata("status")
        >>> print(meta)
        >>> # {
        >>> #   "type": "option",
        >>> #   "description": "Enable/disable this feature",
        >>> #   "default": "enable",
        >>> #   "options": ["enable", "disable"]
        >>> # }
    """
    if field_name not in FIELD_TYPES:
        return None

    metadata = {
        "name": field_name,
        "type": FIELD_TYPES[field_name],
    }

    # Add description if available
    if field_name in FIELD_DESCRIPTIONS:
        metadata["description"] = FIELD_DESCRIPTIONS[field_name]

    # Add constraints if available
    if field_name in FIELD_CONSTRAINTS:
        metadata["constraints"] = FIELD_CONSTRAINTS[field_name]

    # Add default if available
    if field_name in FIELDS_WITH_DEFAULTS:
        metadata["default"] = FIELDS_WITH_DEFAULTS[field_name]

    # Add required flag
    metadata["required"] = field_name in REQUIRED_FIELDS

    # Add options if available
    options = get_field_options(field_name)
    if options:
        metadata["options"] = options

    # Add nested schema if available
    nested = get_nested_schema(field_name)
    if nested:
        metadata["nested_schema"] = nested

    return metadata


def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """
    Validate a single field value against its constraints.

    Args:
        field_name: Name of the field
        value: Value to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_field_value("status", "enable")
        >>> if not is_valid:
        ...     print(error)
    """
    # Get field metadata
    field_type = get_field_type(field_name)
    if field_type is None:
        return (False, f"Unknown field: '{field_name}' (not defined in schema)")

    # Get field description for better error context
    description = get_field_description(field_name)

    # Validate enum values
    options = get_field_options(field_name)
    if options and value not in options:
        error_msg = f"Invalid value for '{field_name}': {repr(value)}"
        if description:
            error_msg += f"\n  → Description: {description}"
        error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in options)}"
        if options:
            error_msg += f"\n  → Example: {field_name}={repr(options[0])}"
        return (False, error_msg)

    # Validate constraints
    constraints = get_field_constraints(field_name)
    if constraints:
        constraint_type = constraints.get("type")

        if constraint_type == "integer":
            if not isinstance(value, int):
                error_msg = f"Field '{field_name}' must be an integer"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            min_val = constraints.get("min")
            max_val = constraints.get("max")

            if min_val is not None and value < min_val:
                error_msg = f"Field '{field_name}' value {value} is below minimum {min_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if max_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

            if max_val is not None and value > max_val:
                error_msg = f"Field '{field_name}' value {value} exceeds maximum {max_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if min_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

        elif constraint_type == "string":
            if not isinstance(value, str):
                error_msg = f"Field '{field_name}' must be a string"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            max_length = constraints.get("max_length")
            if max_length and len(value) > max_length:
                error_msg = f"Field '{field_name}' length {len(value)} exceeds maximum {max_length}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → Your value: {repr(value[:50])}{'...' if len(value) > 50 else ''}"
                return (False, error_msg)

    return (True, None)


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
    """
    Get information about this endpoint schema.

    Returns:
        Dict with schema metadata

    Example:
        >>> info = get_schema_info()
        >>> print(f"Endpoint: {info['endpoint']}")
        >>> print(f"Total fields: {info['total_fields']}")
    """
    return SCHEMA_INFO.copy()
