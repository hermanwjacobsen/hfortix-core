"""
Validation helpers for system/admin endpoint.

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
    "remote-group",  # User group name used for remote auth.
    "password",  # Admin user password.
    "peer-group",  # Name of peer group defined under config user group which has PKI members. Used for peer certificate authentication (for HTTPS admin access).
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "remote-auth": "disable",
    "remote-group": "",
    "wildcard": "disable",
    "peer-auth": "disable",
    "peer-group": "",
    "trusthost1": "0.0.0.0 0.0.0.0",
    "trusthost2": "0.0.0.0 0.0.0.0",
    "trusthost3": "0.0.0.0 0.0.0.0",
    "trusthost4": "0.0.0.0 0.0.0.0",
    "trusthost5": "0.0.0.0 0.0.0.0",
    "trusthost6": "0.0.0.0 0.0.0.0",
    "trusthost7": "0.0.0.0 0.0.0.0",
    "trusthost8": "0.0.0.0 0.0.0.0",
    "trusthost9": "0.0.0.0 0.0.0.0",
    "trusthost10": "0.0.0.0 0.0.0.0",
    "ip6-trusthost1": "::/0",
    "ip6-trusthost2": "::/0",
    "ip6-trusthost3": "::/0",
    "ip6-trusthost4": "::/0",
    "ip6-trusthost5": "::/0",
    "ip6-trusthost6": "::/0",
    "ip6-trusthost7": "::/0",
    "ip6-trusthost8": "::/0",
    "ip6-trusthost9": "::/0",
    "ip6-trusthost10": "::/0",
    "accprofile": "",
    "allow-remove-admin-session": "enable",
    "ssh-public-key1": "",
    "ssh-public-key2": "",
    "ssh-public-key3": "",
    "ssh-certificate": "",
    "schedule": "",
    "accprofile-override": "disable",
    "vdom-override": "disable",
    "password-expire": "0000-00-00 00:00:00",
    "force-password-change": "disable",
    "two-factor": "disable",
    "two-factor-authentication": "",
    "two-factor-notification": "",
    "fortitoken": "",
    "email-to": "",
    "sms-server": "fortiguard",
    "sms-custom-server": "",
    "sms-phone": "",
    "guest-auth": "disable",
    "guest-lang": "",
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
    "name": "string",  # User name.
    "vdom": "string",  # Virtual domain(s) that the administrator can access.
    "remote-auth": "option",  # Enable/disable authentication using a remote RADIUS, LDAP, o
    "remote-group": "string",  # User group name used for remote auth.
    "wildcard": "option",  # Enable/disable wildcard RADIUS authentication.
    "password": "password-2",  # Admin user password.
    "peer-auth": "option",  # Set to enable peer certificate authentication (for HTTPS adm
    "peer-group": "string",  # Name of peer group defined under config user group which has
    "trusthost1": "ipv4-classnet",  # Any IPv4 address or subnet address and netmask from which th
    "trusthost2": "ipv4-classnet",  # Any IPv4 address or subnet address and netmask from which th
    "trusthost3": "ipv4-classnet",  # Any IPv4 address or subnet address and netmask from which th
    "trusthost4": "ipv4-classnet",  # Any IPv4 address or subnet address and netmask from which th
    "trusthost5": "ipv4-classnet",  # Any IPv4 address or subnet address and netmask from which th
    "trusthost6": "ipv4-classnet",  # Any IPv4 address or subnet address and netmask from which th
    "trusthost7": "ipv4-classnet",  # Any IPv4 address or subnet address and netmask from which th
    "trusthost8": "ipv4-classnet",  # Any IPv4 address or subnet address and netmask from which th
    "trusthost9": "ipv4-classnet",  # Any IPv4 address or subnet address and netmask from which th
    "trusthost10": "ipv4-classnet",  # Any IPv4 address or subnet address and netmask from which th
    "ip6-trusthost1": "ipv6-prefix",  # Any IPv6 address from which the administrator can connect to
    "ip6-trusthost2": "ipv6-prefix",  # Any IPv6 address from which the administrator can connect to
    "ip6-trusthost3": "ipv6-prefix",  # Any IPv6 address from which the administrator can connect to
    "ip6-trusthost4": "ipv6-prefix",  # Any IPv6 address from which the administrator can connect to
    "ip6-trusthost5": "ipv6-prefix",  # Any IPv6 address from which the administrator can connect to
    "ip6-trusthost6": "ipv6-prefix",  # Any IPv6 address from which the administrator can connect to
    "ip6-trusthost7": "ipv6-prefix",  # Any IPv6 address from which the administrator can connect to
    "ip6-trusthost8": "ipv6-prefix",  # Any IPv6 address from which the administrator can connect to
    "ip6-trusthost9": "ipv6-prefix",  # Any IPv6 address from which the administrator can connect to
    "ip6-trusthost10": "ipv6-prefix",  # Any IPv6 address from which the administrator can connect to
    "accprofile": "string",  # Access profile for this administrator. Access profiles contr
    "allow-remove-admin-session": "option",  # Enable/disable allow admin session to be removed by privileg
    "comments": "var-string",  # Comment.
    "ssh-public-key1": "user",  # Public key of an SSH client. The client is authenticated wit
    "ssh-public-key2": "user",  # Public key of an SSH client. The client is authenticated wit
    "ssh-public-key3": "user",  # Public key of an SSH client. The client is authenticated wit
    "ssh-certificate": "string",  # Select the certificate to be used by the FortiGate for authe
    "schedule": "string",  # Firewall schedule used to restrict when the administrator ca
    "accprofile-override": "option",  # Enable to use the name of an access profile provided by the 
    "vdom-override": "option",  # Enable to use the names of VDOMs provided by the remote auth
    "password-expire": "datetime",  # Password expire time.
    "force-password-change": "option",  # Enable/disable force password change on next login.
    "two-factor": "option",  # Enable/disable two-factor authentication.
    "two-factor-authentication": "option",  # Authentication method by FortiToken Cloud.
    "two-factor-notification": "option",  # Notification method for user activation by FortiToken Cloud.
    "fortitoken": "string",  # This administrator's FortiToken serial number.
    "email-to": "string",  # This administrator's email address.
    "sms-server": "option",  # Send SMS messages using the FortiGuard SMS server or a custo
    "sms-custom-server": "string",  # Custom SMS server to send SMS messages to.
    "sms-phone": "string",  # Phone number on which the administrator receives SMS message
    "guest-auth": "option",  # Enable/disable guest authentication.
    "guest-usergroups": "string",  # Select guest user groups.
    "guest-lang": "string",  # Guest management portal language.
    "status": "key",  # print admin status information
    "list": "key",  # print admin list information
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "User name.",
    "vdom": "Virtual domain(s) that the administrator can access.",
    "remote-auth": "Enable/disable authentication using a remote RADIUS, LDAP, or TACACS+ server.",
    "remote-group": "User group name used for remote auth.",
    "wildcard": "Enable/disable wildcard RADIUS authentication.",
    "password": "Admin user password.",
    "peer-auth": "Set to enable peer certificate authentication (for HTTPS admin access).",
    "peer-group": "Name of peer group defined under config user group which has PKI members. Used for peer certificate authentication (for HTTPS admin access).",
    "trusthost1": "Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.",
    "trusthost2": "Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.",
    "trusthost3": "Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.",
    "trusthost4": "Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.",
    "trusthost5": "Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.",
    "trusthost6": "Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.",
    "trusthost7": "Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.",
    "trusthost8": "Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.",
    "trusthost9": "Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.",
    "trusthost10": "Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.",
    "ip6-trusthost1": "Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.",
    "ip6-trusthost2": "Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.",
    "ip6-trusthost3": "Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.",
    "ip6-trusthost4": "Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.",
    "ip6-trusthost5": "Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.",
    "ip6-trusthost6": "Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.",
    "ip6-trusthost7": "Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.",
    "ip6-trusthost8": "Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.",
    "ip6-trusthost9": "Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.",
    "ip6-trusthost10": "Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.",
    "accprofile": "Access profile for this administrator. Access profiles control administrator access to FortiGate features.",
    "allow-remove-admin-session": "Enable/disable allow admin session to be removed by privileged admin users.",
    "comments": "Comment.",
    "ssh-public-key1": "Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.",
    "ssh-public-key2": "Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.",
    "ssh-public-key3": "Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.",
    "ssh-certificate": "Select the certificate to be used by the FortiGate for authentication with an SSH client.",
    "schedule": "Firewall schedule used to restrict when the administrator can log in. No schedule means no restrictions.",
    "accprofile-override": "Enable to use the name of an access profile provided by the remote authentication server to control the FortiGate features that this administrator can access.",
    "vdom-override": "Enable to use the names of VDOMs provided by the remote authentication server to control the VDOMs that this administrator can access.",
    "password-expire": "Password expire time.",
    "force-password-change": "Enable/disable force password change on next login.",
    "two-factor": "Enable/disable two-factor authentication.",
    "two-factor-authentication": "Authentication method by FortiToken Cloud.",
    "two-factor-notification": "Notification method for user activation by FortiToken Cloud.",
    "fortitoken": "This administrator's FortiToken serial number.",
    "email-to": "This administrator's email address.",
    "sms-server": "Send SMS messages using the FortiGuard SMS server or a custom server.",
    "sms-custom-server": "Custom SMS server to send SMS messages to.",
    "sms-phone": "Phone number on which the administrator receives SMS messages.",
    "guest-auth": "Enable/disable guest authentication.",
    "guest-usergroups": "Select guest user groups.",
    "guest-lang": "Guest management portal language.",
    "status": "print admin status information",
    "list": "print admin list information",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 64},
    "remote-group": {"type": "string", "max_length": 35},
    "peer-group": {"type": "string", "max_length": 35},
    "accprofile": {"type": "string", "max_length": 35},
    "ssh-certificate": {"type": "string", "max_length": 35},
    "schedule": {"type": "string", "max_length": 35},
    "fortitoken": {"type": "string", "max_length": 16},
    "email-to": {"type": "string", "max_length": 63},
    "sms-custom-server": {"type": "string", "max_length": 35},
    "sms-phone": {"type": "string", "max_length": 15},
    "guest-lang": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "vdom": {
        "name": {
            "type": "string",
            "help": "Virtual domain name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "guest-usergroups": {
        "name": {
            "type": "string",
            "help": "Select guest user groups.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_REMOTE_AUTH = [
    "enable",  # Enable remote authentication.
    "disable",  # Disable remote authentication.
]
VALID_BODY_WILDCARD = [
    "enable",  # Enable username wildcard.
    "disable",  # Disable username wildcard.
]
VALID_BODY_PEER_AUTH = [
    "enable",  # Enable peer.
    "disable",  # Disable peer.
]
VALID_BODY_ALLOW_REMOVE_ADMIN_SESSION = [
    "enable",  # Enable allow-remove option.
    "disable",  # Disable allow-remove option.
]
VALID_BODY_ACCPROFILE_OVERRIDE = [
    "enable",  # Enable access profile override.
    "disable",  # Disable access profile override.
]
VALID_BODY_VDOM_OVERRIDE = [
    "enable",  # Enable VDOM override.
    "disable",  # Disable VDOM override.
]
VALID_BODY_FORCE_PASSWORD_CHANGE = [
    "enable",  # Enable force password change on next login.
    "disable",  # Disable force password change on next login.
]
VALID_BODY_TWO_FACTOR = [
    "disable",  # Disable two-factor authentication.
    "fortitoken",  # Use FortiToken or FortiToken mobile two-factor authentication.
    "fortitoken-cloud",  # FortiToken Cloud Service.
    "email",  # Send a two-factor authentication code to the configured email-to email address.
    "sms",  # Send a two-factor authentication code to the configured sms-server and sms-phone.
]
VALID_BODY_TWO_FACTOR_AUTHENTICATION = [
    "fortitoken",  # FortiToken authentication.
    "email",  # Email one time password.
    "sms",  # SMS one time password.
]
VALID_BODY_TWO_FACTOR_NOTIFICATION = [
    "email",  # Email notification for activation code.
    "sms",  # SMS notification for activation code.
]
VALID_BODY_SMS_SERVER = [
    "fortiguard",  # Send SMS by FortiGuard.
    "custom",  # Send SMS by custom server.
]
VALID_BODY_GUEST_AUTH = [
    "disable",  # Disable guest authentication.
    "enable",  # Enable guest authentication.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_admin_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/admin.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_admin_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_system_admin_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_admin_get(
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
    Validate required fields for system/admin.

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


def validate_system_admin_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/admin object.

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
        ...     "remote-group": True,  # User group name used for remote auth.
        ...     "password": True,  # Admin user password.
        ... }
        >>> is_valid, error = validate_system_admin_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "remote-group": True,
        ...     "remote-auth": "{'name': 'enable', 'help': 'Enable remote authentication.', 'label': 'Enable', 'description': 'Enable remote authentication'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_admin_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["remote-auth"] = "invalid-value"
        >>> is_valid, error = validate_system_admin_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_admin_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "remote-auth" in payload:
        value = payload["remote-auth"]
        if value not in VALID_BODY_REMOTE_AUTH:
            desc = FIELD_DESCRIPTIONS.get("remote-auth", "")
            error_msg = f"Invalid value for 'remote-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REMOTE_AUTH)}"
            error_msg += f"\n  → Example: remote-auth='{{ VALID_BODY_REMOTE_AUTH[0] }}'"
            return (False, error_msg)
    if "wildcard" in payload:
        value = payload["wildcard"]
        if value not in VALID_BODY_WILDCARD:
            desc = FIELD_DESCRIPTIONS.get("wildcard", "")
            error_msg = f"Invalid value for 'wildcard': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WILDCARD)}"
            error_msg += f"\n  → Example: wildcard='{{ VALID_BODY_WILDCARD[0] }}'"
            return (False, error_msg)
    if "peer-auth" in payload:
        value = payload["peer-auth"]
        if value not in VALID_BODY_PEER_AUTH:
            desc = FIELD_DESCRIPTIONS.get("peer-auth", "")
            error_msg = f"Invalid value for 'peer-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PEER_AUTH)}"
            error_msg += f"\n  → Example: peer-auth='{{ VALID_BODY_PEER_AUTH[0] }}'"
            return (False, error_msg)
    if "allow-remove-admin-session" in payload:
        value = payload["allow-remove-admin-session"]
        if value not in VALID_BODY_ALLOW_REMOVE_ADMIN_SESSION:
            desc = FIELD_DESCRIPTIONS.get("allow-remove-admin-session", "")
            error_msg = f"Invalid value for 'allow-remove-admin-session': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_REMOVE_ADMIN_SESSION)}"
            error_msg += f"\n  → Example: allow-remove-admin-session='{{ VALID_BODY_ALLOW_REMOVE_ADMIN_SESSION[0] }}'"
            return (False, error_msg)
    if "accprofile-override" in payload:
        value = payload["accprofile-override"]
        if value not in VALID_BODY_ACCPROFILE_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("accprofile-override", "")
            error_msg = f"Invalid value for 'accprofile-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCPROFILE_OVERRIDE)}"
            error_msg += f"\n  → Example: accprofile-override='{{ VALID_BODY_ACCPROFILE_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "vdom-override" in payload:
        value = payload["vdom-override"]
        if value not in VALID_BODY_VDOM_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("vdom-override", "")
            error_msg = f"Invalid value for 'vdom-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VDOM_OVERRIDE)}"
            error_msg += f"\n  → Example: vdom-override='{{ VALID_BODY_VDOM_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "force-password-change" in payload:
        value = payload["force-password-change"]
        if value not in VALID_BODY_FORCE_PASSWORD_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("force-password-change", "")
            error_msg = f"Invalid value for 'force-password-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORCE_PASSWORD_CHANGE)}"
            error_msg += f"\n  → Example: force-password-change='{{ VALID_BODY_FORCE_PASSWORD_CHANGE[0] }}'"
            return (False, error_msg)
    if "two-factor" in payload:
        value = payload["two-factor"]
        if value not in VALID_BODY_TWO_FACTOR:
            desc = FIELD_DESCRIPTIONS.get("two-factor", "")
            error_msg = f"Invalid value for 'two-factor': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TWO_FACTOR)}"
            error_msg += f"\n  → Example: two-factor='{{ VALID_BODY_TWO_FACTOR[0] }}'"
            return (False, error_msg)
    if "two-factor-authentication" in payload:
        value = payload["two-factor-authentication"]
        if value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("two-factor-authentication", "")
            error_msg = f"Invalid value for 'two-factor-authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TWO_FACTOR_AUTHENTICATION)}"
            error_msg += f"\n  → Example: two-factor-authentication='{{ VALID_BODY_TWO_FACTOR_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "two-factor-notification" in payload:
        value = payload["two-factor-notification"]
        if value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            desc = FIELD_DESCRIPTIONS.get("two-factor-notification", "")
            error_msg = f"Invalid value for 'two-factor-notification': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TWO_FACTOR_NOTIFICATION)}"
            error_msg += f"\n  → Example: two-factor-notification='{{ VALID_BODY_TWO_FACTOR_NOTIFICATION[0] }}'"
            return (False, error_msg)
    if "sms-server" in payload:
        value = payload["sms-server"]
        if value not in VALID_BODY_SMS_SERVER:
            desc = FIELD_DESCRIPTIONS.get("sms-server", "")
            error_msg = f"Invalid value for 'sms-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SMS_SERVER)}"
            error_msg += f"\n  → Example: sms-server='{{ VALID_BODY_SMS_SERVER[0] }}'"
            return (False, error_msg)
    if "guest-auth" in payload:
        value = payload["guest-auth"]
        if value not in VALID_BODY_GUEST_AUTH:
            desc = FIELD_DESCRIPTIONS.get("guest-auth", "")
            error_msg = f"Invalid value for 'guest-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUEST_AUTH)}"
            error_msg += f"\n  → Example: guest-auth='{{ VALID_BODY_GUEST_AUTH[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_admin_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/admin.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_admin_put(payload)
    """
    # Step 1: Validate enum values
    if "remote-auth" in payload:
        value = payload["remote-auth"]
        if value not in VALID_BODY_REMOTE_AUTH:
            return (
                False,
                f"Invalid value for 'remote-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_AUTH)}",
            )
    if "wildcard" in payload:
        value = payload["wildcard"]
        if value not in VALID_BODY_WILDCARD:
            return (
                False,
                f"Invalid value for 'wildcard'='{value}'. Must be one of: {', '.join(VALID_BODY_WILDCARD)}",
            )
    if "peer-auth" in payload:
        value = payload["peer-auth"]
        if value not in VALID_BODY_PEER_AUTH:
            return (
                False,
                f"Invalid value for 'peer-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_PEER_AUTH)}",
            )
    if "allow-remove-admin-session" in payload:
        value = payload["allow-remove-admin-session"]
        if value not in VALID_BODY_ALLOW_REMOVE_ADMIN_SESSION:
            return (
                False,
                f"Invalid value for 'allow-remove-admin-session'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_REMOVE_ADMIN_SESSION)}",
            )
    if "accprofile-override" in payload:
        value = payload["accprofile-override"]
        if value not in VALID_BODY_ACCPROFILE_OVERRIDE:
            return (
                False,
                f"Invalid value for 'accprofile-override'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCPROFILE_OVERRIDE)}",
            )
    if "vdom-override" in payload:
        value = payload["vdom-override"]
        if value not in VALID_BODY_VDOM_OVERRIDE:
            return (
                False,
                f"Invalid value for 'vdom-override'='{value}'. Must be one of: {', '.join(VALID_BODY_VDOM_OVERRIDE)}",
            )
    if "force-password-change" in payload:
        value = payload["force-password-change"]
        if value not in VALID_BODY_FORCE_PASSWORD_CHANGE:
            return (
                False,
                f"Invalid value for 'force-password-change'='{value}'. Must be one of: {', '.join(VALID_BODY_FORCE_PASSWORD_CHANGE)}",
            )
    if "two-factor" in payload:
        value = payload["two-factor"]
        if value not in VALID_BODY_TWO_FACTOR:
            return (
                False,
                f"Invalid value for 'two-factor'='{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR)}",
            )
    if "two-factor-authentication" in payload:
        value = payload["two-factor-authentication"]
        if value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'two-factor-authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_AUTHENTICATION)}",
            )
    if "two-factor-notification" in payload:
        value = payload["two-factor-notification"]
        if value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            return (
                False,
                f"Invalid value for 'two-factor-notification'='{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_NOTIFICATION)}",
            )
    if "sms-server" in payload:
        value = payload["sms-server"]
        if value not in VALID_BODY_SMS_SERVER:
            return (
                False,
                f"Invalid value for 'sms-server'='{value}'. Must be one of: {', '.join(VALID_BODY_SMS_SERVER)}",
            )
    if "guest-auth" in payload:
        value = payload["guest-auth"]
        if value not in VALID_BODY_GUEST_AUTH:
            return (
                False,
                f"Invalid value for 'guest-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_GUEST_AUTH)}",
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
    "endpoint": "system/admin",
    "category": "cmdb",
    "api_path": "system/admin",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure admin users.",
    "total_fields": 53,
    "required_fields_count": 3,
    "fields_with_defaults_count": 47,
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
