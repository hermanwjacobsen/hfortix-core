from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class QosQueuePolicyPayload(TypedDict, total=False):
    """
    Type hints for switch-controller/qos_queue_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: QosQueuePolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # QoS policy name.
    schedule: Literal["strict", "round-robin", "weighted"]  # COS queue scheduling.
    rate_by: Literal["kbps", "percent"]  # COS queue rate by kbps or percent.
    cos_queue: NotRequired[list[dict[str, Any]]]  # COS queue configuration.


class QosQueuePolicy:
    """
    Configure FortiSwitch QoS egress queue policy.
    
    Path: switch-controller/qos_queue_policy
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
        payload_dict: QosQueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal["strict", "round-robin", "weighted"] | None = ...,
        rate_by: Literal["kbps", "percent"] | None = ...,
        cos_queue: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: QosQueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal["strict", "round-robin", "weighted"] | None = ...,
        rate_by: Literal["kbps", "percent"] | None = ...,
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
        payload_dict: QosQueuePolicyPayload | None = ...,
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