"""Validation helpers for switch_controller/security_policy/x802_1x - Auto-generated"""

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
    "user-group",  # Name of user-group to assign to this MAC Authentication Bypass (MAB) policy.
    "guest-vlan-id",  # Guest VLAN name.
    "auth-fail-vlan-id",  # VLAN ID on which authentication failed.
    "authserver-timeout-vlanid",  # Authentication server timeout VLAN name.
    "authserver-timeout-tagged-vlanid",  # Tagged VLAN name for which the timeout option is applied to (only one VLAN ID).
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "security-mode": "802.1X",
    "mac-auth-bypass": "disable",
    "auth-order": "mab-dot1x",
    "auth-priority": "legacy",
    "open-auth": "disable",
    "eap-passthru": "enable",
    "eap-auto-untagged-vlans": "enable",
    "guest-vlan": "disable",
    "guest-vlan-id": "",
    "guest-auth-delay": 30,
    "auth-fail-vlan": "disable",
    "auth-fail-vlan-id": "",
    "framevid-apply": "enable",
    "radius-timeout-overwrite": "disable",
    "policy-type": "802.1X",
    "authserver-timeout-period": 3,
    "authserver-timeout-vlan": "disable",
    "authserver-timeout-vlanid": "",
    "authserver-timeout-tagged": "disable",
    "authserver-timeout-tagged-vlanid": "",
    "dacl": "disable",
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
    "name": "string",  # Policy name.
    "security-mode": "option",  # Port or MAC based 802.1X security mode.
    "user-group": "string",  # Name of user-group to assign to this MAC Authentication Bypa
    "mac-auth-bypass": "option",  # Enable/disable MAB for this policy.
    "auth-order": "option",  # Configure authentication order.
    "auth-priority": "option",  # Configure authentication priority.
    "open-auth": "option",  # Enable/disable open authentication for this policy.
    "eap-passthru": "option",  # Enable/disable EAP pass-through mode, allowing protocols (su
    "eap-auto-untagged-vlans": "option",  # Enable/disable automatic inclusion of untagged VLANs.
    "guest-vlan": "option",  # Enable the guest VLAN feature to allow limited access to non
    "guest-vlan-id": "string",  # Guest VLAN name.
    "guest-auth-delay": "integer",  # Guest authentication delay (1 - 900  sec, default = 30).
    "auth-fail-vlan": "option",  # Enable to allow limited access to clients that cannot authen
    "auth-fail-vlan-id": "string",  # VLAN ID on which authentication failed.
    "framevid-apply": "option",  # Enable/disable the capability to apply the EAP/MAB frame VLA
    "radius-timeout-overwrite": "option",  # Enable to override the global RADIUS session timeout.
    "policy-type": "option",  # Policy type.
    "authserver-timeout-period": "integer",  # Authentication server timeout period (3 - 15 sec, default = 
    "authserver-timeout-vlan": "option",  # Enable/disable the authentication server timeout VLAN to all
    "authserver-timeout-vlanid": "string",  # Authentication server timeout VLAN name.
    "authserver-timeout-tagged": "option",  # Configure timeout option for the tagged VLAN which allows li
    "authserver-timeout-tagged-vlanid": "string",  # Tagged VLAN name for which the timeout option is applied to 
    "dacl": "option",  # Enable/disable dynamic access control list on this interface
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Policy name.",
    "security-mode": "Port or MAC based 802.1X security mode.",
    "user-group": "Name of user-group to assign to this MAC Authentication Bypass (MAB) policy.",
    "mac-auth-bypass": "Enable/disable MAB for this policy.",
    "auth-order": "Configure authentication order.",
    "auth-priority": "Configure authentication priority.",
    "open-auth": "Enable/disable open authentication for this policy.",
    "eap-passthru": "Enable/disable EAP pass-through mode, allowing protocols (such as LLDP) to pass through ports for more flexible authentication.",
    "eap-auto-untagged-vlans": "Enable/disable automatic inclusion of untagged VLANs.",
    "guest-vlan": "Enable the guest VLAN feature to allow limited access to non-802.1X-compliant clients.",
    "guest-vlan-id": "Guest VLAN name.",
    "guest-auth-delay": "Guest authentication delay (1 - 900  sec, default = 30).",
    "auth-fail-vlan": "Enable to allow limited access to clients that cannot authenticate.",
    "auth-fail-vlan-id": "VLAN ID on which authentication failed.",
    "framevid-apply": "Enable/disable the capability to apply the EAP/MAB frame VLAN to the port native VLAN.",
    "radius-timeout-overwrite": "Enable to override the global RADIUS session timeout.",
    "policy-type": "Policy type.",
    "authserver-timeout-period": "Authentication server timeout period (3 - 15 sec, default = 3).",
    "authserver-timeout-vlan": "Enable/disable the authentication server timeout VLAN to allow limited access when RADIUS is unavailable.",
    "authserver-timeout-vlanid": "Authentication server timeout VLAN name.",
    "authserver-timeout-tagged": "Configure timeout option for the tagged VLAN which allows limited access when the authentication server is unavailable.",
    "authserver-timeout-tagged-vlanid": "Tagged VLAN name for which the timeout option is applied to (only one VLAN ID).",
    "dacl": "Enable/disable dynamic access control list on this interface.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 31},
    "guest-vlan-id": {"type": "string", "max_length": 15},
    "guest-auth-delay": {"type": "integer", "min": 1, "max": 900},
    "auth-fail-vlan-id": {"type": "string", "max_length": 15},
    "authserver-timeout-period": {"type": "integer", "min": 3, "max": 15},
    "authserver-timeout-vlanid": {"type": "string", "max_length": 15},
    "authserver-timeout-tagged-vlanid": {"type": "string", "max_length": 15},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "user-group": {
        "name": {
            "type": "string",
            "help": "Group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_SECURITY_MODE = [
    "802.1X",  # 802.1X port based authentication.
    "802.1X-mac-based",  # 802.1X MAC based authentication.
]
VALID_BODY_MAC_AUTH_BYPASS = [
    "disable",  # Disable MAB.
    "enable",  # Enable MAB.
]
VALID_BODY_AUTH_ORDER = [
    "dot1x-mab",  # Use EAP 1X authentication first then MAB.
    "mab-dot1x",  # Use MAB authentication first then EAP 1X.
    "mab",  # Use MAB authentication only.
]
VALID_BODY_AUTH_PRIORITY = [
    "legacy",  # EAP 1X authentication has a higher priority than MAB with the legacy implementation.
    "dot1x-mab",  # EAP 1X authentication has a higher priority than MAB.
    "mab-dot1x",  # MAB authentication has a higher priority than EAP 1X.
]
VALID_BODY_OPEN_AUTH = [
    "disable",  # Disable open authentication.
    "enable",  # Enable open authentication.
]
VALID_BODY_EAP_PASSTHRU = [
    "disable",  # Disable EAP pass-through mode on this interface.
    "enable",  # Enable EAP pass-through mode on this interface.
]
VALID_BODY_EAP_AUTO_UNTAGGED_VLANS = [
    "disable",  # Disable automatic inclusion of untagged VLANs.
    "enable",  # Enable automatic inclusion of untagged VLANs.
]
VALID_BODY_GUEST_VLAN = [
    "disable",  # Disable guest VLAN on this interface.
    "enable",  # Enable guest VLAN on this interface.
]
VALID_BODY_AUTH_FAIL_VLAN = [
    "disable",  # Disable authentication fail VLAN on this interface.
    "enable",  # Enable authentication fail VLAN on this interface.
]
VALID_BODY_FRAMEVID_APPLY = [
    "disable",  # Disable the capability to apply the EAP/MAB frame VLAN to the port native VLAN.
    "enable",  # Enable the capability to apply the EAP/MAB frame VLAN to the port native VLAN.
]
VALID_BODY_RADIUS_TIMEOUT_OVERWRITE = [
    "disable",  # Override the global RADIUS session timeout.
    "enable",  # Use the global RADIUS session timeout.
]
VALID_BODY_POLICY_TYPE = [
    "802.1X",  # 802.1X security policy.
]
VALID_BODY_AUTHSERVER_TIMEOUT_VLAN = [
    "disable",  # Disable authentication server timeout VLAN on this interface.
    "enable",  # Enable authentication server timeout VLAN on this interface.
]
VALID_BODY_AUTHSERVER_TIMEOUT_TAGGED = [
    "disable",  # Disable authentication server timeout on this interface.
    "lldp-voice",  # LLDP voice timeout for the tagged VLAN on this interface.
    "static",  # Static timeout for the tagged VLAN on this interface.
]
VALID_BODY_DACL = [
    "disable",  # Disable dynamic access control list on this interface.
    "enable",  # Enable dynamic access control on this interface.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_security_policy_x802_1x_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/security_policy/x802_1x."""
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
    """Validate required fields for switch_controller/security_policy/x802_1x."""
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


def validate_switch_controller_security_policy_x802_1x_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/security_policy/x802_1x object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
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
    if "mac-auth-bypass" in payload:
        value = payload["mac-auth-bypass"]
        if value not in VALID_BODY_MAC_AUTH_BYPASS:
            desc = FIELD_DESCRIPTIONS.get("mac-auth-bypass", "")
            error_msg = f"Invalid value for 'mac-auth-bypass': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_AUTH_BYPASS)}"
            error_msg += f"\n  → Example: mac-auth-bypass='{{ VALID_BODY_MAC_AUTH_BYPASS[0] }}'"
            return (False, error_msg)
    if "auth-order" in payload:
        value = payload["auth-order"]
        if value not in VALID_BODY_AUTH_ORDER:
            desc = FIELD_DESCRIPTIONS.get("auth-order", "")
            error_msg = f"Invalid value for 'auth-order': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_ORDER)}"
            error_msg += f"\n  → Example: auth-order='{{ VALID_BODY_AUTH_ORDER[0] }}'"
            return (False, error_msg)
    if "auth-priority" in payload:
        value = payload["auth-priority"]
        if value not in VALID_BODY_AUTH_PRIORITY:
            desc = FIELD_DESCRIPTIONS.get("auth-priority", "")
            error_msg = f"Invalid value for 'auth-priority': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_PRIORITY)}"
            error_msg += f"\n  → Example: auth-priority='{{ VALID_BODY_AUTH_PRIORITY[0] }}'"
            return (False, error_msg)
    if "open-auth" in payload:
        value = payload["open-auth"]
        if value not in VALID_BODY_OPEN_AUTH:
            desc = FIELD_DESCRIPTIONS.get("open-auth", "")
            error_msg = f"Invalid value for 'open-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OPEN_AUTH)}"
            error_msg += f"\n  → Example: open-auth='{{ VALID_BODY_OPEN_AUTH[0] }}'"
            return (False, error_msg)
    if "eap-passthru" in payload:
        value = payload["eap-passthru"]
        if value not in VALID_BODY_EAP_PASSTHRU:
            desc = FIELD_DESCRIPTIONS.get("eap-passthru", "")
            error_msg = f"Invalid value for 'eap-passthru': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAP_PASSTHRU)}"
            error_msg += f"\n  → Example: eap-passthru='{{ VALID_BODY_EAP_PASSTHRU[0] }}'"
            return (False, error_msg)
    if "eap-auto-untagged-vlans" in payload:
        value = payload["eap-auto-untagged-vlans"]
        if value not in VALID_BODY_EAP_AUTO_UNTAGGED_VLANS:
            desc = FIELD_DESCRIPTIONS.get("eap-auto-untagged-vlans", "")
            error_msg = f"Invalid value for 'eap-auto-untagged-vlans': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAP_AUTO_UNTAGGED_VLANS)}"
            error_msg += f"\n  → Example: eap-auto-untagged-vlans='{{ VALID_BODY_EAP_AUTO_UNTAGGED_VLANS[0] }}'"
            return (False, error_msg)
    if "guest-vlan" in payload:
        value = payload["guest-vlan"]
        if value not in VALID_BODY_GUEST_VLAN:
            desc = FIELD_DESCRIPTIONS.get("guest-vlan", "")
            error_msg = f"Invalid value for 'guest-vlan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUEST_VLAN)}"
            error_msg += f"\n  → Example: guest-vlan='{{ VALID_BODY_GUEST_VLAN[0] }}'"
            return (False, error_msg)
    if "auth-fail-vlan" in payload:
        value = payload["auth-fail-vlan"]
        if value not in VALID_BODY_AUTH_FAIL_VLAN:
            desc = FIELD_DESCRIPTIONS.get("auth-fail-vlan", "")
            error_msg = f"Invalid value for 'auth-fail-vlan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_FAIL_VLAN)}"
            error_msg += f"\n  → Example: auth-fail-vlan='{{ VALID_BODY_AUTH_FAIL_VLAN[0] }}'"
            return (False, error_msg)
    if "framevid-apply" in payload:
        value = payload["framevid-apply"]
        if value not in VALID_BODY_FRAMEVID_APPLY:
            desc = FIELD_DESCRIPTIONS.get("framevid-apply", "")
            error_msg = f"Invalid value for 'framevid-apply': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FRAMEVID_APPLY)}"
            error_msg += f"\n  → Example: framevid-apply='{{ VALID_BODY_FRAMEVID_APPLY[0] }}'"
            return (False, error_msg)
    if "radius-timeout-overwrite" in payload:
        value = payload["radius-timeout-overwrite"]
        if value not in VALID_BODY_RADIUS_TIMEOUT_OVERWRITE:
            desc = FIELD_DESCRIPTIONS.get("radius-timeout-overwrite", "")
            error_msg = f"Invalid value for 'radius-timeout-overwrite': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RADIUS_TIMEOUT_OVERWRITE)}"
            error_msg += f"\n  → Example: radius-timeout-overwrite='{{ VALID_BODY_RADIUS_TIMEOUT_OVERWRITE[0] }}'"
            return (False, error_msg)
    if "policy-type" in payload:
        value = payload["policy-type"]
        if value not in VALID_BODY_POLICY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("policy-type", "")
            error_msg = f"Invalid value for 'policy-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_POLICY_TYPE)}"
            error_msg += f"\n  → Example: policy-type='{{ VALID_BODY_POLICY_TYPE[0] }}'"
            return (False, error_msg)
    if "authserver-timeout-vlan" in payload:
        value = payload["authserver-timeout-vlan"]
        if value not in VALID_BODY_AUTHSERVER_TIMEOUT_VLAN:
            desc = FIELD_DESCRIPTIONS.get("authserver-timeout-vlan", "")
            error_msg = f"Invalid value for 'authserver-timeout-vlan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHSERVER_TIMEOUT_VLAN)}"
            error_msg += f"\n  → Example: authserver-timeout-vlan='{{ VALID_BODY_AUTHSERVER_TIMEOUT_VLAN[0] }}'"
            return (False, error_msg)
    if "authserver-timeout-tagged" in payload:
        value = payload["authserver-timeout-tagged"]
        if value not in VALID_BODY_AUTHSERVER_TIMEOUT_TAGGED:
            desc = FIELD_DESCRIPTIONS.get("authserver-timeout-tagged", "")
            error_msg = f"Invalid value for 'authserver-timeout-tagged': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHSERVER_TIMEOUT_TAGGED)}"
            error_msg += f"\n  → Example: authserver-timeout-tagged='{{ VALID_BODY_AUTHSERVER_TIMEOUT_TAGGED[0] }}'"
            return (False, error_msg)
    if "dacl" in payload:
        value = payload["dacl"]
        if value not in VALID_BODY_DACL:
            desc = FIELD_DESCRIPTIONS.get("dacl", "")
            error_msg = f"Invalid value for 'dacl': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DACL)}"
            error_msg += f"\n  → Example: dacl='{{ VALID_BODY_DACL[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_security_policy_x802_1x_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/security_policy/x802_1x."""
    # Step 1: Validate enum values
    if "security-mode" in payload:
        value = payload["security-mode"]
        if value not in VALID_BODY_SECURITY_MODE:
            return (
                False,
                f"Invalid value for 'security-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MODE)}",
            )
    if "mac-auth-bypass" in payload:
        value = payload["mac-auth-bypass"]
        if value not in VALID_BODY_MAC_AUTH_BYPASS:
            return (
                False,
                f"Invalid value for 'mac-auth-bypass'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_AUTH_BYPASS)}",
            )
    if "auth-order" in payload:
        value = payload["auth-order"]
        if value not in VALID_BODY_AUTH_ORDER:
            return (
                False,
                f"Invalid value for 'auth-order'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_ORDER)}",
            )
    if "auth-priority" in payload:
        value = payload["auth-priority"]
        if value not in VALID_BODY_AUTH_PRIORITY:
            return (
                False,
                f"Invalid value for 'auth-priority'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PRIORITY)}",
            )
    if "open-auth" in payload:
        value = payload["open-auth"]
        if value not in VALID_BODY_OPEN_AUTH:
            return (
                False,
                f"Invalid value for 'open-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_OPEN_AUTH)}",
            )
    if "eap-passthru" in payload:
        value = payload["eap-passthru"]
        if value not in VALID_BODY_EAP_PASSTHRU:
            return (
                False,
                f"Invalid value for 'eap-passthru'='{value}'. Must be one of: {', '.join(VALID_BODY_EAP_PASSTHRU)}",
            )
    if "eap-auto-untagged-vlans" in payload:
        value = payload["eap-auto-untagged-vlans"]
        if value not in VALID_BODY_EAP_AUTO_UNTAGGED_VLANS:
            return (
                False,
                f"Invalid value for 'eap-auto-untagged-vlans'='{value}'. Must be one of: {', '.join(VALID_BODY_EAP_AUTO_UNTAGGED_VLANS)}",
            )
    if "guest-vlan" in payload:
        value = payload["guest-vlan"]
        if value not in VALID_BODY_GUEST_VLAN:
            return (
                False,
                f"Invalid value for 'guest-vlan'='{value}'. Must be one of: {', '.join(VALID_BODY_GUEST_VLAN)}",
            )
    if "auth-fail-vlan" in payload:
        value = payload["auth-fail-vlan"]
        if value not in VALID_BODY_AUTH_FAIL_VLAN:
            return (
                False,
                f"Invalid value for 'auth-fail-vlan'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_FAIL_VLAN)}",
            )
    if "framevid-apply" in payload:
        value = payload["framevid-apply"]
        if value not in VALID_BODY_FRAMEVID_APPLY:
            return (
                False,
                f"Invalid value for 'framevid-apply'='{value}'. Must be one of: {', '.join(VALID_BODY_FRAMEVID_APPLY)}",
            )
    if "radius-timeout-overwrite" in payload:
        value = payload["radius-timeout-overwrite"]
        if value not in VALID_BODY_RADIUS_TIMEOUT_OVERWRITE:
            return (
                False,
                f"Invalid value for 'radius-timeout-overwrite'='{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_TIMEOUT_OVERWRITE)}",
            )
    if "policy-type" in payload:
        value = payload["policy-type"]
        if value not in VALID_BODY_POLICY_TYPE:
            return (
                False,
                f"Invalid value for 'policy-type'='{value}'. Must be one of: {', '.join(VALID_BODY_POLICY_TYPE)}",
            )
    if "authserver-timeout-vlan" in payload:
        value = payload["authserver-timeout-vlan"]
        if value not in VALID_BODY_AUTHSERVER_TIMEOUT_VLAN:
            return (
                False,
                f"Invalid value for 'authserver-timeout-vlan'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHSERVER_TIMEOUT_VLAN)}",
            )
    if "authserver-timeout-tagged" in payload:
        value = payload["authserver-timeout-tagged"]
        if value not in VALID_BODY_AUTHSERVER_TIMEOUT_TAGGED:
            return (
                False,
                f"Invalid value for 'authserver-timeout-tagged'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHSERVER_TIMEOUT_TAGGED)}",
            )
    if "dacl" in payload:
        value = payload["dacl"]
        if value not in VALID_BODY_DACL:
            return (
                False,
                f"Invalid value for 'dacl'='{value}'. Must be one of: {', '.join(VALID_BODY_DACL)}",
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
    "endpoint": "switch_controller/security_policy/x802_1x",
    "category": "cmdb",
    "api_path": "switch-controller.security-policy/802-1X",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure 802.1x MAC Authentication Bypass (MAB) policies.",
    "total_fields": 23,
    "required_fields_count": 5,
    "fields_with_defaults_count": 22,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
