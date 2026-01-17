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
class StartPayload(TypedDict, total=False):
    """
    Type hints for network/debug_flow/start payload fields.
    
    Start debug flow packet capture.
    
    **Usage:**
        payload: StartPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    num_packets: int  # num_packets
    ipv6: bool  # ipv6
    negate: bool  # negate
    addr_from: str  # addr_from
    addr_to: str  # addr_to
    daddr_from: str  # daddr_from
    daddr_to: str  # daddr_to
    saddr_from: str  # saddr_from
    saddr_to: str  # saddr_to
    port_from: int  # port_from
    port_to: int  # port_to
    dport_from: int  # dport_from
    dport_to: int  # dport_to
    sport_from: int  # sport_from
    sport_to: int  # sport_to
    proto: int  # proto

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class StartResponse(TypedDict):
    """
    Type hints for network/debug_flow/start API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    num_packets: int
    ipv6: bool
    negate: bool
    addr_from: str
    addr_to: str
    daddr_from: str
    daddr_to: str
    saddr_from: str
    saddr_to: str
    port_from: int
    port_to: int
    dport_from: int
    dport_to: int
    sport_from: int
    sport_to: int
    proto: int


@final
class StartObject:
    """Typed FortiObject for network/debug_flow/start with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # num_packets
    num_packets: int
    # ipv6
    ipv6: bool
    # negate
    negate: bool
    # addr_from
    addr_from: str
    # addr_to
    addr_to: str
    # daddr_from
    daddr_from: str
    # daddr_to
    daddr_to: str
    # saddr_from
    saddr_from: str
    # saddr_to
    saddr_to: str
    # port_from
    port_from: int
    # port_to
    port_to: int
    # dport_from
    dport_from: int
    # dport_to
    dport_to: int
    # sport_from
    sport_from: int
    # sport_to
    sport_to: int
    # proto
    proto: int
    
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
    def to_dict(self) -> StartPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Start:
    """
    Start debug flow packet capture.
    
    Path: network/debug_flow/start
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
    ) -> StartObject: ...
    
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
    ) -> StartObject: ...
    
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
    ) -> StartObject: ...
    
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
    ) -> StartObject: ...
    
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
    ) -> StartObject: ...
    
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
    ) -> StartObject: ...
    
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
    ) -> StartObject: ...
    
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
    ) -> StartObject: ...
    
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
    ) -> StartObject: ...
    
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
    ) -> StartObject | dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: StartPayload | None = ...,
        num_packets: int | None = ...,
        ipv6: str | None = ...,
        negate: str | None = ...,
        addr_from: str | None = ...,
        addr_to: str | None = ...,
        daddr_from: str | None = ...,
        daddr_to: str | None = ...,
        saddr_from: str | None = ...,
        saddr_to: str | None = ...,
        port_from: int | None = ...,
        port_to: int | None = ...,
        dport_from: int | None = ...,
        dport_to: int | None = ...,
        sport_from: int | None = ...,
        sport_to: int | None = ...,
        proto: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> StartObject: ...
    
    @overload
    def post(
        self,
        payload_dict: StartPayload | None = ...,
        num_packets: int | None = ...,
        ipv6: str | None = ...,
        negate: str | None = ...,
        addr_from: str | None = ...,
        addr_to: str | None = ...,
        daddr_from: str | None = ...,
        daddr_to: str | None = ...,
        saddr_from: str | None = ...,
        saddr_to: str | None = ...,
        port_from: int | None = ...,
        port_to: int | None = ...,
        dport_from: int | None = ...,
        dport_to: int | None = ...,
        sport_from: int | None = ...,
        sport_to: int | None = ...,
        proto: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: StartPayload | None = ...,
        num_packets: int | None = ...,
        ipv6: str | None = ...,
        negate: str | None = ...,
        addr_from: str | None = ...,
        addr_to: str | None = ...,
        daddr_from: str | None = ...,
        daddr_to: str | None = ...,
        saddr_from: str | None = ...,
        saddr_to: str | None = ...,
        port_from: int | None = ...,
        port_to: int | None = ...,
        dport_from: int | None = ...,
        dport_to: int | None = ...,
        sport_from: int | None = ...,
        sport_to: int | None = ...,
        proto: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: StartPayload | None = ...,
        num_packets: int | None = ...,
        ipv6: str | None = ...,
        negate: str | None = ...,
        addr_from: str | None = ...,
        addr_to: str | None = ...,
        daddr_from: str | None = ...,
        daddr_to: str | None = ...,
        saddr_from: str | None = ...,
        saddr_to: str | None = ...,
        port_from: int | None = ...,
        port_to: int | None = ...,
        dport_from: int | None = ...,
        dport_to: int | None = ...,
        sport_from: int | None = ...,
        sport_to: int | None = ...,
        proto: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: StartPayload | None = ...,
        num_packets: int | None = ...,
        ipv6: str | None = ...,
        negate: str | None = ...,
        addr_from: str | None = ...,
        addr_to: str | None = ...,
        daddr_from: str | None = ...,
        daddr_to: str | None = ...,
        saddr_from: str | None = ...,
        saddr_to: str | None = ...,
        port_from: int | None = ...,
        port_to: int | None = ...,
        dport_from: int | None = ...,
        dport_to: int | None = ...,
        sport_from: int | None = ...,
        sport_to: int | None = ...,
        proto: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> StartObject: ...
    
    @overload
    def put(
        self,
        payload_dict: StartPayload | None = ...,
        num_packets: int | None = ...,
        ipv6: str | None = ...,
        negate: str | None = ...,
        addr_from: str | None = ...,
        addr_to: str | None = ...,
        daddr_from: str | None = ...,
        daddr_to: str | None = ...,
        saddr_from: str | None = ...,
        saddr_to: str | None = ...,
        port_from: int | None = ...,
        port_to: int | None = ...,
        dport_from: int | None = ...,
        dport_to: int | None = ...,
        sport_from: int | None = ...,
        sport_to: int | None = ...,
        proto: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: StartPayload | None = ...,
        num_packets: int | None = ...,
        ipv6: str | None = ...,
        negate: str | None = ...,
        addr_from: str | None = ...,
        addr_to: str | None = ...,
        daddr_from: str | None = ...,
        daddr_to: str | None = ...,
        saddr_from: str | None = ...,
        saddr_to: str | None = ...,
        port_from: int | None = ...,
        port_to: int | None = ...,
        dport_from: int | None = ...,
        dport_to: int | None = ...,
        sport_from: int | None = ...,
        sport_to: int | None = ...,
        proto: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: StartPayload | None = ...,
        num_packets: int | None = ...,
        ipv6: str | None = ...,
        negate: str | None = ...,
        addr_from: str | None = ...,
        addr_to: str | None = ...,
        daddr_from: str | None = ...,
        daddr_to: str | None = ...,
        saddr_from: str | None = ...,
        saddr_to: str | None = ...,
        port_from: int | None = ...,
        port_to: int | None = ...,
        dport_from: int | None = ...,
        dport_to: int | None = ...,
        sport_from: int | None = ...,
        sport_to: int | None = ...,
        proto: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: StartPayload | None = ...,
        num_packets: int | None = ...,
        ipv6: str | None = ...,
        negate: str | None = ...,
        addr_from: str | None = ...,
        addr_to: str | None = ...,
        daddr_from: str | None = ...,
        daddr_to: str | None = ...,
        saddr_from: str | None = ...,
        saddr_to: str | None = ...,
        port_from: int | None = ...,
        port_to: int | None = ...,
        dport_from: int | None = ...,
        dport_to: int | None = ...,
        sport_from: int | None = ...,
        sport_to: int | None = ...,
        proto: int | None = ...,
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
    "Start",
    "StartPayload",
    "StartResponse",
    "StartObject",
]