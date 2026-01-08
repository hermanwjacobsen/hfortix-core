from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ProbeResponsePayload(TypedDict, total=False):
    """
    Type hints for system/probe_response payload fields.
    
    Configure system probe response.
    
    **Usage:**
        payload: ProbeResponsePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    port: NotRequired[int]  # Port number to response.
    http_probe_value: NotRequired[str]  # Value to respond to the monitoring server.
    ttl_mode: NotRequired[Literal["reinit", "decrease", "retain"]]  # Mode for TWAMP packet TTL modification.
    mode: NotRequired[Literal["none", "http-probe", "twamp"]]  # SLA response mode.
    security_mode: NotRequired[Literal["none", "authentication"]]  # TWAMP responder security mode.
    password: NotRequired[str]  # TWAMP responder password in authentication mode.
    timeout: NotRequired[int]  # An inactivity timer for a twamp test session.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class ProbeResponseResponse(TypedDict):
    """
    Type hints for system/probe_response API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    port: int
    http_probe_value: str
    ttl_mode: Literal["reinit", "decrease", "retain"]
    mode: Literal["none", "http-probe", "twamp"]
    security_mode: Literal["none", "authentication"]
    password: str
    timeout: int


@final
class ProbeResponseObject:
    """Typed FortiObject for system/probe_response with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Port number to response.
    port: int
    # Value to respond to the monitoring server.
    http_probe_value: str
    # Mode for TWAMP packet TTL modification.
    ttl_mode: Literal["reinit", "decrease", "retain"]
    # SLA response mode.
    mode: Literal["none", "http-probe", "twamp"]
    # TWAMP responder security mode.
    security_mode: Literal["none", "authentication"]
    # TWAMP responder password in authentication mode.
    password: str
    # An inactivity timer for a twamp test session.
    timeout: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProbeResponsePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class ProbeResponse:
    """
    Configure system probe response.
    
    Path: system/probe_response
    Category: cmdb
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProbeResponseObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProbeResponseObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProbeResponseObject: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> ProbeResponseResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> ProbeResponseResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> ProbeResponseResponse: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> ProbeResponseObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProbeResponsePayload | None = ...,
        port: int | None = ...,
        http_probe_value: str | None = ...,
        ttl_mode: Literal["reinit", "decrease", "retain"] | None = ...,
        mode: Literal["none", "http-probe", "twamp"] | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProbeResponseObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProbeResponsePayload | None = ...,
        port: int | None = ...,
        http_probe_value: str | None = ...,
        ttl_mode: Literal["reinit", "decrease", "retain"] | None = ...,
        mode: Literal["none", "http-probe", "twamp"] | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ProbeResponsePayload | None = ...,
        port: int | None = ...,
        http_probe_value: str | None = ...,
        ttl_mode: Literal["reinit", "decrease", "retain"] | None = ...,
        mode: Literal["none", "http-probe", "twamp"] | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ProbeResponsePayload | None = ...,
        port: int | None = ...,
        http_probe_value: str | None = ...,
        ttl_mode: Literal["reinit", "decrease", "retain"] | None = ...,
        mode: Literal["none", "http-probe", "twamp"] | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ProbeResponsePayload | None = ...,
        port: int | None = ...,
        http_probe_value: str | None = ...,
        ttl_mode: Literal["reinit", "decrease", "retain"] | None = ...,
        mode: Literal["none", "http-probe", "twamp"] | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        timeout: int | None = ...,
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
    "ProbeResponse",
    "ProbeResponsePayload",
    "ProbeResponseObject",
]