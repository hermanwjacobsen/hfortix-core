from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SnmpPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/snmp payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SnmpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    engine_id: NotRequired[str]  # AC SNMP engineID string (maximum 24 characters).
    contact_info: NotRequired[str]  # Contact Information.
    trap_high_cpu_threshold: NotRequired[int]  # CPU usage when trap is sent.
    trap_high_mem_threshold: NotRequired[int]  # Memory usage when trap is sent.
    community: NotRequired[list[dict[str, Any]]]  # SNMP Community Configuration.
    user: NotRequired[list[dict[str, Any]]]  # SNMP User Configuration.


class Snmp:
    """
    Configure SNMP.
    
    Path: wireless_controller/snmp
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
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: list[dict[str, Any]] | None = ...,
        user: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: list[dict[str, Any]] | None = ...,
        user: list[dict[str, Any]] | None = ...,
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
        payload_dict: SnmpPayload | None = ...,
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
    "Snmp",
    "SnmpPayload",
]