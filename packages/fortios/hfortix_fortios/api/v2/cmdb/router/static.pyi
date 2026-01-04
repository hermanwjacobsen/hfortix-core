from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class StaticPayload(TypedDict, total=False):
    """
    Type hints for router/static payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Static:
    """
    Configure IPv4 static routing tables.
    
    Path: router/static
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
        sdwan_zone: list[dict[str, Any]] | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        sdwan_zone: list[dict[str, Any]] | None = ...,
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
        payload_dict: StaticPayload | None = ...,
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


__all__ = [
    "Static",
    "StaticPayload",
]