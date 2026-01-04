from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class RipngPayload(TypedDict, total=False):
    """
    Type hints for router/ripng payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: RipngPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    default_information_originate: NotRequired[Literal["enable", "disable"]]  # Enable/disable generation of default route.
    default_metric: NotRequired[int]  # Default metric.
    max_out_metric: NotRequired[int]  # Maximum metric allowed to output(0 means 'not set').
    distance: NotRequired[list[dict[str, Any]]]  # Distance.
    distribute_list: NotRequired[list[dict[str, Any]]]  # Distribute list.
    neighbor: NotRequired[list[dict[str, Any]]]  # Neighbor.
    network: NotRequired[list[dict[str, Any]]]  # Network.
    aggregate_address: NotRequired[list[dict[str, Any]]]  # Aggregate address.
    offset_list: NotRequired[list[dict[str, Any]]]  # Offset list.
    passive_interface: NotRequired[list[dict[str, Any]]]  # Passive interface configuration.
    redistribute: NotRequired[list[dict[str, Any]]]  # Redistribute configuration.
    update_timer: NotRequired[int]  # Update timer in seconds.
    timeout_timer: NotRequired[int]  # Timeout timer in seconds.
    garbage_timer: NotRequired[int]  # Garbage timer in seconds.
    interface: NotRequired[list[dict[str, Any]]]  # RIPng interface configuration.


class Ripng:
    """
    Configure RIPng.
    
    Path: router/ripng
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
        payload_dict: RipngPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: list[dict[str, Any]] | None = ...,
        distribute_list: list[dict[str, Any]] | None = ...,
        neighbor: list[dict[str, Any]] | None = ...,
        network: list[dict[str, Any]] | None = ...,
        aggregate_address: list[dict[str, Any]] | None = ...,
        offset_list: list[dict[str, Any]] | None = ...,
        passive_interface: list[dict[str, Any]] | None = ...,
        redistribute: list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        interface: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: RipngPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: list[dict[str, Any]] | None = ...,
        distribute_list: list[dict[str, Any]] | None = ...,
        neighbor: list[dict[str, Any]] | None = ...,
        network: list[dict[str, Any]] | None = ...,
        aggregate_address: list[dict[str, Any]] | None = ...,
        offset_list: list[dict[str, Any]] | None = ...,
        passive_interface: list[dict[str, Any]] | None = ...,
        redistribute: list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
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
        payload_dict: RipngPayload | None = ...,
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