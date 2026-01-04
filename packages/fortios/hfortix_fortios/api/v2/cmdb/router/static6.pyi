from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Static6Payload(TypedDict, total=False):
    """
    Type hints for router/static6 payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Static6:
    """
    Configure IPv6 static routing tables.
    
    Path: router/static6
    Category: cmdb
    Primary Key: seq-num
    """
    
    def get(
        self,
        seq_num: int | None = ...,
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
        sdwan_zone: list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        sdwan_zone: list[dict[str, Any]] | None = ...,
        dstaddr: str | None = ...,
        link_monitor_exempt: Literal["enable", "disable"] | None = ...,
        vrf: int | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        tag: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        seq_num: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: Static6Payload | None = ...,
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