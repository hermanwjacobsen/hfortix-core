from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class QueuePolicyPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/qos/queue_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: QueuePolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # QoS policy name.
    schedule: Literal[{"description": "Strict scheduling (queue7: highest priority, queue0: lowest priority)", "help": "Strict scheduling (queue7: highest priority, queue0: lowest priority).", "label": "Strict", "name": "strict"}, {"description": "Round robin scheduling", "help": "Round robin scheduling.", "label": "Round Robin", "name": "round-robin"}, {"description": "Weighted round robin scheduling", "help": "Weighted round robin scheduling.", "label": "Weighted", "name": "weighted"}]  # COS queue scheduling.
    rate_by: Literal[{"description": "Rate by kbps", "help": "Rate by kbps.", "label": "Kbps", "name": "kbps"}, {"description": "Rate by percent", "help": "Rate by percent.", "label": "Percent", "name": "percent"}]  # COS queue rate by kbps or percent.
    cos_queue: NotRequired[list[dict[str, Any]]]  # COS queue configuration.


class QueuePolicy:
    """
    Configure FortiSwitch QoS egress queue policy.
    
    Path: switch_controller/qos/queue_policy
    Category: cmdb
    Primary Key: name
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
        payload_dict: QueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal[{"description": "Strict scheduling (queue7: highest priority, queue0: lowest priority)", "help": "Strict scheduling (queue7: highest priority, queue0: lowest priority).", "label": "Strict", "name": "strict"}, {"description": "Round robin scheduling", "help": "Round robin scheduling.", "label": "Round Robin", "name": "round-robin"}, {"description": "Weighted round robin scheduling", "help": "Weighted round robin scheduling.", "label": "Weighted", "name": "weighted"}] | None = ...,
        rate_by: Literal[{"description": "Rate by kbps", "help": "Rate by kbps.", "label": "Kbps", "name": "kbps"}, {"description": "Rate by percent", "help": "Rate by percent.", "label": "Percent", "name": "percent"}] | None = ...,
        cos_queue: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: QueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal[{"description": "Strict scheduling (queue7: highest priority, queue0: lowest priority)", "help": "Strict scheduling (queue7: highest priority, queue0: lowest priority).", "label": "Strict", "name": "strict"}, {"description": "Round robin scheduling", "help": "Round robin scheduling.", "label": "Round Robin", "name": "round-robin"}, {"description": "Weighted round robin scheduling", "help": "Weighted round robin scheduling.", "label": "Weighted", "name": "weighted"}] | None = ...,
        rate_by: Literal[{"description": "Rate by kbps", "help": "Rate by kbps.", "label": "Kbps", "name": "kbps"}, {"description": "Rate by percent", "help": "Rate by percent.", "label": "Percent", "name": "percent"}] | None = ...,
        cos_queue: list[dict[str, Any]] | None = ...,
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
        payload_dict: QueuePolicyPayload | None = ...,
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
    "QueuePolicy",
    "QueuePolicyPayload",
]