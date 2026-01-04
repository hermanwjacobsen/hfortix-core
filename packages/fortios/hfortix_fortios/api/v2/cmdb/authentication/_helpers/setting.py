"""
Validation helpers for authentication/setting endpoint.

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
    "active-auth-scheme": "",
    "sso-auth-scheme": "",
    "update-time": "",
    "persistent-cookie": "enable",
    "ip-auth-cookie": "disable",
    "cookie-max-age": 480,
    "cookie-refresh-div": 2,
    "captive-portal-type": "fqdn",
    "captive-portal-ip": "0.0.0.0",
    "captive-portal-ip6": "::",
    "captive-portal": "",
    "captive-portal6": "",
    "cert-auth": "disable",
    "cert-captive-portal": "",
    "cert-captive-portal-ip": "0.0.0.0",
    "cert-captive-portal-port": 7832,
    "captive-portal-port": 7830,
    "auth-https": "enable",
    "captive-portal-ssl-port": 7831,
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
    "active-auth-scheme": "string",  # Active authentication method (scheme name).
    "sso-auth-scheme": "string",  # Single-Sign-On authentication method (scheme name).
    "update-time": "user",  # Time of the last update.
    "persistent-cookie": "option",  # Enable/disable persistent cookie on web portal authenticatio
    "ip-auth-cookie": "option",  # Enable/disable persistent cookie on IP based web portal auth
    "cookie-max-age": "integer",  # Persistent web portal cookie maximum age in minutes (30 - 10
    "cookie-refresh-div": "integer",  # Refresh rate divider of persistent web portal cookie (defaul
    "captive-portal-type": "option",  # Captive portal type.
    "captive-portal-ip": "ipv4-address-any",  # Captive portal IP address.
    "captive-portal-ip6": "ipv6-address",  # Captive portal IPv6 address.
    "captive-portal": "string",  # Captive portal host name.
    "captive-portal6": "string",  # IPv6 captive portal host name.
    "cert-auth": "option",  # Enable/disable redirecting certificate authentication to HTT
    "cert-captive-portal": "string",  # Certificate captive portal host name.
    "cert-captive-portal-ip": "ipv4-address-any",  # Certificate captive portal IP address.
    "cert-captive-portal-port": "integer",  # Certificate captive portal port number (1 - 65535, default =
    "captive-portal-port": "integer",  # Captive portal port number (1 - 65535, default = 7830).
    "auth-https": "option",  # Enable/disable redirecting HTTP user authentication to HTTPS
    "captive-portal-ssl-port": "integer",  # Captive portal SSL port number (1 - 65535, default = 7831).
    "user-cert-ca": "string",  # CA certificate used for client certificate verification.
    "dev-range": "string",  # Address range for the IP based device query.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "active-auth-scheme": "Active authentication method (scheme name).",
    "sso-auth-scheme": "Single-Sign-On authentication method (scheme name).",
    "update-time": "Time of the last update.",
    "persistent-cookie": "Enable/disable persistent cookie on web portal authentication (default = enable).",
    "ip-auth-cookie": "Enable/disable persistent cookie on IP based web portal authentication (default = disable).",
    "cookie-max-age": "Persistent web portal cookie maximum age in minutes (30 - 10080 (1 week), default = 480 (8 hours)).",
    "cookie-refresh-div": "Refresh rate divider of persistent web portal cookie (default = 2). Refresh value = cookie-max-age/cookie-refresh-div.",
    "captive-portal-type": "Captive portal type.",
    "captive-portal-ip": "Captive portal IP address.",
    "captive-portal-ip6": "Captive portal IPv6 address.",
    "captive-portal": "Captive portal host name.",
    "captive-portal6": "IPv6 captive portal host name.",
    "cert-auth": "Enable/disable redirecting certificate authentication to HTTPS portal.",
    "cert-captive-portal": "Certificate captive portal host name.",
    "cert-captive-portal-ip": "Certificate captive portal IP address.",
    "cert-captive-portal-port": "Certificate captive portal port number (1 - 65535, default = 7832).",
    "captive-portal-port": "Captive portal port number (1 - 65535, default = 7830).",
    "auth-https": "Enable/disable redirecting HTTP user authentication to HTTPS.",
    "captive-portal-ssl-port": "Captive portal SSL port number (1 - 65535, default = 7831).",
    "user-cert-ca": "CA certificate used for client certificate verification.",
    "dev-range": "Address range for the IP based device query.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "active-auth-scheme": {"type": "string", "max_length": 35},
    "sso-auth-scheme": {"type": "string", "max_length": 35},
    "cookie-max-age": {"type": "integer", "min": 30, "max": 10080},
    "cookie-refresh-div": {"type": "integer", "min": 2, "max": 4},
    "captive-portal": {"type": "string", "max_length": 255},
    "captive-portal6": {"type": "string", "max_length": 255},
    "cert-captive-portal": {"type": "string", "max_length": 255},
    "cert-captive-portal-port": {"type": "integer", "min": 1, "max": 65535},
    "captive-portal-port": {"type": "integer", "min": 1, "max": 65535},
    "captive-portal-ssl-port": {"type": "integer", "min": 1, "max": 65535},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "user-cert-ca": {
        "name": {
            "type": "string",
            "help": "CA certificate list.",
            "default": "",
            "max_length": 79,
        },
    },
    "dev-range": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_PERSISTENT_COOKIE = [
    "enable",
    "disable",
]
VALID_BODY_IP_AUTH_COOKIE = [
    "enable",
    "disable",
]
VALID_BODY_CAPTIVE_PORTAL_TYPE = [
    "fqdn",
    "ip",
]
VALID_BODY_CERT_AUTH = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_HTTPS = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_authentication_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for authentication/setting.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_authentication_setting_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_authentication_setting_get(
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
    Validate required fields for authentication/setting.

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


def validate_authentication_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new authentication/setting object.

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
        >>> is_valid, error = validate_authentication_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "persistent-cookie": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_authentication_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["persistent-cookie"] = "invalid-value"
        >>> is_valid, error = validate_authentication_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_authentication_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "persistent-cookie" in payload:
        value = payload["persistent-cookie"]
        if value not in VALID_BODY_PERSISTENT_COOKIE:
            desc = FIELD_DESCRIPTIONS.get("persistent-cookie", "")
            error_msg = f"Invalid value for 'persistent-cookie': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERSISTENT_COOKIE)}"
            error_msg += f"\n  → Example: persistent-cookie='{{ VALID_BODY_PERSISTENT_COOKIE[0] }}'"
            return (False, error_msg)
    if "ip-auth-cookie" in payload:
        value = payload["ip-auth-cookie"]
        if value not in VALID_BODY_IP_AUTH_COOKIE:
            desc = FIELD_DESCRIPTIONS.get("ip-auth-cookie", "")
            error_msg = f"Invalid value for 'ip-auth-cookie': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_AUTH_COOKIE)}"
            error_msg += f"\n  → Example: ip-auth-cookie='{{ VALID_BODY_IP_AUTH_COOKIE[0] }}'"
            return (False, error_msg)
    if "captive-portal-type" in payload:
        value = payload["captive-portal-type"]
        if value not in VALID_BODY_CAPTIVE_PORTAL_TYPE:
            desc = FIELD_DESCRIPTIONS.get("captive-portal-type", "")
            error_msg = f"Invalid value for 'captive-portal-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CAPTIVE_PORTAL_TYPE)}"
            error_msg += f"\n  → Example: captive-portal-type='{{ VALID_BODY_CAPTIVE_PORTAL_TYPE[0] }}'"
            return (False, error_msg)
    if "cert-auth" in payload:
        value = payload["cert-auth"]
        if value not in VALID_BODY_CERT_AUTH:
            desc = FIELD_DESCRIPTIONS.get("cert-auth", "")
            error_msg = f"Invalid value for 'cert-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CERT_AUTH)}"
            error_msg += f"\n  → Example: cert-auth='{{ VALID_BODY_CERT_AUTH[0] }}'"
            return (False, error_msg)
    if "auth-https" in payload:
        value = payload["auth-https"]
        if value not in VALID_BODY_AUTH_HTTPS:
            desc = FIELD_DESCRIPTIONS.get("auth-https", "")
            error_msg = f"Invalid value for 'auth-https': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_HTTPS)}"
            error_msg += f"\n  → Example: auth-https='{{ VALID_BODY_AUTH_HTTPS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_authentication_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update authentication/setting.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_authentication_setting_put(payload)
    """
    # Step 1: Validate enum values
    if "persistent-cookie" in payload:
        value = payload["persistent-cookie"]
        if value not in VALID_BODY_PERSISTENT_COOKIE:
            return (
                False,
                f"Invalid value for 'persistent-cookie'='{value}'. Must be one of: {', '.join(VALID_BODY_PERSISTENT_COOKIE)}",
            )
    if "ip-auth-cookie" in payload:
        value = payload["ip-auth-cookie"]
        if value not in VALID_BODY_IP_AUTH_COOKIE:
            return (
                False,
                f"Invalid value for 'ip-auth-cookie'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_AUTH_COOKIE)}",
            )
    if "captive-portal-type" in payload:
        value = payload["captive-portal-type"]
        if value not in VALID_BODY_CAPTIVE_PORTAL_TYPE:
            return (
                False,
                f"Invalid value for 'captive-portal-type'='{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL_TYPE)}",
            )
    if "cert-auth" in payload:
        value = payload["cert-auth"]
        if value not in VALID_BODY_CERT_AUTH:
            return (
                False,
                f"Invalid value for 'cert-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_CERT_AUTH)}",
            )
    if "auth-https" in payload:
        value = payload["auth-https"]
        if value not in VALID_BODY_AUTH_HTTPS:
            return (
                False,
                f"Invalid value for 'auth-https'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_HTTPS)}",
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
    # Replace all non-alphanumeric characters with underscores for valid Python identifiers
    import re
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', field_name)
    constant_name = f"VALID_BODY_{safe_name.upper()}"
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
    "endpoint": "authentication/setting",
    "category": "cmdb",
    "api_path": "authentication/setting",
    "help": "Configure authentication setting.",
    "total_fields": 21,
    "required_fields_count": 0,
    "fields_with_defaults_count": 19,
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
