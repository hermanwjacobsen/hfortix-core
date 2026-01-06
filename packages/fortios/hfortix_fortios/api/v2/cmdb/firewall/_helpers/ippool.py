"""Validation helpers for firewall/ippool - Auto-generated"""

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
    "permit-any-host": "option",  # Enable/disable fullcone NAT. Accept UDP packets from any hos
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
    "permit-any-host": "Enable/disable fullcone NAT. Accept UDP packets from any host.",
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
    "overload",  # IP addresses in the IP pool can be shared by clients.
    "one-to-one",  # One to one mapping.
    "fixed-port-range",  # Fixed port range.
    "port-block-allocation",  # Port block allocation.
]
VALID_BODY_PERMIT_ANY_HOST = [
    "disable",  # Disable full cone NAT.
    "enable",  # Enable full cone NAT.
]
VALID_BODY_ARP_REPLY = [
    "disable",  # Disable ARP reply.
    "enable",  # Enable ARP reply.
]
VALID_BODY_NAT64 = [
    "disable",  # Disable DNAT64.
    "enable",  # Enable DNAT64.
]
VALID_BODY_ADD_NAT64_ROUTE = [
    "disable",  # Disable adding NAT64 route.
    "enable",  # Enable adding NAT64 route.
]
VALID_BODY_PRIVILEGED_PORT_USE_PBA = [
    "disable",  # Select new nat port for privileged source ports from priviliged range 512-1023.
    "enable",  # Select new nat port for privileged source ports from client's port block
]
VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL = [
    "disable",  # Do not include the subnetwork address and broadcast IP address in the NAT64 IP pool.
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
    """Validate GET request parameters for firewall/ippool."""
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
    """Validate required fields for firewall/ippool."""
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
    """Validate POST request to create new firewall/ippool object."""
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
    """Validate PUT request to update firewall/ippool."""
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
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
