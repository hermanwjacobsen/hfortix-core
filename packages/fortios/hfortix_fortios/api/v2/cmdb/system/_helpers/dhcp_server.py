"""
Validation helpers for system/dhcp_server endpoint.

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
    "interface",  # DHCP server can assign IP configurations to clients connected to this interface.
    "timezone",  # Select the time zone to be assigned to DHCP clients.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "status": "enable",
    "lease-time": 604800,
    "mac-acl-default-action": "assign",
    "forticlient-on-net-status": "enable",
    "dns-service": "specify",
    "dns-server1": "0.0.0.0",
    "dns-server2": "0.0.0.0",
    "dns-server3": "0.0.0.0",
    "dns-server4": "0.0.0.0",
    "wifi-ac-service": "specify",
    "wifi-ac1": "0.0.0.0",
    "wifi-ac2": "0.0.0.0",
    "wifi-ac3": "0.0.0.0",
    "ntp-service": "specify",
    "ntp-server1": "0.0.0.0",
    "ntp-server2": "0.0.0.0",
    "ntp-server3": "0.0.0.0",
    "domain": "",
    "wins-server1": "0.0.0.0",
    "wins-server2": "0.0.0.0",
    "default-gateway": "0.0.0.0",
    "next-server": "0.0.0.0",
    "netmask": "0.0.0.0",
    "interface": "",
    "timezone-option": "disable",
    "timezone": "",
    "filename": "",
    "server-type": "regular",
    "ip-mode": "range",
    "conflicted-ip-timeout": 1800,
    "ipsec-lease-hold": 60,
    "auto-configuration": "enable",
    "dhcp-settings-from-fortiipam": "disable",
    "auto-managed-status": "enable",
    "ddns-update": "disable",
    "ddns-update-override": "disable",
    "ddns-server-ip": "0.0.0.0",
    "ddns-zone": "",
    "ddns-auth": "disable",
    "ddns-keyname": "",
    "ddns-ttl": 300,
    "vci-match": "disable",
    "shared-subnet": "disable",
    "relay-agent": "0.0.0.0",
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
    "id": "integer",  # ID.
    "status": "option",  # Enable/disable this DHCP configuration.
    "lease-time": "integer",  # Lease time in seconds, 0 means unlimited.
    "mac-acl-default-action": "option",  # MAC access control default action (allow or block assigning 
    "forticlient-on-net-status": "option",  # Enable/disable FortiClient-On-Net service for this DHCP serv
    "dns-service": "option",  # Options for assigning DNS servers to DHCP clients.
    "dns-server1": "ipv4-address",  # DNS server 1.
    "dns-server2": "ipv4-address",  # DNS server 2.
    "dns-server3": "ipv4-address",  # DNS server 3.
    "dns-server4": "ipv4-address",  # DNS server 4.
    "wifi-ac-service": "option",  # Options for assigning WiFi access controllers to DHCP client
    "wifi-ac1": "ipv4-address",  # WiFi Access Controller 1 IP address (DHCP option 138, RFC 54
    "wifi-ac2": "ipv4-address",  # WiFi Access Controller 2 IP address (DHCP option 138, RFC 54
    "wifi-ac3": "ipv4-address",  # WiFi Access Controller 3 IP address (DHCP option 138, RFC 54
    "ntp-service": "option",  # Options for assigning Network Time Protocol (NTP) servers to
    "ntp-server1": "ipv4-address",  # NTP server 1.
    "ntp-server2": "ipv4-address",  # NTP server 2.
    "ntp-server3": "ipv4-address",  # NTP server 3.
    "domain": "string",  # Domain name suffix for the IP addresses that the DHCP server
    "wins-server1": "ipv4-address",  # WINS server 1.
    "wins-server2": "ipv4-address",  # WINS server 2.
    "default-gateway": "ipv4-address",  # Default gateway IP address assigned by the DHCP server.
    "next-server": "ipv4-address",  # IP address of a server (for example, a TFTP sever) that DHCP
    "netmask": "ipv4-netmask",  # Netmask assigned by the DHCP server.
    "interface": "string",  # DHCP server can assign IP configurations to clients connecte
    "ip-range": "string",  # DHCP IP range configuration.
    "timezone-option": "option",  # Options for the DHCP server to set the client's time zone.
    "timezone": "string",  # Select the time zone to be assigned to DHCP clients.
    "tftp-server": "string",  # One or more hostnames or IP addresses of the TFTP servers in
    "filename": "string",  # Name of the boot file on the TFTP server.
    "options": "string",  # DHCP options.
    "server-type": "option",  # DHCP server can be a normal DHCP server or an IPsec DHCP ser
    "ip-mode": "option",  # Method used to assign client IP.
    "conflicted-ip-timeout": "integer",  # Time in seconds to wait after a conflicted IP address is rem
    "ipsec-lease-hold": "integer",  # DHCP over IPsec leases expire this many seconds after tunnel
    "auto-configuration": "option",  # Enable/disable auto configuration.
    "dhcp-settings-from-fortiipam": "option",  # Enable/disable populating of DHCP server settings from Forti
    "auto-managed-status": "option",  # Enable/disable use of this DHCP server once this interface h
    "ddns-update": "option",  # Enable/disable DDNS update for DHCP.
    "ddns-update-override": "option",  # Enable/disable DDNS update override for DHCP.
    "ddns-server-ip": "ipv4-address",  # DDNS server IP.
    "ddns-zone": "string",  # Zone of your domain name (ex. DDNS.com).
    "ddns-auth": "option",  # DDNS authentication mode.
    "ddns-keyname": "string",  # DDNS update key name.
    "ddns-key": "password_aes256",  # DDNS update key (base 64 encoding).
    "ddns-ttl": "integer",  # TTL.
    "vci-match": "option",  # Enable/disable vendor class identifier (VCI) matching. When 
    "vci-string": "string",  # One or more VCI strings in quotes separated by spaces.
    "exclude-range": "string",  # Exclude one or more ranges of IP addresses from being assign
    "shared-subnet": "option",  # Enable/disable shared subnet.
    "relay-agent": "ipv4-address",  # Relay agent IP.
    "reserved-address": "string",  # Options for the DHCP server to assign IP settings to specifi
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "ID.",
    "status": "Enable/disable this DHCP configuration.",
    "lease-time": "Lease time in seconds, 0 means unlimited.",
    "mac-acl-default-action": "MAC access control default action (allow or block assigning IP settings).",
    "forticlient-on-net-status": "Enable/disable FortiClient-On-Net service for this DHCP server.",
    "dns-service": "Options for assigning DNS servers to DHCP clients.",
    "dns-server1": "DNS server 1.",
    "dns-server2": "DNS server 2.",
    "dns-server3": "DNS server 3.",
    "dns-server4": "DNS server 4.",
    "wifi-ac-service": "Options for assigning WiFi access controllers to DHCP clients.",
    "wifi-ac1": "WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417).",
    "wifi-ac2": "WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417).",
    "wifi-ac3": "WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417).",
    "ntp-service": "Options for assigning Network Time Protocol (NTP) servers to DHCP clients.",
    "ntp-server1": "NTP server 1.",
    "ntp-server2": "NTP server 2.",
    "ntp-server3": "NTP server 3.",
    "domain": "Domain name suffix for the IP addresses that the DHCP server assigns to clients.",
    "wins-server1": "WINS server 1.",
    "wins-server2": "WINS server 2.",
    "default-gateway": "Default gateway IP address assigned by the DHCP server.",
    "next-server": "IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from.",
    "netmask": "Netmask assigned by the DHCP server.",
    "interface": "DHCP server can assign IP configurations to clients connected to this interface.",
    "ip-range": "DHCP IP range configuration.",
    "timezone-option": "Options for the DHCP server to set the client's time zone.",
    "timezone": "Select the time zone to be assigned to DHCP clients.",
    "tftp-server": "One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces.",
    "filename": "Name of the boot file on the TFTP server.",
    "options": "DHCP options.",
    "server-type": "DHCP server can be a normal DHCP server or an IPsec DHCP server.",
    "ip-mode": "Method used to assign client IP.",
    "conflicted-ip-timeout": "Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused.",
    "ipsec-lease-hold": "DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry).",
    "auto-configuration": "Enable/disable auto configuration.",
    "dhcp-settings-from-fortiipam": "Enable/disable populating of DHCP server settings from FortiIPAM.",
    "auto-managed-status": "Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM.",
    "ddns-update": "Enable/disable DDNS update for DHCP.",
    "ddns-update-override": "Enable/disable DDNS update override for DHCP.",
    "ddns-server-ip": "DDNS server IP.",
    "ddns-zone": "Zone of your domain name (ex. DDNS.com).",
    "ddns-auth": "DDNS authentication mode.",
    "ddns-keyname": "DDNS update key name.",
    "ddns-key": "DDNS update key (base 64 encoding).",
    "ddns-ttl": "TTL.",
    "vci-match": "Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served.",
    "vci-string": "One or more VCI strings in quotes separated by spaces.",
    "exclude-range": "Exclude one or more ranges of IP addresses from being assigned to clients.",
    "shared-subnet": "Enable/disable shared subnet.",
    "relay-agent": "Relay agent IP.",
    "reserved-address": "Options for the DHCP server to assign IP settings to specific MAC addresses.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "lease-time": {"type": "integer", "min": 300, "max": 8640000},
    "domain": {"type": "string", "max_length": 35},
    "interface": {"type": "string", "max_length": 15},
    "timezone": {"type": "string", "max_length": 63},
    "filename": {"type": "string", "max_length": 127},
    "conflicted-ip-timeout": {"type": "integer", "min": 60, "max": 8640000},
    "ipsec-lease-hold": {"type": "integer", "min": 0, "max": 8640000},
    "ddns-zone": {"type": "string", "max_length": 64},
    "ddns-keyname": {"type": "string", "max_length": 64},
    "ddns-ttl": {"type": "integer", "min": 60, "max": 86400},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "ip-range": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "start-ip": {
            "type": "ipv4-address",
            "help": "Start of IP range.",
            "required": True,
            "default": "0.0.0.0",
        },
        "end-ip": {
            "type": "ipv4-address",
            "help": "End of IP range.",
            "required": True,
            "default": "0.0.0.0",
        },
        "vci-match": {
            "type": "option",
            "help": "Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served with this range.",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "vci-string": {
            "type": "string",
            "help": "One or more VCI strings in quotes separated by spaces.",
        },
        "uci-match": {
            "type": "option",
            "help": "Enable/disable user class identifier (UCI) matching. When enabled only DHCP requests with a matching UCI are served with this range.",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "uci-string": {
            "type": "string",
            "help": "One or more UCI strings in quotes separated by spaces.",
        },
        "lease-time": {
            "type": "integer",
            "help": "Lease time in seconds, 0 means default lease time.",
            "default": 0,
            "min_value": 300,
            "max_value": 8640000,
        },
    },
    "tftp-server": {
        "tftp-server": {
            "type": "string",
            "help": "TFTP server.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
    },
    "options": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "code": {
            "type": "integer",
            "help": "DHCP option code.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "type": {
            "type": "option",
            "help": "DHCP option type.",
            "default": "hex",
            "options": ["hex", "string", "ip", "fqdn"],
        },
        "value": {
            "type": "string",
            "help": "DHCP option value.",
            "default": "",
            "max_length": 312,
        },
        "ip": {
            "type": "user",
            "help": "DHCP option IPs.",
            "default": "",
        },
        "vci-match": {
            "type": "option",
            "help": "Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served with this option.",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "vci-string": {
            "type": "string",
            "help": "One or more VCI strings in quotes separated by spaces.",
        },
        "uci-match": {
            "type": "option",
            "help": "Enable/disable user class identifier (UCI) matching. When enabled only DHCP requests with a matching UCI are served with this option.",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "uci-string": {
            "type": "string",
            "help": "One or more UCI strings in quotes separated by spaces.",
        },
    },
    "vci-string": {
        "vci-string": {
            "type": "string",
            "help": "VCI strings.",
            "required": True,
            "default": "",
            "max_length": 255,
        },
    },
    "exclude-range": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "start-ip": {
            "type": "ipv4-address",
            "help": "Start of IP range.",
            "required": True,
            "default": "0.0.0.0",
        },
        "end-ip": {
            "type": "ipv4-address",
            "help": "End of IP range.",
            "required": True,
            "default": "0.0.0.0",
        },
        "vci-match": {
            "type": "option",
            "help": "Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served with this range.",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "vci-string": {
            "type": "string",
            "help": "One or more VCI strings in quotes separated by spaces.",
        },
        "uci-match": {
            "type": "option",
            "help": "Enable/disable user class identifier (UCI) matching. When enabled only DHCP requests with a matching UCI are served with this range.",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "uci-string": {
            "type": "string",
            "help": "One or more UCI strings in quotes separated by spaces.",
        },
        "lease-time": {
            "type": "integer",
            "help": "Lease time in seconds, 0 means default lease time.",
            "default": 0,
            "min_value": 300,
            "max_value": 8640000,
        },
    },
    "reserved-address": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "type": {
            "type": "option",
            "help": "DHCP reserved-address type.",
            "default": "mac",
            "options": ["mac", "option82"],
        },
        "ip": {
            "type": "ipv4-address",
            "help": "IP address to be reserved for the MAC address.",
            "required": True,
            "default": "0.0.0.0",
        },
        "mac": {
            "type": "mac-address",
            "help": "MAC address of the client that will get the reserved IP address.",
            "required": True,
            "default": "00:00:00:00:00:00",
        },
        "action": {
            "type": "option",
            "help": "Options for the DHCP server to configure the client with the reserved MAC address.",
            "default": "reserved",
            "options": ["assign", "block", "reserved"],
        },
        "circuit-id-type": {
            "type": "option",
            "help": "DHCP option type.",
            "default": "string",
            "options": ["hex", "string"],
        },
        "circuit-id": {
            "type": "string",
            "help": "Option 82 circuit-ID of the client that will get the reserved IP address.",
            "default": "",
            "max_length": 312,
        },
        "remote-id-type": {
            "type": "option",
            "help": "DHCP option type.",
            "default": "string",
            "options": ["hex", "string"],
        },
        "remote-id": {
            "type": "string",
            "help": "Option 82 remote-ID of the client that will get the reserved IP address.",
            "default": "",
            "max_length": 312,
        },
        "description": {
            "type": "var-string",
            "help": "Description.",
            "max_length": 255,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "disable",
    "enable",
]
VALID_BODY_MAC_ACL_DEFAULT_ACTION = [
    "assign",
    "block",
]
VALID_BODY_FORTICLIENT_ON_NET_STATUS = [
    "disable",
    "enable",
]
VALID_BODY_DNS_SERVICE = [
    "local",
    "default",
    "specify",
]
VALID_BODY_WIFI_AC_SERVICE = [
    "specify",
    "local",
]
VALID_BODY_NTP_SERVICE = [
    "local",
    "default",
    "specify",
]
VALID_BODY_TIMEZONE_OPTION = [
    "disable",
    "default",
    "specify",
]
VALID_BODY_SERVER_TYPE = [
    "regular",
    "ipsec",
]
VALID_BODY_IP_MODE = [
    "range",
    "usrgrp",
]
VALID_BODY_AUTO_CONFIGURATION = [
    "disable",
    "enable",
]
VALID_BODY_DHCP_SETTINGS_FROM_FORTIIPAM = [
    "disable",
    "enable",
]
VALID_BODY_AUTO_MANAGED_STATUS = [
    "disable",
    "enable",
]
VALID_BODY_DDNS_UPDATE = [
    "disable",
    "enable",
]
VALID_BODY_DDNS_UPDATE_OVERRIDE = [
    "disable",
    "enable",
]
VALID_BODY_DDNS_AUTH = [
    "disable",
    "tsig",
]
VALID_BODY_VCI_MATCH = [
    "disable",
    "enable",
]
VALID_BODY_SHARED_SUBNET = [
    "disable",
    "enable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_dhcp_server_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/dhcp_server.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_dhcp_server_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by id
        >>> is_valid, error = validate_system_dhcp_server_get(id="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_dhcp_server_get(
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
    Validate required fields for system/dhcp_server.

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


def validate_system_dhcp_server_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/dhcp_server object.

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
        ...     "interface": True,  # DHCP server can assign IP configurations to client
        ...     "timezone": True,  # Select the time zone to be assigned to DHCP client
        ... }
        >>> is_valid, error = validate_system_dhcp_server_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "interface": True,
        ...     "status": "disable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_dhcp_server_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_system_dhcp_server_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_dhcp_server_post(payload)
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
    if "mac-acl-default-action" in payload:
        value = payload["mac-acl-default-action"]
        if value not in VALID_BODY_MAC_ACL_DEFAULT_ACTION:
            desc = FIELD_DESCRIPTIONS.get("mac-acl-default-action", "")
            error_msg = f"Invalid value for 'mac-acl-default-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_ACL_DEFAULT_ACTION)}"
            error_msg += f"\n  → Example: mac-acl-default-action='{{ VALID_BODY_MAC_ACL_DEFAULT_ACTION[0] }}'"
            return (False, error_msg)
    if "forticlient-on-net-status" in payload:
        value = payload["forticlient-on-net-status"]
        if value not in VALID_BODY_FORTICLIENT_ON_NET_STATUS:
            desc = FIELD_DESCRIPTIONS.get("forticlient-on-net-status", "")
            error_msg = f"Invalid value for 'forticlient-on-net-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTICLIENT_ON_NET_STATUS)}"
            error_msg += f"\n  → Example: forticlient-on-net-status='{{ VALID_BODY_FORTICLIENT_ON_NET_STATUS[0] }}'"
            return (False, error_msg)
    if "dns-service" in payload:
        value = payload["dns-service"]
        if value not in VALID_BODY_DNS_SERVICE:
            desc = FIELD_DESCRIPTIONS.get("dns-service", "")
            error_msg = f"Invalid value for 'dns-service': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DNS_SERVICE)}"
            error_msg += f"\n  → Example: dns-service='{{ VALID_BODY_DNS_SERVICE[0] }}'"
            return (False, error_msg)
    if "wifi-ac-service" in payload:
        value = payload["wifi-ac-service"]
        if value not in VALID_BODY_WIFI_AC_SERVICE:
            desc = FIELD_DESCRIPTIONS.get("wifi-ac-service", "")
            error_msg = f"Invalid value for 'wifi-ac-service': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WIFI_AC_SERVICE)}"
            error_msg += f"\n  → Example: wifi-ac-service='{{ VALID_BODY_WIFI_AC_SERVICE[0] }}'"
            return (False, error_msg)
    if "ntp-service" in payload:
        value = payload["ntp-service"]
        if value not in VALID_BODY_NTP_SERVICE:
            desc = FIELD_DESCRIPTIONS.get("ntp-service", "")
            error_msg = f"Invalid value for 'ntp-service': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NTP_SERVICE)}"
            error_msg += f"\n  → Example: ntp-service='{{ VALID_BODY_NTP_SERVICE[0] }}'"
            return (False, error_msg)
    if "timezone-option" in payload:
        value = payload["timezone-option"]
        if value not in VALID_BODY_TIMEZONE_OPTION:
            desc = FIELD_DESCRIPTIONS.get("timezone-option", "")
            error_msg = f"Invalid value for 'timezone-option': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TIMEZONE_OPTION)}"
            error_msg += f"\n  → Example: timezone-option='{{ VALID_BODY_TIMEZONE_OPTION[0] }}'"
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
    if "ip-mode" in payload:
        value = payload["ip-mode"]
        if value not in VALID_BODY_IP_MODE:
            desc = FIELD_DESCRIPTIONS.get("ip-mode", "")
            error_msg = f"Invalid value for 'ip-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_MODE)}"
            error_msg += f"\n  → Example: ip-mode='{{ VALID_BODY_IP_MODE[0] }}'"
            return (False, error_msg)
    if "auto-configuration" in payload:
        value = payload["auto-configuration"]
        if value not in VALID_BODY_AUTO_CONFIGURATION:
            desc = FIELD_DESCRIPTIONS.get("auto-configuration", "")
            error_msg = f"Invalid value for 'auto-configuration': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_CONFIGURATION)}"
            error_msg += f"\n  → Example: auto-configuration='{{ VALID_BODY_AUTO_CONFIGURATION[0] }}'"
            return (False, error_msg)
    if "dhcp-settings-from-fortiipam" in payload:
        value = payload["dhcp-settings-from-fortiipam"]
        if value not in VALID_BODY_DHCP_SETTINGS_FROM_FORTIIPAM:
            desc = FIELD_DESCRIPTIONS.get("dhcp-settings-from-fortiipam", "")
            error_msg = f"Invalid value for 'dhcp-settings-from-fortiipam': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_SETTINGS_FROM_FORTIIPAM)}"
            error_msg += f"\n  → Example: dhcp-settings-from-fortiipam='{{ VALID_BODY_DHCP_SETTINGS_FROM_FORTIIPAM[0] }}'"
            return (False, error_msg)
    if "auto-managed-status" in payload:
        value = payload["auto-managed-status"]
        if value not in VALID_BODY_AUTO_MANAGED_STATUS:
            desc = FIELD_DESCRIPTIONS.get("auto-managed-status", "")
            error_msg = f"Invalid value for 'auto-managed-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_MANAGED_STATUS)}"
            error_msg += f"\n  → Example: auto-managed-status='{{ VALID_BODY_AUTO_MANAGED_STATUS[0] }}'"
            return (False, error_msg)
    if "ddns-update" in payload:
        value = payload["ddns-update"]
        if value not in VALID_BODY_DDNS_UPDATE:
            desc = FIELD_DESCRIPTIONS.get("ddns-update", "")
            error_msg = f"Invalid value for 'ddns-update': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DDNS_UPDATE)}"
            error_msg += f"\n  → Example: ddns-update='{{ VALID_BODY_DDNS_UPDATE[0] }}'"
            return (False, error_msg)
    if "ddns-update-override" in payload:
        value = payload["ddns-update-override"]
        if value not in VALID_BODY_DDNS_UPDATE_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("ddns-update-override", "")
            error_msg = f"Invalid value for 'ddns-update-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DDNS_UPDATE_OVERRIDE)}"
            error_msg += f"\n  → Example: ddns-update-override='{{ VALID_BODY_DDNS_UPDATE_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "ddns-auth" in payload:
        value = payload["ddns-auth"]
        if value not in VALID_BODY_DDNS_AUTH:
            desc = FIELD_DESCRIPTIONS.get("ddns-auth", "")
            error_msg = f"Invalid value for 'ddns-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DDNS_AUTH)}"
            error_msg += f"\n  → Example: ddns-auth='{{ VALID_BODY_DDNS_AUTH[0] }}'"
            return (False, error_msg)
    if "vci-match" in payload:
        value = payload["vci-match"]
        if value not in VALID_BODY_VCI_MATCH:
            desc = FIELD_DESCRIPTIONS.get("vci-match", "")
            error_msg = f"Invalid value for 'vci-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VCI_MATCH)}"
            error_msg += f"\n  → Example: vci-match='{{ VALID_BODY_VCI_MATCH[0] }}'"
            return (False, error_msg)
    if "shared-subnet" in payload:
        value = payload["shared-subnet"]
        if value not in VALID_BODY_SHARED_SUBNET:
            desc = FIELD_DESCRIPTIONS.get("shared-subnet", "")
            error_msg = f"Invalid value for 'shared-subnet': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SHARED_SUBNET)}"
            error_msg += f"\n  → Example: shared-subnet='{{ VALID_BODY_SHARED_SUBNET[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_dhcp_server_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/dhcp_server.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_dhcp_server_put(payload)
    """
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "mac-acl-default-action" in payload:
        value = payload["mac-acl-default-action"]
        if value not in VALID_BODY_MAC_ACL_DEFAULT_ACTION:
            return (
                False,
                f"Invalid value for 'mac-acl-default-action'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_ACL_DEFAULT_ACTION)}",
            )
    if "forticlient-on-net-status" in payload:
        value = payload["forticlient-on-net-status"]
        if value not in VALID_BODY_FORTICLIENT_ON_NET_STATUS:
            return (
                False,
                f"Invalid value for 'forticlient-on-net-status'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTICLIENT_ON_NET_STATUS)}",
            )
    if "dns-service" in payload:
        value = payload["dns-service"]
        if value not in VALID_BODY_DNS_SERVICE:
            return (
                False,
                f"Invalid value for 'dns-service'='{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVICE)}",
            )
    if "wifi-ac-service" in payload:
        value = payload["wifi-ac-service"]
        if value not in VALID_BODY_WIFI_AC_SERVICE:
            return (
                False,
                f"Invalid value for 'wifi-ac-service'='{value}'. Must be one of: {', '.join(VALID_BODY_WIFI_AC_SERVICE)}",
            )
    if "ntp-service" in payload:
        value = payload["ntp-service"]
        if value not in VALID_BODY_NTP_SERVICE:
            return (
                False,
                f"Invalid value for 'ntp-service'='{value}'. Must be one of: {', '.join(VALID_BODY_NTP_SERVICE)}",
            )
    if "timezone-option" in payload:
        value = payload["timezone-option"]
        if value not in VALID_BODY_TIMEZONE_OPTION:
            return (
                False,
                f"Invalid value for 'timezone-option'='{value}'. Must be one of: {', '.join(VALID_BODY_TIMEZONE_OPTION)}",
            )
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid value for 'server-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )
    if "ip-mode" in payload:
        value = payload["ip-mode"]
        if value not in VALID_BODY_IP_MODE:
            return (
                False,
                f"Invalid value for 'ip-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_MODE)}",
            )
    if "auto-configuration" in payload:
        value = payload["auto-configuration"]
        if value not in VALID_BODY_AUTO_CONFIGURATION:
            return (
                False,
                f"Invalid value for 'auto-configuration'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_CONFIGURATION)}",
            )
    if "dhcp-settings-from-fortiipam" in payload:
        value = payload["dhcp-settings-from-fortiipam"]
        if value not in VALID_BODY_DHCP_SETTINGS_FROM_FORTIIPAM:
            return (
                False,
                f"Invalid value for 'dhcp-settings-from-fortiipam'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SETTINGS_FROM_FORTIIPAM)}",
            )
    if "auto-managed-status" in payload:
        value = payload["auto-managed-status"]
        if value not in VALID_BODY_AUTO_MANAGED_STATUS:
            return (
                False,
                f"Invalid value for 'auto-managed-status'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_MANAGED_STATUS)}",
            )
    if "ddns-update" in payload:
        value = payload["ddns-update"]
        if value not in VALID_BODY_DDNS_UPDATE:
            return (
                False,
                f"Invalid value for 'ddns-update'='{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_UPDATE)}",
            )
    if "ddns-update-override" in payload:
        value = payload["ddns-update-override"]
        if value not in VALID_BODY_DDNS_UPDATE_OVERRIDE:
            return (
                False,
                f"Invalid value for 'ddns-update-override'='{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_UPDATE_OVERRIDE)}",
            )
    if "ddns-auth" in payload:
        value = payload["ddns-auth"]
        if value not in VALID_BODY_DDNS_AUTH:
            return (
                False,
                f"Invalid value for 'ddns-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_AUTH)}",
            )
    if "vci-match" in payload:
        value = payload["vci-match"]
        if value not in VALID_BODY_VCI_MATCH:
            return (
                False,
                f"Invalid value for 'vci-match'='{value}'. Must be one of: {', '.join(VALID_BODY_VCI_MATCH)}",
            )
    if "shared-subnet" in payload:
        value = payload["shared-subnet"]
        if value not in VALID_BODY_SHARED_SUBNET:
            return (
                False,
                f"Invalid value for 'shared-subnet'='{value}'. Must be one of: {', '.join(VALID_BODY_SHARED_SUBNET)}",
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
    "endpoint": "system/dhcp_server",
    "category": "cmdb",
    "api_path": "system.dhcp/server",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure DHCP servers.",
    "total_fields": 52,
    "required_fields_count": 2,
    "fields_with_defaults_count": 45,
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
