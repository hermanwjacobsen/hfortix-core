from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class Vip6Payload(TypedDict, total=False):
    """
    Type hints for firewall/vip6 payload fields.
    
    Configure virtual IP for IPv6.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: ssl-hpkp-backup, ssl-hpkp-primary)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: ssl-hpkp-backup, ssl-hpkp-primary)

    **Usage:**
        payload: Vip6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Virtual ip6 name.
    id: NotRequired[int]  # Custom defined ID.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    comment: NotRequired[str]  # Comment.
    type: NotRequired[Literal["static-nat", "server-load-balance", "access-proxy"]]  # Configure a static NAT server load balance VIP or access pro
    src_filter: NotRequired[list[dict[str, Any]]]  # Source IP6 filter (x:x:x:x:x:x:x:x/x). Separate addresses wi
    src_vip_filter: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of 'src-filter' to match destinations for
    extip: str  # IPv6 address or address range on the external interface that
    mappedip: str  # Mapped IPv6 address range in the format startIP-endIP.
    nat_source_vip: NotRequired[Literal["disable", "enable"]]  # Enable to perform SNAT on traffic from mappedip to the extip
    ndp_reply: NotRequired[Literal["disable", "enable"]]  # Enable/disable this FortiGate unit's ability to respond to N
    portforward: NotRequired[Literal["disable", "enable"]]  # Enable port forwarding.
    protocol: NotRequired[Literal["tcp", "udp", "sctp"]]  # Protocol to use when forwarding packets.
    extport: str  # Incoming port number range that you want to map to a port nu
    mappedport: NotRequired[str]  # Port number range on the destination network to which the ex
    color: NotRequired[int]  # Color of icon on the GUI.
    ldb_method: NotRequired[Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"]]  # Method used to distribute sessions to real servers.
    server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"]  # Protocol to be load balanced by the virtual server (also cal
    http_redirect: NotRequired[Literal["enable", "disable"]]  # Enable/disable redirection of HTTP to HTTPS.
    persistence: NotRequired[Literal["none", "http-cookie", "ssl-session-id"]]  # Configure how to make sure that clients connect to the same 
    h2_support: Literal["enable", "disable"]  # Enable/disable HTTP2 support (default = enable).
    h3_support: NotRequired[Literal["enable", "disable"]]  # Enable/disable HTTP3/QUIC support (default = disable).
    quic: NotRequired[str]  # QUIC setting.
    nat66: NotRequired[Literal["disable", "enable"]]  # Enable/disable DNAT66.
    nat64: NotRequired[Literal["disable", "enable"]]  # Enable/disable DNAT64.
    add_nat64_route: NotRequired[Literal["disable", "enable"]]  # Enable/disable adding NAT64 route.
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
    ssl_server_renegotiation: NotRequired[Literal["enable", "disable"]]  # Enable/disable secure renegotiation to comply with RFC 5746.
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
    ssl_server_session_state_type: NotRequired[Literal["disable", "time", "count", "both"]]  # How to expire SSL sessions for the segment of the SSL connec
    ssl_server_session_state_timeout: NotRequired[int]  # Number of minutes to keep FortiGate to Server SSL session st
    ssl_server_session_state_max: NotRequired[int]  # Maximum number of FortiGate to Server SSL session states to 
    ssl_http_location_conversion: NotRequired[Literal["enable", "disable"]]  # Enable to replace HTTP with HTTPS in the reply's Location HT
    ssl_http_match_host: NotRequired[Literal["enable", "disable"]]  # Enable/disable HTTP host matching for location conversion.
    ssl_hpkp: NotRequired[Literal["disable", "enable", "report-only"]]  # Enable/disable including HPKP header in response.
    ssl_hpkp_primary: NotRequired[str]  # Certificate to generate primary HPKP pin from.
    ssl_hpkp_backup: NotRequired[str]  # Certificate to generate backup HPKP pin from.
    ssl_hpkp_age: NotRequired[int]  # Number of minutes the web browser should keep HPKP.
    ssl_hpkp_report_uri: NotRequired[str]  # URL to report HPKP violations to.
    ssl_hpkp_include_subdomains: NotRequired[Literal["disable", "enable"]]  # Indicate that HPKP header applies to all subdomains.
    ssl_hsts: NotRequired[Literal["disable", "enable"]]  # Enable/disable including HSTS header in response.
    ssl_hsts_age: NotRequired[int]  # Number of seconds the client should honor the HSTS setting.
    ssl_hsts_include_subdomains: NotRequired[Literal["disable", "enable"]]  # Indicate that HSTS header applies to all subdomains.
    monitor: NotRequired[list[dict[str, Any]]]  # Name of the health check monitor to use when polling to dete
    max_embryonic_connections: NotRequired[int]  # Maximum number of incomplete connections.
    embedded_ipv4_address: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of the lower 32 bits of the external IPv6
    ipv4_mappedip: NotRequired[str]  # Range of mapped IP addresses. Specify the start IP address f
    ipv4_mappedport: NotRequired[str]  # IPv4 port number range on the destination network to which t


class Vip6Object(FortiObject[Vip6Payload]):
    """Typed FortiObject for firewall/vip6 with IDE autocomplete support."""
    
    # Virtual ip6 name.
    name: str
    # Custom defined ID.
    id: int
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Comment.
    comment: str
    # Configure a static NAT server load balance VIP or access proxy.
    type: Literal["static-nat", "server-load-balance", "access-proxy"]
    # Source IP6 filter (x:x:x:x:x:x:x:x/x). Separate addresses with spaces.
    src_filter: list[str]  # Auto-flattened from member_table
    # Enable/disable use of 'src-filter' to match destinations for the reverse SNAT ru
    src_vip_filter: Literal["disable", "enable"]
    # IPv6 address or address range on the external interface that you want to map to 
    extip: str
    # Mapped IPv6 address range in the format startIP-endIP.
    mappedip: str
    # Enable to perform SNAT on traffic from mappedip to the extip for all egress inte
    nat_source_vip: Literal["disable", "enable"]
    # Enable/disable this FortiGate unit's ability to respond to NDP requests for this
    ndp_reply: Literal["disable", "enable"]
    # Enable port forwarding.
    portforward: Literal["disable", "enable"]
    # Protocol to use when forwarding packets.
    protocol: Literal["tcp", "udp", "sctp"]
    # Incoming port number range that you want to map to a port number range on the de
    extport: str
    # Port number range on the destination network to which the external port number r
    mappedport: str
    # Color of icon on the GUI.
    color: int
    # Method used to distribute sessions to real servers.
    ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"]
    # Protocol to be load balanced by the virtual server (also called the server load 
    server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"]
    # Enable/disable redirection of HTTP to HTTPS.
    http_redirect: Literal["enable", "disable"]
    # Configure how to make sure that clients connect to the same server every time th
    persistence: Literal["none", "http-cookie", "ssl-session-id"]
    # Enable/disable HTTP2 support (default = enable).
    h2_support: Literal["enable", "disable"]
    # Enable/disable HTTP3/QUIC support (default = disable).
    h3_support: Literal["enable", "disable"]
    # QUIC setting.
    quic: str
    # Enable/disable DNAT66.
    nat66: Literal["disable", "enable"]
    # Enable/disable DNAT64.
    nat64: Literal["disable", "enable"]
    # Enable/disable adding NAT64 route.
    add_nat64_route: Literal["disable", "enable"]
    # Action for an empty client certificate.
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]
    # Enable/disable detecting device type by HTTP user-agent if no client certificate
    user_agent_detect: Literal["disable", "enable"]
    # Enable/disable requesting client certificate.
    client_cert: Literal["disable", "enable"]
    # Select the real servers that this server load balancing VIP will distribute traf
    realservers: list[str]  # Auto-flattened from member_table
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
    ssl_certificate: list[str]  # Auto-flattened from member_table
    # Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL s
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]
    # Permitted encryption algorithms for SSL sessions according to encryption strengt
    ssl_algorithm: Literal["high", "medium", "low", "custom"]
    # SSL/TLS cipher suites acceptable from a client, ordered by priority.
    ssl_cipher_suites: list[str]  # Auto-flattened from member_table
    # Enable/disable secure renegotiation to comply with RFC 5746.
    ssl_server_renegotiation: Literal["enable", "disable"]
    # Permitted encryption algorithms for the server side of SSL full mode sessions ac
    ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"]
    # SSL/TLS cipher suites to offer to a server, ordered by priority.
    ssl_server_cipher_suites: list[str]  # Auto-flattened from member_table
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
    # Enable/disable sending empty fragments to avoid CBC IV attacks (SSL 3.0 & TLS 1.
    ssl_send_empty_frags: Literal["enable", "disable"]
    # Enable/disable support for preventing Downgrade Attacks on client connections (R
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
    # Number of minutes the web browser should keep HPKP.
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
    monitor: list[str]  # Auto-flattened from member_table
    # Maximum number of incomplete connections.
    max_embryonic_connections: int
    # Enable/disable use of the lower 32 bits of the external IPv6 address as mapped I
    embedded_ipv4_address: Literal["disable", "enable"]
    # Range of mapped IP addresses. Specify the start IP address followed by a space a
    ipv4_mappedip: str
    # IPv4 port number range on the destination network to which the external port num
    ipv4_mappedport: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> Vip6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Vip6:
    """
    Configure virtual IP for IPv6.
    
    Path: firewall/vip6
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> Vip6Object: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
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
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[Vip6Object]: ...
    
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
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
    ) -> dict[str, Any]: ...
    
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
    ) -> Vip6Object | list[Vip6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Vip6Payload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        extip: str | None = ...,
        mappedip: str | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        ndp_reply: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        color: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat66: Literal["disable", "enable"] | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
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
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
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
        embedded_ipv4_address: Literal["disable", "enable"] | None = ...,
        ipv4_mappedip: str | None = ...,
        ipv4_mappedport: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Vip6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: Vip6Payload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        extip: str | None = ...,
        mappedip: str | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        ndp_reply: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        color: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat66: Literal["disable", "enable"] | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
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
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
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
        embedded_ipv4_address: Literal["disable", "enable"] | None = ...,
        ipv4_mappedip: str | None = ...,
        ipv4_mappedport: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: Vip6Payload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        extip: str | None = ...,
        mappedip: str | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        ndp_reply: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        color: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat66: Literal["disable", "enable"] | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
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
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
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
        embedded_ipv4_address: Literal["disable", "enable"] | None = ...,
        ipv4_mappedip: str | None = ...,
        ipv4_mappedport: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: Vip6Payload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        extip: str | None = ...,
        mappedip: str | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        ndp_reply: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        color: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat66: Literal["disable", "enable"] | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
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
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
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
        embedded_ipv4_address: Literal["disable", "enable"] | None = ...,
        ipv4_mappedip: str | None = ...,
        ipv4_mappedport: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Vip6Payload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        extip: str | None = ...,
        mappedip: str | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        ndp_reply: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        color: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat66: Literal["disable", "enable"] | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
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
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
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
        embedded_ipv4_address: Literal["disable", "enable"] | None = ...,
        ipv4_mappedip: str | None = ...,
        ipv4_mappedport: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Vip6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Vip6Payload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        extip: str | None = ...,
        mappedip: str | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        ndp_reply: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        color: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat66: Literal["disable", "enable"] | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
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
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
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
        embedded_ipv4_address: Literal["disable", "enable"] | None = ...,
        ipv4_mappedip: str | None = ...,
        ipv4_mappedport: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: Vip6Payload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        extip: str | None = ...,
        mappedip: str | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        ndp_reply: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        color: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat66: Literal["disable", "enable"] | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
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
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
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
        embedded_ipv4_address: Literal["disable", "enable"] | None = ...,
        ipv4_mappedip: str | None = ...,
        ipv4_mappedport: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: Vip6Payload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        extip: str | None = ...,
        mappedip: str | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        ndp_reply: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        color: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat66: Literal["disable", "enable"] | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
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
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
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
        embedded_ipv4_address: Literal["disable", "enable"] | None = ...,
        ipv4_mappedip: str | None = ...,
        ipv4_mappedport: str | None = ...,
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
    ) -> Vip6Object: ...
    
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
        payload_dict: Vip6Payload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        comment: str | None = ...,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = ...,
        src_filter: str | list[str] | list[dict[str, Any]] | None = ...,
        src_vip_filter: Literal["disable", "enable"] | None = ...,
        extip: str | None = ...,
        mappedip: str | None = ...,
        nat_source_vip: Literal["disable", "enable"] | None = ...,
        ndp_reply: Literal["disable", "enable"] | None = ...,
        portforward: Literal["disable", "enable"] | None = ...,
        protocol: Literal["tcp", "udp", "sctp"] | None = ...,
        extport: str | None = ...,
        mappedport: str | None = ...,
        color: int | None = ...,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = ...,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = ...,
        http_redirect: Literal["enable", "disable"] | None = ...,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = ...,
        h2_support: Literal["enable", "disable"] | None = ...,
        h3_support: Literal["enable", "disable"] | None = ...,
        quic: str | None = ...,
        nat66: Literal["disable", "enable"] | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
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
        ssl_server_renegotiation: Literal["enable", "disable"] | None = ...,
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
        embedded_ipv4_address: Literal["disable", "enable"] | None = ...,
        ipv4_mappedip: str | None = ...,
        ipv4_mappedport: str | None = ...,
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
    "Vip6",
    "Vip6Payload",
    "Vip6Object",
]