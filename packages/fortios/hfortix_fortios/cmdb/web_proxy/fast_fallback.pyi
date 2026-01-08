from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class FastFallbackPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/fast_fallback payload fields.
    
    Proxy destination connection fast-fallback.
    
    **Usage:**
        payload: FastFallbackPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Configure a name for the fast-fallback entry.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the fast-fallback entry.
    connection_mode: NotRequired[Literal["sequentially", "simultaneously"]]  # Connection mode for multiple destinations.
    protocol: NotRequired[Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"]]  # Connection protocols for multiple destinations.
    connection_timeout: NotRequired[int]  # Number of milliseconds to wait before starting another conne


class FastFallbackObject(FortiObject[FastFallbackPayload]):
    """Typed FortiObject for web_proxy/fast_fallback with IDE autocomplete support."""
    
    # Configure a name for the fast-fallback entry.
    name: str
    # Enable/disable the fast-fallback entry.
    status: Literal["enable", "disable"]
    # Connection mode for multiple destinations.
    connection_mode: Literal["sequentially", "simultaneously"]
    # Connection protocols for multiple destinations.
    protocol: Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"]
    # Number of milliseconds to wait before starting another connection (200 - 1800000
    connection_timeout: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FastFallbackPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class FastFallback:
    """
    Proxy destination connection fast-fallback.
    
    Path: web_proxy/fast_fallback
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> FastFallbackObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[FastFallbackObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> FastFallbackObject | list[FastFallbackObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: FastFallbackPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        connection_mode: Literal["sequentially", "simultaneously"] | None = ...,
        protocol: Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"] | None = ...,
        connection_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FastFallbackObject: ...
    
    @overload
    def post(
        self,
        payload_dict: FastFallbackPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        connection_mode: Literal["sequentially", "simultaneously"] | None = ...,
        protocol: Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"] | None = ...,
        connection_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: FastFallbackPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        connection_mode: Literal["sequentially", "simultaneously"] | None = ...,
        protocol: Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"] | None = ...,
        connection_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FastFallbackPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        connection_mode: Literal["sequentially", "simultaneously"] | None = ...,
        protocol: Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"] | None = ...,
        connection_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FastFallbackObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FastFallbackPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        connection_mode: Literal["sequentially", "simultaneously"] | None = ...,
        protocol: Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"] | None = ...,
        connection_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: FastFallbackPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        connection_mode: Literal["sequentially", "simultaneously"] | None = ...,
        protocol: Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"] | None = ...,
        connection_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FastFallbackObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FastFallbackPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        connection_mode: Literal["sequentially", "simultaneously"] | None = ...,
        protocol: Literal["IPv4-first", "IPv6-first", "IPv4-only", "IPv6-only"] | None = ...,
        connection_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    "FastFallback",
    "FastFallbackPayload",
    "FastFallbackObject",
]