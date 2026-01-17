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
class ReportPayload(TypedDict, total=False):
    """
    Type hints for sdwan/link_monitor_metrics/report payload fields.
    
    Report the application-level performance metrics collected by other fabric devices.
    
    **Usage:**
        payload: ReportPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    agent_ip: str  # agent_ip
    application_name: str  # application_name
    application_id: int  # application_id
    latency: str  # latency
    jitter: str  # jitter
    packet_loss: str  # packet_loss
    ntt: str  # ntt
    srt: str  # srt
    application_error: str  # application_error

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class ReportResponse(TypedDict):
    """
    Type hints for sdwan/link_monitor_metrics/report API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    agent_ip: str
    application_name: str
    application_id: int
    latency: str
    jitter: str
    packet_loss: str
    ntt: str
    srt: str
    application_error: str


@final
class ReportObject:
    """Typed FortiObject for sdwan/link_monitor_metrics/report with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # agent_ip
    agent_ip: str
    # application_name
    application_name: str
    # application_id
    application_id: int
    # latency
    latency: str
    # jitter
    jitter: str
    # packet_loss
    packet_loss: str
    # ntt
    ntt: str
    # srt
    srt: str
    # application_error
    application_error: str
    
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
    def to_dict(self) -> ReportPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Report:
    """
    Report the application-level performance metrics collected by other fabric devices.
    
    Path: sdwan/link_monitor_metrics/report
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
        vdom: str | bool | None = ...,
    ) -> ReportObject: ...
    
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
        vdom: str | bool | None = ...,
    ) -> ReportObject: ...
    
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
        vdom: str | bool | None = ...,
    ) -> ReportObject: ...
    
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
    ) -> ReportObject: ...
    
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
    ) -> ReportObject: ...
    
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
    ) -> ReportObject: ...
    
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
    ) -> ReportObject: ...
    
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
    ) -> ReportObject: ...
    
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
    ) -> ReportObject: ...
    
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
    ) -> ReportObject | dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ReportPayload | None = ...,
        agent_ip: str | None = ...,
        application_name: str | None = ...,
        application_id: int | None = ...,
        latency: str | None = ...,
        jitter: str | None = ...,
        packet_loss: str | None = ...,
        ntt: str | None = ...,
        srt: str | None = ...,
        application_error: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ReportObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ReportPayload | None = ...,
        agent_ip: str | None = ...,
        application_name: str | None = ...,
        application_id: int | None = ...,
        latency: str | None = ...,
        jitter: str | None = ...,
        packet_loss: str | None = ...,
        ntt: str | None = ...,
        srt: str | None = ...,
        application_error: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ReportPayload | None = ...,
        agent_ip: str | None = ...,
        application_name: str | None = ...,
        application_id: int | None = ...,
        latency: str | None = ...,
        jitter: str | None = ...,
        packet_loss: str | None = ...,
        ntt: str | None = ...,
        srt: str | None = ...,
        application_error: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: ReportPayload | None = ...,
        agent_ip: str | None = ...,
        application_name: str | None = ...,
        application_id: int | None = ...,
        latency: str | None = ...,
        jitter: str | None = ...,
        packet_loss: str | None = ...,
        ntt: str | None = ...,
        srt: str | None = ...,
        application_error: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ReportPayload | None = ...,
        agent_ip: str | None = ...,
        application_name: str | None = ...,
        application_id: int | None = ...,
        latency: str | None = ...,
        jitter: str | None = ...,
        packet_loss: str | None = ...,
        ntt: str | None = ...,
        srt: str | None = ...,
        application_error: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ReportObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ReportPayload | None = ...,
        agent_ip: str | None = ...,
        application_name: str | None = ...,
        application_id: int | None = ...,
        latency: str | None = ...,
        jitter: str | None = ...,
        packet_loss: str | None = ...,
        ntt: str | None = ...,
        srt: str | None = ...,
        application_error: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ReportPayload | None = ...,
        agent_ip: str | None = ...,
        application_name: str | None = ...,
        application_id: int | None = ...,
        latency: str | None = ...,
        jitter: str | None = ...,
        packet_loss: str | None = ...,
        ntt: str | None = ...,
        srt: str | None = ...,
        application_error: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ReportPayload | None = ...,
        agent_ip: str | None = ...,
        application_name: str | None = ...,
        application_id: int | None = ...,
        latency: str | None = ...,
        jitter: str | None = ...,
        packet_loss: str | None = ...,
        ntt: str | None = ...,
        srt: str | None = ...,
        application_error: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ReportPayload | None = ...,
        agent_ip: str | None = ...,
        application_name: str | None = ...,
        application_id: int | None = ...,
        latency: str | None = ...,
        jitter: str | None = ...,
        packet_loss: str | None = ...,
        ntt: str | None = ...,
        srt: str | None = ...,
        application_error: str | None = ...,
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
    "Report",
    "ReportPayload",
    "ReportResponse",
    "ReportObject",
]