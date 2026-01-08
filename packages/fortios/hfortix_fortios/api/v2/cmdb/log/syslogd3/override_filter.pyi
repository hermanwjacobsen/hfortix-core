from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class OverrideFilterPayload(TypedDict, total=False):
    """
    Type hints for log/syslogd3/override_filter payload fields.
    
    Override filters for remote system server.
    
    **Usage:**
        payload: OverrideFilterPayload = {
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

# Nested classes for table field children

@final
class OverrideFilterFreestyleObject:
    """Typed object for free-style table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID.
    id: int
    # Log category.
    category: Literal["traffic", "event", "virus", "webfilter", "attack", "spam", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"]
    # Free style filter string.
    filter: str
    # Include/exclude logs that match the filter.
    filter_type: Literal["include", "exclude"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class OverrideFilterResponse(TypedDict):
    """
    Type hints for log/syslogd3/override_filter API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    forward_traffic: Literal["enable", "disable"]
    local_traffic: Literal["enable", "disable"]
    multicast_traffic: Literal["enable", "disable"]
    sniffer_traffic: Literal["enable", "disable"]
    ztna_traffic: Literal["enable", "disable"]
    http_transaction: Literal["enable", "disable"]
    anomaly: Literal["enable", "disable"]
    voip: Literal["enable", "disable"]
    gtp: Literal["enable", "disable"]
    forti_switch: Literal["enable", "disable"]
    debug: Literal["enable", "disable"]
    free_style: list[dict[str, Any]]


@final
class OverrideFilterObject:
    """Typed FortiObject for log/syslogd3/override_filter with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
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
    free_style: list[OverrideFilterFreestyleObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> OverrideFilterPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class OverrideFilter:
    """
    Override filters for remote system server.
    
    Path: log/syslogd3/override_filter
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
    ) -> OverrideFilterObject: ...
    
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
    ) -> OverrideFilterObject: ...
    
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
    ) -> OverrideFilterObject: ...
    
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
    ) -> OverrideFilterResponse: ...
    
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
    ) -> OverrideFilterResponse: ...
    
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
    ) -> OverrideFilterResponse: ...
    
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
    ) -> OverrideFilterObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: OverrideFilterPayload | None = ...,
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
    ) -> OverrideFilterObject: ...
    
    @overload
    def put(
        self,
        payload_dict: OverrideFilterPayload | None = ...,
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
        payload_dict: OverrideFilterPayload | None = ...,
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
        payload_dict: OverrideFilterPayload | None = ...,
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
        payload_dict: OverrideFilterPayload | None = ...,
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
    "OverrideFilter",
    "OverrideFilterPayload",
    "OverrideFilterObject",
]