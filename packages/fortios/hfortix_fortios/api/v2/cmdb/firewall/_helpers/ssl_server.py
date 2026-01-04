"""
Validation helpers for firewall/ssl_server endpoint.

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
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "ip": "0.0.0.0",
    "port": 443,
    "ssl-mode": "full",
    "add-header-x-forwarded-proto": "enable",
    "mapped-port": 80,
    "ssl-dh-bits": "2048",
    "ssl-algorithm": "high",
    "ssl-client-renegotiation": "allow",
    "ssl-min-version": "tls-1.1",
    "ssl-max-version": "tls-1.3",
    "ssl-send-empty-frags": "enable",
    "url-rewrite": "disable",
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
    "name": "string",  # Server name.
    "ip": "ipv4-address-any",  # IPv4 address of the SSL server.
    "port": "integer",  # Server service port (1 - 65535, default = 443).
    "ssl-mode": "option",  # SSL/TLS mode for encryption and decryption of traffic.
    "add-header-x-forwarded-proto": "option",  # Enable/disable adding an X-Forwarded-Proto header to forward
    "mapped-port": "integer",  # Mapped server service port (1 - 65535, default = 80).
    "ssl-cert": "string",  # List of certificate names to use for SSL connections to this
    "ssl-dh-bits": "option",  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    "ssl-algorithm": "option",  # Relative strength of encryption algorithms accepted in negot
    "ssl-client-renegotiation": "option",  # Allow or block client renegotiation by server.
    "ssl-min-version": "option",  # Lowest SSL/TLS version to negotiate.
    "ssl-max-version": "option",  # Highest SSL/TLS version to negotiate.
    "ssl-send-empty-frags": "option",  # Enable/disable sending empty fragments to avoid attack on CB
    "url-rewrite": "option",  # Enable/disable rewriting the URL.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Server name.",
    "ip": "IPv4 address of the SSL server.",
    "port": "Server service port (1 - 65535, default = 443).",
    "ssl-mode": "SSL/TLS mode for encryption and decryption of traffic.",
    "add-header-x-forwarded-proto": "Enable/disable adding an X-Forwarded-Proto header to forwarded requests.",
    "mapped-port": "Mapped server service port (1 - 65535, default = 80).",
    "ssl-cert": "List of certificate names to use for SSL connections to this server. (default = \"Fortinet_SSL\").",
    "ssl-dh-bits": "Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048).",
    "ssl-algorithm": "Relative strength of encryption algorithms accepted in negotiation.",
    "ssl-client-renegotiation": "Allow or block client renegotiation by server.",
    "ssl-min-version": "Lowest SSL/TLS version to negotiate.",
    "ssl-max-version": "Highest SSL/TLS version to negotiate.",
    "ssl-send-empty-frags": "Enable/disable sending empty fragments to avoid attack on CBC IV.",
    "url-rewrite": "Enable/disable rewriting the URL.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "port": {"type": "integer", "min": 1, "max": 65535},
    "mapped-port": {"type": "integer", "min": 1, "max": 65535},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "ssl-cert": {
        "name": {
            "type": "string",
            "help": "Certificate list.",
            "default": "Fortinet_SSL",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_SSL_MODE = [
    "half",
    "full",
]
VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO = [
    "enable",
    "disable",
]
VALID_BODY_SSL_DH_BITS = [
    "768",
    "1024",
    "1536",
    "2048",
]
VALID_BODY_SSL_ALGORITHM = [
    "high",
    "medium",
    "low",
]
VALID_BODY_SSL_CLIENT_RENEGOTIATION = [
    "allow",
    "deny",
    "secure",
]
VALID_BODY_SSL_MIN_VERSION = [
    "tls-1.0",
    "tls-1.1",
    "tls-1.2",
    "tls-1.3",
]
VALID_BODY_SSL_MAX_VERSION = [
    "tls-1.0",
    "tls-1.1",
    "tls-1.2",
    "tls-1.3",
]
VALID_BODY_SSL_SEND_EMPTY_FRAGS = [
    "enable",
    "disable",
]
VALID_BODY_URL_REWRITE = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_ssl_server_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for firewall/ssl_server.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_firewall_ssl_server_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_firewall_ssl_server_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_firewall_ssl_server_get(
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
    Validate required fields for firewall/ssl_server.

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


def validate_firewall_ssl_server_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new firewall/ssl_server object.

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
        ... }
        >>> is_valid, error = validate_firewall_ssl_server_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "ssl-mode": "half",  # Valid enum value
        ... }
        >>> is_valid, error = validate_firewall_ssl_server_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["ssl-mode"] = "invalid-value"
        >>> is_valid, error = validate_firewall_ssl_server_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_firewall_ssl_server_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "ssl-mode" in payload:
        value = payload["ssl-mode"]
        if value not in VALID_BODY_SSL_MODE:
            desc = FIELD_DESCRIPTIONS.get("ssl-mode", "")
            error_msg = f"Invalid value for 'ssl-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MODE)}"
            error_msg += f"\n  → Example: ssl-mode='{{ VALID_BODY_SSL_MODE[0] }}'"
            return (False, error_msg)
    if "add-header-x-forwarded-proto" in payload:
        value = payload["add-header-x-forwarded-proto"]
        if value not in VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO:
            desc = FIELD_DESCRIPTIONS.get("add-header-x-forwarded-proto", "")
            error_msg = f"Invalid value for 'add-header-x-forwarded-proto': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO)}"
            error_msg += f"\n  → Example: add-header-x-forwarded-proto='{{ VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO[0] }}'"
            return (False, error_msg)
    if "ssl-dh-bits" in payload:
        value = payload["ssl-dh-bits"]
        if value not in VALID_BODY_SSL_DH_BITS:
            desc = FIELD_DESCRIPTIONS.get("ssl-dh-bits", "")
            error_msg = f"Invalid value for 'ssl-dh-bits': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_DH_BITS)}"
            error_msg += f"\n  → Example: ssl-dh-bits='{{ VALID_BODY_SSL_DH_BITS[0] }}'"
            return (False, error_msg)
    if "ssl-algorithm" in payload:
        value = payload["ssl-algorithm"]
        if value not in VALID_BODY_SSL_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("ssl-algorithm", "")
            error_msg = f"Invalid value for 'ssl-algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_ALGORITHM)}"
            error_msg += f"\n  → Example: ssl-algorithm='{{ VALID_BODY_SSL_ALGORITHM[0] }}'"
            return (False, error_msg)
    if "ssl-client-renegotiation" in payload:
        value = payload["ssl-client-renegotiation"]
        if value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            desc = FIELD_DESCRIPTIONS.get("ssl-client-renegotiation", "")
            error_msg = f"Invalid value for 'ssl-client-renegotiation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_CLIENT_RENEGOTIATION)}"
            error_msg += f"\n  → Example: ssl-client-renegotiation='{{ VALID_BODY_SSL_CLIENT_RENEGOTIATION[0] }}'"
            return (False, error_msg)
    if "ssl-min-version" in payload:
        value = payload["ssl-min-version"]
        if value not in VALID_BODY_SSL_MIN_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-min-version", "")
            error_msg = f"Invalid value for 'ssl-min-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MIN_VERSION)}"
            error_msg += f"\n  → Example: ssl-min-version='{{ VALID_BODY_SSL_MIN_VERSION[0] }}'"
            return (False, error_msg)
    if "ssl-max-version" in payload:
        value = payload["ssl-max-version"]
        if value not in VALID_BODY_SSL_MAX_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-max-version", "")
            error_msg = f"Invalid value for 'ssl-max-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MAX_VERSION)}"
            error_msg += f"\n  → Example: ssl-max-version='{{ VALID_BODY_SSL_MAX_VERSION[0] }}'"
            return (False, error_msg)
    if "ssl-send-empty-frags" in payload:
        value = payload["ssl-send-empty-frags"]
        if value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            desc = FIELD_DESCRIPTIONS.get("ssl-send-empty-frags", "")
            error_msg = f"Invalid value for 'ssl-send-empty-frags': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_SEND_EMPTY_FRAGS)}"
            error_msg += f"\n  → Example: ssl-send-empty-frags='{{ VALID_BODY_SSL_SEND_EMPTY_FRAGS[0] }}'"
            return (False, error_msg)
    if "url-rewrite" in payload:
        value = payload["url-rewrite"]
        if value not in VALID_BODY_URL_REWRITE:
            desc = FIELD_DESCRIPTIONS.get("url-rewrite", "")
            error_msg = f"Invalid value for 'url-rewrite': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_URL_REWRITE)}"
            error_msg += f"\n  → Example: url-rewrite='{{ VALID_BODY_URL_REWRITE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_ssl_server_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update firewall/ssl_server.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_firewall_ssl_server_put(payload)
    """
    # Step 1: Validate enum values
    if "ssl-mode" in payload:
        value = payload["ssl-mode"]
        if value not in VALID_BODY_SSL_MODE:
            return (
                False,
                f"Invalid value for 'ssl-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MODE)}",
            )
    if "add-header-x-forwarded-proto" in payload:
        value = payload["add-header-x-forwarded-proto"]
        if value not in VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO:
            return (
                False,
                f"Invalid value for 'add-header-x-forwarded-proto'='{value}'. Must be one of: {', '.join(VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO)}",
            )
    if "ssl-dh-bits" in payload:
        value = payload["ssl-dh-bits"]
        if value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid value for 'ssl-dh-bits'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )
    if "ssl-algorithm" in payload:
        value = payload["ssl-algorithm"]
        if value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid value for 'ssl-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )
    if "ssl-client-renegotiation" in payload:
        value = payload["ssl-client-renegotiation"]
        if value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            return (
                False,
                f"Invalid value for 'ssl-client-renegotiation'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_RENEGOTIATION)}",
            )
    if "ssl-min-version" in payload:
        value = payload["ssl-min-version"]
        if value not in VALID_BODY_SSL_MIN_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-min-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_VERSION)}",
            )
    if "ssl-max-version" in payload:
        value = payload["ssl-max-version"]
        if value not in VALID_BODY_SSL_MAX_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-max-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MAX_VERSION)}",
            )
    if "ssl-send-empty-frags" in payload:
        value = payload["ssl-send-empty-frags"]
        if value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            return (
                False,
                f"Invalid value for 'ssl-send-empty-frags'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SEND_EMPTY_FRAGS)}",
            )
    if "url-rewrite" in payload:
        value = payload["url-rewrite"]
        if value not in VALID_BODY_URL_REWRITE:
            return (
                False,
                f"Invalid value for 'url-rewrite'='{value}'. Must be one of: {', '.join(VALID_BODY_URL_REWRITE)}",
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
    "endpoint": "firewall/ssl_server",
    "category": "cmdb",
    "api_path": "firewall/ssl-server",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure SSL servers.",
    "total_fields": 14,
    "required_fields_count": 0,
    "fields_with_defaults_count": 13,
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
