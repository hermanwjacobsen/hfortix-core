from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class MulticastPayload(TypedDict, total=False):
    """
    Type hints for router/multicast payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: MulticastPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    route_threshold: NotRequired[int]  # Generate warnings when the number of multicast routes exceed
    route_limit: NotRequired[int]  # Maximum number of multicast routes.
    multicast_routing: NotRequired[Literal["enable", "disable"]]  # Enable/disable IP multicast routing.
    pim_sm_global: NotRequired[str]  # PIM sparse-mode global settings.
    pim_sm_global_vrf: NotRequired[list[dict[str, Any]]]  # per-VRF PIM sparse-mode global settings.
    interface: NotRequired[list[dict[str, Any]]]  # PIM interfaces.


class Multicast:
    """
    Configure router multicast.
    
    Path: router/multicast
    Category: cmdb
    """
    
    def get(
        self,
        name: str | None = ...,
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
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: list[dict[str, Any]] | None = ...,
        interface: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: list[dict[str, Any]] | None = ...,
        interface: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: MulticastPayload | None = ...,
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