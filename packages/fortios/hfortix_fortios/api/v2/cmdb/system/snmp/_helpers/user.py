"""Validation helpers for system/snmp/user - Auto-generated"""

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
    "name",  # SNMP user name.
    "auth-pwd",  # Password for authentication protocol.
    "priv-pwd",  # Password for privacy (encryption) protocol.
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "status": "enable",
    "trap-status": "enable",
    "trap-lport": 162,
    "trap-rport": 162,
    "queries": "enable",
    "query-port": 161,
    "notify-hosts": "",
    "notify-hosts6": "",
    "source-ip": "0.0.0.0",
    "source-ipv6": "::",
    "ha-direct": "disable",
    "events": "cpu-high mem-low log-full intf-ip vpn-tun-up vpn-tun-down ha-switch ha-hb-failure ips-signature ips-anomaly av-virus av-oversize av-pattern av-fragmented fm-if-change bgp-established bgp-backward-transition ha-member-up ha-member-down ent-conf-change av-conserve av-bypass av-oversize-passed av-oversize-blocked ips-pkg-update ips-fail-open faz-disconnect faz wc-ap-up wc-ap-down fswctl-session-up fswctl-session-down load-balance-real-server-down per-cpu-high dhcp pool-usage ippool interface ospf-nbr-state-change ospf-virtnbr-state-change bfd",
    "mib-view": "",
    "security-level": "no-auth-no-priv",
    "auth-proto": "sha",
    "priv-proto": "aes",
    "interface-select-method": "auto",
    "interface": "",
    "vrf-select": 0,
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
    "name": "string",  # SNMP user name.
    "status": "option",  # Enable/disable this SNMP user.
    "trap-status": "option",  # Enable/disable traps for this SNMP user.
    "trap-lport": "integer",  # SNMPv3 local trap port (default = 162).
    "trap-rport": "integer",  # SNMPv3 trap remote port (default = 162).
    "queries": "option",  # Enable/disable SNMP queries for this user.
    "query-port": "integer",  # SNMPv3 query port (default = 161).
    "notify-hosts": "ipv4-address",  # SNMP managers to send notifications (traps) to.
    "notify-hosts6": "ipv6-address",  # IPv6 SNMP managers to send notifications (traps) to.
    "source-ip": "ipv4-address",  # Source IP for SNMP trap.
    "source-ipv6": "ipv6-address",  # Source IPv6 for SNMP trap.
    "ha-direct": "option",  # Enable/disable direct management of HA cluster members.
    "events": "option",  # SNMP notifications (traps) to send.
    "mib-view": "string",  # SNMP access control MIB view.
    "vdoms": "string",  # SNMP access control VDOMs.
    "security-level": "option",  # Security level for message authentication and encryption.
    "auth-proto": "option",  # Authentication protocol.
    "auth-pwd": "password",  # Password for authentication protocol.
    "priv-proto": "option",  # Privacy (encryption) protocol.
    "priv-pwd": "password",  # Password for privacy (encryption) protocol.
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "SNMP user name.",
    "status": "Enable/disable this SNMP user.",
    "trap-status": "Enable/disable traps for this SNMP user.",
    "trap-lport": "SNMPv3 local trap port (default = 162).",
    "trap-rport": "SNMPv3 trap remote port (default = 162).",
    "queries": "Enable/disable SNMP queries for this user.",
    "query-port": "SNMPv3 query port (default = 161).",
    "notify-hosts": "SNMP managers to send notifications (traps) to.",
    "notify-hosts6": "IPv6 SNMP managers to send notifications (traps) to.",
    "source-ip": "Source IP for SNMP trap.",
    "source-ipv6": "Source IPv6 for SNMP trap.",
    "ha-direct": "Enable/disable direct management of HA cluster members.",
    "events": "SNMP notifications (traps) to send.",
    "mib-view": "SNMP access control MIB view.",
    "vdoms": "SNMP access control VDOMs.",
    "security-level": "Security level for message authentication and encryption.",
    "auth-proto": "Authentication protocol.",
    "auth-pwd": "Password for authentication protocol.",
    "priv-proto": "Privacy (encryption) protocol.",
    "priv-pwd": "Password for privacy (encryption) protocol.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 32},
    "trap-lport": {"type": "integer", "min": 1, "max": 65535},
    "trap-rport": {"type": "integer", "min": 1, "max": 65535},
    "query-port": {"type": "integer", "min": 1, "max": 65535},
    "mib-view": {"type": "string", "max_length": 32},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
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
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_TRAP_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_QUERIES = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_HA_DIRECT = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_EVENTS = [
    "cpu-high",  # Send a trap when CPU usage is high.
    "mem-low",  # Send a trap when used memory is high, free memory is low, or freeable memory is high.
    "log-full",  # Send a trap when log disk space becomes low.
    "intf-ip",  # Send a trap when an interface IP address is changed.
    "vpn-tun-up",  # Send a trap when a VPN tunnel comes up.
    "vpn-tun-down",  # Send a trap when a VPN tunnel goes down.
    "ha-switch",  # Send a trap after an HA failover when the backup unit has taken over.
    "ha-hb-failure",  # Send a trap when HA heartbeats are not received.
    "ips-signature",  # Send a trap when IPS detects an attack.
    "ips-anomaly",  # Send a trap when IPS finds an anomaly.
    "av-virus",  # Send a trap when AntiVirus finds a virus.
    "av-oversize",  # Send a trap when AntiVirus finds an oversized file.
    "av-pattern",  # Send a trap when AntiVirus finds file matching pattern.
    "av-fragmented",  # Send a trap when AntiVirus finds a fragmented file.
    "fm-if-change",  # Send a trap when FortiManager interface changes. Send a FortiManager trap.
    "fm-conf-change",  # Send a trap when a configuration change is made by a FortiGate administrator and the FortiGate is managed by FortiManager.
    "bgp-established",  # Send a trap when a BGP FSM transitions to the established state.
    "bgp-backward-transition",  # Send a trap when a BGP FSM goes from a high numbered state to a lower numbered state.
    "ha-member-up",  # Send a trap when an HA cluster member goes up.
    "ha-member-down",  # Send a trap when an HA cluster member goes down.
    "ent-conf-change",  # Send a trap when an entity MIB change occurs (RFC4133).
    "av-conserve",  # Send a trap when the FortiGate enters conserve mode.
    "av-bypass",  # Send a trap when the FortiGate enters bypass mode.
    "av-oversize-passed",  # Send a trap when AntiVirus passes an oversized file.
    "av-oversize-blocked",  # Send a trap when AntiVirus blocks an oversized file.
    "ips-pkg-update",  # Send a trap when the IPS signature database or engine is updated.
    "ips-fail-open",  # Send a trap when the IPS network buffer is full.
    "faz-disconnect",  # Send a trap when a FortiAnalyzer disconnects from the FortiGate.
    "faz",  # Send a trap when Fortianalyzer main server failover and alternate server take over, or alternate server failover and main server take over.
    "wc-ap-up",  # Send a trap when a managed FortiAP comes up.
    "wc-ap-down",  # Send a trap when a managed FortiAP goes down.
    "fswctl-session-up",  # Send a trap when a FortiSwitch controller session comes up.
    "fswctl-session-down",  # Send a trap when a FortiSwitch controller session goes down.
    "load-balance-real-server-down",  # Send a trap when a server load balance real server goes down.
    "device-new",  # Send a trap when a new device is found.
    "per-cpu-high",  # Send a trap when per-CPU usage is high.
    "dhcp",  # Send a trap when the DHCP server exhausts the IP pool, an IP address already is in use, or a DHCP client interface received a DHCP-NAK.
    "pool-usage",  # Send a trap about ippool usage.
    "ippool",  # Send a trap for ippool events.
    "interface",  # Send a trap for interface event.
    "ospf-nbr-state-change",  # Send a trap when there has been a change in the state of a non-virtual OSPF neighbor.
    "ospf-virtnbr-state-change",  # Send a trap when there has been a change in the state of an OSPF virtual neighbor.
    "bfd",  # Send a trap for bfd event.
]
VALID_BODY_SECURITY_LEVEL = [
    "no-auth-no-priv",  # Message with no authentication and no privacy (encryption).
    "auth-no-priv",  # Message with authentication but no privacy (encryption).
    "auth-priv",  # Message with authentication and privacy (encryption).
]
VALID_BODY_AUTH_PROTO = [
    "md5",  # HMAC-MD5-96 authentication protocol.
    "sha",  # HMAC-SHA-96 authentication protocol.
    "sha224",  # HMAC-SHA224 authentication protocol.
    "sha256",  # HMAC-SHA256 authentication protocol.
    "sha384",  # HMAC-SHA384 authentication protocol.
    "sha512",  # HMAC-SHA512 authentication protocol.
]
VALID_BODY_PRIV_PROTO = [
    "aes",  # CFB128-AES-128 symmetric encryption protocol.
    "des",  # CBC-DES symmetric encryption protocol.
    "aes256",  # CFB128-AES-256 symmetric encryption protocol.
    "aes256cisco",  # CFB128-AES-256 symmetric encryption protocol compatible with CISCO.
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",  # Set outgoing interface automatically.
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_snmp_user_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/snmp/user."""
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
    """Validate required fields for system/snmp/user."""
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


def validate_system_snmp_user_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/snmp/user object."""
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
    if "trap-status" in payload:
        value = payload["trap-status"]
        if value not in VALID_BODY_TRAP_STATUS:
            desc = FIELD_DESCRIPTIONS.get("trap-status", "")
            error_msg = f"Invalid value for 'trap-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRAP_STATUS)}"
            error_msg += f"\n  → Example: trap-status='{{ VALID_BODY_TRAP_STATUS[0] }}'"
            return (False, error_msg)
    if "queries" in payload:
        value = payload["queries"]
        if value not in VALID_BODY_QUERIES:
            desc = FIELD_DESCRIPTIONS.get("queries", "")
            error_msg = f"Invalid value for 'queries': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QUERIES)}"
            error_msg += f"\n  → Example: queries='{{ VALID_BODY_QUERIES[0] }}'"
            return (False, error_msg)
    if "ha-direct" in payload:
        value = payload["ha-direct"]
        if value not in VALID_BODY_HA_DIRECT:
            desc = FIELD_DESCRIPTIONS.get("ha-direct", "")
            error_msg = f"Invalid value for 'ha-direct': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HA_DIRECT)}"
            error_msg += f"\n  → Example: ha-direct='{{ VALID_BODY_HA_DIRECT[0] }}'"
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
    if "security-level" in payload:
        value = payload["security-level"]
        if value not in VALID_BODY_SECURITY_LEVEL:
            desc = FIELD_DESCRIPTIONS.get("security-level", "")
            error_msg = f"Invalid value for 'security-level': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURITY_LEVEL)}"
            error_msg += f"\n  → Example: security-level='{{ VALID_BODY_SECURITY_LEVEL[0] }}'"
            return (False, error_msg)
    if "auth-proto" in payload:
        value = payload["auth-proto"]
        if value not in VALID_BODY_AUTH_PROTO:
            desc = FIELD_DESCRIPTIONS.get("auth-proto", "")
            error_msg = f"Invalid value for 'auth-proto': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_PROTO)}"
            error_msg += f"\n  → Example: auth-proto='{{ VALID_BODY_AUTH_PROTO[0] }}'"
            return (False, error_msg)
    if "priv-proto" in payload:
        value = payload["priv-proto"]
        if value not in VALID_BODY_PRIV_PROTO:
            desc = FIELD_DESCRIPTIONS.get("priv-proto", "")
            error_msg = f"Invalid value for 'priv-proto': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIV_PROTO)}"
            error_msg += f"\n  → Example: priv-proto='{{ VALID_BODY_PRIV_PROTO[0] }}'"
            return (False, error_msg)
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("interface-select-method", "")
            error_msg = f"Invalid value for 'interface-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERFACE_SELECT_METHOD)}"
            error_msg += f"\n  → Example: interface-select-method='{{ VALID_BODY_INTERFACE_SELECT_METHOD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_snmp_user_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/snmp/user."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "trap-status" in payload:
        value = payload["trap-status"]
        if value not in VALID_BODY_TRAP_STATUS:
            return (
                False,
                f"Invalid value for 'trap-status'='{value}'. Must be one of: {', '.join(VALID_BODY_TRAP_STATUS)}",
            )
    if "queries" in payload:
        value = payload["queries"]
        if value not in VALID_BODY_QUERIES:
            return (
                False,
                f"Invalid value for 'queries'='{value}'. Must be one of: {', '.join(VALID_BODY_QUERIES)}",
            )
    if "ha-direct" in payload:
        value = payload["ha-direct"]
        if value not in VALID_BODY_HA_DIRECT:
            return (
                False,
                f"Invalid value for 'ha-direct'='{value}'. Must be one of: {', '.join(VALID_BODY_HA_DIRECT)}",
            )
    if "events" in payload:
        value = payload["events"]
        if value not in VALID_BODY_EVENTS:
            return (
                False,
                f"Invalid value for 'events'='{value}'. Must be one of: {', '.join(VALID_BODY_EVENTS)}",
            )
    if "security-level" in payload:
        value = payload["security-level"]
        if value not in VALID_BODY_SECURITY_LEVEL:
            return (
                False,
                f"Invalid value for 'security-level'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_LEVEL)}",
            )
    if "auth-proto" in payload:
        value = payload["auth-proto"]
        if value not in VALID_BODY_AUTH_PROTO:
            return (
                False,
                f"Invalid value for 'auth-proto'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PROTO)}",
            )
    if "priv-proto" in payload:
        value = payload["priv-proto"]
        if value not in VALID_BODY_PRIV_PROTO:
            return (
                False,
                f"Invalid value for 'priv-proto'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIV_PROTO)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
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
    "endpoint": "system/snmp/user",
    "category": "cmdb",
    "api_path": "system.snmp/user",
    "mkey": "name",
    "mkey_type": "string",
    "help": "SNMP user configuration.",
    "total_fields": 23,
    "required_fields_count": 4,
    "fields_with_defaults_count": 20,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
