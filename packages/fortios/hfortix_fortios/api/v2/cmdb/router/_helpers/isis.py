"""
Validation helpers for router/isis endpoint.

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
    "is-type": "level-1-2",
    "adv-passive-only": "disable",
    "adv-passive-only6": "disable",
    "auth-mode-l1": "password",
    "auth-mode-l2": "password",
    "auth-keychain-l1": "",
    "auth-keychain-l2": "",
    "auth-sendonly-l1": "disable",
    "auth-sendonly-l2": "disable",
    "ignore-lsp-errors": "disable",
    "lsp-gen-interval-l1": 30,
    "lsp-gen-interval-l2": 30,
    "lsp-refresh-interval": 900,
    "max-lsp-lifetime": 1200,
    "spf-interval-exp-l1": "",
    "spf-interval-exp-l2": "",
    "dynamic-hostname": "disable",
    "adjacency-check": "disable",
    "adjacency-check6": "disable",
    "overload-bit": "disable",
    "overload-bit-suppress": "",
    "overload-bit-on-startup": 0,
    "default-originate": "disable",
    "default-originate6": "disable",
    "metric-style": "narrow",
    "redistribute-l1": "disable",
    "redistribute-l1-list": "",
    "redistribute-l2": "disable",
    "redistribute-l2-list": "",
    "redistribute6-l1": "disable",
    "redistribute6-l1-list": "",
    "redistribute6-l2": "disable",
    "redistribute6-l2-list": "",
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
    "is-type": "option",  # IS type.
    "adv-passive-only": "option",  # Enable/disable IS-IS advertisement of passive interfaces onl
    "adv-passive-only6": "option",  # Enable/disable IPv6 IS-IS advertisement of passive interface
    "auth-mode-l1": "option",  # Level 1 authentication mode.
    "auth-mode-l2": "option",  # Level 2 authentication mode.
    "auth-password-l1": "password",  # Authentication password for level 1 PDUs.
    "auth-password-l2": "password",  # Authentication password for level 2 PDUs.
    "auth-keychain-l1": "string",  # Authentication key-chain for level 1 PDUs.
    "auth-keychain-l2": "string",  # Authentication key-chain for level 2 PDUs.
    "auth-sendonly-l1": "option",  # Enable/disable level 1 authentication send-only.
    "auth-sendonly-l2": "option",  # Enable/disable level 2 authentication send-only.
    "ignore-lsp-errors": "option",  # Enable/disable ignoring of LSP errors with bad checksums.
    "lsp-gen-interval-l1": "integer",  # Minimum interval for level 1 LSP regenerating.
    "lsp-gen-interval-l2": "integer",  # Minimum interval for level 2 LSP regenerating.
    "lsp-refresh-interval": "integer",  # LSP refresh time in seconds.
    "max-lsp-lifetime": "integer",  # Maximum LSP lifetime in seconds.
    "spf-interval-exp-l1": "user",  # Level 1 SPF calculation delay.
    "spf-interval-exp-l2": "user",  # Level 2 SPF calculation delay.
    "dynamic-hostname": "option",  # Enable/disable dynamic hostname.
    "adjacency-check": "option",  # Enable/disable adjacency check.
    "adjacency-check6": "option",  # Enable/disable IPv6 adjacency check.
    "overload-bit": "option",  # Enable/disable signal other routers not to use us in SPF.
    "overload-bit-suppress": "option",  # Suppress overload-bit for the specific prefixes.
    "overload-bit-on-startup": "integer",  # Overload-bit only temporarily after reboot.
    "default-originate": "option",  # Enable/disable distribution of default route information.
    "default-originate6": "option",  # Enable/disable distribution of default IPv6 route informatio
    "metric-style": "option",  # Use old-style (ISO 10589) or new-style packet formats.
    "redistribute-l1": "option",  # Enable/disable redistribution of level 1 routes into level 2
    "redistribute-l1-list": "string",  # Access-list for route redistribution from l1 to l2.
    "redistribute-l2": "option",  # Enable/disable redistribution of level 2 routes into level 1
    "redistribute-l2-list": "string",  # Access-list for route redistribution from l2 to l1.
    "redistribute6-l1": "option",  # Enable/disable redistribution of level 1 IPv6 routes into le
    "redistribute6-l1-list": "string",  # Access-list for IPv6 route redistribution from l1 to l2.
    "redistribute6-l2": "option",  # Enable/disable redistribution of level 2 IPv6 routes into le
    "redistribute6-l2-list": "string",  # Access-list for IPv6 route redistribution from l2 to l1.
    "isis-net": "string",  # IS-IS net configuration.
    "isis-interface": "string",  # IS-IS interface configuration.
    "summary-address": "string",  # IS-IS summary addresses.
    "summary-address6": "string",  # IS-IS IPv6 summary address.
    "redistribute": "string",  # IS-IS redistribute protocols.
    "redistribute6": "string",  # IS-IS IPv6 redistribution for routing protocols.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "is-type": "IS type.",
    "adv-passive-only": "Enable/disable IS-IS advertisement of passive interfaces only.",
    "adv-passive-only6": "Enable/disable IPv6 IS-IS advertisement of passive interfaces only.",
    "auth-mode-l1": "Level 1 authentication mode.",
    "auth-mode-l2": "Level 2 authentication mode.",
    "auth-password-l1": "Authentication password for level 1 PDUs.",
    "auth-password-l2": "Authentication password for level 2 PDUs.",
    "auth-keychain-l1": "Authentication key-chain for level 1 PDUs.",
    "auth-keychain-l2": "Authentication key-chain for level 2 PDUs.",
    "auth-sendonly-l1": "Enable/disable level 1 authentication send-only.",
    "auth-sendonly-l2": "Enable/disable level 2 authentication send-only.",
    "ignore-lsp-errors": "Enable/disable ignoring of LSP errors with bad checksums.",
    "lsp-gen-interval-l1": "Minimum interval for level 1 LSP regenerating.",
    "lsp-gen-interval-l2": "Minimum interval for level 2 LSP regenerating.",
    "lsp-refresh-interval": "LSP refresh time in seconds.",
    "max-lsp-lifetime": "Maximum LSP lifetime in seconds.",
    "spf-interval-exp-l1": "Level 1 SPF calculation delay.",
    "spf-interval-exp-l2": "Level 2 SPF calculation delay.",
    "dynamic-hostname": "Enable/disable dynamic hostname.",
    "adjacency-check": "Enable/disable adjacency check.",
    "adjacency-check6": "Enable/disable IPv6 adjacency check.",
    "overload-bit": "Enable/disable signal other routers not to use us in SPF.",
    "overload-bit-suppress": "Suppress overload-bit for the specific prefixes.",
    "overload-bit-on-startup": "Overload-bit only temporarily after reboot.",
    "default-originate": "Enable/disable distribution of default route information.",
    "default-originate6": "Enable/disable distribution of default IPv6 route information.",
    "metric-style": "Use old-style (ISO 10589) or new-style packet formats.",
    "redistribute-l1": "Enable/disable redistribution of level 1 routes into level 2.",
    "redistribute-l1-list": "Access-list for route redistribution from l1 to l2.",
    "redistribute-l2": "Enable/disable redistribution of level 2 routes into level 1.",
    "redistribute-l2-list": "Access-list for route redistribution from l2 to l1.",
    "redistribute6-l1": "Enable/disable redistribution of level 1 IPv6 routes into level 2.",
    "redistribute6-l1-list": "Access-list for IPv6 route redistribution from l1 to l2.",
    "redistribute6-l2": "Enable/disable redistribution of level 2 IPv6 routes into level 1.",
    "redistribute6-l2-list": "Access-list for IPv6 route redistribution from l2 to l1.",
    "isis-net": "IS-IS net configuration.",
    "isis-interface": "IS-IS interface configuration.",
    "summary-address": "IS-IS summary addresses.",
    "summary-address6": "IS-IS IPv6 summary address.",
    "redistribute": "IS-IS redistribute protocols.",
    "redistribute6": "IS-IS IPv6 redistribution for routing protocols.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "auth-keychain-l1": {"type": "string", "max_length": 35},
    "auth-keychain-l2": {"type": "string", "max_length": 35},
    "lsp-gen-interval-l1": {"type": "integer", "min": 1, "max": 120},
    "lsp-gen-interval-l2": {"type": "integer", "min": 1, "max": 120},
    "lsp-refresh-interval": {"type": "integer", "min": 1, "max": 65535},
    "max-lsp-lifetime": {"type": "integer", "min": 350, "max": 65535},
    "overload-bit-on-startup": {"type": "integer", "min": 5, "max": 86400},
    "redistribute-l1-list": {"type": "string", "max_length": 35},
    "redistribute-l2-list": {"type": "string", "max_length": 35},
    "redistribute6-l1-list": {"type": "string", "max_length": 35},
    "redistribute6-l2-list": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "isis-net": {
        "id": {
            "type": "integer",
            "help": "ISIS network ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "net": {
            "type": "user",
            "help": "IS-IS networks (format = xx.xxxx.  .xxxx.xx.).",
            "default": "",
        },
    },
    "isis-interface": {
        "name": {
            "type": "string",
            "help": "IS-IS interface name.",
            "default": "",
            "max_length": 15,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable interface for IS-IS.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "status6": {
            "type": "option",
            "help": "Enable/disable IPv6 interface for IS-IS.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "network-type": {
            "type": "option",
            "help": "IS-IS interface's network type.",
            "default": "",
            "options": ["broadcast", "point-to-point", "loopback"],
        },
        "circuit-type": {
            "type": "option",
            "help": "IS-IS interface's circuit type.",
            "default": "level-1-2",
            "options": ["level-1-2", "level-1", "level-2"],
        },
        "csnp-interval-l1": {
            "type": "integer",
            "help": "Level 1 CSNP interval.",
            "default": 10,
            "min_value": 1,
            "max_value": 65535,
        },
        "csnp-interval-l2": {
            "type": "integer",
            "help": "Level 2 CSNP interval.",
            "default": 10,
            "min_value": 1,
            "max_value": 65535,
        },
        "hello-interval-l1": {
            "type": "integer",
            "help": "Level 1 hello interval.",
            "default": 10,
            "min_value": 0,
            "max_value": 65535,
        },
        "hello-interval-l2": {
            "type": "integer",
            "help": "Level 2 hello interval.",
            "default": 10,
            "min_value": 0,
            "max_value": 65535,
        },
        "hello-multiplier-l1": {
            "type": "integer",
            "help": "Level 1 multiplier for Hello holding time.",
            "default": 3,
            "min_value": 2,
            "max_value": 100,
        },
        "hello-multiplier-l2": {
            "type": "integer",
            "help": "Level 2 multiplier for Hello holding time.",
            "default": 3,
            "min_value": 2,
            "max_value": 100,
        },
        "hello-padding": {
            "type": "option",
            "help": "Enable/disable padding to IS-IS hello packets.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "lsp-interval": {
            "type": "integer",
            "help": "LSP transmission interval (milliseconds).",
            "default": 33,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "lsp-retransmit-interval": {
            "type": "integer",
            "help": "LSP retransmission interval (sec).",
            "default": 5,
            "min_value": 1,
            "max_value": 65535,
        },
        "metric-l1": {
            "type": "integer",
            "help": "Level 1 metric for interface.",
            "default": 10,
            "min_value": 1,
            "max_value": 63,
        },
        "metric-l2": {
            "type": "integer",
            "help": "Level 2 metric for interface.",
            "default": 10,
            "min_value": 1,
            "max_value": 63,
        },
        "wide-metric-l1": {
            "type": "integer",
            "help": "Level 1 wide metric for interface.",
            "default": 10,
            "min_value": 1,
            "max_value": 16777214,
        },
        "wide-metric-l2": {
            "type": "integer",
            "help": "Level 2 wide metric for interface.",
            "default": 10,
            "min_value": 1,
            "max_value": 16777214,
        },
        "auth-password-l1": {
            "type": "password",
            "help": "Authentication password for level 1 PDUs.",
            "max_length": 128,
        },
        "auth-password-l2": {
            "type": "password",
            "help": "Authentication password for level 2 PDUs.",
            "max_length": 128,
        },
        "auth-keychain-l1": {
            "type": "string",
            "help": "Authentication key-chain for level 1 PDUs.",
            "default": "",
            "max_length": 35,
        },
        "auth-keychain-l2": {
            "type": "string",
            "help": "Authentication key-chain for level 2 PDUs.",
            "default": "",
            "max_length": 35,
        },
        "auth-send-only-l1": {
            "type": "option",
            "help": "Enable/disable authentication send-only for level 1 PDUs.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "auth-send-only-l2": {
            "type": "option",
            "help": "Enable/disable authentication send-only for level 2 PDUs.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "auth-mode-l1": {
            "type": "option",
            "help": "Level 1 authentication mode.",
            "default": "password",
            "options": ["md5", "password"],
        },
        "auth-mode-l2": {
            "type": "option",
            "help": "Level 2 authentication mode.",
            "default": "password",
            "options": ["md5", "password"],
        },
        "priority-l1": {
            "type": "integer",
            "help": "Level 1 priority.",
            "default": 64,
            "min_value": 0,
            "max_value": 127,
        },
        "priority-l2": {
            "type": "integer",
            "help": "Level 2 priority.",
            "default": 64,
            "min_value": 0,
            "max_value": 127,
        },
        "mesh-group": {
            "type": "option",
            "help": "Enable/disable IS-IS mesh group.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "mesh-group-id": {
            "type": "integer",
            "help": "Mesh group ID <0-4294967295>, 0: mesh-group blocked.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "summary-address": {
        "id": {
            "type": "integer",
            "help": "Summary address entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix": {
            "type": "ipv4-classnet-any",
            "help": "Prefix.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "level": {
            "type": "option",
            "help": "Level.",
            "default": "level-2",
            "options": ["level-1-2", "level-1", "level-2"],
        },
    },
    "summary-address6": {
        "id": {
            "type": "integer",
            "help": "Prefix entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix6": {
            "type": "ipv6-prefix",
            "help": "IPv6 prefix.",
            "required": True,
            "default": "::/0",
        },
        "level": {
            "type": "option",
            "help": "Level.",
            "default": "level-2",
            "options": ["level-1-2", "level-1", "level-2"],
        },
    },
    "redistribute": {
        "protocol": {
            "type": "string",
            "help": "Protocol name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Status.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "metric": {
            "type": "integer",
            "help": "Metric.",
            "default": 0,
            "min_value": 0,
            "max_value": 4261412864,
        },
        "metric-type": {
            "type": "option",
            "help": "Metric type.",
            "default": "internal",
            "options": ["external", "internal"],
        },
        "level": {
            "type": "option",
            "help": "Level.",
            "default": "level-2",
            "options": ["level-1-2", "level-1", "level-2"],
        },
        "routemap": {
            "type": "string",
            "help": "Route map name.",
            "default": "",
            "max_length": 35,
        },
    },
    "redistribute6": {
        "protocol": {
            "type": "string",
            "help": "Protocol name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable redistribution.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "metric": {
            "type": "integer",
            "help": "Metric.",
            "default": 0,
            "min_value": 0,
            "max_value": 4261412864,
        },
        "metric-type": {
            "type": "option",
            "help": "Metric type.",
            "default": "internal",
            "options": ["external", "internal"],
        },
        "level": {
            "type": "option",
            "help": "Level.",
            "default": "level-2",
            "options": ["level-1-2", "level-1", "level-2"],
        },
        "routemap": {
            "type": "string",
            "help": "Route map name.",
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_IS_TYPE = [
    "level-1-2",
    "level-1",
    "level-2-only",
]
VALID_BODY_ADV_PASSIVE_ONLY = [
    "enable",
    "disable",
]
VALID_BODY_ADV_PASSIVE_ONLY6 = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_MODE_L1 = [
    "password",
    "md5",
]
VALID_BODY_AUTH_MODE_L2 = [
    "password",
    "md5",
]
VALID_BODY_AUTH_SENDONLY_L1 = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_SENDONLY_L2 = [
    "enable",
    "disable",
]
VALID_BODY_IGNORE_LSP_ERRORS = [
    "enable",
    "disable",
]
VALID_BODY_DYNAMIC_HOSTNAME = [
    "enable",
    "disable",
]
VALID_BODY_ADJACENCY_CHECK = [
    "enable",
    "disable",
]
VALID_BODY_ADJACENCY_CHECK6 = [
    "enable",
    "disable",
]
VALID_BODY_OVERLOAD_BIT = [
    "enable",
    "disable",
]
VALID_BODY_OVERLOAD_BIT_SUPPRESS = [
    "external",
    "interlevel",
]
VALID_BODY_DEFAULT_ORIGINATE = [
    "enable",
    "disable",
]
VALID_BODY_DEFAULT_ORIGINATE6 = [
    "enable",
    "disable",
]
VALID_BODY_METRIC_STYLE = [
    "narrow",
    "wide",
    "transition",
    "narrow-transition",
    "narrow-transition-l1",
    "narrow-transition-l2",
    "wide-l1",
    "wide-l2",
    "wide-transition",
    "wide-transition-l1",
    "wide-transition-l2",
    "transition-l1",
    "transition-l2",
]
VALID_BODY_REDISTRIBUTE_L1 = [
    "enable",
    "disable",
]
VALID_BODY_REDISTRIBUTE_L2 = [
    "enable",
    "disable",
]
VALID_BODY_REDISTRIBUTE6_L1 = [
    "enable",
    "disable",
]
VALID_BODY_REDISTRIBUTE6_L2 = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_router_isis_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for router/isis.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_router_isis_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_router_isis_get(
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
    Validate required fields for router/isis.

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


def validate_router_isis_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new router/isis object.

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
        >>> is_valid, error = validate_router_isis_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "is-type": "level-1-2",  # Valid enum value
        ... }
        >>> is_valid, error = validate_router_isis_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["is-type"] = "invalid-value"
        >>> is_valid, error = validate_router_isis_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_router_isis_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "is-type" in payload:
        value = payload["is-type"]
        if value not in VALID_BODY_IS_TYPE:
            desc = FIELD_DESCRIPTIONS.get("is-type", "")
            error_msg = f"Invalid value for 'is-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IS_TYPE)}"
            error_msg += f"\n  → Example: is-type='{{ VALID_BODY_IS_TYPE[0] }}'"
            return (False, error_msg)
    if "adv-passive-only" in payload:
        value = payload["adv-passive-only"]
        if value not in VALID_BODY_ADV_PASSIVE_ONLY:
            desc = FIELD_DESCRIPTIONS.get("adv-passive-only", "")
            error_msg = f"Invalid value for 'adv-passive-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADV_PASSIVE_ONLY)}"
            error_msg += f"\n  → Example: adv-passive-only='{{ VALID_BODY_ADV_PASSIVE_ONLY[0] }}'"
            return (False, error_msg)
    if "adv-passive-only6" in payload:
        value = payload["adv-passive-only6"]
        if value not in VALID_BODY_ADV_PASSIVE_ONLY6:
            desc = FIELD_DESCRIPTIONS.get("adv-passive-only6", "")
            error_msg = f"Invalid value for 'adv-passive-only6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADV_PASSIVE_ONLY6)}"
            error_msg += f"\n  → Example: adv-passive-only6='{{ VALID_BODY_ADV_PASSIVE_ONLY6[0] }}'"
            return (False, error_msg)
    if "auth-mode-l1" in payload:
        value = payload["auth-mode-l1"]
        if value not in VALID_BODY_AUTH_MODE_L1:
            desc = FIELD_DESCRIPTIONS.get("auth-mode-l1", "")
            error_msg = f"Invalid value for 'auth-mode-l1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_MODE_L1)}"
            error_msg += f"\n  → Example: auth-mode-l1='{{ VALID_BODY_AUTH_MODE_L1[0] }}'"
            return (False, error_msg)
    if "auth-mode-l2" in payload:
        value = payload["auth-mode-l2"]
        if value not in VALID_BODY_AUTH_MODE_L2:
            desc = FIELD_DESCRIPTIONS.get("auth-mode-l2", "")
            error_msg = f"Invalid value for 'auth-mode-l2': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_MODE_L2)}"
            error_msg += f"\n  → Example: auth-mode-l2='{{ VALID_BODY_AUTH_MODE_L2[0] }}'"
            return (False, error_msg)
    if "auth-sendonly-l1" in payload:
        value = payload["auth-sendonly-l1"]
        if value not in VALID_BODY_AUTH_SENDONLY_L1:
            desc = FIELD_DESCRIPTIONS.get("auth-sendonly-l1", "")
            error_msg = f"Invalid value for 'auth-sendonly-l1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SENDONLY_L1)}"
            error_msg += f"\n  → Example: auth-sendonly-l1='{{ VALID_BODY_AUTH_SENDONLY_L1[0] }}'"
            return (False, error_msg)
    if "auth-sendonly-l2" in payload:
        value = payload["auth-sendonly-l2"]
        if value not in VALID_BODY_AUTH_SENDONLY_L2:
            desc = FIELD_DESCRIPTIONS.get("auth-sendonly-l2", "")
            error_msg = f"Invalid value for 'auth-sendonly-l2': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SENDONLY_L2)}"
            error_msg += f"\n  → Example: auth-sendonly-l2='{{ VALID_BODY_AUTH_SENDONLY_L2[0] }}'"
            return (False, error_msg)
    if "ignore-lsp-errors" in payload:
        value = payload["ignore-lsp-errors"]
        if value not in VALID_BODY_IGNORE_LSP_ERRORS:
            desc = FIELD_DESCRIPTIONS.get("ignore-lsp-errors", "")
            error_msg = f"Invalid value for 'ignore-lsp-errors': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IGNORE_LSP_ERRORS)}"
            error_msg += f"\n  → Example: ignore-lsp-errors='{{ VALID_BODY_IGNORE_LSP_ERRORS[0] }}'"
            return (False, error_msg)
    if "dynamic-hostname" in payload:
        value = payload["dynamic-hostname"]
        if value not in VALID_BODY_DYNAMIC_HOSTNAME:
            desc = FIELD_DESCRIPTIONS.get("dynamic-hostname", "")
            error_msg = f"Invalid value for 'dynamic-hostname': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DYNAMIC_HOSTNAME)}"
            error_msg += f"\n  → Example: dynamic-hostname='{{ VALID_BODY_DYNAMIC_HOSTNAME[0] }}'"
            return (False, error_msg)
    if "adjacency-check" in payload:
        value = payload["adjacency-check"]
        if value not in VALID_BODY_ADJACENCY_CHECK:
            desc = FIELD_DESCRIPTIONS.get("adjacency-check", "")
            error_msg = f"Invalid value for 'adjacency-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADJACENCY_CHECK)}"
            error_msg += f"\n  → Example: adjacency-check='{{ VALID_BODY_ADJACENCY_CHECK[0] }}'"
            return (False, error_msg)
    if "adjacency-check6" in payload:
        value = payload["adjacency-check6"]
        if value not in VALID_BODY_ADJACENCY_CHECK6:
            desc = FIELD_DESCRIPTIONS.get("adjacency-check6", "")
            error_msg = f"Invalid value for 'adjacency-check6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADJACENCY_CHECK6)}"
            error_msg += f"\n  → Example: adjacency-check6='{{ VALID_BODY_ADJACENCY_CHECK6[0] }}'"
            return (False, error_msg)
    if "overload-bit" in payload:
        value = payload["overload-bit"]
        if value not in VALID_BODY_OVERLOAD_BIT:
            desc = FIELD_DESCRIPTIONS.get("overload-bit", "")
            error_msg = f"Invalid value for 'overload-bit': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERLOAD_BIT)}"
            error_msg += f"\n  → Example: overload-bit='{{ VALID_BODY_OVERLOAD_BIT[0] }}'"
            return (False, error_msg)
    if "overload-bit-suppress" in payload:
        value = payload["overload-bit-suppress"]
        if value not in VALID_BODY_OVERLOAD_BIT_SUPPRESS:
            desc = FIELD_DESCRIPTIONS.get("overload-bit-suppress", "")
            error_msg = f"Invalid value for 'overload-bit-suppress': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERLOAD_BIT_SUPPRESS)}"
            error_msg += f"\n  → Example: overload-bit-suppress='{{ VALID_BODY_OVERLOAD_BIT_SUPPRESS[0] }}'"
            return (False, error_msg)
    if "default-originate" in payload:
        value = payload["default-originate"]
        if value not in VALID_BODY_DEFAULT_ORIGINATE:
            desc = FIELD_DESCRIPTIONS.get("default-originate", "")
            error_msg = f"Invalid value for 'default-originate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_ORIGINATE)}"
            error_msg += f"\n  → Example: default-originate='{{ VALID_BODY_DEFAULT_ORIGINATE[0] }}'"
            return (False, error_msg)
    if "default-originate6" in payload:
        value = payload["default-originate6"]
        if value not in VALID_BODY_DEFAULT_ORIGINATE6:
            desc = FIELD_DESCRIPTIONS.get("default-originate6", "")
            error_msg = f"Invalid value for 'default-originate6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_ORIGINATE6)}"
            error_msg += f"\n  → Example: default-originate6='{{ VALID_BODY_DEFAULT_ORIGINATE6[0] }}'"
            return (False, error_msg)
    if "metric-style" in payload:
        value = payload["metric-style"]
        if value not in VALID_BODY_METRIC_STYLE:
            desc = FIELD_DESCRIPTIONS.get("metric-style", "")
            error_msg = f"Invalid value for 'metric-style': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_METRIC_STYLE)}"
            error_msg += f"\n  → Example: metric-style='{{ VALID_BODY_METRIC_STYLE[0] }}'"
            return (False, error_msg)
    if "redistribute-l1" in payload:
        value = payload["redistribute-l1"]
        if value not in VALID_BODY_REDISTRIBUTE_L1:
            desc = FIELD_DESCRIPTIONS.get("redistribute-l1", "")
            error_msg = f"Invalid value for 'redistribute-l1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REDISTRIBUTE_L1)}"
            error_msg += f"\n  → Example: redistribute-l1='{{ VALID_BODY_REDISTRIBUTE_L1[0] }}'"
            return (False, error_msg)
    if "redistribute-l2" in payload:
        value = payload["redistribute-l2"]
        if value not in VALID_BODY_REDISTRIBUTE_L2:
            desc = FIELD_DESCRIPTIONS.get("redistribute-l2", "")
            error_msg = f"Invalid value for 'redistribute-l2': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REDISTRIBUTE_L2)}"
            error_msg += f"\n  → Example: redistribute-l2='{{ VALID_BODY_REDISTRIBUTE_L2[0] }}'"
            return (False, error_msg)
    if "redistribute6-l1" in payload:
        value = payload["redistribute6-l1"]
        if value not in VALID_BODY_REDISTRIBUTE6_L1:
            desc = FIELD_DESCRIPTIONS.get("redistribute6-l1", "")
            error_msg = f"Invalid value for 'redistribute6-l1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REDISTRIBUTE6_L1)}"
            error_msg += f"\n  → Example: redistribute6-l1='{{ VALID_BODY_REDISTRIBUTE6_L1[0] }}'"
            return (False, error_msg)
    if "redistribute6-l2" in payload:
        value = payload["redistribute6-l2"]
        if value not in VALID_BODY_REDISTRIBUTE6_L2:
            desc = FIELD_DESCRIPTIONS.get("redistribute6-l2", "")
            error_msg = f"Invalid value for 'redistribute6-l2': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REDISTRIBUTE6_L2)}"
            error_msg += f"\n  → Example: redistribute6-l2='{{ VALID_BODY_REDISTRIBUTE6_L2[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_router_isis_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update router/isis.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_router_isis_put(payload)
    """
    # Step 1: Validate enum values
    if "is-type" in payload:
        value = payload["is-type"]
        if value not in VALID_BODY_IS_TYPE:
            return (
                False,
                f"Invalid value for 'is-type'='{value}'. Must be one of: {', '.join(VALID_BODY_IS_TYPE)}",
            )
    if "adv-passive-only" in payload:
        value = payload["adv-passive-only"]
        if value not in VALID_BODY_ADV_PASSIVE_ONLY:
            return (
                False,
                f"Invalid value for 'adv-passive-only'='{value}'. Must be one of: {', '.join(VALID_BODY_ADV_PASSIVE_ONLY)}",
            )
    if "adv-passive-only6" in payload:
        value = payload["adv-passive-only6"]
        if value not in VALID_BODY_ADV_PASSIVE_ONLY6:
            return (
                False,
                f"Invalid value for 'adv-passive-only6'='{value}'. Must be one of: {', '.join(VALID_BODY_ADV_PASSIVE_ONLY6)}",
            )
    if "auth-mode-l1" in payload:
        value = payload["auth-mode-l1"]
        if value not in VALID_BODY_AUTH_MODE_L1:
            return (
                False,
                f"Invalid value for 'auth-mode-l1'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_MODE_L1)}",
            )
    if "auth-mode-l2" in payload:
        value = payload["auth-mode-l2"]
        if value not in VALID_BODY_AUTH_MODE_L2:
            return (
                False,
                f"Invalid value for 'auth-mode-l2'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_MODE_L2)}",
            )
    if "auth-sendonly-l1" in payload:
        value = payload["auth-sendonly-l1"]
        if value not in VALID_BODY_AUTH_SENDONLY_L1:
            return (
                False,
                f"Invalid value for 'auth-sendonly-l1'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SENDONLY_L1)}",
            )
    if "auth-sendonly-l2" in payload:
        value = payload["auth-sendonly-l2"]
        if value not in VALID_BODY_AUTH_SENDONLY_L2:
            return (
                False,
                f"Invalid value for 'auth-sendonly-l2'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SENDONLY_L2)}",
            )
    if "ignore-lsp-errors" in payload:
        value = payload["ignore-lsp-errors"]
        if value not in VALID_BODY_IGNORE_LSP_ERRORS:
            return (
                False,
                f"Invalid value for 'ignore-lsp-errors'='{value}'. Must be one of: {', '.join(VALID_BODY_IGNORE_LSP_ERRORS)}",
            )
    if "dynamic-hostname" in payload:
        value = payload["dynamic-hostname"]
        if value not in VALID_BODY_DYNAMIC_HOSTNAME:
            return (
                False,
                f"Invalid value for 'dynamic-hostname'='{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_HOSTNAME)}",
            )
    if "adjacency-check" in payload:
        value = payload["adjacency-check"]
        if value not in VALID_BODY_ADJACENCY_CHECK:
            return (
                False,
                f"Invalid value for 'adjacency-check'='{value}'. Must be one of: {', '.join(VALID_BODY_ADJACENCY_CHECK)}",
            )
    if "adjacency-check6" in payload:
        value = payload["adjacency-check6"]
        if value not in VALID_BODY_ADJACENCY_CHECK6:
            return (
                False,
                f"Invalid value for 'adjacency-check6'='{value}'. Must be one of: {', '.join(VALID_BODY_ADJACENCY_CHECK6)}",
            )
    if "overload-bit" in payload:
        value = payload["overload-bit"]
        if value not in VALID_BODY_OVERLOAD_BIT:
            return (
                False,
                f"Invalid value for 'overload-bit'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERLOAD_BIT)}",
            )
    if "overload-bit-suppress" in payload:
        value = payload["overload-bit-suppress"]
        if value not in VALID_BODY_OVERLOAD_BIT_SUPPRESS:
            return (
                False,
                f"Invalid value for 'overload-bit-suppress'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERLOAD_BIT_SUPPRESS)}",
            )
    if "default-originate" in payload:
        value = payload["default-originate"]
        if value not in VALID_BODY_DEFAULT_ORIGINATE:
            return (
                False,
                f"Invalid value for 'default-originate'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_ORIGINATE)}",
            )
    if "default-originate6" in payload:
        value = payload["default-originate6"]
        if value not in VALID_BODY_DEFAULT_ORIGINATE6:
            return (
                False,
                f"Invalid value for 'default-originate6'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_ORIGINATE6)}",
            )
    if "metric-style" in payload:
        value = payload["metric-style"]
        if value not in VALID_BODY_METRIC_STYLE:
            return (
                False,
                f"Invalid value for 'metric-style'='{value}'. Must be one of: {', '.join(VALID_BODY_METRIC_STYLE)}",
            )
    if "redistribute-l1" in payload:
        value = payload["redistribute-l1"]
        if value not in VALID_BODY_REDISTRIBUTE_L1:
            return (
                False,
                f"Invalid value for 'redistribute-l1'='{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE_L1)}",
            )
    if "redistribute-l2" in payload:
        value = payload["redistribute-l2"]
        if value not in VALID_BODY_REDISTRIBUTE_L2:
            return (
                False,
                f"Invalid value for 'redistribute-l2'='{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE_L2)}",
            )
    if "redistribute6-l1" in payload:
        value = payload["redistribute6-l1"]
        if value not in VALID_BODY_REDISTRIBUTE6_L1:
            return (
                False,
                f"Invalid value for 'redistribute6-l1'='{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE6_L1)}",
            )
    if "redistribute6-l2" in payload:
        value = payload["redistribute6-l2"]
        if value not in VALID_BODY_REDISTRIBUTE6_L2:
            return (
                False,
                f"Invalid value for 'redistribute6-l2'='{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE6_L2)}",
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
    "endpoint": "router/isis",
    "category": "cmdb",
    "api_path": "router/isis",
    "help": "Configure IS-IS.",
    "total_fields": 41,
    "required_fields_count": 0,
    "fields_with_defaults_count": 33,
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
