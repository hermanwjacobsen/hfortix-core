"""
Validation helpers for firewall/vip endpoint.

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
    "server-type",  # Protocol to be load balanced by the virtual server (also called the server load balance virtual IP).
    "extip",  # IP address or address range on the external interface that you want to map to an address or address range on the destination network.
    "mappedip",  # IP address or address range on the destination network to which the external IP address is mapped.
    "extintf",  # Interface connected to the source network that receives the packets that will be forwarded to the destination network.
    "extport",  # Incoming port number range that you want to map to a port number range on the destination network.
    "ssl-certificate",  # Name of the certificate to use for SSL handshake.
    "ipv6-mappedip",  # Range of mapped IPv6 addresses. Specify the start IPv6 address followed by a space and the end IPv6 address.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "id": 0,
    "uuid": "00000000-0000-0000-0000-000000000000",
    "type": "static-nat",
    "server-type": "",
    "dns-mapping-ttl": 0,
    "ldb-method": "static",
    "src-vip-filter": "disable",
    "extip": "",
    "h2-support": "enable",
    "h3-support": "disable",
    "nat44": "enable",
    "nat46": "disable",
    "add-nat46-route": "enable",
    "mapped-addr": "",
    "extintf": "",
    "arp-reply": "enable",
    "http-redirect": "disable",
    "persistence": "none",
    "nat-source-vip": "disable",
    "portforward": "disable",
    "status": "enable",
    "protocol": "tcp",
    "extport": "",
    "mappedport": "",
    "gratuitous-arp-interval": 0,
    "portmapping-type": "1-to-1",
    "empty-cert-action": "block",
    "user-agent-detect": "enable",
    "client-cert": "enable",
    "http-cookie-domain-from-host": "disable",
    "http-cookie-domain": "",
    "http-cookie-path": "",
    "http-cookie-generation": 0,
    "http-cookie-age": 60,
    "http-cookie-share": "same-ip",
    "https-cookie-secure": "disable",
    "http-multiplex": "disable",
    "http-multiplex-ttl": 15,
    "http-multiplex-max-request": 0,
    "http-multiplex-max-concurrent-request": 0,
    "http-ip-header": "disable",
    "http-ip-header-name": "",
    "outlook-web-access": "disable",
    "weblogic-server": "disable",
    "websphere-server": "disable",
    "ssl-mode": "half",
    "ssl-dh-bits": "2048",
    "ssl-algorithm": "high",
    "ssl-server-algorithm": "client",
    "ssl-pfs": "require",
    "ssl-min-version": "tls-1.1",
    "ssl-max-version": "tls-1.3",
    "ssl-server-min-version": "client",
    "ssl-server-max-version": "client",
    "ssl-accept-ffdhe-groups": "enable",
    "ssl-send-empty-frags": "enable",
    "ssl-client-fallback": "enable",
    "ssl-client-renegotiation": "secure",
    "ssl-client-session-state-type": "both",
    "ssl-client-session-state-timeout": 30,
    "ssl-client-session-state-max": 1000,
    "ssl-client-rekey-count": 0,
    "ssl-server-renegotiation": "enable",
    "ssl-server-session-state-type": "both",
    "ssl-server-session-state-timeout": 60,
    "ssl-server-session-state-max": 100,
    "ssl-http-location-conversion": "disable",
    "ssl-http-match-host": "enable",
    "ssl-hpkp": "disable",
    "ssl-hpkp-primary": "",
    "ssl-hpkp-backup": "",
    "ssl-hpkp-age": 5184000,
    "ssl-hpkp-include-subdomains": "disable",
    "ssl-hsts": "disable",
    "ssl-hsts-age": 5184000,
    "ssl-hsts-include-subdomains": "disable",
    "max-embryonic-connections": 1000,
    "color": 0,
    "ipv6-mappedip": "",
    "ipv6-mappedport": "",
    "one-click-gslb-server": "disable",
    "gslb-hostname": "",
    "gslb-domain-name": "",
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
    "name": "string",  # Virtual IP name.
    "id": "integer",  # Custom defined ID.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "comment": "var-string",  # Comment.
    "type": "option",  # Configure a static NAT, load balance, server load balance, a
    "server-type": "option",  # Protocol to be load balanced by the virtual server (also cal
    "dns-mapping-ttl": "integer",  # DNS mapping TTL (Set to zero to use TTL in DNS response, def
    "ldb-method": "option",  # Method used to distribute sessions to real servers.
    "src-filter": "string",  # Source address filter. Each address must be either an IP/sub
    "src-vip-filter": "option",  # Enable/disable use of 'src-filter' to match destinations for
    "service": "string",  # Service name.
    "extip": "user",  # IP address or address range on the external interface that y
    "extaddr": "string",  # External FQDN address name.
    "h2-support": "option",  # Enable/disable HTTP2 support (default = enable).
    "h3-support": "option",  # Enable/disable HTTP3/QUIC support (default = disable).
    "quic": "string",  # QUIC setting.
    "nat44": "option",  # Enable/disable NAT44.
    "nat46": "option",  # Enable/disable NAT46.
    "add-nat46-route": "option",  # Enable/disable adding NAT46 route.
    "mappedip": "string",  # IP address or address range on the destination network to wh
    "mapped-addr": "string",  # Mapped FQDN address name.
    "extintf": "string",  # Interface connected to the source network that receives the 
    "arp-reply": "option",  # Enable to respond to ARP requests for this virtual IP addres
    "http-redirect": "option",  # Enable/disable redirection of HTTP to HTTPS.
    "persistence": "option",  # Configure how to make sure that clients connect to the same 
    "nat-source-vip": "option",  # Enable/disable forcing the source NAT mapped IP to the exter
    "portforward": "option",  # Enable/disable port forwarding.
    "status": "option",  # Enable/disable VIP.
    "protocol": "option",  # Protocol to use when forwarding packets.
    "extport": "user",  # Incoming port number range that you want to map to a port nu
    "mappedport": "user",  # Port number range on the destination network to which the ex
    "gratuitous-arp-interval": "integer",  # Enable to have the VIP send gratuitous ARPs. 0=disabled. Set
    "srcintf-filter": "string",  # Interfaces to which the VIP applies. Separate the names with
    "portmapping-type": "option",  # Port mapping type.
    "empty-cert-action": "option",  # Action for an empty client certificate.
    "user-agent-detect": "option",  # Enable/disable detecting device type by HTTP user-agent if n
    "client-cert": "option",  # Enable/disable requesting client certificate.
    "realservers": "string",  # Select the real servers that this server load balancing VIP 
    "http-cookie-domain-from-host": "option",  # Enable/disable use of HTTP cookie domain from host field in 
    "http-cookie-domain": "string",  # Domain that HTTP cookie persistence should apply to.
    "http-cookie-path": "string",  # Limit HTTP cookie persistence to the specified path.
    "http-cookie-generation": "integer",  # Generation of HTTP cookie to be accepted. Changing invalidat
    "http-cookie-age": "integer",  # Time in minutes that client web browsers should keep a cooki
    "http-cookie-share": "option",  # Control sharing of cookies across virtual servers. Use of sa
    "https-cookie-secure": "option",  # Enable/disable verification that inserted HTTPS cookies are 
    "http-multiplex": "option",  # Enable/disable HTTP multiplexing.
    "http-multiplex-ttl": "integer",  # Time-to-live for idle connections to servers.
    "http-multiplex-max-request": "integer",  # Maximum number of requests that a multiplex server can handl
    "http-multiplex-max-concurrent-request": "integer",  # Maximum number of concurrent requests that a multiplex serve
    "http-ip-header": "option",  # For HTTP multiplexing, enable to add the original client IP 
    "http-ip-header-name": "string",  # For HTTP multiplexing, enter a custom HTTPS header name. The
    "outlook-web-access": "option",  # Enable to add the Front-End-Https header for Microsoft Outlo
    "weblogic-server": "option",  # Enable to add an HTTP header to indicate SSL offloading for 
    "websphere-server": "option",  # Enable to add an HTTP header to indicate SSL offloading for 
    "ssl-mode": "option",  # Apply SSL offloading between the client and the FortiGate (h
    "ssl-certificate": "string",  # Name of the certificate to use for SSL handshake.
    "ssl-dh-bits": "option",  # Number of bits to use in the Diffie-Hellman exchange for RSA
    "ssl-algorithm": "option",  # Permitted encryption algorithms for SSL sessions according t
    "ssl-cipher-suites": "string",  # SSL/TLS cipher suites acceptable from a client, ordered by p
    "ssl-server-algorithm": "option",  # Permitted encryption algorithms for the server side of SSL f
    "ssl-server-cipher-suites": "string",  # SSL/TLS cipher suites to offer to a server, ordered by prior
    "ssl-pfs": "option",  # Select the cipher suites that can be used for SSL perfect fo
    "ssl-min-version": "option",  # Lowest SSL/TLS version acceptable from a client.
    "ssl-max-version": "option",  # Highest SSL/TLS version acceptable from a client.
    "ssl-server-min-version": "option",  # Lowest SSL/TLS version acceptable from a server. Use the cli
    "ssl-server-max-version": "option",  # Highest SSL/TLS version acceptable from a server. Use the cl
    "ssl-accept-ffdhe-groups": "option",  # Enable/disable FFDHE cipher suite for SSL key exchange.
    "ssl-send-empty-frags": "option",  # Enable/disable sending empty fragments to avoid CBC IV attac
    "ssl-client-fallback": "option",  # Enable/disable support for preventing Downgrade Attacks on c
    "ssl-client-renegotiation": "option",  # Allow, deny, or require secure renegotiation of client sessi
    "ssl-client-session-state-type": "option",  # How to expire SSL sessions for the segment of the SSL connec
    "ssl-client-session-state-timeout": "integer",  # Number of minutes to keep client to FortiGate SSL session st
    "ssl-client-session-state-max": "integer",  # Maximum number of client to FortiGate SSL session states to 
    "ssl-client-rekey-count": "integer",  # Maximum length of data in MB before triggering a client reke
    "ssl-server-renegotiation": "option",  # Enable/disable secure renegotiation to comply with RFC 5746.
    "ssl-server-session-state-type": "option",  # How to expire SSL sessions for the segment of the SSL connec
    "ssl-server-session-state-timeout": "integer",  # Number of minutes to keep FortiGate to Server SSL session st
    "ssl-server-session-state-max": "integer",  # Maximum number of FortiGate to Server SSL session states to 
    "ssl-http-location-conversion": "option",  # Enable to replace HTTP with HTTPS in the reply's Location HT
    "ssl-http-match-host": "option",  # Enable/disable HTTP host matching for location conversion.
    "ssl-hpkp": "option",  # Enable/disable including HPKP header in response.
    "ssl-hpkp-primary": "string",  # Certificate to generate primary HPKP pin from.
    "ssl-hpkp-backup": "string",  # Certificate to generate backup HPKP pin from.
    "ssl-hpkp-age": "integer",  # Number of seconds the client should honor the HPKP setting.
    "ssl-hpkp-report-uri": "var-string",  # URL to report HPKP violations to.
    "ssl-hpkp-include-subdomains": "option",  # Indicate that HPKP header applies to all subdomains.
    "ssl-hsts": "option",  # Enable/disable including HSTS header in response.
    "ssl-hsts-age": "integer",  # Number of seconds the client should honor the HSTS setting.
    "ssl-hsts-include-subdomains": "option",  # Indicate that HSTS header applies to all subdomains.
    "monitor": "string",  # Name of the health check monitor to use when polling to dete
    "max-embryonic-connections": "integer",  # Maximum number of incomplete connections.
    "color": "integer",  # Color of icon on the GUI.
    "ipv6-mappedip": "user",  # Range of mapped IPv6 addresses. Specify the start IPv6 addre
    "ipv6-mappedport": "user",  # IPv6 port number range on the destination network to which t
    "one-click-gslb-server": "option",  # Enable/disable one click GSLB server integration with FortiG
    "gslb-hostname": "string",  # Hostname to use within the configured FortiGSLB domain.
    "gslb-domain-name": "string",  # Domain to use when integrating with FortiGSLB.
    "gslb-public-ips": "string",  # Publicly accessible IP addresses for the FortiGSLB service.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Virtual IP name.",
    "id": "Custom defined ID.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "comment": "Comment.",
    "type": "Configure a static NAT, load balance, server load balance, access proxy, DNS translation, or FQDN VIP.",
    "server-type": "Protocol to be load balanced by the virtual server (also called the server load balance virtual IP).",
    "dns-mapping-ttl": "DNS mapping TTL (Set to zero to use TTL in DNS response, default = 0).",
    "ldb-method": "Method used to distribute sessions to real servers.",
    "src-filter": "Source address filter. Each address must be either an IP/subnet (x.x.x.x/n) or a range (x.x.x.x-y.y.y.y). Separate addresses with spaces.",
    "src-vip-filter": "Enable/disable use of 'src-filter' to match destinations for the reverse SNAT rule.",
    "service": "Service name.",
    "extip": "IP address or address range on the external interface that you want to map to an address or address range on the destination network.",
    "extaddr": "External FQDN address name.",
    "h2-support": "Enable/disable HTTP2 support (default = enable).",
    "h3-support": "Enable/disable HTTP3/QUIC support (default = disable).",
    "quic": "QUIC setting.",
    "nat44": "Enable/disable NAT44.",
    "nat46": "Enable/disable NAT46.",
    "add-nat46-route": "Enable/disable adding NAT46 route.",
    "mappedip": "IP address or address range on the destination network to which the external IP address is mapped.",
    "mapped-addr": "Mapped FQDN address name.",
    "extintf": "Interface connected to the source network that receives the packets that will be forwarded to the destination network.",
    "arp-reply": "Enable to respond to ARP requests for this virtual IP address. Enabled by default.",
    "http-redirect": "Enable/disable redirection of HTTP to HTTPS.",
    "persistence": "Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.",
    "nat-source-vip": "Enable/disable forcing the source NAT mapped IP to the external IP for all traffic.",
    "portforward": "Enable/disable port forwarding.",
    "status": "Enable/disable VIP.",
    "protocol": "Protocol to use when forwarding packets.",
    "extport": "Incoming port number range that you want to map to a port number range on the destination network.",
    "mappedport": "Port number range on the destination network to which the external port number range is mapped.",
    "gratuitous-arp-interval": "Enable to have the VIP send gratuitous ARPs. 0=disabled. Set from 5 up to 8640000 seconds to enable.",
    "srcintf-filter": "Interfaces to which the VIP applies. Separate the names with spaces.",
    "portmapping-type": "Port mapping type.",
    "empty-cert-action": "Action for an empty client certificate.",
    "user-agent-detect": "Enable/disable detecting device type by HTTP user-agent if no client certificate is provided.",
    "client-cert": "Enable/disable requesting client certificate.",
    "realservers": "Select the real servers that this server load balancing VIP will distribute traffic to.",
    "http-cookie-domain-from-host": "Enable/disable use of HTTP cookie domain from host field in HTTP.",
    "http-cookie-domain": "Domain that HTTP cookie persistence should apply to.",
    "http-cookie-path": "Limit HTTP cookie persistence to the specified path.",
    "http-cookie-generation": "Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies.",
    "http-cookie-age": "Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.",
    "http-cookie-share": "Control sharing of cookies across virtual servers. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.",
    "https-cookie-secure": "Enable/disable verification that inserted HTTPS cookies are secure.",
    "http-multiplex": "Enable/disable HTTP multiplexing.",
    "http-multiplex-ttl": "Time-to-live for idle connections to servers.",
    "http-multiplex-max-request": "Maximum number of requests that a multiplex server can handle before disconnecting sessions (default = unlimited).",
    "http-multiplex-max-concurrent-request": "Maximum number of concurrent requests that a multiplex server can handle (default = unlimited).",
    "http-ip-header": "For HTTP multiplexing, enable to add the original client IP address in the X-Forwarded-For HTTP header.",
    "http-ip-header-name": "For HTTP multiplexing, enter a custom HTTPS header name. The original client IP address is added to this header. If empty, X-Forwarded-For is used.",
    "outlook-web-access": "Enable to add the Front-End-Https header for Microsoft Outlook Web Access.",
    "weblogic-server": "Enable to add an HTTP header to indicate SSL offloading for a WebLogic server.",
    "websphere-server": "Enable to add an HTTP header to indicate SSL offloading for a WebSphere server.",
    "ssl-mode": "Apply SSL offloading between the client and the FortiGate (half) or from the client to the FortiGate and from the FortiGate to the server (full).",
    "ssl-certificate": "Name of the certificate to use for SSL handshake.",
    "ssl-dh-bits": "Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.",
    "ssl-algorithm": "Permitted encryption algorithms for SSL sessions according to encryption strength.",
    "ssl-cipher-suites": "SSL/TLS cipher suites acceptable from a client, ordered by priority.",
    "ssl-server-algorithm": "Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.",
    "ssl-server-cipher-suites": "SSL/TLS cipher suites to offer to a server, ordered by priority.",
    "ssl-pfs": "Select the cipher suites that can be used for SSL perfect forward secrecy (PFS). Applies to both client and server sessions.",
    "ssl-min-version": "Lowest SSL/TLS version acceptable from a client.",
    "ssl-max-version": "Highest SSL/TLS version acceptable from a client.",
    "ssl-server-min-version": "Lowest SSL/TLS version acceptable from a server. Use the client setting by default.",
    "ssl-server-max-version": "Highest SSL/TLS version acceptable from a server. Use the client setting by default.",
    "ssl-accept-ffdhe-groups": "Enable/disable FFDHE cipher suite for SSL key exchange.",
    "ssl-send-empty-frags": "Enable/disable sending empty fragments to avoid CBC IV attacks (SSL 3.0 & TLS 1.0 only). May need to be disabled for compatibility with older systems.",
    "ssl-client-fallback": "Enable/disable support for preventing Downgrade Attacks on client connections (RFC 7507).",
    "ssl-client-renegotiation": "Allow, deny, or require secure renegotiation of client sessions to comply with RFC 5746.",
    "ssl-client-session-state-type": "How to expire SSL sessions for the segment of the SSL connection between the client and the FortiGate.",
    "ssl-client-session-state-timeout": "Number of minutes to keep client to FortiGate SSL session state.",
    "ssl-client-session-state-max": "Maximum number of client to FortiGate SSL session states to keep.",
    "ssl-client-rekey-count": "Maximum length of data in MB before triggering a client rekey (0 = disable).",
    "ssl-server-renegotiation": "Enable/disable secure renegotiation to comply with RFC 5746.",
    "ssl-server-session-state-type": "How to expire SSL sessions for the segment of the SSL connection between the server and the FortiGate.",
    "ssl-server-session-state-timeout": "Number of minutes to keep FortiGate to Server SSL session state.",
    "ssl-server-session-state-max": "Maximum number of FortiGate to Server SSL session states to keep.",
    "ssl-http-location-conversion": "Enable to replace HTTP with HTTPS in the reply's Location HTTP header field.",
    "ssl-http-match-host": "Enable/disable HTTP host matching for location conversion.",
    "ssl-hpkp": "Enable/disable including HPKP header in response.",
    "ssl-hpkp-primary": "Certificate to generate primary HPKP pin from.",
    "ssl-hpkp-backup": "Certificate to generate backup HPKP pin from.",
    "ssl-hpkp-age": "Number of seconds the client should honor the HPKP setting.",
    "ssl-hpkp-report-uri": "URL to report HPKP violations to.",
    "ssl-hpkp-include-subdomains": "Indicate that HPKP header applies to all subdomains.",
    "ssl-hsts": "Enable/disable including HSTS header in response.",
    "ssl-hsts-age": "Number of seconds the client should honor the HSTS setting.",
    "ssl-hsts-include-subdomains": "Indicate that HSTS header applies to all subdomains.",
    "monitor": "Name of the health check monitor to use when polling to determine a virtual server's connectivity status.",
    "max-embryonic-connections": "Maximum number of incomplete connections.",
    "color": "Color of icon on the GUI.",
    "ipv6-mappedip": "Range of mapped IPv6 addresses. Specify the start IPv6 address followed by a space and the end IPv6 address.",
    "ipv6-mappedport": "IPv6 port number range on the destination network to which the external port number range is mapped.",
    "one-click-gslb-server": "Enable/disable one click GSLB server integration with FortiGSLB.",
    "gslb-hostname": "Hostname to use within the configured FortiGSLB domain.",
    "gslb-domain-name": "Domain to use when integrating with FortiGSLB.",
    "gslb-public-ips": "Publicly accessible IP addresses for the FortiGSLB service.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "id": {"type": "integer", "min": 0, "max": 65535},
    "dns-mapping-ttl": {"type": "integer", "min": 0, "max": 604800},
    "mapped-addr": {"type": "string", "max_length": 79},
    "extintf": {"type": "string", "max_length": 35},
    "gratuitous-arp-interval": {"type": "integer", "min": 5, "max": 8640000},
    "http-cookie-domain": {"type": "string", "max_length": 35},
    "http-cookie-path": {"type": "string", "max_length": 35},
    "http-cookie-generation": {"type": "integer", "min": 0, "max": 4294967295},
    "http-cookie-age": {"type": "integer", "min": 0, "max": 525600},
    "http-multiplex-ttl": {"type": "integer", "min": 0, "max": 2147483647},
    "http-multiplex-max-request": {"type": "integer", "min": 0, "max": 2147483647},
    "http-multiplex-max-concurrent-request": {"type": "integer", "min": 0, "max": 2147483647},
    "http-ip-header-name": {"type": "string", "max_length": 35},
    "ssl-client-session-state-timeout": {"type": "integer", "min": 1, "max": 14400},
    "ssl-client-session-state-max": {"type": "integer", "min": 1, "max": 10000},
    "ssl-client-rekey-count": {"type": "integer", "min": 200, "max": 1048576},
    "ssl-server-session-state-timeout": {"type": "integer", "min": 1, "max": 14400},
    "ssl-server-session-state-max": {"type": "integer", "min": 1, "max": 10000},
    "ssl-hpkp-primary": {"type": "string", "max_length": 79},
    "ssl-hpkp-backup": {"type": "string", "max_length": 79},
    "ssl-hpkp-age": {"type": "integer", "min": 60, "max": 157680000},
    "ssl-hsts-age": {"type": "integer", "min": 60, "max": 157680000},
    "max-embryonic-connections": {"type": "integer", "min": 0, "max": 100000},
    "color": {"type": "integer", "min": 0, "max": 32},
    "gslb-hostname": {"type": "string", "max_length": 35},
    "gslb-domain-name": {"type": "string", "max_length": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "src-filter": {
        "range": {
            "type": "string",
            "help": "Source-filter range.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "service": {
        "name": {
            "type": "string",
            "help": "Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "extaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "quic": {
        "max-idle-timeout": {
            "type": "integer",
            "help": "Maximum idle timeout milliseconds (1 - 60000, default = 30000).",
            "default": 30000,
            "min_value": 1,
            "max_value": 60000,
        },
        "max-udp-payload-size": {
            "type": "integer",
            "help": "Maximum UDP payload size in bytes (1200 - 1500, default = 1500).",
            "default": 1500,
            "min_value": 1200,
            "max_value": 1500,
        },
        "active-connection-id-limit": {
            "type": "integer",
            "help": "Active connection ID limit (1 - 8, default = 2).",
            "default": 2,
            "min_value": 1,
            "max_value": 8,
        },
        "ack-delay-exponent": {
            "type": "integer",
            "help": "ACK delay exponent (1 - 20, default = 3).",
            "default": 3,
            "min_value": 1,
            "max_value": 20,
        },
        "max-ack-delay": {
            "type": "integer",
            "help": "Maximum ACK delay in milliseconds (1 - 16383, default = 25).",
            "default": 25,
            "min_value": 1,
            "max_value": 16383,
        },
        "max-datagram-frame-size": {
            "type": "integer",
            "help": "Maximum datagram frame size in bytes (1 - 1500, default = 1500).",
            "default": 1500,
            "min_value": 1,
            "max_value": 1500,
        },
        "active-migration": {
            "type": "option",
            "help": "Enable/disable active migration (default = disable).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "grease-quic-bit": {
            "type": "option",
            "help": "Enable/disable grease QUIC bit (default = enable).",
            "default": "enable",
            "options": ["enable", "disable"],
        },
    },
    "mappedip": {
        "range": {
            "type": "string",
            "help": "Mapped IP range.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "srcintf-filter": {
        "interface-name": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 79,
        },
    },
    "realservers": {
        "id": {
            "type": "integer",
            "help": "Real server ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "type": {
            "type": "option",
            "help": "Type of address.",
            "required": True,
            "default": "ip",
            "options": ["ip", "address"],
        },
        "address": {
            "type": "string",
            "help": "Dynamic address of the real server.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
        "ip": {
            "type": "user",
            "help": "IP address of the real server.",
            "required": True,
            "default": "",
        },
        "port": {
            "type": "integer",
            "help": "Port for communicating with the real server. Required if port forwarding is enabled.",
            "default": 0,
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent.",
            "default": "active",
            "options": ["active", "standby", "disable"],
        },
        "weight": {
            "type": "integer",
            "help": "Weight of the real server. If weighted load balancing is enabled, the server with the highest weight gets more connections.",
            "default": 1,
            "min_value": 1,
            "max_value": 255,
        },
        "holddown-interval": {
            "type": "integer",
            "help": "Time in seconds that the system waits before re-activating a previously down active server in the active-standby mode. This is to prevent any flapping issues.",
            "default": 300,
            "min_value": 30,
            "max_value": 65535,
        },
        "healthcheck": {
            "type": "option",
            "help": "Enable to check the responsiveness of the real server before forwarding traffic.",
            "default": "vip",
            "options": ["disable", "enable", "vip"],
        },
        "http-host": {
            "type": "string",
            "help": "HTTP server domain name in HTTP header.",
            "default": "",
            "max_length": 63,
        },
        "translate-host": {
            "type": "option",
            "help": "Enable/disable translation of hostname/IP from virtual server to real server.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "max-connections": {
            "type": "integer",
            "help": "Max number of active connections that can be directed to the real server. When reached, sessions are sent to other real servers.",
            "default": 0,
            "min_value": 0,
            "max_value": 2147483647,
        },
        "monitor": {
            "type": "string",
            "help": "Name of the health check monitor to use when polling to determine a virtual server's connectivity status.",
        },
        "client-ip": {
            "type": "user",
            "help": "Only clients in this IP range can connect to this real server.",
            "default": "",
        },
        "verify-cert": {
            "type": "option",
            "help": "Enable/disable certificate verification of the real server.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
    },
    "ssl-certificate": {
        "name": {
            "type": "string",
            "help": "Certificate list.",
            "default": "",
            "max_length": 79,
        },
    },
    "ssl-cipher-suites": {
        "priority": {
            "type": "integer",
            "help": "SSL/TLS cipher suites priority.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "cipher": {
            "type": "option",
            "help": "Cipher suite name.",
            "required": True,
            "default": "",
            "options": ["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-128-GCM-SHA256", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-AES-128-CBC-SHA", "TLS-RSA-WITH-AES-256-CBC-SHA", "TLS-RSA-WITH-AES-128-CBC-SHA256", "TLS-RSA-WITH-AES-128-GCM-SHA256", "TLS-RSA-WITH-AES-256-CBC-SHA256", "TLS-RSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-SEED-CBC-SHA", "TLS-DHE-DSS-WITH-SEED-CBC-SHA", "TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384", "TLS-RSA-WITH-SEED-CBC-SHA", "TLS-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-RC4-128-SHA", "TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-RC4-128-MD5", "TLS-RSA-WITH-RC4-128-SHA", "TLS-DHE-RSA-WITH-DES-CBC-SHA", "TLS-DHE-DSS-WITH-DES-CBC-SHA", "TLS-RSA-WITH-DES-CBC-SHA"],
        },
        "versions": {
            "type": "option",
            "help": "SSL/TLS versions that the cipher suite can be used with.",
            "default": "ssl-3.0 tls-1.0 tls-1.1 tls-1.2 tls-1.3",
            "options": ["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"],
        },
    },
    "ssl-server-cipher-suites": {
        "priority": {
            "type": "integer",
            "help": "SSL/TLS cipher suites priority.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "cipher": {
            "type": "option",
            "help": "Cipher suite name.",
            "required": True,
            "default": "",
            "options": ["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-128-GCM-SHA256", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-AES-128-CBC-SHA", "TLS-RSA-WITH-AES-256-CBC-SHA", "TLS-RSA-WITH-AES-128-CBC-SHA256", "TLS-RSA-WITH-AES-128-GCM-SHA256", "TLS-RSA-WITH-AES-256-CBC-SHA256", "TLS-RSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-SEED-CBC-SHA", "TLS-DHE-DSS-WITH-SEED-CBC-SHA", "TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384", "TLS-RSA-WITH-SEED-CBC-SHA", "TLS-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-RC4-128-SHA", "TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-RC4-128-MD5", "TLS-RSA-WITH-RC4-128-SHA", "TLS-DHE-RSA-WITH-DES-CBC-SHA", "TLS-DHE-DSS-WITH-DES-CBC-SHA", "TLS-RSA-WITH-DES-CBC-SHA"],
        },
        "versions": {
            "type": "option",
            "help": "SSL/TLS versions that the cipher suite can be used with.",
            "default": "ssl-3.0 tls-1.0 tls-1.1 tls-1.2 tls-1.3",
            "options": ["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"],
        },
    },
    "monitor": {
        "name": {
            "type": "string",
            "help": "Health monitor name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "gslb-public-ips": {
        "index": {
            "type": "integer",
            "help": "Index of this public IP setting.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ip": {
            "type": "ipv4-address-any",
            "help": "The publicly accessible IP address.",
            "default": "0.0.0.0",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "static-nat",
    "load-balance",
    "server-load-balance",
    "dns-translation",
    "fqdn",
    "access-proxy",
]
VALID_BODY_SERVER_TYPE = [
    "http",
    "https",
    "imaps",
    "pop3s",
    "smtps",
    "ssl",
    "tcp",
    "udp",
    "ip",
]
VALID_BODY_LDB_METHOD = [
    "static",
    "round-robin",
    "weighted",
    "least-session",
    "least-rtt",
    "first-alive",
    "http-host",
]
VALID_BODY_SRC_VIP_FILTER = [
    "disable",
    "enable",
]
VALID_BODY_H2_SUPPORT = [
    "enable",
    "disable",
]
VALID_BODY_H3_SUPPORT = [
    "enable",
    "disable",
]
VALID_BODY_NAT44 = [
    "disable",
    "enable",
]
VALID_BODY_NAT46 = [
    "disable",
    "enable",
]
VALID_BODY_ADD_NAT46_ROUTE = [
    "disable",
    "enable",
]
VALID_BODY_ARP_REPLY = [
    "disable",
    "enable",
]
VALID_BODY_HTTP_REDIRECT = [
    "enable",
    "disable",
]
VALID_BODY_PERSISTENCE = [
    "none",
    "http-cookie",
    "ssl-session-id",
]
VALID_BODY_NAT_SOURCE_VIP = [
    "disable",
    "enable",
]
VALID_BODY_PORTFORWARD = [
    "disable",
    "enable",
]
VALID_BODY_STATUS = [
    "disable",
    "enable",
]
VALID_BODY_PROTOCOL = [
    "tcp",
    "udp",
    "sctp",
    "icmp",
]
VALID_BODY_PORTMAPPING_TYPE = [
    "1-to-1",
    "m-to-n",
]
VALID_BODY_EMPTY_CERT_ACTION = [
    "accept",
    "block",
    "accept-unmanageable",
]
VALID_BODY_USER_AGENT_DETECT = [
    "disable",
    "enable",
]
VALID_BODY_CLIENT_CERT = [
    "disable",
    "enable",
]
VALID_BODY_HTTP_COOKIE_DOMAIN_FROM_HOST = [
    "disable",
    "enable",
]
VALID_BODY_HTTP_COOKIE_SHARE = [
    "disable",
    "same-ip",
]
VALID_BODY_HTTPS_COOKIE_SECURE = [
    "disable",
    "enable",
]
VALID_BODY_HTTP_MULTIPLEX = [
    "enable",
    "disable",
]
VALID_BODY_HTTP_IP_HEADER = [
    "enable",
    "disable",
]
VALID_BODY_OUTLOOK_WEB_ACCESS = [
    "disable",
    "enable",
]
VALID_BODY_WEBLOGIC_SERVER = [
    "disable",
    "enable",
]
VALID_BODY_WEBSPHERE_SERVER = [
    "disable",
    "enable",
]
VALID_BODY_SSL_MODE = [
    "half",
    "full",
]
VALID_BODY_SSL_DH_BITS = [
    "768",
    "1024",
    "1536",
    "2048",
    "3072",
    "4096",
]
VALID_BODY_SSL_ALGORITHM = [
    "high",
    "medium",
    "low",
    "custom",
]
VALID_BODY_SSL_SERVER_ALGORITHM = [
    "high",
    "medium",
    "low",
    "custom",
    "client",
]
VALID_BODY_SSL_PFS = [
    "require",
    "deny",
    "allow",
]
VALID_BODY_SSL_MIN_VERSION = [
    "ssl-3.0",
    "tls-1.0",
    "tls-1.1",
    "tls-1.2",
    "tls-1.3",
]
VALID_BODY_SSL_MAX_VERSION = [
    "ssl-3.0",
    "tls-1.0",
    "tls-1.1",
    "tls-1.2",
    "tls-1.3",
]
VALID_BODY_SSL_SERVER_MIN_VERSION = [
    "ssl-3.0",
    "tls-1.0",
    "tls-1.1",
    "tls-1.2",
    "tls-1.3",
    "client",
]
VALID_BODY_SSL_SERVER_MAX_VERSION = [
    "ssl-3.0",
    "tls-1.0",
    "tls-1.1",
    "tls-1.2",
    "tls-1.3",
    "client",
]
VALID_BODY_SSL_ACCEPT_FFDHE_GROUPS = [
    "enable",
    "disable",
]
VALID_BODY_SSL_SEND_EMPTY_FRAGS = [
    "enable",
    "disable",
]
VALID_BODY_SSL_CLIENT_FALLBACK = [
    "disable",
    "enable",
]
VALID_BODY_SSL_CLIENT_RENEGOTIATION = [
    "allow",
    "deny",
    "secure",
]
VALID_BODY_SSL_CLIENT_SESSION_STATE_TYPE = [
    "disable",
    "time",
    "count",
    "both",
]
VALID_BODY_SSL_SERVER_RENEGOTIATION = [
    "enable",
    "disable",
]
VALID_BODY_SSL_SERVER_SESSION_STATE_TYPE = [
    "disable",
    "time",
    "count",
    "both",
]
VALID_BODY_SSL_HTTP_LOCATION_CONVERSION = [
    "enable",
    "disable",
]
VALID_BODY_SSL_HTTP_MATCH_HOST = [
    "enable",
    "disable",
]
VALID_BODY_SSL_HPKP = [
    "disable",
    "enable",
    "report-only",
]
VALID_BODY_SSL_HPKP_INCLUDE_SUBDOMAINS = [
    "disable",
    "enable",
]
VALID_BODY_SSL_HSTS = [
    "disable",
    "enable",
]
VALID_BODY_SSL_HSTS_INCLUDE_SUBDOMAINS = [
    "disable",
    "enable",
]
VALID_BODY_ONE_CLICK_GSLB_SERVER = [
    "disable",
    "enable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_vip_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for firewall/vip.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_firewall_vip_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_firewall_vip_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_firewall_vip_get(
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
    Validate required fields for firewall/vip.

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


def validate_firewall_vip_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new firewall/vip object.

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
        ...     "server-type": True,  # Protocol to be load balanced by the virtual server
        ...     "extip": True,  # IP address or address range on the external interf
        ... }
        >>> is_valid, error = validate_firewall_vip_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "server-type": True,
        ...     "type": "static-nat",  # Valid enum value
        ... }
        >>> is_valid, error = validate_firewall_vip_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["type"] = "invalid-value"
        >>> is_valid, error = validate_firewall_vip_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_firewall_vip_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            desc = FIELD_DESCRIPTIONS.get("server-type", "")
            error_msg = f"Invalid value for 'server-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_TYPE)}"
            error_msg += f"\n  → Example: server-type='{{ VALID_BODY_SERVER_TYPE[0] }}'"
            return (False, error_msg)
    if "ldb-method" in payload:
        value = payload["ldb-method"]
        if value not in VALID_BODY_LDB_METHOD:
            desc = FIELD_DESCRIPTIONS.get("ldb-method", "")
            error_msg = f"Invalid value for 'ldb-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LDB_METHOD)}"
            error_msg += f"\n  → Example: ldb-method='{{ VALID_BODY_LDB_METHOD[0] }}'"
            return (False, error_msg)
    if "src-vip-filter" in payload:
        value = payload["src-vip-filter"]
        if value not in VALID_BODY_SRC_VIP_FILTER:
            desc = FIELD_DESCRIPTIONS.get("src-vip-filter", "")
            error_msg = f"Invalid value for 'src-vip-filter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SRC_VIP_FILTER)}"
            error_msg += f"\n  → Example: src-vip-filter='{{ VALID_BODY_SRC_VIP_FILTER[0] }}'"
            return (False, error_msg)
    if "h2-support" in payload:
        value = payload["h2-support"]
        if value not in VALID_BODY_H2_SUPPORT:
            desc = FIELD_DESCRIPTIONS.get("h2-support", "")
            error_msg = f"Invalid value for 'h2-support': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_H2_SUPPORT)}"
            error_msg += f"\n  → Example: h2-support='{{ VALID_BODY_H2_SUPPORT[0] }}'"
            return (False, error_msg)
    if "h3-support" in payload:
        value = payload["h3-support"]
        if value not in VALID_BODY_H3_SUPPORT:
            desc = FIELD_DESCRIPTIONS.get("h3-support", "")
            error_msg = f"Invalid value for 'h3-support': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_H3_SUPPORT)}"
            error_msg += f"\n  → Example: h3-support='{{ VALID_BODY_H3_SUPPORT[0] }}'"
            return (False, error_msg)
    if "nat44" in payload:
        value = payload["nat44"]
        if value not in VALID_BODY_NAT44:
            desc = FIELD_DESCRIPTIONS.get("nat44", "")
            error_msg = f"Invalid value for 'nat44': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT44)}"
            error_msg += f"\n  → Example: nat44='{{ VALID_BODY_NAT44[0] }}'"
            return (False, error_msg)
    if "nat46" in payload:
        value = payload["nat46"]
        if value not in VALID_BODY_NAT46:
            desc = FIELD_DESCRIPTIONS.get("nat46", "")
            error_msg = f"Invalid value for 'nat46': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT46)}"
            error_msg += f"\n  → Example: nat46='{{ VALID_BODY_NAT46[0] }}'"
            return (False, error_msg)
    if "add-nat46-route" in payload:
        value = payload["add-nat46-route"]
        if value not in VALID_BODY_ADD_NAT46_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("add-nat46-route", "")
            error_msg = f"Invalid value for 'add-nat46-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADD_NAT46_ROUTE)}"
            error_msg += f"\n  → Example: add-nat46-route='{{ VALID_BODY_ADD_NAT46_ROUTE[0] }}'"
            return (False, error_msg)
    if "arp-reply" in payload:
        value = payload["arp-reply"]
        if value not in VALID_BODY_ARP_REPLY:
            desc = FIELD_DESCRIPTIONS.get("arp-reply", "")
            error_msg = f"Invalid value for 'arp-reply': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ARP_REPLY)}"
            error_msg += f"\n  → Example: arp-reply='{{ VALID_BODY_ARP_REPLY[0] }}'"
            return (False, error_msg)
    if "http-redirect" in payload:
        value = payload["http-redirect"]
        if value not in VALID_BODY_HTTP_REDIRECT:
            desc = FIELD_DESCRIPTIONS.get("http-redirect", "")
            error_msg = f"Invalid value for 'http-redirect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_REDIRECT)}"
            error_msg += f"\n  → Example: http-redirect='{{ VALID_BODY_HTTP_REDIRECT[0] }}'"
            return (False, error_msg)
    if "persistence" in payload:
        value = payload["persistence"]
        if value not in VALID_BODY_PERSISTENCE:
            desc = FIELD_DESCRIPTIONS.get("persistence", "")
            error_msg = f"Invalid value for 'persistence': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERSISTENCE)}"
            error_msg += f"\n  → Example: persistence='{{ VALID_BODY_PERSISTENCE[0] }}'"
            return (False, error_msg)
    if "nat-source-vip" in payload:
        value = payload["nat-source-vip"]
        if value not in VALID_BODY_NAT_SOURCE_VIP:
            desc = FIELD_DESCRIPTIONS.get("nat-source-vip", "")
            error_msg = f"Invalid value for 'nat-source-vip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT_SOURCE_VIP)}"
            error_msg += f"\n  → Example: nat-source-vip='{{ VALID_BODY_NAT_SOURCE_VIP[0] }}'"
            return (False, error_msg)
    if "portforward" in payload:
        value = payload["portforward"]
        if value not in VALID_BODY_PORTFORWARD:
            desc = FIELD_DESCRIPTIONS.get("portforward", "")
            error_msg = f"Invalid value for 'portforward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORTFORWARD)}"
            error_msg += f"\n  → Example: portforward='{{ VALID_BODY_PORTFORWARD[0] }}'"
            return (False, error_msg)
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
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("protocol", "")
            error_msg = f"Invalid value for 'protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROTOCOL)}"
            error_msg += f"\n  → Example: protocol='{{ VALID_BODY_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "portmapping-type" in payload:
        value = payload["portmapping-type"]
        if value not in VALID_BODY_PORTMAPPING_TYPE:
            desc = FIELD_DESCRIPTIONS.get("portmapping-type", "")
            error_msg = f"Invalid value for 'portmapping-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORTMAPPING_TYPE)}"
            error_msg += f"\n  → Example: portmapping-type='{{ VALID_BODY_PORTMAPPING_TYPE[0] }}'"
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
    if "http-cookie-domain-from-host" in payload:
        value = payload["http-cookie-domain-from-host"]
        if value not in VALID_BODY_HTTP_COOKIE_DOMAIN_FROM_HOST:
            desc = FIELD_DESCRIPTIONS.get("http-cookie-domain-from-host", "")
            error_msg = f"Invalid value for 'http-cookie-domain-from-host': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_COOKIE_DOMAIN_FROM_HOST)}"
            error_msg += f"\n  → Example: http-cookie-domain-from-host='{{ VALID_BODY_HTTP_COOKIE_DOMAIN_FROM_HOST[0] }}'"
            return (False, error_msg)
    if "http-cookie-share" in payload:
        value = payload["http-cookie-share"]
        if value not in VALID_BODY_HTTP_COOKIE_SHARE:
            desc = FIELD_DESCRIPTIONS.get("http-cookie-share", "")
            error_msg = f"Invalid value for 'http-cookie-share': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_COOKIE_SHARE)}"
            error_msg += f"\n  → Example: http-cookie-share='{{ VALID_BODY_HTTP_COOKIE_SHARE[0] }}'"
            return (False, error_msg)
    if "https-cookie-secure" in payload:
        value = payload["https-cookie-secure"]
        if value not in VALID_BODY_HTTPS_COOKIE_SECURE:
            desc = FIELD_DESCRIPTIONS.get("https-cookie-secure", "")
            error_msg = f"Invalid value for 'https-cookie-secure': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTPS_COOKIE_SECURE)}"
            error_msg += f"\n  → Example: https-cookie-secure='{{ VALID_BODY_HTTPS_COOKIE_SECURE[0] }}'"
            return (False, error_msg)
    if "http-multiplex" in payload:
        value = payload["http-multiplex"]
        if value not in VALID_BODY_HTTP_MULTIPLEX:
            desc = FIELD_DESCRIPTIONS.get("http-multiplex", "")
            error_msg = f"Invalid value for 'http-multiplex': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_MULTIPLEX)}"
            error_msg += f"\n  → Example: http-multiplex='{{ VALID_BODY_HTTP_MULTIPLEX[0] }}'"
            return (False, error_msg)
    if "http-ip-header" in payload:
        value = payload["http-ip-header"]
        if value not in VALID_BODY_HTTP_IP_HEADER:
            desc = FIELD_DESCRIPTIONS.get("http-ip-header", "")
            error_msg = f"Invalid value for 'http-ip-header': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_IP_HEADER)}"
            error_msg += f"\n  → Example: http-ip-header='{{ VALID_BODY_HTTP_IP_HEADER[0] }}'"
            return (False, error_msg)
    if "outlook-web-access" in payload:
        value = payload["outlook-web-access"]
        if value not in VALID_BODY_OUTLOOK_WEB_ACCESS:
            desc = FIELD_DESCRIPTIONS.get("outlook-web-access", "")
            error_msg = f"Invalid value for 'outlook-web-access': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OUTLOOK_WEB_ACCESS)}"
            error_msg += f"\n  → Example: outlook-web-access='{{ VALID_BODY_OUTLOOK_WEB_ACCESS[0] }}'"
            return (False, error_msg)
    if "weblogic-server" in payload:
        value = payload["weblogic-server"]
        if value not in VALID_BODY_WEBLOGIC_SERVER:
            desc = FIELD_DESCRIPTIONS.get("weblogic-server", "")
            error_msg = f"Invalid value for 'weblogic-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEBLOGIC_SERVER)}"
            error_msg += f"\n  → Example: weblogic-server='{{ VALID_BODY_WEBLOGIC_SERVER[0] }}'"
            return (False, error_msg)
    if "websphere-server" in payload:
        value = payload["websphere-server"]
        if value not in VALID_BODY_WEBSPHERE_SERVER:
            desc = FIELD_DESCRIPTIONS.get("websphere-server", "")
            error_msg = f"Invalid value for 'websphere-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEBSPHERE_SERVER)}"
            error_msg += f"\n  → Example: websphere-server='{{ VALID_BODY_WEBSPHERE_SERVER[0] }}'"
            return (False, error_msg)
    if "ssl-mode" in payload:
        value = payload["ssl-mode"]
        if value not in VALID_BODY_SSL_MODE:
            desc = FIELD_DESCRIPTIONS.get("ssl-mode", "")
            error_msg = f"Invalid value for 'ssl-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MODE)}"
            error_msg += f"\n  → Example: ssl-mode='{{ VALID_BODY_SSL_MODE[0] }}'"
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
    if "ssl-server-algorithm" in payload:
        value = payload["ssl-server-algorithm"]
        if value not in VALID_BODY_SSL_SERVER_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("ssl-server-algorithm", "")
            error_msg = f"Invalid value for 'ssl-server-algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_SERVER_ALGORITHM)}"
            error_msg += f"\n  → Example: ssl-server-algorithm='{{ VALID_BODY_SSL_SERVER_ALGORITHM[0] }}'"
            return (False, error_msg)
    if "ssl-pfs" in payload:
        value = payload["ssl-pfs"]
        if value not in VALID_BODY_SSL_PFS:
            desc = FIELD_DESCRIPTIONS.get("ssl-pfs", "")
            error_msg = f"Invalid value for 'ssl-pfs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_PFS)}"
            error_msg += f"\n  → Example: ssl-pfs='{{ VALID_BODY_SSL_PFS[0] }}'"
            return (False, error_msg)
    if "ssl-min-version" in payload:
        value = payload["ssl-min-version"]
        if value not in VALID_BODY_SSL_MIN_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-min-version", "")
            error_msg = f"Invalid value for 'ssl-min-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MIN_VERSION)}"
            error_msg += f"\n  → Example: ssl-min-version='{{ VALID_BODY_SSL_MIN_VERSION[0] }}'"
            return (False, error_msg)
    if "ssl-max-version" in payload:
        value = payload["ssl-max-version"]
        if value not in VALID_BODY_SSL_MAX_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-max-version", "")
            error_msg = f"Invalid value for 'ssl-max-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MAX_VERSION)}"
            error_msg += f"\n  → Example: ssl-max-version='{{ VALID_BODY_SSL_MAX_VERSION[0] }}'"
            return (False, error_msg)
    if "ssl-server-min-version" in payload:
        value = payload["ssl-server-min-version"]
        if value not in VALID_BODY_SSL_SERVER_MIN_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-server-min-version", "")
            error_msg = f"Invalid value for 'ssl-server-min-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_SERVER_MIN_VERSION)}"
            error_msg += f"\n  → Example: ssl-server-min-version='{{ VALID_BODY_SSL_SERVER_MIN_VERSION[0] }}'"
            return (False, error_msg)
    if "ssl-server-max-version" in payload:
        value = payload["ssl-server-max-version"]
        if value not in VALID_BODY_SSL_SERVER_MAX_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-server-max-version", "")
            error_msg = f"Invalid value for 'ssl-server-max-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_SERVER_MAX_VERSION)}"
            error_msg += f"\n  → Example: ssl-server-max-version='{{ VALID_BODY_SSL_SERVER_MAX_VERSION[0] }}'"
            return (False, error_msg)
    if "ssl-accept-ffdhe-groups" in payload:
        value = payload["ssl-accept-ffdhe-groups"]
        if value not in VALID_BODY_SSL_ACCEPT_FFDHE_GROUPS:
            desc = FIELD_DESCRIPTIONS.get("ssl-accept-ffdhe-groups", "")
            error_msg = f"Invalid value for 'ssl-accept-ffdhe-groups': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_ACCEPT_FFDHE_GROUPS)}"
            error_msg += f"\n  → Example: ssl-accept-ffdhe-groups='{{ VALID_BODY_SSL_ACCEPT_FFDHE_GROUPS[0] }}'"
            return (False, error_msg)
    if "ssl-send-empty-frags" in payload:
        value = payload["ssl-send-empty-frags"]
        if value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            desc = FIELD_DESCRIPTIONS.get("ssl-send-empty-frags", "")
            error_msg = f"Invalid value for 'ssl-send-empty-frags': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_SEND_EMPTY_FRAGS)}"
            error_msg += f"\n  → Example: ssl-send-empty-frags='{{ VALID_BODY_SSL_SEND_EMPTY_FRAGS[0] }}'"
            return (False, error_msg)
    if "ssl-client-fallback" in payload:
        value = payload["ssl-client-fallback"]
        if value not in VALID_BODY_SSL_CLIENT_FALLBACK:
            desc = FIELD_DESCRIPTIONS.get("ssl-client-fallback", "")
            error_msg = f"Invalid value for 'ssl-client-fallback': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_CLIENT_FALLBACK)}"
            error_msg += f"\n  → Example: ssl-client-fallback='{{ VALID_BODY_SSL_CLIENT_FALLBACK[0] }}'"
            return (False, error_msg)
    if "ssl-client-renegotiation" in payload:
        value = payload["ssl-client-renegotiation"]
        if value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            desc = FIELD_DESCRIPTIONS.get("ssl-client-renegotiation", "")
            error_msg = f"Invalid value for 'ssl-client-renegotiation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_CLIENT_RENEGOTIATION)}"
            error_msg += f"\n  → Example: ssl-client-renegotiation='{{ VALID_BODY_SSL_CLIENT_RENEGOTIATION[0] }}'"
            return (False, error_msg)
    if "ssl-client-session-state-type" in payload:
        value = payload["ssl-client-session-state-type"]
        if value not in VALID_BODY_SSL_CLIENT_SESSION_STATE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("ssl-client-session-state-type", "")
            error_msg = f"Invalid value for 'ssl-client-session-state-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_CLIENT_SESSION_STATE_TYPE)}"
            error_msg += f"\n  → Example: ssl-client-session-state-type='{{ VALID_BODY_SSL_CLIENT_SESSION_STATE_TYPE[0] }}'"
            return (False, error_msg)
    if "ssl-server-renegotiation" in payload:
        value = payload["ssl-server-renegotiation"]
        if value not in VALID_BODY_SSL_SERVER_RENEGOTIATION:
            desc = FIELD_DESCRIPTIONS.get("ssl-server-renegotiation", "")
            error_msg = f"Invalid value for 'ssl-server-renegotiation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_SERVER_RENEGOTIATION)}"
            error_msg += f"\n  → Example: ssl-server-renegotiation='{{ VALID_BODY_SSL_SERVER_RENEGOTIATION[0] }}'"
            return (False, error_msg)
    if "ssl-server-session-state-type" in payload:
        value = payload["ssl-server-session-state-type"]
        if value not in VALID_BODY_SSL_SERVER_SESSION_STATE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("ssl-server-session-state-type", "")
            error_msg = f"Invalid value for 'ssl-server-session-state-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_SERVER_SESSION_STATE_TYPE)}"
            error_msg += f"\n  → Example: ssl-server-session-state-type='{{ VALID_BODY_SSL_SERVER_SESSION_STATE_TYPE[0] }}'"
            return (False, error_msg)
    if "ssl-http-location-conversion" in payload:
        value = payload["ssl-http-location-conversion"]
        if value not in VALID_BODY_SSL_HTTP_LOCATION_CONVERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-http-location-conversion", "")
            error_msg = f"Invalid value for 'ssl-http-location-conversion': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_HTTP_LOCATION_CONVERSION)}"
            error_msg += f"\n  → Example: ssl-http-location-conversion='{{ VALID_BODY_SSL_HTTP_LOCATION_CONVERSION[0] }}'"
            return (False, error_msg)
    if "ssl-http-match-host" in payload:
        value = payload["ssl-http-match-host"]
        if value not in VALID_BODY_SSL_HTTP_MATCH_HOST:
            desc = FIELD_DESCRIPTIONS.get("ssl-http-match-host", "")
            error_msg = f"Invalid value for 'ssl-http-match-host': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_HTTP_MATCH_HOST)}"
            error_msg += f"\n  → Example: ssl-http-match-host='{{ VALID_BODY_SSL_HTTP_MATCH_HOST[0] }}'"
            return (False, error_msg)
    if "ssl-hpkp" in payload:
        value = payload["ssl-hpkp"]
        if value not in VALID_BODY_SSL_HPKP:
            desc = FIELD_DESCRIPTIONS.get("ssl-hpkp", "")
            error_msg = f"Invalid value for 'ssl-hpkp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_HPKP)}"
            error_msg += f"\n  → Example: ssl-hpkp='{{ VALID_BODY_SSL_HPKP[0] }}'"
            return (False, error_msg)
    if "ssl-hpkp-include-subdomains" in payload:
        value = payload["ssl-hpkp-include-subdomains"]
        if value not in VALID_BODY_SSL_HPKP_INCLUDE_SUBDOMAINS:
            desc = FIELD_DESCRIPTIONS.get("ssl-hpkp-include-subdomains", "")
            error_msg = f"Invalid value for 'ssl-hpkp-include-subdomains': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_HPKP_INCLUDE_SUBDOMAINS)}"
            error_msg += f"\n  → Example: ssl-hpkp-include-subdomains='{{ VALID_BODY_SSL_HPKP_INCLUDE_SUBDOMAINS[0] }}'"
            return (False, error_msg)
    if "ssl-hsts" in payload:
        value = payload["ssl-hsts"]
        if value not in VALID_BODY_SSL_HSTS:
            desc = FIELD_DESCRIPTIONS.get("ssl-hsts", "")
            error_msg = f"Invalid value for 'ssl-hsts': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_HSTS)}"
            error_msg += f"\n  → Example: ssl-hsts='{{ VALID_BODY_SSL_HSTS[0] }}'"
            return (False, error_msg)
    if "ssl-hsts-include-subdomains" in payload:
        value = payload["ssl-hsts-include-subdomains"]
        if value not in VALID_BODY_SSL_HSTS_INCLUDE_SUBDOMAINS:
            desc = FIELD_DESCRIPTIONS.get("ssl-hsts-include-subdomains", "")
            error_msg = f"Invalid value for 'ssl-hsts-include-subdomains': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_HSTS_INCLUDE_SUBDOMAINS)}"
            error_msg += f"\n  → Example: ssl-hsts-include-subdomains='{{ VALID_BODY_SSL_HSTS_INCLUDE_SUBDOMAINS[0] }}'"
            return (False, error_msg)
    if "one-click-gslb-server" in payload:
        value = payload["one-click-gslb-server"]
        if value not in VALID_BODY_ONE_CLICK_GSLB_SERVER:
            desc = FIELD_DESCRIPTIONS.get("one-click-gslb-server", "")
            error_msg = f"Invalid value for 'one-click-gslb-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ONE_CLICK_GSLB_SERVER)}"
            error_msg += f"\n  → Example: one-click-gslb-server='{{ VALID_BODY_ONE_CLICK_GSLB_SERVER[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_vip_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update firewall/vip.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_firewall_vip_put(payload)
    """
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid value for 'server-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )
    if "ldb-method" in payload:
        value = payload["ldb-method"]
        if value not in VALID_BODY_LDB_METHOD:
            return (
                False,
                f"Invalid value for 'ldb-method'='{value}'. Must be one of: {', '.join(VALID_BODY_LDB_METHOD)}",
            )
    if "src-vip-filter" in payload:
        value = payload["src-vip-filter"]
        if value not in VALID_BODY_SRC_VIP_FILTER:
            return (
                False,
                f"Invalid value for 'src-vip-filter'='{value}'. Must be one of: {', '.join(VALID_BODY_SRC_VIP_FILTER)}",
            )
    if "h2-support" in payload:
        value = payload["h2-support"]
        if value not in VALID_BODY_H2_SUPPORT:
            return (
                False,
                f"Invalid value for 'h2-support'='{value}'. Must be one of: {', '.join(VALID_BODY_H2_SUPPORT)}",
            )
    if "h3-support" in payload:
        value = payload["h3-support"]
        if value not in VALID_BODY_H3_SUPPORT:
            return (
                False,
                f"Invalid value for 'h3-support'='{value}'. Must be one of: {', '.join(VALID_BODY_H3_SUPPORT)}",
            )
    if "nat44" in payload:
        value = payload["nat44"]
        if value not in VALID_BODY_NAT44:
            return (
                False,
                f"Invalid value for 'nat44'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT44)}",
            )
    if "nat46" in payload:
        value = payload["nat46"]
        if value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid value for 'nat46'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )
    if "add-nat46-route" in payload:
        value = payload["add-nat46-route"]
        if value not in VALID_BODY_ADD_NAT46_ROUTE:
            return (
                False,
                f"Invalid value for 'add-nat46-route'='{value}'. Must be one of: {', '.join(VALID_BODY_ADD_NAT46_ROUTE)}",
            )
    if "arp-reply" in payload:
        value = payload["arp-reply"]
        if value not in VALID_BODY_ARP_REPLY:
            return (
                False,
                f"Invalid value for 'arp-reply'='{value}'. Must be one of: {', '.join(VALID_BODY_ARP_REPLY)}",
            )
    if "http-redirect" in payload:
        value = payload["http-redirect"]
        if value not in VALID_BODY_HTTP_REDIRECT:
            return (
                False,
                f"Invalid value for 'http-redirect'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_REDIRECT)}",
            )
    if "persistence" in payload:
        value = payload["persistence"]
        if value not in VALID_BODY_PERSISTENCE:
            return (
                False,
                f"Invalid value for 'persistence'='{value}'. Must be one of: {', '.join(VALID_BODY_PERSISTENCE)}",
            )
    if "nat-source-vip" in payload:
        value = payload["nat-source-vip"]
        if value not in VALID_BODY_NAT_SOURCE_VIP:
            return (
                False,
                f"Invalid value for 'nat-source-vip'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT_SOURCE_VIP)}",
            )
    if "portforward" in payload:
        value = payload["portforward"]
        if value not in VALID_BODY_PORTFORWARD:
            return (
                False,
                f"Invalid value for 'portforward'='{value}'. Must be one of: {', '.join(VALID_BODY_PORTFORWARD)}",
            )
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid value for 'protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )
    if "portmapping-type" in payload:
        value = payload["portmapping-type"]
        if value not in VALID_BODY_PORTMAPPING_TYPE:
            return (
                False,
                f"Invalid value for 'portmapping-type'='{value}'. Must be one of: {', '.join(VALID_BODY_PORTMAPPING_TYPE)}",
            )
    if "empty-cert-action" in payload:
        value = payload["empty-cert-action"]
        if value not in VALID_BODY_EMPTY_CERT_ACTION:
            return (
                False,
                f"Invalid value for 'empty-cert-action'='{value}'. Must be one of: {', '.join(VALID_BODY_EMPTY_CERT_ACTION)}",
            )
    if "user-agent-detect" in payload:
        value = payload["user-agent-detect"]
        if value not in VALID_BODY_USER_AGENT_DETECT:
            return (
                False,
                f"Invalid value for 'user-agent-detect'='{value}'. Must be one of: {', '.join(VALID_BODY_USER_AGENT_DETECT)}",
            )
    if "client-cert" in payload:
        value = payload["client-cert"]
        if value not in VALID_BODY_CLIENT_CERT:
            return (
                False,
                f"Invalid value for 'client-cert'='{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_CERT)}",
            )
    if "http-cookie-domain-from-host" in payload:
        value = payload["http-cookie-domain-from-host"]
        if value not in VALID_BODY_HTTP_COOKIE_DOMAIN_FROM_HOST:
            return (
                False,
                f"Invalid value for 'http-cookie-domain-from-host'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_COOKIE_DOMAIN_FROM_HOST)}",
            )
    if "http-cookie-share" in payload:
        value = payload["http-cookie-share"]
        if value not in VALID_BODY_HTTP_COOKIE_SHARE:
            return (
                False,
                f"Invalid value for 'http-cookie-share'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_COOKIE_SHARE)}",
            )
    if "https-cookie-secure" in payload:
        value = payload["https-cookie-secure"]
        if value not in VALID_BODY_HTTPS_COOKIE_SECURE:
            return (
                False,
                f"Invalid value for 'https-cookie-secure'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_COOKIE_SECURE)}",
            )
    if "http-multiplex" in payload:
        value = payload["http-multiplex"]
        if value not in VALID_BODY_HTTP_MULTIPLEX:
            return (
                False,
                f"Invalid value for 'http-multiplex'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_MULTIPLEX)}",
            )
    if "http-ip-header" in payload:
        value = payload["http-ip-header"]
        if value not in VALID_BODY_HTTP_IP_HEADER:
            return (
                False,
                f"Invalid value for 'http-ip-header'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_IP_HEADER)}",
            )
    if "outlook-web-access" in payload:
        value = payload["outlook-web-access"]
        if value not in VALID_BODY_OUTLOOK_WEB_ACCESS:
            return (
                False,
                f"Invalid value for 'outlook-web-access'='{value}'. Must be one of: {', '.join(VALID_BODY_OUTLOOK_WEB_ACCESS)}",
            )
    if "weblogic-server" in payload:
        value = payload["weblogic-server"]
        if value not in VALID_BODY_WEBLOGIC_SERVER:
            return (
                False,
                f"Invalid value for 'weblogic-server'='{value}'. Must be one of: {', '.join(VALID_BODY_WEBLOGIC_SERVER)}",
            )
    if "websphere-server" in payload:
        value = payload["websphere-server"]
        if value not in VALID_BODY_WEBSPHERE_SERVER:
            return (
                False,
                f"Invalid value for 'websphere-server'='{value}'. Must be one of: {', '.join(VALID_BODY_WEBSPHERE_SERVER)}",
            )
    if "ssl-mode" in payload:
        value = payload["ssl-mode"]
        if value not in VALID_BODY_SSL_MODE:
            return (
                False,
                f"Invalid value for 'ssl-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MODE)}",
            )
    if "ssl-dh-bits" in payload:
        value = payload["ssl-dh-bits"]
        if value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid value for 'ssl-dh-bits'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )
    if "ssl-algorithm" in payload:
        value = payload["ssl-algorithm"]
        if value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid value for 'ssl-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )
    if "ssl-server-algorithm" in payload:
        value = payload["ssl-server-algorithm"]
        if value not in VALID_BODY_SSL_SERVER_ALGORITHM:
            return (
                False,
                f"Invalid value for 'ssl-server-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_ALGORITHM)}",
            )
    if "ssl-pfs" in payload:
        value = payload["ssl-pfs"]
        if value not in VALID_BODY_SSL_PFS:
            return (
                False,
                f"Invalid value for 'ssl-pfs'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_PFS)}",
            )
    if "ssl-min-version" in payload:
        value = payload["ssl-min-version"]
        if value not in VALID_BODY_SSL_MIN_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-min-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_VERSION)}",
            )
    if "ssl-max-version" in payload:
        value = payload["ssl-max-version"]
        if value not in VALID_BODY_SSL_MAX_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-max-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MAX_VERSION)}",
            )
    if "ssl-server-min-version" in payload:
        value = payload["ssl-server-min-version"]
        if value not in VALID_BODY_SSL_SERVER_MIN_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-server-min-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_MIN_VERSION)}",
            )
    if "ssl-server-max-version" in payload:
        value = payload["ssl-server-max-version"]
        if value not in VALID_BODY_SSL_SERVER_MAX_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-server-max-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_MAX_VERSION)}",
            )
    if "ssl-accept-ffdhe-groups" in payload:
        value = payload["ssl-accept-ffdhe-groups"]
        if value not in VALID_BODY_SSL_ACCEPT_FFDHE_GROUPS:
            return (
                False,
                f"Invalid value for 'ssl-accept-ffdhe-groups'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ACCEPT_FFDHE_GROUPS)}",
            )
    if "ssl-send-empty-frags" in payload:
        value = payload["ssl-send-empty-frags"]
        if value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            return (
                False,
                f"Invalid value for 'ssl-send-empty-frags'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SEND_EMPTY_FRAGS)}",
            )
    if "ssl-client-fallback" in payload:
        value = payload["ssl-client-fallback"]
        if value not in VALID_BODY_SSL_CLIENT_FALLBACK:
            return (
                False,
                f"Invalid value for 'ssl-client-fallback'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_FALLBACK)}",
            )
    if "ssl-client-renegotiation" in payload:
        value = payload["ssl-client-renegotiation"]
        if value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            return (
                False,
                f"Invalid value for 'ssl-client-renegotiation'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_RENEGOTIATION)}",
            )
    if "ssl-client-session-state-type" in payload:
        value = payload["ssl-client-session-state-type"]
        if value not in VALID_BODY_SSL_CLIENT_SESSION_STATE_TYPE:
            return (
                False,
                f"Invalid value for 'ssl-client-session-state-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_SESSION_STATE_TYPE)}",
            )
    if "ssl-server-renegotiation" in payload:
        value = payload["ssl-server-renegotiation"]
        if value not in VALID_BODY_SSL_SERVER_RENEGOTIATION:
            return (
                False,
                f"Invalid value for 'ssl-server-renegotiation'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_RENEGOTIATION)}",
            )
    if "ssl-server-session-state-type" in payload:
        value = payload["ssl-server-session-state-type"]
        if value not in VALID_BODY_SSL_SERVER_SESSION_STATE_TYPE:
            return (
                False,
                f"Invalid value for 'ssl-server-session-state-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_SESSION_STATE_TYPE)}",
            )
    if "ssl-http-location-conversion" in payload:
        value = payload["ssl-http-location-conversion"]
        if value not in VALID_BODY_SSL_HTTP_LOCATION_CONVERSION:
            return (
                False,
                f"Invalid value for 'ssl-http-location-conversion'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HTTP_LOCATION_CONVERSION)}",
            )
    if "ssl-http-match-host" in payload:
        value = payload["ssl-http-match-host"]
        if value not in VALID_BODY_SSL_HTTP_MATCH_HOST:
            return (
                False,
                f"Invalid value for 'ssl-http-match-host'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HTTP_MATCH_HOST)}",
            )
    if "ssl-hpkp" in payload:
        value = payload["ssl-hpkp"]
        if value not in VALID_BODY_SSL_HPKP:
            return (
                False,
                f"Invalid value for 'ssl-hpkp'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HPKP)}",
            )
    if "ssl-hpkp-include-subdomains" in payload:
        value = payload["ssl-hpkp-include-subdomains"]
        if value not in VALID_BODY_SSL_HPKP_INCLUDE_SUBDOMAINS:
            return (
                False,
                f"Invalid value for 'ssl-hpkp-include-subdomains'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HPKP_INCLUDE_SUBDOMAINS)}",
            )
    if "ssl-hsts" in payload:
        value = payload["ssl-hsts"]
        if value not in VALID_BODY_SSL_HSTS:
            return (
                False,
                f"Invalid value for 'ssl-hsts'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HSTS)}",
            )
    if "ssl-hsts-include-subdomains" in payload:
        value = payload["ssl-hsts-include-subdomains"]
        if value not in VALID_BODY_SSL_HSTS_INCLUDE_SUBDOMAINS:
            return (
                False,
                f"Invalid value for 'ssl-hsts-include-subdomains'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HSTS_INCLUDE_SUBDOMAINS)}",
            )
    if "one-click-gslb-server" in payload:
        value = payload["one-click-gslb-server"]
        if value not in VALID_BODY_ONE_CLICK_GSLB_SERVER:
            return (
                False,
                f"Invalid value for 'one-click-gslb-server'='{value}'. Must be one of: {', '.join(VALID_BODY_ONE_CLICK_GSLB_SERVER)}",
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
    "endpoint": "firewall/vip",
    "category": "cmdb",
    "api_path": "firewall/vip",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure virtual IP for IPv4.",
    "total_fields": 98,
    "required_fields_count": 7,
    "fields_with_defaults_count": 84,
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
