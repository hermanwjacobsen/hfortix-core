from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FastFallbackPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/fast_fallback payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FastFallbackPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Configure a name for the fast-fallback entry.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the fast-fallback entry.
    connection_mode: NotRequired[Literal["sequentially", "simultaneously"]]  # Connection mode for multiple destinations.
    protocol: NotRequired[Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"]]  # Connection protocols for multiple destinations.
    connection_timeout: NotRequired[int]  # Number of milliseconds to wait before starting another conne


class FastFallback:
    """
    Proxy destination connection fast-fallback.
    
    Path: web_proxy/fast_fallback
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
        payload_dict: FastFallbackPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        connection_mode: Literal["sequentially", "simultaneously"] | None = ...,
        protocol: Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"] | None = ...,
        connection_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FastFallbackPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        connection_mode: Literal["sequentially", "simultaneously"] | None = ...,
        protocol: Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"] | None = ...,
        connection_timeout: int | None = ...,
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
        payload_dict: FastFallbackPayload | None = ...,
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