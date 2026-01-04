from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class VipPayload(TypedDict, total=False):
    """
    Type hints for firewall/vip payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: VipPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Virtual IP name.
    id: NotRequired[int]  # Custom defined ID.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    comment: NotRequired[str]  # Comment.
    type: NotRequired[Literal["static-nat", "load-balance", "server-load-balance", "dns-translation", "fqdn", "access-proxy"]]  # Configure a static NAT, load balance, server load balance, a
    server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"]  # Protocol to be load balanced by the virtual server (also cal
    dns_mapping_ttl: NotRequired[int]  # DNS mapping TTL (Set to zero to use TTL in DNS response, def
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
    ssl_mode: NotRequired[Literal["half", "full"]]  # Apply SSL offloading between the client and the FortiGate (h
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


class Vip:
    """
    Configure virtual IP for IPv4.
    
    Path: firewall/vip
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        src_filter: list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        src_filter: list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        service: list[dict[str, Any]] | None = ...,
        extip: str | None = ...,
        extaddr: list[dict[str, Any]] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat44: Literal["disable", "enable"] | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        mappedip: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: VipPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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