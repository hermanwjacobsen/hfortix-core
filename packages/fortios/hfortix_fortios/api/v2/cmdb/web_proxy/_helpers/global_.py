"""Validation helpers for web_proxy/global_ - Auto-generated"""

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
    "ssl-cert": "Fortinet_Factory",
    "ssl-ca-cert": "Fortinet_CA_SSL",
    "fast-policy-match": "enable",
    "ldap-user-cache": "disable",
    "proxy-fqdn": "default.fqdn",
    "max-request-length": 8,
    "max-message-length": 32,
    "http2-client-window-size": 1048576,
    "http2-server-window-size": 1048576,
    "auth-sign-timeout": 120,
    "strict-web-check": "disable",
    "forward-proxy-auth": "disable",
    "forward-server-affinity-timeout": 30,
    "max-waf-body-cache-length": 1,
    "webproxy-profile": "",
    "learn-client-ip": "disable",
    "always-learn-client-ip": "disable",
    "learn-client-ip-from-header": "",
    "src-affinity-exempt-addr": "",
    "src-affinity-exempt-addr6": "",
    "policy-partial-match": "enable",
    "log-policy-pending": "disable",
    "log-forward-server": "disable",
    "log-app-id": "disable",
    "proxy-transparent-cert-inspection": "disable",
    "request-obs-fold": "keep",
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
    "ssl-cert": "string",  # SSL certificate for SSL interception.
    "ssl-ca-cert": "string",  # SSL CA certificate for SSL interception.
    "fast-policy-match": "option",  # Enable/disable fast matching algorithm for explicit and tran
    "ldap-user-cache": "option",  # Enable/disable LDAP user cache for explicit and transparent 
    "proxy-fqdn": "string",  # Fully Qualified Domain Name of the explicit web proxy (defau
    "max-request-length": "integer",  # Maximum length of HTTP request line (2 - 64 Kbytes, default 
    "max-message-length": "integer",  # Maximum length of HTTP message, not including body (16 - 256
    "http2-client-window-size": "integer",  # HTTP/2 client initial window size in bytes (65535 - 21474836
    "http2-server-window-size": "integer",  # HTTP/2 server initial window size in bytes (65535 - 21474836
    "auth-sign-timeout": "integer",  # Proxy auth query sign timeout in seconds (30 - 3600, default
    "strict-web-check": "option",  # Enable/disable strict web checking to block web sites that s
    "forward-proxy-auth": "option",  # Enable/disable forwarding proxy authentication headers.
    "forward-server-affinity-timeout": "integer",  # Period of time before the source IP's traffic is no longer a
    "max-waf-body-cache-length": "integer",  # Maximum length of HTTP messages processed by Web Application
    "webproxy-profile": "string",  # Name of the web proxy profile to apply when explicit proxy t
    "learn-client-ip": "option",  # Enable/disable learning the client's IP address from headers
    "always-learn-client-ip": "option",  # Enable/disable learning the client's IP address from headers
    "learn-client-ip-from-header": "option",  # Learn client IP address from the specified headers.
    "learn-client-ip-srcaddr": "string",  # Source address name (srcaddr or srcaddr6 must be set).
    "learn-client-ip-srcaddr6": "string",  # IPv6 Source address name (srcaddr or srcaddr6 must be set).
    "src-affinity-exempt-addr": "ipv4-address-any",  # IPv4 source addresses to exempt proxy affinity.
    "src-affinity-exempt-addr6": "ipv6-address",  # IPv6 source addresses to exempt proxy affinity.
    "policy-partial-match": "option",  # Enable/disable policy partial matching.
    "log-policy-pending": "option",  # Enable/disable logging sessions that are pending on policy m
    "log-forward-server": "option",  # Enable/disable forward server name logging in forward traffi
    "log-app-id": "option",  # Enable/disable always log application type in traffic log.
    "proxy-transparent-cert-inspection": "option",  # Enable/disable transparent proxy certificate inspection.
    "request-obs-fold": "option",  # Action when HTTP/1.x request header contains obs-fold (defau
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "ssl-cert": "SSL certificate for SSL interception.",
    "ssl-ca-cert": "SSL CA certificate for SSL interception.",
    "fast-policy-match": "Enable/disable fast matching algorithm for explicit and transparent proxy policy.",
    "ldap-user-cache": "Enable/disable LDAP user cache for explicit and transparent proxy user.",
    "proxy-fqdn": "Fully Qualified Domain Name of the explicit web proxy (default = default.fqdn) that clients connect to.",
    "max-request-length": "Maximum length of HTTP request line (2 - 64 Kbytes, default = 8).",
    "max-message-length": "Maximum length of HTTP message, not including body (16 - 256 Kbytes, default = 32).",
    "http2-client-window-size": "HTTP/2 client initial window size in bytes (65535 - 2147483647, default = 1048576 (1MB)).",
    "http2-server-window-size": "HTTP/2 server initial window size in bytes (65535 - 2147483647, default = 1048576 (1MB)).",
    "auth-sign-timeout": "Proxy auth query sign timeout in seconds (30 - 3600, default = 120).",
    "strict-web-check": "Enable/disable strict web checking to block web sites that send incorrect headers that don't conform to HTTP.",
    "forward-proxy-auth": "Enable/disable forwarding proxy authentication headers.",
    "forward-server-affinity-timeout": "Period of time before the source IP's traffic is no longer assigned to the forwarding server (6 - 60 min, default = 30).",
    "max-waf-body-cache-length": "Maximum length of HTTP messages processed by Web Application Firewall (WAF) (1 - 1024 Kbytes, default = 1).",
    "webproxy-profile": "Name of the web proxy profile to apply when explicit proxy traffic is allowed by default and traffic is accepted that does not match an explicit proxy policy.",
    "learn-client-ip": "Enable/disable learning the client's IP address from headers.",
    "always-learn-client-ip": "Enable/disable learning the client's IP address from headers for every request.",
    "learn-client-ip-from-header": "Learn client IP address from the specified headers.",
    "learn-client-ip-srcaddr": "Source address name (srcaddr or srcaddr6 must be set).",
    "learn-client-ip-srcaddr6": "IPv6 Source address name (srcaddr or srcaddr6 must be set).",
    "src-affinity-exempt-addr": "IPv4 source addresses to exempt proxy affinity.",
    "src-affinity-exempt-addr6": "IPv6 source addresses to exempt proxy affinity.",
    "policy-partial-match": "Enable/disable policy partial matching.",
    "log-policy-pending": "Enable/disable logging sessions that are pending on policy matching.",
    "log-forward-server": "Enable/disable forward server name logging in forward traffic log.",
    "log-app-id": "Enable/disable always log application type in traffic log.",
    "proxy-transparent-cert-inspection": "Enable/disable transparent proxy certificate inspection.",
    "request-obs-fold": "Action when HTTP/1.x request header contains obs-fold (default = keep).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "ssl-cert": {"type": "string", "max_length": 35},
    "ssl-ca-cert": {"type": "string", "max_length": 35},
    "proxy-fqdn": {"type": "string", "max_length": 255},
    "max-request-length": {"type": "integer", "min": 2, "max": 64},
    "max-message-length": {"type": "integer", "min": 16, "max": 256},
    "http2-client-window-size": {"type": "integer", "min": 65535, "max": 2147483647},
    "http2-server-window-size": {"type": "integer", "min": 65535, "max": 2147483647},
    "auth-sign-timeout": {"type": "integer", "min": 30, "max": 3600},
    "forward-server-affinity-timeout": {"type": "integer", "min": 6, "max": 60},
    "max-waf-body-cache-length": {"type": "integer", "min": 1, "max": 1024},
    "webproxy-profile": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "learn-client-ip-srcaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "learn-client-ip-srcaddr6": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_FAST_POLICY_MATCH = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_LDAP_USER_CACHE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_STRICT_WEB_CHECK = [
    "enable",  # Enable strict web checking.
    "disable",  # Disable strict web checking.
]
VALID_BODY_FORWARD_PROXY_AUTH = [
    "enable",  # Enable forwarding proxy authentication headers.
    "disable",  # Disable forwarding proxy authentication headers.
]
VALID_BODY_LEARN_CLIENT_IP = [
    "enable",  # Enable learning the client's IP address from headers.
    "disable",  # Disable learning the client's IP address from headers.
]
VALID_BODY_ALWAYS_LEARN_CLIENT_IP = [
    "enable",  # Enable learning the client's IP address from headers for every request.
    "disable",  # Disable learning the client's IP address from headers for every request.
]
VALID_BODY_LEARN_CLIENT_IP_FROM_HEADER = [
    "true-client-ip",  # Learn the client IP address from the True-Client-IP header.
    "x-real-ip",  # Learn the client IP address from the X-Real-IP header.
    "x-forwarded-for",  # Learn the client IP address from the X-Forwarded-For header.
]
VALID_BODY_POLICY_PARTIAL_MATCH = [
    "enable",  # Enable policy partial matching.
    "disable",  # Disable policy partial matching.
]
VALID_BODY_LOG_POLICY_PENDING = [
    "enable",  # Enable logging sessions that are pending on policy matching.
    "disable",  # Disable logging sessions that are pending on policy matching.
]
VALID_BODY_LOG_FORWARD_SERVER = [
    "enable",  # Enable logging forward server name in forward traffic log.
    "disable",  # Disable logging forward server name in forward traffic log.
]
VALID_BODY_LOG_APP_ID = [
    "enable",  # Enable logging application type in traffic log.
    "disable",  # Disable logging application type in traffic log.
]
VALID_BODY_PROXY_TRANSPARENT_CERT_INSPECTION = [
    "enable",  # Enable proxying certificate inspection in transparent mode.
    "disable",  # Disable proxying certificate inspection in transparent mode.
]
VALID_BODY_REQUEST_OBS_FOLD = [
    "replace-with-sp",  # Replace CRLF in obs-fold with SP in the request header for HTTP/1.x.
    "block",  # Block HTTP/1.x request with obs-fold.
    "keep",  # Keep obs-fold in the request header for HTTP/1.x. There are known security risks.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_web_proxy_global__get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for web_proxy/global_."""
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
    """Validate required fields for web_proxy/global_."""
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


def validate_web_proxy_global__post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new web_proxy/global_ object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "fast-policy-match" in payload:
        value = payload["fast-policy-match"]
        if value not in VALID_BODY_FAST_POLICY_MATCH:
            desc = FIELD_DESCRIPTIONS.get("fast-policy-match", "")
            error_msg = f"Invalid value for 'fast-policy-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAST_POLICY_MATCH)}"
            error_msg += f"\n  → Example: fast-policy-match='{{ VALID_BODY_FAST_POLICY_MATCH[0] }}'"
            return (False, error_msg)
    if "ldap-user-cache" in payload:
        value = payload["ldap-user-cache"]
        if value not in VALID_BODY_LDAP_USER_CACHE:
            desc = FIELD_DESCRIPTIONS.get("ldap-user-cache", "")
            error_msg = f"Invalid value for 'ldap-user-cache': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LDAP_USER_CACHE)}"
            error_msg += f"\n  → Example: ldap-user-cache='{{ VALID_BODY_LDAP_USER_CACHE[0] }}'"
            return (False, error_msg)
    if "strict-web-check" in payload:
        value = payload["strict-web-check"]
        if value not in VALID_BODY_STRICT_WEB_CHECK:
            desc = FIELD_DESCRIPTIONS.get("strict-web-check", "")
            error_msg = f"Invalid value for 'strict-web-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STRICT_WEB_CHECK)}"
            error_msg += f"\n  → Example: strict-web-check='{{ VALID_BODY_STRICT_WEB_CHECK[0] }}'"
            return (False, error_msg)
    if "forward-proxy-auth" in payload:
        value = payload["forward-proxy-auth"]
        if value not in VALID_BODY_FORWARD_PROXY_AUTH:
            desc = FIELD_DESCRIPTIONS.get("forward-proxy-auth", "")
            error_msg = f"Invalid value for 'forward-proxy-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORWARD_PROXY_AUTH)}"
            error_msg += f"\n  → Example: forward-proxy-auth='{{ VALID_BODY_FORWARD_PROXY_AUTH[0] }}'"
            return (False, error_msg)
    if "learn-client-ip" in payload:
        value = payload["learn-client-ip"]
        if value not in VALID_BODY_LEARN_CLIENT_IP:
            desc = FIELD_DESCRIPTIONS.get("learn-client-ip", "")
            error_msg = f"Invalid value for 'learn-client-ip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LEARN_CLIENT_IP)}"
            error_msg += f"\n  → Example: learn-client-ip='{{ VALID_BODY_LEARN_CLIENT_IP[0] }}'"
            return (False, error_msg)
    if "always-learn-client-ip" in payload:
        value = payload["always-learn-client-ip"]
        if value not in VALID_BODY_ALWAYS_LEARN_CLIENT_IP:
            desc = FIELD_DESCRIPTIONS.get("always-learn-client-ip", "")
            error_msg = f"Invalid value for 'always-learn-client-ip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALWAYS_LEARN_CLIENT_IP)}"
            error_msg += f"\n  → Example: always-learn-client-ip='{{ VALID_BODY_ALWAYS_LEARN_CLIENT_IP[0] }}'"
            return (False, error_msg)
    if "learn-client-ip-from-header" in payload:
        value = payload["learn-client-ip-from-header"]
        if value not in VALID_BODY_LEARN_CLIENT_IP_FROM_HEADER:
            desc = FIELD_DESCRIPTIONS.get("learn-client-ip-from-header", "")
            error_msg = f"Invalid value for 'learn-client-ip-from-header': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LEARN_CLIENT_IP_FROM_HEADER)}"
            error_msg += f"\n  → Example: learn-client-ip-from-header='{{ VALID_BODY_LEARN_CLIENT_IP_FROM_HEADER[0] }}'"
            return (False, error_msg)
    if "policy-partial-match" in payload:
        value = payload["policy-partial-match"]
        if value not in VALID_BODY_POLICY_PARTIAL_MATCH:
            desc = FIELD_DESCRIPTIONS.get("policy-partial-match", "")
            error_msg = f"Invalid value for 'policy-partial-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_POLICY_PARTIAL_MATCH)}"
            error_msg += f"\n  → Example: policy-partial-match='{{ VALID_BODY_POLICY_PARTIAL_MATCH[0] }}'"
            return (False, error_msg)
    if "log-policy-pending" in payload:
        value = payload["log-policy-pending"]
        if value not in VALID_BODY_LOG_POLICY_PENDING:
            desc = FIELD_DESCRIPTIONS.get("log-policy-pending", "")
            error_msg = f"Invalid value for 'log-policy-pending': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_POLICY_PENDING)}"
            error_msg += f"\n  → Example: log-policy-pending='{{ VALID_BODY_LOG_POLICY_PENDING[0] }}'"
            return (False, error_msg)
    if "log-forward-server" in payload:
        value = payload["log-forward-server"]
        if value not in VALID_BODY_LOG_FORWARD_SERVER:
            desc = FIELD_DESCRIPTIONS.get("log-forward-server", "")
            error_msg = f"Invalid value for 'log-forward-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_FORWARD_SERVER)}"
            error_msg += f"\n  → Example: log-forward-server='{{ VALID_BODY_LOG_FORWARD_SERVER[0] }}'"
            return (False, error_msg)
    if "log-app-id" in payload:
        value = payload["log-app-id"]
        if value not in VALID_BODY_LOG_APP_ID:
            desc = FIELD_DESCRIPTIONS.get("log-app-id", "")
            error_msg = f"Invalid value for 'log-app-id': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_APP_ID)}"
            error_msg += f"\n  → Example: log-app-id='{{ VALID_BODY_LOG_APP_ID[0] }}'"
            return (False, error_msg)
    if "proxy-transparent-cert-inspection" in payload:
        value = payload["proxy-transparent-cert-inspection"]
        if value not in VALID_BODY_PROXY_TRANSPARENT_CERT_INSPECTION:
            desc = FIELD_DESCRIPTIONS.get("proxy-transparent-cert-inspection", "")
            error_msg = f"Invalid value for 'proxy-transparent-cert-inspection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROXY_TRANSPARENT_CERT_INSPECTION)}"
            error_msg += f"\n  → Example: proxy-transparent-cert-inspection='{{ VALID_BODY_PROXY_TRANSPARENT_CERT_INSPECTION[0] }}'"
            return (False, error_msg)
    if "request-obs-fold" in payload:
        value = payload["request-obs-fold"]
        if value not in VALID_BODY_REQUEST_OBS_FOLD:
            desc = FIELD_DESCRIPTIONS.get("request-obs-fold", "")
            error_msg = f"Invalid value for 'request-obs-fold': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REQUEST_OBS_FOLD)}"
            error_msg += f"\n  → Example: request-obs-fold='{{ VALID_BODY_REQUEST_OBS_FOLD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_web_proxy_global__put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update web_proxy/global_."""
    # Step 1: Validate enum values
    if "fast-policy-match" in payload:
        value = payload["fast-policy-match"]
        if value not in VALID_BODY_FAST_POLICY_MATCH:
            return (
                False,
                f"Invalid value for 'fast-policy-match'='{value}'. Must be one of: {', '.join(VALID_BODY_FAST_POLICY_MATCH)}",
            )
    if "ldap-user-cache" in payload:
        value = payload["ldap-user-cache"]
        if value not in VALID_BODY_LDAP_USER_CACHE:
            return (
                False,
                f"Invalid value for 'ldap-user-cache'='{value}'. Must be one of: {', '.join(VALID_BODY_LDAP_USER_CACHE)}",
            )
    if "strict-web-check" in payload:
        value = payload["strict-web-check"]
        if value not in VALID_BODY_STRICT_WEB_CHECK:
            return (
                False,
                f"Invalid value for 'strict-web-check'='{value}'. Must be one of: {', '.join(VALID_BODY_STRICT_WEB_CHECK)}",
            )
    if "forward-proxy-auth" in payload:
        value = payload["forward-proxy-auth"]
        if value not in VALID_BODY_FORWARD_PROXY_AUTH:
            return (
                False,
                f"Invalid value for 'forward-proxy-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_FORWARD_PROXY_AUTH)}",
            )
    if "learn-client-ip" in payload:
        value = payload["learn-client-ip"]
        if value not in VALID_BODY_LEARN_CLIENT_IP:
            return (
                False,
                f"Invalid value for 'learn-client-ip'='{value}'. Must be one of: {', '.join(VALID_BODY_LEARN_CLIENT_IP)}",
            )
    if "always-learn-client-ip" in payload:
        value = payload["always-learn-client-ip"]
        if value not in VALID_BODY_ALWAYS_LEARN_CLIENT_IP:
            return (
                False,
                f"Invalid value for 'always-learn-client-ip'='{value}'. Must be one of: {', '.join(VALID_BODY_ALWAYS_LEARN_CLIENT_IP)}",
            )
    if "learn-client-ip-from-header" in payload:
        value = payload["learn-client-ip-from-header"]
        if value not in VALID_BODY_LEARN_CLIENT_IP_FROM_HEADER:
            return (
                False,
                f"Invalid value for 'learn-client-ip-from-header'='{value}'. Must be one of: {', '.join(VALID_BODY_LEARN_CLIENT_IP_FROM_HEADER)}",
            )
    if "policy-partial-match" in payload:
        value = payload["policy-partial-match"]
        if value not in VALID_BODY_POLICY_PARTIAL_MATCH:
            return (
                False,
                f"Invalid value for 'policy-partial-match'='{value}'. Must be one of: {', '.join(VALID_BODY_POLICY_PARTIAL_MATCH)}",
            )
    if "log-policy-pending" in payload:
        value = payload["log-policy-pending"]
        if value not in VALID_BODY_LOG_POLICY_PENDING:
            return (
                False,
                f"Invalid value for 'log-policy-pending'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_POLICY_PENDING)}",
            )
    if "log-forward-server" in payload:
        value = payload["log-forward-server"]
        if value not in VALID_BODY_LOG_FORWARD_SERVER:
            return (
                False,
                f"Invalid value for 'log-forward-server'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_FORWARD_SERVER)}",
            )
    if "log-app-id" in payload:
        value = payload["log-app-id"]
        if value not in VALID_BODY_LOG_APP_ID:
            return (
                False,
                f"Invalid value for 'log-app-id'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_APP_ID)}",
            )
    if "proxy-transparent-cert-inspection" in payload:
        value = payload["proxy-transparent-cert-inspection"]
        if value not in VALID_BODY_PROXY_TRANSPARENT_CERT_INSPECTION:
            return (
                False,
                f"Invalid value for 'proxy-transparent-cert-inspection'='{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_TRANSPARENT_CERT_INSPECTION)}",
            )
    if "request-obs-fold" in payload:
        value = payload["request-obs-fold"]
        if value not in VALID_BODY_REQUEST_OBS_FOLD:
            return (
                False,
                f"Invalid value for 'request-obs-fold'='{value}'. Must be one of: {', '.join(VALID_BODY_REQUEST_OBS_FOLD)}",
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
    "endpoint": "web_proxy/global_",
    "category": "cmdb",
    "api_path": "web-proxy/global",
    "help": "Configure Web proxy global settings.",
    "total_fields": 28,
    "required_fields_count": 0,
    "fields_with_defaults_count": 26,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
