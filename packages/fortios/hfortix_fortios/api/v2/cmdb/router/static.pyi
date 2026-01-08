from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class StaticPayload(TypedDict, total=False):
    """
    Type hints for router/static payload fields.
    
    Configure IPv4 static routing tables.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address.AddressEndpoint` (via: dstaddr)
        - :class:`~.firewall.addrgrp.AddrgrpEndpoint` (via: dstaddr)
        - :class:`~.firewall.internet-service.InternetServiceEndpoint` (via: internet-service)
        - :class:`~.firewall.internet-service-custom.InternetServiceCustomEndpoint` (via: internet-service-custom)
        - :class:`~.firewall.internet-service-fortiguard.InternetServiceFortiguardEndpoint` (via: internet-service-fortiguard)
        - :class:`~.system.interface.InterfaceEndpoint` (via: device)

    **Usage:**
        payload: StaticPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    seq_num: NotRequired[int]  # Sequence number.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this static route.
    dst: str  # Destination IP and mask for this route.
    src: NotRequired[str]  # Source prefix for this route.
    gateway: NotRequired[str]  # Gateway IP for this route.
    preferred_source: NotRequired[str]  # Preferred source IP for this route.
    distance: NotRequired[int]  # Administrative distance (1 - 255).
    weight: NotRequired[int]  # Administrative weight (0 - 255).
    priority: NotRequired[int]  # Administrative priority (1 - 65535).
    device: str  # Gateway out interface or tunnel.
    comment: NotRequired[str]  # Optional comments.
    blackhole: NotRequired[Literal["enable", "disable"]]  # Enable/disable black hole.
    dynamic_gateway: NotRequired[Literal["enable", "disable"]]  # Enable use of dynamic gateway retrieved from a DHCP or PPP s
    sdwan_zone: NotRequired[list[dict[str, Any]]]  # Choose SD-WAN Zone.
    dstaddr: NotRequired[str]  # Name of firewall address or address group.
    internet_service: NotRequired[int]  # Application ID in the Internet service database.
    internet_service_custom: NotRequired[str]  # Application name in the Internet service custom database.
    internet_service_fortiguard: NotRequired[str]  # Application name in the Internet service fortiguard database
    link_monitor_exempt: NotRequired[Literal["enable", "disable"]]  # Enable/disable withdrawal of this static route when link mon
    tag: NotRequired[int]  # Route tag.
    vrf: NotRequired[int]  # Virtual Routing Forwarding ID.
    bfd: NotRequired[Literal["enable", "disable"]]  # Enable/disable Bidirectional Forwarding Detection (BFD).

# Nested classes for table field children

@final
class StaticSdwanzoneObject:
    """Typed object for sdwan-zone table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SD-WAN zone name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class StaticResponse(TypedDict):
    """
    Type hints for router/static API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    seq_num: int
    status: Literal["enable", "disable"]
    dst: str
    src: str
    gateway: str
    preferred_source: str
    distance: int
    weight: int
    priority: int
    device: str
    comment: str
    blackhole: Literal["enable", "disable"]
    dynamic_gateway: Literal["enable", "disable"]
    sdwan_zone: list[dict[str, Any]]
    dstaddr: str
    internet_service: int
    internet_service_custom: str
    internet_service_fortiguard: str
    link_monitor_exempt: Literal["enable", "disable"]
    tag: int
    vrf: int
    bfd: Literal["enable", "disable"]


@final
class StaticObject:
    """Typed FortiObject for router/static with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Sequence number.
    seq_num: int
    # Enable/disable this static route.
    status: Literal["enable", "disable"]
    # Destination IP and mask for this route.
    dst: str
    # Source prefix for this route.
    src: str
    # Gateway IP for this route.
    gateway: str
    # Preferred source IP for this route.
    preferred_source: str
    # Administrative distance (1 - 255).
    distance: int
    # Administrative weight (0 - 255).
    weight: int
    # Administrative priority (1 - 65535).
    priority: int
    # Gateway out interface or tunnel.
    device: str
    # Optional comments.
    comment: str
    # Enable/disable black hole.
    blackhole: Literal["enable", "disable"]
    # Enable use of dynamic gateway retrieved from a DHCP or PPP server.
    dynamic_gateway: Literal["enable", "disable"]
    # Choose SD-WAN Zone.
    sdwan_zone: list[StaticSdwanzoneObject]  # Table field - list of typed objects
    # Name of firewall address or address group.
    dstaddr: str
    # Application ID in the Internet service database.
    internet_service: int
    # Application name in the Internet service custom database.
    internet_service_custom: str
    # Application name in the Internet service fortiguard database.
    internet_service_fortiguard: str
    # Enable/disable withdrawal of this static route when link monitor or health check
    link_monitor_exempt: Literal["enable", "disable"]
    # Route tag.
    tag: int
    # Virtual Routing Forwarding ID.
    vrf: int
    # Enable/disable Bidirectional Forwarding Detection (BFD).
    bfd: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> StaticPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Static:
    """
    Configure IPv4 static routing tables.
    
    Path: router/static
    Category: cmdb
    Primary Key: seq-num
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        seq_num: int,
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
    ) -> StaticObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        seq_num: int,
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
    ) -> StaticObject: ...
    
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
    ) -> list[StaticObject]: ...
    
    @overload
    def get(
        self,
        seq_num: int | None = ...,
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
        seq_num: int,
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
    ) -> StaticResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        seq_num: int,
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
    ) -> StaticResponse: ...
    
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
    ) -> list[StaticResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        seq_num: int | None = ...,
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
        seq_num: int | None = ...,
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
    ) -> StaticObject | list[StaticObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> StaticObject: ...
    
    @overload
    def post(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> StaticObject: ...
    
    @overload
    def put(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> StaticObject: ...
    
    @overload
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        seq_num: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: StaticPayload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        src: str | None = ...,
        gateway: str | None = ...,
        preferred_source: str | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        device: str | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        internet_service: int | None = ...,
        internet_service_custom: str | None = ...,
        internet_service_fortiguard: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
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
    "Static",
    "StaticPayload",
    "StaticObject",
]