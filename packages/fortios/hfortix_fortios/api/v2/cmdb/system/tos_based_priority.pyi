from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class TosBasedPriorityPayload(TypedDict, total=False):
    """
    Type hints for system/tos_based_priority payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: TosBasedPriorityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Item ID.
    tos: NotRequired[int]  # Value of the ToS byte in the IP datagram header (0-15, 8: mi
    priority: NotRequired[Literal[{"description": "Low priority", "help": "Low priority.", "label": "Low", "name": "low"}, {"description": "Medium priority", "help": "Medium priority.", "label": "Medium", "name": "medium"}, {"description": "High priority", "help": "High priority.", "label": "High", "name": "high"}]]  # ToS based priority level to low, medium or high (these prior


class TosBasedPriority:
    """
    Configure Type of Service (ToS) based priority table to set network traffic priorities.
    
    Path: system/tos_based_priority
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
        payload_dict: TosBasedPriorityPayload | None = ...,
        id: int | None = ...,
        tos: int | None = ...,
        priority: Literal[{"description": "Low priority", "help": "Low priority.", "label": "Low", "name": "low"}, {"description": "Medium priority", "help": "Medium priority.", "label": "Medium", "name": "medium"}, {"description": "High priority", "help": "High priority.", "label": "High", "name": "high"}] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: TosBasedPriorityPayload | None = ...,
        id: int | None = ...,
        tos: int | None = ...,
        priority: Literal[{"description": "Low priority", "help": "Low priority.", "label": "Low", "name": "low"}, {"description": "Medium priority", "help": "Medium priority.", "label": "Medium", "name": "medium"}, {"description": "High priority", "help": "High priority.", "label": "High", "name": "high"}] | None = ...,
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
        payload_dict: TosBasedPriorityPayload | None = ...,
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
    "TosBasedPriority",
    "TosBasedPriorityPayload",
]