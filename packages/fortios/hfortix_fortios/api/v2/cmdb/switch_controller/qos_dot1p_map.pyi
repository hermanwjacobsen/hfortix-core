from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class QosDot1pMapPayload(TypedDict, total=False):
    """
    Type hints for switch-controller/qos_dot1p_map payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: QosDot1pMapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Dot1p map name.
    description: NotRequired[str]  # Description of the 802.1p name.
    egress_pri_tagging: Literal["disable", "enable"]  # Enable/disable egress priority-tag frame.
    priority_0: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_1: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_2: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_3: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_4: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_5: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_6: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_7: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.


class QosDot1pMap:
    """
    Configure FortiSwitch QoS 802.1p.
    
    Path: switch-controller/qos_dot1p_map
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
        payload_dict: QosDot1pMapPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        egress_pri_tagging: Literal["disable", "enable"] | None = ...,
        priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: QosDot1pMapPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        egress_pri_tagging: Literal["disable", "enable"] | None = ...,
        priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
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
        payload_dict: QosDot1pMapPayload | None = ...,
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