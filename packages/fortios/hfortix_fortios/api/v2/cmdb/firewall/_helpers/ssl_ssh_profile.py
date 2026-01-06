"""Validation helpers for firewall/ssl_ssh_profile - Auto-generated"""

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
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Inspect SSL handshake only.", "label": "Certificate Inspection", "name": "certificate-inspection"}, {"help": "Full SSL inspection.", "label": "Deep Inspection", "name": "deep-inspection"}],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "bypass",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": [{"help": "Bypass the session when the version is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the version is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the cipher is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the cipher is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the negotiation is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the negotiation is not supported.", "label": "Block", "name": "block"}],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": [{"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, use the CN in the server certificate to do URL filtering.", "label": "Enable", "name": "enable"}, {"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, close the connection.", "label": "Strict", "name": "strict"}, {"help": "Do not check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.", "label": "Disable", "name": "disable"}],
        },
        "cert-probe-failure": {
            "type": "option",
            "help": "Action based on certificate probe failure.",
            "default": "allow",
            "options": [{"help": "Bypass the session when unable to retrieve server\u0027s certificate for inspection.", "label": "Allow", "name": "allow"}, {"help": "Block the session when unable to retrieve server\u0027s certificate for inspection.", "label": "Block", "name": "block"}],
        },
        "encrypted-client-hello": {
            "type": "option",
            "help": "Block/allow session based on existence of encrypted-client-hello.",
            "default": "block",
            "options": [{"help": "Pass the session when encrypted-client-hello exists.", "label": "Allow", "name": "allow"}, {"help": "Block the session when encrypted-client-hello exists.", "label": "Block", "name": "block"}],
        },
        "min-allowed-ssl-version": {
            "type": "option",
            "help": "Minimum SSL version to be allowed.",
            "default": "tls-1.1",
            "options": [{"help": "SSL 3.0.", "label": "Ssl 3.0", "name": "ssl-3.0"}, {"help": "TLS 1.0.", "label": "Tls 1.0", "name": "tls-1.0"}, {"help": "TLS 1.1.", "label": "Tls 1.1", "name": "tls-1.1"}, {"help": "TLS 1.2.", "label": "Tls 1.2", "name": "tls-1.2"}, {"help": "TLS 1.3.", "label": "Tls 1.3", "name": "tls-1.3"}],
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
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Inspect SSL handshake only.", "label": "Certificate Inspection", "name": "certificate-inspection"}, {"help": "Full SSL inspection.", "label": "Deep Inspection", "name": "deep-inspection"}],
        },
        "quic": {
            "type": "option",
            "help": "QUIC inspection status (default = inspect).",
            "default": "inspect",
            "options": [{"help": "Inspect QUIC traffic.", "label": "Inspect", "name": "inspect"}, {"help": "Bypass QUIC traffic.", "label": "Bypass", "name": "bypass"}, {"help": "Block QUIC traffic.", "label": "Block", "name": "block"}],
        },
        "udp-not-quic": {
            "type": "option",
            "help": "Action to be taken when matched UDP packet is not QUIC.",
            "default": "allow",
            "options": [{"help": "Bypass the session when UDP packet is not QUIC.", "label": "Allow", "name": "allow"}, {"help": "Block the session when UDP packet is not QUIC.", "label": "Block", "name": "block"}],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "bypass",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": [{"help": "Bypass the session when the version is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the version is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the cipher is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the cipher is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the negotiation is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the negotiation is not supported.", "label": "Block", "name": "block"}],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": [{"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, use the CN in the server certificate to do URL filtering.", "label": "Enable", "name": "enable"}, {"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, close the connection.", "label": "Strict", "name": "strict"}, {"help": "Do not check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.", "label": "Disable", "name": "disable"}],
        },
        "cert-probe-failure": {
            "type": "option",
            "help": "Action based on certificate probe failure.",
            "default": "allow",
            "options": [{"help": "Bypass the session when unable to retrieve server\u0027s certificate for inspection.", "label": "Allow", "name": "allow"}, {"help": "Block the session when unable to retrieve server\u0027s certificate for inspection.", "label": "Block", "name": "block"}],
        },
        "encrypted-client-hello": {
            "type": "option",
            "help": "Block/allow session based on existence of encrypted-client-hello.",
            "default": "block",
            "options": [{"help": "Pass the session when encrypted-client-hello exists.", "label": "Allow", "name": "allow"}, {"help": "Block the session when encrypted-client-hello exists.", "label": "Block", "name": "block"}],
        },
        "min-allowed-ssl-version": {
            "type": "option",
            "help": "Minimum SSL version to be allowed.",
            "default": "tls-1.1",
            "options": [{"help": "SSL 3.0.", "label": "Ssl 3.0", "name": "ssl-3.0"}, {"help": "TLS 1.0.", "label": "Tls 1.0", "name": "tls-1.0"}, {"help": "TLS 1.1.", "label": "Tls 1.1", "name": "tls-1.1"}, {"help": "TLS 1.2.", "label": "Tls 1.2", "name": "tls-1.2"}, {"help": "TLS 1.3.", "label": "Tls 1.3", "name": "tls-1.3"}],
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
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Full SSL inspection.", "label": "Deep Inspection", "name": "deep-inspection"}],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "bypass",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": [{"help": "Bypass the session when the version is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the version is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the cipher is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the cipher is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the negotiation is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the negotiation is not supported.", "label": "Block", "name": "block"}],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": [{"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, use the CN in the server certificate to do URL filtering.", "label": "Enable", "name": "enable"}, {"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, close the connection.", "label": "Strict", "name": "strict"}, {"help": "Do not check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.", "label": "Disable", "name": "disable"}],
        },
        "min-allowed-ssl-version": {
            "type": "option",
            "help": "Minimum SSL version to be allowed.",
            "default": "tls-1.1",
            "options": [{"help": "SSL 3.0.", "label": "Ssl 3.0", "name": "ssl-3.0"}, {"help": "TLS 1.0.", "label": "Tls 1.0", "name": "tls-1.0"}, {"help": "TLS 1.1.", "label": "Tls 1.1", "name": "tls-1.1"}, {"help": "TLS 1.2.", "label": "Tls 1.2", "name": "tls-1.2"}, {"help": "TLS 1.3.", "label": "Tls 1.3", "name": "tls-1.3"}],
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
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Full SSL inspection.", "label": "Deep Inspection", "name": "deep-inspection"}],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "inspect",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": [{"help": "Bypass the session when the version is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the version is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the cipher is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the cipher is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the negotiation is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the negotiation is not supported.", "label": "Block", "name": "block"}],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": [{"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, use the CN in the server certificate to do URL filtering.", "label": "Enable", "name": "enable"}, {"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, close the connection.", "label": "Strict", "name": "strict"}, {"help": "Do not check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Full SSL inspection.", "label": "Deep Inspection", "name": "deep-inspection"}],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "inspect",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": [{"help": "Bypass the session when the version is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the version is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the cipher is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the cipher is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the negotiation is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the negotiation is not supported.", "label": "Block", "name": "block"}],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": [{"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, use the CN in the server certificate to do URL filtering.", "label": "Enable", "name": "enable"}, {"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, close the connection.", "label": "Strict", "name": "strict"}, {"help": "Do not check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Full SSL inspection.", "label": "Deep Inspection", "name": "deep-inspection"}],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "inspect",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": [{"help": "Bypass the session when the version is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the version is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the cipher is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the cipher is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the negotiation is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the negotiation is not supported.", "label": "Block", "name": "block"}],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": [{"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, use the CN in the server certificate to do URL filtering.", "label": "Enable", "name": "enable"}, {"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, close the connection.", "label": "Strict", "name": "strict"}, {"help": "Do not check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Full SSL inspection.", "label": "Deep Inspection", "name": "deep-inspection"}],
        },
        "inspect-all": {
            "type": "option",
            "help": "Level of SSL inspection.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Full SSL inspection.", "label": "Deep Inspection", "name": "deep-inspection"}],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "unsupported-version": {
            "type": "option",
            "help": "Action based on SSH version being unsupported.",
            "default": "bypass",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "ssh-tun-policy-check": {
            "type": "option",
            "help": "Enable/disable SSH tunnel policy check.",
            "default": "disable",
            "options": [{"help": "Disable SSH tunnel policy check.", "label": "Disable", "name": "disable"}, {"help": "Enable SSH tunnel policy check.", "label": "Enable", "name": "enable"}],
        },
        "ssh-algorithm": {
            "type": "option",
            "help": "Relative strength of encryption algorithms accepted during negotiation.",
            "default": "compatible",
            "options": [{"help": "Allow a broader set of encryption algorithms for best compatibility.", "label": "Compatible", "name": "compatible"}, {"help": "Allow only AES-CTR, AES-GCM ciphers and high encryption algorithms.", "label": "High Encryption", "name": "high-encryption"}],
        },
    },
    "dot": {
        "status": {
            "type": "option",
            "help": "Configure protocol inspection status.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Full SSL inspection.", "label": "Deep Inspection", "name": "deep-inspection"}],
        },
        "quic": {
            "type": "option",
            "help": "QUIC inspection status (default = inspect).",
            "default": "inspect",
            "options": [{"help": "Inspect QUIC traffic.", "label": "Inspect", "name": "inspect"}, {"help": "Bypass QUIC traffic.", "label": "Bypass", "name": "bypass"}, {"help": "Block QUIC traffic.", "label": "Block", "name": "block"}],
        },
        "udp-not-quic": {
            "type": "option",
            "help": "Action to be taken when matched UDP packet is not QUIC.",
            "default": "allow",
            "options": [{"help": "Bypass the session when UDP packet is not QUIC.", "label": "Allow", "name": "allow"}, {"help": "Block the session when UDP packet is not QUIC.", "label": "Block", "name": "block"}],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate.",
            "default": "bypass",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-version": {
            "type": "option",
            "help": "Action based on the SSL version used being unsupported.",
            "default": "block",
            "options": [{"help": "Bypass the session when the version is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the version is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-cipher": {
            "type": "option",
            "help": "Action based on the SSL cipher used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the cipher is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the cipher is not supported.", "label": "Block", "name": "block"}],
        },
        "unsupported-ssl-negotiation": {
            "type": "option",
            "help": "Action based on the SSL negotiation used being unsupported.",
            "default": "allow",
            "options": [{"help": "Bypass the session when the negotiation is not supported.", "label": "Allow", "name": "allow"}, {"help": "Block the session when the negotiation is not supported.", "label": "Block", "name": "block"}],
        },
        "expired-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is expired.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "revoked-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is revoked.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "untrusted-server-cert": {
            "type": "option",
            "help": "Action based on server certificate is not issued by a trusted CA.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-timeout": {
            "type": "option",
            "help": "Action based on certificate validation timeout.",
            "default": "allow",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "cert-validation-failure": {
            "type": "option",
            "help": "Action based on certificate validation failure.",
            "default": "block",
            "options": [{"help": "Allow the server certificate.", "label": "Allow", "name": "allow"}, {"help": "Block the session.", "label": "Block", "name": "block"}, {"help": "Re-sign the server certificate as trusted.", "label": "Ignore", "name": "ignore"}],
        },
        "sni-server-cert-check": {
            "type": "option",
            "help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.",
            "default": "enable",
            "options": [{"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, use the CN in the server certificate to do URL filtering.", "label": "Enable", "name": "enable"}, {"help": "Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. If mismatched, close the connection.", "label": "Strict", "name": "strict"}, {"help": "Do not check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.", "label": "Disable", "name": "disable"}],
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
            "options": [{"help": "FortiGuard category.", "label": "Fortiguard Category", "name": "fortiguard-category"}, {"help": "Firewall IPv4 address.", "label": "Address", "name": "address"}, {"help": "Firewall IPv6 address.", "label": "Address6", "name": "address6"}, {"help": "Fully Qualified Domain Name with wildcard characters.", "label": "Wildcard Fqdn", "name": "wildcard-fqdn"}, {"help": "Regular expression FQDN.", "label": "Regex", "name": "regex"}],
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
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "smtps-client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate during the SMTPS handshake.",
            "default": "bypass",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "pop3s-client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate during the POP3S handshake.",
            "default": "bypass",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "imaps-client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate during the IMAPS handshake.",
            "default": "bypass",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "ftps-client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate during the FTPS handshake.",
            "default": "bypass",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
        "ssl-other-client-certificate": {
            "type": "option",
            "help": "Action based on received client certificate during an SSL protocol handshake.",
            "default": "bypass",
            "options": [{"help": "Bypass the session.", "label": "Bypass", "name": "bypass"}, {"help": "Inspect the session.", "label": "Inspect", "name": "inspect"}, {"help": "Block the session.", "label": "Block", "name": "block"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_ALLOWLIST = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_BLOCK_BLOCKLISTED_CERTIFICATES = [
    "disable",  # Disable FortiGuard certificate blocklist.
    "enable",  # Enable FortiGuard certificate blocklist.
]
VALID_BODY_SERVER_CERT_MODE = [
    "re-sign",  # Multiple clients connecting to multiple servers.
    "replace",  # Protect an SSL server.
]
VALID_BODY_USE_SSL_SERVER = [
    "disable",  # Don't use SSL server configuration.
    "enable",  # Use SSL server configuration.
]
VALID_BODY_SSL_EXEMPTION_IP_RATING = [
    "enable",  # Enable IP based URL rating.
    "disable",  # Disable IP based URL rating.
]
VALID_BODY_SSL_EXEMPTION_LOG = [
    "disable",  # Disable logging of SSL exemptions.
    "enable",  # Enable logging of SSL exemptions.
]
VALID_BODY_SSL_ANOMALY_LOG = [
    "disable",  # Disable logging of SSL anomalies.
    "enable",  # Enable logging of SSL anomalies.
]
VALID_BODY_SSL_NEGOTIATION_LOG = [
    "disable",  # Disable logging of SSL negotiation events.
    "enable",  # Enable logging of SSL negotiation events.
]
VALID_BODY_SSL_SERVER_CERT_LOG = [
    "disable",  # Disable logging of server certificate information.
    "enable",  # Enable logging of server certificate information.
]
VALID_BODY_SSL_HANDSHAKE_LOG = [
    "disable",  # Disable logging of TLS handshakes.
    "enable",  # Enable logging of TLS handshakes.
]
VALID_BODY_RPC_OVER_HTTPS = [
    "enable",  # Enable inspection of RPC over HTTPS.
    "disable",  # Disable inspection of RPC over HTTPS.
]
VALID_BODY_MAPI_OVER_HTTPS = [
    "enable",  # Enable inspection of MAPI over HTTPS.
    "disable",  # Disable inspection of MAPI over HTTPS.
]
VALID_BODY_SUPPORTED_ALPN = [
    "http1-1",  # Enable all ALPN including HTTP1.1 except HTTP2 and SPDY.
    "http2",  # Enable all ALPN including HTTP2 except HTTP1.1 and SPDY.
    "all",  # Allow all ALPN extensions except SPDY.
    "none",  # Do not use ALPN.
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
    """Validate GET request parameters for firewall/ssl_ssh_profile."""
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
    """Validate required fields for firewall/ssl_ssh_profile."""
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
    """Validate POST request to create new firewall/ssl_ssh_profile object."""
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
    """Validate PUT request to update firewall/ssl_ssh_profile."""
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
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
