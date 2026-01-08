from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class NetflowPayload(TypedDict, total=False):
    """
    Type hints for system/netflow payload fields.
    
    Configure NetFlow.
    
    **Usage:**
        payload: NetflowPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    active_flow_timeout: NotRequired[int]  # Timeout to report active flows (60 - 3600 sec, default = 180
    inactive_flow_timeout: NotRequired[int]  # Timeout for periodic report of finished flows (10 - 600 sec,
    template_tx_timeout: NotRequired[int]  # Timeout for periodic template flowset transmission (60 - 864
    template_tx_counter: NotRequired[int]  # Counter of flowset records before resending a template flows
    session_cache_size: NotRequired[Literal["min", "default", "max"]]  # Maximum RAM usage allowed for Netflow session cache.
    exclusion_filters: NotRequired[list[dict[str, Any]]]  # Exclusion filters
    collectors: NotRequired[list[dict[str, Any]]]  # Netflow collectors.


class NetflowObject(FortiObject[NetflowPayload]):
    """Typed FortiObject for system/netflow with IDE autocomplete support."""
    
    # Timeout to report active flows (60 - 3600 sec, default = 1800).
    active_flow_timeout: int
    # Timeout for periodic report of finished flows (10 - 600 sec, default = 15).
    inactive_flow_timeout: int
    # Timeout for periodic template flowset transmission (60 - 86400 sec, default = 18
    template_tx_timeout: int
    # Counter of flowset records before resending a template flowset record.
    template_tx_counter: int
    # Maximum RAM usage allowed for Netflow session cache.
    session_cache_size: Literal["min", "default", "max"]
    # Exclusion filters
    exclusion_filters: list[str]  # Auto-flattened from member_table
    # Netflow collectors.
    collectors: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> NetflowPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Netflow:
    """
    Configure NetFlow.
    
    Path: system/netflow
    Category: cmdb
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> NetflowObject: ...
    
    @overload
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Netflow",
    "NetflowPayload",
    "NetflowObject",
]