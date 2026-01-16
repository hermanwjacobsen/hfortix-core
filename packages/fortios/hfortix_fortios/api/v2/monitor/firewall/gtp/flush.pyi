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
class FlushPayload(TypedDict, total=False):
    """
    Type hints for firewall/gtp/flush payload fields.
    
    Flush GTP tunnels.
    
    **Usage:**
        payload: FlushPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    scope: str  # scope
    gtp_profile: str  # gtp_profile
    version: int  # version
    imsi: str  # imsi
    msisdn: str  # msisdn
    ms_addr: str  # ms_addr
    ms_addr6: str  # ms_addr6
    cteid: int  # cteid
    cteid_addr: str  # cteid_addr
    cteid_addr6: str  # cteid_addr6
    fteid: int  # fteid
    fteid_addr: str  # fteid_addr
    fteid_addr6: str  # fteid_addr6
    apn: str  # apn

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class FlushResponse(TypedDict):
    """
    Type hints for firewall/gtp/flush API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    scope: str
    gtp_profile: str
    version: int
    imsi: str
    msisdn: str
    ms_addr: str
    ms_addr6: str
    cteid: int
    cteid_addr: str
    cteid_addr6: str
    fteid: int
    fteid_addr: str
    fteid_addr6: str
    apn: str


@final
class FlushObject:
    """Typed FortiObject for firewall/gtp/flush with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # scope
    scope: str
    # gtp_profile
    gtp_profile: str
    # version
    version: int
    # imsi
    imsi: str
    # msisdn
    msisdn: str
    # ms_addr
    ms_addr: str
    # ms_addr6
    ms_addr6: str
    # cteid
    cteid: int
    # cteid_addr
    cteid_addr: str
    # cteid_addr6
    cteid_addr6: str
    # fteid
    fteid: int
    # fteid_addr
    fteid_addr: str
    # fteid_addr6
    fteid_addr6: str
    # apn
    apn: str
    
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
    def to_dict(self) -> FlushPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Flush:
    """
    Flush GTP tunnels.
    
    Path: firewall/gtp/flush
    Category: monitor
    """
    
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
    ) -> FlushObject: ...
    
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
    ) -> FlushObject: ...
    
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
    ) -> FlushObject: ...
    
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
    ) -> FlushObject: ...
    
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
    ) -> FlushObject: ...
    
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
    ) -> FlushObject: ...
    
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
    ) -> FlushObject: ...
    
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
    ) -> FlushObject: ...
    
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
    ) -> FlushObject: ...
    
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
    ) -> FlushObject | dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: FlushPayload | None = ...,
        scope: str | None = ...,
        gtp_profile: str | None = ...,
        version: int | None = ...,
        imsi: str | None = ...,
        msisdn: str | None = ...,
        ms_addr: str | None = ...,
        ms_addr6: str | None = ...,
        cteid: int | None = ...,
        cteid_addr: str | None = ...,
        cteid_addr6: str | None = ...,
        fteid: int | None = ...,
        fteid_addr: str | None = ...,
        fteid_addr6: str | None = ...,
        apn: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FlushObject: ...
    
    @overload
    def post(
        self,
        payload_dict: FlushPayload | None = ...,
        scope: str | None = ...,
        gtp_profile: str | None = ...,
        version: int | None = ...,
        imsi: str | None = ...,
        msisdn: str | None = ...,
        ms_addr: str | None = ...,
        ms_addr6: str | None = ...,
        cteid: int | None = ...,
        cteid_addr: str | None = ...,
        cteid_addr6: str | None = ...,
        fteid: int | None = ...,
        fteid_addr: str | None = ...,
        fteid_addr6: str | None = ...,
        apn: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: FlushPayload | None = ...,
        scope: str | None = ...,
        gtp_profile: str | None = ...,
        version: int | None = ...,
        imsi: str | None = ...,
        msisdn: str | None = ...,
        ms_addr: str | None = ...,
        ms_addr6: str | None = ...,
        cteid: int | None = ...,
        cteid_addr: str | None = ...,
        cteid_addr6: str | None = ...,
        fteid: int | None = ...,
        fteid_addr: str | None = ...,
        fteid_addr6: str | None = ...,
        apn: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: FlushPayload | None = ...,
        scope: str | None = ...,
        gtp_profile: str | None = ...,
        version: int | None = ...,
        imsi: str | None = ...,
        msisdn: str | None = ...,
        ms_addr: str | None = ...,
        ms_addr6: str | None = ...,
        cteid: int | None = ...,
        cteid_addr: str | None = ...,
        cteid_addr6: str | None = ...,
        fteid: int | None = ...,
        fteid_addr: str | None = ...,
        fteid_addr6: str | None = ...,
        apn: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FlushPayload | None = ...,
        scope: str | None = ...,
        gtp_profile: str | None = ...,
        version: int | None = ...,
        imsi: str | None = ...,
        msisdn: str | None = ...,
        ms_addr: str | None = ...,
        ms_addr6: str | None = ...,
        cteid: int | None = ...,
        cteid_addr: str | None = ...,
        cteid_addr6: str | None = ...,
        fteid: int | None = ...,
        fteid_addr: str | None = ...,
        fteid_addr6: str | None = ...,
        apn: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FlushObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FlushPayload | None = ...,
        scope: str | None = ...,
        gtp_profile: str | None = ...,
        version: int | None = ...,
        imsi: str | None = ...,
        msisdn: str | None = ...,
        ms_addr: str | None = ...,
        ms_addr6: str | None = ...,
        cteid: int | None = ...,
        cteid_addr: str | None = ...,
        cteid_addr6: str | None = ...,
        fteid: int | None = ...,
        fteid_addr: str | None = ...,
        fteid_addr6: str | None = ...,
        apn: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: FlushPayload | None = ...,
        scope: str | None = ...,
        gtp_profile: str | None = ...,
        version: int | None = ...,
        imsi: str | None = ...,
        msisdn: str | None = ...,
        ms_addr: str | None = ...,
        ms_addr6: str | None = ...,
        cteid: int | None = ...,
        cteid_addr: str | None = ...,
        cteid_addr6: str | None = ...,
        fteid: int | None = ...,
        fteid_addr: str | None = ...,
        fteid_addr6: str | None = ...,
        apn: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: FlushPayload | None = ...,
        scope: str | None = ...,
        gtp_profile: str | None = ...,
        version: int | None = ...,
        imsi: str | None = ...,
        msisdn: str | None = ...,
        ms_addr: str | None = ...,
        ms_addr6: str | None = ...,
        cteid: int | None = ...,
        cteid_addr: str | None = ...,
        cteid_addr6: str | None = ...,
        fteid: int | None = ...,
        fteid_addr: str | None = ...,
        fteid_addr6: str | None = ...,
        apn: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FlushPayload | None = ...,
        scope: str | None = ...,
        gtp_profile: str | None = ...,
        version: int | None = ...,
        imsi: str | None = ...,
        msisdn: str | None = ...,
        ms_addr: str | None = ...,
        ms_addr6: str | None = ...,
        cteid: int | None = ...,
        cteid_addr: str | None = ...,
        cteid_addr6: str | None = ...,
        fteid: int | None = ...,
        fteid_addr: str | None = ...,
        fteid_addr6: str | None = ...,
        apn: str | None = ...,
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
    "Flush",
    "FlushPayload",
    "FlushResponse",
    "FlushObject",
]