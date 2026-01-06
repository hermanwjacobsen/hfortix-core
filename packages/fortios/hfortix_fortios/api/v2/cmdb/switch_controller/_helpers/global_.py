"""Validation helpers for switch_controller/global_ - Auto-generated"""

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
    "mac-aging-interval": 300,
    "https-image-push": "enable",
    "vlan-all-mode": "defined",
    "vlan-optimization": "configured",
    "vlan-identity": "name",
    "mac-retention-period": 24,
    "default-virtual-switch-vlan": "",
    "dhcp-server-access-list": "disable",
    "dhcp-option82-format": "ascii",
    "dhcp-option82-circuit-id": "intfname vlan mode",
    "dhcp-option82-remote-id": "mac",
    "dhcp-snoop-client-req": "drop-untrusted",
    "dhcp-snoop-client-db-exp": 86400,
    "dhcp-snoop-db-per-port-learn-limit": 64,
    "log-mac-limit-violations": "disable",
    "mac-violation-timer": 0,
    "sn-dns-resolution": "enable",
    "mac-event-logging": "disable",
    "bounce-quarantined-link": "disable",
    "quarantine-mode": "by-vlan",
    "update-user-device": "mac-cache lldp dhcp-snooping l2-db l3-db",
    "fips-enforce": "enable",
    "firmware-provision-on-authorization": "disable",
    "switch-on-deauth": "no-op",
    "firewall-auth-user-hold-period": 5,
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
    "mac-aging-interval": "integer",  # Time after which an inactive MAC is aged out (10 - 1000000 s
    "https-image-push": "option",  # Enable/disable image push to FortiSwitch using HTTPS.
    "vlan-all-mode": "option",  # VLAN configuration mode, user-defined-vlans or all-possible-
    "vlan-optimization": "option",  # FortiLink VLAN optimization.
    "vlan-identity": "option",  # Identity of the VLAN. Commonly used for RADIUS Tunnel-Privat
    "disable-discovery": "string",  # Prevent this FortiSwitch from discovering.
    "mac-retention-period": "integer",  # Time in hours after which an inactive MAC is removed from cl
    "default-virtual-switch-vlan": "string",  # Default VLAN for ports when added to the virtual-switch.
    "dhcp-server-access-list": "option",  # Enable/disable DHCP snooping server access list.
    "dhcp-option82-format": "option",  # DHCP option-82 format string.
    "dhcp-option82-circuit-id": "option",  # List the parameters to be included to inform about client id
    "dhcp-option82-remote-id": "option",  # List the parameters to be included to inform about client id
    "dhcp-snoop-client-req": "option",  # Client DHCP packet broadcast mode.
    "dhcp-snoop-client-db-exp": "integer",  # Expiry time for DHCP snooping server database entries (300 -
    "dhcp-snoop-db-per-port-learn-limit": "integer",  # Per Interface dhcp-server entries learn limit (0 - 1024, def
    "log-mac-limit-violations": "option",  # Enable/disable logs for Learning Limit Violations.
    "mac-violation-timer": "integer",  # Set timeout for Learning Limit Violations (0 = disabled).
    "sn-dns-resolution": "option",  # Enable/disable DNS resolution of the FortiSwitch unit's IP a
    "mac-event-logging": "option",  # Enable/disable MAC address event logging.
    "bounce-quarantined-link": "option",  # Enable/disable bouncing (administratively bring the link dow
    "quarantine-mode": "option",  # Quarantine mode.
    "update-user-device": "option",  # Control which sources update the device user list.
    "custom-command": "string",  # List of custom commands to be pushed to all FortiSwitches in
    "fips-enforce": "option",  # Enable/disable enforcement of FIPS on managed FortiSwitch de
    "firmware-provision-on-authorization": "option",  # Enable/disable automatic provisioning of latest firmware on 
    "switch-on-deauth": "option",  # No-operation/Factory-reset the managed FortiSwitch on deauth
    "firewall-auth-user-hold-period": "integer",  # Time period in minutes to hold firewall authenticated MAC us
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "mac-aging-interval": "Time after which an inactive MAC is aged out (10 - 1000000 sec, default = 300, 0 = disable).",
    "https-image-push": "Enable/disable image push to FortiSwitch using HTTPS.",
    "vlan-all-mode": "VLAN configuration mode, user-defined-vlans or all-possible-vlans.",
    "vlan-optimization": "FortiLink VLAN optimization.",
    "vlan-identity": "Identity of the VLAN. Commonly used for RADIUS Tunnel-Private-Group-Id.",
    "disable-discovery": "Prevent this FortiSwitch from discovering.",
    "mac-retention-period": "Time in hours after which an inactive MAC is removed from client DB (0 = aged out based on mac-aging-interval).",
    "default-virtual-switch-vlan": "Default VLAN for ports when added to the virtual-switch.",
    "dhcp-server-access-list": "Enable/disable DHCP snooping server access list.",
    "dhcp-option82-format": "DHCP option-82 format string.",
    "dhcp-option82-circuit-id": "List the parameters to be included to inform about client identification.",
    "dhcp-option82-remote-id": "List the parameters to be included to inform about client identification.",
    "dhcp-snoop-client-req": "Client DHCP packet broadcast mode.",
    "dhcp-snoop-client-db-exp": "Expiry time for DHCP snooping server database entries (300 - 259200 sec, default = 86400 sec).",
    "dhcp-snoop-db-per-port-learn-limit": "Per Interface dhcp-server entries learn limit (0 - 1024, default = 64).",
    "log-mac-limit-violations": "Enable/disable logs for Learning Limit Violations.",
    "mac-violation-timer": "Set timeout for Learning Limit Violations (0 = disabled).",
    "sn-dns-resolution": "Enable/disable DNS resolution of the FortiSwitch unit's IP address with switch name.",
    "mac-event-logging": "Enable/disable MAC address event logging.",
    "bounce-quarantined-link": "Enable/disable bouncing (administratively bring the link down, up) of a switch port where a quarantined device was seen last. Helps to re-initiate the DHCP process for a device.",
    "quarantine-mode": "Quarantine mode.",
    "update-user-device": "Control which sources update the device user list.",
    "custom-command": "List of custom commands to be pushed to all FortiSwitches in the VDOM.",
    "fips-enforce": "Enable/disable enforcement of FIPS on managed FortiSwitch devices.",
    "firmware-provision-on-authorization": "Enable/disable automatic provisioning of latest firmware on authorization.",
    "switch-on-deauth": "No-operation/Factory-reset the managed FortiSwitch on deauthorization.",
    "firewall-auth-user-hold-period": "Time period in minutes to hold firewall authenticated MAC users (5 - 1440, default = 5, disable = 0).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "mac-aging-interval": {"type": "integer", "min": 10, "max": 1000000},
    "mac-retention-period": {"type": "integer", "min": 0, "max": 168},
    "default-virtual-switch-vlan": {"type": "string", "max_length": 15},
    "dhcp-snoop-client-db-exp": {"type": "integer", "min": 300, "max": 259200},
    "dhcp-snoop-db-per-port-learn-limit": {"type": "integer", "min": 0, "max": 2048},
    "mac-violation-timer": {"type": "integer", "min": 0, "max": 4294967295},
    "firewall-auth-user-hold-period": {"type": "integer", "min": 5, "max": 1440},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "disable-discovery": {
        "name": {
            "type": "string",
            "help": "FortiSwitch Serial-number.",
            "default": "",
            "max_length": 79,
        },
    },
    "custom-command": {
        "command-entry": {
            "type": "string",
            "help": "List of FortiSwitch commands.",
            "default": "",
            "max_length": 35,
        },
        "command-name": {
            "type": "string",
            "help": "Name of custom command to push to all FortiSwitches in VDOM.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_HTTPS_IMAGE_PUSH = [
    "enable",  # Enable image push to FortiSwitch using HTTPS.
    "disable",  # Disable image push to FortiSwitch using HTTPS.
]
VALID_BODY_VLAN_ALL_MODE = [
    "all",  # Include all possible VLANs (1-4093).
    "defined",  # Include user defined VLANs.
]
VALID_BODY_VLAN_OPTIMIZATION = [
    "prune",  # Enable VLAN optimization (only VLANs necessary on or along path between destinations) on FortiSwitch units for auto-generated trunks.
    "configured",  # Enable VLAN optimization (only VLANs created on Fortilink interface) on FortiSwitch units for auto-generated trunks.
    "none",  # Disable VLAN optimization on FortiSwitch units for auto-generated trunks.
]
VALID_BODY_VLAN_IDENTITY = [
    "description",  # Configure the VLAN description to that of the FortiOS interface description if available; otherwise use the interface name.
    "name",  # Configure the VLAN description to that of the FortiOS interface name.
]
VALID_BODY_DHCP_SERVER_ACCESS_LIST = [
    "enable",  # Enable DHCP server access list.
    "disable",  # Disable DHCP server access list.
]
VALID_BODY_DHCP_OPTION82_FORMAT = [
    "ascii",  # Allow user to choose values for circuit-id and remote-id. 	  Format:  cid= [hostname,interface,mode,vlan,description] rid=[hostname,xx:xx:xx:xx:xx:xx,ip] 
    "legacy",  # Generate predefine fixed format for circuit-id and remote. 	Format: cid=hostname-[<vlan:16><mod:8><port:8>].32bit, rid= [mac(0..6)].48bit 
]
VALID_BODY_DHCP_OPTION82_CIRCUIT_ID = [
    "intfname",  # Interface name.
    "vlan",  # VLAN name.
    "hostname",  # Hostname.
    "mode",  # Mode.
    "description",  # Description.
]
VALID_BODY_DHCP_OPTION82_REMOTE_ID = [
    "mac",  # MAC address.
    "hostname",  # Hostname.
    "ip",  # IP address.
]
VALID_BODY_DHCP_SNOOP_CLIENT_REQ = [
    "drop-untrusted",  # Broadcast packets on trusted ports in the VLAN.
    "forward-untrusted",  # Broadcast packets on all ports in the VLAN.
]
VALID_BODY_LOG_MAC_LIMIT_VIOLATIONS = [
    "enable",  # Enable Learn Limit Violation.
    "disable",  # Disable Learn Limit Violation.
]
VALID_BODY_SN_DNS_RESOLUTION = [
    "enable",  # Enable DNS resolution of the FortiSwitch unit's IP address with switch name.
    "disable",  # Disable DNS resolution of the FortiSwitch unit's IP address with switch name.
]
VALID_BODY_MAC_EVENT_LOGGING = [
    "enable",  # Enable MAC address event logging.
    "disable",  # Disable MAC address event logging.
]
VALID_BODY_BOUNCE_QUARANTINED_LINK = [
    "disable",  # Disable bouncing (administratively bring the link down, up) of a switch port where a quarantined device was seen last.
    "enable",  # Enable bouncing (administratively bring the link down, up) of a switch port where a quarantined device was seen last.
]
VALID_BODY_QUARANTINE_MODE = [
    "by-vlan",  # Quarantined device traffic is sent to FortiGate on a separate quarantine VLAN.
    "by-redirect",  # Quarantined device traffic is redirected only to the FortiGate on the received VLAN.
]
VALID_BODY_UPDATE_USER_DEVICE = [
    "mac-cache",  # Update MAC address from switch-controller mac-cache.
    "lldp",  # Update from FortiSwitch LLDP neighbor database.
    "dhcp-snooping",  # Update from FortiSwitch DHCP snooping client and server databases.
    "l2-db",  # Update from FortiSwitch Network-monitor Layer 2 tracking database.
    "l3-db",  # Update from FortiSwitch Network-monitor Layer 3 tracking database.
]
VALID_BODY_FIPS_ENFORCE = [
    "disable",  # Disable enforcement of FIPS on managed FortiSwitch devices.
    "enable",  # Enable enforcement of FIPS on managed FortiSwitch devices.
]
VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION = [
    "enable",  # Enable firmware provision on authorization.
    "disable",  # Disable firmware provision on authorization.
]
VALID_BODY_SWITCH_ON_DEAUTH = [
    "no-op",  # No-operation on the managed FortiSwitch on deauthorization.
    "factory-reset",  # Factory-reset the managed FortiSwitch on deauthorization.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_global__get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/global_."""
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
    """Validate required fields for switch_controller/global_."""
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


def validate_switch_controller_global__post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/global_ object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "https-image-push" in payload:
        value = payload["https-image-push"]
        if value not in VALID_BODY_HTTPS_IMAGE_PUSH:
            desc = FIELD_DESCRIPTIONS.get("https-image-push", "")
            error_msg = f"Invalid value for 'https-image-push': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTPS_IMAGE_PUSH)}"
            error_msg += f"\n  → Example: https-image-push='{{ VALID_BODY_HTTPS_IMAGE_PUSH[0] }}'"
            return (False, error_msg)
    if "vlan-all-mode" in payload:
        value = payload["vlan-all-mode"]
        if value not in VALID_BODY_VLAN_ALL_MODE:
            desc = FIELD_DESCRIPTIONS.get("vlan-all-mode", "")
            error_msg = f"Invalid value for 'vlan-all-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VLAN_ALL_MODE)}"
            error_msg += f"\n  → Example: vlan-all-mode='{{ VALID_BODY_VLAN_ALL_MODE[0] }}'"
            return (False, error_msg)
    if "vlan-optimization" in payload:
        value = payload["vlan-optimization"]
        if value not in VALID_BODY_VLAN_OPTIMIZATION:
            desc = FIELD_DESCRIPTIONS.get("vlan-optimization", "")
            error_msg = f"Invalid value for 'vlan-optimization': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VLAN_OPTIMIZATION)}"
            error_msg += f"\n  → Example: vlan-optimization='{{ VALID_BODY_VLAN_OPTIMIZATION[0] }}'"
            return (False, error_msg)
    if "vlan-identity" in payload:
        value = payload["vlan-identity"]
        if value not in VALID_BODY_VLAN_IDENTITY:
            desc = FIELD_DESCRIPTIONS.get("vlan-identity", "")
            error_msg = f"Invalid value for 'vlan-identity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VLAN_IDENTITY)}"
            error_msg += f"\n  → Example: vlan-identity='{{ VALID_BODY_VLAN_IDENTITY[0] }}'"
            return (False, error_msg)
    if "dhcp-server-access-list" in payload:
        value = payload["dhcp-server-access-list"]
        if value not in VALID_BODY_DHCP_SERVER_ACCESS_LIST:
            desc = FIELD_DESCRIPTIONS.get("dhcp-server-access-list", "")
            error_msg = f"Invalid value for 'dhcp-server-access-list': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_SERVER_ACCESS_LIST)}"
            error_msg += f"\n  → Example: dhcp-server-access-list='{{ VALID_BODY_DHCP_SERVER_ACCESS_LIST[0] }}'"
            return (False, error_msg)
    if "dhcp-option82-format" in payload:
        value = payload["dhcp-option82-format"]
        if value not in VALID_BODY_DHCP_OPTION82_FORMAT:
            desc = FIELD_DESCRIPTIONS.get("dhcp-option82-format", "")
            error_msg = f"Invalid value for 'dhcp-option82-format': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_OPTION82_FORMAT)}"
            error_msg += f"\n  → Example: dhcp-option82-format='{{ VALID_BODY_DHCP_OPTION82_FORMAT[0] }}'"
            return (False, error_msg)
    if "dhcp-option82-circuit-id" in payload:
        value = payload["dhcp-option82-circuit-id"]
        if value not in VALID_BODY_DHCP_OPTION82_CIRCUIT_ID:
            desc = FIELD_DESCRIPTIONS.get("dhcp-option82-circuit-id", "")
            error_msg = f"Invalid value for 'dhcp-option82-circuit-id': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_OPTION82_CIRCUIT_ID)}"
            error_msg += f"\n  → Example: dhcp-option82-circuit-id='{{ VALID_BODY_DHCP_OPTION82_CIRCUIT_ID[0] }}'"
            return (False, error_msg)
    if "dhcp-option82-remote-id" in payload:
        value = payload["dhcp-option82-remote-id"]
        if value not in VALID_BODY_DHCP_OPTION82_REMOTE_ID:
            desc = FIELD_DESCRIPTIONS.get("dhcp-option82-remote-id", "")
            error_msg = f"Invalid value for 'dhcp-option82-remote-id': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_OPTION82_REMOTE_ID)}"
            error_msg += f"\n  → Example: dhcp-option82-remote-id='{{ VALID_BODY_DHCP_OPTION82_REMOTE_ID[0] }}'"
            return (False, error_msg)
    if "dhcp-snoop-client-req" in payload:
        value = payload["dhcp-snoop-client-req"]
        if value not in VALID_BODY_DHCP_SNOOP_CLIENT_REQ:
            desc = FIELD_DESCRIPTIONS.get("dhcp-snoop-client-req", "")
            error_msg = f"Invalid value for 'dhcp-snoop-client-req': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_SNOOP_CLIENT_REQ)}"
            error_msg += f"\n  → Example: dhcp-snoop-client-req='{{ VALID_BODY_DHCP_SNOOP_CLIENT_REQ[0] }}'"
            return (False, error_msg)
    if "log-mac-limit-violations" in payload:
        value = payload["log-mac-limit-violations"]
        if value not in VALID_BODY_LOG_MAC_LIMIT_VIOLATIONS:
            desc = FIELD_DESCRIPTIONS.get("log-mac-limit-violations", "")
            error_msg = f"Invalid value for 'log-mac-limit-violations': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_MAC_LIMIT_VIOLATIONS)}"
            error_msg += f"\n  → Example: log-mac-limit-violations='{{ VALID_BODY_LOG_MAC_LIMIT_VIOLATIONS[0] }}'"
            return (False, error_msg)
    if "sn-dns-resolution" in payload:
        value = payload["sn-dns-resolution"]
        if value not in VALID_BODY_SN_DNS_RESOLUTION:
            desc = FIELD_DESCRIPTIONS.get("sn-dns-resolution", "")
            error_msg = f"Invalid value for 'sn-dns-resolution': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SN_DNS_RESOLUTION)}"
            error_msg += f"\n  → Example: sn-dns-resolution='{{ VALID_BODY_SN_DNS_RESOLUTION[0] }}'"
            return (False, error_msg)
    if "mac-event-logging" in payload:
        value = payload["mac-event-logging"]
        if value not in VALID_BODY_MAC_EVENT_LOGGING:
            desc = FIELD_DESCRIPTIONS.get("mac-event-logging", "")
            error_msg = f"Invalid value for 'mac-event-logging': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_EVENT_LOGGING)}"
            error_msg += f"\n  → Example: mac-event-logging='{{ VALID_BODY_MAC_EVENT_LOGGING[0] }}'"
            return (False, error_msg)
    if "bounce-quarantined-link" in payload:
        value = payload["bounce-quarantined-link"]
        if value not in VALID_BODY_BOUNCE_QUARANTINED_LINK:
            desc = FIELD_DESCRIPTIONS.get("bounce-quarantined-link", "")
            error_msg = f"Invalid value for 'bounce-quarantined-link': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BOUNCE_QUARANTINED_LINK)}"
            error_msg += f"\n  → Example: bounce-quarantined-link='{{ VALID_BODY_BOUNCE_QUARANTINED_LINK[0] }}'"
            return (False, error_msg)
    if "quarantine-mode" in payload:
        value = payload["quarantine-mode"]
        if value not in VALID_BODY_QUARANTINE_MODE:
            desc = FIELD_DESCRIPTIONS.get("quarantine-mode", "")
            error_msg = f"Invalid value for 'quarantine-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QUARANTINE_MODE)}"
            error_msg += f"\n  → Example: quarantine-mode='{{ VALID_BODY_QUARANTINE_MODE[0] }}'"
            return (False, error_msg)
    if "update-user-device" in payload:
        value = payload["update-user-device"]
        if value not in VALID_BODY_UPDATE_USER_DEVICE:
            desc = FIELD_DESCRIPTIONS.get("update-user-device", "")
            error_msg = f"Invalid value for 'update-user-device': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_USER_DEVICE)}"
            error_msg += f"\n  → Example: update-user-device='{{ VALID_BODY_UPDATE_USER_DEVICE[0] }}'"
            return (False, error_msg)
    if "fips-enforce" in payload:
        value = payload["fips-enforce"]
        if value not in VALID_BODY_FIPS_ENFORCE:
            desc = FIELD_DESCRIPTIONS.get("fips-enforce", "")
            error_msg = f"Invalid value for 'fips-enforce': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FIPS_ENFORCE)}"
            error_msg += f"\n  → Example: fips-enforce='{{ VALID_BODY_FIPS_ENFORCE[0] }}'"
            return (False, error_msg)
    if "firmware-provision-on-authorization" in payload:
        value = payload["firmware-provision-on-authorization"]
        if value not in VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION:
            desc = FIELD_DESCRIPTIONS.get("firmware-provision-on-authorization", "")
            error_msg = f"Invalid value for 'firmware-provision-on-authorization': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION)}"
            error_msg += f"\n  → Example: firmware-provision-on-authorization='{{ VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION[0] }}'"
            return (False, error_msg)
    if "switch-on-deauth" in payload:
        value = payload["switch-on-deauth"]
        if value not in VALID_BODY_SWITCH_ON_DEAUTH:
            desc = FIELD_DESCRIPTIONS.get("switch-on-deauth", "")
            error_msg = f"Invalid value for 'switch-on-deauth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_ON_DEAUTH)}"
            error_msg += f"\n  → Example: switch-on-deauth='{{ VALID_BODY_SWITCH_ON_DEAUTH[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_global__put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/global_."""
    # Step 1: Validate enum values
    if "https-image-push" in payload:
        value = payload["https-image-push"]
        if value not in VALID_BODY_HTTPS_IMAGE_PUSH:
            return (
                False,
                f"Invalid value for 'https-image-push'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_IMAGE_PUSH)}",
            )
    if "vlan-all-mode" in payload:
        value = payload["vlan-all-mode"]
        if value not in VALID_BODY_VLAN_ALL_MODE:
            return (
                False,
                f"Invalid value for 'vlan-all-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_ALL_MODE)}",
            )
    if "vlan-optimization" in payload:
        value = payload["vlan-optimization"]
        if value not in VALID_BODY_VLAN_OPTIMIZATION:
            return (
                False,
                f"Invalid value for 'vlan-optimization'='{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_OPTIMIZATION)}",
            )
    if "vlan-identity" in payload:
        value = payload["vlan-identity"]
        if value not in VALID_BODY_VLAN_IDENTITY:
            return (
                False,
                f"Invalid value for 'vlan-identity'='{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_IDENTITY)}",
            )
    if "dhcp-server-access-list" in payload:
        value = payload["dhcp-server-access-list"]
        if value not in VALID_BODY_DHCP_SERVER_ACCESS_LIST:
            return (
                False,
                f"Invalid value for 'dhcp-server-access-list'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SERVER_ACCESS_LIST)}",
            )
    if "dhcp-option82-format" in payload:
        value = payload["dhcp-option82-format"]
        if value not in VALID_BODY_DHCP_OPTION82_FORMAT:
            return (
                False,
                f"Invalid value for 'dhcp-option82-format'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_FORMAT)}",
            )
    if "dhcp-option82-circuit-id" in payload:
        value = payload["dhcp-option82-circuit-id"]
        if value not in VALID_BODY_DHCP_OPTION82_CIRCUIT_ID:
            return (
                False,
                f"Invalid value for 'dhcp-option82-circuit-id'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_CIRCUIT_ID)}",
            )
    if "dhcp-option82-remote-id" in payload:
        value = payload["dhcp-option82-remote-id"]
        if value not in VALID_BODY_DHCP_OPTION82_REMOTE_ID:
            return (
                False,
                f"Invalid value for 'dhcp-option82-remote-id'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_REMOTE_ID)}",
            )
    if "dhcp-snoop-client-req" in payload:
        value = payload["dhcp-snoop-client-req"]
        if value not in VALID_BODY_DHCP_SNOOP_CLIENT_REQ:
            return (
                False,
                f"Invalid value for 'dhcp-snoop-client-req'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SNOOP_CLIENT_REQ)}",
            )
    if "log-mac-limit-violations" in payload:
        value = payload["log-mac-limit-violations"]
        if value not in VALID_BODY_LOG_MAC_LIMIT_VIOLATIONS:
            return (
                False,
                f"Invalid value for 'log-mac-limit-violations'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_MAC_LIMIT_VIOLATIONS)}",
            )
    if "sn-dns-resolution" in payload:
        value = payload["sn-dns-resolution"]
        if value not in VALID_BODY_SN_DNS_RESOLUTION:
            return (
                False,
                f"Invalid value for 'sn-dns-resolution'='{value}'. Must be one of: {', '.join(VALID_BODY_SN_DNS_RESOLUTION)}",
            )
    if "mac-event-logging" in payload:
        value = payload["mac-event-logging"]
        if value not in VALID_BODY_MAC_EVENT_LOGGING:
            return (
                False,
                f"Invalid value for 'mac-event-logging'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_EVENT_LOGGING)}",
            )
    if "bounce-quarantined-link" in payload:
        value = payload["bounce-quarantined-link"]
        if value not in VALID_BODY_BOUNCE_QUARANTINED_LINK:
            return (
                False,
                f"Invalid value for 'bounce-quarantined-link'='{value}'. Must be one of: {', '.join(VALID_BODY_BOUNCE_QUARANTINED_LINK)}",
            )
    if "quarantine-mode" in payload:
        value = payload["quarantine-mode"]
        if value not in VALID_BODY_QUARANTINE_MODE:
            return (
                False,
                f"Invalid value for 'quarantine-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_QUARANTINE_MODE)}",
            )
    if "update-user-device" in payload:
        value = payload["update-user-device"]
        if value not in VALID_BODY_UPDATE_USER_DEVICE:
            return (
                False,
                f"Invalid value for 'update-user-device'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_USER_DEVICE)}",
            )
    if "fips-enforce" in payload:
        value = payload["fips-enforce"]
        if value not in VALID_BODY_FIPS_ENFORCE:
            return (
                False,
                f"Invalid value for 'fips-enforce'='{value}'. Must be one of: {', '.join(VALID_BODY_FIPS_ENFORCE)}",
            )
    if "firmware-provision-on-authorization" in payload:
        value = payload["firmware-provision-on-authorization"]
        if value not in VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION:
            return (
                False,
                f"Invalid value for 'firmware-provision-on-authorization'='{value}'. Must be one of: {', '.join(VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION)}",
            )
    if "switch-on-deauth" in payload:
        value = payload["switch-on-deauth"]
        if value not in VALID_BODY_SWITCH_ON_DEAUTH:
            return (
                False,
                f"Invalid value for 'switch-on-deauth'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_ON_DEAUTH)}",
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
    "endpoint": "switch_controller/global_",
    "category": "cmdb",
    "api_path": "switch-controller/global",
    "help": "Configure FortiSwitch global settings.",
    "total_fields": 27,
    "required_fields_count": 0,
    "fields_with_defaults_count": 25,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
