from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# ============================================================================
# Nested TypedDicts for table field children (dict mode)
# These MUST be defined before the Payload class to use them as type hints
# ============================================================================

# ============================================================================
# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
# ============================================================================
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class StatsPayload(TypedDict, total=False):
    """
    Type hints for user/device/stats payload fields.
    
    Retrieve user devices stats from device store by given stat item.
    
    **Usage:**
        payload: StatsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    stat_query_type: str  # stat-query-type
    stat_key: str  # stat-key
    timestamp_from: int  # timestamp_from
    timestamp_to: int  # timestamp_to
    filters: str  # filters
    filter_logic: str  # filter_logic

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class StatsResponse(TypedDict):
    """
    Type hints for user/device/stats API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    stat_query_type: str
    stat_key: str
    timestamp_from: int
    timestamp_to: int
    filters: str
    filter_logic: str


@final
class StatsObject:
    """Typed FortiObject for user/device/stats with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # stat-query-type
    stat_query_type: str
    # stat-key
    stat_key: str
    # timestamp_from
    timestamp_from: int
    # timestamp_to
    timestamp_to: int
    # filters
    filters: str
    # filter_logic
    filter_logic: str
    
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
    def to_dict(self) -> StatsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Stats:
    """
    Retrieve user devices stats from device store by given stat item.
    
    Path: user/device/stats
    Category: monitor
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
    
    # Service/Monitor endpoint with query parameters
    @overload
    def get(
        self,
        *,
        stat_query_type: Literal["device", "fortiswitch_client", "forticlient"] | None = ...,
        stat_key: Literal["os_name", "hardware_type", "detected_interface", "is_online", "max_vuln_level", "fortiswitch_id", "fortiswitch_port_name"],
        timestamp_from: str | None = ...,
        timestamp_to: str,
        filters: Literal["exact", "contains"] | None = ...,
        filter_logic: Literal["and", "or"] | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> StatsObject: ...
    
    
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
        vdom: str | bool | None = ...,
    ) -> StatsObject: ...
    
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
        vdom: str | bool | None = ...,
    ) -> StatsObject: ...
    
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
        vdom: str | bool | None = ...,
    ) -> StatsObject: ...
    
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
    ) -> StatsObject: ...
    
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
    ) -> StatsObject: ...
    
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
    ) -> StatsObject: ...
    
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
        vdom: str | bool | None = ...,
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
        vdom: str | bool | None = ...,
    ) -> StatsObject | dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: StatsPayload | None = ...,
        stat_query_type: str | None = ...,
        stat_key: str | None = ...,
        timestamp_from: int | None = ...,
        timestamp_to: int | None = ...,
        filters: str | None = ...,
        filter_logic: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> StatsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: StatsPayload | None = ...,
        stat_query_type: str | None = ...,
        stat_key: str | None = ...,
        timestamp_from: int | None = ...,
        timestamp_to: int | None = ...,
        filters: str | None = ...,
        filter_logic: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: StatsPayload | None = ...,
        stat_query_type: str | None = ...,
        stat_key: str | None = ...,
        timestamp_from: int | None = ...,
        timestamp_to: int | None = ...,
        filters: str | None = ...,
        filter_logic: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: StatsPayload | None = ...,
        stat_query_type: str | None = ...,
        stat_key: str | None = ...,
        timestamp_from: int | None = ...,
        timestamp_to: int | None = ...,
        filters: str | None = ...,
        filter_logic: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: StatsPayload | None = ...,
        stat_query_type: str | None = ...,
        stat_key: str | None = ...,
        timestamp_from: int | None = ...,
        timestamp_to: int | None = ...,
        filters: str | None = ...,
        filter_logic: str | None = ...,
        vdom: str | bool | None = ...,
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
    "Stats",
    "StatsPayload",
    "StatsResponse",
    "StatsObject",
]