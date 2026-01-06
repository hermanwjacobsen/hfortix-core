"""Validation helpers for log/setting - Auto-generated"""

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
    "rest-api-performance": "disable",
    "long-live-session-stat": "enable",
    "extended-utm-log": "disable",
    "zone-name": "disable",
    "web-svc-perf": "disable",
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
    "rest-api-performance": "option",  # Enable/disable REST API memory and performance stats in rest
    "long-live-session-stat": "option",  # Enable/disable long-live-session statistics logging.
    "extended-utm-log": "option",  # Enable/disable extended UTM logging.
    "zone-name": "option",  # Enable/disable zone name logging.
    "web-svc-perf": "option",  # Enable/disable web-svc performance logging.
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
    "rest-api-performance": "Enable/disable REST API memory and performance stats in rest-api-get/set logs.",
    "long-live-session-stat": "Enable/disable long-live-session statistics logging.",
    "extended-utm-log": "Enable/disable extended UTM logging.",
    "zone-name": "Enable/disable zone name logging.",
    "web-svc-perf": "Enable/disable web-svc performance logging.",
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
    "enable",  # Enable adding resolved domain names to traffic logs.
    "disable",  # Disable adding resolved domain names to traffic logs.
]
VALID_BODY_RESOLVE_PORT = [
    "enable",  # Enable adding resolved service names to traffic logs.
    "disable",  # Disable adding resolved service names to traffic logs.
]
VALID_BODY_LOG_USER_IN_UPPER = [
    "enable",  # Enable logs with user-in-upper.
    "disable",  # Disable logs with user-in-upper.
]
VALID_BODY_FWPOLICY_IMPLICIT_LOG = [
    "enable",  # Enable implicit firewall policy logging.
    "disable",  # Disable implicit firewall policy logging.
]
VALID_BODY_FWPOLICY6_IMPLICIT_LOG = [
    "enable",  # Enable implicit firewall policy6 logging.
    "disable",  # Disable implicit firewall policy6 logging.
]
VALID_BODY_EXTENDED_LOG = [
    "enable",  # Enable extended traffic logging.
    "disable",  # Disable extended traffic logging.
]
VALID_BODY_LOCAL_IN_ALLOW = [
    "enable",  # Enable local-in-allow logging.
    "disable",  # Disable local-in-allow logging.
]
VALID_BODY_LOCAL_IN_DENY_UNICAST = [
    "enable",  # Enable local-in-deny-unicast logging.
    "disable",  # Disable local-in-deny-unicast logging.
]
VALID_BODY_LOCAL_IN_DENY_BROADCAST = [
    "enable",  # Enable local-in-deny-broadcast logging.
    "disable",  # Disable local-in-deny-broadcast logging.
]
VALID_BODY_LOCAL_IN_POLICY_LOG = [
    "enable",  # Enable local-in-policy logging.
    "disable",  # Disable local-in-policy logging.
]
VALID_BODY_LOCAL_OUT = [
    "enable",  # Enable local-out logging.
    "disable",  # Disable local-out logging.
]
VALID_BODY_LOCAL_OUT_IOC_DETECTION = [
    "enable",  # Enable local-out traffic IoC detection. Requires local-out to be enabled.
    "disable",  # Disable local-out traffic IoC detection.
]
VALID_BODY_DAEMON_LOG = [
    "enable",  # Enable daemon logging.
    "disable",  # Disable daemon logging.
]
VALID_BODY_NEIGHBOR_EVENT = [
    "enable",  # Enable neighbor event logging.
    "disable",  # Disable neighbor event logging.
]
VALID_BODY_BRIEF_TRAFFIC_FORMAT = [
    "enable",  # Enable brief format traffic logging.
    "disable",  # Disable brief format traffic logging.
]
VALID_BODY_USER_ANONYMIZE = [
    "enable",  # Enable anonymizing user names in log messages.
    "disable",  # Disable anonymizing user names in log messages.
]
VALID_BODY_EXPOLICY_IMPLICIT_LOG = [
    "enable",  # Enable proxy firewall implicit policy logging.
    "disable",  # Disable proxy firewall implicit policy logging.
]
VALID_BODY_LOG_POLICY_COMMENT = [
    "enable",  # Enable inserting policy comments into traffic logs.
    "disable",  # Disable inserting policy comments into traffic logs.
]
VALID_BODY_FAZ_OVERRIDE = [
    "enable",  # Enable override FortiAnalyzer settings.
    "disable",  # Disable override FortiAnalyzer settings.
]
VALID_BODY_SYSLOG_OVERRIDE = [
    "enable",  # Enable override Syslog settings.
    "disable",  # Disable override Syslog settings.
]
VALID_BODY_REST_API_SET = [
    "enable",  # Enable POST/PUT/DELETE REST API logging.
    "disable",  # Disable POST/PUT/DELETE REST API logging.
]
VALID_BODY_REST_API_GET = [
    "enable",  # Enable GET REST API logging.
    "disable",  # Disable GET REST API logging.
]
VALID_BODY_REST_API_PERFORMANCE = [
    "enable",  # Enable REST API performance stats in REST API logs.
    "disable",  # Disable REST API performance stats in REST API logs.
]
VALID_BODY_LONG_LIVE_SESSION_STAT = [
    "enable",  # Enable long-live-session statistics logging.
    "disable",  # Disable long-live-session statistics logging.
]
VALID_BODY_EXTENDED_UTM_LOG = [
    "enable",  # Enable extended UTM logging.
    "disable",  # Disable extended UTM logging.
]
VALID_BODY_ZONE_NAME = [
    "enable",  # Enable zone name logging.
    "disable",  # Disable zone name logging.
]
VALID_BODY_WEB_SVC_PERF = [
    "enable",  # Enable web-svc performance logging.
    "disable",  # Disable web-svc performance logging.
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
    """Validate GET request parameters for log/setting."""
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
    """Validate required fields for log/setting."""
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
    """Validate POST request to create new log/setting object."""
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
    if "rest-api-performance" in payload:
        value = payload["rest-api-performance"]
        if value not in VALID_BODY_REST_API_PERFORMANCE:
            desc = FIELD_DESCRIPTIONS.get("rest-api-performance", "")
            error_msg = f"Invalid value for 'rest-api-performance': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REST_API_PERFORMANCE)}"
            error_msg += f"\n  → Example: rest-api-performance='{{ VALID_BODY_REST_API_PERFORMANCE[0] }}'"
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
    if "web-svc-perf" in payload:
        value = payload["web-svc-perf"]
        if value not in VALID_BODY_WEB_SVC_PERF:
            desc = FIELD_DESCRIPTIONS.get("web-svc-perf", "")
            error_msg = f"Invalid value for 'web-svc-perf': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_SVC_PERF)}"
            error_msg += f"\n  → Example: web-svc-perf='{{ VALID_BODY_WEB_SVC_PERF[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update log/setting."""
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
    if "rest-api-performance" in payload:
        value = payload["rest-api-performance"]
        if value not in VALID_BODY_REST_API_PERFORMANCE:
            return (
                False,
                f"Invalid value for 'rest-api-performance'='{value}'. Must be one of: {', '.join(VALID_BODY_REST_API_PERFORMANCE)}",
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
    if "web-svc-perf" in payload:
        value = payload["web-svc-perf"]
        if value not in VALID_BODY_WEB_SVC_PERF:
            return (
                False,
                f"Invalid value for 'web-svc-perf'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_SVC_PERF)}",
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
    "endpoint": "log/setting",
    "category": "cmdb",
    "api_path": "log/setting",
    "help": "Configure general log settings.",
    "total_fields": 29,
    "required_fields_count": 0,
    "fields_with_defaults_count": 28,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
