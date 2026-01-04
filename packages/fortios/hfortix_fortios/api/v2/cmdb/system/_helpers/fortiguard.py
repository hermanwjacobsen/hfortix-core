"""
Validation helpers for system/fortiguard endpoint.

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
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "fortiguard-anycast": "enable",
    "fortiguard-anycast-source": "fortinet",
    "protocol": "https",
    "port": "443",
    "load-balance-servers": 1,
    "auto-join-forticloud": "enable",
    "update-server-location": "automatic",
    "sandbox-region": "",
    "sandbox-inline-scan": "disable",
    "update-ffdb": "enable",
    "update-uwdb": "enable",
    "update-dldb": "enable",
    "update-extdb": "enable",
    "update-build-proxy": "enable",
    "persistent-connection": "disable",
    "vdom": "",
    "auto-firmware-upgrade": "enable",
    "auto-firmware-upgrade-day": "",
    "auto-firmware-upgrade-delay": 3,
    "auto-firmware-upgrade-start-hour": 1,
    "auto-firmware-upgrade-end-hour": 4,
    "FDS-license-expiring-days": 15,
    "subscribe-update-notification": "disable",
    "antispam-force-off": "disable",
    "antispam-cache": "enable",
    "antispam-cache-ttl": 1800,
    "antispam-cache-mpermille": 1,
    "antispam-license": 4294967295,
    "antispam-expiration": 0,
    "antispam-timeout": 7,
    "outbreak-prevention-force-off": "disable",
    "outbreak-prevention-cache": "enable",
    "outbreak-prevention-cache-ttl": 300,
    "outbreak-prevention-cache-mpermille": 1,
    "outbreak-prevention-license": 4294967295,
    "outbreak-prevention-expiration": 0,
    "outbreak-prevention-timeout": 7,
    "webfilter-force-off": "disable",
    "webfilter-cache": "enable",
    "webfilter-cache-ttl": 3600,
    "webfilter-license": 4294967295,
    "webfilter-expiration": 0,
    "webfilter-timeout": 15,
    "sdns-server-ip": "",
    "sdns-server-port": 53,
    "anycast-sdns-server-ip": "0.0.0.0",
    "anycast-sdns-server-port": 853,
    "sdns-options": "",
    "source-ip": "0.0.0.0",
    "source-ip6": "::",
    "proxy-server-ip": "",
    "proxy-server-port": 0,
    "proxy-username": "",
    "ddns-server-ip": "0.0.0.0",
    "ddns-server-ip6": "::",
    "ddns-server-port": 443,
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
    "fortiguard-anycast": "option",  # Enable/disable use of FortiGuard's Anycast network.
    "fortiguard-anycast-source": "option",  # Configure which of Fortinet's servers to provide FortiGuard 
    "protocol": "option",  # Protocol used to communicate with the FortiGuard servers.
    "port": "option",  # Port used to communicate with the FortiGuard servers.
    "load-balance-servers": "integer",  # Number of servers to alternate between as first FortiGuard o
    "auto-join-forticloud": "option",  # Automatically connect to and login to FortiCloud.
    "update-server-location": "option",  # Location from which to receive FortiGuard updates.
    "sandbox-region": "string",  # FortiCloud Sandbox region.
    "sandbox-inline-scan": "option",  # Enable/disable FortiCloud Sandbox inline-scan.
    "update-ffdb": "option",  # Enable/disable Internet Service Database update.
    "update-uwdb": "option",  # Enable/disable allowlist update.
    "update-dldb": "option",  # Enable/disable DLP signature update.
    "update-extdb": "option",  # Enable/disable external resource update.
    "update-build-proxy": "option",  # Enable/disable proxy dictionary rebuild.
    "persistent-connection": "option",  # Enable/disable use of persistent connection to receive updat
    "vdom": "string",  # FortiGuard Service virtual domain name.
    "auto-firmware-upgrade": "option",  # Enable/disable automatic patch-level firmware upgrade from F
    "auto-firmware-upgrade-day": "option",  # Allowed day(s) of the week to install an automatic patch-lev
    "auto-firmware-upgrade-delay": "integer",  # Delay of day(s) before installing an automatic patch-level f
    "auto-firmware-upgrade-start-hour": "integer",  # Start time in the designated time window for automatic patch
    "auto-firmware-upgrade-end-hour": "integer",  # End time in the designated time window for automatic patch-l
    "FDS-license-expiring-days": "integer",  # Threshold for number of days before FortiGuard license expir
    "subscribe-update-notification": "option",  # Enable/disable subscription to receive update notification f
    "antispam-force-off": "option",  # Enable/disable turning off the FortiGuard antispam service.
    "antispam-cache": "option",  # Enable/disable FortiGuard antispam request caching. Uses a s
    "antispam-cache-ttl": "integer",  # Time-to-live for antispam cache entries in seconds (300 - 86
    "antispam-cache-mpermille": "integer",  # Maximum permille of FortiGate memory the antispam cache is a
    "antispam-license": "integer",  # Interval of time between license checks for the FortiGuard a
    "antispam-expiration": "integer",  # Expiration date of the FortiGuard antispam contract.
    "antispam-timeout": "integer",  # Antispam query time out (1 - 30 sec, default = 7).
    "outbreak-prevention-force-off": "option",  # Turn off FortiGuard Virus Outbreak Prevention service.
    "outbreak-prevention-cache": "option",  # Enable/disable FortiGuard Virus Outbreak Prevention cache.
    "outbreak-prevention-cache-ttl": "integer",  # Time-to-live for FortiGuard Virus Outbreak Prevention cache 
    "outbreak-prevention-cache-mpermille": "integer",  # Maximum permille of memory FortiGuard Virus Outbreak Prevent
    "outbreak-prevention-license": "integer",  # Interval of time between license checks for FortiGuard Virus
    "outbreak-prevention-expiration": "integer",  # Expiration date of FortiGuard Virus Outbreak Prevention cont
    "outbreak-prevention-timeout": "integer",  # FortiGuard Virus Outbreak Prevention time out (1 - 30 sec, d
    "webfilter-force-off": "option",  # Enable/disable turning off the FortiGuard web filtering serv
    "webfilter-cache": "option",  # Enable/disable FortiGuard web filter caching.
    "webfilter-cache-ttl": "integer",  # Time-to-live for web filter cache entries in seconds (300 - 
    "webfilter-license": "integer",  # Interval of time between license checks for the FortiGuard w
    "webfilter-expiration": "integer",  # Expiration date of the FortiGuard web filter contract.
    "webfilter-timeout": "integer",  # Web filter query time out (1 - 30 sec, default = 15).
    "sdns-server-ip": "user",  # IP address of the FortiGuard DNS rating server.
    "sdns-server-port": "integer",  # Port to connect to on the FortiGuard DNS rating server.
    "anycast-sdns-server-ip": "ipv4-address",  # IP address of the FortiGuard anycast DNS rating server.
    "anycast-sdns-server-port": "integer",  # Port to connect to on the FortiGuard anycast DNS rating serv
    "sdns-options": "option",  # Customization options for the FortiGuard DNS service.
    "source-ip": "ipv4-address",  # Source IPv4 address used to communicate with FortiGuard.
    "source-ip6": "ipv6-address",  # Source IPv6 address used to communicate with FortiGuard.
    "proxy-server-ip": "string",  # Hostname or IPv4 address of the proxy server.
    "proxy-server-port": "integer",  # Port used to communicate with the proxy server.
    "proxy-username": "string",  # Proxy user name.
    "proxy-password": "password",  # Proxy user password.
    "ddns-server-ip": "ipv4-address",  # IP address of the FortiDDNS server.
    "ddns-server-ip6": "ipv6-address",  # IPv6 address of the FortiDDNS server.
    "ddns-server-port": "integer",  # Port used to communicate with FortiDDNS servers.
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "fortiguard-anycast": "Enable/disable use of FortiGuard's Anycast network.",
    "fortiguard-anycast-source": "Configure which of Fortinet's servers to provide FortiGuard services in FortiGuard's anycast network. Default is Fortinet.",
    "protocol": "Protocol used to communicate with the FortiGuard servers.",
    "port": "Port used to communicate with the FortiGuard servers.",
    "load-balance-servers": "Number of servers to alternate between as first FortiGuard option.",
    "auto-join-forticloud": "Automatically connect to and login to FortiCloud.",
    "update-server-location": "Location from which to receive FortiGuard updates.",
    "sandbox-region": "FortiCloud Sandbox region.",
    "sandbox-inline-scan": "Enable/disable FortiCloud Sandbox inline-scan.",
    "update-ffdb": "Enable/disable Internet Service Database update.",
    "update-uwdb": "Enable/disable allowlist update.",
    "update-dldb": "Enable/disable DLP signature update.",
    "update-extdb": "Enable/disable external resource update.",
    "update-build-proxy": "Enable/disable proxy dictionary rebuild.",
    "persistent-connection": "Enable/disable use of persistent connection to receive update notification from FortiGuard.",
    "vdom": "FortiGuard Service virtual domain name.",
    "auto-firmware-upgrade": "Enable/disable automatic patch-level firmware upgrade from FortiGuard. The FortiGate unit searches for new patches only in the same major and minor version.",
    "auto-firmware-upgrade-day": "Allowed day(s) of the week to install an automatic patch-level firmware upgrade from FortiGuard (default is none). Disallow any day of the week to use auto-firmware-upgrade-delay instead, which waits for designated days before installing an automatic patch-level firmware upgrade.",
    "auto-firmware-upgrade-delay": "Delay of day(s) before installing an automatic patch-level firmware upgrade from FortiGuard (default = 3). Set it 0 to use auto-firmware-upgrade-day instead, which selects allowed day(s) of the week for installing an automatic patch-level firmware upgrade.",
    "auto-firmware-upgrade-start-hour": "Start time in the designated time window for automatic patch-level firmware upgrade from FortiGuard in 24 hour time (0 ~ 23, default = 2). The actual upgrade time is selected randomly within the time window.",
    "auto-firmware-upgrade-end-hour": "End time in the designated time window for automatic patch-level firmware upgrade from FortiGuard in 24 hour time (0 ~ 23, default = 4). When the end time is smaller than the start time, the end time is interpreted as the next day. The actual upgrade time is selected randomly within the time window.",
    "FDS-license-expiring-days": "Threshold for number of days before FortiGuard license expiration to generate license expiring event log (1 - 100 days, default = 15).",
    "subscribe-update-notification": "Enable/disable subscription to receive update notification from FortiGuard.",
    "antispam-force-off": "Enable/disable turning off the FortiGuard antispam service.",
    "antispam-cache": "Enable/disable FortiGuard antispam request caching. Uses a small amount of memory but improves performance.",
    "antispam-cache-ttl": "Time-to-live for antispam cache entries in seconds (300 - 86400). Lower times reduce the cache size. Higher times may improve performance since the cache will have more entries.",
    "antispam-cache-mpermille": "Maximum permille of FortiGate memory the antispam cache is allowed to use (1 - 150).",
    "antispam-license": "Interval of time between license checks for the FortiGuard antispam contract.",
    "antispam-expiration": "Expiration date of the FortiGuard antispam contract.",
    "antispam-timeout": "Antispam query time out (1 - 30 sec, default = 7).",
    "outbreak-prevention-force-off": "Turn off FortiGuard Virus Outbreak Prevention service.",
    "outbreak-prevention-cache": "Enable/disable FortiGuard Virus Outbreak Prevention cache.",
    "outbreak-prevention-cache-ttl": "Time-to-live for FortiGuard Virus Outbreak Prevention cache entries (300 - 86400 sec, default = 300).",
    "outbreak-prevention-cache-mpermille": "Maximum permille of memory FortiGuard Virus Outbreak Prevention cache can use (1 - 150 permille, default = 1).",
    "outbreak-prevention-license": "Interval of time between license checks for FortiGuard Virus Outbreak Prevention contract.",
    "outbreak-prevention-expiration": "Expiration date of FortiGuard Virus Outbreak Prevention contract.",
    "outbreak-prevention-timeout": "FortiGuard Virus Outbreak Prevention time out (1 - 30 sec, default = 7).",
    "webfilter-force-off": "Enable/disable turning off the FortiGuard web filtering service.",
    "webfilter-cache": "Enable/disable FortiGuard web filter caching.",
    "webfilter-cache-ttl": "Time-to-live for web filter cache entries in seconds (300 - 86400).",
    "webfilter-license": "Interval of time between license checks for the FortiGuard web filter contract.",
    "webfilter-expiration": "Expiration date of the FortiGuard web filter contract.",
    "webfilter-timeout": "Web filter query time out (1 - 30 sec, default = 15).",
    "sdns-server-ip": "IP address of the FortiGuard DNS rating server.",
    "sdns-server-port": "Port to connect to on the FortiGuard DNS rating server.",
    "anycast-sdns-server-ip": "IP address of the FortiGuard anycast DNS rating server.",
    "anycast-sdns-server-port": "Port to connect to on the FortiGuard anycast DNS rating server.",
    "sdns-options": "Customization options for the FortiGuard DNS service.",
    "source-ip": "Source IPv4 address used to communicate with FortiGuard.",
    "source-ip6": "Source IPv6 address used to communicate with FortiGuard.",
    "proxy-server-ip": "Hostname or IPv4 address of the proxy server.",
    "proxy-server-port": "Port used to communicate with the proxy server.",
    "proxy-username": "Proxy user name.",
    "proxy-password": "Proxy user password.",
    "ddns-server-ip": "IP address of the FortiDDNS server.",
    "ddns-server-ip6": "IPv6 address of the FortiDDNS server.",
    "ddns-server-port": "Port used to communicate with FortiDDNS servers.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "load-balance-servers": {"type": "integer", "min": 1, "max": 266},
    "sandbox-region": {"type": "string", "max_length": 63},
    "vdom": {"type": "string", "max_length": 31},
    "auto-firmware-upgrade-delay": {"type": "integer", "min": 0, "max": 14},
    "auto-firmware-upgrade-start-hour": {"type": "integer", "min": 0, "max": 23},
    "auto-firmware-upgrade-end-hour": {"type": "integer", "min": 0, "max": 23},
    "FDS-license-expiring-days": {"type": "integer", "min": 1, "max": 100},
    "antispam-cache-ttl": {"type": "integer", "min": 300, "max": 86400},
    "antispam-cache-mpermille": {"type": "integer", "min": 1, "max": 150},
    "antispam-license": {"type": "integer", "min": 0, "max": 4294967295},
    "antispam-expiration": {"type": "integer", "min": 0, "max": 4294967295},
    "antispam-timeout": {"type": "integer", "min": 1, "max": 30},
    "outbreak-prevention-cache-ttl": {"type": "integer", "min": 300, "max": 86400},
    "outbreak-prevention-cache-mpermille": {"type": "integer", "min": 1, "max": 150},
    "outbreak-prevention-license": {"type": "integer", "min": 0, "max": 4294967295},
    "outbreak-prevention-expiration": {"type": "integer", "min": 0, "max": 4294967295},
    "outbreak-prevention-timeout": {"type": "integer", "min": 1, "max": 30},
    "webfilter-cache-ttl": {"type": "integer", "min": 300, "max": 86400},
    "webfilter-license": {"type": "integer", "min": 0, "max": 4294967295},
    "webfilter-expiration": {"type": "integer", "min": 0, "max": 4294967295},
    "webfilter-timeout": {"type": "integer", "min": 1, "max": 30},
    "sdns-server-port": {"type": "integer", "min": 1, "max": 65535},
    "anycast-sdns-server-port": {"type": "integer", "min": 1, "max": 65535},
    "proxy-server-ip": {"type": "string", "max_length": 63},
    "proxy-server-port": {"type": "integer", "min": 0, "max": 65535},
    "proxy-username": {"type": "string", "max_length": 64},
    "ddns-server-port": {"type": "integer", "min": 1, "max": 65535},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_FORTIGUARD_ANYCAST = [
    "enable",
    "disable",
]
VALID_BODY_FORTIGUARD_ANYCAST_SOURCE = [
    "fortinet",
    "aws",
    "debug",
]
VALID_BODY_PROTOCOL = [
    "udp",
    "http",
    "https",
]
VALID_BODY_PORT = [
    "8888",
    "53",
    "80",
    "443",
]
VALID_BODY_AUTO_JOIN_FORTICLOUD = [
    "enable",
    "disable",
]
VALID_BODY_UPDATE_SERVER_LOCATION = [
    "automatic",
    "usa",
    "eu",
]
VALID_BODY_SANDBOX_INLINE_SCAN = [
    "enable",
    "disable",
]
VALID_BODY_UPDATE_FFDB = [
    "enable",
    "disable",
]
VALID_BODY_UPDATE_UWDB = [
    "enable",
    "disable",
]
VALID_BODY_UPDATE_DLDB = [
    "enable",
    "disable",
]
VALID_BODY_UPDATE_EXTDB = [
    "enable",
    "disable",
]
VALID_BODY_UPDATE_BUILD_PROXY = [
    "enable",
    "disable",
]
VALID_BODY_PERSISTENT_CONNECTION = [
    "enable",
    "disable",
]
VALID_BODY_AUTO_FIRMWARE_UPGRADE = [
    "enable",
    "disable",
]
VALID_BODY_AUTO_FIRMWARE_UPGRADE_DAY = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]
VALID_BODY_SUBSCRIBE_UPDATE_NOTIFICATION = [
    "enable",
    "disable",
]
VALID_BODY_ANTISPAM_FORCE_OFF = [
    "enable",
    "disable",
]
VALID_BODY_ANTISPAM_CACHE = [
    "enable",
    "disable",
]
VALID_BODY_OUTBREAK_PREVENTION_FORCE_OFF = [
    "enable",
    "disable",
]
VALID_BODY_OUTBREAK_PREVENTION_CACHE = [
    "enable",
    "disable",
]
VALID_BODY_WEBFILTER_FORCE_OFF = [
    "enable",
    "disable",
]
VALID_BODY_WEBFILTER_CACHE = [
    "enable",
    "disable",
]
VALID_BODY_SDNS_OPTIONS = [
    "include-question-section",
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "auto",
    "sdwan",
    "specify",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_fortiguard_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/fortiguard.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_fortiguard_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_fortiguard_get(
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
    Validate required fields for system/fortiguard.

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


def validate_system_fortiguard_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/fortiguard object.

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
        ...     "interface": True,  # Specify outgoing interface to reach server.
        ... }
        >>> is_valid, error = validate_system_fortiguard_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "interface": True,
        ...     "fortiguard-anycast": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_fortiguard_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["fortiguard-anycast"] = "invalid-value"
        >>> is_valid, error = validate_system_fortiguard_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_fortiguard_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "fortiguard-anycast" in payload:
        value = payload["fortiguard-anycast"]
        if value not in VALID_BODY_FORTIGUARD_ANYCAST:
            desc = FIELD_DESCRIPTIONS.get("fortiguard-anycast", "")
            error_msg = f"Invalid value for 'fortiguard-anycast': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTIGUARD_ANYCAST)}"
            error_msg += f"\n  → Example: fortiguard-anycast='{{ VALID_BODY_FORTIGUARD_ANYCAST[0] }}'"
            return (False, error_msg)
    if "fortiguard-anycast-source" in payload:
        value = payload["fortiguard-anycast-source"]
        if value not in VALID_BODY_FORTIGUARD_ANYCAST_SOURCE:
            desc = FIELD_DESCRIPTIONS.get("fortiguard-anycast-source", "")
            error_msg = f"Invalid value for 'fortiguard-anycast-source': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTIGUARD_ANYCAST_SOURCE)}"
            error_msg += f"\n  → Example: fortiguard-anycast-source='{{ VALID_BODY_FORTIGUARD_ANYCAST_SOURCE[0] }}'"
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
    if "port" in payload:
        value = payload["port"]
        if value not in VALID_BODY_PORT:
            desc = FIELD_DESCRIPTIONS.get("port", "")
            error_msg = f"Invalid value for 'port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORT)}"
            error_msg += f"\n  → Example: port='{{ VALID_BODY_PORT[0] }}'"
            return (False, error_msg)
    if "auto-join-forticloud" in payload:
        value = payload["auto-join-forticloud"]
        if value not in VALID_BODY_AUTO_JOIN_FORTICLOUD:
            desc = FIELD_DESCRIPTIONS.get("auto-join-forticloud", "")
            error_msg = f"Invalid value for 'auto-join-forticloud': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_JOIN_FORTICLOUD)}"
            error_msg += f"\n  → Example: auto-join-forticloud='{{ VALID_BODY_AUTO_JOIN_FORTICLOUD[0] }}'"
            return (False, error_msg)
    if "update-server-location" in payload:
        value = payload["update-server-location"]
        if value not in VALID_BODY_UPDATE_SERVER_LOCATION:
            desc = FIELD_DESCRIPTIONS.get("update-server-location", "")
            error_msg = f"Invalid value for 'update-server-location': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_SERVER_LOCATION)}"
            error_msg += f"\n  → Example: update-server-location='{{ VALID_BODY_UPDATE_SERVER_LOCATION[0] }}'"
            return (False, error_msg)
    if "sandbox-inline-scan" in payload:
        value = payload["sandbox-inline-scan"]
        if value not in VALID_BODY_SANDBOX_INLINE_SCAN:
            desc = FIELD_DESCRIPTIONS.get("sandbox-inline-scan", "")
            error_msg = f"Invalid value for 'sandbox-inline-scan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SANDBOX_INLINE_SCAN)}"
            error_msg += f"\n  → Example: sandbox-inline-scan='{{ VALID_BODY_SANDBOX_INLINE_SCAN[0] }}'"
            return (False, error_msg)
    if "update-ffdb" in payload:
        value = payload["update-ffdb"]
        if value not in VALID_BODY_UPDATE_FFDB:
            desc = FIELD_DESCRIPTIONS.get("update-ffdb", "")
            error_msg = f"Invalid value for 'update-ffdb': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_FFDB)}"
            error_msg += f"\n  → Example: update-ffdb='{{ VALID_BODY_UPDATE_FFDB[0] }}'"
            return (False, error_msg)
    if "update-uwdb" in payload:
        value = payload["update-uwdb"]
        if value not in VALID_BODY_UPDATE_UWDB:
            desc = FIELD_DESCRIPTIONS.get("update-uwdb", "")
            error_msg = f"Invalid value for 'update-uwdb': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_UWDB)}"
            error_msg += f"\n  → Example: update-uwdb='{{ VALID_BODY_UPDATE_UWDB[0] }}'"
            return (False, error_msg)
    if "update-dldb" in payload:
        value = payload["update-dldb"]
        if value not in VALID_BODY_UPDATE_DLDB:
            desc = FIELD_DESCRIPTIONS.get("update-dldb", "")
            error_msg = f"Invalid value for 'update-dldb': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_DLDB)}"
            error_msg += f"\n  → Example: update-dldb='{{ VALID_BODY_UPDATE_DLDB[0] }}'"
            return (False, error_msg)
    if "update-extdb" in payload:
        value = payload["update-extdb"]
        if value not in VALID_BODY_UPDATE_EXTDB:
            desc = FIELD_DESCRIPTIONS.get("update-extdb", "")
            error_msg = f"Invalid value for 'update-extdb': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_EXTDB)}"
            error_msg += f"\n  → Example: update-extdb='{{ VALID_BODY_UPDATE_EXTDB[0] }}'"
            return (False, error_msg)
    if "update-build-proxy" in payload:
        value = payload["update-build-proxy"]
        if value not in VALID_BODY_UPDATE_BUILD_PROXY:
            desc = FIELD_DESCRIPTIONS.get("update-build-proxy", "")
            error_msg = f"Invalid value for 'update-build-proxy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_BUILD_PROXY)}"
            error_msg += f"\n  → Example: update-build-proxy='{{ VALID_BODY_UPDATE_BUILD_PROXY[0] }}'"
            return (False, error_msg)
    if "persistent-connection" in payload:
        value = payload["persistent-connection"]
        if value not in VALID_BODY_PERSISTENT_CONNECTION:
            desc = FIELD_DESCRIPTIONS.get("persistent-connection", "")
            error_msg = f"Invalid value for 'persistent-connection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERSISTENT_CONNECTION)}"
            error_msg += f"\n  → Example: persistent-connection='{{ VALID_BODY_PERSISTENT_CONNECTION[0] }}'"
            return (False, error_msg)
    if "auto-firmware-upgrade" in payload:
        value = payload["auto-firmware-upgrade"]
        if value not in VALID_BODY_AUTO_FIRMWARE_UPGRADE:
            desc = FIELD_DESCRIPTIONS.get("auto-firmware-upgrade", "")
            error_msg = f"Invalid value for 'auto-firmware-upgrade': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_FIRMWARE_UPGRADE)}"
            error_msg += f"\n  → Example: auto-firmware-upgrade='{{ VALID_BODY_AUTO_FIRMWARE_UPGRADE[0] }}'"
            return (False, error_msg)
    if "auto-firmware-upgrade-day" in payload:
        value = payload["auto-firmware-upgrade-day"]
        if value not in VALID_BODY_AUTO_FIRMWARE_UPGRADE_DAY:
            desc = FIELD_DESCRIPTIONS.get("auto-firmware-upgrade-day", "")
            error_msg = f"Invalid value for 'auto-firmware-upgrade-day': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_FIRMWARE_UPGRADE_DAY)}"
            error_msg += f"\n  → Example: auto-firmware-upgrade-day='{{ VALID_BODY_AUTO_FIRMWARE_UPGRADE_DAY[0] }}'"
            return (False, error_msg)
    if "subscribe-update-notification" in payload:
        value = payload["subscribe-update-notification"]
        if value not in VALID_BODY_SUBSCRIBE_UPDATE_NOTIFICATION:
            desc = FIELD_DESCRIPTIONS.get("subscribe-update-notification", "")
            error_msg = f"Invalid value for 'subscribe-update-notification': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SUBSCRIBE_UPDATE_NOTIFICATION)}"
            error_msg += f"\n  → Example: subscribe-update-notification='{{ VALID_BODY_SUBSCRIBE_UPDATE_NOTIFICATION[0] }}'"
            return (False, error_msg)
    if "antispam-force-off" in payload:
        value = payload["antispam-force-off"]
        if value not in VALID_BODY_ANTISPAM_FORCE_OFF:
            desc = FIELD_DESCRIPTIONS.get("antispam-force-off", "")
            error_msg = f"Invalid value for 'antispam-force-off': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ANTISPAM_FORCE_OFF)}"
            error_msg += f"\n  → Example: antispam-force-off='{{ VALID_BODY_ANTISPAM_FORCE_OFF[0] }}'"
            return (False, error_msg)
    if "antispam-cache" in payload:
        value = payload["antispam-cache"]
        if value not in VALID_BODY_ANTISPAM_CACHE:
            desc = FIELD_DESCRIPTIONS.get("antispam-cache", "")
            error_msg = f"Invalid value for 'antispam-cache': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ANTISPAM_CACHE)}"
            error_msg += f"\n  → Example: antispam-cache='{{ VALID_BODY_ANTISPAM_CACHE[0] }}'"
            return (False, error_msg)
    if "outbreak-prevention-force-off" in payload:
        value = payload["outbreak-prevention-force-off"]
        if value not in VALID_BODY_OUTBREAK_PREVENTION_FORCE_OFF:
            desc = FIELD_DESCRIPTIONS.get("outbreak-prevention-force-off", "")
            error_msg = f"Invalid value for 'outbreak-prevention-force-off': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OUTBREAK_PREVENTION_FORCE_OFF)}"
            error_msg += f"\n  → Example: outbreak-prevention-force-off='{{ VALID_BODY_OUTBREAK_PREVENTION_FORCE_OFF[0] }}'"
            return (False, error_msg)
    if "outbreak-prevention-cache" in payload:
        value = payload["outbreak-prevention-cache"]
        if value not in VALID_BODY_OUTBREAK_PREVENTION_CACHE:
            desc = FIELD_DESCRIPTIONS.get("outbreak-prevention-cache", "")
            error_msg = f"Invalid value for 'outbreak-prevention-cache': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OUTBREAK_PREVENTION_CACHE)}"
            error_msg += f"\n  → Example: outbreak-prevention-cache='{{ VALID_BODY_OUTBREAK_PREVENTION_CACHE[0] }}'"
            return (False, error_msg)
    if "webfilter-force-off" in payload:
        value = payload["webfilter-force-off"]
        if value not in VALID_BODY_WEBFILTER_FORCE_OFF:
            desc = FIELD_DESCRIPTIONS.get("webfilter-force-off", "")
            error_msg = f"Invalid value for 'webfilter-force-off': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEBFILTER_FORCE_OFF)}"
            error_msg += f"\n  → Example: webfilter-force-off='{{ VALID_BODY_WEBFILTER_FORCE_OFF[0] }}'"
            return (False, error_msg)
    if "webfilter-cache" in payload:
        value = payload["webfilter-cache"]
        if value not in VALID_BODY_WEBFILTER_CACHE:
            desc = FIELD_DESCRIPTIONS.get("webfilter-cache", "")
            error_msg = f"Invalid value for 'webfilter-cache': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEBFILTER_CACHE)}"
            error_msg += f"\n  → Example: webfilter-cache='{{ VALID_BODY_WEBFILTER_CACHE[0] }}'"
            return (False, error_msg)
    if "sdns-options" in payload:
        value = payload["sdns-options"]
        if value not in VALID_BODY_SDNS_OPTIONS:
            desc = FIELD_DESCRIPTIONS.get("sdns-options", "")
            error_msg = f"Invalid value for 'sdns-options': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SDNS_OPTIONS)}"
            error_msg += f"\n  → Example: sdns-options='{{ VALID_BODY_SDNS_OPTIONS[0] }}'"
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


def validate_system_fortiguard_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/fortiguard.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_fortiguard_put(payload)
    """
    # Step 1: Validate enum values
    if "fortiguard-anycast" in payload:
        value = payload["fortiguard-anycast"]
        if value not in VALID_BODY_FORTIGUARD_ANYCAST:
            return (
                False,
                f"Invalid value for 'fortiguard-anycast'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTIGUARD_ANYCAST)}",
            )
    if "fortiguard-anycast-source" in payload:
        value = payload["fortiguard-anycast-source"]
        if value not in VALID_BODY_FORTIGUARD_ANYCAST_SOURCE:
            return (
                False,
                f"Invalid value for 'fortiguard-anycast-source'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTIGUARD_ANYCAST_SOURCE)}",
            )
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid value for 'protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )
    if "port" in payload:
        value = payload["port"]
        if value not in VALID_BODY_PORT:
            return (
                False,
                f"Invalid value for 'port'='{value}'. Must be one of: {', '.join(VALID_BODY_PORT)}",
            )
    if "auto-join-forticloud" in payload:
        value = payload["auto-join-forticloud"]
        if value not in VALID_BODY_AUTO_JOIN_FORTICLOUD:
            return (
                False,
                f"Invalid value for 'auto-join-forticloud'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_JOIN_FORTICLOUD)}",
            )
    if "update-server-location" in payload:
        value = payload["update-server-location"]
        if value not in VALID_BODY_UPDATE_SERVER_LOCATION:
            return (
                False,
                f"Invalid value for 'update-server-location'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_SERVER_LOCATION)}",
            )
    if "sandbox-inline-scan" in payload:
        value = payload["sandbox-inline-scan"]
        if value not in VALID_BODY_SANDBOX_INLINE_SCAN:
            return (
                False,
                f"Invalid value for 'sandbox-inline-scan'='{value}'. Must be one of: {', '.join(VALID_BODY_SANDBOX_INLINE_SCAN)}",
            )
    if "update-ffdb" in payload:
        value = payload["update-ffdb"]
        if value not in VALID_BODY_UPDATE_FFDB:
            return (
                False,
                f"Invalid value for 'update-ffdb'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_FFDB)}",
            )
    if "update-uwdb" in payload:
        value = payload["update-uwdb"]
        if value not in VALID_BODY_UPDATE_UWDB:
            return (
                False,
                f"Invalid value for 'update-uwdb'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_UWDB)}",
            )
    if "update-dldb" in payload:
        value = payload["update-dldb"]
        if value not in VALID_BODY_UPDATE_DLDB:
            return (
                False,
                f"Invalid value for 'update-dldb'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_DLDB)}",
            )
    if "update-extdb" in payload:
        value = payload["update-extdb"]
        if value not in VALID_BODY_UPDATE_EXTDB:
            return (
                False,
                f"Invalid value for 'update-extdb'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_EXTDB)}",
            )
    if "update-build-proxy" in payload:
        value = payload["update-build-proxy"]
        if value not in VALID_BODY_UPDATE_BUILD_PROXY:
            return (
                False,
                f"Invalid value for 'update-build-proxy'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_BUILD_PROXY)}",
            )
    if "persistent-connection" in payload:
        value = payload["persistent-connection"]
        if value not in VALID_BODY_PERSISTENT_CONNECTION:
            return (
                False,
                f"Invalid value for 'persistent-connection'='{value}'. Must be one of: {', '.join(VALID_BODY_PERSISTENT_CONNECTION)}",
            )
    if "auto-firmware-upgrade" in payload:
        value = payload["auto-firmware-upgrade"]
        if value not in VALID_BODY_AUTO_FIRMWARE_UPGRADE:
            return (
                False,
                f"Invalid value for 'auto-firmware-upgrade'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_FIRMWARE_UPGRADE)}",
            )
    if "auto-firmware-upgrade-day" in payload:
        value = payload["auto-firmware-upgrade-day"]
        if value not in VALID_BODY_AUTO_FIRMWARE_UPGRADE_DAY:
            return (
                False,
                f"Invalid value for 'auto-firmware-upgrade-day'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_FIRMWARE_UPGRADE_DAY)}",
            )
    if "subscribe-update-notification" in payload:
        value = payload["subscribe-update-notification"]
        if value not in VALID_BODY_SUBSCRIBE_UPDATE_NOTIFICATION:
            return (
                False,
                f"Invalid value for 'subscribe-update-notification'='{value}'. Must be one of: {', '.join(VALID_BODY_SUBSCRIBE_UPDATE_NOTIFICATION)}",
            )
    if "antispam-force-off" in payload:
        value = payload["antispam-force-off"]
        if value not in VALID_BODY_ANTISPAM_FORCE_OFF:
            return (
                False,
                f"Invalid value for 'antispam-force-off'='{value}'. Must be one of: {', '.join(VALID_BODY_ANTISPAM_FORCE_OFF)}",
            )
    if "antispam-cache" in payload:
        value = payload["antispam-cache"]
        if value not in VALID_BODY_ANTISPAM_CACHE:
            return (
                False,
                f"Invalid value for 'antispam-cache'='{value}'. Must be one of: {', '.join(VALID_BODY_ANTISPAM_CACHE)}",
            )
    if "outbreak-prevention-force-off" in payload:
        value = payload["outbreak-prevention-force-off"]
        if value not in VALID_BODY_OUTBREAK_PREVENTION_FORCE_OFF:
            return (
                False,
                f"Invalid value for 'outbreak-prevention-force-off'='{value}'. Must be one of: {', '.join(VALID_BODY_OUTBREAK_PREVENTION_FORCE_OFF)}",
            )
    if "outbreak-prevention-cache" in payload:
        value = payload["outbreak-prevention-cache"]
        if value not in VALID_BODY_OUTBREAK_PREVENTION_CACHE:
            return (
                False,
                f"Invalid value for 'outbreak-prevention-cache'='{value}'. Must be one of: {', '.join(VALID_BODY_OUTBREAK_PREVENTION_CACHE)}",
            )
    if "webfilter-force-off" in payload:
        value = payload["webfilter-force-off"]
        if value not in VALID_BODY_WEBFILTER_FORCE_OFF:
            return (
                False,
                f"Invalid value for 'webfilter-force-off'='{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_FORCE_OFF)}",
            )
    if "webfilter-cache" in payload:
        value = payload["webfilter-cache"]
        if value not in VALID_BODY_WEBFILTER_CACHE:
            return (
                False,
                f"Invalid value for 'webfilter-cache'='{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_CACHE)}",
            )
    if "sdns-options" in payload:
        value = payload["sdns-options"]
        if value not in VALID_BODY_SDNS_OPTIONS:
            return (
                False,
                f"Invalid value for 'sdns-options'='{value}'. Must be one of: {', '.join(VALID_BODY_SDNS_OPTIONS)}",
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
    "endpoint": "system/fortiguard",
    "category": "cmdb",
    "api_path": "system/fortiguard",
    "help": "Configure FortiGuard services.",
    "total_fields": 60,
    "required_fields_count": 1,
    "fields_with_defaults_count": 59,
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
