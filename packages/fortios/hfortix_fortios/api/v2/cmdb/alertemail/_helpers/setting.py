"""
Validation helpers for alertemail/setting endpoint.

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
    "username": "",
    "mailto1": "",
    "mailto2": "",
    "mailto3": "",
    "filter-mode": "category",
    "email-interval": 5,
    "IPS-logs": "disable",
    "firewall-authentication-failure-logs": "disable",
    "HA-logs": "disable",
    "IPsec-errors-logs": "disable",
    "FDS-update-logs": "disable",
    "PPP-errors-logs": "disable",
    "sslvpn-authentication-errors-logs": "disable",
    "antivirus-logs": "disable",
    "webfilter-logs": "disable",
    "configuration-changes-logs": "disable",
    "violation-traffic-logs": "disable",
    "admin-login-logs": "disable",
    "FDS-license-expiring-warning": "disable",
    "log-disk-usage-warning": "disable",
    "fortiguard-log-quota-warning": "disable",
    "amc-interface-bypass-mode": "disable",
    "FIPS-CC-errors": "disable",
    "FSSO-disconnect-logs": "disable",
    "ssh-logs": "disable",
    "local-disk-usage": 75,
    "emergency-interval": 1,
    "alert-interval": 2,
    "critical-interval": 3,
    "error-interval": 5,
    "warning-interval": 10,
    "notification-interval": 20,
    "information-interval": 30,
    "debug-interval": 60,
    "severity": "alert",
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
    "username": "string",  # Name that appears in the From: field of alert emails (max. 6
    "mailto1": "string",  # Email address to send alert email to (usually a system admin
    "mailto2": "string",  # Optional second email address to send alert email to (max. 6
    "mailto3": "string",  # Optional third email address to send alert email to (max. 63
    "filter-mode": "option",  # How to filter log messages that are sent to alert emails.
    "email-interval": "integer",  # Interval between sending alert emails (1 - 99999 min, defaul
    "IPS-logs": "option",  # Enable/disable IPS logs in alert email.
    "firewall-authentication-failure-logs": "option",  # Enable/disable firewall authentication failure logs in alert
    "HA-logs": "option",  # Enable/disable HA logs in alert email.
    "IPsec-errors-logs": "option",  # Enable/disable IPsec error logs in alert email.
    "FDS-update-logs": "option",  # Enable/disable FortiGuard update logs in alert email.
    "PPP-errors-logs": "option",  # Enable/disable PPP error logs in alert email.
    "sslvpn-authentication-errors-logs": "option",  # Enable/disable Agentless VPN authentication error logs in al
    "antivirus-logs": "option",  # Enable/disable antivirus logs in alert email.
    "webfilter-logs": "option",  # Enable/disable web filter logs in alert email.
    "configuration-changes-logs": "option",  # Enable/disable configuration change logs in alert email.
    "violation-traffic-logs": "option",  # Enable/disable violation traffic logs in alert email.
    "admin-login-logs": "option",  # Enable/disable administrator login/logout logs in alert emai
    "FDS-license-expiring-warning": "option",  # Enable/disable FortiGuard license expiration warnings in ale
    "log-disk-usage-warning": "option",  # Enable/disable disk usage warnings in alert email.
    "fortiguard-log-quota-warning": "option",  # Enable/disable FortiCloud log quota warnings in alert email.
    "amc-interface-bypass-mode": "option",  # Enable/disable Fortinet Advanced Mezzanine Card (AMC) interf
    "FIPS-CC-errors": "option",  # Enable/disable FIPS and Common Criteria error logs in alert 
    "FSSO-disconnect-logs": "option",  # Enable/disable logging of FSSO collector agent disconnect.
    "ssh-logs": "option",  # Enable/disable SSH logs in alert email.
    "local-disk-usage": "integer",  # Disk usage percentage at which to send alert email (1 - 99 p
    "emergency-interval": "integer",  # Emergency alert interval in minutes.
    "alert-interval": "integer",  # Alert alert interval in minutes.
    "critical-interval": "integer",  # Critical alert interval in minutes.
    "error-interval": "integer",  # Error alert interval in minutes.
    "warning-interval": "integer",  # Warning alert interval in minutes.
    "notification-interval": "integer",  # Notification alert interval in minutes.
    "information-interval": "integer",  # Information alert interval in minutes.
    "debug-interval": "integer",  # Debug alert interval in minutes.
    "severity": "option",  # Lowest severity level to log.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "username": "Name that appears in the From: field of alert emails (max. 63 characters).",
    "mailto1": "Email address to send alert email to (usually a system administrator) (max. 63 characters).",
    "mailto2": "Optional second email address to send alert email to (max. 63 characters).",
    "mailto3": "Optional third email address to send alert email to (max. 63 characters).",
    "filter-mode": "How to filter log messages that are sent to alert emails.",
    "email-interval": "Interval between sending alert emails (1 - 99999 min, default = 5).",
    "IPS-logs": "Enable/disable IPS logs in alert email.",
    "firewall-authentication-failure-logs": "Enable/disable firewall authentication failure logs in alert email.",
    "HA-logs": "Enable/disable HA logs in alert email.",
    "IPsec-errors-logs": "Enable/disable IPsec error logs in alert email.",
    "FDS-update-logs": "Enable/disable FortiGuard update logs in alert email.",
    "PPP-errors-logs": "Enable/disable PPP error logs in alert email.",
    "sslvpn-authentication-errors-logs": "Enable/disable Agentless VPN authentication error logs in alert email.",
    "antivirus-logs": "Enable/disable antivirus logs in alert email.",
    "webfilter-logs": "Enable/disable web filter logs in alert email.",
    "configuration-changes-logs": "Enable/disable configuration change logs in alert email.",
    "violation-traffic-logs": "Enable/disable violation traffic logs in alert email.",
    "admin-login-logs": "Enable/disable administrator login/logout logs in alert email.",
    "FDS-license-expiring-warning": "Enable/disable FortiGuard license expiration warnings in alert email.",
    "log-disk-usage-warning": "Enable/disable disk usage warnings in alert email.",
    "fortiguard-log-quota-warning": "Enable/disable FortiCloud log quota warnings in alert email.",
    "amc-interface-bypass-mode": "Enable/disable Fortinet Advanced Mezzanine Card (AMC) interface bypass mode logs in alert email.",
    "FIPS-CC-errors": "Enable/disable FIPS and Common Criteria error logs in alert email.",
    "FSSO-disconnect-logs": "Enable/disable logging of FSSO collector agent disconnect.",
    "ssh-logs": "Enable/disable SSH logs in alert email.",
    "local-disk-usage": "Disk usage percentage at which to send alert email (1 - 99 percent, default = 75).",
    "emergency-interval": "Emergency alert interval in minutes.",
    "alert-interval": "Alert alert interval in minutes.",
    "critical-interval": "Critical alert interval in minutes.",
    "error-interval": "Error alert interval in minutes.",
    "warning-interval": "Warning alert interval in minutes.",
    "notification-interval": "Notification alert interval in minutes.",
    "information-interval": "Information alert interval in minutes.",
    "debug-interval": "Debug alert interval in minutes.",
    "severity": "Lowest severity level to log.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "username": {"type": "string", "max_length": 63},
    "mailto1": {"type": "string", "max_length": 63},
    "mailto2": {"type": "string", "max_length": 63},
    "mailto3": {"type": "string", "max_length": 63},
    "email-interval": {"type": "integer", "min": 1, "max": 99999},
    "local-disk-usage": {"type": "integer", "min": 1, "max": 99},
    "emergency-interval": {"type": "integer", "min": 1, "max": 99999},
    "alert-interval": {"type": "integer", "min": 1, "max": 99999},
    "critical-interval": {"type": "integer", "min": 1, "max": 99999},
    "error-interval": {"type": "integer", "min": 1, "max": 99999},
    "warning-interval": {"type": "integer", "min": 1, "max": 99999},
    "notification-interval": {"type": "integer", "min": 1, "max": 99999},
    "information-interval": {"type": "integer", "min": 1, "max": 99999},
    "debug-interval": {"type": "integer", "min": 1, "max": 99999},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_FILTER_MODE = [
    "category",  # Filter based on category.
    "threshold",  # Filter based on severity.
]
VALID_BODY_IPS_LOGS = [
    "enable",  # Enable IPS logs in alert email.
    "disable",  # Disable IPS logs in alert email.
]
VALID_BODY_FIREWALL_AUTHENTICATION_FAILURE_LOGS = [
    "enable",  # Enable firewall authentication failure logs in alert email.
    "disable",  # Disable firewall authentication failure logs in alert email.
]
VALID_BODY_HA_LOGS = [
    "enable",  # Enable HA logs in alert email.
    "disable",  # Disable HA logs in alert email.
]
VALID_BODY_IPSEC_ERRORS_LOGS = [
    "enable",  # Enable IPsec error logs in alert email.
    "disable",  # Disable IPsec error logs in alert email.
]
VALID_BODY_FDS_UPDATE_LOGS = [
    "enable",  # Enable FortiGuard update logs in alert email.
    "disable",  # Disable FortiGuard update logs in alert email.
]
VALID_BODY_PPP_ERRORS_LOGS = [
    "enable",  # Enable PPP error logs in alert email.
    "disable",  # Disable PPP error logs in alert email.
]
VALID_BODY_SSLVPN_AUTHENTICATION_ERRORS_LOGS = [
    "enable",  # Enable Agentless VPN authentication error logs in alert email.
    "disable",  # Disable Agentless VPN authentication error logs in alert email.
]
VALID_BODY_ANTIVIRUS_LOGS = [
    "enable",  # Enable antivirus logs in alert email.
    "disable",  # Disable antivirus logs in alert email.
]
VALID_BODY_WEBFILTER_LOGS = [
    "enable",  # Enable web filter logs in alert email.
    "disable",  # Disable web filter logs in alert email.
]
VALID_BODY_CONFIGURATION_CHANGES_LOGS = [
    "enable",  # Enable configuration change logs in alert email.
    "disable",  # Disable configuration change logs in alert email.
]
VALID_BODY_VIOLATION_TRAFFIC_LOGS = [
    "enable",  # Enable violation traffic logs in alert email.
    "disable",  # Disable violation traffic logs in alert email.
]
VALID_BODY_ADMIN_LOGIN_LOGS = [
    "enable",  # Enable administrator login/logout logs in alert email.
    "disable",  # Disable administrator login/logout logs in alert email.
]
VALID_BODY_FDS_LICENSE_EXPIRING_WARNING = [
    "enable",  # Enable FortiGuard license expiration warnings in alert email.
    "disable",  # Disable FortiGuard license expiration warnings in alert email.
]
VALID_BODY_LOG_DISK_USAGE_WARNING = [
    "enable",  # Enable disk usage warnings in alert email.
    "disable",  # Disable disk usage warnings in alert email.
]
VALID_BODY_FORTIGUARD_LOG_QUOTA_WARNING = [
    "enable",  # Enable FortiCloud log quota warnings in alert email.
    "disable",  # Disable FortiCloud log quota warnings in alert email.
]
VALID_BODY_AMC_INTERFACE_BYPASS_MODE = [
    "enable",  # Enable Fortinet Advanced Mezzanine Card (AMC) interface bypass mode logs in alert email.
    "disable",  # Disable Fortinet Advanced Mezzanine Card (AMC) interface bypass mode logs in alert email.
]
VALID_BODY_FIPS_CC_ERRORS = [
    "enable",  # Enable FIPS and Common Criteria error logs in alert email.
    "disable",  # Disable FIPS and Common Criteria error logs in alert email.
]
VALID_BODY_FSSO_DISCONNECT_LOGS = [
    "enable",  # Enable logging of FSSO collector agent disconnect.
    "disable",  # Disable logging of FSSO collector agent disconnect.
]
VALID_BODY_SSH_LOGS = [
    "enable",  # Enable SSH logs in alert email.
    "disable",  # Disable SSH logs in alert email.
]
VALID_BODY_SEVERITY = [
    "emergency",  # Emergency level.
    "alert",  # Alert level.
    "critical",  # Critical level.
    "error",  # Error level.
    "warning",  # Warning level.
    "notification",  # Notification level.
    "information",  # Information level.
    "debug",  # Debug level.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_alertemail_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for alertemail/setting.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_alertemail_setting_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_alertemail_setting_get(
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
    Validate required fields for alertemail/setting.

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


def validate_alertemail_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new alertemail/setting object.

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
        >>> is_valid, error = validate_alertemail_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "filter-mode": "{'name': 'category', 'help': 'Filter based on category.', 'label': 'Category', 'description': 'Filter based on category'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_alertemail_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["filter-mode"] = "invalid-value"
        >>> is_valid, error = validate_alertemail_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_alertemail_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "filter-mode" in payload:
        value = payload["filter-mode"]
        if value not in VALID_BODY_FILTER_MODE:
            desc = FIELD_DESCRIPTIONS.get("filter-mode", "")
            error_msg = f"Invalid value for 'filter-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FILTER_MODE)}"
            error_msg += f"\n  → Example: filter-mode='{{ VALID_BODY_FILTER_MODE[0] }}'"
            return (False, error_msg)
    if "IPS-logs" in payload:
        value = payload["IPS-logs"]
        if value not in VALID_BODY_IPS_LOGS:
            desc = FIELD_DESCRIPTIONS.get("IPS-logs", "")
            error_msg = f"Invalid value for 'IPS-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPS_LOGS)}"
            error_msg += f"\n  → Example: IPS-logs='{{ VALID_BODY_IPS_LOGS[0] }}'"
            return (False, error_msg)
    if "firewall-authentication-failure-logs" in payload:
        value = payload["firewall-authentication-failure-logs"]
        if value not in VALID_BODY_FIREWALL_AUTHENTICATION_FAILURE_LOGS:
            desc = FIELD_DESCRIPTIONS.get("firewall-authentication-failure-logs", "")
            error_msg = f"Invalid value for 'firewall-authentication-failure-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FIREWALL_AUTHENTICATION_FAILURE_LOGS)}"
            error_msg += f"\n  → Example: firewall-authentication-failure-logs='{{ VALID_BODY_FIREWALL_AUTHENTICATION_FAILURE_LOGS[0] }}'"
            return (False, error_msg)
    if "HA-logs" in payload:
        value = payload["HA-logs"]
        if value not in VALID_BODY_HA_LOGS:
            desc = FIELD_DESCRIPTIONS.get("HA-logs", "")
            error_msg = f"Invalid value for 'HA-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HA_LOGS)}"
            error_msg += f"\n  → Example: HA-logs='{{ VALID_BODY_HA_LOGS[0] }}'"
            return (False, error_msg)
    if "IPsec-errors-logs" in payload:
        value = payload["IPsec-errors-logs"]
        if value not in VALID_BODY_IPSEC_ERRORS_LOGS:
            desc = FIELD_DESCRIPTIONS.get("IPsec-errors-logs", "")
            error_msg = f"Invalid value for 'IPsec-errors-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPSEC_ERRORS_LOGS)}"
            error_msg += f"\n  → Example: IPsec-errors-logs='{{ VALID_BODY_IPSEC_ERRORS_LOGS[0] }}'"
            return (False, error_msg)
    if "FDS-update-logs" in payload:
        value = payload["FDS-update-logs"]
        if value not in VALID_BODY_FDS_UPDATE_LOGS:
            desc = FIELD_DESCRIPTIONS.get("FDS-update-logs", "")
            error_msg = f"Invalid value for 'FDS-update-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FDS_UPDATE_LOGS)}"
            error_msg += f"\n  → Example: FDS-update-logs='{{ VALID_BODY_FDS_UPDATE_LOGS[0] }}'"
            return (False, error_msg)
    if "PPP-errors-logs" in payload:
        value = payload["PPP-errors-logs"]
        if value not in VALID_BODY_PPP_ERRORS_LOGS:
            desc = FIELD_DESCRIPTIONS.get("PPP-errors-logs", "")
            error_msg = f"Invalid value for 'PPP-errors-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PPP_ERRORS_LOGS)}"
            error_msg += f"\n  → Example: PPP-errors-logs='{{ VALID_BODY_PPP_ERRORS_LOGS[0] }}'"
            return (False, error_msg)
    if "sslvpn-authentication-errors-logs" in payload:
        value = payload["sslvpn-authentication-errors-logs"]
        if value not in VALID_BODY_SSLVPN_AUTHENTICATION_ERRORS_LOGS:
            desc = FIELD_DESCRIPTIONS.get("sslvpn-authentication-errors-logs", "")
            error_msg = f"Invalid value for 'sslvpn-authentication-errors-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSLVPN_AUTHENTICATION_ERRORS_LOGS)}"
            error_msg += f"\n  → Example: sslvpn-authentication-errors-logs='{{ VALID_BODY_SSLVPN_AUTHENTICATION_ERRORS_LOGS[0] }}'"
            return (False, error_msg)
    if "antivirus-logs" in payload:
        value = payload["antivirus-logs"]
        if value not in VALID_BODY_ANTIVIRUS_LOGS:
            desc = FIELD_DESCRIPTIONS.get("antivirus-logs", "")
            error_msg = f"Invalid value for 'antivirus-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ANTIVIRUS_LOGS)}"
            error_msg += f"\n  → Example: antivirus-logs='{{ VALID_BODY_ANTIVIRUS_LOGS[0] }}'"
            return (False, error_msg)
    if "webfilter-logs" in payload:
        value = payload["webfilter-logs"]
        if value not in VALID_BODY_WEBFILTER_LOGS:
            desc = FIELD_DESCRIPTIONS.get("webfilter-logs", "")
            error_msg = f"Invalid value for 'webfilter-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEBFILTER_LOGS)}"
            error_msg += f"\n  → Example: webfilter-logs='{{ VALID_BODY_WEBFILTER_LOGS[0] }}'"
            return (False, error_msg)
    if "configuration-changes-logs" in payload:
        value = payload["configuration-changes-logs"]
        if value not in VALID_BODY_CONFIGURATION_CHANGES_LOGS:
            desc = FIELD_DESCRIPTIONS.get("configuration-changes-logs", "")
            error_msg = f"Invalid value for 'configuration-changes-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CONFIGURATION_CHANGES_LOGS)}"
            error_msg += f"\n  → Example: configuration-changes-logs='{{ VALID_BODY_CONFIGURATION_CHANGES_LOGS[0] }}'"
            return (False, error_msg)
    if "violation-traffic-logs" in payload:
        value = payload["violation-traffic-logs"]
        if value not in VALID_BODY_VIOLATION_TRAFFIC_LOGS:
            desc = FIELD_DESCRIPTIONS.get("violation-traffic-logs", "")
            error_msg = f"Invalid value for 'violation-traffic-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VIOLATION_TRAFFIC_LOGS)}"
            error_msg += f"\n  → Example: violation-traffic-logs='{{ VALID_BODY_VIOLATION_TRAFFIC_LOGS[0] }}'"
            return (False, error_msg)
    if "admin-login-logs" in payload:
        value = payload["admin-login-logs"]
        if value not in VALID_BODY_ADMIN_LOGIN_LOGS:
            desc = FIELD_DESCRIPTIONS.get("admin-login-logs", "")
            error_msg = f"Invalid value for 'admin-login-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_LOGIN_LOGS)}"
            error_msg += f"\n  → Example: admin-login-logs='{{ VALID_BODY_ADMIN_LOGIN_LOGS[0] }}'"
            return (False, error_msg)
    if "FDS-license-expiring-warning" in payload:
        value = payload["FDS-license-expiring-warning"]
        if value not in VALID_BODY_FDS_LICENSE_EXPIRING_WARNING:
            desc = FIELD_DESCRIPTIONS.get("FDS-license-expiring-warning", "")
            error_msg = f"Invalid value for 'FDS-license-expiring-warning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FDS_LICENSE_EXPIRING_WARNING)}"
            error_msg += f"\n  → Example: FDS-license-expiring-warning='{{ VALID_BODY_FDS_LICENSE_EXPIRING_WARNING[0] }}'"
            return (False, error_msg)
    if "log-disk-usage-warning" in payload:
        value = payload["log-disk-usage-warning"]
        if value not in VALID_BODY_LOG_DISK_USAGE_WARNING:
            desc = FIELD_DESCRIPTIONS.get("log-disk-usage-warning", "")
            error_msg = f"Invalid value for 'log-disk-usage-warning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_DISK_USAGE_WARNING)}"
            error_msg += f"\n  → Example: log-disk-usage-warning='{{ VALID_BODY_LOG_DISK_USAGE_WARNING[0] }}'"
            return (False, error_msg)
    if "fortiguard-log-quota-warning" in payload:
        value = payload["fortiguard-log-quota-warning"]
        if value not in VALID_BODY_FORTIGUARD_LOG_QUOTA_WARNING:
            desc = FIELD_DESCRIPTIONS.get("fortiguard-log-quota-warning", "")
            error_msg = f"Invalid value for 'fortiguard-log-quota-warning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTIGUARD_LOG_QUOTA_WARNING)}"
            error_msg += f"\n  → Example: fortiguard-log-quota-warning='{{ VALID_BODY_FORTIGUARD_LOG_QUOTA_WARNING[0] }}'"
            return (False, error_msg)
    if "amc-interface-bypass-mode" in payload:
        value = payload["amc-interface-bypass-mode"]
        if value not in VALID_BODY_AMC_INTERFACE_BYPASS_MODE:
            desc = FIELD_DESCRIPTIONS.get("amc-interface-bypass-mode", "")
            error_msg = f"Invalid value for 'amc-interface-bypass-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AMC_INTERFACE_BYPASS_MODE)}"
            error_msg += f"\n  → Example: amc-interface-bypass-mode='{{ VALID_BODY_AMC_INTERFACE_BYPASS_MODE[0] }}'"
            return (False, error_msg)
    if "FIPS-CC-errors" in payload:
        value = payload["FIPS-CC-errors"]
        if value not in VALID_BODY_FIPS_CC_ERRORS:
            desc = FIELD_DESCRIPTIONS.get("FIPS-CC-errors", "")
            error_msg = f"Invalid value for 'FIPS-CC-errors': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FIPS_CC_ERRORS)}"
            error_msg += f"\n  → Example: FIPS-CC-errors='{{ VALID_BODY_FIPS_CC_ERRORS[0] }}'"
            return (False, error_msg)
    if "FSSO-disconnect-logs" in payload:
        value = payload["FSSO-disconnect-logs"]
        if value not in VALID_BODY_FSSO_DISCONNECT_LOGS:
            desc = FIELD_DESCRIPTIONS.get("FSSO-disconnect-logs", "")
            error_msg = f"Invalid value for 'FSSO-disconnect-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FSSO_DISCONNECT_LOGS)}"
            error_msg += f"\n  → Example: FSSO-disconnect-logs='{{ VALID_BODY_FSSO_DISCONNECT_LOGS[0] }}'"
            return (False, error_msg)
    if "ssh-logs" in payload:
        value = payload["ssh-logs"]
        if value not in VALID_BODY_SSH_LOGS:
            desc = FIELD_DESCRIPTIONS.get("ssh-logs", "")
            error_msg = f"Invalid value for 'ssh-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSH_LOGS)}"
            error_msg += f"\n  → Example: ssh-logs='{{ VALID_BODY_SSH_LOGS[0] }}'"
            return (False, error_msg)
    if "severity" in payload:
        value = payload["severity"]
        if value not in VALID_BODY_SEVERITY:
            desc = FIELD_DESCRIPTIONS.get("severity", "")
            error_msg = f"Invalid value for 'severity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SEVERITY)}"
            error_msg += f"\n  → Example: severity='{{ VALID_BODY_SEVERITY[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_alertemail_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update alertemail/setting.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_alertemail_setting_put(payload)
    """
    # Step 1: Validate enum values
    if "filter-mode" in payload:
        value = payload["filter-mode"]
        if value not in VALID_BODY_FILTER_MODE:
            return (
                False,
                f"Invalid value for 'filter-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_FILTER_MODE)}",
            )
    if "IPS-logs" in payload:
        value = payload["IPS-logs"]
        if value not in VALID_BODY_IPS_LOGS:
            return (
                False,
                f"Invalid value for 'IPS-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_IPS_LOGS)}",
            )
    if "firewall-authentication-failure-logs" in payload:
        value = payload["firewall-authentication-failure-logs"]
        if value not in VALID_BODY_FIREWALL_AUTHENTICATION_FAILURE_LOGS:
            return (
                False,
                f"Invalid value for 'firewall-authentication-failure-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_FIREWALL_AUTHENTICATION_FAILURE_LOGS)}",
            )
    if "HA-logs" in payload:
        value = payload["HA-logs"]
        if value not in VALID_BODY_HA_LOGS:
            return (
                False,
                f"Invalid value for 'HA-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_HA_LOGS)}",
            )
    if "IPsec-errors-logs" in payload:
        value = payload["IPsec-errors-logs"]
        if value not in VALID_BODY_IPSEC_ERRORS_LOGS:
            return (
                False,
                f"Invalid value for 'IPsec-errors-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_ERRORS_LOGS)}",
            )
    if "FDS-update-logs" in payload:
        value = payload["FDS-update-logs"]
        if value not in VALID_BODY_FDS_UPDATE_LOGS:
            return (
                False,
                f"Invalid value for 'FDS-update-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_FDS_UPDATE_LOGS)}",
            )
    if "PPP-errors-logs" in payload:
        value = payload["PPP-errors-logs"]
        if value not in VALID_BODY_PPP_ERRORS_LOGS:
            return (
                False,
                f"Invalid value for 'PPP-errors-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_PPP_ERRORS_LOGS)}",
            )
    if "sslvpn-authentication-errors-logs" in payload:
        value = payload["sslvpn-authentication-errors-logs"]
        if value not in VALID_BODY_SSLVPN_AUTHENTICATION_ERRORS_LOGS:
            return (
                False,
                f"Invalid value for 'sslvpn-authentication-errors-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_SSLVPN_AUTHENTICATION_ERRORS_LOGS)}",
            )
    if "antivirus-logs" in payload:
        value = payload["antivirus-logs"]
        if value not in VALID_BODY_ANTIVIRUS_LOGS:
            return (
                False,
                f"Invalid value for 'antivirus-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_ANTIVIRUS_LOGS)}",
            )
    if "webfilter-logs" in payload:
        value = payload["webfilter-logs"]
        if value not in VALID_BODY_WEBFILTER_LOGS:
            return (
                False,
                f"Invalid value for 'webfilter-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_LOGS)}",
            )
    if "configuration-changes-logs" in payload:
        value = payload["configuration-changes-logs"]
        if value not in VALID_BODY_CONFIGURATION_CHANGES_LOGS:
            return (
                False,
                f"Invalid value for 'configuration-changes-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_CONFIGURATION_CHANGES_LOGS)}",
            )
    if "violation-traffic-logs" in payload:
        value = payload["violation-traffic-logs"]
        if value not in VALID_BODY_VIOLATION_TRAFFIC_LOGS:
            return (
                False,
                f"Invalid value for 'violation-traffic-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_VIOLATION_TRAFFIC_LOGS)}",
            )
    if "admin-login-logs" in payload:
        value = payload["admin-login-logs"]
        if value not in VALID_BODY_ADMIN_LOGIN_LOGS:
            return (
                False,
                f"Invalid value for 'admin-login-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_LOGIN_LOGS)}",
            )
    if "FDS-license-expiring-warning" in payload:
        value = payload["FDS-license-expiring-warning"]
        if value not in VALID_BODY_FDS_LICENSE_EXPIRING_WARNING:
            return (
                False,
                f"Invalid value for 'FDS-license-expiring-warning'='{value}'. Must be one of: {', '.join(VALID_BODY_FDS_LICENSE_EXPIRING_WARNING)}",
            )
    if "log-disk-usage-warning" in payload:
        value = payload["log-disk-usage-warning"]
        if value not in VALID_BODY_LOG_DISK_USAGE_WARNING:
            return (
                False,
                f"Invalid value for 'log-disk-usage-warning'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_DISK_USAGE_WARNING)}",
            )
    if "fortiguard-log-quota-warning" in payload:
        value = payload["fortiguard-log-quota-warning"]
        if value not in VALID_BODY_FORTIGUARD_LOG_QUOTA_WARNING:
            return (
                False,
                f"Invalid value for 'fortiguard-log-quota-warning'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTIGUARD_LOG_QUOTA_WARNING)}",
            )
    if "amc-interface-bypass-mode" in payload:
        value = payload["amc-interface-bypass-mode"]
        if value not in VALID_BODY_AMC_INTERFACE_BYPASS_MODE:
            return (
                False,
                f"Invalid value for 'amc-interface-bypass-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_AMC_INTERFACE_BYPASS_MODE)}",
            )
    if "FIPS-CC-errors" in payload:
        value = payload["FIPS-CC-errors"]
        if value not in VALID_BODY_FIPS_CC_ERRORS:
            return (
                False,
                f"Invalid value for 'FIPS-CC-errors'='{value}'. Must be one of: {', '.join(VALID_BODY_FIPS_CC_ERRORS)}",
            )
    if "FSSO-disconnect-logs" in payload:
        value = payload["FSSO-disconnect-logs"]
        if value not in VALID_BODY_FSSO_DISCONNECT_LOGS:
            return (
                False,
                f"Invalid value for 'FSSO-disconnect-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_FSSO_DISCONNECT_LOGS)}",
            )
    if "ssh-logs" in payload:
        value = payload["ssh-logs"]
        if value not in VALID_BODY_SSH_LOGS:
            return (
                False,
                f"Invalid value for 'ssh-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_SSH_LOGS)}",
            )
    if "severity" in payload:
        value = payload["severity"]
        if value not in VALID_BODY_SEVERITY:
            return (
                False,
                f"Invalid value for 'severity'='{value}'. Must be one of: {', '.join(VALID_BODY_SEVERITY)}",
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
    "endpoint": "alertemail/setting",
    "category": "cmdb",
    "api_path": "alertemail/setting",
    "help": "Configure alert email settings.",
    "total_fields": 35,
    "required_fields_count": 0,
    "fields_with_defaults_count": 35,
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
