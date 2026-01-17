from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# ============================================================================
# Nested TypedDicts for table field children (dict mode)
# These MUST be defined before the Payload class to use them as type hints
# ============================================================================

class FilterFreestyleItem(TypedDict, total=False):
    """Type hints for free-style table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - id: int
        - category: "traffic" | "event" | "virus" | "webfilter" | "attack" | "spam" | "anomaly" | "voip" | "dlp" | "app-ctrl" | "waf" | "gtp" | "dns" | "ssh" | "ssl" | "file-filter" | "icap" | "virtual-patch" | "debug"
        - filter: str
        - filter_type: "include" | "exclude"
    
    **Example:**
        entry: FilterFreestyleItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    id: int  # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    category: Literal["traffic", "event", "virus", "webfilter", "attack", "spam", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"]  # Log category. | Default: traffic
    filter: str  # Free style filter string. | MaxLen: 1023
    filter_type: Literal["include", "exclude"]  # Include/exclude logs that match the filter. | Default: include


# ============================================================================
# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
# ============================================================================
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class FilterPayload(TypedDict, total=False):
    """
    Type hints for log/syslogd3/filter payload fields.
    
    Filters for remote system server.
    
    **Usage:**
        payload: FilterPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log. | Default: information
    forward_traffic: Literal["enable", "disable"]  # Enable/disable forward traffic logging. | Default: enable
    local_traffic: Literal["enable", "disable"]  # Enable/disable local in or out traffic logging. | Default: enable
    multicast_traffic: Literal["enable", "disable"]  # Enable/disable multicast traffic logging. | Default: enable
    sniffer_traffic: Literal["enable", "disable"]  # Enable/disable sniffer traffic logging. | Default: enable
    ztna_traffic: Literal["enable", "disable"]  # Enable/disable ztna traffic logging. | Default: enable
    http_transaction: Literal["enable", "disable"]  # Enable/disable log HTTP transaction messages. | Default: enable
    anomaly: Literal["enable", "disable"]  # Enable/disable anomaly logging. | Default: enable
    voip: Literal["enable", "disable"]  # Enable/disable VoIP logging. | Default: enable
    gtp: Literal["enable", "disable"]  # Enable/disable GTP messages logging. | Default: enable
    forti_switch: Literal["enable", "disable"]  # Enable/disable Forti-Switch logging. | Default: enable
    debug: Literal["enable", "disable"]  # Enable/disable debug logging. | Default: disable
    free_style: list[FilterFreestyleItem]  # Free style filters.

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================

@final
class FilterFreestyleObject:
    """Typed object for free-style table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Log category. | Default: traffic
    category: Literal["traffic", "event", "virus", "webfilter", "attack", "spam", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"]
    # Free style filter string. | MaxLen: 1023
    filter: str
    # Include/exclude logs that match the filter. | Default: include
    filter_type: Literal["include", "exclude"]
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...




# Response TypedDict for GET returns (all fields present in API response)
class FilterResponse(TypedDict):
    """
    Type hints for log/syslogd3/filter API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log. | Default: information
    forward_traffic: Literal["enable", "disable"]  # Enable/disable forward traffic logging. | Default: enable
    local_traffic: Literal["enable", "disable"]  # Enable/disable local in or out traffic logging. | Default: enable
    multicast_traffic: Literal["enable", "disable"]  # Enable/disable multicast traffic logging. | Default: enable
    sniffer_traffic: Literal["enable", "disable"]  # Enable/disable sniffer traffic logging. | Default: enable
    ztna_traffic: Literal["enable", "disable"]  # Enable/disable ztna traffic logging. | Default: enable
    http_transaction: Literal["enable", "disable"]  # Enable/disable log HTTP transaction messages. | Default: enable
    anomaly: Literal["enable", "disable"]  # Enable/disable anomaly logging. | Default: enable
    voip: Literal["enable", "disable"]  # Enable/disable VoIP logging. | Default: enable
    gtp: Literal["enable", "disable"]  # Enable/disable GTP messages logging. | Default: enable
    forti_switch: Literal["enable", "disable"]  # Enable/disable Forti-Switch logging. | Default: enable
    debug: Literal["enable", "disable"]  # Enable/disable debug logging. | Default: disable
    free_style: list[FilterFreestyleItem]  # Free style filters.


@final
class FilterObject:
    """Typed FortiObject for log/syslogd3/filter with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Lowest severity level to log. | Default: information
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Enable/disable forward traffic logging. | Default: enable
    forward_traffic: Literal["enable", "disable"]
    # Enable/disable local in or out traffic logging. | Default: enable
    local_traffic: Literal["enable", "disable"]
    # Enable/disable multicast traffic logging. | Default: enable
    multicast_traffic: Literal["enable", "disable"]
    # Enable/disable sniffer traffic logging. | Default: enable
    sniffer_traffic: Literal["enable", "disable"]
    # Enable/disable ztna traffic logging. | Default: enable
    ztna_traffic: Literal["enable", "disable"]
    # Enable/disable log HTTP transaction messages. | Default: enable
    http_transaction: Literal["enable", "disable"]
    # Enable/disable anomaly logging. | Default: enable
    anomaly: Literal["enable", "disable"]
    # Enable/disable VoIP logging. | Default: enable
    voip: Literal["enable", "disable"]
    # Enable/disable GTP messages logging. | Default: enable
    gtp: Literal["enable", "disable"]
    # Enable/disable Forti-Switch logging. | Default: enable
    forti_switch: Literal["enable", "disable"]
    # Enable/disable debug logging. | Default: disable
    debug: Literal["enable", "disable"]
    # Free style filters.
    free_style: list[FilterFreestyleObject]
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FilterPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Filter:
    """
    Filters for remote system server.
    
    Path: log/syslogd3/filter
    Category: cmdb
    """
    
    def __init__(self, client: Any) -> None:
        """Initialize endpoint with HTTP client.
        
        Args:
            client: HTTP client instance for API communication
        """
        ...
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
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
    ) -> FilterObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
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
    ) -> FilterObject: ...
    
    # Without mkey -> returns list of FortiObjects
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
    ) -> FilterObject: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
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
    ) -> FilterObject: ...
    
    # With mkey as keyword arg -> returns single object
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
    ) -> FilterObject: ...
    
    # With no mkey -> returns list of objects
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
    ) -> FilterObject: ...
    
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
    ) -> FilterObject: ...
    
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
    ) -> FilterObject: ...
    
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
    ) -> FilterObject: ...
    
    # Fallback overload for all other cases
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> FilterObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        format: str = ...,
    ) -> FortiObject: ...
    
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
        free_style: str | list[str] | list[FilterFreestyleItem] | None = ...,
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
        free_style: str | list[str] | list[FilterFreestyleItem] | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
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
        free_style: str | list[str] | list[FilterFreestyleItem] | None = ...,
    ) -> FortiObject: ...
    
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
        free_style: str | list[str] | list[FilterFreestyleItem] | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
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
        free_style: str | list[str] | list[FilterFreestyleItem] | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "Filter",
    "FilterPayload",
    "FilterResponse",
    "FilterObject",
]