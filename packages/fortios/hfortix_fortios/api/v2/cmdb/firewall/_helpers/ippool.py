"""
Validation helpers for firewall/ippool endpoint.

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
    "type": "overload",
    "startip": "0.0.0.0",
    "endip": "0.0.0.0",
    "startport": 5117,
    "endport": 65533,
    "source-startip": "0.0.0.0",
    "source-endip": "0.0.0.0",
    "block-size": 128,
    "port-per-user": 0,
    "num-blocks-per-user": 8,
    "pba-timeout": 30,
    "pba-interim-log": 0,
    "permit-any-host": "disable",
    "arp-reply": "enable",
    "arp-intf": "",
    "associated-interface": "",
    "nat64": "disable",
    "add-nat64-route": "enable",
    "source-prefix6": "::/0",
    "client-prefix-length": 64,
    "tcp-session-quota": 0,
    "udp-session-quota": 0,
    "icmp-session-quota": 0,
    "privileged-port-use-pba": "disable",
    "subnet-broadcast-in-ippool": "",
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
    "name": "string",  # IP pool name.
    "type": "option",  # IP pool type: overload, one-to-one, fixed-port-range, port-b
    "startip": "ipv4-address-any",  # First IPv4 address (inclusive) in the range for the address 
    "endip": "ipv4-address-any",  # Final IPv4 address (inclusive) in the range for the address 
    "startport": "integer",  # First port number (inclusive) in the range for the address p
    "endport": "integer",  # Final port number (inclusive) in the range for the address p
    "source-startip": "ipv4-address-any",  # First IPv4 address (inclusive) in the range of the source ad
    "source-endip": "ipv4-address-any",  # Final IPv4 address (inclusive) in the range of the source ad
    "block-size": "integer",  # Number of addresses in a block (64 - 4096, default = 128).
    "port-per-user": "integer",  # Number of port for each user (32 - 60416, default = 0, which
    "num-blocks-per-user": "integer",  # Number of addresses blocks that can be used by a user (1 to 
    "pba-timeout": "integer",  # Port block allocation timeout (seconds).
    "pba-interim-log": "integer",  # Port block allocation interim logging interval (600 - 86400 
    "permit-any-host": "option",  # Enable/disable full cone NAT.
    "arp-reply": "option",  # Enable/disable replying to ARP requests when an IP Pool is a
    "arp-intf": "string",  # Select an interface from available options that will reply t
    "associated-interface": "string",  # Associated interface name.
    "comments": "var-string",  # Comment.
    "nat64": "option",  # Enable/disable NAT64.
    "add-nat64-route": "option",  # Enable/disable adding NAT64 route.
    "source-prefix6": "ipv6-network",  # Source IPv6 network to be translated (format = xxxx:xxxx:xxx
    "client-prefix-length": "integer",  # Subnet length of a single deterministic NAT64 client (1 - 12
    "tcp-session-quota": "integer",  # Maximum number of concurrent TCP sessions allowed per client
    "udp-session-quota": "integer",  # Maximum number of concurrent UDP sessions allowed per client
    "icmp-session-quota": "integer",  # Maximum number of concurrent ICMP sessions allowed per clien
    "privileged-port-use-pba": "option",  # Enable/disable selection of the external port from the port 
    "subnet-broadcast-in-ippool": "option",  # Enable/disable inclusion of the subnetwork address and broad
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "IP pool name.",
    "type": "IP pool type: overload, one-to-one, fixed-port-range, port-block-allocation, cgn-resource-allocation (hyperscale vdom only)",
    "startip": "First IPv4 address (inclusive) in the range for the address pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).",
    "endip": "Final IPv4 address (inclusive) in the range for the address pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).",
    "startport": "First port number (inclusive) in the range for the address pool (1024 - 65535, Default: 5117).",
    "endport": "Final port number (inclusive) in the range for the address pool (1024 - 65535, Default: 65533).",
    "source-startip": "First IPv4 address (inclusive) in the range of the source addresses to be translated (format = xxx.xxx.xxx.xxx, default = 0.0.0.0).",
    "source-endip": "Final IPv4 address (inclusive) in the range of the source addresses to be translated (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).",
    "block-size": "Number of addresses in a block (64 - 4096, default = 128).",
    "port-per-user": "Number of port for each user (32 - 60416, default = 0, which is auto).",
    "num-blocks-per-user": "Number of addresses blocks that can be used by a user (1 to 128, default = 8).",
    "pba-timeout": "Port block allocation timeout (seconds).",
    "pba-interim-log": "Port block allocation interim logging interval (600 - 86400 seconds, default = 0 which disables interim logging).",
    "permit-any-host": "Enable/disable full cone NAT.",
    "arp-reply": "Enable/disable replying to ARP requests when an IP Pool is added to a policy (default = enable).",
    "arp-intf": "Select an interface from available options that will reply to ARP requests. (If blank, any is selected).",
    "associated-interface": "Associated interface name.",
    "comments": "Comment.",
    "nat64": "Enable/disable NAT64.",
    "add-nat64-route": "Enable/disable adding NAT64 route.",
    "source-prefix6": "Source IPv6 network to be translated (format = xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx, default = ::/0).",
    "client-prefix-length": "Subnet length of a single deterministic NAT64 client (1 - 128, default = 64).",
    "tcp-session-quota": "Maximum number of concurrent TCP sessions allowed per client (0 - 2097000, default = 0 which means no limit).",
    "udp-session-quota": "Maximum number of concurrent UDP sessions allowed per client (0 - 2097000, default = 0 which means no limit).",
    "icmp-session-quota": "Maximum number of concurrent ICMP sessions allowed per client (0 - 2097000, default = 0 which means no limit).",
    "privileged-port-use-pba": "Enable/disable selection of the external port from the port block allocation for NAT'ing privileged ports (deafult = disable).",
    "subnet-broadcast-in-ippool": "Enable/disable inclusion of the subnetwork address and broadcast IP address in the NAT64 IP pool.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "startport": {"type": "integer", "min": 1024, "max": 65535},
    "endport": {"type": "integer", "min": 1024, "max": 65535},
    "block-size": {"type": "integer", "min": 64, "max": 4096},
    "port-per-user": {"type": "integer", "min": 32, "max": 60417},
    "num-blocks-per-user": {"type": "integer", "min": 1, "max": 128},
    "pba-timeout": {"type": "integer", "min": 3, "max": 86400},
    "pba-interim-log": {"type": "integer", "min": 600, "max": 86400},
    "arp-intf": {"type": "string", "max_length": 15},
    "associated-interface": {"type": "string", "max_length": 15},
    "client-prefix-length": {"type": "integer", "min": 1, "max": 128},
    "tcp-session-quota": {"type": "integer", "min": 0, "max": 2097000},
    "udp-session-quota": {"type": "integer", "min": 0, "max": 2097000},
    "icmp-session-quota": {"type": "integer", "min": 0, "max": 2097000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "overload",
    "one-to-one",
    "fixed-port-range",
    "port-block-allocation",
]
VALID_BODY_PERMIT_ANY_HOST = [
    "disable",
    "enable",
]
VALID_BODY_ARP_REPLY = [
    "disable",
    "enable",
]
VALID_BODY_NAT64 = [
    "disable",
    "enable",
]
VALID_BODY_ADD_NAT64_ROUTE = [
    "disable",
    "enable",
]
VALID_BODY_PRIVILEGED_PORT_USE_PBA = [
    "disable",
    "enable",
]
VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL = [
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_ippool_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for firewall/ippool.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_firewall_ippool_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_firewall_ippool_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_firewall_ippool_get(
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
    Validate required fields for firewall/ippool.

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


def validate_firewall_ippool_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new firewall/ippool object.

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
        >>> is_valid, error = validate_firewall_ippool_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "type": "overload",  # Valid enum value
        ... }
        >>> is_valid, error = validate_firewall_ippool_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["type"] = "invalid-value"
        >>> is_valid, error = validate_firewall_ippool_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_firewall_ippool_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
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
    if "permit-any-host" in payload:
        value = payload["permit-any-host"]
        if value not in VALID_BODY_PERMIT_ANY_HOST:
            desc = FIELD_DESCRIPTIONS.get("permit-any-host", "")
            error_msg = f"Invalid value for 'permit-any-host': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERMIT_ANY_HOST)}"
            error_msg += f"\n  → Example: permit-any-host='{{ VALID_BODY_PERMIT_ANY_HOST[0] }}'"
            return (False, error_msg)
    if "arp-reply" in payload:
        value = payload["arp-reply"]
        if value not in VALID_BODY_ARP_REPLY:
            desc = FIELD_DESCRIPTIONS.get("arp-reply", "")
            error_msg = f"Invalid value for 'arp-reply': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ARP_REPLY)}"
            error_msg += f"\n  → Example: arp-reply='{{ VALID_BODY_ARP_REPLY[0] }}'"
            return (False, error_msg)
    if "nat64" in payload:
        value = payload["nat64"]
        if value not in VALID_BODY_NAT64:
            desc = FIELD_DESCRIPTIONS.get("nat64", "")
            error_msg = f"Invalid value for 'nat64': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT64)}"
            error_msg += f"\n  → Example: nat64='{{ VALID_BODY_NAT64[0] }}'"
            return (False, error_msg)
    if "add-nat64-route" in payload:
        value = payload["add-nat64-route"]
        if value not in VALID_BODY_ADD_NAT64_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("add-nat64-route", "")
            error_msg = f"Invalid value for 'add-nat64-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADD_NAT64_ROUTE)}"
            error_msg += f"\n  → Example: add-nat64-route='{{ VALID_BODY_ADD_NAT64_ROUTE[0] }}'"
            return (False, error_msg)
    if "privileged-port-use-pba" in payload:
        value = payload["privileged-port-use-pba"]
        if value not in VALID_BODY_PRIVILEGED_PORT_USE_PBA:
            desc = FIELD_DESCRIPTIONS.get("privileged-port-use-pba", "")
            error_msg = f"Invalid value for 'privileged-port-use-pba': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIVILEGED_PORT_USE_PBA)}"
            error_msg += f"\n  → Example: privileged-port-use-pba='{{ VALID_BODY_PRIVILEGED_PORT_USE_PBA[0] }}'"
            return (False, error_msg)
    if "subnet-broadcast-in-ippool" in payload:
        value = payload["subnet-broadcast-in-ippool"]
        if value not in VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL:
            desc = FIELD_DESCRIPTIONS.get("subnet-broadcast-in-ippool", "")
            error_msg = f"Invalid value for 'subnet-broadcast-in-ippool': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL)}"
            error_msg += f"\n  → Example: subnet-broadcast-in-ippool='{{ VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_ippool_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update firewall/ippool.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_firewall_ippool_put(payload)
    """
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "permit-any-host" in payload:
        value = payload["permit-any-host"]
        if value not in VALID_BODY_PERMIT_ANY_HOST:
            return (
                False,
                f"Invalid value for 'permit-any-host'='{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_ANY_HOST)}",
            )
    if "arp-reply" in payload:
        value = payload["arp-reply"]
        if value not in VALID_BODY_ARP_REPLY:
            return (
                False,
                f"Invalid value for 'arp-reply'='{value}'. Must be one of: {', '.join(VALID_BODY_ARP_REPLY)}",
            )
    if "nat64" in payload:
        value = payload["nat64"]
        if value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid value for 'nat64'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )
    if "add-nat64-route" in payload:
        value = payload["add-nat64-route"]
        if value not in VALID_BODY_ADD_NAT64_ROUTE:
            return (
                False,
                f"Invalid value for 'add-nat64-route'='{value}'. Must be one of: {', '.join(VALID_BODY_ADD_NAT64_ROUTE)}",
            )
    if "privileged-port-use-pba" in payload:
        value = payload["privileged-port-use-pba"]
        if value not in VALID_BODY_PRIVILEGED_PORT_USE_PBA:
            return (
                False,
                f"Invalid value for 'privileged-port-use-pba'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIVILEGED_PORT_USE_PBA)}",
            )
    if "subnet-broadcast-in-ippool" in payload:
        value = payload["subnet-broadcast-in-ippool"]
        if value not in VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL:
            return (
                False,
                f"Invalid value for 'subnet-broadcast-in-ippool'='{value}'. Must be one of: {', '.join(VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL)}",
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
    "endpoint": "firewall/ippool",
    "category": "cmdb",
    "api_path": "firewall/ippool",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure IPv4 IP pools.",
    "total_fields": 27,
    "required_fields_count": 0,
    "fields_with_defaults_count": 26,
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
