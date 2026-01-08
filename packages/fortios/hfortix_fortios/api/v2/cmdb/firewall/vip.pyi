from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class VipPayload(TypedDict, total=False):
    """
    Type hints for firewall/vip payload fields.
    
    Configure virtual IP for IPv4.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address.AddressEndpoint` (via: mapped-addr)
        - :class:`~.system.interface.InterfaceEndpoint` (via: extintf)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: ssl-hpkp-backup, ssl-hpkp-primary)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: ssl-hpkp-backup, ssl-hpkp-primary)

    **Usage:**
        payload: VipPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Virtual IP name.
    id: NotRequired[int]  # Custom defined ID.
    uuid: NotRequired[str]  # Universally Unique Identifier
    comment: NotRequired[str]  # Comment.
    type: NotRequired[Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"]]  # Configure a static NAT, load balance, server load balance, a
    server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"]  # Protocol to be load balanced by the virtual server
    dns_mapping_ttl: NotRequired[int]  # DNS mapping TTL
    ldb_method: NotRequired[Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"]]  # Method used to distribute sessions to real servers.
    src_filter: NotRequired[list[dict[str, Any]]]  # Source address filter. Each address must be either an IP/sub
    src_vip_filter: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of 'src-filter' to match destinations for
    service: NotRequired[list[dict[str, Any]]]  # Service name.
    extip: str  # IP address or address range on the external interface that y
    extaddr: NotRequired[list[dict[str, Any]]]  # External FQDN address name.
    h2_support: Literal["enable", "disable"]  # Enable/disable HTTP2 support (default = enable).
    h3_support: NotRequired[Literal["enable", "disable"]]  # Enable/disable HTTP3/QUIC support (default = disable).
    quic: NotRequired[str]  # QUIC setting.
    nat44: NotRequired[Literal["disable", "enable"]]  # Enable/disable NAT44.
    nat46: NotRequired[Literal["disable", "enable"]]  # Enable/disable NAT46.
    add_nat46_route: NotRequired[Literal["disable", "enable"]]  # Enable/disable adding NAT46 route.
    mappedip: list[dict[str, Any]]  # IP address or address range on the destination network to wh
    mapped_addr: NotRequired[str]  # Mapped FQDN address name.
    extintf: str  # Interface connected to the source network that receives the
    arp_reply: NotRequired[Literal["disable", "enable"]]  # Enable to respond to ARP requests for this virtual IP addres
    http_redirect: NotRequired[Literal["enable", "disable"]]  # Enable/disable redirection of HTTP to HTTPS.
    persistence: NotRequired[Literal["none", "http-cookie", "ssl-session-id"]]  # Configure how to make sure that clients connect to the same
    nat_source_vip: NotRequired[Literal["disable", "enable"]]  # Enable/disable forcing the source NAT mapped IP to the exter
    portforward: NotRequired[Literal["disable", "enable"]]  # Enable/disable port forwarding.
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable VIP.
    protocol: NotRequired[Literal["tcp", "udp", "sctp", "icmp"]]  # Protocol to use when forwarding packets.
    extport: str  # Incoming port number range that you want to map to a port nu
    mappedport: NotRequired[str]  # Port number range on the destination network to which the ex
    gratuitous_arp_interval: NotRequired[int]  # Enable to have the VIP send gratuitous ARPs. 0=disabled. Set
    srcintf_filter: NotRequired[list[dict[str, Any]]]  # Interfaces to which the VIP applies. Separate the names with
    portmapping_type: NotRequired[Literal["1-to-1", "m-to-n"]]  # Port mapping type.
    empty_cert_action: NotRequired[Literal["accept", "block", "accept-unmanageable"]]  # Action for an empty client certificate.
    user_agent_detect: NotRequired[Literal["disable", "enable"]]  # Enable/disable detecting device type by HTTP user-agent if n
    client_cert: NotRequired[Literal["disable", "enable"]]  # Enable/disable requesting client certificate.
    realservers: NotRequired[list[dict[str, Any]]]  # Select the real servers that this server load balancing VIP
    http_cookie_domain_from_host: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of HTTP cookie domain from host field in
    http_cookie_domain: NotRequired[str]  # Domain that HTTP cookie persistence should apply to.
    http_cookie_path: NotRequired[str]  # Limit HTTP cookie persistence to the specified path.
    http_cookie_generation: NotRequired[int]  # Generation of HTTP cookie to be accepted. Changing invalidat
    http_cookie_age: NotRequired[int]  # Time in minutes that client web browsers should keep a cooki
    http_cookie_share: NotRequired[Literal["disable", "same-ip"]]  # Control sharing of cookies across virtual servers. Use of sa
    https_cookie_secure: NotRequired[Literal["disable", "enable"]]  # Enable/disable verification that inserted HTTPS cookies are
    http_multiplex: NotRequired[Literal["enable", "disable"]]  # Enable/disable HTTP multiplexing.
    http_multiplex_ttl: NotRequired[int]  # Time-to-live for idle connections to servers.
    http_multiplex_max_request: NotRequired[int]  # Maximum number of requests that a multiplex server can handl
    http_multiplex_max_concurrent_request: NotRequired[int]  # Maximum number of concurrent requests that a multiplex serve
    http_ip_header: NotRequired[Literal["enable", "disable"]]  # For HTTP multiplexing, enable to add the original client IP
    http_ip_header_name: NotRequired[str]  # For HTTP multiplexing, enter a custom HTTPS header name. The
    outlook_web_access: NotRequired[Literal["disable", "enable"]]  # Enable to add the Front-End-Https header for Microsoft Outlo
    weblogic_server: NotRequired[Literal["disable", "enable"]]  # Enable to add an HTTP header to indicate SSL offloading for
    websphere_server: NotRequired[Literal["disable", "enable"]]  # Enable to add an HTTP header to indicate SSL offloading for
    ssl_mode: NotRequired[Literal["half", "full"]]  # Apply SSL offloading between the client and the FortiGate
    ssl_certificate: list[dict[str, Any]]  # Name of the certificate to use for SSL handshake.
    ssl_dh_bits: NotRequired[Literal["768", "1024", "1536", "2048", "3072", "4096"]]  # Number of bits to use in the Diffie-Hellman exchange for RSA
    ssl_algorithm: NotRequired[Literal["high", "medium", "low", "custom"]]  # Permitted encryption algorithms for SSL sessions according t
    ssl_cipher_suites: NotRequired[list[dict[str, Any]]]  # SSL/TLS cipher suites acceptable from a client, ordered by p
    ssl_server_algorithm: NotRequired[Literal["high", "medium", "low", "custom", "client"]]  # Permitted encryption algorithms for the server side of SSL f
    ssl_server_cipher_suites: NotRequired[list[dict[str, Any]]]  # SSL/TLS cipher suites to offer to a server, ordered by prior
    ssl_pfs: NotRequired[Literal["require", "deny", "allow"]]  # Select the cipher suites that can be used for SSL perfect fo
    ssl_min_version: NotRequired[Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]]  # Lowest SSL/TLS version acceptable from a client.
    ssl_max_version: NotRequired[Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]]  # Highest SSL/TLS version acceptable from a client.
    ssl_server_min_version: NotRequired[Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]]  # Lowest SSL/TLS version acceptable from a server. Use the cli
    ssl_server_max_version: NotRequired[Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]]  # Highest SSL/TLS version acceptable from a server. Use the cl
    ssl_accept_ffdhe_groups: NotRequired[Literal["enable", "disable"]]  # Enable/disable FFDHE cipher suite for SSL key exchange.
    ssl_send_empty_frags: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending empty fragments to avoid CBC IV attac
    ssl_client_fallback: NotRequired[Literal["disable", "enable"]]  # Enable/disable support for preventing Downgrade Attacks on c
    ssl_client_renegotiation: NotRequired[Literal["allow", "deny", "secure"]]  # Allow, deny, or require secure renegotiation of client sessi
    ssl_client_session_state_type: NotRequired[Literal["disable", "time", "count", "both"]]  # How to expire SSL sessions for the segment of the SSL connec
    ssl_client_session_state_timeout: NotRequired[int]  # Number of minutes to keep client to FortiGate SSL session st
    ssl_client_session_state_max: NotRequired[int]  # Maximum number of client to FortiGate SSL session states to
    ssl_client_rekey_count: NotRequired[int]  # Maximum length of data in MB before triggering a client reke
    ssl_server_renegotiation: NotRequired[Literal["enable", "disable"]]  # Enable/disable secure renegotiation to comply with RFC 5746.
    ssl_server_session_state_type: NotRequired[Literal["disable", "time", "count", "both"]]  # How to expire SSL sessions for the segment of the SSL connec
    ssl_server_session_state_timeout: NotRequired[int]  # Number of minutes to keep FortiGate to Server SSL session st
    ssl_server_session_state_max: NotRequired[int]  # Maximum number of FortiGate to Server SSL session states to
    ssl_http_location_conversion: NotRequired[Literal["enable", "disable"]]  # Enable to replace HTTP with HTTPS in the reply's Location HT
    ssl_http_match_host: NotRequired[Literal["enable", "disable"]]  # Enable/disable HTTP host matching for location conversion.
    ssl_hpkp: NotRequired[Literal["disable", "enable", "report-only"]]  # Enable/disable including HPKP header in response.
    ssl_hpkp_primary: NotRequired[str]  # Certificate to generate primary HPKP pin from.
    ssl_hpkp_backup: NotRequired[str]  # Certificate to generate backup HPKP pin from.
    ssl_hpkp_age: NotRequired[int]  # Number of seconds the client should honor the HPKP setting.
    ssl_hpkp_report_uri: NotRequired[str]  # URL to report HPKP violations to.
    ssl_hpkp_include_subdomains: NotRequired[Literal["disable", "enable"]]  # Indicate that HPKP header applies to all subdomains.
    ssl_hsts: NotRequired[Literal["disable", "enable"]]  # Enable/disable including HSTS header in response.
    ssl_hsts_age: NotRequired[int]  # Number of seconds the client should honor the HSTS setting.
    ssl_hsts_include_subdomains: NotRequired[Literal["disable", "enable"]]  # Indicate that HSTS header applies to all subdomains.
    monitor: NotRequired[list[dict[str, Any]]]  # Name of the health check monitor to use when polling to dete
    max_embryonic_connections: NotRequired[int]  # Maximum number of incomplete connections.
    color: NotRequired[int]  # Color of icon on the GUI.
    ipv6_mappedip: str  # Range of mapped IPv6 addresses. Specify the start IPv6 addre
    ipv6_mappedport: NotRequired[str]  # IPv6 port number range on the destination network to which t
    one_click_gslb_server: NotRequired[Literal["disable", "enable"]]  # Enable/disable one click GSLB server integration with FortiG
    gslb_hostname: NotRequired[str]  # Hostname to use within the configured FortiGSLB domain.
    gslb_domain_name: NotRequired[str]  # Domain to use when integrating with FortiGSLB.
    gslb_public_ips: NotRequired[list[dict[str, Any]]]  # Publicly accessible IP addresses for the FortiGSLB service.

# Nested classes for table field children

@final
class VipSrcfilterObject:
    """Typed object for src-filter table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Source-filter range.
    range: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class VipServiceObject:
    """Typed object for service table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Service name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class VipExtaddrObject:
    """Typed object for extaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class VipMappedipObject:
    """Typed object for mappedip table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Mapped IP range.
    range: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class VipSrcintffilterObject:
    """Typed object for srcintf-filter table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
    interface_name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class VipRealserversObject:
    """Typed object for realservers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Real server ID.
    id: int
    # Type of address.
    type: Literal["ip", "address"]
    # Dynamic address of the real server.
    address: str
    # IP address of the real server.
    ip: str
    # Port for communicating with the real server. Required if port forwarding is enab
    port: int
    # Set the status of the real server to active so that it can accept traffic, or on
    status: Literal["active", "standby", "disable"]
    # Weight of the real server. If weighted load balancing is enabled, the server wit
    weight: int
    # Time in seconds that the system waits before re-activating a previously down act
    holddown_interval: int
    # Enable to check the responsiveness of the real server before forwarding traffic.
    healthcheck: Literal["disable", "enable", "vip"]
    # HTTP server domain name in HTTP header.
    http_host: str
    # Enable/disable translation of hostname/IP from virtual server to real server.
    translate_host: Literal["enable", "disable"]
    # Max number of active connections that can be directed to the real server. When r
    max_connections: int
    # Name of the health check monitor to use when polling to determine a virtual serv
    monitor: str
    # Only clients in this IP range can connect to this real server.
    client_ip: str
    # Enable/disable certificate verification of the real server.
    verify_cert: Literal["enable", "disable"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class VipSslcertificateObject:
    """Typed object for ssl-certificate table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Certificate list.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class VipSslciphersuitesObject:
    """Typed object for ssl-cipher-suites table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SSL/TLS cipher suites priority.
    priority: int
    # Cipher suite name.
    cipher: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-128-GCM-SHA256", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-AES-128-CBC-SHA", "TLS-RSA-WITH-AES-256-CBC-SHA", "TLS-RSA-WITH-AES-128-CBC-SHA256", "TLS-RSA-WITH-AES-128-GCM-SHA256", "TLS-RSA-WITH-AES-256-CBC-SHA256", "TLS-RSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-SEED-CBC-SHA", "TLS-DHE-DSS-WITH-SEED-CBC-SHA", "TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384", "TLS-RSA-WITH-SEED-CBC-SHA", "TLS-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-RC4-128-SHA", "TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-RC4-128-MD5", "TLS-RSA-WITH-RC4-128-SHA", "TLS-DHE-RSA-WITH-DES-CBC-SHA", "TLS-DHE-DSS-WITH-DES-CBC-SHA", "TLS-RSA-WITH-DES-CBC-SHA"]
    # SSL/TLS versions that the cipher suite can be used with.
    versions: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class VipSslserverciphersuitesObject:
    """Typed object for ssl-server-cipher-suites table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SSL/TLS cipher suites priority.
    priority: int
    # Cipher suite name.
    cipher: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA", "TLS-DHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-DHE-RSA-WITH-AES-256-CBC-SHA256", "TLS-DHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA", "TLS-DHE-DSS-WITH-AES-128-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-128-GCM-SHA256", "TLS-DHE-DSS-WITH-AES-256-CBC-SHA256", "TLS-DHE-DSS-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA", "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-AES-128-CBC-SHA", "TLS-RSA-WITH-AES-256-CBC-SHA", "TLS-RSA-WITH-AES-128-CBC-SHA256", "TLS-RSA-WITH-AES-128-GCM-SHA256", "TLS-RSA-WITH-AES-256-CBC-SHA256", "TLS-RSA-WITH-AES-256-GCM-SHA384", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA", "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256", "TLS-DHE-RSA-WITH-SEED-CBC-SHA", "TLS-DHE-DSS-WITH-SEED-CBC-SHA", "TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256", "TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384", "TLS-RSA-WITH-SEED-CBC-SHA", "TLS-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256", "TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384", "TLS-ECDHE-RSA-WITH-RC4-128-SHA", "TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-3DES-EDE-CBC-SHA", "TLS-RSA-WITH-RC4-128-MD5", "TLS-RSA-WITH-RC4-128-SHA", "TLS-DHE-RSA-WITH-DES-CBC-SHA", "TLS-DHE-DSS-WITH-DES-CBC-SHA", "TLS-RSA-WITH-DES-CBC-SHA"]
    # SSL/TLS versions that the cipher suite can be used with.
    versions: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class VipMonitorObject:
    """Typed object for monitor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Health monitor name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class VipGslbpublicipsObject:
    """Typed object for gslb-public-ips table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Index of this public IP setting.
    index: int
    # The publicly accessible IP address.
    ip: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class VipResponse(TypedDict):
    """
    Type hints for firewall/vip API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    id: int
    uuid: str
    comment: str
    type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"]
    server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"]
    dns_mapping_ttl: int
    ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"]
    src_filter: list[dict[str, Any]]
    src_vip_filter: Literal["disable", "enable"]
    service: list[dict[str, Any]]
    extip: str
    extaddr: list[dict[str, Any]]
    h2_support: Literal["enable", "disable"]
    h3_support: Literal["enable", "disable"]
    quic: str
    nat44: Literal["disable", "enable"]
    nat46: Literal["disable", "enable"]
    add_nat46_route: Literal["disable", "enable"]
    mappedip: list[dict[str, Any]]
    mapped_addr: str
    extintf: str
    arp_reply: Literal["disable", "enable"]
    http_redirect: Literal["enable", "disable"]
    persistence: Literal["none", "http-cookie", "ssl-session-id"]
    nat_source_vip: Literal["disable", "enable"]
    portforward: Literal["disable", "enable"]
    status: Literal["disable", "enable"]
    protocol: Literal["tcp", "udp", "sctp", "icmp"]
    extport: str
    mappedport: str
    gratuitous_arp_interval: int
    srcintf_filter: list[dict[str, Any]]
    portmapping_type: Literal["1-to-1", "m-to-n"]
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]
    user_agent_detect: Literal["disable", "enable"]
    client_cert: Literal["disable", "enable"]
    realservers: list[dict[str, Any]]
    http_cookie_domain_from_host: Literal["disable", "enable"]
    http_cookie_domain: str
    http_cookie_path: str
    http_cookie_generation: int
    http_cookie_age: int
    http_cookie_share: Literal["disable", "same-ip"]
    https_cookie_secure: Literal["disable", "enable"]
    http_multiplex: Literal["enable", "disable"]
    http_multiplex_ttl: int
    http_multiplex_max_request: int
    http_multiplex_max_concurrent_request: int
    http_ip_header: Literal["enable", "disable"]
    http_ip_header_name: str
    outlook_web_access: Literal["disable", "enable"]
    weblogic_server: Literal["disable", "enable"]
    websphere_server: Literal["disable", "enable"]
    ssl_mode: Literal["half", "full"]
    ssl_certificate: list[dict[str, Any]]
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]
    ssl_algorithm: Literal["high", "medium", "low", "custom"]
    ssl_cipher_suites: list[dict[str, Any]]
    ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"]
    ssl_server_cipher_suites: list[dict[str, Any]]
    ssl_pfs: Literal["require", "deny", "allow"]
    ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]
    ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]
    ssl_accept_ffdhe_groups: Literal["enable", "disable"]
    ssl_send_empty_frags: Literal["enable", "disable"]
    ssl_client_fallback: Literal["disable", "enable"]
    ssl_client_renegotiation: Literal["allow", "deny", "secure"]
    ssl_client_session_state_type: Literal["disable", "time", "count", "both"]
    ssl_client_session_state_timeout: int
    ssl_client_session_state_max: int
    ssl_client_rekey_count: int
    ssl_server_renegotiation: Literal["enable", "disable"]
    ssl_server_session_state_type: Literal["disable", "time", "count", "both"]
    ssl_server_session_state_timeout: int
    ssl_server_session_state_max: int
    ssl_http_location_conversion: Literal["enable", "disable"]
    ssl_http_match_host: Literal["enable", "disable"]
    ssl_hpkp: Literal["disable", "enable", "report-only"]
    ssl_hpkp_primary: str
    ssl_hpkp_backup: str
    ssl_hpkp_age: int
    ssl_hpkp_report_uri: str
    ssl_hpkp_include_subdomains: Literal["disable", "enable"]
    ssl_hsts: Literal["disable", "enable"]
    ssl_hsts_age: int
    ssl_hsts_include_subdomains: Literal["disable", "enable"]
    monitor: list[dict[str, Any]]
    max_embryonic_connections: int
    color: int
    ipv6_mappedip: str
    ipv6_mappedport: str
    one_click_gslb_server: Literal["disable", "enable"]
    gslb_hostname: str
    gslb_domain_name: str
    gslb_public_ips: list[dict[str, Any]]


@final
class VipObject:
    """Typed FortiObject for firewall/vip with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Virtual IP name.
    name: str
    # Custom defined ID.
    id: int
    # Universally Unique Identifier
    uuid: str
    # Comment.
    comment: str
    # Configure a static NAT, load balance, server load balance, access proxy, DNS tra
    type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"]
    # Protocol to be load balanced by the virtual server
    server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"]
    # DNS mapping TTL (Set to zero to use TTL in DNS response, default = 0).
    dns_mapping_ttl: int
    # Method used to distribute sessions to real servers.
    ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"]
    # Source address filter. Each address must be either an IP/subnet (x.x.x.x/n) or a
    src_filter: list[VipSrcfilterObject]  # Table field - list of typed objects
    # Enable/disable use of 'src-filter' to match destinations for the reverse SNAT ru
    src_vip_filter: Literal["disable", "enable"]
    # Service name.
    service: list[VipServiceObject]  # Table field - list of typed objects
    # IP address or address range on the external interface that you want to map to an
    extip: str
    # External FQDN address name.
    extaddr: list[VipExtaddrObject]  # Table field - list of typed objects
    # Enable/disable HTTP2 support (default = enable).
    h2_support: Literal["enable", "disable"]
    # Enable/disable HTTP3/QUIC support (default = disable).
    h3_support: Literal["enable", "disable"]
    # QUIC setting.
    quic: str
    # Enable/disable NAT44.
    nat44: Literal["disable", "enable"]
    # Enable/disable NAT46.
    nat46: Literal["disable", "enable"]
    # Enable/disable adding NAT46 route.
    add_nat46_route: Literal["disable", "enable"]
    # IP address or address range on the destination network to which the external IP
    mappedip: list[VipMappedipObject]  # Table field - list of typed objects
    # Mapped FQDN address name.
    mapped_addr: str
    # Interface connected to the source network that receives the packets that will be
    extintf: str
    # Enable to respond to ARP requests for this virtual IP address. Enabled by defaul
    arp_reply: Literal["disable", "enable"]
    # Enable/disable redirection of HTTP to HTTPS.
    http_redirect: Literal["enable", "disable"]
    # Configure how to make sure that clients connect to the same server every time th
    persistence: Literal["none", "http-cookie", "ssl-session-id"]
    # Enable/disable forcing the source NAT mapped IP to the external IP for all traff
    nat_source_vip: Literal["disable", "enable"]
    # Enable/disable port forwarding.
    portforward: Literal["disable", "enable"]
    # Enable/disable VIP.
    status: Literal["disable", "enable"]
    # Protocol to use when forwarding packets.
    protocol: Literal["tcp", "udp", "sctp", "icmp"]
    # Incoming port number range that you want to map to a port number range on the de
    extport: str
    # Port number range on the destination network to which the external port number r
    mappedport: str
    # Enable to have the VIP send gratuitous ARPs. 0=disabled. Set from 5 up to 864000
    gratuitous_arp_interval: int
    # Interfaces to which the VIP applies. Separate the names with spaces.
    srcintf_filter: list[VipSrcintffilterObject]  # Table field - list of typed objects
    # Port mapping type.
    portmapping_type: Literal["1-to-1", "m-to-n"]
    # Action for an empty client certificate.
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]
    # Enable/disable detecting device type by HTTP user-agent if no client certificate
    user_agent_detect: Literal["disable", "enable"]
    # Enable/disable requesting client certificate.
    client_cert: Literal["disable", "enable"]
    # Select the real servers that this server load balancing VIP will distribute traf
    realservers: list[VipRealserversObject]  # Table field - list of typed objects
    # Enable/disable use of HTTP cookie domain from host field in HTTP.
    http_cookie_domain_from_host: Literal["disable", "enable"]
    # Domain that HTTP cookie persistence should apply to.
    http_cookie_domain: str
    # Limit HTTP cookie persistence to the specified path.
    http_cookie_path: str
    # Generation of HTTP cookie to be accepted. Changing invalidates all existing cook
    http_cookie_generation: int
    # Time in minutes that client web browsers should keep a cookie. Default is 60 min
    http_cookie_age: int
    # Control sharing of cookies across virtual servers. Use of same-ip means a cookie
    http_cookie_share: Literal["disable", "same-ip"]
    # Enable/disable verification that inserted HTTPS cookies are secure.
    https_cookie_secure: Literal["disable", "enable"]
    # Enable/disable HTTP multiplexing.
    http_multiplex: Literal["enable", "disable"]
    # Time-to-live for idle connections to servers.
    http_multiplex_ttl: int
    # Maximum number of requests that a multiplex server can handle before disconnecti
    http_multiplex_max_request: int
    # Maximum number of concurrent requests that a multiplex server can handle
    http_multiplex_max_concurrent_request: int
    # For HTTP multiplexing, enable to add the original client IP address in the X-For
    http_ip_header: Literal["enable", "disable"]
    # For HTTP multiplexing, enter a custom HTTPS header name. The original client IP
    http_ip_header_name: str
    # Enable to add the Front-End-Https header for Microsoft Outlook Web Access.
    outlook_web_access: Literal["disable", "enable"]
    # Enable to add an HTTP header to indicate SSL offloading for a WebLogic server.
    weblogic_server: Literal["disable", "enable"]
    # Enable to add an HTTP header to indicate SSL offloading for a WebSphere server.
    websphere_server: Literal["disable", "enable"]
    # Apply SSL offloading between the client and the FortiGate (half) or from the cli
    ssl_mode: Literal["half", "full"]
    # Name of the certificate to use for SSL handshake.
    ssl_certificate: list[VipSslcertificateObject]  # Table field - list of typed objects
    # Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL s
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]
    # Permitted encryption algorithms for SSL sessions according to encryption strengt
    ssl_algorithm: Literal["high", "medium", "low", "custom"]
    # SSL/TLS cipher suites acceptable from a client, ordered by priority.
    ssl_cipher_suites: list[VipSslciphersuitesObject]  # Table field - list of typed objects
    # Permitted encryption algorithms for the server side of SSL full mode sessions ac
    ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"]
    # SSL/TLS cipher suites to offer to a server, ordered by priority.
    ssl_server_cipher_suites: list[VipSslserverciphersuitesObject]  # Table field - list of typed objects
    # Select the cipher suites that can be used for SSL perfect forward secrecy (PFS).
    ssl_pfs: Literal["require", "deny", "allow"]
    # Lowest SSL/TLS version acceptable from a client.
    ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Highest SSL/TLS version acceptable from a client.
    ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Lowest SSL/TLS version acceptable from a server. Use the client setting by defau
    ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]
    # Highest SSL/TLS version acceptable from a server. Use the client setting by defa
    ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"]
    # Enable/disable FFDHE cipher suite for SSL key exchange.
    ssl_accept_ffdhe_groups: Literal["enable", "disable"]
    # Enable/disable sending empty fragments to avoid CBC IV attacks
    ssl_send_empty_frags: Literal["enable", "disable"]
    # Enable/disable support for preventing Downgrade Attacks on client connections
    ssl_client_fallback: Literal["disable", "enable"]
    # Allow, deny, or require secure renegotiation of client sessions to comply with R
    ssl_client_renegotiation: Literal["allow", "deny", "secure"]
    # How to expire SSL sessions for the segment of the SSL connection between the cli
    ssl_client_session_state_type: Literal["disable", "time", "count", "both"]
    # Number of minutes to keep client to FortiGate SSL session state.
    ssl_client_session_state_timeout: int
    # Maximum number of client to FortiGate SSL session states to keep.
    ssl_client_session_state_max: int
    # Maximum length of data in MB before triggering a client rekey (0 = disable).
    ssl_client_rekey_count: int
    # Enable/disable secure renegotiation to comply with RFC 5746.
    ssl_server_renegotiation: Literal["enable", "disable"]
    # How to expire SSL sessions for the segment of the SSL connection between the ser
    ssl_server_session_state_type: Literal["disable", "time", "count", "both"]
    # Number of minutes to keep FortiGate to Server SSL session state.
    ssl_server_session_state_timeout: int
    # Maximum number of FortiGate to Server SSL session states to keep.
    ssl_server_session_state_max: int
    # Enable to replace HTTP with HTTPS in the reply's Location HTTP header field.
    ssl_http_location_conversion: Literal["enable", "disable"]
    # Enable/disable HTTP host matching for location conversion.
    ssl_http_match_host: Literal["enable", "disable"]
    # Enable/disable including HPKP header in response.
    ssl_hpkp: Literal["disable", "enable", "report-only"]
    # Certificate to generate primary HPKP pin from.
    ssl_hpkp_primary: str
    # Certificate to generate backup HPKP pin from.
    ssl_hpkp_backup: str
    # Number of seconds the client should honor the HPKP setting.
    ssl_hpkp_age: int
    # URL to report HPKP violations to.
    ssl_hpkp_report_uri: str
    # Indicate that HPKP header applies to all subdomains.
    ssl_hpkp_include_subdomains: Literal["disable", "enable"]
    # Enable/disable including HSTS header in response.
    ssl_hsts: Literal["disable", "enable"]
    # Number of seconds the client should honor the HSTS setting.
    ssl_hsts_age: int
    # Indicate that HSTS header applies to all subdomains.
    ssl_hsts_include_subdomains: Literal["disable", "enable"]
    # Name of the health check monitor to use when polling to determine a virtual serv
    monitor: list[VipMonitorObject]  # Table field - list of typed objects
    # Maximum number of incomplete connections.
    max_embryonic_connections: int
    # Color of icon on the GUI.
    color: int
    # Range of mapped IPv6 addresses. Specify the start IPv6 address followed by a spa
    ipv6_mappedip: str
    # IPv6 port number range on the destination network to which the external port num
    ipv6_mappedport: str
    # Enable/disable one click GSLB server integration with FortiGSLB.
    one_click_gslb_server: Literal["disable", "enable"]
    # Hostname to use within the configured FortiGSLB domain.
    gslb_hostname: str
    # Domain to use when integrating with FortiGSLB.
    gslb_domain_name: str
    # Publicly accessible IP addresses for the FortiGSLB service.
    gslb_public_ips: list[VipGslbpublicipsObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> VipPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Vip:
    """
    Configure virtual IP for IPv4.
    
    Path: firewall/vip
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VipObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VipObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[VipObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> VipResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> VipResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[VipResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> VipObject | list[VipObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VipObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VipObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VipObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: VipPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        dns_mapping_ttl: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: str | list[str] | list[dict[str, Any]] | None = ...,
        mapped_addr: str | None = ...,
        extintf: str | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp", "icmp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        gratuitous_arp_interval: int | None = ...,
        srcintf_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        portmapping_type: Literal["1-to-1", "m-to-n"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        realservers: str | list[str] | list[dict[str, Any]] | None = ...,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = ...,
        http_cookie_domain: str | None = ...,
        http_cookie_path: str | None = ...,
        http_cookie_generation: int | None = ...,
        http_cookie_age: int | None = ...,
        http_cookie_share: Literal["disable", "same-ip"] | None = ...,
        https_cookie_secure: Literal["disable", "enable"] | None = ...,
        http_multiplex: Literal["enable", "disable"] | None = ...,
        http_multiplex_ttl: int | None = ...,
        http_multiplex_max_request: int | None = ...,
        http_multiplex_max_concurrent_request: int | None = ...,
        http_ip_header: Literal["enable", "disable"] | None = ...,
        http_ip_header_name: str | None = ...,
        outlook_web_access: Literal["disable", "enable"] | None = ...,
        weblogic_server: Literal["disable", "enable"] | None = ...,
        websphere_server: Literal["disable", "enable"] | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = ...,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = ...,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_pfs: Literal["require", "deny", "allow"] | None = ...,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = ...,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        ssl_client_fallback: Literal["disable", "enable"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_client_session_state_timeout: int | None = ...,
        ssl_client_session_state_max: int | None = ...,
        ssl_client_rekey_count: int | None = ...,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = ...,
        ssl_server_session_state_timeout: int | None = ...,
        ssl_server_session_state_max: int | None = ...,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = ...,
        ssl_http_match_host: Literal["enable", "disable"] | None = ...,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = ...,
        ssl_hpkp_primary: str | None = ...,
        ssl_hpkp_backup: str | None = ...,
        ssl_hpkp_age: int | None = ...,
        ssl_hpkp_report_uri: str | None = ...,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = ...,
        ssl_hsts: Literal["disable", "enable"] | None = ...,
        ssl_hsts_age: int | None = ...,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        max_embryonic_connections: int | None = ...,
        color: int | None = ...,
        ipv6_mappedip: str | None = ...,
        ipv6_mappedport: str | None = ...,
        one_click_gslb_server: Literal["disable", "enable"] | None = ...,
        gslb_hostname: str | None = ...,
        gslb_domain_name: str | None = ...,
        gslb_public_ips: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> dict[str, Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> dict[str, Any]: ...
    
    @staticmethod
    def schema() -> dict[str, Any]: ...


__all__ = [
    "Vip",
    "VipPayload",
    "VipObject",
]