from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class FilterPayload(TypedDict, total=False):
    """
    Type hints for log/null_device/filter payload fields.
    
    Filters for null device logging.
    
    **Usage:**
        payload: FilterPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    severity: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log.
    forward_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable forward traffic logging.
    local_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable local in or out traffic logging.
    multicast_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable multicast traffic logging.
    sniffer_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable sniffer traffic logging.
    ztna_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable ztna traffic logging.
    http_transaction: NotRequired[Literal["enable", "disable"]]  # Enable/disable log HTTP transaction messages.
    anomaly: NotRequired[Literal["enable", "disable"]]  # Enable/disable anomaly logging.
    voip: NotRequired[Literal["enable", "disable"]]  # Enable/disable VoIP logging.
    gtp: NotRequired[Literal["enable", "disable"]]  # Enable/disable GTP messages logging.
    forti_switch: NotRequired[Literal["enable", "disable"]]  # Enable/disable Forti-Switch logging.
    debug: NotRequired[Literal["enable", "disable"]]  # Enable/disable debug logging.
    free_style: NotRequired[list[dict[str, Any]]]  # Free style filters.


class FilterObject(FortiObject[FilterPayload]):
    """Typed FortiObject for log/null_device/filter with IDE autocomplete support."""
    
    # Lowest severity level to log.
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Enable/disable forward traffic logging.
    forward_traffic: Literal["enable", "disable"]
    # Enable/disable local in or out traffic logging.
    local_traffic: Literal["enable", "disable"]
    # Enable/disable multicast traffic logging.
    multicast_traffic: Literal["enable", "disable"]
    # Enable/disable sniffer traffic logging.
    sniffer_traffic: Literal["enable", "disable"]
    # Enable/disable ztna traffic logging.
    ztna_traffic: Literal["enable", "disable"]
    # Enable/disable log HTTP transaction messages.
    http_transaction: Literal["enable", "disable"]
    # Enable/disable anomaly logging.
    anomaly: Literal["enable", "disable"]
    # Enable/disable VoIP logging.
    voip: Literal["enable", "disable"]
    # Enable/disable GTP messages logging.
    gtp: Literal["enable", "disable"]
    # Enable/disable Forti-Switch logging.
    forti_switch: Literal["enable", "disable"]
    # Enable/disable debug logging.
    debug: Literal["enable", "disable"]
    # Free style filters.
    free_style: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FilterPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Filter:
    """
    Filters for null device logging.
    
    Path: log/null_device/filter
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
    ) -> FilterObject: ...
    
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
    ) -> FilterObject: ...
    
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
    ) -> FilterObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FilterPayload | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        forward_traffic: Literal["enable", "disable"] | None = ...,
        local_traffic: Literal["enable", "disable"] | None = ...,
        multicast_traffic: Literal["enable", "disable"] | None = ...,
        sniffer_traffic: Literal["enable", "disable"] | None = ...,
        ztna_traffic: Literal["enable", "disable"] | None = ...,
        http_transaction: Literal["enable", "disable"] | None = ...,
        anomaly: Literal["enable", "disable"] | None = ...,
        voip: Literal["enable", "disable"] | None = ...,
        gtp: Literal["enable", "disable"] | None = ...,
        forti_switch: Literal["enable", "disable"] | None = ...,
        debug: Literal["enable", "disable"] | None = ...,
        free_style: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FilterObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FilterPayload | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        forward_traffic: Literal["enable", "disable"] | None = ...,
        local_traffic: Literal["enable", "disable"] | None = ...,
        multicast_traffic: Literal["enable", "disable"] | None = ...,
        sniffer_traffic: Literal["enable", "disable"] | None = ...,
        ztna_traffic: Literal["enable", "disable"] | None = ...,
        http_transaction: Literal["enable", "disable"] | None = ...,
        anomaly: Literal["enable", "disable"] | None = ...,
        voip: Literal["enable", "disable"] | None = ...,
        gtp: Literal["enable", "disable"] | None = ...,
        forti_switch: Literal["enable", "disable"] | None = ...,
        debug: Literal["enable", "disable"] | None = ...,
        free_style: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: FilterPayload | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        forward_traffic: Literal["enable", "disable"] | None = ...,
        local_traffic: Literal["enable", "disable"] | None = ...,
        multicast_traffic: Literal["enable", "disable"] | None = ...,
        sniffer_traffic: Literal["enable", "disable"] | None = ...,
        ztna_traffic: Literal["enable", "disable"] | None = ...,
        http_transaction: Literal["enable", "disable"] | None = ...,
        anomaly: Literal["enable", "disable"] | None = ...,
        voip: Literal["enable", "disable"] | None = ...,
        gtp: Literal["enable", "disable"] | None = ...,
        forti_switch: Literal["enable", "disable"] | None = ...,
        debug: Literal["enable", "disable"] | None = ...,
        free_style: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: FilterPayload | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        forward_traffic: Literal["enable", "disable"] | None = ...,
        local_traffic: Literal["enable", "disable"] | None = ...,
        multicast_traffic: Literal["enable", "disable"] | None = ...,
        sniffer_traffic: Literal["enable", "disable"] | None = ...,
        ztna_traffic: Literal["enable", "disable"] | None = ...,
        http_transaction: Literal["enable", "disable"] | None = ...,
        anomaly: Literal["enable", "disable"] | None = ...,
        voip: Literal["enable", "disable"] | None = ...,
        gtp: Literal["enable", "disable"] | None = ...,
        forti_switch: Literal["enable", "disable"] | None = ...,
        debug: Literal["enable", "disable"] | None = ...,
        free_style: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: FilterPayload | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        forward_traffic: Literal["enable", "disable"] | None = ...,
        local_traffic: Literal["enable", "disable"] | None = ...,
        multicast_traffic: Literal["enable", "disable"] | None = ...,
        sniffer_traffic: Literal["enable", "disable"] | None = ...,
        ztna_traffic: Literal["enable", "disable"] | None = ...,
        http_transaction: Literal["enable", "disable"] | None = ...,
        anomaly: Literal["enable", "disable"] | None = ...,
        voip: Literal["enable", "disable"] | None = ...,
        gtp: Literal["enable", "disable"] | None = ...,
        forti_switch: Literal["enable", "disable"] | None = ...,
        debug: Literal["enable", "disable"] | None = ...,
        free_style: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Filter",
    "FilterPayload",
    "FilterObject",
]