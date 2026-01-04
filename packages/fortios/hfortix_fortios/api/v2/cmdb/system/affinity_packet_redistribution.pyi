from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AffinityPacketRedistributionPayload(TypedDict, total=False):
    """
    Type hints for system/affinity_packet_redistribution payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AffinityPacketRedistributionPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID of the packet redistribution setting.
    interface: str  # Physical interface name on which to perform packet redistrib
    rxqid: int  # ID of the receive queue (when the interface has multiple que
    round_robin: Literal["enable", "disable"]  # Enable/disable round-robin redistribution to multiple CPUs.
    affinity_cpumask: NotRequired[str]  # Hexadecimal cpumask, empty value means all CPUs.


class AffinityPacketRedistribution:
    """
    Configure packet redistribution.
    
    Path: system/affinity_packet_redistribution
    Category: cmdb
    Primary Key: id
    """
    
    def get(
        self,
        id: int | None = ...,
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
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
        id: int | None = ...,
        interface: str | None = ...,
        rxqid: int | None = ...,
        round_robin: Literal["enable", "disable"] | None = ...,
        affinity_cpumask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
        id: int | None = ...,
        interface: str | None = ...,
        rxqid: int | None = ...,
        round_robin: Literal["enable", "disable"] | None = ...,
        affinity_cpumask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
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