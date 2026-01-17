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
class SessionsPayload(TypedDict, total=False):
    """
    Type hints for firewall/proxy/sessions payload fields.
    
    List all active proxy sessions (optionally filtered).
    
    **Usage:**
        payload: SessionsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ip_version: str  # ip_version
    count: int  # count
    summary: bool  # summary
    srcaddr: str  # srcaddr
    dstaddr: str  # dstaddr
    srcaddr6: str  # srcaddr6
    dstaddr6: str  # dstaddr6
    srcport: str  # srcport
    dstport: str  # dstport
    srcintf: str  # srcintf
    dstintf: str  # dstintf
    policyid: str  # policyid
    proxy_policyid: str  # proxy-policyid
    protocol: str  # protocol
    application: str  # application
    country: str  # country
    seconds: str  # seconds
    since: str  # since
    owner: str  # owner
    username: str  # username
    src_uuid: str  # src_uuid
    dst_uuid: str  # dst_uuid

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class SessionsResponse(TypedDict):
    """
    Type hints for firewall/proxy/sessions API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    summary: str
    details: str


@final
class SessionsObject:
    """Typed FortiObject for firewall/proxy/sessions with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # summary
    summary: str
    # details
    details: str
    
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
    def to_dict(self) -> SessionsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Sessions:
    """
    List all active proxy sessions (optionally filtered).
    
    Path: firewall/proxy/sessions
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
        ip_version: Literal["*ipv4", "ipv6", "ipboth"] | None = ...,
        count: str,
        summary: str | None = ...,
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        policyid: str | None = ...,
        proxy_policyid: str | None = ...,
        protocol: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        src_uuid: str | None = ...,
        dst_uuid: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SessionsObject: ...
    
    
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
    ) -> SessionsObject: ...
    
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
    ) -> SessionsObject: ...
    
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
    ) -> SessionsObject: ...
    
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
    ) -> SessionsObject: ...
    
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
    ) -> SessionsObject: ...
    
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
    ) -> SessionsObject: ...
    
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
    ) -> SessionsObject | dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SessionsPayload | None = ...,
        ip_version: str | None = ...,
        count: int | None = ...,
        summary: str | None = ...,
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        policyid: str | None = ...,
        proxy_policyid: str | None = ...,
        protocol: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        src_uuid: str | None = ...,
        dst_uuid: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SessionsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SessionsPayload | None = ...,
        ip_version: str | None = ...,
        count: int | None = ...,
        summary: str | None = ...,
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        policyid: str | None = ...,
        proxy_policyid: str | None = ...,
        protocol: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        src_uuid: str | None = ...,
        dst_uuid: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SessionsPayload | None = ...,
        ip_version: str | None = ...,
        count: int | None = ...,
        summary: str | None = ...,
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        policyid: str | None = ...,
        proxy_policyid: str | None = ...,
        protocol: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        src_uuid: str | None = ...,
        dst_uuid: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SessionsPayload | None = ...,
        ip_version: str | None = ...,
        count: int | None = ...,
        summary: str | None = ...,
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        policyid: str | None = ...,
        proxy_policyid: str | None = ...,
        protocol: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        src_uuid: str | None = ...,
        dst_uuid: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SessionsPayload | None = ...,
        ip_version: str | None = ...,
        count: int | None = ...,
        summary: str | None = ...,
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        policyid: str | None = ...,
        proxy_policyid: str | None = ...,
        protocol: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        src_uuid: str | None = ...,
        dst_uuid: str | None = ...,
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
    "Sessions",
    "SessionsPayload",
    "SessionsResponse",
    "SessionsObject",
]