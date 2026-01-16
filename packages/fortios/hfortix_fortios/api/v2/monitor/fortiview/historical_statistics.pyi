from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class HistoricalStatisticsPayload(TypedDict, total=False):
    """
    Type hints for fortiview/historical_statistics payload fields.
    
    Retrieve historical drill-down and summary data for FortiView.
    
    **Usage:**
        payload: HistoricalStatisticsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    filter: str  # filter
    sessionid: str  # sessionid
    device: str  # device
    report_by: str  # report_by
    sort_by: str  # sort_by
    chart_only: str  # chart_only
    end: str  # end
    ip_version: str  # ip_version

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class HistoricalStatisticsResponse(TypedDict):
    """
    Type hints for fortiview/historical_statistics API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    filter: str
    sessionid: str
    device: str
    report_by: str
    sort_by: str
    chart_only: str
    end: str
    ip_version: str


@final
class HistoricalStatisticsObject:
    """Typed FortiObject for fortiview/historical_statistics with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # filter
    filter: str
    # sessionid
    sessionid: str
    # device
    device: str
    # report_by
    report_by: str
    # sort_by
    sort_by: str
    # chart_only
    chart_only: str
    # end
    end: str
    # ip_version
    ip_version: str
    
    # Common API response fields
    status: str
    http_status: int | None
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
    def to_dict(self) -> HistoricalStatisticsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class HistoricalStatistics:
    """
    Retrieve historical drill-down and summary data for FortiView.
    
    Path: fortiview/historical_statistics
    Category: monitor
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # Service/Monitor endpoint with query parameters
    @overload
    def get(
        self,
        *,
        filter: str | None = ...,
        sessionid: str | None = ...,
        device: Literal["disk", "fortianalyzer", "forticloud"] | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
        chart_only: str | None = ...,
        end: str | None = ...,
        ip_version: Literal["*ipv4", "ipv6", "ipboth"] | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> HistoricalStatisticsObject: ...
    
    
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
    ) -> HistoricalStatisticsObject: ...
    
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
    ) -> HistoricalStatisticsObject: ...
    
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
    ) -> HistoricalStatisticsObject: ...
    
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
    ) -> HistoricalStatisticsObject: ...
    
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
    ) -> HistoricalStatisticsObject: ...
    
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
    ) -> HistoricalStatisticsObject: ...
    
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
    ) -> HistoricalStatisticsObject | dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: HistoricalStatisticsPayload | None = ...,
        filter: str | None = ...,
        sessionid: str | None = ...,
        device: str | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
        chart_only: str | None = ...,
        end: str | None = ...,
        ip_version: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> HistoricalStatisticsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: HistoricalStatisticsPayload | None = ...,
        filter: str | None = ...,
        sessionid: str | None = ...,
        device: str | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
        chart_only: str | None = ...,
        end: str | None = ...,
        ip_version: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: HistoricalStatisticsPayload | None = ...,
        filter: str | None = ...,
        sessionid: str | None = ...,
        device: str | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
        chart_only: str | None = ...,
        end: str | None = ...,
        ip_version: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: HistoricalStatisticsPayload | None = ...,
        filter: str | None = ...,
        sessionid: str | None = ...,
        device: str | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
        chart_only: str | None = ...,
        end: str | None = ...,
        ip_version: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: HistoricalStatisticsPayload | None = ...,
        filter: str | None = ...,
        sessionid: str | None = ...,
        device: str | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
        chart_only: str | None = ...,
        end: str | None = ...,
        ip_version: str | None = ...,
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
    "HistoricalStatistics",
    "HistoricalStatisticsPayload",
    "HistoricalStatisticsResponse",
    "HistoricalStatisticsObject",
]