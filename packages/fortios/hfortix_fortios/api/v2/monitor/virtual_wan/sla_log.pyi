from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SlaLogPayload(TypedDict, total=False):
    """
    Type hints for virtual_wan/sla_log payload fields.
    
    Retrieve logs of SLA probe results for the specified SD-WAN SLA or health check name.
    
    **Usage:**
        payload: SlaLogPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    sla: str  # sla
    interface: str  # interface
    since: str  # since
    seconds: str  # seconds
    latest: str  # latest
    min_sample_interval: str  # min_sample_interval
    sampling_interval: str  # sampling_interval
    skip_vpn_child: str  # skip_vpn_child
    include_sla_targets_met: str  # include_sla_targets_met

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SlaLogResponse(TypedDict):
    """
    Type hints for virtual_wan/sla_log API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    sla: str
    interface: str
    since: str
    seconds: str
    latest: str
    min_sample_interval: str
    sampling_interval: str
    skip_vpn_child: str
    include_sla_targets_met: str


@final
class SlaLogObject:
    """Typed FortiObject for virtual_wan/sla_log with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # sla
    sla: str
    # interface
    interface: str
    # since
    since: str
    # seconds
    seconds: str
    # latest
    latest: str
    # min_sample_interval
    min_sample_interval: str
    # sampling_interval
    sampling_interval: str
    # skip_vpn_child
    skip_vpn_child: str
    # include_sla_targets_met
    include_sla_targets_met: str
    
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
    def to_dict(self) -> SlaLogPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SlaLog:
    """
    Retrieve logs of SLA probe results for the specified SD-WAN SLA or health check name.
    
    Path: virtual_wan/sla_log
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
        sla: str | None = ...,
        interface: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        latest: str | None = ...,
        min_sample_interval: str | None = ...,
        sampling_interval: str | None = ...,
        skip_vpn_child: str | None = ...,
        include_sla_targets_met: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SlaLogObject: ...
    
    
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
    ) -> SlaLogObject: ...
    
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
    ) -> SlaLogObject: ...
    
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
    ) -> SlaLogObject: ...
    
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
    ) -> SlaLogObject: ...
    
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
    ) -> SlaLogObject: ...
    
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
    ) -> SlaLogObject: ...
    
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
    ) -> SlaLogObject | dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SlaLogPayload | None = ...,
        sla: str | None = ...,
        interface: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        latest: str | None = ...,
        min_sample_interval: str | None = ...,
        sampling_interval: str | None = ...,
        skip_vpn_child: str | None = ...,
        include_sla_targets_met: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SlaLogObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SlaLogPayload | None = ...,
        sla: str | None = ...,
        interface: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        latest: str | None = ...,
        min_sample_interval: str | None = ...,
        sampling_interval: str | None = ...,
        skip_vpn_child: str | None = ...,
        include_sla_targets_met: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SlaLogPayload | None = ...,
        sla: str | None = ...,
        interface: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        latest: str | None = ...,
        min_sample_interval: str | None = ...,
        sampling_interval: str | None = ...,
        skip_vpn_child: str | None = ...,
        include_sla_targets_met: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SlaLogPayload | None = ...,
        sla: str | None = ...,
        interface: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        latest: str | None = ...,
        min_sample_interval: str | None = ...,
        sampling_interval: str | None = ...,
        skip_vpn_child: str | None = ...,
        include_sla_targets_met: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SlaLogPayload | None = ...,
        sla: str | None = ...,
        interface: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        latest: str | None = ...,
        min_sample_interval: str | None = ...,
        sampling_interval: str | None = ...,
        skip_vpn_child: str | None = ...,
        include_sla_targets_met: str | None = ...,
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
    "SlaLog",
    "SlaLogPayload",
    "SlaLogResponse",
    "SlaLogObject",
]