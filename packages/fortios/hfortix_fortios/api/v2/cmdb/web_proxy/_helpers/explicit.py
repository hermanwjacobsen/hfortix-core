"""Validation helpers for web_proxy/explicit - Auto-generated"""

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
    "interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "status": "disable",
    "secure-web-proxy": "disable",
    "ftp-over-http": "disable",
    "socks": "disable",
    "http-incoming-port": "",
    "http-connection-mode": "static",
    "https-incoming-port": "",
    "client-cert": "disable",
    "user-agent-detect": "enable",
    "empty-cert-action": "block",
    "ssl-dh-bits": "2048",
    "ftp-incoming-port": "",
    "socks-incoming-port": "",
    "incoming-ip": "0.0.0.0",
    "outgoing-ip": "",
    "interface-select-method": "sdwan",
    "interface": "",
    "vrf-select": -1,
    "ipv6-status": "disable",
    "incoming-ip6": "::",
    "outgoing-ip6": "",
    "strict-guest": "disable",
    "pref-dns-result": "ipv4",
    "unknown-http-version": "reject",
    "realm": "default",
    "sec-default-action": "deny",
    "https-replacement-message": "enable",
    "message-upon-server-error": "enable",
    "pac-file-server-status": "disable",
    "pac-file-url": "",
    "pac-file-server-port": "",
    "pac-file-through-https": "disable",
    "pac-file-name": "proxy.pac",
    "pac-file-data": "",
    "ssl-algorithm": "low",
    "trace-auth-no-rsp": "disable",
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
    "status": "option",  # Enable/disable the explicit Web proxy for HTTP and HTTPS ses
    "secure-web-proxy": "option",  # Enable/disable/require the secure web proxy for HTTP and HTT
    "ftp-over-http": "option",  # Enable to proxy FTP-over-HTTP sessions sent from a web brows
    "socks": "option",  # Enable/disable the SOCKS proxy.
    "http-incoming-port": "user",  # Accept incoming HTTP requests on one or more ports (0 - 6553
    "http-connection-mode": "option",  # HTTP connection mode (default = static).
    "https-incoming-port": "user",  # Accept incoming HTTPS requests on one or more ports (0 - 655
    "secure-web-proxy-cert": "string",  # Name of certificates for secure web proxy.
    "client-cert": "option",  # Enable/disable to request client certificate.
    "user-agent-detect": "option",  # Enable/disable to detect device type by HTTP user-agent if n
    "empty-cert-action": "option",  # Action of an empty client certificate.
    "ssl-dh-bits": "option",  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    "ftp-incoming-port": "user",  # Accept incoming FTP-over-HTTP requests on one or more ports 
    "socks-incoming-port": "user",  # Accept incoming SOCKS proxy requests on one or more ports (0
    "incoming-ip": "ipv4-address-any",  # Restrict the explicit HTTP proxy to only accept sessions fro
    "outgoing-ip": "ipv4-address-any",  # Outgoing HTTP requests will have this IP address as their so
    "interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "interface": "string",  # Specify outgoing interface to reach server.
    "vrf-select": "integer",  # VRF ID used for connection to server.
    "ipv6-status": "option",  # Enable/disable allowing an IPv6 web proxy destination in pol
    "incoming-ip6": "ipv6-address",  # Restrict the explicit web proxy to only accept sessions from
    "outgoing-ip6": "ipv6-address",  # Outgoing HTTP requests will leave this IPv6. Multiple interf
    "strict-guest": "option",  # Enable/disable strict guest user checking by the explicit we
    "pref-dns-result": "option",  # Prefer resolving addresses using the configured IPv4 or IPv6
    "unknown-http-version": "option",  # How to handle HTTP sessions that do not comply with HTTP 0.9
    "realm": "string",  # Authentication realm used to identify the explicit web proxy
    "sec-default-action": "option",  # Accept or deny explicit web proxy sessions when no web proxy
    "https-replacement-message": "option",  # Enable/disable sending the client a replacement message for 
    "message-upon-server-error": "option",  # Enable/disable displaying a replacement message when a serve
    "pac-file-server-status": "option",  # Enable/disable Proxy Auto-Configuration (PAC) for users of t
    "pac-file-url": "user",  # PAC file access URL.
    "pac-file-server-port": "user",  # Port number that PAC traffic from client web browsers uses t
    "pac-file-through-https": "option",  # Enable/disable to get Proxy Auto-Configuration (PAC) through
    "pac-file-name": "string",  # Pac file name.
    "pac-file-data": "user",  # PAC file contents enclosed in quotes (maximum of 256K bytes)
    "pac-policy": "string",  # PAC policies.
    "ssl-algorithm": "option",  # Relative strength of encryption algorithms accepted in HTTPS
    "trace-auth-no-rsp": "option",  # Enable/disable logging timed-out authentication requests.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable the explicit Web proxy for HTTP and HTTPS session.",
    "secure-web-proxy": "Enable/disable/require the secure web proxy for HTTP and HTTPS session.",
    "ftp-over-http": "Enable to proxy FTP-over-HTTP sessions sent from a web browser.",
    "socks": "Enable/disable the SOCKS proxy.",
    "http-incoming-port": "Accept incoming HTTP requests on one or more ports (0 - 65535, default = 8080).",
    "http-connection-mode": "HTTP connection mode (default = static).",
    "https-incoming-port": "Accept incoming HTTPS requests on one or more ports (0 - 65535, default = 0, use the same as HTTP).",
    "secure-web-proxy-cert": "Name of certificates for secure web proxy.",
    "client-cert": "Enable/disable to request client certificate.",
    "user-agent-detect": "Enable/disable to detect device type by HTTP user-agent if no client certificate provided.",
    "empty-cert-action": "Action of an empty client certificate.",
    "ssl-dh-bits": "Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048).",
    "ftp-incoming-port": "Accept incoming FTP-over-HTTP requests on one or more ports (0 - 65535, default = 0; use the same as HTTP).",
    "socks-incoming-port": "Accept incoming SOCKS proxy requests on one or more ports (0 - 65535, default = 0; use the same as HTTP).",
    "incoming-ip": "Restrict the explicit HTTP proxy to only accept sessions from this IP address. An interface must have this IP address.",
    "outgoing-ip": "Outgoing HTTP requests will have this IP address as their source address. An interface must have this IP address.",
    "interface-select-method": "Specify how to select outgoing interface to reach server.",
    "interface": "Specify outgoing interface to reach server.",
    "vrf-select": "VRF ID used for connection to server.",
    "ipv6-status": "Enable/disable allowing an IPv6 web proxy destination in policies and all IPv6 related entries in this command.",
    "incoming-ip6": "Restrict the explicit web proxy to only accept sessions from this IPv6 address. An interface must have this IPv6 address.",
    "outgoing-ip6": "Outgoing HTTP requests will leave this IPv6. Multiple interfaces can be specified. Interfaces must have these IPv6 addresses.",
    "strict-guest": "Enable/disable strict guest user checking by the explicit web proxy.",
    "pref-dns-result": "Prefer resolving addresses using the configured IPv4 or IPv6 DNS server (default = ipv4).",
    "unknown-http-version": "How to handle HTTP sessions that do not comply with HTTP 0.9, 1.0, or 1.1.",
    "realm": "Authentication realm used to identify the explicit web proxy (maximum of 63 characters).",
    "sec-default-action": "Accept or deny explicit web proxy sessions when no web proxy firewall policy exists.",
    "https-replacement-message": "Enable/disable sending the client a replacement message for HTTPS requests.",
    "message-upon-server-error": "Enable/disable displaying a replacement message when a server error is detected.",
    "pac-file-server-status": "Enable/disable Proxy Auto-Configuration (PAC) for users of this explicit proxy profile.",
    "pac-file-url": "PAC file access URL.",
    "pac-file-server-port": "Port number that PAC traffic from client web browsers uses to connect to the explicit web proxy (0 - 65535, default = 0; use the same as HTTP).",
    "pac-file-through-https": "Enable/disable to get Proxy Auto-Configuration (PAC) through HTTPS.",
    "pac-file-name": "Pac file name.",
    "pac-file-data": "PAC file contents enclosed in quotes (maximum of 256K bytes).",
    "pac-policy": "PAC policies.",
    "ssl-algorithm": "Relative strength of encryption algorithms accepted in HTTPS deep scan: high, medium, or low.",
    "trace-auth-no-rsp": "Enable/disable logging timed-out authentication requests.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "interface": {"type": "string", "max_length": 15},
    "vrf-select": {"type": "integer", "min": 0, "max": 511},
    "realm": {"type": "string", "max_length": 63},
    "pac-file-name": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "secure-web-proxy-cert": {
        "name": {
            "type": "string",
            "help": "Certificate list.",
            "default": "Fortinet_SSL",
            "max_length": 79,
        },
    },
    "pac-policy": {
        "policyid": {
            "type": "integer",
            "help": "Policy ID.",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 100,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable policy.",
            "default": "enable",
            "options": [{"help": "Enable policy.", "label": "Enable", "name": "enable"}, {"help": "Disable policy.", "label": "Disable", "name": "disable"}],
        },
        "srcaddr": {
            "type": "string",
            "help": "Source address objects.",
            "required": True,
        },
        "srcaddr6": {
            "type": "string",
            "help": "Source address6 objects.",
        },
        "dstaddr": {
            "type": "string",
            "help": "Destination address objects.",
            "required": True,
        },
        "pac-file-name": {
            "type": "string",
            "help": "Pac file name.",
            "required": True,
            "default": "proxy.pac",
            "max_length": 63,
        },
        "pac-file-data": {
            "type": "user",
            "help": "PAC file contents enclosed in quotes (maximum of 256K bytes).",
            "default": "",
        },
        "comments": {
            "type": "var-string",
            "help": "Optional comments.",
            "max_length": 1023,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable the explicit web proxy.
    "disable",  # Disable the explicit web proxy.
]
VALID_BODY_SECURE_WEB_PROXY = [
    "disable",  # Disable secure webproxy.
    "enable",  # Enable secure webproxy access.
    "secure",  # Require secure webproxy access.
]
VALID_BODY_FTP_OVER_HTTP = [
    "enable",  # Enable FTP-over-HTTP sessions.
    "disable",  # Disable FTP-over-HTTP sessions.
]
VALID_BODY_SOCKS = [
    "enable",  # Enable the SOCKS proxy.
    "disable",  # Disable the SOCKS proxy.
]
VALID_BODY_HTTP_CONNECTION_MODE = [
    "static",  # Only one server connection exists during the proxy session.
    "multiplex",  # Established connections are held until the proxy session ends.
    "serverpool",  # Established connections are shared with other proxy sessions.
]
VALID_BODY_CLIENT_CERT = [
    "disable",  # Disable client certificate request.
    "enable",  # Enable client certificate request.
]
VALID_BODY_USER_AGENT_DETECT = [
    "disable",  # Disable to detect unknown device by HTTP user-agent if no client certificate provided.
    "enable",  # Enable to detect unknown device by HTTP user-agent if no client certificate provided.
]
VALID_BODY_EMPTY_CERT_ACTION = [
    "accept",  # Accept the SSL handshake if the client certificate is empty.
    "block",  # Block the SSL handshake if the client certificate is empty.
    "accept-unmanageable",  # Accept the SSL handshake only if the end-point is unmanageable.
]
VALID_BODY_SSL_DH_BITS = [
    "768",  # 768-bit Diffie-Hellman prime.
    "1024",  # 1024-bit Diffie-Hellman prime.
    "1536",  # 1536-bit Diffie-Hellman prime.
    "2048",  # 2048-bit Diffie-Hellman prime.
]
VALID_BODY_INTERFACE_SELECT_METHOD = [
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_BODY_IPV6_STATUS = [
    "enable",  # Enable allowing an IPv6 web proxy destination.
    "disable",  # Disable allowing an IPv6 web proxy destination.
]
VALID_BODY_STRICT_GUEST = [
    "enable",  # Enable strict guest user checking.
    "disable",  # Disable strict guest user checking.
]
VALID_BODY_PREF_DNS_RESULT = [
    "ipv4",  # Send the IPv4 request first and then the IPv6 request. Use the DNS response that returns to the FortiGate first.
    "ipv6",  # Send the IPv6 request first and then the IPv4 request. Use the DNS response that returns to the FortiGate first.
    "ipv4-strict",  # Use the IPv4 DNS response. If the IPv6 DNS response arrives first, wait 50ms for the IPv4 response and then use the IPv4 response, otherwise the IPv6.
    "ipv6-strict",  # Use the IPv6 DNS response. If the IPv4 DNS response arrives first, wait 50ms for the IPv6 response and then use the IPv6 response, otherwise the IPv4.
]
VALID_BODY_UNKNOWN_HTTP_VERSION = [
    "reject",  # Reject or tear down HTTP sessions that do not use HTTP 0.9, 1.0, or 1.1.
    "best-effort",  # Assume all HTTP sessions comply with HTTP 0.9, 1.0, or 1.1. If a session uses a different HTTP version, it may not parse correctly and the connection may be lost.
]
VALID_BODY_SEC_DEFAULT_ACTION = [
    "accept",  # Accept requests. All explicit web proxy traffic is accepted whether there is an explicit web proxy policy or not.
    "deny",  # Deny requests unless there is a matching explicit web proxy policy.
]
VALID_BODY_HTTPS_REPLACEMENT_MESSAGE = [
    "enable",  # Display a replacement message for HTTPS requests.
    "disable",  # Do not display a replacement message for HTTPS requests.
]
VALID_BODY_MESSAGE_UPON_SERVER_ERROR = [
    "enable",  # Display a replacement message when a server error is detected.
    "disable",  # Do not display a replacement message when a server error is detected.
]
VALID_BODY_PAC_FILE_SERVER_STATUS = [
    "enable",  # Enable Proxy Auto-Configuration (PAC).
    "disable",  # Disable Proxy Auto-Configuration (PAC).
]
VALID_BODY_PAC_FILE_THROUGH_HTTPS = [
    "enable",  # Enable to get Proxy Auto-Configuration (PAC) through HTTPS.
    "disable",  # Disable to get Proxy Auto-Configuration (PAC) through HTTPS.
]
VALID_BODY_SSL_ALGORITHM = [
    "high",  # High encrption. Allow only AES and ChaCha.
    "medium",  # Medium encryption. Allow AES, ChaCha, 3DES, and RC4.
    "low",  # Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.
]
VALID_BODY_TRACE_AUTH_NO_RSP = [
    "enable",  # Enable logging timed-out authentication requests.
    "disable",  # Disable logging timed-out authentication requests.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_web_proxy_explicit_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for web_proxy/explicit."""
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
    """Validate required fields for web_proxy/explicit."""
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


def validate_web_proxy_explicit_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new web_proxy/explicit object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            desc = FIELD_DESCRIPTIONS.get("status", "")
            error_msg = f"Invalid value for 'status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STATUS)}"
            error_msg += f"\n  → Example: status='{{ VALID_BODY_STATUS[0] }}'"
            return (False, error_msg)
    if "secure-web-proxy" in payload:
        value = payload["secure-web-proxy"]
        if value not in VALID_BODY_SECURE_WEB_PROXY:
            desc = FIELD_DESCRIPTIONS.get("secure-web-proxy", "")
            error_msg = f"Invalid value for 'secure-web-proxy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURE_WEB_PROXY)}"
            error_msg += f"\n  → Example: secure-web-proxy='{{ VALID_BODY_SECURE_WEB_PROXY[0] }}'"
            return (False, error_msg)
    if "ftp-over-http" in payload:
        value = payload["ftp-over-http"]
        if value not in VALID_BODY_FTP_OVER_HTTP:
            desc = FIELD_DESCRIPTIONS.get("ftp-over-http", "")
            error_msg = f"Invalid value for 'ftp-over-http': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FTP_OVER_HTTP)}"
            error_msg += f"\n  → Example: ftp-over-http='{{ VALID_BODY_FTP_OVER_HTTP[0] }}'"
            return (False, error_msg)
    if "socks" in payload:
        value = payload["socks"]
        if value not in VALID_BODY_SOCKS:
            desc = FIELD_DESCRIPTIONS.get("socks", "")
            error_msg = f"Invalid value for 'socks': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SOCKS)}"
            error_msg += f"\n  → Example: socks='{{ VALID_BODY_SOCKS[0] }}'"
            return (False, error_msg)
    if "http-connection-mode" in payload:
        value = payload["http-connection-mode"]
        if value not in VALID_BODY_HTTP_CONNECTION_MODE:
            desc = FIELD_DESCRIPTIONS.get("http-connection-mode", "")
            error_msg = f"Invalid value for 'http-connection-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_CONNECTION_MODE)}"
            error_msg += f"\n  → Example: http-connection-mode='{{ VALID_BODY_HTTP_CONNECTION_MODE[0] }}'"
            return (False, error_msg)
    if "client-cert" in payload:
        value = payload["client-cert"]
        if value not in VALID_BODY_CLIENT_CERT:
            desc = FIELD_DESCRIPTIONS.get("client-cert", "")
            error_msg = f"Invalid value for 'client-cert': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLIENT_CERT)}"
            error_msg += f"\n  → Example: client-cert='{{ VALID_BODY_CLIENT_CERT[0] }}'"
            return (False, error_msg)
    if "user-agent-detect" in payload:
        value = payload["user-agent-detect"]
        if value not in VALID_BODY_USER_AGENT_DETECT:
            desc = FIELD_DESCRIPTIONS.get("user-agent-detect", "")
            error_msg = f"Invalid value for 'user-agent-detect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USER_AGENT_DETECT)}"
            error_msg += f"\n  → Example: user-agent-detect='{{ VALID_BODY_USER_AGENT_DETECT[0] }}'"
            return (False, error_msg)
    if "empty-cert-action" in payload:
        value = payload["empty-cert-action"]
        if value not in VALID_BODY_EMPTY_CERT_ACTION:
            desc = FIELD_DESCRIPTIONS.get("empty-cert-action", "")
            error_msg = f"Invalid value for 'empty-cert-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EMPTY_CERT_ACTION)}"
            error_msg += f"\n  → Example: empty-cert-action='{{ VALID_BODY_EMPTY_CERT_ACTION[0] }}'"
            return (False, error_msg)
    if "ssl-dh-bits" in payload:
        value = payload["ssl-dh-bits"]
        if value not in VALID_BODY_SSL_DH_BITS:
            desc = FIELD_DESCRIPTIONS.get("ssl-dh-bits", "")
            error_msg = f"Invalid value for 'ssl-dh-bits': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_DH_BITS)}"
            error_msg += f"\n  → Example: ssl-dh-bits='{{ VALID_BODY_SSL_DH_BITS[0] }}'"
            return (False, error_msg)
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("interface-select-method", "")
            error_msg = f"Invalid value for 'interface-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERFACE_SELECT_METHOD)}"
            error_msg += f"\n  → Example: interface-select-method='{{ VALID_BODY_INTERFACE_SELECT_METHOD[0] }}'"
            return (False, error_msg)
    if "ipv6-status" in payload:
        value = payload["ipv6-status"]
        if value not in VALID_BODY_IPV6_STATUS:
            desc = FIELD_DESCRIPTIONS.get("ipv6-status", "")
            error_msg = f"Invalid value for 'ipv6-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPV6_STATUS)}"
            error_msg += f"\n  → Example: ipv6-status='{{ VALID_BODY_IPV6_STATUS[0] }}'"
            return (False, error_msg)
    if "strict-guest" in payload:
        value = payload["strict-guest"]
        if value not in VALID_BODY_STRICT_GUEST:
            desc = FIELD_DESCRIPTIONS.get("strict-guest", "")
            error_msg = f"Invalid value for 'strict-guest': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STRICT_GUEST)}"
            error_msg += f"\n  → Example: strict-guest='{{ VALID_BODY_STRICT_GUEST[0] }}'"
            return (False, error_msg)
    if "pref-dns-result" in payload:
        value = payload["pref-dns-result"]
        if value not in VALID_BODY_PREF_DNS_RESULT:
            desc = FIELD_DESCRIPTIONS.get("pref-dns-result", "")
            error_msg = f"Invalid value for 'pref-dns-result': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PREF_DNS_RESULT)}"
            error_msg += f"\n  → Example: pref-dns-result='{{ VALID_BODY_PREF_DNS_RESULT[0] }}'"
            return (False, error_msg)
    if "unknown-http-version" in payload:
        value = payload["unknown-http-version"]
        if value not in VALID_BODY_UNKNOWN_HTTP_VERSION:
            desc = FIELD_DESCRIPTIONS.get("unknown-http-version", "")
            error_msg = f"Invalid value for 'unknown-http-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UNKNOWN_HTTP_VERSION)}"
            error_msg += f"\n  → Example: unknown-http-version='{{ VALID_BODY_UNKNOWN_HTTP_VERSION[0] }}'"
            return (False, error_msg)
    if "sec-default-action" in payload:
        value = payload["sec-default-action"]
        if value not in VALID_BODY_SEC_DEFAULT_ACTION:
            desc = FIELD_DESCRIPTIONS.get("sec-default-action", "")
            error_msg = f"Invalid value for 'sec-default-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SEC_DEFAULT_ACTION)}"
            error_msg += f"\n  → Example: sec-default-action='{{ VALID_BODY_SEC_DEFAULT_ACTION[0] }}'"
            return (False, error_msg)
    if "https-replacement-message" in payload:
        value = payload["https-replacement-message"]
        if value not in VALID_BODY_HTTPS_REPLACEMENT_MESSAGE:
            desc = FIELD_DESCRIPTIONS.get("https-replacement-message", "")
            error_msg = f"Invalid value for 'https-replacement-message': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTPS_REPLACEMENT_MESSAGE)}"
            error_msg += f"\n  → Example: https-replacement-message='{{ VALID_BODY_HTTPS_REPLACEMENT_MESSAGE[0] }}'"
            return (False, error_msg)
    if "message-upon-server-error" in payload:
        value = payload["message-upon-server-error"]
        if value not in VALID_BODY_MESSAGE_UPON_SERVER_ERROR:
            desc = FIELD_DESCRIPTIONS.get("message-upon-server-error", "")
            error_msg = f"Invalid value for 'message-upon-server-error': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MESSAGE_UPON_SERVER_ERROR)}"
            error_msg += f"\n  → Example: message-upon-server-error='{{ VALID_BODY_MESSAGE_UPON_SERVER_ERROR[0] }}'"
            return (False, error_msg)
    if "pac-file-server-status" in payload:
        value = payload["pac-file-server-status"]
        if value not in VALID_BODY_PAC_FILE_SERVER_STATUS:
            desc = FIELD_DESCRIPTIONS.get("pac-file-server-status", "")
            error_msg = f"Invalid value for 'pac-file-server-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PAC_FILE_SERVER_STATUS)}"
            error_msg += f"\n  → Example: pac-file-server-status='{{ VALID_BODY_PAC_FILE_SERVER_STATUS[0] }}'"
            return (False, error_msg)
    if "pac-file-through-https" in payload:
        value = payload["pac-file-through-https"]
        if value not in VALID_BODY_PAC_FILE_THROUGH_HTTPS:
            desc = FIELD_DESCRIPTIONS.get("pac-file-through-https", "")
            error_msg = f"Invalid value for 'pac-file-through-https': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PAC_FILE_THROUGH_HTTPS)}"
            error_msg += f"\n  → Example: pac-file-through-https='{{ VALID_BODY_PAC_FILE_THROUGH_HTTPS[0] }}'"
            return (False, error_msg)
    if "ssl-algorithm" in payload:
        value = payload["ssl-algorithm"]
        if value not in VALID_BODY_SSL_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("ssl-algorithm", "")
            error_msg = f"Invalid value for 'ssl-algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_ALGORITHM)}"
            error_msg += f"\n  → Example: ssl-algorithm='{{ VALID_BODY_SSL_ALGORITHM[0] }}'"
            return (False, error_msg)
    if "trace-auth-no-rsp" in payload:
        value = payload["trace-auth-no-rsp"]
        if value not in VALID_BODY_TRACE_AUTH_NO_RSP:
            desc = FIELD_DESCRIPTIONS.get("trace-auth-no-rsp", "")
            error_msg = f"Invalid value for 'trace-auth-no-rsp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRACE_AUTH_NO_RSP)}"
            error_msg += f"\n  → Example: trace-auth-no-rsp='{{ VALID_BODY_TRACE_AUTH_NO_RSP[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_web_proxy_explicit_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update web_proxy/explicit."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "secure-web-proxy" in payload:
        value = payload["secure-web-proxy"]
        if value not in VALID_BODY_SECURE_WEB_PROXY:
            return (
                False,
                f"Invalid value for 'secure-web-proxy'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURE_WEB_PROXY)}",
            )
    if "ftp-over-http" in payload:
        value = payload["ftp-over-http"]
        if value not in VALID_BODY_FTP_OVER_HTTP:
            return (
                False,
                f"Invalid value for 'ftp-over-http'='{value}'. Must be one of: {', '.join(VALID_BODY_FTP_OVER_HTTP)}",
            )
    if "socks" in payload:
        value = payload["socks"]
        if value not in VALID_BODY_SOCKS:
            return (
                False,
                f"Invalid value for 'socks'='{value}'. Must be one of: {', '.join(VALID_BODY_SOCKS)}",
            )
    if "http-connection-mode" in payload:
        value = payload["http-connection-mode"]
        if value not in VALID_BODY_HTTP_CONNECTION_MODE:
            return (
                False,
                f"Invalid value for 'http-connection-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_CONNECTION_MODE)}",
            )
    if "client-cert" in payload:
        value = payload["client-cert"]
        if value not in VALID_BODY_CLIENT_CERT:
            return (
                False,
                f"Invalid value for 'client-cert'='{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_CERT)}",
            )
    if "user-agent-detect" in payload:
        value = payload["user-agent-detect"]
        if value not in VALID_BODY_USER_AGENT_DETECT:
            return (
                False,
                f"Invalid value for 'user-agent-detect'='{value}'. Must be one of: {', '.join(VALID_BODY_USER_AGENT_DETECT)}",
            )
    if "empty-cert-action" in payload:
        value = payload["empty-cert-action"]
        if value not in VALID_BODY_EMPTY_CERT_ACTION:
            return (
                False,
                f"Invalid value for 'empty-cert-action'='{value}'. Must be one of: {', '.join(VALID_BODY_EMPTY_CERT_ACTION)}",
            )
    if "ssl-dh-bits" in payload:
        value = payload["ssl-dh-bits"]
        if value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid value for 'ssl-dh-bits'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )
    if "interface-select-method" in payload:
        value = payload["interface-select-method"]
        if value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )
    if "ipv6-status" in payload:
        value = payload["ipv6-status"]
        if value not in VALID_BODY_IPV6_STATUS:
            return (
                False,
                f"Invalid value for 'ipv6-status'='{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_STATUS)}",
            )
    if "strict-guest" in payload:
        value = payload["strict-guest"]
        if value not in VALID_BODY_STRICT_GUEST:
            return (
                False,
                f"Invalid value for 'strict-guest'='{value}'. Must be one of: {', '.join(VALID_BODY_STRICT_GUEST)}",
            )
    if "pref-dns-result" in payload:
        value = payload["pref-dns-result"]
        if value not in VALID_BODY_PREF_DNS_RESULT:
            return (
                False,
                f"Invalid value for 'pref-dns-result'='{value}'. Must be one of: {', '.join(VALID_BODY_PREF_DNS_RESULT)}",
            )
    if "unknown-http-version" in payload:
        value = payload["unknown-http-version"]
        if value not in VALID_BODY_UNKNOWN_HTTP_VERSION:
            return (
                False,
                f"Invalid value for 'unknown-http-version'='{value}'. Must be one of: {', '.join(VALID_BODY_UNKNOWN_HTTP_VERSION)}",
            )
    if "sec-default-action" in payload:
        value = payload["sec-default-action"]
        if value not in VALID_BODY_SEC_DEFAULT_ACTION:
            return (
                False,
                f"Invalid value for 'sec-default-action'='{value}'. Must be one of: {', '.join(VALID_BODY_SEC_DEFAULT_ACTION)}",
            )
    if "https-replacement-message" in payload:
        value = payload["https-replacement-message"]
        if value not in VALID_BODY_HTTPS_REPLACEMENT_MESSAGE:
            return (
                False,
                f"Invalid value for 'https-replacement-message'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_REPLACEMENT_MESSAGE)}",
            )
    if "message-upon-server-error" in payload:
        value = payload["message-upon-server-error"]
        if value not in VALID_BODY_MESSAGE_UPON_SERVER_ERROR:
            return (
                False,
                f"Invalid value for 'message-upon-server-error'='{value}'. Must be one of: {', '.join(VALID_BODY_MESSAGE_UPON_SERVER_ERROR)}",
            )
    if "pac-file-server-status" in payload:
        value = payload["pac-file-server-status"]
        if value not in VALID_BODY_PAC_FILE_SERVER_STATUS:
            return (
                False,
                f"Invalid value for 'pac-file-server-status'='{value}'. Must be one of: {', '.join(VALID_BODY_PAC_FILE_SERVER_STATUS)}",
            )
    if "pac-file-through-https" in payload:
        value = payload["pac-file-through-https"]
        if value not in VALID_BODY_PAC_FILE_THROUGH_HTTPS:
            return (
                False,
                f"Invalid value for 'pac-file-through-https'='{value}'. Must be one of: {', '.join(VALID_BODY_PAC_FILE_THROUGH_HTTPS)}",
            )
    if "ssl-algorithm" in payload:
        value = payload["ssl-algorithm"]
        if value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid value for 'ssl-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )
    if "trace-auth-no-rsp" in payload:
        value = payload["trace-auth-no-rsp"]
        if value not in VALID_BODY_TRACE_AUTH_NO_RSP:
            return (
                False,
                f"Invalid value for 'trace-auth-no-rsp'='{value}'. Must be one of: {', '.join(VALID_BODY_TRACE_AUTH_NO_RSP)}",
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
    "endpoint": "web_proxy/explicit",
    "category": "cmdb",
    "api_path": "web-proxy/explicit",
    "help": "Configure explicit Web proxy settings.",
    "total_fields": 38,
    "required_fields_count": 1,
    "fields_with_defaults_count": 36,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
