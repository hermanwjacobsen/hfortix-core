"""
Validation helpers for system/wccp endpoint.

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
    "service-id": "",
    "router-id": "0.0.0.0",
    "cache-id": "0.0.0.0",
    "group-address": "0.0.0.0",
    "server-list": "",
    "router-list": "",
    "ports-defined": "",
    "server-type": "forward",
    "ports": "",
    "authentication": "disable",
    "forward-method": "GRE",
    "cache-engine-method": "GRE",
    "service-type": "auto",
    "primary-hash": "dst-ip",
    "priority": 0,
    "protocol": 0,
    "assignment-weight": 0,
    "assignment-bucket-format": "cisco-implementation",
    "return-method": "GRE",
    "assignment-method": "HASH",
    "assignment-srcaddr-mask": "0.0.23.65",
    "assignment-dstaddr-mask": "0.0.0.0",
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
    "service-id": "string",  # Service ID.
    "router-id": "ipv4-address",  # IP address known to all cache engines. If all cache engines 
    "cache-id": "ipv4-address",  # IP address known to all routers. If the addresses are the sa
    "group-address": "ipv4-address-multicast",  # IP multicast address used by the cache routers. For the Fort
    "server-list": "user",  # IP addresses and netmasks for up to four cache servers.
    "router-list": "user",  # IP addresses of one or more WCCP routers.
    "ports-defined": "option",  # Match method.
    "server-type": "option",  # Cache server type.
    "ports": "user",  # Service ports.
    "authentication": "option",  # Enable/disable MD5 authentication.
    "password": "password",  # Password for MD5 authentication.
    "forward-method": "option",  # Method used to forward traffic to the cache servers.
    "cache-engine-method": "option",  # Method used to forward traffic to the routers or to return t
    "service-type": "option",  # WCCP service type used by the cache server for logical inter
    "primary-hash": "option",  # Hash method.
    "priority": "integer",  # Service priority.
    "protocol": "integer",  # Service protocol.
    "assignment-weight": "integer",  # Assignment of hash weight/ratio for the WCCP cache engine.
    "assignment-bucket-format": "option",  # Assignment bucket format for the WCCP cache engine.
    "return-method": "option",  # Method used to decline a redirected packet and return it to 
    "assignment-method": "option",  # Hash key assignment preference.
    "assignment-srcaddr-mask": "ipv4-netmask-any",  # Assignment source address mask.
    "assignment-dstaddr-mask": "ipv4-netmask-any",  # Assignment destination address mask.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "service-id": "Service ID.",
    "router-id": "IP address known to all cache engines. If all cache engines connect to the same FortiGate interface, use the default 0.0.0.0.",
    "cache-id": "IP address known to all routers. If the addresses are the same, use the default 0.0.0.0.",
    "group-address": "IP multicast address used by the cache routers. For the FortiGate to ignore multicast WCCP traffic, use the default 0.0.0.0.",
    "server-list": "IP addresses and netmasks for up to four cache servers.",
    "router-list": "IP addresses of one or more WCCP routers.",
    "ports-defined": "Match method.",
    "server-type": "Cache server type.",
    "ports": "Service ports.",
    "authentication": "Enable/disable MD5 authentication.",
    "password": "Password for MD5 authentication.",
    "forward-method": "Method used to forward traffic to the cache servers.",
    "cache-engine-method": "Method used to forward traffic to the routers or to return to the cache engine.",
    "service-type": "WCCP service type used by the cache server for logical interception and redirection of traffic.",
    "primary-hash": "Hash method.",
    "priority": "Service priority.",
    "protocol": "Service protocol.",
    "assignment-weight": "Assignment of hash weight/ratio for the WCCP cache engine.",
    "assignment-bucket-format": "Assignment bucket format for the WCCP cache engine.",
    "return-method": "Method used to decline a redirected packet and return it to the FortiGate unit.",
    "assignment-method": "Hash key assignment preference.",
    "assignment-srcaddr-mask": "Assignment source address mask.",
    "assignment-dstaddr-mask": "Assignment destination address mask.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "service-id": {"type": "string", "max_length": 3},
    "priority": {"type": "integer", "min": 0, "max": 255},
    "protocol": {"type": "integer", "min": 0, "max": 255},
    "assignment-weight": {"type": "integer", "min": 0, "max": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_PORTS_DEFINED = [
    "source",
    "destination",
]
VALID_BODY_SERVER_TYPE = [
    "forward",
    "proxy",
]
VALID_BODY_AUTHENTICATION = [
    "enable",
    "disable",
]
VALID_BODY_FORWARD_METHOD = [
    "GRE",
    "L2",
    "any",
]
VALID_BODY_CACHE_ENGINE_METHOD = [
    "GRE",
    "L2",
]
VALID_BODY_SERVICE_TYPE = [
    "auto",
    "standard",
    "dynamic",
]
VALID_BODY_PRIMARY_HASH = [
    "src-ip",
    "dst-ip",
    "src-port",
    "dst-port",
]
VALID_BODY_ASSIGNMENT_BUCKET_FORMAT = [
    "wccp-v2",
    "cisco-implementation",
]
VALID_BODY_RETURN_METHOD = [
    "GRE",
    "L2",
    "any",
]
VALID_BODY_ASSIGNMENT_METHOD = [
    "HASH",
    "MASK",
    "any",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_wccp_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/wccp.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_wccp_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by service-id
        >>> is_valid, error = validate_system_wccp_get(service_id="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_wccp_get(
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
    Validate required fields for system/wccp.

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


def validate_system_wccp_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/wccp object.

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
        >>> is_valid, error = validate_system_wccp_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "ports-defined": "source",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_wccp_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["ports-defined"] = "invalid-value"
        >>> is_valid, error = validate_system_wccp_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_wccp_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "ports-defined" in payload:
        value = payload["ports-defined"]
        if value not in VALID_BODY_PORTS_DEFINED:
            desc = FIELD_DESCRIPTIONS.get("ports-defined", "")
            error_msg = f"Invalid value for 'ports-defined': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORTS_DEFINED)}"
            error_msg += f"\n  → Example: ports-defined='{{ VALID_BODY_PORTS_DEFINED[0] }}'"
            return (False, error_msg)
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            desc = FIELD_DESCRIPTIONS.get("server-type", "")
            error_msg = f"Invalid value for 'server-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_TYPE)}"
            error_msg += f"\n  → Example: server-type='{{ VALID_BODY_SERVER_TYPE[0] }}'"
            return (False, error_msg)
    if "authentication" in payload:
        value = payload["authentication"]
        if value not in VALID_BODY_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("authentication", "")
            error_msg = f"Invalid value for 'authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHENTICATION)}"
            error_msg += f"\n  → Example: authentication='{{ VALID_BODY_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "forward-method" in payload:
        value = payload["forward-method"]
        if value not in VALID_BODY_FORWARD_METHOD:
            desc = FIELD_DESCRIPTIONS.get("forward-method", "")
            error_msg = f"Invalid value for 'forward-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORWARD_METHOD)}"
            error_msg += f"\n  → Example: forward-method='{{ VALID_BODY_FORWARD_METHOD[0] }}'"
            return (False, error_msg)
    if "cache-engine-method" in payload:
        value = payload["cache-engine-method"]
        if value not in VALID_BODY_CACHE_ENGINE_METHOD:
            desc = FIELD_DESCRIPTIONS.get("cache-engine-method", "")
            error_msg = f"Invalid value for 'cache-engine-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CACHE_ENGINE_METHOD)}"
            error_msg += f"\n  → Example: cache-engine-method='{{ VALID_BODY_CACHE_ENGINE_METHOD[0] }}'"
            return (False, error_msg)
    if "service-type" in payload:
        value = payload["service-type"]
        if value not in VALID_BODY_SERVICE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("service-type", "")
            error_msg = f"Invalid value for 'service-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVICE_TYPE)}"
            error_msg += f"\n  → Example: service-type='{{ VALID_BODY_SERVICE_TYPE[0] }}'"
            return (False, error_msg)
    if "primary-hash" in payload:
        value = payload["primary-hash"]
        if value not in VALID_BODY_PRIMARY_HASH:
            desc = FIELD_DESCRIPTIONS.get("primary-hash", "")
            error_msg = f"Invalid value for 'primary-hash': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIMARY_HASH)}"
            error_msg += f"\n  → Example: primary-hash='{{ VALID_BODY_PRIMARY_HASH[0] }}'"
            return (False, error_msg)
    if "assignment-bucket-format" in payload:
        value = payload["assignment-bucket-format"]
        if value not in VALID_BODY_ASSIGNMENT_BUCKET_FORMAT:
            desc = FIELD_DESCRIPTIONS.get("assignment-bucket-format", "")
            error_msg = f"Invalid value for 'assignment-bucket-format': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASSIGNMENT_BUCKET_FORMAT)}"
            error_msg += f"\n  → Example: assignment-bucket-format='{{ VALID_BODY_ASSIGNMENT_BUCKET_FORMAT[0] }}'"
            return (False, error_msg)
    if "return-method" in payload:
        value = payload["return-method"]
        if value not in VALID_BODY_RETURN_METHOD:
            desc = FIELD_DESCRIPTIONS.get("return-method", "")
            error_msg = f"Invalid value for 'return-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RETURN_METHOD)}"
            error_msg += f"\n  → Example: return-method='{{ VALID_BODY_RETURN_METHOD[0] }}'"
            return (False, error_msg)
    if "assignment-method" in payload:
        value = payload["assignment-method"]
        if value not in VALID_BODY_ASSIGNMENT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("assignment-method", "")
            error_msg = f"Invalid value for 'assignment-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASSIGNMENT_METHOD)}"
            error_msg += f"\n  → Example: assignment-method='{{ VALID_BODY_ASSIGNMENT_METHOD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_wccp_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/wccp.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_wccp_put(payload)
    """
    # Step 1: Validate enum values
    if "ports-defined" in payload:
        value = payload["ports-defined"]
        if value not in VALID_BODY_PORTS_DEFINED:
            return (
                False,
                f"Invalid value for 'ports-defined'='{value}'. Must be one of: {', '.join(VALID_BODY_PORTS_DEFINED)}",
            )
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid value for 'server-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )
    if "authentication" in payload:
        value = payload["authentication"]
        if value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )
    if "forward-method" in payload:
        value = payload["forward-method"]
        if value not in VALID_BODY_FORWARD_METHOD:
            return (
                False,
                f"Invalid value for 'forward-method'='{value}'. Must be one of: {', '.join(VALID_BODY_FORWARD_METHOD)}",
            )
    if "cache-engine-method" in payload:
        value = payload["cache-engine-method"]
        if value not in VALID_BODY_CACHE_ENGINE_METHOD:
            return (
                False,
                f"Invalid value for 'cache-engine-method'='{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_ENGINE_METHOD)}",
            )
    if "service-type" in payload:
        value = payload["service-type"]
        if value not in VALID_BODY_SERVICE_TYPE:
            return (
                False,
                f"Invalid value for 'service-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_TYPE)}",
            )
    if "primary-hash" in payload:
        value = payload["primary-hash"]
        if value not in VALID_BODY_PRIMARY_HASH:
            return (
                False,
                f"Invalid value for 'primary-hash'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIMARY_HASH)}",
            )
    if "assignment-bucket-format" in payload:
        value = payload["assignment-bucket-format"]
        if value not in VALID_BODY_ASSIGNMENT_BUCKET_FORMAT:
            return (
                False,
                f"Invalid value for 'assignment-bucket-format'='{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGNMENT_BUCKET_FORMAT)}",
            )
    if "return-method" in payload:
        value = payload["return-method"]
        if value not in VALID_BODY_RETURN_METHOD:
            return (
                False,
                f"Invalid value for 'return-method'='{value}'. Must be one of: {', '.join(VALID_BODY_RETURN_METHOD)}",
            )
    if "assignment-method" in payload:
        value = payload["assignment-method"]
        if value not in VALID_BODY_ASSIGNMENT_METHOD:
            return (
                False,
                f"Invalid value for 'assignment-method'='{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGNMENT_METHOD)}",
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
    "endpoint": "system/wccp",
    "category": "cmdb",
    "api_path": "system/wccp",
    "mkey": "service-id",
    "mkey_type": "string",
    "help": "Configure WCCP.",
    "total_fields": 23,
    "required_fields_count": 0,
    "fields_with_defaults_count": 22,
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
