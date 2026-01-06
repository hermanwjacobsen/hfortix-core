"""
Validation helpers for firewall/access_proxy6 endpoint.

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
    "vip",  # Virtual IP name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "vip": "",
    "auth-portal": "disable",
    "auth-virtual-host": "",
    "log-blocked-traffic": "enable",
    "add-vhost-domain-to-dnsdb": "disable",
    "svr-pool-multiplex": "disable",
    "svr-pool-ttl": 15,
    "svr-pool-server-max-request": 0,
    "svr-pool-server-max-concurrent-request": 0,
    "decrypted-traffic-mirror": "",
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
    "name": "string",  # Access Proxy name.
    "vip": "string",  # Virtual IP name.
    "auth-portal": "option",  # Enable/disable authentication portal.
    "auth-virtual-host": "string",  # Virtual host for authentication portal.
    "log-blocked-traffic": "option",  # Enable/disable logging of blocked traffic.
    "add-vhost-domain-to-dnsdb": "option",  # Enable/disable adding vhost/domain to dnsdb for ztna dox tun
    "svr-pool-multiplex": "option",  # Enable/disable server pool multiplexing (default = disable).
    "svr-pool-ttl": "integer",  # Time-to-live in the server pool for idle connections to serv
    "svr-pool-server-max-request": "integer",  # Maximum number of requests that servers in server pool handl
    "svr-pool-server-max-concurrent-request": "integer",  # Maximum number of concurrent requests that servers in server
    "decrypted-traffic-mirror": "string",  # Decrypted traffic mirror.
    "api-gateway": "string",  # Set IPv4 API Gateway.
    "api-gateway6": "string",  # Set IPv6 API Gateway.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Access Proxy name.",
    "vip": "Virtual IP name.",
    "auth-portal": "Enable/disable authentication portal.",
    "auth-virtual-host": "Virtual host for authentication portal.",
    "log-blocked-traffic": "Enable/disable logging of blocked traffic.",
    "add-vhost-domain-to-dnsdb": "Enable/disable adding vhost/domain to dnsdb for ztna dox tunnel.",
    "svr-pool-multiplex": "Enable/disable server pool multiplexing (default = disable). Share connected server in HTTP, HTTPS, and web-portal api-gateway.",
    "svr-pool-ttl": "Time-to-live in the server pool for idle connections to servers.",
    "svr-pool-server-max-request": "Maximum number of requests that servers in server pool handle before disconnecting (default = unlimited).",
    "svr-pool-server-max-concurrent-request": "Maximum number of concurrent requests that servers in server pool could handle (default = unlimited).",
    "decrypted-traffic-mirror": "Decrypted traffic mirror.",
    "api-gateway": "Set IPv4 API Gateway.",
    "api-gateway6": "Set IPv6 API Gateway.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "vip": {"type": "string", "max_length": 79},
    "auth-virtual-host": {"type": "string", "max_length": 79},
    "svr-pool-ttl": {"type": "integer", "min": 0, "max": 2147483647},
    "svr-pool-server-max-request": {"type": "integer", "min": 0, "max": 2147483647},
    "svr-pool-server-max-concurrent-request": {"type": "integer", "min": 0, "max": 2147483647},
    "decrypted-traffic-mirror": {"type": "string", "max_length": 35},
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
            "options": [{"help": "HTTP.", "label": "Http", "name": "http"}, {"help": "HTTPS.", "label": "Https", "name": "https"}, {"help": "TCP-FORWARDING.", "label": "Tcp Forwarding", "name": "tcp-forwarding"}, {"help": "SAML-SP.", "label": "Samlsp", "name": "samlsp"}, {"help": "VPN-SSL-WEB-PORTAL.", "label": "Web Portal", "name": "web-portal"}, {"help": "SAAS.", "label": "Saas", "name": "saas"}],
        },
        "ldb-method": {
            "type": "option",
            "help": "Method used to distribute sessions to real servers.",
            "default": "static",
            "options": [{"help": "Distribute to server based on source IP.", "label": "Static", "name": "static"}, {"help": "Distribute to server based round robin order.", "label": "Round Robin", "name": "round-robin"}, {"help": "Distribute to server based on weight.", "label": "Weighted", "name": "weighted"}, {"help": "Distribute to the first server that is alive.", "label": "First Alive", "name": "first-alive"}, {"help": "Distribute to server based on host field in HTTP header.", "label": "Http Host", "name": "http-host"}],
        },
        "virtual-host": {
            "type": "string",
            "help": "Virtual host.",
            "default": "",
            "max_length": 79,
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
        "application": {
            "type": "string",
            "help": "SaaS application controlled by this Access Proxy.",
            "required": True,
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
            "options": [{"help": "Disable use of HTTP cookie domain from host field in HTTP (use http-cooke-domain setting).", "label": "Disable", "name": "disable"}, {"help": "Enable use of HTTP cookie domain from host field in HTTP.", "label": "Enable", "name": "enable"}],
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
            "options": [{"help": "Only allow HTTP cookie to match this API Gateway.", "label": "Disable", "name": "disable"}, {"help": "Allow HTTP cookie to match any API Gateway with same IP.", "label": "Same Ip", "name": "same-ip"}],
        },
        "https-cookie-secure": {
            "type": "option",
            "help": "Enable/disable verification that inserted HTTPS cookies are secure.",
            "default": "disable",
            "options": [{"help": "Do not mark cookie as secure, allow sharing between an HTTP and HTTPS connection.", "label": "Disable", "name": "disable"}, {"help": "Mark inserted cookie as secure, cookie can only be used for HTTPS a connection.", "label": "Enable", "name": "enable"}],
        },
        "saml-server": {
            "type": "string",
            "help": "SAML service provider configuration for VIP authentication.",
            "default": "",
            "max_length": 35,
        },
        "saml-redirect": {
            "type": "option",
            "help": "Enable/disable SAML redirection after successful authentication.",
            "default": "enable",
            "options": [{"help": "Do not support redirection after successful SAML authentication.", "label": "Disable", "name": "disable"}, {"help": "Support redirection after successful SAML authentication.", "label": "Enable", "name": "enable"}],
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
        "ssl-vpn-web-portal": {
            "type": "string",
            "help": "Agentless VPN web portal.",
            "default": "",
            "max_length": 35,
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
            "options": [{"help": "HTTP.", "label": "Http", "name": "http"}, {"help": "HTTPS.", "label": "Https", "name": "https"}, {"help": "TCP-FORWARDING.", "label": "Tcp Forwarding", "name": "tcp-forwarding"}, {"help": "SAML-SP.", "label": "Samlsp", "name": "samlsp"}, {"help": "VPN-SSL-WEB-PORTAL.", "label": "Web Portal", "name": "web-portal"}, {"help": "SAAS.", "label": "Saas", "name": "saas"}],
        },
        "ldb-method": {
            "type": "option",
            "help": "Method used to distribute sessions to real servers.",
            "default": "static",
            "options": [{"help": "Distribute to server based on source IP.", "label": "Static", "name": "static"}, {"help": "Distribute to server based round robin order.", "label": "Round Robin", "name": "round-robin"}, {"help": "Distribute to server based on weight.", "label": "Weighted", "name": "weighted"}, {"help": "Distribute to the first server that is alive.", "label": "First Alive", "name": "first-alive"}, {"help": "Distribute to server based on host field in HTTP header.", "label": "Http Host", "name": "http-host"}],
        },
        "virtual-host": {
            "type": "string",
            "help": "Virtual host.",
            "default": "",
            "max_length": 79,
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
        "application": {
            "type": "string",
            "help": "SaaS application controlled by this Access Proxy.",
            "required": True,
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
            "options": [{"help": "Disable use of HTTP cookie domain from host field in HTTP (use http-cooke-domain setting).", "label": "Disable", "name": "disable"}, {"help": "Enable use of HTTP cookie domain from host field in HTTP.", "label": "Enable", "name": "enable"}],
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
            "options": [{"help": "Only allow HTTP cookie to match this API Gateway.", "label": "Disable", "name": "disable"}, {"help": "Allow HTTP cookie to match any API Gateway with same IP.", "label": "Same Ip", "name": "same-ip"}],
        },
        "https-cookie-secure": {
            "type": "option",
            "help": "Enable/disable verification that inserted HTTPS cookies are secure.",
            "default": "disable",
            "options": [{"help": "Do not mark cookie as secure, allow sharing between an HTTP and HTTPS connection.", "label": "Disable", "name": "disable"}, {"help": "Mark inserted cookie as secure, cookie can only be used for HTTPS a connection.", "label": "Enable", "name": "enable"}],
        },
        "saml-server": {
            "type": "string",
            "help": "SAML service provider configuration for VIP authentication.",
            "default": "",
            "max_length": 35,
        },
        "saml-redirect": {
            "type": "option",
            "help": "Enable/disable SAML redirection after successful authentication.",
            "default": "enable",
            "options": [{"help": "Do not support redirection after successful SAML authentication.", "label": "Disable", "name": "disable"}, {"help": "Support redirection after successful SAML authentication.", "label": "Enable", "name": "enable"}],
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
        "ssl-vpn-web-portal": {
            "type": "string",
            "help": "Agentless VPN web portal.",
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_AUTH_PORTAL = [
    "disable",  # Disable authentication portal.
    "enable",  # Enable authentication portal.
]
VALID_BODY_LOG_BLOCKED_TRAFFIC = [
    "enable",  # Log all traffic denied by this access proxy.
    "disable",  # Do not log all traffic denied by this access proxy.
]
VALID_BODY_ADD_VHOST_DOMAIN_TO_DNSDB = [
    "enable",  # add dns entry for all vhosts used by access proxy.
    "disable",  # Do not add dns entry for all vhosts used by access proxy.
]
VALID_BODY_SVR_POOL_MULTIPLEX = [
    "enable",  # Enable server pool multiplexing.  Share connected server.
    "disable",  # Disable server pool multiplexing.  Do not share connected server.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_access_proxy6_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for firewall/access_proxy6.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_firewall_access_proxy6_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_firewall_access_proxy6_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_firewall_access_proxy6_get(
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
    Validate required fields for firewall/access_proxy6.

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


def validate_firewall_access_proxy6_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new firewall/access_proxy6 object.

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
        ...     "vip": True,  # Virtual IP name.
        ... }
        >>> is_valid, error = validate_firewall_access_proxy6_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "vip": True,
        ...     "auth-portal": "{'name': 'disable', 'help': 'Disable authentication portal.', 'label': 'Disable', 'description': 'Disable authentication portal'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_firewall_access_proxy6_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["auth-portal"] = "invalid-value"
        >>> is_valid, error = validate_firewall_access_proxy6_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_firewall_access_proxy6_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
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
    if "add-vhost-domain-to-dnsdb" in payload:
        value = payload["add-vhost-domain-to-dnsdb"]
        if value not in VALID_BODY_ADD_VHOST_DOMAIN_TO_DNSDB:
            desc = FIELD_DESCRIPTIONS.get("add-vhost-domain-to-dnsdb", "")
            error_msg = f"Invalid value for 'add-vhost-domain-to-dnsdb': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADD_VHOST_DOMAIN_TO_DNSDB)}"
            error_msg += f"\n  → Example: add-vhost-domain-to-dnsdb='{{ VALID_BODY_ADD_VHOST_DOMAIN_TO_DNSDB[0] }}'"
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


def validate_firewall_access_proxy6_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update firewall/access_proxy6.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_firewall_access_proxy6_put(payload)
    """
    # Step 1: Validate enum values
    if "auth-portal" in payload:
        value = payload["auth-portal"]
        if value not in VALID_BODY_AUTH_PORTAL:
            return (
                False,
                f"Invalid value for 'auth-portal'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PORTAL)}",
            )
    if "log-blocked-traffic" in payload:
        value = payload["log-blocked-traffic"]
        if value not in VALID_BODY_LOG_BLOCKED_TRAFFIC:
            return (
                False,
                f"Invalid value for 'log-blocked-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_BLOCKED_TRAFFIC)}",
            )
    if "add-vhost-domain-to-dnsdb" in payload:
        value = payload["add-vhost-domain-to-dnsdb"]
        if value not in VALID_BODY_ADD_VHOST_DOMAIN_TO_DNSDB:
            return (
                False,
                f"Invalid value for 'add-vhost-domain-to-dnsdb'='{value}'. Must be one of: {', '.join(VALID_BODY_ADD_VHOST_DOMAIN_TO_DNSDB)}",
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
    "endpoint": "firewall/access_proxy6",
    "category": "cmdb",
    "api_path": "firewall/access-proxy6",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure IPv6 access proxy.",
    "total_fields": 13,
    "required_fields_count": 1,
    "fields_with_defaults_count": 11,
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
