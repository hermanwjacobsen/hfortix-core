from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class HealthCheckFortiguardPayload(TypedDict, total=False):
    """
    Type hints for system/health_check_fortiguard payload fields.
    
    SD-WAN status checking or health checking. Identify a server predefine by FortiGuard and determine how SD-WAN verifies that FGT can communicate with it.
    
    **Usage:**
        payload: HealthCheckFortiguardPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Status check or predefined health-check targets name.
    server: str  # Status check or predefined health-check domain name.
    obsolete: NotRequired[int]  # Indicates whether Health Check service can be used.
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"]  # Protocol name.


class HealthCheckFortiguardObject(FortiObject[HealthCheckFortiguardPayload]):
    """Typed FortiObject for system/health_check_fortiguard with IDE autocomplete support."""
    
    # Status check or predefined health-check targets name.
    name: str
    # Status check or predefined health-check domain name.
    server: str
    # Indicates whether Health Check service can be used.
    obsolete: int
    # Protocol name.
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> HealthCheckFortiguardPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class HealthCheckFortiguard:
    """
    SD-WAN status checking or health checking. Identify a server predefine by FortiGuard and determine how SD-WAN verifies that FGT can communicate with it.
    
    Path: system/health_check_fortiguard
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
    ) -> HealthCheckFortiguardObject: ...
    
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
    ) -> list[HealthCheckFortiguardObject]: ...
    
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
    ) -> HealthCheckFortiguardObject | list[HealthCheckFortiguardObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> HealthCheckFortiguardObject: ...
    
    @overload
    def post(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> HealthCheckFortiguardObject: ...
    
    @overload
    def put(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
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
    ) -> HealthCheckFortiguardObject: ...
    
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
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
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
    "HealthCheckFortiguard",
    "HealthCheckFortiguardPayload",
    "HealthCheckFortiguardObject",
]