from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class DdnsPayload(TypedDict, total=False):
    """
    Type hints for system/ddns payload fields.
    
    Configure DDNS.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: ssl-certificate)

    **Usage:**
        payload: DdnsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ddnsid: NotRequired[int]  # DDNS ID.
    ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"]  # Select a DDNS service provider.
    addr_type: NotRequired[Literal["ipv4", "ipv6"]]  # Address type of interface address in DDNS update.
    server_type: NotRequired[Literal["ipv4", "ipv6"]]  # Address type of the DDNS server.
    ddns_server_addr: NotRequired[list[dict[str, Any]]]  # Generic DDNS server IP/FQDN list.
    ddns_zone: NotRequired[str]  # Zone of your domain name (for example, DDNS.com).
    ddns_ttl: NotRequired[int]  # Time-to-live for DDNS packets.
    ddns_auth: NotRequired[Literal["disable", "tsig"]]  # Enable/disable TSIG authentication for your DDNS server.
    ddns_keyname: NotRequired[str]  # DDNS update key name.
    ddns_key: NotRequired[str]  # DDNS update key (base 64 encoding).
    ddns_domain: NotRequired[str]  # Your fully qualified domain name. For example, yourname.ddns
    ddns_username: NotRequired[str]  # DDNS user name.
    ddns_sn: NotRequired[str]  # DDNS Serial Number.
    ddns_password: NotRequired[str]  # DDNS password.
    use_public_ip: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of public IP address.
    update_interval: NotRequired[int]  # DDNS update interval (60 - 2592000 sec, 0 means default).
    clear_text: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of clear text connections.
    ssl_certificate: NotRequired[str]  # Name of local certificate for SSL connections.
    bound_ip: NotRequired[str]  # Bound IP address.
    monitor_interface: list[dict[str, Any]]  # Monitored interface.

# Nested classes for table field children

@final
class DdnsDdnsserveraddrObject:
    """Typed object for ddns-server-addr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP address or FQDN of the server.
    addr: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class DdnsMonitorinterfaceObject:
    """Typed object for monitor-interface table items.
    
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



# Response TypedDict for GET returns (all fields present in API response)
class DdnsResponse(TypedDict):
    """
    Type hints for system/ddns API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    ddnsid: int
    ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"]
    addr_type: Literal["ipv4", "ipv6"]
    server_type: Literal["ipv4", "ipv6"]
    ddns_server_addr: list[dict[str, Any]]
    ddns_zone: str
    ddns_ttl: int
    ddns_auth: Literal["disable", "tsig"]
    ddns_keyname: str
    ddns_key: str
    ddns_domain: str
    ddns_username: str
    ddns_sn: str
    ddns_password: str
    use_public_ip: Literal["disable", "enable"]
    update_interval: int
    clear_text: Literal["disable", "enable"]
    ssl_certificate: str
    bound_ip: str
    monitor_interface: list[dict[str, Any]]


@final
class DdnsObject:
    """Typed FortiObject for system/ddns with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # DDNS ID.
    ddnsid: int
    # Select a DDNS service provider.
    ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"]
    # Address type of interface address in DDNS update.
    addr_type: Literal["ipv4", "ipv6"]
    # Address type of the DDNS server.
    server_type: Literal["ipv4", "ipv6"]
    # Generic DDNS server IP/FQDN list.
    ddns_server_addr: list[DdnsDdnsserveraddrObject]  # Table field - list of typed objects
    # Zone of your domain name (for example, DDNS.com).
    ddns_zone: str
    # Time-to-live for DDNS packets.
    ddns_ttl: int
    # Enable/disable TSIG authentication for your DDNS server.
    ddns_auth: Literal["disable", "tsig"]
    # DDNS update key name.
    ddns_keyname: str
    # DDNS update key (base 64 encoding).
    ddns_key: str
    # Your fully qualified domain name. For example, yourname.ddns.com.
    ddns_domain: str
    # DDNS user name.
    ddns_username: str
    # DDNS Serial Number.
    ddns_sn: str
    # DDNS password.
    ddns_password: str
    # Enable/disable use of public IP address.
    use_public_ip: Literal["disable", "enable"]
    # DDNS update interval (60 - 2592000 sec, 0 means default).
    update_interval: int
    # Enable/disable use of clear text connections.
    clear_text: Literal["disable", "enable"]
    # Name of local certificate for SSL connections.
    ssl_certificate: str
    # Bound IP address.
    bound_ip: str
    # Monitored interface.
    monitor_interface: list[DdnsMonitorinterfaceObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> DdnsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Ddns:
    """
    Configure DDNS.
    
    Path: system/ddns
    Category: cmdb
    Primary Key: ddnsid
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        ddnsid: int,
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
    ) -> DdnsObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        ddnsid: int,
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
    ) -> DdnsObject: ...
    
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
    ) -> list[DdnsObject]: ...
    
    @overload
    def get(
        self,
        ddnsid: int | None = ...,
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
        ddnsid: int,
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
    ) -> DdnsResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        ddnsid: int,
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
    ) -> DdnsResponse: ...
    
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
    ) -> list[DdnsResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        ddnsid: int | None = ...,
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
        ddnsid: int | None = ...,
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
    ) -> DdnsObject | list[DdnsObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DdnsPayload | None = ...,
        ddnsid: int | None = ...,
        ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"] | None = ...,
        addr_type: Literal["ipv4", "ipv6"] | None = ...,
        server_type: Literal["ipv4", "ipv6"] | None = ...,
        ddns_server_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        ddns_zone: str | None = ...,
        ddns_ttl: int | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_domain: str | None = ...,
        ddns_username: str | None = ...,
        ddns_sn: str | None = ...,
        ddns_password: str | None = ...,
        use_public_ip: Literal["disable", "enable"] | None = ...,
        update_interval: int | None = ...,
        clear_text: Literal["disable", "enable"] | None = ...,
        ssl_certificate: str | None = ...,
        bound_ip: str | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DdnsObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DdnsPayload | None = ...,
        ddnsid: int | None = ...,
        ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"] | None = ...,
        addr_type: Literal["ipv4", "ipv6"] | None = ...,
        server_type: Literal["ipv4", "ipv6"] | None = ...,
        ddns_server_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        ddns_zone: str | None = ...,
        ddns_ttl: int | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_domain: str | None = ...,
        ddns_username: str | None = ...,
        ddns_sn: str | None = ...,
        ddns_password: str | None = ...,
        use_public_ip: Literal["disable", "enable"] | None = ...,
        update_interval: int | None = ...,
        clear_text: Literal["disable", "enable"] | None = ...,
        ssl_certificate: str | None = ...,
        bound_ip: str | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: DdnsPayload | None = ...,
        ddnsid: int | None = ...,
        ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"] | None = ...,
        addr_type: Literal["ipv4", "ipv6"] | None = ...,
        server_type: Literal["ipv4", "ipv6"] | None = ...,
        ddns_server_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        ddns_zone: str | None = ...,
        ddns_ttl: int | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_domain: str | None = ...,
        ddns_username: str | None = ...,
        ddns_sn: str | None = ...,
        ddns_password: str | None = ...,
        use_public_ip: Literal["disable", "enable"] | None = ...,
        update_interval: int | None = ...,
        clear_text: Literal["disable", "enable"] | None = ...,
        ssl_certificate: str | None = ...,
        bound_ip: str | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: DdnsPayload | None = ...,
        ddnsid: int | None = ...,
        ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"] | None = ...,
        addr_type: Literal["ipv4", "ipv6"] | None = ...,
        server_type: Literal["ipv4", "ipv6"] | None = ...,
        ddns_server_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        ddns_zone: str | None = ...,
        ddns_ttl: int | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_domain: str | None = ...,
        ddns_username: str | None = ...,
        ddns_sn: str | None = ...,
        ddns_password: str | None = ...,
        use_public_ip: Literal["disable", "enable"] | None = ...,
        update_interval: int | None = ...,
        clear_text: Literal["disable", "enable"] | None = ...,
        ssl_certificate: str | None = ...,
        bound_ip: str | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DdnsPayload | None = ...,
        ddnsid: int | None = ...,
        ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"] | None = ...,
        addr_type: Literal["ipv4", "ipv6"] | None = ...,
        server_type: Literal["ipv4", "ipv6"] | None = ...,
        ddns_server_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        ddns_zone: str | None = ...,
        ddns_ttl: int | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_domain: str | None = ...,
        ddns_username: str | None = ...,
        ddns_sn: str | None = ...,
        ddns_password: str | None = ...,
        use_public_ip: Literal["disable", "enable"] | None = ...,
        update_interval: int | None = ...,
        clear_text: Literal["disable", "enable"] | None = ...,
        ssl_certificate: str | None = ...,
        bound_ip: str | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DdnsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DdnsPayload | None = ...,
        ddnsid: int | None = ...,
        ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"] | None = ...,
        addr_type: Literal["ipv4", "ipv6"] | None = ...,
        server_type: Literal["ipv4", "ipv6"] | None = ...,
        ddns_server_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        ddns_zone: str | None = ...,
        ddns_ttl: int | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_domain: str | None = ...,
        ddns_username: str | None = ...,
        ddns_sn: str | None = ...,
        ddns_password: str | None = ...,
        use_public_ip: Literal["disable", "enable"] | None = ...,
        update_interval: int | None = ...,
        clear_text: Literal["disable", "enable"] | None = ...,
        ssl_certificate: str | None = ...,
        bound_ip: str | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: DdnsPayload | None = ...,
        ddnsid: int | None = ...,
        ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"] | None = ...,
        addr_type: Literal["ipv4", "ipv6"] | None = ...,
        server_type: Literal["ipv4", "ipv6"] | None = ...,
        ddns_server_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        ddns_zone: str | None = ...,
        ddns_ttl: int | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_domain: str | None = ...,
        ddns_username: str | None = ...,
        ddns_sn: str | None = ...,
        ddns_password: str | None = ...,
        use_public_ip: Literal["disable", "enable"] | None = ...,
        update_interval: int | None = ...,
        clear_text: Literal["disable", "enable"] | None = ...,
        ssl_certificate: str | None = ...,
        bound_ip: str | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: DdnsPayload | None = ...,
        ddnsid: int | None = ...,
        ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"] | None = ...,
        addr_type: Literal["ipv4", "ipv6"] | None = ...,
        server_type: Literal["ipv4", "ipv6"] | None = ...,
        ddns_server_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        ddns_zone: str | None = ...,
        ddns_ttl: int | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_domain: str | None = ...,
        ddns_username: str | None = ...,
        ddns_sn: str | None = ...,
        ddns_password: str | None = ...,
        use_public_ip: Literal["disable", "enable"] | None = ...,
        update_interval: int | None = ...,
        clear_text: Literal["disable", "enable"] | None = ...,
        ssl_certificate: str | None = ...,
        bound_ip: str | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        ddnsid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DdnsObject: ...
    
    @overload
    def delete(
        self,
        ddnsid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        ddnsid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        ddnsid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        ddnsid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: DdnsPayload | None = ...,
        ddnsid: int | None = ...,
        ddns_server: Literal["dyndns.org", "dyns.net", "tzo.com", "vavic.com", "dipdns.net", "now.net.cn", "dhs.org", "easydns.com", "genericDDNS", "FortiGuardDDNS", "noip.com"] | None = ...,
        addr_type: Literal["ipv4", "ipv6"] | None = ...,
        server_type: Literal["ipv4", "ipv6"] | None = ...,
        ddns_server_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        ddns_zone: str | None = ...,
        ddns_ttl: int | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_domain: str | None = ...,
        ddns_username: str | None = ...,
        ddns_sn: str | None = ...,
        ddns_password: str | None = ...,
        use_public_ip: Literal["disable", "enable"] | None = ...,
        update_interval: int | None = ...,
        clear_text: Literal["disable", "enable"] | None = ...,
        ssl_certificate: str | None = ...,
        bound_ip: str | None = ...,
        monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Ddns",
    "DdnsPayload",
    "DdnsObject",
]