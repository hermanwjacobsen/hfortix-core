"""
Validation helpers for router/multicast endpoint.

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
    "route-threshold": "",
    "route-limit": 2147483647,
    "multicast-routing": "disable",
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
    "route-threshold": "integer",  # Generate warnings when the number of multicast routes exceed
    "route-limit": "integer",  # Maximum number of multicast routes.
    "multicast-routing": "option",  # Enable/disable IP multicast routing.
    "pim-sm-global": "string",  # PIM sparse-mode global settings.
    "pim-sm-global-vrf": "string",  # per-VRF PIM sparse-mode global settings.
    "interface": "string",  # PIM interfaces.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "route-threshold": "Generate warnings when the number of multicast routes exceeds this number, must not be greater than route-limit.",
    "route-limit": "Maximum number of multicast routes.",
    "multicast-routing": "Enable/disable IP multicast routing.",
    "pim-sm-global": "PIM sparse-mode global settings.",
    "pim-sm-global-vrf": "per-VRF PIM sparse-mode global settings.",
    "interface": "PIM interfaces.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "route-threshold": {"type": "integer", "min": 1, "max": 2147483647},
    "route-limit": {"type": "integer", "min": 1, "max": 2147483647},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "pim-sm-global": {
        "message-interval": {
            "type": "integer",
            "help": "Period of time between sending periodic PIM join/prune messages in seconds (1 - 65535, default = 60).",
            "default": 60,
            "min_value": 1,
            "max_value": 65535,
        },
        "join-prune-holdtime": {
            "type": "integer",
            "help": "Join/prune holdtime (1 - 65535, default = 210).",
            "default": 210,
            "min_value": 1,
            "max_value": 65535,
        },
        "accept-register-list": {
            "type": "string",
            "help": "Sources allowed to register packets with this Rendezvous Point (RP).",
            "default": "",
            "max_length": 35,
        },
        "accept-source-list": {
            "type": "string",
            "help": "Sources allowed to send multicast traffic.",
            "default": "",
            "max_length": 35,
        },
        "bsr-candidate": {
            "type": "option",
            "help": "Enable/disable allowing this router to become a bootstrap router (BSR).",
            "default": "disable",
            "options": [{"help": "Allow this router to function as a BSR.", "label": "Enable", "name": "enable"}, {"help": "Do not allow this router to function as a BSR.", "label": "Disable", "name": "disable"}],
        },
        "bsr-interface": {
            "type": "string",
            "help": "Interface to advertise as candidate BSR.",
            "default": "",
            "max_length": 15,
        },
        "bsr-priority": {
            "type": "integer",
            "help": "BSR priority (0 - 255, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "bsr-hash": {
            "type": "integer",
            "help": "BSR hash length (0 - 32, default = 10).",
            "default": 10,
            "min_value": 0,
            "max_value": 32,
        },
        "bsr-allow-quick-refresh": {
            "type": "option",
            "help": "Enable/disable accept BSR quick refresh packets from neighbors.",
            "default": "disable",
            "options": [{"help": "Allow quick refresh packets.", "label": "Enable", "name": "enable"}, {"help": "Do not allow quick refresh packets.", "label": "Disable", "name": "disable"}],
        },
        "cisco-crp-prefix": {
            "type": "option",
            "help": "Enable/disable making candidate RP compatible with old Cisco IOS.",
            "default": "disable",
            "options": [{"help": "Do not allow sending group prefix of zero.", "label": "Enable", "name": "enable"}, {"help": "Allow sending group prefix of zero.", "label": "Disable", "name": "disable"}],
        },
        "cisco-register-checksum": {
            "type": "option",
            "help": "Checksum entire register packet(for old Cisco IOS compatibility).",
            "default": "disable",
            "options": [{"help": "register checksum entire packet.", "label": "Enable", "name": "enable"}, {"help": "Do not register checksum entire packet.", "label": "Disable", "name": "disable"}],
        },
        "cisco-register-checksum-group": {
            "type": "string",
            "help": "Cisco register checksum only these groups.",
            "default": "",
            "max_length": 35,
        },
        "cisco-ignore-rp-set-priority": {
            "type": "option",
            "help": "Use only hash for RP selection (compatibility with old Cisco IOS).",
            "default": "disable",
            "options": [{"help": "Ignore RP-SET priority value.", "label": "Enable", "name": "enable"}, {"help": "Do not ignore RP-SET priority value.", "label": "Disable", "name": "disable"}],
        },
        "register-rp-reachability": {
            "type": "option",
            "help": "Enable/disable check RP is reachable before registering packets.",
            "default": "enable",
            "options": [{"help": "Check target RP is unicast reachable before registering.", "label": "Enable", "name": "enable"}, {"help": "Do not check RP unicast reachability.", "label": "Disable", "name": "disable"}],
        },
        "register-source": {
            "type": "option",
            "help": "Override source address in register packets.",
            "default": "disable",
            "options": [{"help": "Use source address of RPF interface.", "label": "Disable", "name": "disable"}, {"help": "Use primary IP of an interface.", "label": "Interface", "name": "interface"}, {"help": "Use a local IP address.", "label": "Ip Address", "name": "ip-address"}],
        },
        "register-source-interface": {
            "type": "string",
            "help": "Override with primary interface address.",
            "default": "",
            "max_length": 15,
        },
        "register-source-ip": {
            "type": "ipv4-address",
            "help": "Override with local IP address.",
            "default": "0.0.0.0",
        },
        "register-supression": {
            "type": "integer",
            "help": "Period of time to honor register-stop message (1 - 65535 sec, default = 60).",
            "default": 60,
            "min_value": 1,
            "max_value": 65535,
        },
        "null-register-retries": {
            "type": "integer",
            "help": "Maximum retries of null register (1 - 20, default = 1).",
            "default": 1,
            "min_value": 1,
            "max_value": 20,
        },
        "rp-register-keepalive": {
            "type": "integer",
            "help": "Timeout for RP receiving data on (S,G) tree (1 - 65535 sec, default = 185).",
            "default": 185,
            "min_value": 1,
            "max_value": 65535,
        },
        "spt-threshold": {
            "type": "option",
            "help": "Enable/disable switching to source specific trees.",
            "default": "enable",
            "options": [{"help": "Switch to Source tree when available.", "label": "Enable", "name": "enable"}, {"help": "Do not switch to Source tree when available.", "label": "Disable", "name": "disable"}],
        },
        "spt-threshold-group": {
            "type": "string",
            "help": "Groups allowed to switch to source tree.",
            "default": "",
            "max_length": 35,
        },
        "ssm": {
            "type": "option",
            "help": "Enable/disable source specific multicast.",
            "default": "disable",
            "options": [{"help": "Allow source specific multicast.", "label": "Enable", "name": "enable"}, {"help": "Do not allow source specific multicast.", "label": "Disable", "name": "disable"}],
        },
        "ssm-range": {
            "type": "string",
            "help": "Groups allowed to source specific multicast.",
            "default": "",
            "max_length": 35,
        },
        "register-rate-limit": {
            "type": "integer",
            "help": "Limit of packets/sec per source registered through this RP (0 - 65535, default = 0 which means unlimited).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "pim-use-sdwan": {
            "type": "option",
            "help": "Enable/disable use of SDWAN when checking RPF neighbor and sending of REG packet.",
            "default": "disable",
            "options": [{"help": "Enable use of SDWAN when checking RPF neighbor and sending of REG packet.", "label": "Enable", "name": "enable"}, {"help": "Disable use of SDWAN when checking RPF neighbor and sending of REG packet.", "label": "Disable", "name": "disable"}],
        },
        "rp-address": {
            "type": "string",
            "help": "Statically configure RP addresses.",
        },
    },
    "pim-sm-global-vrf": {
        "vrf": {
            "type": "integer",
            "help": "VRF ID.",
            "default": 0,
            "min_value": 1,
            "max_value": 511,
        },
        "bsr-candidate": {
            "type": "option",
            "help": "Enable/disable allowing this router to become a bootstrap router (BSR).",
            "default": "disable",
            "options": [{"help": "Allow this router to function as a BSR.", "label": "Enable", "name": "enable"}, {"help": "Do not allow this router to function as a BSR.", "label": "Disable", "name": "disable"}],
        },
        "bsr-interface": {
            "type": "string",
            "help": "Interface to advertise as candidate BSR.",
            "default": "",
            "max_length": 15,
        },
        "bsr-priority": {
            "type": "integer",
            "help": "BSR priority (0 - 255, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "bsr-hash": {
            "type": "integer",
            "help": "BSR hash length (0 - 32, default = 10).",
            "default": 10,
            "min_value": 0,
            "max_value": 32,
        },
        "bsr-allow-quick-refresh": {
            "type": "option",
            "help": "Enable/disable accept BSR quick refresh packets from neighbors.",
            "default": "disable",
            "options": [{"help": "Allow quick refresh packets.", "label": "Enable", "name": "enable"}, {"help": "Do not allow quick refresh packets.", "label": "Disable", "name": "disable"}],
        },
        "cisco-crp-prefix": {
            "type": "option",
            "help": "Enable/disable making candidate RP compatible with old Cisco IOS.",
            "default": "disable",
            "options": [{"help": "Do not allow sending group prefix of zero.", "label": "Enable", "name": "enable"}, {"help": "Allow sending group prefix of zero.", "label": "Disable", "name": "disable"}],
        },
        "rp-address": {
            "type": "string",
            "help": "Statically configure RP addresses.",
        },
    },
    "interface": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 15,
        },
        "ttl-threshold": {
            "type": "integer",
            "help": "Minimum TTL of multicast packets that will be forwarded (applied only to new multicast routes) (1 - 255, default = 1).",
            "default": 1,
            "min_value": 1,
            "max_value": 255,
        },
        "pim-mode": {
            "type": "option",
            "help": "PIM operation mode.",
            "default": "sparse-mode",
            "options": [{"help": "sparse-mode", "label": "Sparse Mode", "name": "sparse-mode"}, {"help": "dense-mode", "label": "Dense Mode", "name": "dense-mode"}],
        },
        "passive": {
            "type": "option",
            "help": "Enable/disable listening to IGMP but not participating in PIM.",
            "default": "disable",
            "options": [{"help": "Listen only.", "label": "Enable", "name": "enable"}, {"help": "Participate in PIM.", "label": "Disable", "name": "disable"}],
        },
        "bfd": {
            "type": "option",
            "help": "Enable/disable Protocol Independent Multicast (PIM) Bidirectional Forwarding Detection (BFD).",
            "default": "disable",
            "options": [{"help": "Enable Protocol Independent Multicast (PIM) Bidirectional Forwarding Detection (BFD).", "label": "Enable", "name": "enable"}, {"help": "Disable Protocol Independent Multicast (PIM) Bidirectional Forwarding Detection (BFD).", "label": "Disable", "name": "disable"}],
        },
        "neighbour-filter": {
            "type": "string",
            "help": "Routers acknowledged as neighbor routers.",
            "default": "",
            "max_length": 35,
        },
        "hello-interval": {
            "type": "integer",
            "help": "Interval between sending PIM hello messages (0 - 65535 sec, default = 30).",
            "default": 30,
            "min_value": 1,
            "max_value": 65535,
        },
        "hello-holdtime": {
            "type": "integer",
            "help": "Time before old neighbor information expires (0 - 65535 sec, default = 105).",
            "default": 105,
            "min_value": 1,
            "max_value": 65535,
        },
        "cisco-exclude-genid": {
            "type": "option",
            "help": "Exclude GenID from hello packets (compatibility with old Cisco IOS).",
            "default": "disable",
            "options": [{"help": "Do not send GenID.", "label": "Enable", "name": "enable"}, {"help": "Send GenID according to standard.", "label": "Disable", "name": "disable"}],
        },
        "dr-priority": {
            "type": "integer",
            "help": "DR election priority.",
            "default": 1,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "propagation-delay": {
            "type": "integer",
            "help": "Delay flooding packets on this interface (100 - 5000 msec, default = 500).",
            "default": 500,
            "min_value": 100,
            "max_value": 5000,
        },
        "state-refresh-interval": {
            "type": "integer",
            "help": "Interval between sending state-refresh packets (1 - 100 sec, default = 60).",
            "default": 60,
            "min_value": 1,
            "max_value": 100,
        },
        "rp-candidate": {
            "type": "option",
            "help": "Enable/disable compete to become RP in elections.",
            "default": "disable",
            "options": [{"help": "Compete for RP elections.", "label": "Enable", "name": "enable"}, {"help": "Do not compete for RP elections.", "label": "Disable", "name": "disable"}],
        },
        "rp-candidate-group": {
            "type": "string",
            "help": "Multicast groups managed by this RP.",
            "default": "",
            "max_length": 35,
        },
        "rp-candidate-priority": {
            "type": "integer",
            "help": "Router's priority as RP.",
            "default": 192,
            "min_value": 0,
            "max_value": 255,
        },
        "rp-candidate-interval": {
            "type": "integer",
            "help": "RP candidate advertisement interval (1 - 16383 sec, default = 60).",
            "default": 60,
            "min_value": 1,
            "max_value": 16383,
        },
        "multicast-flow": {
            "type": "string",
            "help": "Acceptable source for multicast group.",
            "default": "",
            "max_length": 35,
        },
        "static-group": {
            "type": "string",
            "help": "Statically set multicast groups to forward out.",
            "default": "",
            "max_length": 35,
        },
        "rpf-nbr-fail-back": {
            "type": "option",
            "help": "Enable/disable fail back for RPF neighbor query.",
            "default": "disable",
            "options": [{"help": "Enable fail back for RPF neighbor query.", "label": "Enable", "name": "enable"}, {"help": "Disable fail back for RPF neighbor query.", "label": "Disable", "name": "disable"}],
        },
        "rpf-nbr-fail-back-filter": {
            "type": "string",
            "help": "Filter for fail back RPF neighbors.",
            "default": "",
            "max_length": 35,
        },
        "join-group": {
            "type": "string",
            "help": "Join multicast groups.",
        },
        "igmp": {
            "type": "string",
            "help": "IGMP configuration options.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_MULTICAST_ROUTING = [
    "enable",  # Enable IP multicast routing.
    "disable",  # Disable IP multicast routing.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_router_multicast_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for router/multicast.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_router_multicast_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_router_multicast_get(
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
    Validate required fields for router/multicast.

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


def validate_router_multicast_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new router/multicast object.

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
        >>> is_valid, error = validate_router_multicast_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "multicast-routing": "{'name': 'enable', 'help': 'Enable IP multicast routing.', 'label': 'Enable', 'description': 'Enable IP multicast routing'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_router_multicast_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["multicast-routing"] = "invalid-value"
        >>> is_valid, error = validate_router_multicast_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_router_multicast_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "multicast-routing" in payload:
        value = payload["multicast-routing"]
        if value not in VALID_BODY_MULTICAST_ROUTING:
            desc = FIELD_DESCRIPTIONS.get("multicast-routing", "")
            error_msg = f"Invalid value for 'multicast-routing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTICAST_ROUTING)}"
            error_msg += f"\n  → Example: multicast-routing='{{ VALID_BODY_MULTICAST_ROUTING[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_router_multicast_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update router/multicast.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_router_multicast_put(payload)
    """
    # Step 1: Validate enum values
    if "multicast-routing" in payload:
        value = payload["multicast-routing"]
        if value not in VALID_BODY_MULTICAST_ROUTING:
            return (
                False,
                f"Invalid value for 'multicast-routing'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_ROUTING)}",
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
    "endpoint": "router/multicast",
    "category": "cmdb",
    "api_path": "router/multicast",
    "help": "Configure router multicast.",
    "total_fields": 6,
    "required_fields_count": 0,
    "fields_with_defaults_count": 3,
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
