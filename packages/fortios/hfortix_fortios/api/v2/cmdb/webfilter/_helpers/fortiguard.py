"""
Validation helpers for webfilter/fortiguard endpoint.

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
    "cache-mode": "ttl",
    "cache-prefix-match": "enable",
    "cache-mem-permille": 1,
    "ovrd-auth-port-http": 8008,
    "ovrd-auth-port-https": 8010,
    "ovrd-auth-port-https-flow": 8015,
    "ovrd-auth-port-warning": 8020,
    "ovrd-auth-https": "enable",
    "warn-auth-https": "enable",
    "close-ports": "disable",
    "request-packet-size-limit": 0,
    "embed-image": "enable",
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
    "cache-mode": "option",  # Cache entry expiration mode.
    "cache-prefix-match": "option",  # Enable/disable prefix matching in the cache.
    "cache-mem-permille": "integer",  # Maximum permille of available memory allocated to caching (1
    "ovrd-auth-port-http": "integer",  # Port to use for FortiGuard Web Filter HTTP override authenti
    "ovrd-auth-port-https": "integer",  # Port to use for FortiGuard Web Filter HTTPS override authent
    "ovrd-auth-port-https-flow": "integer",  # Port to use for FortiGuard Web Filter HTTPS override authent
    "ovrd-auth-port-warning": "integer",  # Port to use for FortiGuard Web Filter Warning override authe
    "ovrd-auth-https": "option",  # Enable/disable use of HTTPS for override authentication.
    "warn-auth-https": "option",  # Enable/disable use of HTTPS for warning and authentication.
    "close-ports": "option",  # Close ports used for HTTP/HTTPS override authentication and 
    "request-packet-size-limit": "integer",  # Limit size of URL request packets sent to FortiGuard server 
    "embed-image": "option",  # Enable/disable embedding images into replacement messages (d
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "cache-mode": "Cache entry expiration mode.",
    "cache-prefix-match": "Enable/disable prefix matching in the cache.",
    "cache-mem-permille": "Maximum permille of available memory allocated to caching (1 - 150).",
    "ovrd-auth-port-http": "Port to use for FortiGuard Web Filter HTTP override authentication.",
    "ovrd-auth-port-https": "Port to use for FortiGuard Web Filter HTTPS override authentication in proxy mode.",
    "ovrd-auth-port-https-flow": "Port to use for FortiGuard Web Filter HTTPS override authentication in flow mode.",
    "ovrd-auth-port-warning": "Port to use for FortiGuard Web Filter Warning override authentication.",
    "ovrd-auth-https": "Enable/disable use of HTTPS for override authentication.",
    "warn-auth-https": "Enable/disable use of HTTPS for warning and authentication.",
    "close-ports": "Close ports used for HTTP/HTTPS override authentication and disable user overrides.",
    "request-packet-size-limit": "Limit size of URL request packets sent to FortiGuard server (0 for default).",
    "embed-image": "Enable/disable embedding images into replacement messages (default = enable).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "cache-mem-permille": {"type": "integer", "min": 1, "max": 150},
    "ovrd-auth-port-http": {"type": "integer", "min": 0, "max": 65535},
    "ovrd-auth-port-https": {"type": "integer", "min": 0, "max": 65535},
    "ovrd-auth-port-https-flow": {"type": "integer", "min": 0, "max": 65535},
    "ovrd-auth-port-warning": {"type": "integer", "min": 0, "max": 65535},
    "request-packet-size-limit": {"type": "integer", "min": 576, "max": 10000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_CACHE_MODE = [
    "ttl",
    "db-ver",
]
VALID_BODY_CACHE_PREFIX_MATCH = [
    "enable",
    "disable",
]
VALID_BODY_OVRD_AUTH_HTTPS = [
    "enable",
    "disable",
]
VALID_BODY_WARN_AUTH_HTTPS = [
    "enable",
    "disable",
]
VALID_BODY_CLOSE_PORTS = [
    "enable",
    "disable",
]
VALID_BODY_EMBED_IMAGE = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_webfilter_fortiguard_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for webfilter/fortiguard.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_webfilter_fortiguard_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_webfilter_fortiguard_get(
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
    Validate required fields for webfilter/fortiguard.

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


def validate_webfilter_fortiguard_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new webfilter/fortiguard object.

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
        >>> is_valid, error = validate_webfilter_fortiguard_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "cache-mode": "ttl",  # Valid enum value
        ... }
        >>> is_valid, error = validate_webfilter_fortiguard_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["cache-mode"] = "invalid-value"
        >>> is_valid, error = validate_webfilter_fortiguard_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_webfilter_fortiguard_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "cache-mode" in payload:
        value = payload["cache-mode"]
        if value not in VALID_BODY_CACHE_MODE:
            desc = FIELD_DESCRIPTIONS.get("cache-mode", "")
            error_msg = f"Invalid value for 'cache-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CACHE_MODE)}"
            error_msg += f"\n  → Example: cache-mode='{{ VALID_BODY_CACHE_MODE[0] }}'"
            return (False, error_msg)
    if "cache-prefix-match" in payload:
        value = payload["cache-prefix-match"]
        if value not in VALID_BODY_CACHE_PREFIX_MATCH:
            desc = FIELD_DESCRIPTIONS.get("cache-prefix-match", "")
            error_msg = f"Invalid value for 'cache-prefix-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CACHE_PREFIX_MATCH)}"
            error_msg += f"\n  → Example: cache-prefix-match='{{ VALID_BODY_CACHE_PREFIX_MATCH[0] }}'"
            return (False, error_msg)
    if "ovrd-auth-https" in payload:
        value = payload["ovrd-auth-https"]
        if value not in VALID_BODY_OVRD_AUTH_HTTPS:
            desc = FIELD_DESCRIPTIONS.get("ovrd-auth-https", "")
            error_msg = f"Invalid value for 'ovrd-auth-https': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVRD_AUTH_HTTPS)}"
            error_msg += f"\n  → Example: ovrd-auth-https='{{ VALID_BODY_OVRD_AUTH_HTTPS[0] }}'"
            return (False, error_msg)
    if "warn-auth-https" in payload:
        value = payload["warn-auth-https"]
        if value not in VALID_BODY_WARN_AUTH_HTTPS:
            desc = FIELD_DESCRIPTIONS.get("warn-auth-https", "")
            error_msg = f"Invalid value for 'warn-auth-https': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WARN_AUTH_HTTPS)}"
            error_msg += f"\n  → Example: warn-auth-https='{{ VALID_BODY_WARN_AUTH_HTTPS[0] }}'"
            return (False, error_msg)
    if "close-ports" in payload:
        value = payload["close-ports"]
        if value not in VALID_BODY_CLOSE_PORTS:
            desc = FIELD_DESCRIPTIONS.get("close-ports", "")
            error_msg = f"Invalid value for 'close-ports': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLOSE_PORTS)}"
            error_msg += f"\n  → Example: close-ports='{{ VALID_BODY_CLOSE_PORTS[0] }}'"
            return (False, error_msg)
    if "embed-image" in payload:
        value = payload["embed-image"]
        if value not in VALID_BODY_EMBED_IMAGE:
            desc = FIELD_DESCRIPTIONS.get("embed-image", "")
            error_msg = f"Invalid value for 'embed-image': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EMBED_IMAGE)}"
            error_msg += f"\n  → Example: embed-image='{{ VALID_BODY_EMBED_IMAGE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_webfilter_fortiguard_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update webfilter/fortiguard.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_webfilter_fortiguard_put(payload)
    """
    # Step 1: Validate enum values
    if "cache-mode" in payload:
        value = payload["cache-mode"]
        if value not in VALID_BODY_CACHE_MODE:
            return (
                False,
                f"Invalid value for 'cache-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_MODE)}",
            )
    if "cache-prefix-match" in payload:
        value = payload["cache-prefix-match"]
        if value not in VALID_BODY_CACHE_PREFIX_MATCH:
            return (
                False,
                f"Invalid value for 'cache-prefix-match'='{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_PREFIX_MATCH)}",
            )
    if "ovrd-auth-https" in payload:
        value = payload["ovrd-auth-https"]
        if value not in VALID_BODY_OVRD_AUTH_HTTPS:
            return (
                False,
                f"Invalid value for 'ovrd-auth-https'='{value}'. Must be one of: {', '.join(VALID_BODY_OVRD_AUTH_HTTPS)}",
            )
    if "warn-auth-https" in payload:
        value = payload["warn-auth-https"]
        if value not in VALID_BODY_WARN_AUTH_HTTPS:
            return (
                False,
                f"Invalid value for 'warn-auth-https'='{value}'. Must be one of: {', '.join(VALID_BODY_WARN_AUTH_HTTPS)}",
            )
    if "close-ports" in payload:
        value = payload["close-ports"]
        if value not in VALID_BODY_CLOSE_PORTS:
            return (
                False,
                f"Invalid value for 'close-ports'='{value}'. Must be one of: {', '.join(VALID_BODY_CLOSE_PORTS)}",
            )
    if "embed-image" in payload:
        value = payload["embed-image"]
        if value not in VALID_BODY_EMBED_IMAGE:
            return (
                False,
                f"Invalid value for 'embed-image'='{value}'. Must be one of: {', '.join(VALID_BODY_EMBED_IMAGE)}",
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
    "endpoint": "webfilter/fortiguard",
    "category": "cmdb",
    "api_path": "webfilter/fortiguard",
    "help": "Configure FortiGuard Web Filter service.",
    "total_fields": 12,
    "required_fields_count": 0,
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
