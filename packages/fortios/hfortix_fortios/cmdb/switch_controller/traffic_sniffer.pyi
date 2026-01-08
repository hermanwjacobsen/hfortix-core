from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class TrafficSnifferPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/traffic_sniffer payload fields.
    
    Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
    
    **Usage:**
        payload: TrafficSnifferPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    mode: NotRequired[Literal["erspan-auto", "rspan", "none"]]  # Configure traffic sniffer mode.
    erspan_ip: NotRequired[str]  # Configure ERSPAN collector IP address.
    target_mac: NotRequired[list[dict[str, Any]]]  # Sniffer MACs to filter.
    target_ip: NotRequired[list[dict[str, Any]]]  # Sniffer IPs to filter.
    target_port: NotRequired[list[dict[str, Any]]]  # Sniffer ports to filter.


class TrafficSnifferObject(FortiObject[TrafficSnifferPayload]):
    """Typed FortiObject for switch_controller/traffic_sniffer with IDE autocomplete support."""
    
    # Configure traffic sniffer mode.
    mode: Literal["erspan-auto", "rspan", "none"]
    # Configure ERSPAN collector IP address.
    erspan_ip: str
    # Sniffer MACs to filter.
    target_mac: list[str]  # Auto-flattened from member_table
    # Sniffer IPs to filter.
    target_ip: list[str]  # Auto-flattened from member_table
    # Sniffer ports to filter.
    target_port: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> TrafficSnifferPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class TrafficSniffer:
    """
    Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
    
    Path: switch_controller/traffic_sniffer
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
    ) -> TrafficSnifferObject: ...
    
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
    ) -> TrafficSnifferObject: ...
    
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
    ) -> TrafficSnifferObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TrafficSnifferObject: ...
    
    @overload
    def put(
        self,
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "TrafficSniffer",
    "TrafficSnifferPayload",
    "TrafficSnifferObject",
]