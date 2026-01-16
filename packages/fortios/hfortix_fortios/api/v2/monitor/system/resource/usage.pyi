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
class UsagePayload(TypedDict, total=False):
    """
    Type hints for system/resource/usage payload fields.
    
    Retreive current and historical usage data for a provided resource.
    
    **Usage:**
        payload: UsagePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    scope: str  # scope
    resource: str  # resource
    interval: str  # interval

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class UsageResponse(TypedDict):
    """
    Type hints for system/resource/usage API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    cpu: str
    disk: str
    disk_lograte: str
    faz_cloud_lograte: str
    faz_lograte: str
    forticloud_lograte: str
    gtp_tunnel: str
    gtp_tunnel_setup_rate: str
    mem: str
    session: str
    session6: str
    setuprate: str
    setuprate6: str
    npu_session: str
    npu_session6: str
    nturbo_session: str
    nturbo_session6: str
    hw_session: str
    hw_session6: str
    hw_setuprate: str
    hw_setuprate6: str
    hw_ps_log_rate: str
    hw_pm_log_rate: str


@final
class UsageObject:
    """Typed FortiObject for system/resource/usage with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # cpu
    cpu: str
    # disk
    disk: str
    # disk_lograte
    disk_lograte: str
    # faz_cloud_lograte
    faz_cloud_lograte: str
    # faz_lograte
    faz_lograte: str
    # forticloud_lograte
    forticloud_lograte: str
    # gtp_tunnel
    gtp_tunnel: str
    # gtp_tunnel_setup_rate
    gtp_tunnel_setup_rate: str
    # mem
    mem: str
    # session
    session: str
    # session6
    session6: str
    # setuprate
    setuprate: str
    # setuprate6
    setuprate6: str
    # npu_session
    npu_session: str
    # npu_session6
    npu_session6: str
    # nturbo_session
    nturbo_session: str
    # nturbo_session6
    nturbo_session6: str
    # hw_session
    hw_session: str
    # hw_session6
    hw_session6: str
    # hw_setuprate
    hw_setuprate: str
    # hw_setuprate6
    hw_setuprate6: str
    # hw_ps_log_rate
    hw_ps_log_rate: str
    # hw_pm_log_rate
    hw_pm_log_rate: str
    
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
    def to_dict(self) -> UsagePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Usage:
    """
    Retreive current and historical usage data for a provided resource.
    
    Path: system/resource/usage
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
        scope: Literal["vdom", "global"] | None = ...,
        resource: Literal["cpu", "mem", "disk", "session", "session6", "setuprate", "setuprate6", "disk_lograte", "faz_lograte", "forticloud_lograte", "gtp_tunnel", "gtp_tunnel_setup_rate"] | None = ...,
        interval: Literal["1-min", "10-min", "30-min", "1-hour", "12-hour", "24-hour"] | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> UsageObject: ...
    
    
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
    ) -> UsageObject: ...
    
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
    ) -> UsageObject: ...
    
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
    ) -> UsageObject: ...
    
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
    ) -> UsageObject: ...
    
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
    ) -> UsageObject: ...
    
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
    ) -> UsageObject: ...
    
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
    ) -> UsageObject | dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: UsagePayload | None = ...,
        scope: str | None = ...,
        resource: str | None = ...,
        interval: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> UsageObject: ...
    
    @overload
    def put(
        self,
        payload_dict: UsagePayload | None = ...,
        scope: str | None = ...,
        resource: str | None = ...,
        interval: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: UsagePayload | None = ...,
        scope: str | None = ...,
        resource: str | None = ...,
        interval: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: UsagePayload | None = ...,
        scope: str | None = ...,
        resource: str | None = ...,
        interval: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: UsagePayload | None = ...,
        scope: str | None = ...,
        resource: str | None = ...,
        interval: str | None = ...,
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
    "Usage",
    "UsagePayload",
    "UsageResponse",
    "UsageObject",
]