"""
Validation helpers for system/central_management endpoint.

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
    "mode": "normal",
    "type": "fortiguard",
    "fortigate-cloud-sso-default-profile": "",
    "schedule-config-restore": "enable",
    "schedule-script-restore": "enable",
    "allow-push-configuration": "enable",
    "allow-push-firmware": "enable",
    "allow-remote-firmware-upgrade": "enable",
    "allow-monitor": "enable",
    "serial-number": "",
    "fmg": "",
    "fmg-source-ip": "0.0.0.0",
    "fmg-source-ip6": "::",
    "local-cert": "",
    "ca-cert": "",
    "vdom": "root",
    "fmg-update-port": "8890",
    "fmg-update-http-header": "disable",
    "include-default-servers": "enable",
    "enc-algorithm": "high",
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
    "mode": "option",  # Central management mode.
    "type": "option",  # Central management type.
    "fortigate-cloud-sso-default-profile": "string",  # Override access profile. Permission is set to read-only with
    "schedule-config-restore": "option",  # Enable/disable allowing the central management server to res
    "schedule-script-restore": "option",  # Enable/disable allowing the central management server to res
    "allow-push-configuration": "option",  # Enable/disable allowing the central management server to pus
    "allow-push-firmware": "option",  # Enable/disable allowing the central management server to pus
    "allow-remote-firmware-upgrade": "option",  # Enable/disable remotely upgrading the firmware on this Forti
    "allow-monitor": "option",  # Enable/disable allowing the central management server to rem
    "serial-number": "user",  # Serial number.
    "fmg": "user",  # IP address or FQDN of the FortiManager.
    "fmg-source-ip": "ipv4-address",  # IPv4 source address that this FortiGate uses when communicat
    "fmg-source-ip6": "ipv6-address",  # IPv6 source address that this FortiGate uses when communicat
    "local-cert": "string",  # Certificate to be used by FGFM protocol.
    "ca-cert": "user",  # CA certificate to be used by FGFM protocol.
    "vdom": "string",  # Virtual domain (VDOM) name to use when communicating with Fo
    "server-list": "string",  # Additional severs that the FortiGate can use for updates (fo
    "fmg-update-port": "option",  # Port used to communicate with FortiManager that is acting as
    "fmg-update-http-header": "option",  # Enable/disable inclusion of HTTP header in update request.
    "include-default-servers": "option",  # Enable/disable inclusion of public FortiGuard servers in the
    "enc-algorithm": "option",  # Encryption strength for communications between the FortiGate
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "mode": "Central management mode.",
    "type": "Central management type.",
    "fortigate-cloud-sso-default-profile": "Override access profile. Permission is set to read-only without a FortiGate Cloud Central Management license.",
    "schedule-config-restore": "Enable/disable allowing the central management server to restore the configuration of this FortiGate.",
    "schedule-script-restore": "Enable/disable allowing the central management server to restore the scripts stored on this FortiGate.",
    "allow-push-configuration": "Enable/disable allowing the central management server to push configuration changes to this FortiGate.",
    "allow-push-firmware": "Enable/disable allowing the central management server to push firmware updates to this FortiGate.",
    "allow-remote-firmware-upgrade": "Enable/disable remotely upgrading the firmware on this FortiGate from the central management server.",
    "allow-monitor": "Enable/disable allowing the central management server to remotely monitor this FortiGate unit.",
    "serial-number": "Serial number.",
    "fmg": "IP address or FQDN of the FortiManager.",
    "fmg-source-ip": "IPv4 source address that this FortiGate uses when communicating with FortiManager.",
    "fmg-source-ip6": "IPv6 source address that this FortiGate uses when communicating with FortiManager.",
    "local-cert": "Certificate to be used by FGFM protocol.",
    "ca-cert": "CA certificate to be used by FGFM protocol.",
    "vdom": "Virtual domain (VDOM) name to use when communicating with FortiManager.",
    "server-list": "Additional severs that the FortiGate can use for updates (for AV, IPS, updates) and ratings (for web filter and antispam ratings) servers.",
    "fmg-update-port": "Port used to communicate with FortiManager that is acting as a FortiGuard update server.",
    "fmg-update-http-header": "Enable/disable inclusion of HTTP header in update request.",
    "include-default-servers": "Enable/disable inclusion of public FortiGuard servers in the override server list.",
    "enc-algorithm": "Encryption strength for communications between the FortiGate and central management.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "fortigate-cloud-sso-default-profile": {"type": "string", "max_length": 35},
    "local-cert": {"type": "string", "max_length": 35},
    "vdom": {"type": "string", "max_length": 31},
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "server-list": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "server-type": {
            "type": "option",
            "help": "FortiGuard service type.",
            "required": True,
            "default": "",
            "options": [{"help": "AV, IPS, and AV-query update server.", "label": "Update", "name": "update"}, {"help": "Web filter and anti-spam rating server.", "label": "Rating", "name": "rating"}, {"help": "Virtual patch query server.", "label": "Vpatch Query", "name": "vpatch-query"}, {"help": "IoT device collection server.", "label": "Iot Collect", "name": "iot-collect"}],
        },
        "addr-type": {
            "type": "option",
            "help": "Indicate whether the FortiGate communicates with the override server using an IPv4 address, an IPv6 address or a FQDN.",
            "default": "ipv4",
            "options": [{"help": "IPv4 address.", "label": "Ipv4", "name": "ipv4"}, {"help": "IPv6 address.", "label": "Ipv6", "name": "ipv6"}, {"help": "FQDN.", "label": "Fqdn", "name": "fqdn"}],
        },
        "server-address": {
            "type": "ipv4-address",
            "help": "IPv4 address of override server.",
            "required": True,
            "default": "0.0.0.0",
        },
        "server-address6": {
            "type": "ipv6-address",
            "help": "IPv6 address of override server.",
            "required": True,
            "default": "::",
        },
        "fqdn": {
            "type": "string",
            "help": "FQDN address of override server.",
            "required": True,
            "default": "",
            "max_length": 255,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_MODE = [
    "normal",  # Manage and configure this FortiGate from FortiManager.
    "backup",  # Manage and configure this FortiGate locally and back up its configuration to FortiManager.
]
VALID_BODY_TYPE = [
    "fortimanager",  # FortiManager.
    "fortiguard",  # Central management of this FortiGate using FortiCloud.
    "none",  # No central management.
]
VALID_BODY_SCHEDULE_CONFIG_RESTORE = [
    "enable",  # Enable scheduled configuration restore.
    "disable",  # Disable scheduled configuration restore.
]
VALID_BODY_SCHEDULE_SCRIPT_RESTORE = [
    "enable",  # Enable scheduled script restore.
    "disable",  # Disable scheduled script restore.
]
VALID_BODY_ALLOW_PUSH_CONFIGURATION = [
    "enable",  # Enable push configuration.
    "disable",  # Disable push configuration.
]
VALID_BODY_ALLOW_PUSH_FIRMWARE = [
    "enable",  # Enable push firmware.
    "disable",  # Disable push firmware.
]
VALID_BODY_ALLOW_REMOTE_FIRMWARE_UPGRADE = [
    "enable",  # Enable remote firmware upgrade.
    "disable",  # Disable remote firmware upgrade.
]
VALID_BODY_ALLOW_MONITOR = [
    "enable",  # Enable remote monitoring of device.
    "disable",  # Disable remote monitoring of device.
]
VALID_BODY_FMG_UPDATE_PORT = [
    "8890",  # Use port 8890 to communicate with FortiManager that is acting as a FortiGuard update server.
    "443",  # Use port 443 to communicate with FortiManager that is acting as a FortiGuard update server.
]
VALID_BODY_FMG_UPDATE_HTTP_HEADER = [
    "enable",  # Enable inclusion of HTTP header in update request.
    "disable",  # Disable inclusion of HTTP header in update request.
]
VALID_BODY_INCLUDE_DEFAULT_SERVERS = [
    "enable",  # Enable inclusion of public FortiGuard servers in the override server list.
    "disable",  # Disable inclusion of public FortiGuard servers in the override server list.
]
VALID_BODY_ENC_ALGORITHM = [
    "default",  # High strength algorithms and medium-strength 128-bit key length algorithms.
    "high",  # 128-bit and larger key length algorithms.
    "low",  # 64-bit or 56-bit key length algorithms without export restrictions.
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


def validate_system_central_management_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/central_management.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_central_management_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_central_management_get(
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
    Validate required fields for system/central_management.

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


def validate_system_central_management_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/central_management object.

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
        >>> is_valid, error = validate_system_central_management_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "interface": True,
        ...     "mode": "{'name': 'normal', 'help': 'Manage and configure this FortiGate from FortiManager.', 'label': 'Normal', 'description': 'Manage and configure this FortiGate from FortiManager'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_central_management_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["mode"] = "invalid-value"
        >>> is_valid, error = validate_system_central_management_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_central_management_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            desc = FIELD_DESCRIPTIONS.get("mode", "")
            error_msg = f"Invalid value for 'mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MODE)}"
            error_msg += f"\n  → Example: mode='{{ VALID_BODY_MODE[0] }}'"
            return (False, error_msg)
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
    if "schedule-config-restore" in payload:
        value = payload["schedule-config-restore"]
        if value not in VALID_BODY_SCHEDULE_CONFIG_RESTORE:
            desc = FIELD_DESCRIPTIONS.get("schedule-config-restore", "")
            error_msg = f"Invalid value for 'schedule-config-restore': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCHEDULE_CONFIG_RESTORE)}"
            error_msg += f"\n  → Example: schedule-config-restore='{{ VALID_BODY_SCHEDULE_CONFIG_RESTORE[0] }}'"
            return (False, error_msg)
    if "schedule-script-restore" in payload:
        value = payload["schedule-script-restore"]
        if value not in VALID_BODY_SCHEDULE_SCRIPT_RESTORE:
            desc = FIELD_DESCRIPTIONS.get("schedule-script-restore", "")
            error_msg = f"Invalid value for 'schedule-script-restore': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCHEDULE_SCRIPT_RESTORE)}"
            error_msg += f"\n  → Example: schedule-script-restore='{{ VALID_BODY_SCHEDULE_SCRIPT_RESTORE[0] }}'"
            return (False, error_msg)
    if "allow-push-configuration" in payload:
        value = payload["allow-push-configuration"]
        if value not in VALID_BODY_ALLOW_PUSH_CONFIGURATION:
            desc = FIELD_DESCRIPTIONS.get("allow-push-configuration", "")
            error_msg = f"Invalid value for 'allow-push-configuration': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_PUSH_CONFIGURATION)}"
            error_msg += f"\n  → Example: allow-push-configuration='{{ VALID_BODY_ALLOW_PUSH_CONFIGURATION[0] }}'"
            return (False, error_msg)
    if "allow-push-firmware" in payload:
        value = payload["allow-push-firmware"]
        if value not in VALID_BODY_ALLOW_PUSH_FIRMWARE:
            desc = FIELD_DESCRIPTIONS.get("allow-push-firmware", "")
            error_msg = f"Invalid value for 'allow-push-firmware': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_PUSH_FIRMWARE)}"
            error_msg += f"\n  → Example: allow-push-firmware='{{ VALID_BODY_ALLOW_PUSH_FIRMWARE[0] }}'"
            return (False, error_msg)
    if "allow-remote-firmware-upgrade" in payload:
        value = payload["allow-remote-firmware-upgrade"]
        if value not in VALID_BODY_ALLOW_REMOTE_FIRMWARE_UPGRADE:
            desc = FIELD_DESCRIPTIONS.get("allow-remote-firmware-upgrade", "")
            error_msg = f"Invalid value for 'allow-remote-firmware-upgrade': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_REMOTE_FIRMWARE_UPGRADE)}"
            error_msg += f"\n  → Example: allow-remote-firmware-upgrade='{{ VALID_BODY_ALLOW_REMOTE_FIRMWARE_UPGRADE[0] }}'"
            return (False, error_msg)
    if "allow-monitor" in payload:
        value = payload["allow-monitor"]
        if value not in VALID_BODY_ALLOW_MONITOR:
            desc = FIELD_DESCRIPTIONS.get("allow-monitor", "")
            error_msg = f"Invalid value for 'allow-monitor': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_MONITOR)}"
            error_msg += f"\n  → Example: allow-monitor='{{ VALID_BODY_ALLOW_MONITOR[0] }}'"
            return (False, error_msg)
    if "fmg-update-port" in payload:
        value = payload["fmg-update-port"]
        if value not in VALID_BODY_FMG_UPDATE_PORT:
            desc = FIELD_DESCRIPTIONS.get("fmg-update-port", "")
            error_msg = f"Invalid value for 'fmg-update-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FMG_UPDATE_PORT)}"
            error_msg += f"\n  → Example: fmg-update-port='{{ VALID_BODY_FMG_UPDATE_PORT[0] }}'"
            return (False, error_msg)
    if "fmg-update-http-header" in payload:
        value = payload["fmg-update-http-header"]
        if value not in VALID_BODY_FMG_UPDATE_HTTP_HEADER:
            desc = FIELD_DESCRIPTIONS.get("fmg-update-http-header", "")
            error_msg = f"Invalid value for 'fmg-update-http-header': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FMG_UPDATE_HTTP_HEADER)}"
            error_msg += f"\n  → Example: fmg-update-http-header='{{ VALID_BODY_FMG_UPDATE_HTTP_HEADER[0] }}'"
            return (False, error_msg)
    if "include-default-servers" in payload:
        value = payload["include-default-servers"]
        if value not in VALID_BODY_INCLUDE_DEFAULT_SERVERS:
            desc = FIELD_DESCRIPTIONS.get("include-default-servers", "")
            error_msg = f"Invalid value for 'include-default-servers': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INCLUDE_DEFAULT_SERVERS)}"
            error_msg += f"\n  → Example: include-default-servers='{{ VALID_BODY_INCLUDE_DEFAULT_SERVERS[0] }}'"
            return (False, error_msg)
    if "enc-algorithm" in payload:
        value = payload["enc-algorithm"]
        if value not in VALID_BODY_ENC_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("enc-algorithm", "")
            error_msg = f"Invalid value for 'enc-algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENC_ALGORITHM)}"
            error_msg += f"\n  → Example: enc-algorithm='{{ VALID_BODY_ENC_ALGORITHM[0] }}'"
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


def validate_system_central_management_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/central_management.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_central_management_put(payload)
    """
    # Step 1: Validate enum values
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid value for 'mode'='{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "schedule-config-restore" in payload:
        value = payload["schedule-config-restore"]
        if value not in VALID_BODY_SCHEDULE_CONFIG_RESTORE:
            return (
                False,
                f"Invalid value for 'schedule-config-restore'='{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE_CONFIG_RESTORE)}",
            )
    if "schedule-script-restore" in payload:
        value = payload["schedule-script-restore"]
        if value not in VALID_BODY_SCHEDULE_SCRIPT_RESTORE:
            return (
                False,
                f"Invalid value for 'schedule-script-restore'='{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE_SCRIPT_RESTORE)}",
            )
    if "allow-push-configuration" in payload:
        value = payload["allow-push-configuration"]
        if value not in VALID_BODY_ALLOW_PUSH_CONFIGURATION:
            return (
                False,
                f"Invalid value for 'allow-push-configuration'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_PUSH_CONFIGURATION)}",
            )
    if "allow-push-firmware" in payload:
        value = payload["allow-push-firmware"]
        if value not in VALID_BODY_ALLOW_PUSH_FIRMWARE:
            return (
                False,
                f"Invalid value for 'allow-push-firmware'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_PUSH_FIRMWARE)}",
            )
    if "allow-remote-firmware-upgrade" in payload:
        value = payload["allow-remote-firmware-upgrade"]
        if value not in VALID_BODY_ALLOW_REMOTE_FIRMWARE_UPGRADE:
            return (
                False,
                f"Invalid value for 'allow-remote-firmware-upgrade'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_REMOTE_FIRMWARE_UPGRADE)}",
            )
    if "allow-monitor" in payload:
        value = payload["allow-monitor"]
        if value not in VALID_BODY_ALLOW_MONITOR:
            return (
                False,
                f"Invalid value for 'allow-monitor'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_MONITOR)}",
            )
    if "fmg-update-port" in payload:
        value = payload["fmg-update-port"]
        if value not in VALID_BODY_FMG_UPDATE_PORT:
            return (
                False,
                f"Invalid value for 'fmg-update-port'='{value}'. Must be one of: {', '.join(VALID_BODY_FMG_UPDATE_PORT)}",
            )
    if "fmg-update-http-header" in payload:
        value = payload["fmg-update-http-header"]
        if value not in VALID_BODY_FMG_UPDATE_HTTP_HEADER:
            return (
                False,
                f"Invalid value for 'fmg-update-http-header'='{value}'. Must be one of: {', '.join(VALID_BODY_FMG_UPDATE_HTTP_HEADER)}",
            )
    if "include-default-servers" in payload:
        value = payload["include-default-servers"]
        if value not in VALID_BODY_INCLUDE_DEFAULT_SERVERS:
            return (
                False,
                f"Invalid value for 'include-default-servers'='{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_DEFAULT_SERVERS)}",
            )
    if "enc-algorithm" in payload:
        value = payload["enc-algorithm"]
        if value not in VALID_BODY_ENC_ALGORITHM:
            return (
                False,
                f"Invalid value for 'enc-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_ENC_ALGORITHM)}",
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
    "endpoint": "system/central_management",
    "category": "cmdb",
    "api_path": "system/central-management",
    "help": "Configure central management.",
    "total_fields": 24,
    "required_fields_count": 1,
    "fields_with_defaults_count": 23,
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
