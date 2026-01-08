from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class AccessProxy6Payload(TypedDict, total=False):
    """
    Type hints for firewall/access_proxy6 payload fields.
    
    Configure IPv6 access proxy.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.access-proxy-virtual-host.AccessProxyVirtualHostEndpoint` (via: auth-virtual-host)
        - :class:`~.firewall.decrypted-traffic-mirror.DecryptedTrafficMirrorEndpoint` (via: decrypted-traffic-mirror)
        - :class:`~.firewall.vip6.Vip6Endpoint` (via: vip)

    **Usage:**
        payload: AccessProxy6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Access Proxy name.
    vip: str  # Virtual IP name.
    auth_portal: NotRequired[Literal["disable", "enable"]]  # Enable/disable authentication portal.
    auth_virtual_host: NotRequired[str]  # Virtual host for authentication portal.
    log_blocked_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging of blocked traffic.
    add_vhost_domain_to_dnsdb: NotRequired[Literal["enable", "disable"]]  # Enable/disable adding vhost/domain to dnsdb for ztna dox tun
    svr_pool_multiplex: NotRequired[Literal["enable", "disable"]]  # Enable/disable server pool multiplexing (default = disable).
    svr_pool_ttl: NotRequired[int]  # Time-to-live in the server pool for idle connections to serv
    svr_pool_server_max_request: NotRequired[int]  # Maximum number of requests that servers in server pool handl
    svr_pool_server_max_concurrent_request: NotRequired[int]  # Maximum number of concurrent requests that servers in server
    decrypted_traffic_mirror: NotRequired[str]  # Decrypted traffic mirror.
    api_gateway: NotRequired[list[dict[str, Any]]]  # Set IPv4 API Gateway.
    api_gateway6: NotRequired[list[dict[str, Any]]]  # Set IPv6 API Gateway.

# Nested classes for table field children

@final
class AccessProxy6ApigatewayObject:
    """Typed object for api-gateway table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # API Gateway ID.
    id: int
    # URL pattern to match.
    url_map: str
    # Service.
    service: Literal["http", "https", "tcp-forwarding", "samlsp", "web-portal", "saas"]
    # Method used to distribute sessions to real servers.
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]
    # Virtual host.
    virtual_host: str
    # Type of url-map.
    url_map_type: Literal["sub-string", "wildcard", "regex"]
    # HTTP2 support, default=Enable.
    h2_support: Literal["enable", "disable"]
    # HTTP3/QUIC support, default=Disable.
    h3_support: Literal["enable", "disable"]
    # QUIC setting.
    quic: str
    # Select the real servers that this Access Proxy will distribute traffic to.
    realservers: str
    # SaaS application controlled by this Access Proxy.
    application: str
    # Configure how to make sure that clients connect to the same server every time th
    persistence: Literal["none", "http-cookie"]
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
    # Control sharing of cookies across API Gateway. Use of same-ip means a cookie fro
    http_cookie_share: Literal["disable", "same-ip"]
    # Enable/disable verification that inserted HTTPS cookies are secure.
    https_cookie_secure: Literal["disable", "enable"]
    # SAML service provider configuration for VIP authentication.
    saml_server: str
    # Enable/disable SAML redirection after successful authentication.
    saml_redirect: Literal["disable", "enable"]
    # Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL s
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]
    # Permitted encryption algorithms for the server side of SSL full mode sessions ac
    ssl_algorithm: Literal["high", "medium", "low"]
    # SSL/TLS cipher suites to offer to a server, ordered by priority.
    ssl_cipher_suites: str
    # Lowest SSL/TLS version acceptable from a server.
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Highest SSL/TLS version acceptable from a server.
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Enable/disable secure renegotiation to comply with RFC 5746.
    ssl_renegotiation: Literal["enable", "disable"]
    # Agentless VPN web portal.
    ssl_vpn_web_portal: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AccessProxy6Apigateway6Object:
    """Typed object for api-gateway6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # API Gateway ID.
    id: int
    # URL pattern to match.
    url_map: str
    # Service.
    service: Literal["http", "https", "tcp-forwarding", "samlsp", "web-portal", "saas"]
    # Method used to distribute sessions to real servers.
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]
    # Virtual host.
    virtual_host: str
    # Type of url-map.
    url_map_type: Literal["sub-string", "wildcard", "regex"]
    # HTTP2 support, default=Enable.
    h2_support: Literal["enable", "disable"]
    # HTTP3/QUIC support, default=Disable.
    h3_support: Literal["enable", "disable"]
    # QUIC setting.
    quic: str
    # Select the real servers that this Access Proxy will distribute traffic to.
    realservers: str
    # SaaS application controlled by this Access Proxy.
    application: str
    # Configure how to make sure that clients connect to the same server every time th
    persistence: Literal["none", "http-cookie"]
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
    # Control sharing of cookies across API Gateway. Use of same-ip means a cookie fro
    http_cookie_share: Literal["disable", "same-ip"]
    # Enable/disable verification that inserted HTTPS cookies are secure.
    https_cookie_secure: Literal["disable", "enable"]
    # SAML service provider configuration for VIP authentication.
    saml_server: str
    # Enable/disable SAML redirection after successful authentication.
    saml_redirect: Literal["disable", "enable"]
    # Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL s
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]
    # Permitted encryption algorithms for the server side of SSL full mode sessions ac
    ssl_algorithm: Literal["high", "medium", "low"]
    # SSL/TLS cipher suites to offer to a server, ordered by priority.
    ssl_cipher_suites: str
    # Lowest SSL/TLS version acceptable from a server.
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Highest SSL/TLS version acceptable from a server.
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Enable/disable secure renegotiation to comply with RFC 5746.
    ssl_renegotiation: Literal["enable", "disable"]
    # Agentless VPN web portal.
    ssl_vpn_web_portal: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class AccessProxy6Response(TypedDict):
    """
    Type hints for firewall/access_proxy6 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    vip: str
    auth_portal: Literal["disable", "enable"]
    auth_virtual_host: str
    log_blocked_traffic: Literal["enable", "disable"]
    add_vhost_domain_to_dnsdb: Literal["enable", "disable"]
    svr_pool_multiplex: Literal["enable", "disable"]
    svr_pool_ttl: int
    svr_pool_server_max_request: int
    svr_pool_server_max_concurrent_request: int
    decrypted_traffic_mirror: str
    api_gateway: list[dict[str, Any]]
    api_gateway6: list[dict[str, Any]]


@final
class AccessProxy6Object:
    """Typed FortiObject for firewall/access_proxy6 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Access Proxy name.
    name: str
    # Virtual IP name.
    vip: str
    # Enable/disable authentication portal.
    auth_portal: Literal["disable", "enable"]
    # Virtual host for authentication portal.
    auth_virtual_host: str
    # Enable/disable logging of blocked traffic.
    log_blocked_traffic: Literal["enable", "disable"]
    # Enable/disable adding vhost/domain to dnsdb for ztna dox tunnel.
    add_vhost_domain_to_dnsdb: Literal["enable", "disable"]
    # Enable/disable server pool multiplexing (default = disable). Share connected ser
    svr_pool_multiplex: Literal["enable", "disable"]
    # Time-to-live in the server pool for idle connections to servers.
    svr_pool_ttl: int
    # Maximum number of requests that servers in server pool handle before disconnecti
    svr_pool_server_max_request: int
    # Maximum number of concurrent requests that servers in server pool could handle
    svr_pool_server_max_concurrent_request: int
    # Decrypted traffic mirror.
    decrypted_traffic_mirror: str
    # Set IPv4 API Gateway.
    api_gateway: list[AccessProxy6ApigatewayObject]  # Table field - list of typed objects
    # Set IPv6 API Gateway.
    api_gateway6: list[AccessProxy6Apigateway6Object]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AccessProxy6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class AccessProxy6:
    """
    Configure IPv6 access proxy.
    
    Path: firewall/access_proxy6
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
    ) -> AccessProxy6Object: ...
    
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
    ) -> AccessProxy6Object: ...
    
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
    ) -> list[AccessProxy6Object]: ...
    
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
    ) -> AccessProxy6Response: ...
    
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
    ) -> AccessProxy6Response: ...
    
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
    ) -> list[AccessProxy6Response]: ...
    
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
    ) -> AccessProxy6Object | list[AccessProxy6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccessProxy6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccessProxy6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> AccessProxy6Object: ...
    
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
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "AccessProxy6",
    "AccessProxy6Payload",
    "AccessProxy6Object",
]