from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class Static6Payload(TypedDict, total=False):
    """
    Type hints for router/static6 payload fields.
    
    Configure IPv6 static routing tables.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address6.Address6Endpoint` (via: dstaddr)
        - :class:`~.firewall.addrgrp6.Addrgrp6Endpoint` (via: dstaddr)
        - :class:`~.system.interface.InterfaceEndpoint` (via: device)

    **Usage:**
        payload: Static6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    seq_num: NotRequired[int]  # Sequence number.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this static route.
    dst: str  # Destination IPv6 prefix.
    gateway: NotRequired[str]  # IPv6 address of the gateway.
    device: str  # Gateway out interface or tunnel.
    devindex: NotRequired[int]  # Device index (0 - 4294967295).
    distance: NotRequired[int]  # Administrative distance (1 - 255).
    weight: NotRequired[int]  # Administrative weight (0 - 255).
    priority: NotRequired[int]  # Administrative priority (1 - 65535).
    comment: NotRequired[str]  # Optional comments.
    blackhole: NotRequired[Literal["enable", "disable"]]  # Enable/disable black hole.
    dynamic_gateway: NotRequired[Literal["enable", "disable"]]  # Enable use of dynamic gateway retrieved from Router Advertis
    sdwan_zone: NotRequired[list[dict[str, Any]]]  # Choose SD-WAN Zone.
    dstaddr: NotRequired[str]  # Name of firewall address or address group.
    link_monitor_exempt: NotRequired[Literal["enable", "disable"]]  # Enable/disable withdrawal of this static route when link mon
    vrf: NotRequired[int]  # Virtual Routing Forwarding ID.
    bfd: NotRequired[Literal["enable", "disable"]]  # Enable/disable Bidirectional Forwarding Detection (BFD).
    tag: NotRequired[int]  # Route tag.


class Static6Object(FortiObject[Static6Payload]):
    """Typed FortiObject for router/static6 with IDE autocomplete support."""
    
    # Sequence number.
    seq_num: int
    # Enable/disable this static route.
    status: Literal["enable", "disable"]
    # Destination IPv6 prefix.
    dst: str
    # IPv6 address of the gateway.
    gateway: str
    # Gateway out interface or tunnel.
    device: str
    # Device index (0 - 4294967295).
    devindex: int
    # Administrative distance (1 - 255).
    distance: int
    # Administrative weight (0 - 255).
    weight: int
    # Administrative priority (1 - 65535).
    priority: int
    # Optional comments.
    comment: str
    # Enable/disable black hole.
    blackhole: Literal["enable", "disable"]
    # Enable use of dynamic gateway retrieved from Router Advertisement (RA).
    dynamic_gateway: Literal["enable", "disable"]
    # Choose SD-WAN Zone.
    sdwan_zone: list[str]  # Auto-flattened from member_table
    # Name of firewall address or address group.
    dstaddr: str
    # Enable/disable withdrawal of this static route when link monitor or health check
    link_monitor_exempt: Literal["enable", "disable"]
    # Virtual Routing Forwarding ID.
    vrf: int
    # Enable/disable Bidirectional Forwarding Detection (BFD).
    bfd: Literal["enable", "disable"]
    # Route tag.
    tag: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> Static6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Static6:
    """
    Configure IPv6 static routing tables.
    
    Path: router/static6
    Category: cmdb
    Primary Key: seq-num
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> Static6Object: ...
    
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
    ) -> list[Static6Object]: ...
    
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        seq_num: None = None,
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
    ) -> Static6Object | list[Static6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Static6Payload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        gateway: str | None = ...,
        device: str | None = ...,
        devindex: int | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Static6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: Static6Payload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        gateway: str | None = ...,
        device: str | None = ...,
        devindex: int | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: Static6Payload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        gateway: str | None = ...,
        device: str | None = ...,
        devindex: int | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: Static6Payload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        gateway: str | None = ...,
        device: str | None = ...,
        devindex: int | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Static6Payload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        gateway: str | None = ...,
        device: str | None = ...,
        devindex: int | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Static6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Static6Payload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        gateway: str | None = ...,
        device: str | None = ...,
        devindex: int | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: Static6Payload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        gateway: str | None = ...,
        device: str | None = ...,
        devindex: int | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: Static6Payload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        gateway: str | None = ...,
        device: str | None = ...,
        devindex: int | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
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
    ) -> Static6Object: ...
    
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
        payload_dict: Static6Payload | None = ...,
        seq_num: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        dst: str | None = ...,
        gateway: str | None = ...,
        device: str | None = ...,
        devindex: int | None = ...,
        distance: int | None = ...,
        weight: int | None = ...,
        priority: int | None = ...,
        comment: str | None = ...,
        blackhole: Literal["enable", "disable"] | None = ...,
        dynamic_gateway: Literal["enable", "disable"] | None = ...,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
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
    "Static6",
    "Static6Payload",
    "Static6Object",
]