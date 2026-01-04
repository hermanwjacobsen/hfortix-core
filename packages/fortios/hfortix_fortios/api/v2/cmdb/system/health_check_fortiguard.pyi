from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class HealthCheckFortiguardPayload(TypedDict, total=False):
    """
    Type hints for system/health_check_fortiguard payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: HealthCheckFortiguardPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Status check or predefined health-check targets name.
    server: str  # Status check or predefined health-check domain name.
    obsolete: NotRequired[int]  # Indicates whether Health Check service can be used.
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"]  # Protocol name.


class HealthCheckFortiguard:
    """
    SD-WAN status checking or health checking. Identify a server predefine by FortiGuard and determine how SD-WAN verifies that FGT can communicate with it.
    
    Path: system/health_check_fortiguard
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
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
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
        payload_dict: HealthCheckFortiguardPayload | None = ...,
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