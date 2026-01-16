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
    Type hints for firewall/sessions payload fields.
    
    List all active firewall sessions (optionally filtered).
    
    **Usage:**
        payload: SessionsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ip_version: str  # ip_version
    count: int  # count
    summary: bool  # summary
    srcport: str  # srcport
    policyid: str  # policyid
    security_policyid: str  # security-policyid
    application: str  # application
    protocol: str  # protocol
    dstport: str  # dstport
    srcintf: str  # srcintf
    dstintf: str  # dstintf
    srcintfrole: str  # srcintfrole
    dstintfrole: str  # dstintfrole
    srcaddr: str  # srcaddr
    srcaddr6: str  # srcaddr6
    srcuuid: str  # srcuuid
    dstaddr: str  # dstaddr
    dstaddr6: str  # dstaddr6
    dstuuid: str  # dstuuid
    username: str  # username
    shaper: str  # shaper
    country: str  # country
    owner: str  # owner
    natsourceaddress: str  # natsourceaddress
    natsourceport: str  # natsourceport
    since: str  # since
    seconds: str  # seconds
    fortiasic: str  # fortiasic

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class SessionsResponse(TypedDict):
    """
    Type hints for firewall/sessions API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    summary: str
    details: str


@final
class SessionsObject:
    """Typed FortiObject for firewall/sessions with IDE autocomplete support.
    
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
    List all active firewall sessions (optionally filtered).
    
    Path: firewall/sessions
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
        ip_version: Literal["*ipv4", "ipv6", "ipboth"] | None = ...,
        count: str,
        summary: str | None = ...,
        srcport: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        application: str | None = ...,
        protocol: Literal["all", "igmp", "tcp", "udp", "icmp", "etc"] | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintfrole: str | None = ...,
        srcaddr: str | None = ...,
        srcaddr6: str | None = ...,
        srcuuid: str | None = ...,
        dstaddr: str | None = ...,
        dstaddr6: str | None = ...,
        dstuuid: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        country: str | None = ...,
        owner: str | None = ...,
        natsourceaddress: str | None = ...,
        natsourceport: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        fortiasic: str | None = ...,
        nturbo: str | None = ...,
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
        srcport: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        application: str | None = ...,
        protocol: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintfrole: str | None = ...,
        srcaddr: str | None = ...,
        srcaddr6: str | None = ...,
        srcuuid: str | None = ...,
        dstaddr: str | None = ...,
        dstaddr6: str | None = ...,
        dstuuid: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        country: str | None = ...,
        owner: str | None = ...,
        natsourceaddress: str | None = ...,
        natsourceport: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        fortiasic: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SessionsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SessionsPayload | None = ...,
        ip_version: str | None = ...,
        count: int | None = ...,
        summary: str | None = ...,
        srcport: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        application: str | None = ...,
        protocol: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintfrole: str | None = ...,
        srcaddr: str | None = ...,
        srcaddr6: str | None = ...,
        srcuuid: str | None = ...,
        dstaddr: str | None = ...,
        dstaddr6: str | None = ...,
        dstuuid: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        country: str | None = ...,
        owner: str | None = ...,
        natsourceaddress: str | None = ...,
        natsourceport: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        fortiasic: str | None = ...,
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
        srcport: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        application: str | None = ...,
        protocol: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintfrole: str | None = ...,
        srcaddr: str | None = ...,
        srcaddr6: str | None = ...,
        srcuuid: str | None = ...,
        dstaddr: str | None = ...,
        dstaddr6: str | None = ...,
        dstuuid: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        country: str | None = ...,
        owner: str | None = ...,
        natsourceaddress: str | None = ...,
        natsourceport: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        fortiasic: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SessionsPayload | None = ...,
        ip_version: str | None = ...,
        count: int | None = ...,
        summary: str | None = ...,
        srcport: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        application: str | None = ...,
        protocol: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintfrole: str | None = ...,
        srcaddr: str | None = ...,
        srcaddr6: str | None = ...,
        srcuuid: str | None = ...,
        dstaddr: str | None = ...,
        dstaddr6: str | None = ...,
        dstuuid: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        country: str | None = ...,
        owner: str | None = ...,
        natsourceaddress: str | None = ...,
        natsourceport: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        fortiasic: str | None = ...,
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
        srcport: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        application: str | None = ...,
        protocol: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintfrole: str | None = ...,
        srcaddr: str | None = ...,
        srcaddr6: str | None = ...,
        srcuuid: str | None = ...,
        dstaddr: str | None = ...,
        dstaddr6: str | None = ...,
        dstuuid: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        country: str | None = ...,
        owner: str | None = ...,
        natsourceaddress: str | None = ...,
        natsourceport: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        fortiasic: str | None = ...,
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