"""
Validation helpers for firewall/ssl_ssh_profile endpoint.

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
    "name",  # Name.
    "ssl-server",  # SSL server settings used for client certificate request.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "allowlist": "disable",
    "block-blocklisted-certificates": "enable",
    "server-cert-mode": "re-sign",
    "use-ssl-server": "disable",
    "caname": "Fortinet_CA_SSL",
    "untrusted-caname": "Fortinet_CA_Untrusted",
    "ssl-exemption-ip-rating": "enable",
    "ssl-exemption-log": "disable",
    "ssl-anomaly-log": "enable",
    "ssl-negotiation-log": "enable",
    "ssl-server-cert-log": "disable",
    "ssl-handshake-log": "disable",
    "rpc-over-https": "disable",
    "mapi-over-https": "disable",
    "supported-alpn": "all",
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
    "name": "string",  # Name.
    "comment": "var-string",  # Optional comments.
    "ssl": "string",  # Configure SSL options.
    "https": "string",  # Configure HTTPS options.
    "ftps": "string",  # Configure FTPS options.
    "imaps": "string",  # Configure IMAPS options.
    "pop3s": "string",  # Configure POP3S options.
    "smtps": "string",  # Configure SMTPS options.
    "ssh": "string",  # Configure SSH options.
    "dot": "string",  # Configure DNS over TLS options.
    "allowlist": "option",  # Enable/disable exempting servers by FortiGuard allowlist.
    "block-blocklisted-certificates": "option",  # Enable/disable blocking SSL-based botnet communication by Fo
    "ssl-exempt": "string",  # Servers to exempt from SSL inspection.
    "ech-outer-sni": "string",  # ClientHelloOuter SNIs to be blocked.
    "server-cert-mode": "option",  # Re-sign or replace the server's certificate.
    "use-ssl-server": "option",  # Enable/disable the use of SSL server table for SSL offloadin
    "caname": "string",  # CA certificate used by SSL Inspection.
    "untrusted-caname": "string",  # Untrusted CA certificate used by SSL Inspection.
    "server-cert": "string",  # Certificate used by SSL Inspection to replace server certifi
    "ssl-server": "string",  # SSL server settings used for client certificate request.
    "ssl-exemption-ip-rating": "option",  # Enable/disable IP based URL rating.
    "ssl-exemption-log": "option",  # Enable/disable logging of SSL exemptions.
    "ssl-anomaly-log": "option",  # Enable/disable logging of SSL anomalies.
    "ssl-negotiation-log": "option",  # Enable/disable logging of SSL negotiation events.
    "ssl-server-cert-log": "option",  # Enable/disable logging of server certificate information.
    "ssl-handshake-log": "option",  # Enable/disable logging of TLS handshakes.
    "rpc-over-https": "option",  # Enable/disable inspection of RPC over HTTPS.
    "mapi-over-https": "option",  # Enable/disable inspection of MAPI over HTTPS.
    "supported-alpn": "option",  # Configure ALPN option.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Name.",
    "comment": "Optional comments.",
    "ssl": "Configure SSL options.",
    "https": "Configure HTTPS options.",
    "ftps": "Configure FTPS options.",
    "imaps": "Configure IMAPS options.",
    "pop3s": "Configure POP3S options.",
    "smtps": "Configure SMTPS options.",
    "ssh": "Configure SSH options.",
    "dot": "Configure DNS over TLS options.",
    "allowlist": "Enable/disable exempting servers by FortiGuard allowlist.",
    "block-blocklisted-certificates": "Enable/disable blocking SSL-based botnet communication by FortiGuard certificate blocklist.",
    "ssl-exempt": "Servers to exempt from SSL inspection.",
    "ech-outer-sni": "ClientHelloOuter SNIs to be blocked.",
    "server-cert-mode": "Re-sign or replace the server's certificate.",
    "use-ssl-server": "Enable/disable the use of SSL server table for SSL offloading.",
    "caname": "CA certificate used by SSL Inspection.",
    "untrusted-caname": "Untrusted CA certificate used by SSL Inspection.",
    "server-cert": "Certificate used by SSL Inspection to replace server certificate.",
    "ssl-server": "SSL server settings used for client certificate request.",
    "ssl-exemption-ip-rating": "Enable/disable IP based URL rating.",
    "ssl-exemption-log": "Enable/disable logging of SSL exemptions.",
    "ssl-anomaly-log": "Enable/disable logging of SSL anomalies.",
    "ssl-negotiation-log": "Enable/disable logging of SSL negotiation events.",
    "ssl-server-cert-log": "Enable/disable logging of server certificate information.",
    "ssl-handshake-log": "Enable/disable logging of TLS handshakes.",
    "rpc-over-https": "Enable/disable inspection of RPC over HTTPS.",
    "mapi-over-https": "Enable/disable inspection of MAPI over HTTPS.",
    "supported-alpn": "Configure ALPN option.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 47},
    "caname": {"type": "string", "max_length": 35},
    "untrusted-caname": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "ssl": {
        "inspect-all": {
            "type": "option",
            "help": "Level of SSL inspection.",
            "default": "disable",
            "options": ["disable", "certificate-inspection", "deep-inspection"],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "bypass",
            "options": ["bypass", "inspect", "block"],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": ["enable", "strict", "disable"],
        },
        "cert-probe-failure": {
            "type": "option",
            "help": "Action based on certificate probe failure.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "encrypted-client-hello": {
            "type": "option",
            "help": "Block/allow session based on existence of encrypted-client-hello.",
            "default": "block",
            "options": ["allow", "block"],
        },
        "min-allowed-ssl-version": {
            "type": "option",
            "help": "Minimum SSL version to be allowed.",
            "default": "tls-1.1",
            "options": ["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"],
        },
    },
    "https": {
        "ports": {
            "type": "integer",
            "help": "Ports to use for scanning (1 - 65535, default = 443).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Configure protocol inspection status.",
            "default": "deep-inspection",
            "options": ["disable", "certificate-inspection", "deep-inspection"],
        },
        "quic": {
            "type": "option",
            "help": "QUIC inspection status (default = inspect).",
            "default": "inspect",
            "options": ["inspect", "bypass", "block"],
        },
        "udp-not-quic": {
            "type": "option",
            "help": "Action to be taken when matched UDP packet is not QUIC.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "bypass",
            "options": ["bypass", "inspect", "block"],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": ["enable", "strict", "disable"],
        },
        "cert-probe-failure": {
            "type": "option",
            "help": "Action based on certificate probe failure.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "encrypted-client-hello": {
            "type": "option",
            "help": "Block/allow session based on existence of encrypted-client-hello.",
            "default": "block",
            "options": ["allow", "block"],
        },
        "min-allowed-ssl-version": {
            "type": "option",
            "help": "Minimum SSL version to be allowed.",
            "default": "tls-1.1",
            "options": ["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"],
        },
    },
    "ftps": {
        "ports": {
            "type": "integer",
            "help": "Ports to use for scanning (1 - 65535, default = 443).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Configure protocol inspection status.",
            "default": "deep-inspection",
            "options": ["disable", "deep-inspection"],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "bypass",
            "options": ["bypass", "inspect", "block"],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": ["enable", "strict", "disable"],
        },
        "min-allowed-ssl-version": {
            "type": "option",
            "help": "Minimum SSL version to be allowed.",
            "default": "tls-1.1",
            "options": ["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"],
        },
    },
    "imaps": {
        "ports": {
            "type": "integer",
            "help": "Ports to use for scanning (1 - 65535, default = 443).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Configure protocol inspection status.",
            "default": "deep-inspection",
            "options": ["disable", "deep-inspection"],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "inspect",
            "options": ["bypass", "inspect", "block"],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": ["enable", "strict", "disable"],
        },
    },
    "pop3s": {
        "ports": {
            "type": "integer",
            "help": "Ports to use for scanning (1 - 65535, default = 443).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Configure protocol inspection status.",
            "default": "deep-inspection",
            "options": ["disable", "deep-inspection"],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "inspect",
            "options": ["bypass", "inspect", "block"],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": ["enable", "strict", "disable"],
        },
    },
    "smtps": {
        "ports": {
            "type": "integer",
            "help": "Ports to use for scanning (1 - 65535, default = 443).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Configure protocol inspection status.",
            "default": "deep-inspection",
            "options": ["disable", "deep-inspection"],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "inspect",
            "options": ["bypass", "inspect", "block"],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": ["enable", "strict", "disable"],
        },
    },
    "ssh": {
        "ports": {
            "type": "integer",
            "help": "Ports to use for scanning (1 - 65535, default = 443).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Configure protocol inspection status.",
            "default": "disable",
            "options": ["disable", "deep-inspection"],
        },
        "inspect-all": {
            "type": "option",
            "help": "Level of SSL inspection.",
            "default": "disable",
            "options": ["disable", "deep-inspection"],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "unsupported-version": {
            "type": "option",
            "help": "Action based on SSH version being unsupported.",
            "default": "bypass",
            "options": ["bypass", "block"],
        },
        "ssh-tun-policy-check": {
            "type": "option",
            "help": "Enable/disable SSH tunnel policy check.",
            "default": "disable",
            "options": ["disable", "enable"],
        },
        "ssh-algorithm": {
            "type": "option",
            "help": "Relative strength of encryption algorithms accepted during negotiation.",
            "default": "compatible",
            "options": ["compatible", "high-encryption"],
        },
    },
    "dot": {
        "status": {
            "type": "option",
            "help": "Configure protocol inspection status.",
            "default": "disable",
            "options": ["disable", "deep-inspection"],
        },
        "quic": {
            "type": "option",
            "help": "QUIC inspection status (default = inspect).",
            "default": "inspect",
            "options": ["inspect", "bypass", "block"],
        },
        "udp-not-quic": {
            "type": "option",
            "help": "Action to be taken when matched UDP packet is not QUIC.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "bypass",
            "options": ["bypass", "inspect", "block"],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": ["allow", "block"],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": ["allow", "block", "ignore"],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": ["allow", "block", "ignore"],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": ["enable", "strict", "disable"],
        },
    },
    "ssl-exempt": {
        "id": {
            "type": "integer",
            "help": "ID number.",
            "default": 0,
            "min_value": 0,
            "max_value": 512,
        },
        "type": {
            "type": "option",
            "help": "Type of address object (IPv4 or IPv6) or FortiGuard category.",
            "required": True,
            "default": "fortiguard-category",
            "options": ["fortiguard-category", "address", "address6", "wildcard-fqdn", "regex"],
        },
        "fortiguard-category": {
            "type": "integer",
            "help": "FortiGuard category ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "address": {
            "type": "string",
            "help": "IPv4 address object.",
            "default": "",
            "max_length": 79,
        },
        "address6": {
            "type": "string",
            "help": "IPv6 address object.",
            "default": "",
            "max_length": 79,
        },
        "wildcard-fqdn": {
            "type": "string",
            "help": "Exempt servers by wildcard FQDN.",
            "default": "",
            "max_length": 79,
        },
        "regex": {
            "type": "string",
            "help": "Exempt servers by regular expression.",
            "default": "",
            "max_length": 255,
        },
    },
    "ech-outer-sni": {
        "name": {
            "type": "string",
            "help": "ClientHelloOuter SNI name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
        "sni": {
            "type": "string",
            "help": "ClientHelloOuter SNI to be blocked.",
            "required": True,
            "default": "",
            "max_length": 255,
        },
    },
    "server-cert": {
        "name": {
            "type": "string",
            "help": "Certificate list.",
            "default": "Fortinet_SSL",
            "max_length": 79,
        },
    },
    "ssl-server": {
        "id": {
            "type": "integer",
            "help": "SSL server ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ip": {
            "type": "ipv4-address-any",
            "help": "IPv4 address of the SSL server.",
            "required": True,
            "default": "0.0.0.0",
        },
        "https-client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate during the HTTPS handshake.",
            "default": "bypass",
            "options": ["bypass", "inspect", "block"],
        },
        "smtps-client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate during the SMTPS handshake.",
            "default": "bypass",
            "options": ["bypass", "inspect", "block"],
        },
        "pop3s-client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate during the POP3S handshake.",
            "default": "bypass",
            "options": ["bypass", "inspect", "block"],
        },
        "imaps-client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate during the IMAPS handshake.",
            "default": "bypass",
            "options": ["bypass", "inspect", "block"],
        },
        "ftps-client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate during the FTPS handshake.",
            "default": "bypass",
            "options": ["bypass", "inspect", "block"],
        },
        "ssl-other-client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate during an SSL protocol handshake.",
            "default": "bypass",
            "options": ["bypass", "inspect", "block"],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_ALLOWLIST = [
    "enable",
    "disable",
]
VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES = [
    "disable",
    "enable",
]
VALID_BODY_SERVER_CERT_MODE = [
    "re-sign",
    "replace",
]
VALID_BODY_USE_SSL_SERVER = [
    "disable",
    "enable",
]
VALID_BODY_SSL_EXEMPTION_IP_RATING = [
    "enable",
    "disable",
]
VALID_BODY_SSL_EXEMPTION_LOG = [
    "disable",
    "enable",
]
VALID_BODY_SSL_ANOMALY_LOG = [
    "disable",
    "enable",
]
VALID_BODY_SSL_NEGOTIATION_LOG = [
    "disable",
    "enable",
]
VALID_BODY_SSL_SERVER_CERT_LOG = [
    "disable",
    "enable",
]
VALID_BODY_SSL_HANDSHAKE_LOG = [
    "disable",
    "enable",
]
VALID_BODY_RPC_OVER_HTTPS = [
    "enable",
    "disable",
]
VALID_BODY_MAPI_OVER_HTTPS = [
    "enable",
    "disable",
]
VALID_BODY_SUPPORTED_ALPN = [
    "http1-1",
    "http2",
    "all",
    "none",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_ssl_ssh_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for firewall/ssl_ssh_profile.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_firewall_ssl_ssh_profile_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_firewall_ssl_ssh_profile_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_firewall_ssl_ssh_profile_get(
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
    Validate required fields for firewall/ssl_ssh_profile.

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


def validate_firewall_ssl_ssh_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new firewall/ssl_ssh_profile object.

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
        ...     "name": True,  # Name.
        ...     "ssl-server": True,  # SSL server settings used for client certificate re
        ... }
        >>> is_valid, error = validate_firewall_ssl_ssh_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "name": True,
        ...     "allowlist": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_firewall_ssl_ssh_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["allowlist"] = "invalid-value"
        >>> is_valid, error = validate_firewall_ssl_ssh_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_firewall_ssl_ssh_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "allowlist" in payload:
        value = payload["allowlist"]
        if value not in VALID_BODY_ALLOWLIST:
            desc = FIELD_DESCRIPTIONS.get("allowlist", "")
            error_msg = f"Invalid value for 'allowlist': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOWLIST)}"
            error_msg += f"\n  → Example: allowlist='{{ VALID_BODY_ALLOWLIST[0] }}'"
            return (False, error_msg)
    if "block-blocklisted-certificates" in payload:
        value = payload["block-blocklisted-certificates"]
        if value not in VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES:
            desc = FIELD_DESCRIPTIONS.get("block-blocklisted-certificates", "")
            error_msg = f"Invalid value for 'block-blocklisted-certificates': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES)}"
            error_msg += f"\n  → Example: block-blocklisted-certificates='{{ VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES[0] }}'"
            return (False, error_msg)
    if "server-cert-mode" in payload:
        value = payload["server-cert-mode"]
        if value not in VALID_BODY_SERVER_CERT_MODE:
            desc = FIELD_DESCRIPTIONS.get("server-cert-mode", "")
            error_msg = f"Invalid value for 'server-cert-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_CERT_MODE)}"
            error_msg += f"\n  → Example: server-cert-mode='{{ VALID_BODY_SERVER_CERT_MODE[0] }}'"
            return (False, error_msg)
    if "use-ssl-server" in payload:
        value = payload["use-ssl-server"]
        if value not in VALID_BODY_USE_SSL_SERVER:
            desc = FIELD_DESCRIPTIONS.get("use-ssl-server", "")
            error_msg = f"Invalid value for 'use-ssl-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USE_SSL_SERVER)}"
            error_msg += f"\n  → Example: use-ssl-server='{{ VALID_BODY_USE_SSL_SERVER[0] }}'"
            return (False, error_msg)
    if "ssl-exemption-ip-rating" in payload:
        value = payload["ssl-exemption-ip-rating"]
        if value not in VALID_BODY_SSL_EXEMPTION_IP_RATING:
            desc = FIELD_DESCRIPTIONS.get("ssl-exemption-ip-rating", "")
            error_msg = f"Invalid value for 'ssl-exemption-ip-rating': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_EXEMPTION_IP_RATING)}"
            error_msg += f"\n  → Example: ssl-exemption-ip-rating='{{ VALID_BODY_SSL_EXEMPTION_IP_RATING[0] }}'"
            return (False, error_msg)
    if "ssl-exemption-log" in payload:
        value = payload["ssl-exemption-log"]
        if value not in VALID_BODY_SSL_EXEMPTION_LOG:
            desc = FIELD_DESCRIPTIONS.get("ssl-exemption-log", "")
            error_msg = f"Invalid value for 'ssl-exemption-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_EXEMPTION_LOG)}"
            error_msg += f"\n  → Example: ssl-exemption-log='{{ VALID_BODY_SSL_EXEMPTION_LOG[0] }}'"
            return (False, error_msg)
    if "ssl-anomaly-log" in payload:
        value = payload["ssl-anomaly-log"]
        if value not in VALID_BODY_SSL_ANOMALY_LOG:
            desc = FIELD_DESCRIPTIONS.get("ssl-anomaly-log", "")
            error_msg = f"Invalid value for 'ssl-anomaly-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_ANOMALY_LOG)}"
            error_msg += f"\n  → Example: ssl-anomaly-log='{{ VALID_BODY_SSL_ANOMALY_LOG[0] }}'"
            return (False, error_msg)
    if "ssl-negotiation-log" in payload:
        value = payload["ssl-negotiation-log"]
        if value not in VALID_BODY_SSL_NEGOTIATION_LOG:
            desc = FIELD_DESCRIPTIONS.get("ssl-negotiation-log", "")
            error_msg = f"Invalid value for 'ssl-negotiation-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_NEGOTIATION_LOG)}"
            error_msg += f"\n  → Example: ssl-negotiation-log='{{ VALID_BODY_SSL_NEGOTIATION_LOG[0] }}'"
            return (False, error_msg)
    if "ssl-server-cert-log" in payload:
        value = payload["ssl-server-cert-log"]
        if value not in VALID_BODY_SSL_SERVER_CERT_LOG:
            desc = FIELD_DESCRIPTIONS.get("ssl-server-cert-log", "")
            error_msg = f"Invalid value for 'ssl-server-cert-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_SERVER_CERT_LOG)}"
            error_msg += f"\n  → Example: ssl-server-cert-log='{{ VALID_BODY_SSL_SERVER_CERT_LOG[0] }}'"
            return (False, error_msg)
    if "ssl-handshake-log" in payload:
        value = payload["ssl-handshake-log"]
        if value not in VALID_BODY_SSL_HANDSHAKE_LOG:
            desc = FIELD_DESCRIPTIONS.get("ssl-handshake-log", "")
            error_msg = f"Invalid value for 'ssl-handshake-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_HANDSHAKE_LOG)}"
            error_msg += f"\n  → Example: ssl-handshake-log='{{ VALID_BODY_SSL_HANDSHAKE_LOG[0] }}'"
            return (False, error_msg)
    if "rpc-over-https" in payload:
        value = payload["rpc-over-https"]
        if value not in VALID_BODY_RPC_OVER_HTTPS:
            desc = FIELD_DESCRIPTIONS.get("rpc-over-https", "")
            error_msg = f"Invalid value for 'rpc-over-https': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RPC_OVER_HTTPS)}"
            error_msg += f"\n  → Example: rpc-over-https='{{ VALID_BODY_RPC_OVER_HTTPS[0] }}'"
            return (False, error_msg)
    if "mapi-over-https" in payload:
        value = payload["mapi-over-https"]
        if value not in VALID_BODY_MAPI_OVER_HTTPS:
            desc = FIELD_DESCRIPTIONS.get("mapi-over-https", "")
            error_msg = f"Invalid value for 'mapi-over-https': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAPI_OVER_HTTPS)}"
            error_msg += f"\n  → Example: mapi-over-https='{{ VALID_BODY_MAPI_OVER_HTTPS[0] }}'"
            return (False, error_msg)
    if "supported-alpn" in payload:
        value = payload["supported-alpn"]
        if value not in VALID_BODY_SUPPORTED_ALPN:
            desc = FIELD_DESCRIPTIONS.get("supported-alpn", "")
            error_msg = f"Invalid value for 'supported-alpn': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SUPPORTED_ALPN)}"
            error_msg += f"\n  → Example: supported-alpn='{{ VALID_BODY_SUPPORTED_ALPN[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_ssl_ssh_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update firewall/ssl_ssh_profile.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_firewall_ssl_ssh_profile_put(payload)
    """
    # Step 1: Validate enum values
    if "allowlist" in payload:
        value = payload["allowlist"]
        if value not in VALID_BODY_ALLOWLIST:
            return (
                False,
                f"Invalid value for 'allowlist'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWLIST)}",
            )
    if "block-blocklisted-certificates" in payload:
        value = payload["block-blocklisted-certificates"]
        if value not in VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES:
            return (
                False,
                f"Invalid value for 'block-blocklisted-certificates'='{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES)}",
            )
    if "server-cert-mode" in payload:
        value = payload["server-cert-mode"]
        if value not in VALID_BODY_SERVER_CERT_MODE:
            return (
                False,
                f"Invalid value for 'server-cert-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_CERT_MODE)}",
            )
    if "use-ssl-server" in payload:
        value = payload["use-ssl-server"]
        if value not in VALID_BODY_USE_SSL_SERVER:
            return (
                False,
                f"Invalid value for 'use-ssl-server'='{value}'. Must be one of: {', '.join(VALID_BODY_USE_SSL_SERVER)}",
            )
    if "ssl-exemption-ip-rating" in payload:
        value = payload["ssl-exemption-ip-rating"]
        if value not in VALID_BODY_SSL_EXEMPTION_IP_RATING:
            return (
                False,
                f"Invalid value for 'ssl-exemption-ip-rating'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_EXEMPTION_IP_RATING)}",
            )
    if "ssl-exemption-log" in payload:
        value = payload["ssl-exemption-log"]
        if value not in VALID_BODY_SSL_EXEMPTION_LOG:
            return (
                False,
                f"Invalid value for 'ssl-exemption-log'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_EXEMPTION_LOG)}",
            )
    if "ssl-anomaly-log" in payload:
        value = payload["ssl-anomaly-log"]
        if value not in VALID_BODY_SSL_ANOMALY_LOG:
            return (
                False,
                f"Invalid value for 'ssl-anomaly-log'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ANOMALY_LOG)}",
            )
    if "ssl-negotiation-log" in payload:
        value = payload["ssl-negotiation-log"]
        if value not in VALID_BODY_SSL_NEGOTIATION_LOG:
            return (
                False,
                f"Invalid value for 'ssl-negotiation-log'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_NEGOTIATION_LOG)}",
            )
    if "ssl-server-cert-log" in payload:
        value = payload["ssl-server-cert-log"]
        if value not in VALID_BODY_SSL_SERVER_CERT_LOG:
            return (
                False,
                f"Invalid value for 'ssl-server-cert-log'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_CERT_LOG)}",
            )
    if "ssl-handshake-log" in payload:
        value = payload["ssl-handshake-log"]
        if value not in VALID_BODY_SSL_HANDSHAKE_LOG:
            return (
                False,
                f"Invalid value for 'ssl-handshake-log'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HANDSHAKE_LOG)}",
            )
    if "rpc-over-https" in payload:
        value = payload["rpc-over-https"]
        if value not in VALID_BODY_RPC_OVER_HTTPS:
            return (
                False,
                f"Invalid value for 'rpc-over-https'='{value}'. Must be one of: {', '.join(VALID_BODY_RPC_OVER_HTTPS)}",
            )
    if "mapi-over-https" in payload:
        value = payload["mapi-over-https"]
        if value not in VALID_BODY_MAPI_OVER_HTTPS:
            return (
                False,
                f"Invalid value for 'mapi-over-https'='{value}'. Must be one of: {', '.join(VALID_BODY_MAPI_OVER_HTTPS)}",
            )
    if "supported-alpn" in payload:
        value = payload["supported-alpn"]
        if value not in VALID_BODY_SUPPORTED_ALPN:
            return (
                False,
                f"Invalid value for 'supported-alpn'='{value}'. Must be one of: {', '.join(VALID_BODY_SUPPORTED_ALPN)}",
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
    "endpoint": "firewall/ssl_ssh_profile",
    "category": "cmdb",
    "api_path": "firewall/ssl-ssh-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure SSL/SSH protocol options.",
    "total_fields": 29,
    "required_fields_count": 2,
    "fields_with_defaults_count": 16,
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
