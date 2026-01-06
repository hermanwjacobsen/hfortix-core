"""
Validation helpers for system/link_monitor endpoint.

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
    "server",  # IP address of the server(s) to be monitored.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "addr-mode": "ipv4",
    "srcintf": "",
    "server-config": "default",
    "server-type": "static",
    "protocol": "ping",
    "port": 0,
    "gateway-ip": "0.0.0.0",
    "gateway-ip6": "::",
    "source-ip": "0.0.0.0",
    "source-ip6": "::",
    "http-get": "/",
    "http-agent": "Chrome/ Safari/",
    "http-match": "",
    "interval": 500,
    "probe-timeout": 500,
    "failtime": 5,
    "recoverytime": 5,
    "probe-count": 30,
    "security-mode": "none",
    "packet-size": 124,
    "ha-priority": 1,
    "fail-weight": 0,
    "update-cascade-interface": "enable",
    "update-static-route": "enable",
    "update-policy-route": "enable",
    "status": "enable",
    "diffservcode": "",
    "class-id": 0,
    "service-detection": "disable",
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
    "name": "string",  # Link monitor name.
    "addr-mode": "option",  # Address mode (IPv4 or IPv6).
    "srcintf": "string",  # Interface that receives the traffic to be monitored.
    "server-config": "option",  # Mode of server configuration.
    "server-type": "option",  # Server type (static or dynamic).
    "server": "string",  # IP address of the server(s) to be monitored.
    "protocol": "option",  # Protocols used to monitor the server.
    "port": "integer",  # Port number of the traffic to be used to monitor the server.
    "gateway-ip": "ipv4-address-any",  # Gateway IP address used to probe the server.
    "gateway-ip6": "ipv6-address",  # Gateway IPv6 address used to probe the server.
    "route": "string",  # Subnet to monitor.
    "source-ip": "ipv4-address-any",  # Source IP address used in packet to the server.
    "source-ip6": "ipv6-address",  # Source IPv6 address used in packet to the server.
    "http-get": "string",  # If you are monitoring an HTML server you can send an HTTP-GE
    "http-agent": "string",  # String in the http-agent field in the HTTP header.
    "http-match": "string",  # String that you expect to see in the HTTP-GET requests of th
    "interval": "integer",  # Detection interval in milliseconds (20 - 3600 * 1000 msec, d
    "probe-timeout": "integer",  # Time to wait before a probe packet is considered lost (20 - 
    "failtime": "integer",  # Number of retry attempts before the server is considered dow
    "recoverytime": "integer",  # Number of successful responses received before server is con
    "probe-count": "integer",  # Number of most recent probes that should be used to calculat
    "security-mode": "option",  # Twamp controller security mode.
    "password": "password",  # TWAMP controller password in authentication mode.
    "packet-size": "integer",  # Packet size of a TWAMP test session (124/158 - 1024).
    "ha-priority": "integer",  # HA election priority (1 - 50).
    "fail-weight": "integer",  # Threshold weight to trigger link failure alert.
    "update-cascade-interface": "option",  # Enable/disable update cascade interface.
    "update-static-route": "option",  # Enable/disable updating the static route.
    "update-policy-route": "option",  # Enable/disable updating the policy route.
    "status": "option",  # Enable/disable this link monitor.
    "diffservcode": "user",  # Differentiated services code point (DSCP) in the IP header o
    "class-id": "integer",  # Traffic class ID.
    "service-detection": "option",  # Only use monitor to read quality values. If enabled, static 
    "server-list": "string",  # Servers for link-monitor to monitor.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Link monitor name.",
    "addr-mode": "Address mode (IPv4 or IPv6).",
    "srcintf": "Interface that receives the traffic to be monitored.",
    "server-config": "Mode of server configuration.",
    "server-type": "Server type (static or dynamic).",
    "server": "IP address of the server(s) to be monitored.",
    "protocol": "Protocols used to monitor the server.",
    "port": "Port number of the traffic to be used to monitor the server.",
    "gateway-ip": "Gateway IP address used to probe the server.",
    "gateway-ip6": "Gateway IPv6 address used to probe the server.",
    "route": "Subnet to monitor.",
    "source-ip": "Source IP address used in packet to the server.",
    "source-ip6": "Source IPv6 address used in packet to the server.",
    "http-get": "If you are monitoring an HTML server you can send an HTTP-GET request with a custom string. Use this option to define the string.",
    "http-agent": "String in the http-agent field in the HTTP header.",
    "http-match": "String that you expect to see in the HTTP-GET requests of the traffic to be monitored.",
    "interval": "Detection interval in milliseconds (20 - 3600 * 1000 msec, default = 500).",
    "probe-timeout": "Time to wait before a probe packet is considered lost (20 - 5000 msec, default = 500).",
    "failtime": "Number of retry attempts before the server is considered down (1 - 3600, default = 5).",
    "recoverytime": "Number of successful responses received before server is considered recovered (1 - 3600, default = 5).",
    "probe-count": "Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30).",
    "security-mode": "Twamp controller security mode.",
    "password": "TWAMP controller password in authentication mode.",
    "packet-size": "Packet size of a TWAMP test session (124/158 - 1024).",
    "ha-priority": "HA election priority (1 - 50).",
    "fail-weight": "Threshold weight to trigger link failure alert.",
    "update-cascade-interface": "Enable/disable update cascade interface.",
    "update-static-route": "Enable/disable updating the static route.",
    "update-policy-route": "Enable/disable updating the policy route.",
    "status": "Enable/disable this link monitor.",
    "diffservcode": "Differentiated services code point (DSCP) in the IP header of the probe packet.",
    "class-id": "Traffic class ID.",
    "service-detection": "Only use monitor to read quality values. If enabled, static routes and cascade interfaces will not be updated.",
    "server-list": "Servers for link-monitor to monitor.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "srcintf": {"type": "string", "max_length": 15},
    "port": {"type": "integer", "min": 1, "max": 65535},
    "http-get": {"type": "string", "max_length": 1024},
    "http-agent": {"type": "string", "max_length": 1024},
    "http-match": {"type": "string", "max_length": 1024},
    "interval": {"type": "integer", "min": 20, "max": 3600000},
    "probe-timeout": {"type": "integer", "min": 20, "max": 5000},
    "failtime": {"type": "integer", "min": 1, "max": 3600},
    "recoverytime": {"type": "integer", "min": 1, "max": 3600},
    "probe-count": {"type": "integer", "min": 5, "max": 30},
    "packet-size": {"type": "integer", "min": 0, "max": 65535},
    "ha-priority": {"type": "integer", "min": 1, "max": 50},
    "fail-weight": {"type": "integer", "min": 0, "max": 255},
    "class-id": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "server": {
        "address": {
            "type": "string",
            "help": "Server address.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "route": {
        "subnet": {
            "type": "string",
            "help": "IP and netmask (x.x.x.x/y).",
            "default": "",
            "max_length": 79,
        },
    },
    "server-list": {
        "id": {
            "type": "integer",
            "help": "Server ID.",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 32,
        },
        "dst": {
            "type": "string",
            "help": "IP address of the server to be monitored.",
            "required": True,
            "default": "",
            "max_length": 64,
        },
        "protocol": {
            "type": "option",
            "help": "Protocols used to monitor the server.",
            "default": "ping",
            "options": [{"help": "PING link monitor.", "label": "Ping", "name": "ping"}, {"help": "TCP echo link monitor.", "label": "Tcp Echo", "name": "tcp-echo"}, {"help": "UDP echo link monitor.", "label": "Udp Echo", "name": "udp-echo"}, {"help": "HTTP-GET link monitor.", "label": "Http", "name": "http"}, {"help": "HTTPS-GET link monitor.", "label": "Https", "name": "https"}, {"help": "TWAMP link monitor.", "label": "Twamp", "name": "twamp"}],
        },
        "port": {
            "type": "integer",
            "help": "Port number of the traffic to be used to monitor the server.",
            "default": 0,
            "min_value": 1,
            "max_value": 65535,
        },
        "weight": {
            "type": "integer",
            "help": "Weight of the monitor to this dst (0 - 255).",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_ADDR_MODE = [
    "ipv4",  # IPv4 mode.
    "ipv6",  # IPv6 mode.
]
VALID_BODY_SERVER_CONFIG = [
    "default",  # All servers share the same attributes.
    "individual",  # Some attributes can be specified for individual servers.
]
VALID_BODY_SERVER_TYPE = [
    "static",  # Static servers.
    "dynamic",  # Dynamic servers.
]
VALID_BODY_PROTOCOL = [
    "ping",  # PING link monitor.
    "tcp-echo",  # TCP echo link monitor.
    "udp-echo",  # UDP echo link monitor.
    "http",  # HTTP-GET link monitor.
    "https",  # HTTPS-GET link monitor.
    "twamp",  # TWAMP link monitor.
]
VALID_BODY_SECURITY_MODE = [
    "none",  # Unauthenticated mode.
    "authentication",  # Authenticated mode.
]
VALID_BODY_UPDATE_CASCADE_INTERFACE = [
    "enable",  # Enable update cascade interface.
    "disable",  # Disable update cascade interface.
]
VALID_BODY_UPDATE_STATIC_ROUTE = [
    "enable",  # Enable updating the static route.
    "disable",  # Disable updating the static route.
]
VALID_BODY_UPDATE_POLICY_ROUTE = [
    "enable",  # Enable updating the policy route.
    "disable",  # Disable updating the policy route.
]
VALID_BODY_STATUS = [
    "enable",  # Enable this link monitor.
    "disable",  # Disable this link monitor.
]
VALID_BODY_SERVICE_DETECTION = [
    "enable",  # Only use monitor for service-detection.
    "disable",  # Monitor will update routes/interfaces on link failure.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_link_monitor_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/link_monitor.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_link_monitor_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_system_link_monitor_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_link_monitor_get(
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
    Validate required fields for system/link_monitor.

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


def validate_system_link_monitor_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/link_monitor object.

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
        ...     "server": True,  # IP address of the server(s) to be monitored.
        ... }
        >>> is_valid, error = validate_system_link_monitor_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "server": True,
        ...     "addr-mode": "{'name': 'ipv4', 'help': 'IPv4 mode.', 'label': 'Ipv4', 'description': 'IPv4 mode'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_link_monitor_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["addr-mode"] = "invalid-value"
        >>> is_valid, error = validate_system_link_monitor_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_link_monitor_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "addr-mode" in payload:
        value = payload["addr-mode"]
        if value not in VALID_BODY_ADDR_MODE:
            desc = FIELD_DESCRIPTIONS.get("addr-mode", "")
            error_msg = f"Invalid value for 'addr-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDR_MODE)}"
            error_msg += f"\n  → Example: addr-mode='{{ VALID_BODY_ADDR_MODE[0] }}'"
            return (False, error_msg)
    if "server-config" in payload:
        value = payload["server-config"]
        if value not in VALID_BODY_SERVER_CONFIG:
            desc = FIELD_DESCRIPTIONS.get("server-config", "")
            error_msg = f"Invalid value for 'server-config': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_CONFIG)}"
            error_msg += f"\n  → Example: server-config='{{ VALID_BODY_SERVER_CONFIG[0] }}'"
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
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("protocol", "")
            error_msg = f"Invalid value for 'protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROTOCOL)}"
            error_msg += f"\n  → Example: protocol='{{ VALID_BODY_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "security-mode" in payload:
        value = payload["security-mode"]
        if value not in VALID_BODY_SECURITY_MODE:
            desc = FIELD_DESCRIPTIONS.get("security-mode", "")
            error_msg = f"Invalid value for 'security-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURITY_MODE)}"
            error_msg += f"\n  → Example: security-mode='{{ VALID_BODY_SECURITY_MODE[0] }}'"
            return (False, error_msg)
    if "update-cascade-interface" in payload:
        value = payload["update-cascade-interface"]
        if value not in VALID_BODY_UPDATE_CASCADE_INTERFACE:
            desc = FIELD_DESCRIPTIONS.get("update-cascade-interface", "")
            error_msg = f"Invalid value for 'update-cascade-interface': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_CASCADE_INTERFACE)}"
            error_msg += f"\n  → Example: update-cascade-interface='{{ VALID_BODY_UPDATE_CASCADE_INTERFACE[0] }}'"
            return (False, error_msg)
    if "update-static-route" in payload:
        value = payload["update-static-route"]
        if value not in VALID_BODY_UPDATE_STATIC_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("update-static-route", "")
            error_msg = f"Invalid value for 'update-static-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_STATIC_ROUTE)}"
            error_msg += f"\n  → Example: update-static-route='{{ VALID_BODY_UPDATE_STATIC_ROUTE[0] }}'"
            return (False, error_msg)
    if "update-policy-route" in payload:
        value = payload["update-policy-route"]
        if value not in VALID_BODY_UPDATE_POLICY_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("update-policy-route", "")
            error_msg = f"Invalid value for 'update-policy-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_POLICY_ROUTE)}"
            error_msg += f"\n  → Example: update-policy-route='{{ VALID_BODY_UPDATE_POLICY_ROUTE[0] }}'"
            return (False, error_msg)
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
    if "service-detection" in payload:
        value = payload["service-detection"]
        if value not in VALID_BODY_SERVICE_DETECTION:
            desc = FIELD_DESCRIPTIONS.get("service-detection", "")
            error_msg = f"Invalid value for 'service-detection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVICE_DETECTION)}"
            error_msg += f"\n  → Example: service-detection='{{ VALID_BODY_SERVICE_DETECTION[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_link_monitor_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/link_monitor.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_link_monitor_put(payload)
    """
    # Step 1: Validate enum values
    if "addr-mode" in payload:
        value = payload["addr-mode"]
        if value not in VALID_BODY_ADDR_MODE:
            return (
                False,
                f"Invalid value for 'addr-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_MODE)}",
            )
    if "server-config" in payload:
        value = payload["server-config"]
        if value not in VALID_BODY_SERVER_CONFIG:
            return (
                False,
                f"Invalid value for 'server-config'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_CONFIG)}",
            )
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid value for 'server-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid value for 'protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )
    if "security-mode" in payload:
        value = payload["security-mode"]
        if value not in VALID_BODY_SECURITY_MODE:
            return (
                False,
                f"Invalid value for 'security-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MODE)}",
            )
    if "update-cascade-interface" in payload:
        value = payload["update-cascade-interface"]
        if value not in VALID_BODY_UPDATE_CASCADE_INTERFACE:
            return (
                False,
                f"Invalid value for 'update-cascade-interface'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_CASCADE_INTERFACE)}",
            )
    if "update-static-route" in payload:
        value = payload["update-static-route"]
        if value not in VALID_BODY_UPDATE_STATIC_ROUTE:
            return (
                False,
                f"Invalid value for 'update-static-route'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_STATIC_ROUTE)}",
            )
    if "update-policy-route" in payload:
        value = payload["update-policy-route"]
        if value not in VALID_BODY_UPDATE_POLICY_ROUTE:
            return (
                False,
                f"Invalid value for 'update-policy-route'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_POLICY_ROUTE)}",
            )
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "service-detection" in payload:
        value = payload["service-detection"]
        if value not in VALID_BODY_SERVICE_DETECTION:
            return (
                False,
                f"Invalid value for 'service-detection'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_DETECTION)}",
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
    "endpoint": "system/link_monitor",
    "category": "cmdb",
    "api_path": "system/link-monitor",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure Link Health Monitor.",
    "total_fields": 34,
    "required_fields_count": 1,
    "fields_with_defaults_count": 30,
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
