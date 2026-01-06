"""Validation helpers for ztna/web_proxy - Auto-generated"""

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
    "name": "",
    "vip": "",
    "host": "",
    "decrypted-traffic-mirror": "",
    "log-blocked-traffic": "enable",
    "auth-portal": "disable",
    "auth-virtual-host": "",
    "vip6": "",
    "svr-pool-multiplex": "disable",
    "svr-pool-ttl": 15,
    "svr-pool-server-max-request": 0,
    "svr-pool-server-max-concurrent-request": 0,
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
    "name": "string",  # ZTNA proxy name.
    "vip": "string",  # Virtual IP name.
    "host": "string",  # Virtual or real host name.
    "decrypted-traffic-mirror": "string",  # Decrypted traffic mirror.
    "log-blocked-traffic": "option",  # Enable/disable logging of blocked traffic.
    "auth-portal": "option",  # Enable/disable authentication portal.
    "auth-virtual-host": "string",  # Virtual host for authentication portal.
    "vip6": "string",  # Virtual IPv6 name.
    "svr-pool-multiplex": "option",  # Enable/disable server pool multiplexing (default = disable).
    "svr-pool-ttl": "integer",  # Time-to-live in the server pool for idle connections to serv
    "svr-pool-server-max-request": "integer",  # Maximum number of requests that servers in the server pool h
    "svr-pool-server-max-concurrent-request": "integer",  # Maximum number of concurrent requests that servers in the se
    "api-gateway": "string",  # Set IPv4 API Gateway.
    "api-gateway6": "string",  # Set IPv6 API Gateway.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "ZTNA proxy name.",
    "vip": "Virtual IP name.",
    "host": "Virtual or real host name.",
    "decrypted-traffic-mirror": "Decrypted traffic mirror.",
    "log-blocked-traffic": "Enable/disable logging of blocked traffic.",
    "auth-portal": "Enable/disable authentication portal.",
    "auth-virtual-host": "Virtual host for authentication portal.",
    "vip6": "Virtual IPv6 name.",
    "svr-pool-multiplex": "Enable/disable server pool multiplexing (default = disable). Share connected server in HTTP and HTTPS api-gateways.",
    "svr-pool-ttl": "Time-to-live in the server pool for idle connections to servers.",
    "svr-pool-server-max-request": "Maximum number of requests that servers in the server pool handle before disconnecting (default = unlimited).",
    "svr-pool-server-max-concurrent-request": "Maximum number of concurrent requests that servers in the server pool could handle (default = unlimited).",
    "api-gateway": "Set IPv4 API Gateway.",
    "api-gateway6": "Set IPv6 API Gateway.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "vip": {"type": "string", "max_length": 79},
    "host": {"type": "string", "max_length": 79},
    "decrypted-traffic-mirror": {"type": "string", "max_length": 35},
    "auth-virtual-host": {"type": "string", "max_length": 79},
    "vip6": {"type": "string", "max_length": 79},
    "svr-pool-ttl": {"type": "integer", "min": 0, "max": 2147483647},
    "svr-pool-server-max-request": {"type": "integer", "min": 0, "max": 2147483647},
    "svr-pool-server-max-concurrent-request": {"type": "integer", "min": 0, "max": 2147483647},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "api-gateway": {
        "id": {
            "type": "integer",
            "help": "API Gateway ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "url-map": {
            "type": "string",
            "help": "URL pattern to match.",
            "required": True,
            "default": "/",
            "max_length": 511,
        },
        "service": {
            "type": "option",
            "help": "Service.",
            "required": True,
            "default": "https",
            "options": [{"help": "HTTP.", "label": "Http", "name": "http"}, {"help": "HTTPS.", "label": "Https", "name": "https"}],
        },
        "ldb-method": {
            "type": "option",
            "help": "Method used to distribute sessions to real servers.",
            "default": "static",
            "options": [{"help": "Distribute to servers based on source IP.", "label": "Static", "name": "static"}, {"help": "Distribute to servers based on round-robin order.", "label": "Round Robin", "name": "round-robin"}, {"help": "Distribute to servers based on weight.", "label": "Weighted", "name": "weighted"}, {"help": "Distribute to the first server that is alive.", "label": "First Alive", "name": "first-alive"}, {"help": "Distribute to servers based on the host field in HTTP header.", "label": "Http Host", "name": "http-host"}],
        },
        "url-map-type": {
            "type": "option",
            "help": "Type of url-map.",
            "required": True,
            "default": "sub-string",
            "options": [{"help": "Match the pattern if a string contains the sub-string.", "label": "Sub String", "name": "sub-string"}, {"help": "Match the pattern with wildcards.", "label": "Wildcard", "name": "wildcard"}, {"help": "Match the pattern with a regular expression.", "label": "Regex", "name": "regex"}],
        },
        "h2-support": {
            "type": "option",
            "help": "HTTP2 support, default=Enable.",
            "required": True,
            "default": "enable",
            "options": [{"help": "Enable HTTP2 support.", "label": "Enable", "name": "enable"}, {"help": "Disable HTTP2 support.", "label": "Disable", "name": "disable"}],
        },
        "h3-support": {
            "type": "option",
            "help": "HTTP3/QUIC support, default=Disable.",
            "default": "disable",
            "options": [{"help": "Enable HTTP3/QUIC support.", "label": "Enable", "name": "enable"}, {"help": "Disable HTTP3/QUIC support.", "label": "Disable", "name": "disable"}],
        },
        "quic": {
            "type": "string",
            "help": "QUIC setting.",
        },
        "realservers": {
            "type": "string",
            "help": "Select the real servers that this Access Proxy will distribute traffic to.",
        },
        "persistence": {
            "type": "option",
            "help": "Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "HTTP cookie.", "label": "Http Cookie", "name": "http-cookie"}],
        },
        "http-cookie-domain-from-host": {
            "type": "option",
            "help": "Enable/disable use of HTTP cookie domain from host field in HTTP.",
            "default": "disable",
            "options": [{"help": "Disable use of HTTP cookie domain from the host field in HTTP (use http-cooke-domain setting).", "label": "Disable", "name": "disable"}, {"help": "Enable use of HTTP cookie domain from the host field in HTTP.", "label": "Enable", "name": "enable"}],
        },
        "http-cookie-domain": {
            "type": "string",
            "help": "Domain that HTTP cookie persistence should apply to.",
            "default": "",
            "max_length": 35,
        },
        "http-cookie-path": {
            "type": "string",
            "help": "Limit HTTP cookie persistence to the specified path.",
            "default": "",
            "max_length": 35,
        },
        "http-cookie-generation": {
            "type": "integer",
            "help": "Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "http-cookie-age": {
            "type": "integer",
            "help": "Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.",
            "default": 60,
            "min_value": 0,
            "max_value": 525600,
        },
        "http-cookie-share": {
            "type": "option",
            "help": "Control sharing of cookies across API Gateway. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.",
            "default": "same-ip",
            "options": [{"help": "Only allow HTTP cookie to match this API Gateway.", "label": "Disable", "name": "disable"}, {"help": "Allow HTTP cookie to match any API Gateway with the same IP.", "label": "Same Ip", "name": "same-ip"}],
        },
        "https-cookie-secure": {
            "type": "option",
            "help": "Enable/disable verification that inserted HTTPS cookies are secure.",
            "default": "disable",
            "options": [{"help": "Do not mark the cookie as secure. Allows sharing the cookie between HTTP and HTTPS connections.", "label": "Disable", "name": "disable"}, {"help": "Mark the inserted cookie as secure. The cookie can only be used for HTTPS connections.", "label": "Enable", "name": "enable"}],
        },
        "ssl-dh-bits": {
            "type": "option",
            "help": "Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.",
            "default": "2048",
            "options": [{"help": "768-bit Diffie-Hellman prime.", "label": "768", "name": "768"}, {"help": "1024-bit Diffie-Hellman prime.", "label": "1024", "name": "1024"}, {"help": "1536-bit Diffie-Hellman prime.", "label": "1536", "name": "1536"}, {"help": "2048-bit Diffie-Hellman prime.", "label": "2048", "name": "2048"}, {"help": "3072-bit Diffie-Hellman prime.", "label": "3072", "name": "3072"}, {"help": "4096-bit Diffie-Hellman prime.", "label": "4096", "name": "4096"}],
        },
        "ssl-algorithm": {
            "type": "option",
            "help": "Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.",
            "default": "high",
            "options": [{"help": "High encryption. Allow only AES and ChaCha.", "label": "High", "name": "high"}, {"help": "Medium encryption. Allow AES, ChaCha, 3DES, and RC4.", "label": "Medium", "name": "medium"}, {"help": "Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.", "label": "Low", "name": "low"}],
        },
        "ssl-cipher-suites": {
            "type": "string",
            "help": "SSL/TLS cipher suites to offer to a server, ordered by priority.",
        },
        "ssl-min-version": {
            "type": "option",
            "help": "Lowest SSL/TLS version acceptable from a server.",
            "default": "tls-1.1",
            "options": [{"help": "TLS 1.0.", "label": "Tls 1.0", "name": "tls-1.0"}, {"help": "TLS 1.1.", "label": "Tls 1.1", "name": "tls-1.1"}, {"help": "TLS 1.2.", "label": "Tls 1.2", "name": "tls-1.2"}, {"help": "TLS 1.3.", "label": "Tls 1.3", "name": "tls-1.3"}],
        },
        "ssl-max-version": {
            "type": "option",
            "help": "Highest SSL/TLS version acceptable from a server.",
            "default": "tls-1.3",
            "options": [{"help": "TLS 1.0.", "label": "Tls 1.0", "name": "tls-1.0"}, {"help": "TLS 1.1.", "label": "Tls 1.1", "name": "tls-1.1"}, {"help": "TLS 1.2.", "label": "Tls 1.2", "name": "tls-1.2"}, {"help": "TLS 1.3.", "label": "Tls 1.3", "name": "tls-1.3"}],
        },
        "ssl-renegotiation": {
            "type": "option",
            "help": "Enable/disable secure renegotiation to comply with RFC 5746.",
            "default": "enable",
            "options": [{"help": "Enable secure renegotiation.", "label": "Enable", "name": "enable"}, {"help": "Disable secure renegotiation.", "label": "Disable", "name": "disable"}],
        },
    },
    "api-gateway6": {
        "id": {
            "type": "integer",
            "help": "API Gateway ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "url-map": {
            "type": "string",
            "help": "URL pattern to match.",
            "required": True,
            "default": "/",
            "max_length": 511,
        },
        "service": {
            "type": "option",
            "help": "Service.",
            "required": True,
            "default": "https",
            "options": [{"help": "HTTP.", "label": "Http", "name": "http"}, {"help": "HTTPS.", "label": "Https", "name": "https"}],
        },
        "ldb-method": {
            "type": "option",
            "help": "Method used to distribute sessions to real servers.",
            "default": "static",
            "options": [{"help": "Distribute to servers based on source IP.", "label": "Static", "name": "static"}, {"help": "Distribute to servers based on round-robin order.", "label": "Round Robin", "name": "round-robin"}, {"help": "Distribute to servers based on weight.", "label": "Weighted", "name": "weighted"}, {"help": "Distribute to the first server that is alive.", "label": "First Alive", "name": "first-alive"}, {"help": "Distribute to servers based on the host field in HTTP header.", "label": "Http Host", "name": "http-host"}],
        },
        "url-map-type": {
            "type": "option",
            "help": "Type of url-map.",
            "required": True,
            "default": "sub-string",
            "options": [{"help": "Match the pattern if a string contains the sub-string.", "label": "Sub String", "name": "sub-string"}, {"help": "Match the pattern with wildcards.", "label": "Wildcard", "name": "wildcard"}, {"help": "Match the pattern with a regular expression.", "label": "Regex", "name": "regex"}],
        },
        "h2-support": {
            "type": "option",
            "help": "HTTP2 support, default=Enable.",
            "required": True,
            "default": "enable",
            "options": [{"help": "Enable HTTP2 support.", "label": "Enable", "name": "enable"}, {"help": "Disable HTTP2 support.", "label": "Disable", "name": "disable"}],
        },
        "h3-support": {
            "type": "option",
            "help": "HTTP3/QUIC support, default=Disable.",
            "default": "disable",
            "options": [{"help": "Enable HTTP3/QUIC support.", "label": "Enable", "name": "enable"}, {"help": "Disable HTTP3/QUIC support.", "label": "Disable", "name": "disable"}],
        },
        "quic": {
            "type": "string",
            "help": "QUIC setting.",
        },
        "realservers": {
            "type": "string",
            "help": "Select the real servers that this Access Proxy will distribute traffic to.",
        },
        "persistence": {
            "type": "option",
            "help": "Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "HTTP cookie.", "label": "Http Cookie", "name": "http-cookie"}],
        },
        "http-cookie-domain-from-host": {
            "type": "option",
            "help": "Enable/disable use of HTTP cookie domain from host field in HTTP.",
            "default": "disable",
            "options": [{"help": "Disable use of HTTP cookie domain from the host field in HTTP (use http-cooke-domain setting).", "label": "Disable", "name": "disable"}, {"help": "Enable use of HTTP cookie domain from the host field in HTTP.", "label": "Enable", "name": "enable"}],
        },
        "http-cookie-domain": {
            "type": "string",
            "help": "Domain that HTTP cookie persistence should apply to.",
            "default": "",
            "max_length": 35,
        },
        "http-cookie-path": {
            "type": "string",
            "help": "Limit HTTP cookie persistence to the specified path.",
            "default": "",
            "max_length": 35,
        },
        "http-cookie-generation": {
            "type": "integer",
            "help": "Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "http-cookie-age": {
            "type": "integer",
            "help": "Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.",
            "default": 60,
            "min_value": 0,
            "max_value": 525600,
        },
        "http-cookie-share": {
            "type": "option",
            "help": "Control sharing of cookies across API Gateway. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.",
            "default": "same-ip",
            "options": [{"help": "Only allow HTTP cookie to match this API Gateway.", "label": "Disable", "name": "disable"}, {"help": "Allow HTTP cookie to match any API Gateway with the same IP.", "label": "Same Ip", "name": "same-ip"}],
        },
        "https-cookie-secure": {
            "type": "option",
            "help": "Enable/disable verification that inserted HTTPS cookies are secure.",
            "default": "disable",
            "options": [{"help": "Do not mark the cookie as secure. Allows sharing the cookie between HTTP and HTTPS connections.", "label": "Disable", "name": "disable"}, {"help": "Mark the inserted cookie as secure. The cookie can only be used for HTTPS connections.", "label": "Enable", "name": "enable"}],
        },
        "ssl-dh-bits": {
            "type": "option",
            "help": "Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.",
            "default": "2048",
            "options": [{"help": "768-bit Diffie-Hellman prime.", "label": "768", "name": "768"}, {"help": "1024-bit Diffie-Hellman prime.", "label": "1024", "name": "1024"}, {"help": "1536-bit Diffie-Hellman prime.", "label": "1536", "name": "1536"}, {"help": "2048-bit Diffie-Hellman prime.", "label": "2048", "name": "2048"}, {"help": "3072-bit Diffie-Hellman prime.", "label": "3072", "name": "3072"}, {"help": "4096-bit Diffie-Hellman prime.", "label": "4096", "name": "4096"}],
        },
        "ssl-algorithm": {
            "type": "option",
            "help": "Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.",
            "default": "high",
            "options": [{"help": "High encryption. Allow only AES and ChaCha.", "label": "High", "name": "high"}, {"help": "Medium encryption. Allow AES, ChaCha, 3DES, and RC4.", "label": "Medium", "name": "medium"}, {"help": "Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.", "label": "Low", "name": "low"}],
        },
        "ssl-cipher-suites": {
            "type": "string",
            "help": "SSL/TLS cipher suites to offer to a server, ordered by priority.",
        },
        "ssl-min-version": {
            "type": "option",
            "help": "Lowest SSL/TLS version acceptable from a server.",
            "default": "tls-1.1",
            "options": [{"help": "TLS 1.0.", "label": "Tls 1.0", "name": "tls-1.0"}, {"help": "TLS 1.1.", "label": "Tls 1.1", "name": "tls-1.1"}, {"help": "TLS 1.2.", "label": "Tls 1.2", "name": "tls-1.2"}, {"help": "TLS 1.3.", "label": "Tls 1.3", "name": "tls-1.3"}],
        },
        "ssl-max-version": {
            "type": "option",
            "help": "Highest SSL/TLS version acceptable from a server.",
            "default": "tls-1.3",
            "options": [{"help": "TLS 1.0.", "label": "Tls 1.0", "name": "tls-1.0"}, {"help": "TLS 1.1.", "label": "Tls 1.1", "name": "tls-1.1"}, {"help": "TLS 1.2.", "label": "Tls 1.2", "name": "tls-1.2"}, {"help": "TLS 1.3.", "label": "Tls 1.3", "name": "tls-1.3"}],
        },
        "ssl-renegotiation": {
            "type": "option",
            "help": "Enable/disable secure renegotiation to comply with RFC 5746.",
            "default": "enable",
            "options": [{"help": "Enable secure renegotiation.", "label": "Enable", "name": "enable"}, {"help": "Disable secure renegotiation.", "label": "Disable", "name": "disable"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_LOG_BLOCKED_TRAFFIC = [
    "disable",  # Do not log all traffic denied by this ZTNA web-proxy.
    "enable",  # Log all traffic denied by this ZTNA web-proxy.
]
VALID_BODY_AUTH_PORTAL = [
    "disable",  # Disable authentication portal.
    "enable",  # Enable authentication portal.
]
VALID_BODY_SVR_POOL_MULTIPLEX = [
    "enable",  # Enable server pool multiplexing. Share connected server.
    "disable",  # Disable server pool multiplexing. Do not share connected server.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ztna_web_proxy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for ztna/web_proxy."""
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
    """Validate required fields for ztna/web_proxy."""
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


def validate_ztna_web_proxy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new ztna/web_proxy object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "log-blocked-traffic" in payload:
        value = payload["log-blocked-traffic"]
        if value not in VALID_BODY_LOG_BLOCKED_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("log-blocked-traffic", "")
            error_msg = f"Invalid value for 'log-blocked-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_BLOCKED_TRAFFIC)}"
            error_msg += f"\n  → Example: log-blocked-traffic='{{ VALID_BODY_LOG_BLOCKED_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "auth-portal" in payload:
        value = payload["auth-portal"]
        if value not in VALID_BODY_AUTH_PORTAL:
            desc = FIELD_DESCRIPTIONS.get("auth-portal", "")
            error_msg = f"Invalid value for 'auth-portal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_PORTAL)}"
            error_msg += f"\n  → Example: auth-portal='{{ VALID_BODY_AUTH_PORTAL[0] }}'"
            return (False, error_msg)
    if "svr-pool-multiplex" in payload:
        value = payload["svr-pool-multiplex"]
        if value not in VALID_BODY_SVR_POOL_MULTIPLEX:
            desc = FIELD_DESCRIPTIONS.get("svr-pool-multiplex", "")
            error_msg = f"Invalid value for 'svr-pool-multiplex': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SVR_POOL_MULTIPLEX)}"
            error_msg += f"\n  → Example: svr-pool-multiplex='{{ VALID_BODY_SVR_POOL_MULTIPLEX[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ztna_web_proxy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update ztna/web_proxy."""
    # Step 1: Validate enum values
    if "log-blocked-traffic" in payload:
        value = payload["log-blocked-traffic"]
        if value not in VALID_BODY_LOG_BLOCKED_TRAFFIC:
            return (
                False,
                f"Invalid value for 'log-blocked-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_BLOCKED_TRAFFIC)}",
            )
    if "auth-portal" in payload:
        value = payload["auth-portal"]
        if value not in VALID_BODY_AUTH_PORTAL:
            return (
                False,
                f"Invalid value for 'auth-portal'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PORTAL)}",
            )
    if "svr-pool-multiplex" in payload:
        value = payload["svr-pool-multiplex"]
        if value not in VALID_BODY_SVR_POOL_MULTIPLEX:
            return (
                False,
                f"Invalid value for 'svr-pool-multiplex'='{value}'. Must be one of: {', '.join(VALID_BODY_SVR_POOL_MULTIPLEX)}",
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
    "endpoint": "ztna/web_proxy",
    "category": "cmdb",
    "api_path": "ztna/web-proxy",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure ZTNA web-proxy.",
    "total_fields": 14,
    "required_fields_count": 0,
    "fields_with_defaults_count": 12,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
