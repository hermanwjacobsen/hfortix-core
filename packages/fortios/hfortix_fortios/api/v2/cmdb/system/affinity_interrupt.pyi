from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AffinityInterruptPayload(TypedDict, total=False):
    """
    Type hints for system/affinity_interrupt payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AffinityInterruptPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID of the interrupt affinity setting.
    interrupt: str  # Interrupt name.
    affinity_cpumask: str  # Affinity setting (64-bit hexadecimal value in the format of 
    default_affinity_cpumask: NotRequired[str]  # Default affinity setting (64-bit hexadecimal value in the fo


class AffinityInterrupt:
    """
    Configure interrupt affinity.
    
    Path: system/affinity_interrupt
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
        payload_dict: AffinityInterruptPayload | None = ...,
        id: int | None = ...,
        interrupt: str | None = ...,
        affinity_cpumask: str | None = ...,
        default_affinity_cpumask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AffinityInterruptPayload | None = ...,
        id: int | None = ...,
        interrupt: str | None = ...,
        affinity_cpumask: str | None = ...,
        default_affinity_cpumask: str | None = ...,
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
        payload_dict: AffinityInterruptPayload | None = ...,
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
    "AffinityInterrupt",
    "AffinityInterruptPayload",
]