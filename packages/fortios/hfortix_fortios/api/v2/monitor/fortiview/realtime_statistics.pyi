from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class RealtimeStatisticsPayload(TypedDict, total=False):
    """
    Type hints for fortiview/realtime_statistics payload fields.
    
    Retrieve realtime drill-down and summary data for FortiView.
    
    **Usage:**
        payload: RealtimeStatisticsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    srcaddr: str  # srcaddr
    dstaddr: str  # dstaddr
    srcaddr6: str  # srcaddr6
    dstaddr6: str  # dstaddr6
    srcport: str  # srcport
    dstport: str  # dstport
    srcintf: str  # srcintf
    srcintfrole: str  # srcintfrole
    dstintf: str  # dstintf
    dstintfrole: str  # dstintfrole
    policyid: str  # policyid
    security_policyid: str  # security-policyid
    protocol: str  # protocol
    web_category: str  # web-category
    web_domain: str  # web-domain
    application: str  # application
    country: str  # country
    seconds: str  # seconds
    since: str  # since
    owner: str  # owner
    username: str  # username
    shaper: str  # shaper
    srcuuid: str  # srcuuid
    dstuuid: str  # dstuuid
    sessionid: str  # sessionid
    report_by: str  # report_by
    sort_by: str  # sort_by
    ip_version: str  # ip_version

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class RealtimeStatisticsResponse(TypedDict):
    """
    Type hints for fortiview/realtime_statistics API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    srcaddr: str
    dstaddr: str
    srcaddr6: str
    dstaddr6: str
    srcport: str
    dstport: str
    srcintf: str
    srcintfrole: str
    dstintf: str
    dstintfrole: str
    policyid: str
    security_policyid: str
    protocol: str
    web_category: str
    web_domain: str
    application: str
    country: str
    seconds: str
    since: str
    owner: str
    username: str
    shaper: str
    srcuuid: str
    dstuuid: str
    sessionid: str
    report_by: str
    sort_by: str
    ip_version: str


@final
class RealtimeStatisticsObject:
    """Typed FortiObject for fortiview/realtime_statistics with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # srcaddr
    srcaddr: str
    # dstaddr
    dstaddr: str
    # srcaddr6
    srcaddr6: str
    # dstaddr6
    dstaddr6: str
    # srcport
    srcport: str
    # dstport
    dstport: str
    # srcintf
    srcintf: str
    # srcintfrole
    srcintfrole: str
    # dstintf
    dstintf: str
    # dstintfrole
    dstintfrole: str
    # policyid
    policyid: str
    # security-policyid
    security_policyid: str
    # protocol
    protocol: str
    # web-category
    web_category: str
    # web-domain
    web_domain: str
    # application
    application: str
    # country
    country: str
    # seconds
    seconds: str
    # since
    since: str
    # owner
    owner: str
    # username
    username: str
    # shaper
    shaper: str
    # srcuuid
    srcuuid: str
    # dstuuid
    dstuuid: str
    # sessionid
    sessionid: str
    # report_by
    report_by: str
    # sort_by
    sort_by: str
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
    def to_dict(self) -> RealtimeStatisticsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class RealtimeStatistics:
    """
    Retrieve realtime drill-down and summary data for FortiView.
    
    Path: fortiview/realtime_statistics
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
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintf: str | None = ...,
        dstintfrole: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        protocol: str | None = ...,
        web_category: str | None = ...,
        web_domain: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        srcuuid: str | None = ...,
        dstuuid: str | None = ...,
        sessionid: str | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
        ip_version: Literal["*ipv4", "ipv6", "ipboth"] | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> RealtimeStatisticsObject: ...
    
    
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
    ) -> RealtimeStatisticsObject: ...
    
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
    ) -> RealtimeStatisticsObject: ...
    
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
    ) -> RealtimeStatisticsObject: ...
    
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
    ) -> RealtimeStatisticsObject: ...
    
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
    ) -> RealtimeStatisticsObject: ...
    
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
    ) -> RealtimeStatisticsObject: ...
    
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
    ) -> RealtimeStatisticsObject | dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RealtimeStatisticsPayload | None = ...,
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintf: str | None = ...,
        dstintfrole: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        protocol: str | None = ...,
        web_category: str | None = ...,
        web_domain: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        srcuuid: str | None = ...,
        dstuuid: str | None = ...,
        sessionid: str | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
        ip_version: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> RealtimeStatisticsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RealtimeStatisticsPayload | None = ...,
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintf: str | None = ...,
        dstintfrole: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        protocol: str | None = ...,
        web_category: str | None = ...,
        web_domain: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        srcuuid: str | None = ...,
        dstuuid: str | None = ...,
        sessionid: str | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
        ip_version: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: RealtimeStatisticsPayload | None = ...,
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintf: str | None = ...,
        dstintfrole: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        protocol: str | None = ...,
        web_category: str | None = ...,
        web_domain: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        srcuuid: str | None = ...,
        dstuuid: str | None = ...,
        sessionid: str | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
        ip_version: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: RealtimeStatisticsPayload | None = ...,
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintf: str | None = ...,
        dstintfrole: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        protocol: str | None = ...,
        web_category: str | None = ...,
        web_domain: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        srcuuid: str | None = ...,
        dstuuid: str | None = ...,
        sessionid: str | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
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
        payload_dict: RealtimeStatisticsPayload | None = ...,
        srcaddr: str | None = ...,
        dstaddr: str | None = ...,
        srcaddr6: str | None = ...,
        dstaddr6: str | None = ...,
        srcport: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintf: str | None = ...,
        dstintfrole: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        protocol: str | None = ...,
        web_category: str | None = ...,
        web_domain: str | None = ...,
        application: str | None = ...,
        country: str | None = ...,
        seconds: str | None = ...,
        since: str | None = ...,
        owner: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        srcuuid: str | None = ...,
        dstuuid: str | None = ...,
        sessionid: str | None = ...,
        report_by: str | None = ...,
        sort_by: str | None = ...,
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
    "RealtimeStatistics",
    "RealtimeStatisticsPayload",
    "RealtimeStatisticsResponse",
    "RealtimeStatisticsObject",
]