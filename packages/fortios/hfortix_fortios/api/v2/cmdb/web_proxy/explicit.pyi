from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ExplicitPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/explicit payload fields.
    
    Configure explicit Web proxy settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: ExplicitPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the explicit Web proxy for HTTP and HTTPS ses
    secure_web_proxy: NotRequired[Literal["disable", "enable", "secure"]]  # Enable/disable/require the secure web proxy for HTTP and HTT
    ftp_over_http: NotRequired[Literal["enable", "disable"]]  # Enable to proxy FTP-over-HTTP sessions sent from a web brows
    socks: NotRequired[Literal["enable", "disable"]]  # Enable/disable the SOCKS proxy.
    http_incoming_port: NotRequired[str]  # Accept incoming HTTP requests on one or more ports
    http_connection_mode: NotRequired[Literal["static", "multiplex", "serverpool"]]  # HTTP connection mode (default = static).
    https_incoming_port: NotRequired[str]  # Accept incoming HTTPS requests on one or more ports
    secure_web_proxy_cert: NotRequired[list[dict[str, Any]]]  # Name of certificates for secure web proxy.
    client_cert: NotRequired[Literal["disable", "enable"]]  # Enable/disable to request client certificate.
    user_agent_detect: NotRequired[Literal["disable", "enable"]]  # Enable/disable to detect device type by HTTP user-agent if n
    empty_cert_action: NotRequired[Literal["accept", "block", "accept-unmanageable"]]  # Action of an empty client certificate.
    ssl_dh_bits: NotRequired[Literal["768", "1024", "1536", "2048"]]  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    ftp_incoming_port: NotRequired[str]  # Accept incoming FTP-over-HTTP requests on one or more ports
    socks_incoming_port: NotRequired[str]  # Accept incoming SOCKS proxy requests on one or more ports
    incoming_ip: NotRequired[str]  # Restrict the explicit HTTP proxy to only accept sessions fro
    outgoing_ip: NotRequired[list[dict[str, Any]]]  # Outgoing HTTP requests will have this IP address as their so
    interface_select_method: NotRequired[Literal["sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    ipv6_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowing an IPv6 web proxy destination in pol
    incoming_ip6: NotRequired[str]  # Restrict the explicit web proxy to only accept sessions from
    outgoing_ip6: NotRequired[list[dict[str, Any]]]  # Outgoing HTTP requests will leave this IPv6. Multiple interf
    strict_guest: NotRequired[Literal["enable", "disable"]]  # Enable/disable strict guest user checking by the explicit we
    pref_dns_result: NotRequired[Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"]]  # Prefer resolving addresses using the configured IPv4 or IPv6
    unknown_http_version: NotRequired[Literal["reject", "best-effort"]]  # How to handle HTTP sessions that do not comply with HTTP 0.9
    realm: str  # Authentication realm used to identify the explicit web proxy
    sec_default_action: NotRequired[Literal["accept", "deny"]]  # Accept or deny explicit web proxy sessions when no web proxy
    https_replacement_message: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending the client a replacement message for
    message_upon_server_error: NotRequired[Literal["enable", "disable"]]  # Enable/disable displaying a replacement message when a serve
    pac_file_server_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable Proxy Auto-Configuration (PAC) for users of t
    pac_file_url: NotRequired[str]  # PAC file access URL.
    pac_file_server_port: NotRequired[str]  # Port number that PAC traffic from client web browsers uses t
    pac_file_through_https: NotRequired[Literal["enable", "disable"]]  # Enable/disable to get Proxy Auto-Configuration (PAC) through
    pac_file_name: str  # Pac file name.
    pac_file_data: NotRequired[str]  # PAC file contents enclosed in quotes (maximum of 256K bytes)
    pac_policy: NotRequired[list[dict[str, Any]]]  # PAC policies.
    ssl_algorithm: NotRequired[Literal["high", "medium", "low"]]  # Relative strength of encryption algorithms accepted in HTTPS
    trace_auth_no_rsp: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging timed-out authentication requests.

# Nested classes for table field children

@final
class ExplicitSecurewebproxycertObject:
    """Typed object for secure-web-proxy-cert table items.
    
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
class ExplicitPacpolicyObject:
    """Typed object for pac-policy table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Policy ID.
    policyid: int
    # Enable/disable policy.
    status: Literal["enable", "disable"]
    # Source address objects.
    srcaddr: str
    # Source address6 objects.
    srcaddr6: str
    # Destination address objects.
    dstaddr: str
    # Pac file name.
    pac_file_name: str
    # PAC file contents enclosed in quotes (maximum of 256K bytes).
    pac_file_data: str
    # Optional comments.
    comments: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class ExplicitResponse(TypedDict):
    """
    Type hints for web_proxy/explicit API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]
    secure_web_proxy: Literal["disable", "enable", "secure"]
    ftp_over_http: Literal["enable", "disable"]
    socks: Literal["enable", "disable"]
    http_incoming_port: str
    http_connection_mode: Literal["static", "multiplex", "serverpool"]
    https_incoming_port: str
    secure_web_proxy_cert: list[dict[str, Any]]
    client_cert: Literal["disable", "enable"]
    user_agent_detect: Literal["disable", "enable"]
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]
    ftp_incoming_port: str
    socks_incoming_port: str
    incoming_ip: str
    outgoing_ip: list[dict[str, Any]]
    interface_select_method: Literal["sdwan", "specify"]
    interface: str
    vrf_select: int
    ipv6_status: Literal["enable", "disable"]
    incoming_ip6: str
    outgoing_ip6: list[dict[str, Any]]
    strict_guest: Literal["enable", "disable"]
    pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"]
    unknown_http_version: Literal["reject", "best-effort"]
    realm: str
    sec_default_action: Literal["accept", "deny"]
    https_replacement_message: Literal["enable", "disable"]
    message_upon_server_error: Literal["enable", "disable"]
    pac_file_server_status: Literal["enable", "disable"]
    pac_file_url: str
    pac_file_server_port: str
    pac_file_through_https: Literal["enable", "disable"]
    pac_file_name: str
    pac_file_data: str
    pac_policy: list[dict[str, Any]]
    ssl_algorithm: Literal["high", "medium", "low"]
    trace_auth_no_rsp: Literal["enable", "disable"]


@final
class ExplicitObject:
    """Typed FortiObject for web_proxy/explicit with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable the explicit Web proxy for HTTP and HTTPS session.
    status: Literal["enable", "disable"]
    # Enable/disable/require the secure web proxy for HTTP and HTTPS session.
    secure_web_proxy: Literal["disable", "enable", "secure"]
    # Enable to proxy FTP-over-HTTP sessions sent from a web browser.
    ftp_over_http: Literal["enable", "disable"]
    # Enable/disable the SOCKS proxy.
    socks: Literal["enable", "disable"]
    # Accept incoming HTTP requests on one or more ports (0 - 65535, default = 8080).
    http_incoming_port: str
    # HTTP connection mode (default = static).
    http_connection_mode: Literal["static", "multiplex", "serverpool"]
    # Accept incoming HTTPS requests on one or more ports
    https_incoming_port: str
    # Name of certificates for secure web proxy.
    secure_web_proxy_cert: list[ExplicitSecurewebproxycertObject]  # Table field - list of typed objects
    # Enable/disable to request client certificate.
    client_cert: Literal["disable", "enable"]
    # Enable/disable to detect device type by HTTP user-agent if no client certificate
    user_agent_detect: Literal["disable", "enable"]
    # Action of an empty client certificate.
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]
    # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]
    # Accept incoming FTP-over-HTTP requests on one or more ports
    ftp_incoming_port: str
    # Accept incoming SOCKS proxy requests on one or more ports
    socks_incoming_port: str
    # Restrict the explicit HTTP proxy to only accept sessions from this IP address. A
    incoming_ip: str
    # Outgoing HTTP requests will have this IP address as their source address. An int
    outgoing_ip: list[dict[str, Any]]  # Multi-value field
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    # Enable/disable allowing an IPv6 web proxy destination in policies and all IPv6 r
    ipv6_status: Literal["enable", "disable"]
    # Restrict the explicit web proxy to only accept sessions from this IPv6 address.
    incoming_ip6: str
    # Outgoing HTTP requests will leave this IPv6. Multiple interfaces can be specifie
    outgoing_ip6: list[dict[str, Any]]  # Multi-value field
    # Enable/disable strict guest user checking by the explicit web proxy.
    strict_guest: Literal["enable", "disable"]
    # Prefer resolving addresses using the configured IPv4 or IPv6 DNS server
    pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"]
    # How to handle HTTP sessions that do not comply with HTTP 0.9, 1.0, or 1.1.
    unknown_http_version: Literal["reject", "best-effort"]
    # Authentication realm used to identify the explicit web proxy
    realm: str
    # Accept or deny explicit web proxy sessions when no web proxy firewall policy exi
    sec_default_action: Literal["accept", "deny"]
    # Enable/disable sending the client a replacement message for HTTPS requests.
    https_replacement_message: Literal["enable", "disable"]
    # Enable/disable displaying a replacement message when a server error is detected.
    message_upon_server_error: Literal["enable", "disable"]
    # Enable/disable Proxy Auto-Configuration (PAC) for users of this explicit proxy p
    pac_file_server_status: Literal["enable", "disable"]
    # PAC file access URL.
    pac_file_url: str
    # Port number that PAC traffic from client web browsers uses to connect to the exp
    pac_file_server_port: str
    # Enable/disable to get Proxy Auto-Configuration (PAC) through HTTPS.
    pac_file_through_https: Literal["enable", "disable"]
    # Pac file name.
    pac_file_name: str
    # PAC file contents enclosed in quotes (maximum of 256K bytes).
    pac_file_data: str
    # PAC policies.
    pac_policy: list[ExplicitPacpolicyObject]  # Table field - list of typed objects
    # Relative strength of encryption algorithms accepted in HTTPS deep scan: high, me
    ssl_algorithm: Literal["high", "medium", "low"]
    # Enable/disable logging timed-out authentication requests.
    trace_auth_no_rsp: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ExplicitPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Explicit:
    """
    Configure explicit Web proxy settings.
    
    Path: web_proxy/explicit
    Category: cmdb
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitResponse: ...
    
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
    ) -> ExplicitResponse: ...
    
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
    ) -> ExplicitResponse: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> ExplicitObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | list[str] | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExplicitObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | list[str] | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | list[str] | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | list[str] | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | list[str] | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
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
    "Explicit",
    "ExplicitPayload",
    "ExplicitObject",
]