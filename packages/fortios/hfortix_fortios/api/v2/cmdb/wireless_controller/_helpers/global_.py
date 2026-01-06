"""
Validation helpers for wireless_controller/global_ endpoint.

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
    "location": "",
    "acd-process-count": 0,
    "wpad-process-count": 0,
    "image-download": "enable",
    "rolling-wtp-upgrade": "disable",
    "rolling-wtp-upgrade-threshold": "-80",
    "max-retransmit": 3,
    "control-message-offload": "ebp-frame aeroscout-tag ap-list sta-list sta-cap-list stats aeroscout-mu sta-health spectral-analysis",
    "data-ethernet-II": "enable",
    "link-aggregation": "disable",
    "mesh-eth-type": 8755,
    "fiapp-eth-type": 5252,
    "discovery-mc-addr": "224.0.1.140",
    "discovery-mc-addr6": "ff02::18c",
    "max-clients": 0,
    "rogue-scan-mac-adjacency": 7,
    "ipsec-base-ip": "169.254.0.1",
    "wtp-share": "disable",
    "tunnel-mode": "compatible",
    "nac-interval": 120,
    "ap-log-server": "disable",
    "ap-log-server-ip": "0.0.0.0",
    "ap-log-server-port": 0,
    "max-sta-offline": 0,
    "max-sta-offline-ip2mac": 0,
    "max-sta-cap": 0,
    "max-sta-cap-wtp": 8,
    "max-rogue-ap": 0,
    "max-rogue-ap-wtp": 16,
    "max-rogue-sta": 0,
    "max-wids-entry": 0,
    "max-ble-device": 0,
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
    "name": "string",  # Name of the wireless controller.
    "location": "string",  # Description of the location of the wireless controller.
    "acd-process-count": "integer",  # Configure the number cw_acd daemons for multi-core CPU suppo
    "wpad-process-count": "integer",  # Wpad daemon process count for multi-core CPU support.
    "image-download": "option",  # Enable/disable WTP image download at join time.
    "rolling-wtp-upgrade": "option",  # Enable/disable rolling WTP upgrade (default = disable).
    "rolling-wtp-upgrade-threshold": "string",  # Minimum signal level/threshold in dBm required for the manag
    "max-retransmit": "integer",  # Maximum number of tunnel packet retransmissions (0 - 64, def
    "control-message-offload": "option",  # Configure CAPWAP control message data channel offload.
    "data-ethernet-II": "option",  # Configure the wireless controller to use Ethernet II or 802.
    "link-aggregation": "option",  # Enable/disable calculating the CAPWAP transmit hash to load 
    "mesh-eth-type": "integer",  # Mesh Ethernet identifier included in backhaul packets (0 - 6
    "fiapp-eth-type": "integer",  # Ethernet type for Fortinet Inter-Access Point Protocol (IAPP
    "discovery-mc-addr": "ipv4-address-multicast",  # Multicast IP address for AP discovery (default = 244.0.1.140
    "discovery-mc-addr6": "ipv6-address",  # Multicast IPv6 address for AP discovery (default = FF02::18C
    "max-clients": "integer",  # Maximum number of clients that can connect simultaneously (d
    "rogue-scan-mac-adjacency": "integer",  # Maximum numerical difference between an AP's Ethernet and wi
    "ipsec-base-ip": "ipv4-address",  # Base IP address for IPsec VPN tunnels between the access poi
    "wtp-share": "option",  # Enable/disable sharing of WTPs between VDOMs.
    "tunnel-mode": "option",  # Compatible/strict tunnel mode.
    "nac-interval": "integer",  # Interval in seconds between two WiFi network access control 
    "ap-log-server": "option",  # Enable/disable configuring FortiGate to redirect wireless ev
    "ap-log-server-ip": "ipv4-address",  # IP address that FortiGate or FortiAPs send log messages to.
    "ap-log-server-port": "integer",  # Port that FortiGate or FortiAPs send log messages to.
    "max-sta-offline": "integer",  # Maximum number of station offline stored on the controller (
    "max-sta-offline-ip2mac": "integer",  # Maximum number of station offline ip2mac stored on the contr
    "max-sta-cap": "integer",  # Maximum number of station cap stored on the controller (defa
    "max-sta-cap-wtp": "integer",  # Maximum number of station cap's wtp info stored on the contr
    "max-rogue-ap": "integer",  # Maximum number of rogue APs stored on the controller (defaul
    "max-rogue-ap-wtp": "integer",  # Maximum number of rogue AP's wtp info stored on the controll
    "max-rogue-sta": "integer",  # Maximum number of rogue stations stored on the controller (d
    "max-wids-entry": "integer",  # Maximum number of wids entries stored on the controller (def
    "max-ble-device": "integer",  # Maximum number of BLE devices stored on the controller (defa
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Name of the wireless controller.",
    "location": "Description of the location of the wireless controller.",
    "acd-process-count": "Configure the number cw_acd daemons for multi-core CPU support (default = 0).",
    "wpad-process-count": "Wpad daemon process count for multi-core CPU support.",
    "image-download": "Enable/disable WTP image download at join time.",
    "rolling-wtp-upgrade": "Enable/disable rolling WTP upgrade (default = disable).",
    "rolling-wtp-upgrade-threshold": "Minimum signal level/threshold in dBm required for the managed WTP to be included in rolling WTP upgrade (-95 to -20, default = -80).",
    "max-retransmit": "Maximum number of tunnel packet retransmissions (0 - 64, default = 3).",
    "control-message-offload": "Configure CAPWAP control message data channel offload.",
    "data-ethernet-II": "Configure the wireless controller to use Ethernet II or 802.3 frames with 802.3 data tunnel mode (default = enable).",
    "link-aggregation": "Enable/disable calculating the CAPWAP transmit hash to load balance sessions to link aggregation nodes (default = disable).",
    "mesh-eth-type": "Mesh Ethernet identifier included in backhaul packets (0 - 65535, default = 8755).",
    "fiapp-eth-type": "Ethernet type for Fortinet Inter-Access Point Protocol (IAPP), or IEEE 802.11f, packets (0 - 65535, default = 5252).",
    "discovery-mc-addr": "Multicast IP address for AP discovery (default = 244.0.1.140).",
    "discovery-mc-addr6": "Multicast IPv6 address for AP discovery (default = FF02::18C).",
    "max-clients": "Maximum number of clients that can connect simultaneously (default = 0, meaning no limitation).",
    "rogue-scan-mac-adjacency": "Maximum numerical difference between an AP's Ethernet and wireless MAC values to match for rogue detection (0 - 31, default = 7).",
    "ipsec-base-ip": "Base IP address for IPsec VPN tunnels between the access points and the wireless controller (default = 169.254.0.1).",
    "wtp-share": "Enable/disable sharing of WTPs between VDOMs.",
    "tunnel-mode": "Compatible/strict tunnel mode.",
    "nac-interval": "Interval in seconds between two WiFi network access control (NAC) checks (10 - 600, default = 120).",
    "ap-log-server": "Enable/disable configuring FortiGate to redirect wireless event log messages or FortiAPs to send UTM log messages to a syslog server (default = disable).",
    "ap-log-server-ip": "IP address that FortiGate or FortiAPs send log messages to.",
    "ap-log-server-port": "Port that FortiGate or FortiAPs send log messages to.",
    "max-sta-offline": "Maximum number of station offline stored on the controller (default = 0).",
    "max-sta-offline-ip2mac": "Maximum number of station offline ip2mac stored on the controller (default = 0).",
    "max-sta-cap": "Maximum number of station cap stored on the controller (default = 0).",
    "max-sta-cap-wtp": "Maximum number of station cap's wtp info stored on the controller (1 - 16, default = 8).",
    "max-rogue-ap": "Maximum number of rogue APs stored on the controller (default = 0).",
    "max-rogue-ap-wtp": "Maximum number of rogue AP's wtp info stored on the controller (1 - 16, default = 16).",
    "max-rogue-sta": "Maximum number of rogue stations stored on the controller (default = 0).",
    "max-wids-entry": "Maximum number of wids entries stored on the controller (default = 0).",
    "max-ble-device": "Maximum number of BLE devices stored on the controller (default = 0).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "location": {"type": "string", "max_length": 35},
    "acd-process-count": {"type": "integer", "min": 0, "max": 255},
    "wpad-process-count": {"type": "integer", "min": 0, "max": 255},
    "rolling-wtp-upgrade-threshold": {"type": "string", "max_length": 7},
    "max-retransmit": {"type": "integer", "min": 0, "max": 64},
    "mesh-eth-type": {"type": "integer", "min": 0, "max": 65535},
    "fiapp-eth-type": {"type": "integer", "min": 0, "max": 65535},
    "max-clients": {"type": "integer", "min": 0, "max": 4294967295},
    "rogue-scan-mac-adjacency": {"type": "integer", "min": 0, "max": 31},
    "nac-interval": {"type": "integer", "min": 10, "max": 600},
    "ap-log-server-port": {"type": "integer", "min": 0, "max": 65535},
    "max-sta-offline": {"type": "integer", "min": 0, "max": 4294967295},
    "max-sta-offline-ip2mac": {"type": "integer", "min": 0, "max": 4294967295},
    "max-sta-cap": {"type": "integer", "min": 0, "max": 4294967295},
    "max-sta-cap-wtp": {"type": "integer", "min": 1, "max": 8},
    "max-rogue-ap": {"type": "integer", "min": 0, "max": 4294967295},
    "max-rogue-ap-wtp": {"type": "integer", "min": 1, "max": 16},
    "max-rogue-sta": {"type": "integer", "min": 0, "max": 4294967295},
    "max-wids-entry": {"type": "integer", "min": 0, "max": 4294967295},
    "max-ble-device": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_IMAGE_DOWNLOAD = [
    "enable",  # Enable WTP image download at join time.
    "disable",  # Disable WTP image download at join time.
]
VALID_BODY_ROLLING_WTP_UPGRADE = [
    "enable",  # Enable rolling WTP upgrade.
    "disable",  # Disable rolling WTP upgrade.
]
VALID_BODY_CONTROL_MESSAGE_OFFLOAD = [
    "ebp-frame",  # Ekahau blink protocol (EBP) frames.
    "aeroscout-tag",  # AeroScout tag.
    "ap-list",  # Rogue AP list.
    "sta-list",  # Rogue STA list.
    "sta-cap-list",  # STA capability list.
    "stats",  # WTP, radio, VAP, and STA statistics.
    "aeroscout-mu",  # AeroScout Mobile Unit (MU) report.
    "sta-health",  # STA health log.
    "spectral-analysis",  # Spectral analysis report.
]
VALID_BODY_DATA_ETHERNET_II = [
    "enable",  # Use Ethernet II frames with 802.3 data tunnel mode.
    "disable",  # Use 802.3 Ethernet frames with 802.3 data tunnel mode.
]
VALID_BODY_LINK_AGGREGATION = [
    "enable",  # Enable calculating the CAPWAP transmit hash.
    "disable",  # Disable calculating the CAPWAP transmit hash.
]
VALID_BODY_WTP_SHARE = [
    "enable",  # WTP can be shared between all VDOMs.
    "disable",  # WTP can be used only in its own VDOM.
]
VALID_BODY_TUNNEL_MODE = [
    "compatible",  # Allow for backward compatible ciphers(3DES+SHA1+Strong list).
    "strict",  # Follow system level strong-crypto ciphers.
]
VALID_BODY_AP_LOG_SERVER = [
    "enable",  # Enable AP log server.
    "disable",  # Disable AP log server.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_global__get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for wireless_controller/global_.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_wireless_controller_global__get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_wireless_controller_global__get(
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
    Validate required fields for wireless_controller/global_.

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


def validate_wireless_controller_global__post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new wireless_controller/global_ object.

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
        >>> is_valid, error = validate_wireless_controller_global__post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "image-download": "{'name': 'enable', 'help': 'Enable WTP image download at join time.', 'label': 'Enable', 'description': 'Enable WTP image download at join time'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_wireless_controller_global__post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["image-download"] = "invalid-value"
        >>> is_valid, error = validate_wireless_controller_global__post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_wireless_controller_global__post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "image-download" in payload:
        value = payload["image-download"]
        if value not in VALID_BODY_IMAGE_DOWNLOAD:
            desc = FIELD_DESCRIPTIONS.get("image-download", "")
            error_msg = f"Invalid value for 'image-download': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IMAGE_DOWNLOAD)}"
            error_msg += f"\n  → Example: image-download='{{ VALID_BODY_IMAGE_DOWNLOAD[0] }}'"
            return (False, error_msg)
    if "rolling-wtp-upgrade" in payload:
        value = payload["rolling-wtp-upgrade"]
        if value not in VALID_BODY_ROLLING_WTP_UPGRADE:
            desc = FIELD_DESCRIPTIONS.get("rolling-wtp-upgrade", "")
            error_msg = f"Invalid value for 'rolling-wtp-upgrade': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROLLING_WTP_UPGRADE)}"
            error_msg += f"\n  → Example: rolling-wtp-upgrade='{{ VALID_BODY_ROLLING_WTP_UPGRADE[0] }}'"
            return (False, error_msg)
    if "control-message-offload" in payload:
        value = payload["control-message-offload"]
        if value not in VALID_BODY_CONTROL_MESSAGE_OFFLOAD:
            desc = FIELD_DESCRIPTIONS.get("control-message-offload", "")
            error_msg = f"Invalid value for 'control-message-offload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CONTROL_MESSAGE_OFFLOAD)}"
            error_msg += f"\n  → Example: control-message-offload='{{ VALID_BODY_CONTROL_MESSAGE_OFFLOAD[0] }}'"
            return (False, error_msg)
    if "data-ethernet-II" in payload:
        value = payload["data-ethernet-II"]
        if value not in VALID_BODY_DATA_ETHERNET_II:
            desc = FIELD_DESCRIPTIONS.get("data-ethernet-II", "")
            error_msg = f"Invalid value for 'data-ethernet-II': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DATA_ETHERNET_II)}"
            error_msg += f"\n  → Example: data-ethernet-II='{{ VALID_BODY_DATA_ETHERNET_II[0] }}'"
            return (False, error_msg)
    if "link-aggregation" in payload:
        value = payload["link-aggregation"]
        if value not in VALID_BODY_LINK_AGGREGATION:
            desc = FIELD_DESCRIPTIONS.get("link-aggregation", "")
            error_msg = f"Invalid value for 'link-aggregation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LINK_AGGREGATION)}"
            error_msg += f"\n  → Example: link-aggregation='{{ VALID_BODY_LINK_AGGREGATION[0] }}'"
            return (False, error_msg)
    if "wtp-share" in payload:
        value = payload["wtp-share"]
        if value not in VALID_BODY_WTP_SHARE:
            desc = FIELD_DESCRIPTIONS.get("wtp-share", "")
            error_msg = f"Invalid value for 'wtp-share': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WTP_SHARE)}"
            error_msg += f"\n  → Example: wtp-share='{{ VALID_BODY_WTP_SHARE[0] }}'"
            return (False, error_msg)
    if "tunnel-mode" in payload:
        value = payload["tunnel-mode"]
        if value not in VALID_BODY_TUNNEL_MODE:
            desc = FIELD_DESCRIPTIONS.get("tunnel-mode", "")
            error_msg = f"Invalid value for 'tunnel-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TUNNEL_MODE)}"
            error_msg += f"\n  → Example: tunnel-mode='{{ VALID_BODY_TUNNEL_MODE[0] }}'"
            return (False, error_msg)
    if "ap-log-server" in payload:
        value = payload["ap-log-server"]
        if value not in VALID_BODY_AP_LOG_SERVER:
            desc = FIELD_DESCRIPTIONS.get("ap-log-server", "")
            error_msg = f"Invalid value for 'ap-log-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AP_LOG_SERVER)}"
            error_msg += f"\n  → Example: ap-log-server='{{ VALID_BODY_AP_LOG_SERVER[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_global__put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update wireless_controller/global_.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_wireless_controller_global__put(payload)
    """
    # Step 1: Validate enum values
    if "image-download" in payload:
        value = payload["image-download"]
        if value not in VALID_BODY_IMAGE_DOWNLOAD:
            return (
                False,
                f"Invalid value for 'image-download'='{value}'. Must be one of: {', '.join(VALID_BODY_IMAGE_DOWNLOAD)}",
            )
    if "rolling-wtp-upgrade" in payload:
        value = payload["rolling-wtp-upgrade"]
        if value not in VALID_BODY_ROLLING_WTP_UPGRADE:
            return (
                False,
                f"Invalid value for 'rolling-wtp-upgrade'='{value}'. Must be one of: {', '.join(VALID_BODY_ROLLING_WTP_UPGRADE)}",
            )
    if "control-message-offload" in payload:
        value = payload["control-message-offload"]
        if value not in VALID_BODY_CONTROL_MESSAGE_OFFLOAD:
            return (
                False,
                f"Invalid value for 'control-message-offload'='{value}'. Must be one of: {', '.join(VALID_BODY_CONTROL_MESSAGE_OFFLOAD)}",
            )
    if "data-ethernet-II" in payload:
        value = payload["data-ethernet-II"]
        if value not in VALID_BODY_DATA_ETHERNET_II:
            return (
                False,
                f"Invalid value for 'data-ethernet-II'='{value}'. Must be one of: {', '.join(VALID_BODY_DATA_ETHERNET_II)}",
            )
    if "link-aggregation" in payload:
        value = payload["link-aggregation"]
        if value not in VALID_BODY_LINK_AGGREGATION:
            return (
                False,
                f"Invalid value for 'link-aggregation'='{value}'. Must be one of: {', '.join(VALID_BODY_LINK_AGGREGATION)}",
            )
    if "wtp-share" in payload:
        value = payload["wtp-share"]
        if value not in VALID_BODY_WTP_SHARE:
            return (
                False,
                f"Invalid value for 'wtp-share'='{value}'. Must be one of: {', '.join(VALID_BODY_WTP_SHARE)}",
            )
    if "tunnel-mode" in payload:
        value = payload["tunnel-mode"]
        if value not in VALID_BODY_TUNNEL_MODE:
            return (
                False,
                f"Invalid value for 'tunnel-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_TUNNEL_MODE)}",
            )
    if "ap-log-server" in payload:
        value = payload["ap-log-server"]
        if value not in VALID_BODY_AP_LOG_SERVER:
            return (
                False,
                f"Invalid value for 'ap-log-server'='{value}'. Must be one of: {', '.join(VALID_BODY_AP_LOG_SERVER)}",
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
    "endpoint": "wireless_controller/global_",
    "category": "cmdb",
    "api_path": "wireless-controller/global",
    "help": "Configure wireless controller global settings.",
    "total_fields": 33,
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
