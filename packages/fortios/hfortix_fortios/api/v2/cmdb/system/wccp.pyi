from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class WccpPayload(TypedDict, total=False):
    """
    Type hints for system/wccp payload fields.
    
    Configure WCCP.
    
    **Usage:**
        payload: WccpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    service_id: NotRequired[str]  # Service ID.
    router_id: NotRequired[str]  # IP address known to all cache engines. If all cache engines
    cache_id: NotRequired[str]  # IP address known to all routers. If the addresses are the sa
    group_address: NotRequired[str]  # IP multicast address used by the cache routers. For the Fort
    server_list: NotRequired[list[dict[str, Any]]]  # IP addresses and netmasks for up to four cache servers.
    router_list: NotRequired[list[dict[str, Any]]]  # IP addresses of one or more WCCP routers.
    ports_defined: NotRequired[Literal["source", "destination"]]  # Match method.
    server_type: NotRequired[Literal["forward", "proxy"]]  # Cache server type.
    ports: NotRequired[list[dict[str, Any]]]  # Service ports.
    authentication: NotRequired[Literal["enable", "disable"]]  # Enable/disable MD5 authentication.
    password: NotRequired[str]  # Password for MD5 authentication.
    forward_method: NotRequired[Literal["GRE", "L2", "any"]]  # Method used to forward traffic to the cache servers.
    cache_engine_method: NotRequired[Literal["GRE", "L2"]]  # Method used to forward traffic to the routers or to return t
    service_type: NotRequired[Literal["auto", "standard", "dynamic"]]  # WCCP service type used by the cache server for logical inter
    primary_hash: NotRequired[Literal["src-ip", "dst-ip", "src-port", "dst-port"]]  # Hash method.
    priority: NotRequired[int]  # Service priority.
    protocol: NotRequired[int]  # Service protocol.
    assignment_weight: NotRequired[int]  # Assignment of hash weight/ratio for the WCCP cache engine.
    assignment_bucket_format: NotRequired[Literal["wccp-v2", "cisco-implementation"]]  # Assignment bucket format for the WCCP cache engine.
    return_method: NotRequired[Literal["GRE", "L2", "any"]]  # Method used to decline a redirected packet and return it to
    assignment_method: NotRequired[Literal["HASH", "MASK", "any"]]  # Hash key assignment preference.
    assignment_srcaddr_mask: NotRequired[str]  # Assignment source address mask.
    assignment_dstaddr_mask: NotRequired[str]  # Assignment destination address mask.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class WccpResponse(TypedDict):
    """
    Type hints for system/wccp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    service_id: str
    router_id: str
    cache_id: str
    group_address: str
    server_list: list[dict[str, Any]]
    router_list: list[dict[str, Any]]
    ports_defined: Literal["source", "destination"]
    server_type: Literal["forward", "proxy"]
    ports: list[dict[str, Any]]
    authentication: Literal["enable", "disable"]
    password: str
    forward_method: Literal["GRE", "L2", "any"]
    cache_engine_method: Literal["GRE", "L2"]
    service_type: Literal["auto", "standard", "dynamic"]
    primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"]
    priority: int
    protocol: int
    assignment_weight: int
    assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"]
    return_method: Literal["GRE", "L2", "any"]
    assignment_method: Literal["HASH", "MASK", "any"]
    assignment_srcaddr_mask: str
    assignment_dstaddr_mask: str


@final
class WccpObject:
    """Typed FortiObject for system/wccp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Service ID.
    service_id: str
    # IP address known to all cache engines. If all cache engines connect to the same
    router_id: str
    # IP address known to all routers. If the addresses are the same, use the default
    cache_id: str
    # IP multicast address used by the cache routers. For the FortiGate to ignore mult
    group_address: str
    # IP addresses and netmasks for up to four cache servers.
    server_list: list[dict[str, Any]]  # Multi-value field
    # IP addresses of one or more WCCP routers.
    router_list: list[dict[str, Any]]  # Multi-value field
    # Match method.
    ports_defined: Literal["source", "destination"]
    # Cache server type.
    server_type: Literal["forward", "proxy"]
    # Service ports.
    ports: list[dict[str, Any]]  # Multi-value field
    # Enable/disable MD5 authentication.
    authentication: Literal["enable", "disable"]
    # Password for MD5 authentication.
    password: str
    # Method used to forward traffic to the cache servers.
    forward_method: Literal["GRE", "L2", "any"]
    # Method used to forward traffic to the routers or to return to the cache engine.
    cache_engine_method: Literal["GRE", "L2"]
    # WCCP service type used by the cache server for logical interception and redirect
    service_type: Literal["auto", "standard", "dynamic"]
    # Hash method.
    primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"]
    # Service priority.
    priority: int
    # Service protocol.
    protocol: int
    # Assignment of hash weight/ratio for the WCCP cache engine.
    assignment_weight: int
    # Assignment bucket format for the WCCP cache engine.
    assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"]
    # Method used to decline a redirected packet and return it to the FortiGate unit.
    return_method: Literal["GRE", "L2", "any"]
    # Hash key assignment preference.
    assignment_method: Literal["HASH", "MASK", "any"]
    # Assignment source address mask.
    assignment_srcaddr_mask: str
    # Assignment destination address mask.
    assignment_dstaddr_mask: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> WccpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Wccp:
    """
    Configure WCCP.
    
    Path: system/wccp
    Category: cmdb
    Primary Key: service-id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        service_id: str,
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
    ) -> WccpObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        service_id: str,
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
    ) -> WccpObject: ...
    
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
    ) -> list[WccpObject]: ...
    
    @overload
    def get(
        self,
        service_id: str | None = ...,
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
        service_id: str,
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
    ) -> WccpResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        service_id: str,
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
    ) -> WccpResponse: ...
    
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
    ) -> list[WccpResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        service_id: str | None = ...,
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
        service_id: str | None = ...,
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
    ) -> WccpObject | list[WccpObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WccpObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WccpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        service_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WccpObject: ...
    
    @overload
    def delete(
        self,
        service_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        service_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        service_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        service_id: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
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
    "Wccp",
    "WccpPayload",
    "WccpObject",
]