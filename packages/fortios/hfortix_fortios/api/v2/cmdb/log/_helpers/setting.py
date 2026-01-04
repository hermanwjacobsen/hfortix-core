"""
Validation helpers for log/setting endpoint.

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
    "resolve-ip": "disable",
    "resolve-port": "enable",
    "log-user-in-upper": "disable",
    "fwpolicy-implicit-log": "disable",
    "fwpolicy6-implicit-log": "disable",
    "extended-log": "disable",
    "local-in-allow": "disable",
    "local-in-deny-unicast": "disable",
    "local-in-deny-broadcast": "disable",
    "local-in-policy-log": "disable",
    "local-out": "enable",
    "local-out-ioc-detection": "enable",
    "daemon-log": "disable",
    "neighbor-event": "disable",
    "brief-traffic-format": "disable",
    "user-anonymize": "disable",
    "expolicy-implicit-log": "disable",
    "log-policy-comment": "disable",
    "faz-override": "disable",
    "syslog-override": "disable",
    "rest-api-set": "disable",
    "rest-api-get": "disable",
    "long-live-session-stat": "enable",
    "extended-utm-log": "disable",
    "zone-name": "disable",
    "anonymization-hash": "",
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
    "resolve-ip": "option",  # Enable/disable adding resolved domain names to traffic logs 
    "resolve-port": "option",  # Enable/disable adding resolved service names to traffic logs
    "log-user-in-upper": "option",  # Enable/disable logs with user-in-upper.
    "fwpolicy-implicit-log": "option",  # Enable/disable implicit firewall policy logging.
    "fwpolicy6-implicit-log": "option",  # Enable/disable implicit firewall policy6 logging.
    "extended-log": "option",  # Enable/disable extended traffic logging.
    "local-in-allow": "option",  # Enable/disable local-in-allow logging.
    "local-in-deny-unicast": "option",  # Enable/disable local-in-deny-unicast logging.
    "local-in-deny-broadcast": "option",  # Enable/disable local-in-deny-broadcast logging.
    "local-in-policy-log": "option",  # Enable/disable local-in-policy logging.
    "local-out": "option",  # Enable/disable local-out logging.
    "local-out-ioc-detection": "option",  # Enable/disable local-out traffic IoC detection. Requires loc
    "daemon-log": "option",  # Enable/disable daemon logging.
    "neighbor-event": "option",  # Enable/disable neighbor event logging.
    "brief-traffic-format": "option",  # Enable/disable brief format traffic logging.
    "user-anonymize": "option",  # Enable/disable anonymizing user names in log messages.
    "expolicy-implicit-log": "option",  # Enable/disable proxy firewall implicit policy logging.
    "log-policy-comment": "option",  # Enable/disable inserting policy comments into traffic logs.
    "faz-override": "option",  # Enable/disable override FortiAnalyzer settings.
    "syslog-override": "option",  # Enable/disable override Syslog settings.
    "rest-api-set": "option",  # Enable/disable REST API POST/PUT/DELETE request logging.
    "rest-api-get": "option",  # Enable/disable REST API GET request logging.
    "long-live-session-stat": "option",  # Enable/disable long-live-session statistics logging.
    "extended-utm-log": "option",  # Enable/disable extended UTM logging.
    "zone-name": "option",  # Enable/disable zone name logging.
    "custom-log-fields": "string",  # Custom fields to append to all log messages.
    "anonymization-hash": "string",  # User name anonymization hash salt.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "resolve-ip": "Enable/disable adding resolved domain names to traffic logs if possible.",
    "resolve-port": "Enable/disable adding resolved service names to traffic logs.",
    "log-user-in-upper": "Enable/disable logs with user-in-upper.",
    "fwpolicy-implicit-log": "Enable/disable implicit firewall policy logging.",
    "fwpolicy6-implicit-log": "Enable/disable implicit firewall policy6 logging.",
    "extended-log": "Enable/disable extended traffic logging.",
    "local-in-allow": "Enable/disable local-in-allow logging.",
    "local-in-deny-unicast": "Enable/disable local-in-deny-unicast logging.",
    "local-in-deny-broadcast": "Enable/disable local-in-deny-broadcast logging.",
    "local-in-policy-log": "Enable/disable local-in-policy logging.",
    "local-out": "Enable/disable local-out logging.",
    "local-out-ioc-detection": "Enable/disable local-out traffic IoC detection. Requires local-out to be enabled.",
    "daemon-log": "Enable/disable daemon logging.",
    "neighbor-event": "Enable/disable neighbor event logging.",
    "brief-traffic-format": "Enable/disable brief format traffic logging.",
    "user-anonymize": "Enable/disable anonymizing user names in log messages.",
    "expolicy-implicit-log": "Enable/disable proxy firewall implicit policy logging.",
    "log-policy-comment": "Enable/disable inserting policy comments into traffic logs.",
    "faz-override": "Enable/disable override FortiAnalyzer settings.",
    "syslog-override": "Enable/disable override Syslog settings.",
    "rest-api-set": "Enable/disable REST API POST/PUT/DELETE request logging.",
    "rest-api-get": "Enable/disable REST API GET request logging.",
    "long-live-session-stat": "Enable/disable long-live-session statistics logging.",
    "extended-utm-log": "Enable/disable extended UTM logging.",
    "zone-name": "Enable/disable zone name logging.",
    "custom-log-fields": "Custom fields to append to all log messages.",
    "anonymization-hash": "User name anonymization hash salt.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "anonymization-hash": {"type": "string", "max_length": 32},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "custom-log-fields": {
        "field-id": {
            "type": "string",
            "help": "Custom log field.",
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_RESOLVE_IP = [
    "enable",
    "disable",
]
VALID_BODY_RESOLVE_PORT = [
    "enable",
    "disable",
]
VALID_BODY_LOG_USER_IN_UPPER = [
    "enable",
    "disable",
]
VALID_BODY_FWPOLICY_IMPLICIT_LOG = [
    "enable",
    "disable",
]
VALID_BODY_FWPOLICY6_IMPLICIT_LOG = [
    "enable",
    "disable",
]
VALID_BODY_EXTENDED_LOG = [
    "enable",
    "disable",
]
VALID_BODY_LOCAL_IN_ALLOW = [
    "enable",
    "disable",
]
VALID_BODY_LOCAL_IN_DENY_UNICAST = [
    "enable",
    "disable",
]
VALID_BODY_LOCAL_IN_DENY_BROADCAST = [
    "enable",
    "disable",
]
VALID_BODY_LOCAL_IN_POLICY_LOG = [
    "enable",
    "disable",
]
VALID_BODY_LOCAL_OUT = [
    "enable",
    "disable",
]
VALID_BODY_LOCAL_OUT_IOC_DETECTION = [
    "enable",
    "disable",
]
VALID_BODY_DAEMON_LOG = [
    "enable",
    "disable",
]
VALID_BODY_NEIGHBOR_EVENT = [
    "enable",
    "disable",
]
VALID_BODY_BRIEF_TRAFFIC_FORMAT = [
    "enable",
    "disable",
]
VALID_BODY_USER_ANONYMIZE = [
    "enable",
    "disable",
]
VALID_BODY_EXPOLICY_IMPLICIT_LOG = [
    "enable",
    "disable",
]
VALID_BODY_LOG_POLICY_COMMENT = [
    "enable",
    "disable",
]
VALID_BODY_FAZ_OVERRIDE = [
    "enable",
    "disable",
]
VALID_BODY_SYSLOG_OVERRIDE = [
    "enable",
    "disable",
]
VALID_BODY_REST_API_SET = [
    "enable",
    "disable",
]
VALID_BODY_REST_API_GET = [
    "enable",
    "disable",
]
VALID_BODY_LONG_LIVE_SESSION_STAT = [
    "enable",
    "disable",
]
VALID_BODY_EXTENDED_UTM_LOG = [
    "enable",
    "disable",
]
VALID_BODY_ZONE_NAME = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_log_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for log/setting.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_log_setting_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_log_setting_get(
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
    Validate required fields for log/setting.

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


def validate_log_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new log/setting object.

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
        >>> is_valid, error = validate_log_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "resolve-ip": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_log_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["resolve-ip"] = "invalid-value"
        >>> is_valid, error = validate_log_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_log_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "resolve-ip" in payload:
        value = payload["resolve-ip"]
        if value not in VALID_BODY_RESOLVE_IP:
            desc = FIELD_DESCRIPTIONS.get("resolve-ip", "")
            error_msg = f"Invalid value for 'resolve-ip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESOLVE_IP)}"
            error_msg += f"\n  → Example: resolve-ip='{{ VALID_BODY_RESOLVE_IP[0] }}'"
            return (False, error_msg)
    if "resolve-port" in payload:
        value = payload["resolve-port"]
        if value not in VALID_BODY_RESOLVE_PORT:
            desc = FIELD_DESCRIPTIONS.get("resolve-port", "")
            error_msg = f"Invalid value for 'resolve-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESOLVE_PORT)}"
            error_msg += f"\n  → Example: resolve-port='{{ VALID_BODY_RESOLVE_PORT[0] }}'"
            return (False, error_msg)
    if "log-user-in-upper" in payload:
        value = payload["log-user-in-upper"]
        if value not in VALID_BODY_LOG_USER_IN_UPPER:
            desc = FIELD_DESCRIPTIONS.get("log-user-in-upper", "")
            error_msg = f"Invalid value for 'log-user-in-upper': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_USER_IN_UPPER)}"
            error_msg += f"\n  → Example: log-user-in-upper='{{ VALID_BODY_LOG_USER_IN_UPPER[0] }}'"
            return (False, error_msg)
    if "fwpolicy-implicit-log" in payload:
        value = payload["fwpolicy-implicit-log"]
        if value not in VALID_BODY_FWPOLICY_IMPLICIT_LOG:
            desc = FIELD_DESCRIPTIONS.get("fwpolicy-implicit-log", "")
            error_msg = f"Invalid value for 'fwpolicy-implicit-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FWPOLICY_IMPLICIT_LOG)}"
            error_msg += f"\n  → Example: fwpolicy-implicit-log='{{ VALID_BODY_FWPOLICY_IMPLICIT_LOG[0] }}'"
            return (False, error_msg)
    if "fwpolicy6-implicit-log" in payload:
        value = payload["fwpolicy6-implicit-log"]
        if value not in VALID_BODY_FWPOLICY6_IMPLICIT_LOG:
            desc = FIELD_DESCRIPTIONS.get("fwpolicy6-implicit-log", "")
            error_msg = f"Invalid value for 'fwpolicy6-implicit-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FWPOLICY6_IMPLICIT_LOG)}"
            error_msg += f"\n  → Example: fwpolicy6-implicit-log='{{ VALID_BODY_FWPOLICY6_IMPLICIT_LOG[0] }}'"
            return (False, error_msg)
    if "extended-log" in payload:
        value = payload["extended-log"]
        if value not in VALID_BODY_EXTENDED_LOG:
            desc = FIELD_DESCRIPTIONS.get("extended-log", "")
            error_msg = f"Invalid value for 'extended-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTENDED_LOG)}"
            error_msg += f"\n  → Example: extended-log='{{ VALID_BODY_EXTENDED_LOG[0] }}'"
            return (False, error_msg)
    if "local-in-allow" in payload:
        value = payload["local-in-allow"]
        if value not in VALID_BODY_LOCAL_IN_ALLOW:
            desc = FIELD_DESCRIPTIONS.get("local-in-allow", "")
            error_msg = f"Invalid value for 'local-in-allow': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_IN_ALLOW)}"
            error_msg += f"\n  → Example: local-in-allow='{{ VALID_BODY_LOCAL_IN_ALLOW[0] }}'"
            return (False, error_msg)
    if "local-in-deny-unicast" in payload:
        value = payload["local-in-deny-unicast"]
        if value not in VALID_BODY_LOCAL_IN_DENY_UNICAST:
            desc = FIELD_DESCRIPTIONS.get("local-in-deny-unicast", "")
            error_msg = f"Invalid value for 'local-in-deny-unicast': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_IN_DENY_UNICAST)}"
            error_msg += f"\n  → Example: local-in-deny-unicast='{{ VALID_BODY_LOCAL_IN_DENY_UNICAST[0] }}'"
            return (False, error_msg)
    if "local-in-deny-broadcast" in payload:
        value = payload["local-in-deny-broadcast"]
        if value not in VALID_BODY_LOCAL_IN_DENY_BROADCAST:
            desc = FIELD_DESCRIPTIONS.get("local-in-deny-broadcast", "")
            error_msg = f"Invalid value for 'local-in-deny-broadcast': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_IN_DENY_BROADCAST)}"
            error_msg += f"\n  → Example: local-in-deny-broadcast='{{ VALID_BODY_LOCAL_IN_DENY_BROADCAST[0] }}'"
            return (False, error_msg)
    if "local-in-policy-log" in payload:
        value = payload["local-in-policy-log"]
        if value not in VALID_BODY_LOCAL_IN_POLICY_LOG:
            desc = FIELD_DESCRIPTIONS.get("local-in-policy-log", "")
            error_msg = f"Invalid value for 'local-in-policy-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_IN_POLICY_LOG)}"
            error_msg += f"\n  → Example: local-in-policy-log='{{ VALID_BODY_LOCAL_IN_POLICY_LOG[0] }}'"
            return (False, error_msg)
    if "local-out" in payload:
        value = payload["local-out"]
        if value not in VALID_BODY_LOCAL_OUT:
            desc = FIELD_DESCRIPTIONS.get("local-out", "")
            error_msg = f"Invalid value for 'local-out': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_OUT)}"
            error_msg += f"\n  → Example: local-out='{{ VALID_BODY_LOCAL_OUT[0] }}'"
            return (False, error_msg)
    if "local-out-ioc-detection" in payload:
        value = payload["local-out-ioc-detection"]
        if value not in VALID_BODY_LOCAL_OUT_IOC_DETECTION:
            desc = FIELD_DESCRIPTIONS.get("local-out-ioc-detection", "")
            error_msg = f"Invalid value for 'local-out-ioc-detection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_OUT_IOC_DETECTION)}"
            error_msg += f"\n  → Example: local-out-ioc-detection='{{ VALID_BODY_LOCAL_OUT_IOC_DETECTION[0] }}'"
            return (False, error_msg)
    if "daemon-log" in payload:
        value = payload["daemon-log"]
        if value not in VALID_BODY_DAEMON_LOG:
            desc = FIELD_DESCRIPTIONS.get("daemon-log", "")
            error_msg = f"Invalid value for 'daemon-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DAEMON_LOG)}"
            error_msg += f"\n  → Example: daemon-log='{{ VALID_BODY_DAEMON_LOG[0] }}'"
            return (False, error_msg)
    if "neighbor-event" in payload:
        value = payload["neighbor-event"]
        if value not in VALID_BODY_NEIGHBOR_EVENT:
            desc = FIELD_DESCRIPTIONS.get("neighbor-event", "")
            error_msg = f"Invalid value for 'neighbor-event': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NEIGHBOR_EVENT)}"
            error_msg += f"\n  → Example: neighbor-event='{{ VALID_BODY_NEIGHBOR_EVENT[0] }}'"
            return (False, error_msg)
    if "brief-traffic-format" in payload:
        value = payload["brief-traffic-format"]
        if value not in VALID_BODY_BRIEF_TRAFFIC_FORMAT:
            desc = FIELD_DESCRIPTIONS.get("brief-traffic-format", "")
            error_msg = f"Invalid value for 'brief-traffic-format': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BRIEF_TRAFFIC_FORMAT)}"
            error_msg += f"\n  → Example: brief-traffic-format='{{ VALID_BODY_BRIEF_TRAFFIC_FORMAT[0] }}'"
            return (False, error_msg)
    if "user-anonymize" in payload:
        value = payload["user-anonymize"]
        if value not in VALID_BODY_USER_ANONYMIZE:
            desc = FIELD_DESCRIPTIONS.get("user-anonymize", "")
            error_msg = f"Invalid value for 'user-anonymize': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USER_ANONYMIZE)}"
            error_msg += f"\n  → Example: user-anonymize='{{ VALID_BODY_USER_ANONYMIZE[0] }}'"
            return (False, error_msg)
    if "expolicy-implicit-log" in payload:
        value = payload["expolicy-implicit-log"]
        if value not in VALID_BODY_EXPOLICY_IMPLICIT_LOG:
            desc = FIELD_DESCRIPTIONS.get("expolicy-implicit-log", "")
            error_msg = f"Invalid value for 'expolicy-implicit-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXPOLICY_IMPLICIT_LOG)}"
            error_msg += f"\n  → Example: expolicy-implicit-log='{{ VALID_BODY_EXPOLICY_IMPLICIT_LOG[0] }}'"
            return (False, error_msg)
    if "log-policy-comment" in payload:
        value = payload["log-policy-comment"]
        if value not in VALID_BODY_LOG_POLICY_COMMENT:
            desc = FIELD_DESCRIPTIONS.get("log-policy-comment", "")
            error_msg = f"Invalid value for 'log-policy-comment': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_POLICY_COMMENT)}"
            error_msg += f"\n  → Example: log-policy-comment='{{ VALID_BODY_LOG_POLICY_COMMENT[0] }}'"
            return (False, error_msg)
    if "faz-override" in payload:
        value = payload["faz-override"]
        if value not in VALID_BODY_FAZ_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("faz-override", "")
            error_msg = f"Invalid value for 'faz-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAZ_OVERRIDE)}"
            error_msg += f"\n  → Example: faz-override='{{ VALID_BODY_FAZ_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "syslog-override" in payload:
        value = payload["syslog-override"]
        if value not in VALID_BODY_SYSLOG_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("syslog-override", "")
            error_msg = f"Invalid value for 'syslog-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYSLOG_OVERRIDE)}"
            error_msg += f"\n  → Example: syslog-override='{{ VALID_BODY_SYSLOG_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "rest-api-set" in payload:
        value = payload["rest-api-set"]
        if value not in VALID_BODY_REST_API_SET:
            desc = FIELD_DESCRIPTIONS.get("rest-api-set", "")
            error_msg = f"Invalid value for 'rest-api-set': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REST_API_SET)}"
            error_msg += f"\n  → Example: rest-api-set='{{ VALID_BODY_REST_API_SET[0] }}'"
            return (False, error_msg)
    if "rest-api-get" in payload:
        value = payload["rest-api-get"]
        if value not in VALID_BODY_REST_API_GET:
            desc = FIELD_DESCRIPTIONS.get("rest-api-get", "")
            error_msg = f"Invalid value for 'rest-api-get': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REST_API_GET)}"
            error_msg += f"\n  → Example: rest-api-get='{{ VALID_BODY_REST_API_GET[0] }}'"
            return (False, error_msg)
    if "long-live-session-stat" in payload:
        value = payload["long-live-session-stat"]
        if value not in VALID_BODY_LONG_LIVE_SESSION_STAT:
            desc = FIELD_DESCRIPTIONS.get("long-live-session-stat", "")
            error_msg = f"Invalid value for 'long-live-session-stat': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LONG_LIVE_SESSION_STAT)}"
            error_msg += f"\n  → Example: long-live-session-stat='{{ VALID_BODY_LONG_LIVE_SESSION_STAT[0] }}'"
            return (False, error_msg)
    if "extended-utm-log" in payload:
        value = payload["extended-utm-log"]
        if value not in VALID_BODY_EXTENDED_UTM_LOG:
            desc = FIELD_DESCRIPTIONS.get("extended-utm-log", "")
            error_msg = f"Invalid value for 'extended-utm-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTENDED_UTM_LOG)}"
            error_msg += f"\n  → Example: extended-utm-log='{{ VALID_BODY_EXTENDED_UTM_LOG[0] }}'"
            return (False, error_msg)
    if "zone-name" in payload:
        value = payload["zone-name"]
        if value not in VALID_BODY_ZONE_NAME:
            desc = FIELD_DESCRIPTIONS.get("zone-name", "")
            error_msg = f"Invalid value for 'zone-name': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ZONE_NAME)}"
            error_msg += f"\n  → Example: zone-name='{{ VALID_BODY_ZONE_NAME[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update log/setting.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_log_setting_put(payload)
    """
    # Step 1: Validate enum values
    if "resolve-ip" in payload:
        value = payload["resolve-ip"]
        if value not in VALID_BODY_RESOLVE_IP:
            return (
                False,
                f"Invalid value for 'resolve-ip'='{value}'. Must be one of: {', '.join(VALID_BODY_RESOLVE_IP)}",
            )
    if "resolve-port" in payload:
        value = payload["resolve-port"]
        if value not in VALID_BODY_RESOLVE_PORT:
            return (
                False,
                f"Invalid value for 'resolve-port'='{value}'. Must be one of: {', '.join(VALID_BODY_RESOLVE_PORT)}",
            )
    if "log-user-in-upper" in payload:
        value = payload["log-user-in-upper"]
        if value not in VALID_BODY_LOG_USER_IN_UPPER:
            return (
                False,
                f"Invalid value for 'log-user-in-upper'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_USER_IN_UPPER)}",
            )
    if "fwpolicy-implicit-log" in payload:
        value = payload["fwpolicy-implicit-log"]
        if value not in VALID_BODY_FWPOLICY_IMPLICIT_LOG:
            return (
                False,
                f"Invalid value for 'fwpolicy-implicit-log'='{value}'. Must be one of: {', '.join(VALID_BODY_FWPOLICY_IMPLICIT_LOG)}",
            )
    if "fwpolicy6-implicit-log" in payload:
        value = payload["fwpolicy6-implicit-log"]
        if value not in VALID_BODY_FWPOLICY6_IMPLICIT_LOG:
            return (
                False,
                f"Invalid value for 'fwpolicy6-implicit-log'='{value}'. Must be one of: {', '.join(VALID_BODY_FWPOLICY6_IMPLICIT_LOG)}",
            )
    if "extended-log" in payload:
        value = payload["extended-log"]
        if value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid value for 'extended-log'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )
    if "local-in-allow" in payload:
        value = payload["local-in-allow"]
        if value not in VALID_BODY_LOCAL_IN_ALLOW:
            return (
                False,
                f"Invalid value for 'local-in-allow'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_IN_ALLOW)}",
            )
    if "local-in-deny-unicast" in payload:
        value = payload["local-in-deny-unicast"]
        if value not in VALID_BODY_LOCAL_IN_DENY_UNICAST:
            return (
                False,
                f"Invalid value for 'local-in-deny-unicast'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_IN_DENY_UNICAST)}",
            )
    if "local-in-deny-broadcast" in payload:
        value = payload["local-in-deny-broadcast"]
        if value not in VALID_BODY_LOCAL_IN_DENY_BROADCAST:
            return (
                False,
                f"Invalid value for 'local-in-deny-broadcast'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_IN_DENY_BROADCAST)}",
            )
    if "local-in-policy-log" in payload:
        value = payload["local-in-policy-log"]
        if value not in VALID_BODY_LOCAL_IN_POLICY_LOG:
            return (
                False,
                f"Invalid value for 'local-in-policy-log'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_IN_POLICY_LOG)}",
            )
    if "local-out" in payload:
        value = payload["local-out"]
        if value not in VALID_BODY_LOCAL_OUT:
            return (
                False,
                f"Invalid value for 'local-out'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_OUT)}",
            )
    if "local-out-ioc-detection" in payload:
        value = payload["local-out-ioc-detection"]
        if value not in VALID_BODY_LOCAL_OUT_IOC_DETECTION:
            return (
                False,
                f"Invalid value for 'local-out-ioc-detection'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_OUT_IOC_DETECTION)}",
            )
    if "daemon-log" in payload:
        value = payload["daemon-log"]
        if value not in VALID_BODY_DAEMON_LOG:
            return (
                False,
                f"Invalid value for 'daemon-log'='{value}'. Must be one of: {', '.join(VALID_BODY_DAEMON_LOG)}",
            )
    if "neighbor-event" in payload:
        value = payload["neighbor-event"]
        if value not in VALID_BODY_NEIGHBOR_EVENT:
            return (
                False,
                f"Invalid value for 'neighbor-event'='{value}'. Must be one of: {', '.join(VALID_BODY_NEIGHBOR_EVENT)}",
            )
    if "brief-traffic-format" in payload:
        value = payload["brief-traffic-format"]
        if value not in VALID_BODY_BRIEF_TRAFFIC_FORMAT:
            return (
                False,
                f"Invalid value for 'brief-traffic-format'='{value}'. Must be one of: {', '.join(VALID_BODY_BRIEF_TRAFFIC_FORMAT)}",
            )
    if "user-anonymize" in payload:
        value = payload["user-anonymize"]
        if value not in VALID_BODY_USER_ANONYMIZE:
            return (
                False,
                f"Invalid value for 'user-anonymize'='{value}'. Must be one of: {', '.join(VALID_BODY_USER_ANONYMIZE)}",
            )
    if "expolicy-implicit-log" in payload:
        value = payload["expolicy-implicit-log"]
        if value not in VALID_BODY_EXPOLICY_IMPLICIT_LOG:
            return (
                False,
                f"Invalid value for 'expolicy-implicit-log'='{value}'. Must be one of: {', '.join(VALID_BODY_EXPOLICY_IMPLICIT_LOG)}",
            )
    if "log-policy-comment" in payload:
        value = payload["log-policy-comment"]
        if value not in VALID_BODY_LOG_POLICY_COMMENT:
            return (
                False,
                f"Invalid value for 'log-policy-comment'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_POLICY_COMMENT)}",
            )
    if "faz-override" in payload:
        value = payload["faz-override"]
        if value not in VALID_BODY_FAZ_OVERRIDE:
            return (
                False,
                f"Invalid value for 'faz-override'='{value}'. Must be one of: {', '.join(VALID_BODY_FAZ_OVERRIDE)}",
            )
    if "syslog-override" in payload:
        value = payload["syslog-override"]
        if value not in VALID_BODY_SYSLOG_OVERRIDE:
            return (
                False,
                f"Invalid value for 'syslog-override'='{value}'. Must be one of: {', '.join(VALID_BODY_SYSLOG_OVERRIDE)}",
            )
    if "rest-api-set" in payload:
        value = payload["rest-api-set"]
        if value not in VALID_BODY_REST_API_SET:
            return (
                False,
                f"Invalid value for 'rest-api-set'='{value}'. Must be one of: {', '.join(VALID_BODY_REST_API_SET)}",
            )
    if "rest-api-get" in payload:
        value = payload["rest-api-get"]
        if value not in VALID_BODY_REST_API_GET:
            return (
                False,
                f"Invalid value for 'rest-api-get'='{value}'. Must be one of: {', '.join(VALID_BODY_REST_API_GET)}",
            )
    if "long-live-session-stat" in payload:
        value = payload["long-live-session-stat"]
        if value not in VALID_BODY_LONG_LIVE_SESSION_STAT:
            return (
                False,
                f"Invalid value for 'long-live-session-stat'='{value}'. Must be one of: {', '.join(VALID_BODY_LONG_LIVE_SESSION_STAT)}",
            )
    if "extended-utm-log" in payload:
        value = payload["extended-utm-log"]
        if value not in VALID_BODY_EXTENDED_UTM_LOG:
            return (
                False,
                f"Invalid value for 'extended-utm-log'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_UTM_LOG)}",
            )
    if "zone-name" in payload:
        value = payload["zone-name"]
        if value not in VALID_BODY_ZONE_NAME:
            return (
                False,
                f"Invalid value for 'zone-name'='{value}'. Must be one of: {', '.join(VALID_BODY_ZONE_NAME)}",
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
    "endpoint": "log/setting",
    "category": "cmdb",
    "api_path": "log/setting",
    "help": "Configure general log settings.",
    "total_fields": 27,
    "required_fields_count": 0,
    "fields_with_defaults_count": 26,
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
