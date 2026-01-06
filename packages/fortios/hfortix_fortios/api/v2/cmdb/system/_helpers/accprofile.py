"""
Validation helpers for system/accprofile endpoint.

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
    "name",  # Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "scope": "vdom",
    "secfabgrp": "none",
    "ftviewgrp": "none",
    "authgrp": "none",
    "sysgrp": "none",
    "netgrp": "none",
    "loggrp": "none",
    "fwgrp": "none",
    "vpngrp": "none",
    "utmgrp": "none",
    "wanoptgrp": "none",
    "wifi": "none",
    "admintimeout-override": "disable",
    "admintimeout": 10,
    "cli-diagnose": "disable",
    "cli-get": "disable",
    "cli-show": "disable",
    "cli-exec": "disable",
    "cli-config": "disable",
    "system-execute-ssh": "enable",
    "system-execute-telnet": "enable",
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
    "name": "string",  # Profile name.
    "scope": "option",  # Scope of admin access: global or specific VDOM(s).
    "comments": "var-string",  # Comment.
    "secfabgrp": "option",  # Security Fabric.
    "ftviewgrp": "option",  # FortiView.
    "authgrp": "option",  # Administrator access to Users and Devices.
    "sysgrp": "option",  # System Configuration.
    "netgrp": "option",  # Network Configuration.
    "loggrp": "option",  # Administrator access to Logging and Reporting including view
    "fwgrp": "option",  # Administrator access to the Firewall configuration.
    "vpngrp": "option",  # Administrator access to IPsec, SSL, PPTP, and L2TP VPN.
    "utmgrp": "option",  # Administrator access to Security Profiles.
    "wanoptgrp": "option",  # Administrator access to WAN Opt & Cache.
    "wifi": "option",  # Administrator access to the WiFi controller and Switch contr
    "netgrp-permission": "string",  # Custom network permission.
    "sysgrp-permission": "string",  # Custom system permission.
    "fwgrp-permission": "string",  # Custom firewall permission.
    "loggrp-permission": "string",  # Custom Log & Report permission.
    "utmgrp-permission": "string",  # Custom Security Profile permissions.
    "secfabgrp-permission": "string",  # Custom Security Fabric permissions.
    "admintimeout-override": "option",  # Enable/disable overriding the global administrator idle time
    "admintimeout": "integer",  # Administrator timeout for this access profile (0 - 480 min, 
    "cli-diagnose": "option",  # Enable/disable permission to run diagnostic commands.
    "cli-get": "option",  # Enable/disable permission to run get commands.
    "cli-show": "option",  # Enable/disable permission to run show commands.
    "cli-exec": "option",  # Enable/disable permission to run execute commands.
    "cli-config": "option",  # Enable/disable permission to run config commands.
    "system-execute-ssh": "option",  # Enable/disable permission to execute SSH commands.
    "system-execute-telnet": "option",  # Enable/disable permission to execute TELNET commands.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "scope": "Scope of admin access: global or specific VDOM(s).",
    "comments": "Comment.",
    "secfabgrp": "Security Fabric.",
    "ftviewgrp": "FortiView.",
    "authgrp": "Administrator access to Users and Devices.",
    "sysgrp": "System Configuration.",
    "netgrp": "Network Configuration.",
    "loggrp": "Administrator access to Logging and Reporting including viewing log messages.",
    "fwgrp": "Administrator access to the Firewall configuration.",
    "vpngrp": "Administrator access to IPsec, SSL, PPTP, and L2TP VPN.",
    "utmgrp": "Administrator access to Security Profiles.",
    "wanoptgrp": "Administrator access to WAN Opt & Cache.",
    "wifi": "Administrator access to the WiFi controller and Switch controller.",
    "netgrp-permission": "Custom network permission.",
    "sysgrp-permission": "Custom system permission.",
    "fwgrp-permission": "Custom firewall permission.",
    "loggrp-permission": "Custom Log & Report permission.",
    "utmgrp-permission": "Custom Security Profile permissions.",
    "secfabgrp-permission": "Custom Security Fabric permissions.",
    "admintimeout-override": "Enable/disable overriding the global administrator idle timeout.",
    "admintimeout": "Administrator timeout for this access profile (0 - 480 min, default = 10, 0 means never timeout).",
    "cli-diagnose": "Enable/disable permission to run diagnostic commands.",
    "cli-get": "Enable/disable permission to run get commands.",
    "cli-show": "Enable/disable permission to run show commands.",
    "cli-exec": "Enable/disable permission to run execute commands.",
    "cli-config": "Enable/disable permission to run config commands.",
    "system-execute-ssh": "Enable/disable permission to execute SSH commands.",
    "system-execute-telnet": "Enable/disable permission to execute TELNET commands.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "admintimeout": {"type": "integer", "min": 1, "max": 480},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "netgrp-permission": {
        "cfg": {
            "type": "option",
            "help": "Network Configuration.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "packet-capture": {
            "type": "option",
            "help": "Packet Capture Configuration.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "route-cfg": {
            "type": "option",
            "help": "Router Configuration.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
    },
    "sysgrp-permission": {
        "admin": {
            "type": "option",
            "help": "Administrator Users.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "upd": {
            "type": "option",
            "help": "FortiGuard Updates.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "cfg": {
            "type": "option",
            "help": "System Configuration.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "mnt": {
            "type": "option",
            "help": "Maintenance.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
    },
    "fwgrp-permission": {
        "policy": {
            "type": "option",
            "help": "Policy Configuration.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "address": {
            "type": "option",
            "help": "Address Configuration.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "service": {
            "type": "option",
            "help": "Service Configuration.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "schedule": {
            "type": "option",
            "help": "Schedule Configuration.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "others": {
            "type": "option",
            "help": "Other Firewall Configuration.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
    },
    "loggrp-permission": {
        "config": {
            "type": "option",
            "help": "Log & Report configuration.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "data-access": {
            "type": "option",
            "help": "Log & Report Data Access.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "report-access": {
            "type": "option",
            "help": "Log & Report Report Access.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "threat-weight": {
            "type": "option",
            "help": "Log & Report Threat Weight.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
    },
    "utmgrp-permission": {
        "antivirus": {
            "type": "option",
            "help": "Antivirus profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "ips": {
            "type": "option",
            "help": "IPS profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "webfilter": {
            "type": "option",
            "help": "Web Filter profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "emailfilter": {
            "type": "option",
            "help": "Email Filter and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "dlp": {
            "type": "option",
            "help": "DLP profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "file-filter": {
            "type": "option",
            "help": "File-filter profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "application-control": {
            "type": "option",
            "help": "Application Control profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "icap": {
            "type": "option",
            "help": "ICAP profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "voip": {
            "type": "option",
            "help": "VoIP profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "waf": {
            "type": "option",
            "help": "Web Application Firewall profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "dnsfilter": {
            "type": "option",
            "help": "DNS Filter profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "endpoint-control": {
            "type": "option",
            "help": "FortiClient Profiles.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "videofilter": {
            "type": "option",
            "help": "Video filter profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "virtual-patch": {
            "type": "option",
            "help": "Virtual patch profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "casb": {
            "type": "option",
            "help": "Inline CASB filter profile and settings",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "telemetry": {
            "type": "option",
            "help": "Telemetry profile and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
    },
    "secfabgrp-permission": {
        "csfsys": {
            "type": "option",
            "help": "Security Fabric system profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
        "csffoo": {
            "type": "option",
            "help": "Fabric Overlay Orchestrator profiles and settings.",
            "default": "none",
            "options": [{"help": "No access.", "label": "None", "name": "none"}, {"help": "Read access.", "label": "Read", "name": "read"}, {"help": "Read/write access.", "label": "Read Write", "name": "read-write"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_SCOPE = [
    "vdom",  # VDOM access.
    "global",  # Global access.
]
VALID_BODY_SECFABGRP = [
    "none",  # No access.
    "read",  # Read access.
    "read-write",  # Read/write access.
    "custom",  # Customized access.
]
VALID_BODY_FTVIEWGRP = [
    "none",  # No access.
    "read",  # Read access.
    "read-write",  # Read/write access.
]
VALID_BODY_AUTHGRP = [
    "none",  # No access.
    "read",  # Read access.
    "read-write",  # Read/write access.
]
VALID_BODY_SYSGRP = [
    "none",  # No access.
    "read",  # Read access.
    "read-write",  # Read/write access.
    "custom",  # Customized access.
]
VALID_BODY_NETGRP = [
    "none",  # No access.
    "read",  # Read access.
    "read-write",  # Read/write access.
    "custom",  # Customized access.
]
VALID_BODY_LOGGRP = [
    "none",  # No access.
    "read",  # Read access.
    "read-write",  # Read/write access.
    "custom",  # Customized access.
]
VALID_BODY_FWGRP = [
    "none",  # No access.
    "read",  # Read access.
    "read-write",  # Read/write access.
    "custom",  # Customized access.
]
VALID_BODY_VPNGRP = [
    "none",  # No access.
    "read",  # Read access.
    "read-write",  # Read/write access.
]
VALID_BODY_UTMGRP = [
    "none",  # No access.
    "read",  # Read access.
    "read-write",  # Read/write access.
    "custom",  # Customized access.
]
VALID_BODY_WANOPTGRP = [
    "none",  # No access.
    "read",  # Read access.
    "read-write",  # Read/write access.
]
VALID_BODY_WIFI = [
    "none",  # No access.
    "read",  # Read access.
    "read-write",  # Read/write access.
]
VALID_BODY_ADMINTIMEOUT_OVERRIDE = [
    "enable",  # Enable overriding the global administrator idle timeout.
    "disable",  # Disable overriding the global administrator idle timeout.
]
VALID_BODY_CLI_DIAGNOSE = [
    "enable",  # Enable permission to run diagnostic commands.
    "disable",  # Disable permission to run diagnostic commands.
]
VALID_BODY_CLI_GET = [
    "enable",  # Enable permission to run get commands.
    "disable",  # Disable permission to run get commands.
]
VALID_BODY_CLI_SHOW = [
    "enable",  # Enable permission to run show commands.
    "disable",  # Disable permission to run show commands.
]
VALID_BODY_CLI_EXEC = [
    "enable",  # Enable permission to run execute commands.
    "disable",  # Disable permission to run execute commands.
]
VALID_BODY_CLI_CONFIG = [
    "enable",  # Enable permission to run config commands.
    "disable",  # Disable permission to run config commands.
]
VALID_BODY_SYSTEM_EXECUTE_SSH = [
    "enable",  # Enable permission to execute SSH commands.
    "disable",  # Disable permission to execute SSH commands.
]
VALID_BODY_SYSTEM_EXECUTE_TELNET = [
    "enable",  # Enable permission to execute TELNET commands.
    "disable",  # Disable permission to execute TELNET commands.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_accprofile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/accprofile.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_accprofile_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_system_accprofile_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_accprofile_get(
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
    Validate required fields for system/accprofile.

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


def validate_system_accprofile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/accprofile object.

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
        ...     "name": True,  # Profile name.
        ... }
        >>> is_valid, error = validate_system_accprofile_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "name": True,
        ...     "scope": "{'name': 'vdom', 'help': 'VDOM access.', 'label': 'Vdom', 'description': 'VDOM access'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_accprofile_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["scope"] = "invalid-value"
        >>> is_valid, error = validate_system_accprofile_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_accprofile_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "scope" in payload:
        value = payload["scope"]
        if value not in VALID_BODY_SCOPE:
            desc = FIELD_DESCRIPTIONS.get("scope", "")
            error_msg = f"Invalid value for 'scope': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCOPE)}"
            error_msg += f"\n  → Example: scope='{{ VALID_BODY_SCOPE[0] }}'"
            return (False, error_msg)
    if "secfabgrp" in payload:
        value = payload["secfabgrp"]
        if value not in VALID_BODY_SECFABGRP:
            desc = FIELD_DESCRIPTIONS.get("secfabgrp", "")
            error_msg = f"Invalid value for 'secfabgrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECFABGRP)}"
            error_msg += f"\n  → Example: secfabgrp='{{ VALID_BODY_SECFABGRP[0] }}'"
            return (False, error_msg)
    if "ftviewgrp" in payload:
        value = payload["ftviewgrp"]
        if value not in VALID_BODY_FTVIEWGRP:
            desc = FIELD_DESCRIPTIONS.get("ftviewgrp", "")
            error_msg = f"Invalid value for 'ftviewgrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FTVIEWGRP)}"
            error_msg += f"\n  → Example: ftviewgrp='{{ VALID_BODY_FTVIEWGRP[0] }}'"
            return (False, error_msg)
    if "authgrp" in payload:
        value = payload["authgrp"]
        if value not in VALID_BODY_AUTHGRP:
            desc = FIELD_DESCRIPTIONS.get("authgrp", "")
            error_msg = f"Invalid value for 'authgrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHGRP)}"
            error_msg += f"\n  → Example: authgrp='{{ VALID_BODY_AUTHGRP[0] }}'"
            return (False, error_msg)
    if "sysgrp" in payload:
        value = payload["sysgrp"]
        if value not in VALID_BODY_SYSGRP:
            desc = FIELD_DESCRIPTIONS.get("sysgrp", "")
            error_msg = f"Invalid value for 'sysgrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYSGRP)}"
            error_msg += f"\n  → Example: sysgrp='{{ VALID_BODY_SYSGRP[0] }}'"
            return (False, error_msg)
    if "netgrp" in payload:
        value = payload["netgrp"]
        if value not in VALID_BODY_NETGRP:
            desc = FIELD_DESCRIPTIONS.get("netgrp", "")
            error_msg = f"Invalid value for 'netgrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NETGRP)}"
            error_msg += f"\n  → Example: netgrp='{{ VALID_BODY_NETGRP[0] }}'"
            return (False, error_msg)
    if "loggrp" in payload:
        value = payload["loggrp"]
        if value not in VALID_BODY_LOGGRP:
            desc = FIELD_DESCRIPTIONS.get("loggrp", "")
            error_msg = f"Invalid value for 'loggrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGGRP)}"
            error_msg += f"\n  → Example: loggrp='{{ VALID_BODY_LOGGRP[0] }}'"
            return (False, error_msg)
    if "fwgrp" in payload:
        value = payload["fwgrp"]
        if value not in VALID_BODY_FWGRP:
            desc = FIELD_DESCRIPTIONS.get("fwgrp", "")
            error_msg = f"Invalid value for 'fwgrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FWGRP)}"
            error_msg += f"\n  → Example: fwgrp='{{ VALID_BODY_FWGRP[0] }}'"
            return (False, error_msg)
    if "vpngrp" in payload:
        value = payload["vpngrp"]
        if value not in VALID_BODY_VPNGRP:
            desc = FIELD_DESCRIPTIONS.get("vpngrp", "")
            error_msg = f"Invalid value for 'vpngrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VPNGRP)}"
            error_msg += f"\n  → Example: vpngrp='{{ VALID_BODY_VPNGRP[0] }}'"
            return (False, error_msg)
    if "utmgrp" in payload:
        value = payload["utmgrp"]
        if value not in VALID_BODY_UTMGRP:
            desc = FIELD_DESCRIPTIONS.get("utmgrp", "")
            error_msg = f"Invalid value for 'utmgrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UTMGRP)}"
            error_msg += f"\n  → Example: utmgrp='{{ VALID_BODY_UTMGRP[0] }}'"
            return (False, error_msg)
    if "wanoptgrp" in payload:
        value = payload["wanoptgrp"]
        if value not in VALID_BODY_WANOPTGRP:
            desc = FIELD_DESCRIPTIONS.get("wanoptgrp", "")
            error_msg = f"Invalid value for 'wanoptgrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WANOPTGRP)}"
            error_msg += f"\n  → Example: wanoptgrp='{{ VALID_BODY_WANOPTGRP[0] }}'"
            return (False, error_msg)
    if "wifi" in payload:
        value = payload["wifi"]
        if value not in VALID_BODY_WIFI:
            desc = FIELD_DESCRIPTIONS.get("wifi", "")
            error_msg = f"Invalid value for 'wifi': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WIFI)}"
            error_msg += f"\n  → Example: wifi='{{ VALID_BODY_WIFI[0] }}'"
            return (False, error_msg)
    if "admintimeout-override" in payload:
        value = payload["admintimeout-override"]
        if value not in VALID_BODY_ADMINTIMEOUT_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("admintimeout-override", "")
            error_msg = f"Invalid value for 'admintimeout-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMINTIMEOUT_OVERRIDE)}"
            error_msg += f"\n  → Example: admintimeout-override='{{ VALID_BODY_ADMINTIMEOUT_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "cli-diagnose" in payload:
        value = payload["cli-diagnose"]
        if value not in VALID_BODY_CLI_DIAGNOSE:
            desc = FIELD_DESCRIPTIONS.get("cli-diagnose", "")
            error_msg = f"Invalid value for 'cli-diagnose': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLI_DIAGNOSE)}"
            error_msg += f"\n  → Example: cli-diagnose='{{ VALID_BODY_CLI_DIAGNOSE[0] }}'"
            return (False, error_msg)
    if "cli-get" in payload:
        value = payload["cli-get"]
        if value not in VALID_BODY_CLI_GET:
            desc = FIELD_DESCRIPTIONS.get("cli-get", "")
            error_msg = f"Invalid value for 'cli-get': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLI_GET)}"
            error_msg += f"\n  → Example: cli-get='{{ VALID_BODY_CLI_GET[0] }}'"
            return (False, error_msg)
    if "cli-show" in payload:
        value = payload["cli-show"]
        if value not in VALID_BODY_CLI_SHOW:
            desc = FIELD_DESCRIPTIONS.get("cli-show", "")
            error_msg = f"Invalid value for 'cli-show': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLI_SHOW)}"
            error_msg += f"\n  → Example: cli-show='{{ VALID_BODY_CLI_SHOW[0] }}'"
            return (False, error_msg)
    if "cli-exec" in payload:
        value = payload["cli-exec"]
        if value not in VALID_BODY_CLI_EXEC:
            desc = FIELD_DESCRIPTIONS.get("cli-exec", "")
            error_msg = f"Invalid value for 'cli-exec': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLI_EXEC)}"
            error_msg += f"\n  → Example: cli-exec='{{ VALID_BODY_CLI_EXEC[0] }}'"
            return (False, error_msg)
    if "cli-config" in payload:
        value = payload["cli-config"]
        if value not in VALID_BODY_CLI_CONFIG:
            desc = FIELD_DESCRIPTIONS.get("cli-config", "")
            error_msg = f"Invalid value for 'cli-config': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLI_CONFIG)}"
            error_msg += f"\n  → Example: cli-config='{{ VALID_BODY_CLI_CONFIG[0] }}'"
            return (False, error_msg)
    if "system-execute-ssh" in payload:
        value = payload["system-execute-ssh"]
        if value not in VALID_BODY_SYSTEM_EXECUTE_SSH:
            desc = FIELD_DESCRIPTIONS.get("system-execute-ssh", "")
            error_msg = f"Invalid value for 'system-execute-ssh': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYSTEM_EXECUTE_SSH)}"
            error_msg += f"\n  → Example: system-execute-ssh='{{ VALID_BODY_SYSTEM_EXECUTE_SSH[0] }}'"
            return (False, error_msg)
    if "system-execute-telnet" in payload:
        value = payload["system-execute-telnet"]
        if value not in VALID_BODY_SYSTEM_EXECUTE_TELNET:
            desc = FIELD_DESCRIPTIONS.get("system-execute-telnet", "")
            error_msg = f"Invalid value for 'system-execute-telnet': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYSTEM_EXECUTE_TELNET)}"
            error_msg += f"\n  → Example: system-execute-telnet='{{ VALID_BODY_SYSTEM_EXECUTE_TELNET[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_accprofile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/accprofile.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_accprofile_put(payload)
    """
    # Step 1: Validate enum values
    if "scope" in payload:
        value = payload["scope"]
        if value not in VALID_BODY_SCOPE:
            return (
                False,
                f"Invalid value for 'scope'='{value}'. Must be one of: {', '.join(VALID_BODY_SCOPE)}",
            )
    if "secfabgrp" in payload:
        value = payload["secfabgrp"]
        if value not in VALID_BODY_SECFABGRP:
            return (
                False,
                f"Invalid value for 'secfabgrp'='{value}'. Must be one of: {', '.join(VALID_BODY_SECFABGRP)}",
            )
    if "ftviewgrp" in payload:
        value = payload["ftviewgrp"]
        if value not in VALID_BODY_FTVIEWGRP:
            return (
                False,
                f"Invalid value for 'ftviewgrp'='{value}'. Must be one of: {', '.join(VALID_BODY_FTVIEWGRP)}",
            )
    if "authgrp" in payload:
        value = payload["authgrp"]
        if value not in VALID_BODY_AUTHGRP:
            return (
                False,
                f"Invalid value for 'authgrp'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHGRP)}",
            )
    if "sysgrp" in payload:
        value = payload["sysgrp"]
        if value not in VALID_BODY_SYSGRP:
            return (
                False,
                f"Invalid value for 'sysgrp'='{value}'. Must be one of: {', '.join(VALID_BODY_SYSGRP)}",
            )
    if "netgrp" in payload:
        value = payload["netgrp"]
        if value not in VALID_BODY_NETGRP:
            return (
                False,
                f"Invalid value for 'netgrp'='{value}'. Must be one of: {', '.join(VALID_BODY_NETGRP)}",
            )
    if "loggrp" in payload:
        value = payload["loggrp"]
        if value not in VALID_BODY_LOGGRP:
            return (
                False,
                f"Invalid value for 'loggrp'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGGRP)}",
            )
    if "fwgrp" in payload:
        value = payload["fwgrp"]
        if value not in VALID_BODY_FWGRP:
            return (
                False,
                f"Invalid value for 'fwgrp'='{value}'. Must be one of: {', '.join(VALID_BODY_FWGRP)}",
            )
    if "vpngrp" in payload:
        value = payload["vpngrp"]
        if value not in VALID_BODY_VPNGRP:
            return (
                False,
                f"Invalid value for 'vpngrp'='{value}'. Must be one of: {', '.join(VALID_BODY_VPNGRP)}",
            )
    if "utmgrp" in payload:
        value = payload["utmgrp"]
        if value not in VALID_BODY_UTMGRP:
            return (
                False,
                f"Invalid value for 'utmgrp'='{value}'. Must be one of: {', '.join(VALID_BODY_UTMGRP)}",
            )
    if "wanoptgrp" in payload:
        value = payload["wanoptgrp"]
        if value not in VALID_BODY_WANOPTGRP:
            return (
                False,
                f"Invalid value for 'wanoptgrp'='{value}'. Must be one of: {', '.join(VALID_BODY_WANOPTGRP)}",
            )
    if "wifi" in payload:
        value = payload["wifi"]
        if value not in VALID_BODY_WIFI:
            return (
                False,
                f"Invalid value for 'wifi'='{value}'. Must be one of: {', '.join(VALID_BODY_WIFI)}",
            )
    if "admintimeout-override" in payload:
        value = payload["admintimeout-override"]
        if value not in VALID_BODY_ADMINTIMEOUT_OVERRIDE:
            return (
                False,
                f"Invalid value for 'admintimeout-override'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMINTIMEOUT_OVERRIDE)}",
            )
    if "cli-diagnose" in payload:
        value = payload["cli-diagnose"]
        if value not in VALID_BODY_CLI_DIAGNOSE:
            return (
                False,
                f"Invalid value for 'cli-diagnose'='{value}'. Must be one of: {', '.join(VALID_BODY_CLI_DIAGNOSE)}",
            )
    if "cli-get" in payload:
        value = payload["cli-get"]
        if value not in VALID_BODY_CLI_GET:
            return (
                False,
                f"Invalid value for 'cli-get'='{value}'. Must be one of: {', '.join(VALID_BODY_CLI_GET)}",
            )
    if "cli-show" in payload:
        value = payload["cli-show"]
        if value not in VALID_BODY_CLI_SHOW:
            return (
                False,
                f"Invalid value for 'cli-show'='{value}'. Must be one of: {', '.join(VALID_BODY_CLI_SHOW)}",
            )
    if "cli-exec" in payload:
        value = payload["cli-exec"]
        if value not in VALID_BODY_CLI_EXEC:
            return (
                False,
                f"Invalid value for 'cli-exec'='{value}'. Must be one of: {', '.join(VALID_BODY_CLI_EXEC)}",
            )
    if "cli-config" in payload:
        value = payload["cli-config"]
        if value not in VALID_BODY_CLI_CONFIG:
            return (
                False,
                f"Invalid value for 'cli-config'='{value}'. Must be one of: {', '.join(VALID_BODY_CLI_CONFIG)}",
            )
    if "system-execute-ssh" in payload:
        value = payload["system-execute-ssh"]
        if value not in VALID_BODY_SYSTEM_EXECUTE_SSH:
            return (
                False,
                f"Invalid value for 'system-execute-ssh'='{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_EXECUTE_SSH)}",
            )
    if "system-execute-telnet" in payload:
        value = payload["system-execute-telnet"]
        if value not in VALID_BODY_SYSTEM_EXECUTE_TELNET:
            return (
                False,
                f"Invalid value for 'system-execute-telnet'='{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_EXECUTE_TELNET)}",
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
    "endpoint": "system/accprofile",
    "category": "cmdb",
    "api_path": "system/accprofile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure access profiles for system administrators.",
    "total_fields": 29,
    "required_fields_count": 1,
    "fields_with_defaults_count": 22,
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
