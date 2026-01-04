"""
Validation helpers for system/snmp_community endpoint.

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
    "name",  # Community name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "name": "",
    "status": "enable",
    "query-v1-status": "enable",
    "query-v1-port": 161,
    "query-v2c-status": "enable",
    "query-v2c-port": 161,
    "trap-v1-status": "enable",
    "trap-v1-lport": 162,
    "trap-v1-rport": 162,
    "trap-v2c-status": "enable",
    "trap-v2c-lport": 162,
    "trap-v2c-rport": 162,
    "events": "cpu-high mem-low log-full intf-ip vpn-tun-up vpn-tun-down ha-switch ha-hb-failure ips-signature ips-anomaly av-virus av-oversize av-pattern av-fragmented fm-if-change bgp-established bgp-backward-transition ha-member-up ha-member-down ent-conf-change av-conserve av-bypass av-oversize-passed av-oversize-blocked ips-pkg-update ips-fail-open faz-disconnect faz wc-ap-up wc-ap-down fswctl-session-up fswctl-session-down load-balance-real-server-down per-cpu-high dhcp pool-usage ippool interface ospf-nbr-state-change ospf-virtnbr-state-change",
    "mib-view": "",
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
    "id": "integer",  # Community ID.
    "name": "string",  # Community name.
    "status": "option",  # Enable/disable this SNMP community.
    "hosts": "string",  # Configure IPv4 SNMP managers (hosts).
    "hosts6": "string",  # Configure IPv6 SNMP managers.
    "query-v1-status": "option",  # Enable/disable SNMP v1 queries.
    "query-v1-port": "integer",  # SNMP v1 query port (default = 161).
    "query-v2c-status": "option",  # Enable/disable SNMP v2c queries.
    "query-v2c-port": "integer",  # SNMP v2c query port (default = 161).
    "trap-v1-status": "option",  # Enable/disable SNMP v1 traps.
    "trap-v1-lport": "integer",  # SNMP v1 trap local port (default = 162).
    "trap-v1-rport": "integer",  # SNMP v1 trap remote port (default = 162).
    "trap-v2c-status": "option",  # Enable/disable SNMP v2c traps.
    "trap-v2c-lport": "integer",  # SNMP v2c trap local port (default = 162).
    "trap-v2c-rport": "integer",  # SNMP v2c trap remote port (default = 162).
    "events": "option",  # SNMP trap events.
    "mib-view": "string",  # SNMP access control MIB view.
    "vdoms": "string",  # SNMP access control VDOMs.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "Community ID.",
    "name": "Community name.",
    "status": "Enable/disable this SNMP community.",
    "hosts": "Configure IPv4 SNMP managers (hosts).",
    "hosts6": "Configure IPv6 SNMP managers.",
    "query-v1-status": "Enable/disable SNMP v1 queries.",
    "query-v1-port": "SNMP v1 query port (default = 161).",
    "query-v2c-status": "Enable/disable SNMP v2c queries.",
    "query-v2c-port": "SNMP v2c query port (default = 161).",
    "trap-v1-status": "Enable/disable SNMP v1 traps.",
    "trap-v1-lport": "SNMP v1 trap local port (default = 162).",
    "trap-v1-rport": "SNMP v1 trap remote port (default = 162).",
    "trap-v2c-status": "Enable/disable SNMP v2c traps.",
    "trap-v2c-lport": "SNMP v2c trap local port (default = 162).",
    "trap-v2c-rport": "SNMP v2c trap remote port (default = 162).",
    "events": "SNMP trap events.",
    "mib-view": "SNMP access control MIB view.",
    "vdoms": "SNMP access control VDOMs.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "name": {"type": "string", "max_length": 35},
    "query-v1-port": {"type": "integer", "min": 1, "max": 65535},
    "query-v2c-port": {"type": "integer", "min": 0, "max": 65535},
    "trap-v1-lport": {"type": "integer", "min": 1, "max": 65535},
    "trap-v1-rport": {"type": "integer", "min": 1, "max": 65535},
    "trap-v2c-lport": {"type": "integer", "min": 1, "max": 65535},
    "trap-v2c-rport": {"type": "integer", "min": 1, "max": 65535},
    "mib-view": {"type": "string", "max_length": 32},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "hosts": {
        "id": {
            "type": "integer",
            "help": "Host entry ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "source-ip": {
            "type": "ipv4-address",
            "help": "Source IPv4 address for SNMP traps.",
            "default": "0.0.0.0",
        },
        "ip": {
            "type": "user",
            "help": "IPv4 address of the SNMP manager (host).",
            "required": True,
            "default": "",
        },
        "ha-direct": {
            "type": "option",
            "help": "Enable/disable direct management of HA cluster members.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "host-type": {
            "type": "option",
            "help": "Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or both. No traps will be sent when IP type is subnet.",
            "default": "any",
            "options": ["any", "query", "trap"],
        },
        "interface-select-method": {
            "type": "option",
            "help": "Specify how to select outgoing interface to reach server.",
            "default": "auto",
            "options": ["auto", "sdwan", "specify"],
        },
        "interface": {
            "type": "string",
            "help": "Specify outgoing interface to reach server.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "vrf-select": {
            "type": "integer",
            "help": "VRF ID used for connection to server.",
            "default": 0,
            "min_value": 0,
            "max_value": 511,
        },
    },
    "hosts6": {
        "id": {
            "type": "integer",
            "help": "Host6 entry ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "source-ipv6": {
            "type": "ipv6-address",
            "help": "Source IPv6 address for SNMP traps.",
            "default": "::",
        },
        "ipv6": {
            "type": "ipv6-prefix",
            "help": "SNMP manager IPv6 address prefix.",
            "required": True,
            "default": "::/0",
        },
        "ha-direct": {
            "type": "option",
            "help": "Enable/disable direct management of HA cluster members.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "host-type": {
            "type": "option",
            "help": "Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or both.",
            "default": "any",
            "options": ["any", "query", "trap"],
        },
        "interface-select-method": {
            "type": "option",
            "help": "Specify how to select outgoing interface to reach server.",
            "default": "auto",
            "options": ["auto", "sdwan", "specify"],
        },
        "interface": {
            "type": "string",
            "help": "Specify outgoing interface to reach server.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "vrf-select": {
            "type": "integer",
            "help": "VRF ID used for connection to server.",
            "default": 0,
            "min_value": 0,
            "max_value": 511,
        },
    },
    "vdoms": {
        "name": {
            "type": "string",
            "help": "VDOM name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_QUERY_V1_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_QUERY_V2C_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_TRAP_V1_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_TRAP_V2C_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_EVENTS = [
    "cpu-high",
    "mem-low",
    "log-full",
    "intf-ip",
    "vpn-tun-up",
    "vpn-tun-down",
    "ha-switch",
    "ha-hb-failure",
    "ips-signature",
    "ips-anomaly",
    "av-virus",
    "av-oversize",
    "av-pattern",
    "av-fragmented",
    "fm-if-change",
    "fm-conf-change",
    "bgp-established",
    "bgp-backward-transition",
    "ha-member-up",
    "ha-member-down",
    "ent-conf-change",
    "av-conserve",
    "av-bypass",
    "av-oversize-passed",
    "av-oversize-blocked",
    "ips-pkg-update",
    "ips-fail-open",
    "faz-disconnect",
    "faz",
    "wc-ap-up",
    "wc-ap-down",
    "fswctl-session-up",
    "fswctl-session-down",
    "load-balance-real-server-down",
    "device-new",
    "per-cpu-high",
    "dhcp",
    "pool-usage",
    "ippool",
    "interface",
    "ospf-nbr-state-change",
    "ospf-virtnbr-state-change",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_snmp_community_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/snmp_community.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_snmp_community_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by id
        >>> is_valid, error = validate_system_snmp_community_get(id="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_snmp_community_get(
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
    Validate required fields for system/snmp_community.

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


def validate_system_snmp_community_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/snmp_community object.

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
        ...     "name": True,  # Community name.
        ... }
        >>> is_valid, error = validate_system_snmp_community_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "name": True,
        ...     "status": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_snmp_community_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_system_snmp_community_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_snmp_community_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            desc = FIELD_DESCRIPTIONS.get("status", "")
            error_msg = f"Invalid value for 'status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STATUS)}"
            error_msg += f"\n  → Example: status='{{ VALID_BODY_STATUS[0] }}'"
            return (False, error_msg)
    if "query-v1-status" in payload:
        value = payload["query-v1-status"]
        if value not in VALID_BODY_QUERY_V1_STATUS:
            desc = FIELD_DESCRIPTIONS.get("query-v1-status", "")
            error_msg = f"Invalid value for 'query-v1-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QUERY_V1_STATUS)}"
            error_msg += f"\n  → Example: query-v1-status='{{ VALID_BODY_QUERY_V1_STATUS[0] }}'"
            return (False, error_msg)
    if "query-v2c-status" in payload:
        value = payload["query-v2c-status"]
        if value not in VALID_BODY_QUERY_V2C_STATUS:
            desc = FIELD_DESCRIPTIONS.get("query-v2c-status", "")
            error_msg = f"Invalid value for 'query-v2c-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QUERY_V2C_STATUS)}"
            error_msg += f"\n  → Example: query-v2c-status='{{ VALID_BODY_QUERY_V2C_STATUS[0] }}'"
            return (False, error_msg)
    if "trap-v1-status" in payload:
        value = payload["trap-v1-status"]
        if value not in VALID_BODY_TRAP_V1_STATUS:
            desc = FIELD_DESCRIPTIONS.get("trap-v1-status", "")
            error_msg = f"Invalid value for 'trap-v1-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRAP_V1_STATUS)}"
            error_msg += f"\n  → Example: trap-v1-status='{{ VALID_BODY_TRAP_V1_STATUS[0] }}'"
            return (False, error_msg)
    if "trap-v2c-status" in payload:
        value = payload["trap-v2c-status"]
        if value not in VALID_BODY_TRAP_V2C_STATUS:
            desc = FIELD_DESCRIPTIONS.get("trap-v2c-status", "")
            error_msg = f"Invalid value for 'trap-v2c-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRAP_V2C_STATUS)}"
            error_msg += f"\n  → Example: trap-v2c-status='{{ VALID_BODY_TRAP_V2C_STATUS[0] }}'"
            return (False, error_msg)
    if "events" in payload:
        value = payload["events"]
        if value not in VALID_BODY_EVENTS:
            desc = FIELD_DESCRIPTIONS.get("events", "")
            error_msg = f"Invalid value for 'events': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EVENTS)}"
            error_msg += f"\n  → Example: events='{{ VALID_BODY_EVENTS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_snmp_community_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/snmp_community.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_snmp_community_put(payload)
    """
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "query-v1-status" in payload:
        value = payload["query-v1-status"]
        if value not in VALID_BODY_QUERY_V1_STATUS:
            return (
                False,
                f"Invalid value for 'query-v1-status'='{value}'. Must be one of: {', '.join(VALID_BODY_QUERY_V1_STATUS)}",
            )
    if "query-v2c-status" in payload:
        value = payload["query-v2c-status"]
        if value not in VALID_BODY_QUERY_V2C_STATUS:
            return (
                False,
                f"Invalid value for 'query-v2c-status'='{value}'. Must be one of: {', '.join(VALID_BODY_QUERY_V2C_STATUS)}",
            )
    if "trap-v1-status" in payload:
        value = payload["trap-v1-status"]
        if value not in VALID_BODY_TRAP_V1_STATUS:
            return (
                False,
                f"Invalid value for 'trap-v1-status'='{value}'. Must be one of: {', '.join(VALID_BODY_TRAP_V1_STATUS)}",
            )
    if "trap-v2c-status" in payload:
        value = payload["trap-v2c-status"]
        if value not in VALID_BODY_TRAP_V2C_STATUS:
            return (
                False,
                f"Invalid value for 'trap-v2c-status'='{value}'. Must be one of: {', '.join(VALID_BODY_TRAP_V2C_STATUS)}",
            )
    if "events" in payload:
        value = payload["events"]
        if value not in VALID_BODY_EVENTS:
            return (
                False,
                f"Invalid value for 'events'='{value}'. Must be one of: {', '.join(VALID_BODY_EVENTS)}",
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
    "endpoint": "system/snmp_community",
    "category": "cmdb",
    "api_path": "system.snmp/community",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "SNMP community configuration.",
    "total_fields": 18,
    "required_fields_count": 1,
    "fields_with_defaults_count": 15,
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
