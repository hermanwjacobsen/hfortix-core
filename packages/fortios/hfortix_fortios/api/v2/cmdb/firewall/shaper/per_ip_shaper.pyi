from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class PerIpShaperPayload(TypedDict, total=False):
    """
    Type hints for firewall/shaper/per_ip_shaper payload fields.
    
    Configure per-IP traffic shaper.
    
    **Usage:**
        payload: PerIpShaperPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Traffic shaper name.
    max_bandwidth: NotRequired[int]  # Upper bandwidth limit enforced by this shaper (0 - 80000000)
    bandwidth_unit: NotRequired[Literal["kbps", "mbps", "gbps"]]  # Unit of measurement for maximum bandwidth for this shaper
    max_concurrent_session: NotRequired[int]  # Maximum number of concurrent sessions allowed by this shaper
    max_concurrent_tcp_session: NotRequired[int]  # Maximum number of concurrent TCP sessions allowed by this sh
    max_concurrent_udp_session: NotRequired[int]  # Maximum number of concurrent UDP sessions allowed by this sh
    diffserv_forward: NotRequired[Literal["enable", "disable"]]  # Enable/disable changing the Forward (original) DiffServ sett
    diffserv_reverse: NotRequired[Literal["enable", "disable"]]  # Enable/disable changing the Reverse (reply) DiffServ setting
    diffservcode_forward: NotRequired[str]  # Forward (original) DiffServ setting to be applied to traffic
    diffservcode_rev: NotRequired[str]  # Reverse (reply) DiffServ setting to be applied to traffic ac

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class PerIpShaperResponse(TypedDict):
    """
    Type hints for firewall/shaper/per_ip_shaper API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    max_bandwidth: int
    bandwidth_unit: Literal["kbps", "mbps", "gbps"]
    max_concurrent_session: int
    max_concurrent_tcp_session: int
    max_concurrent_udp_session: int
    diffserv_forward: Literal["enable", "disable"]
    diffserv_reverse: Literal["enable", "disable"]
    diffservcode_forward: str
    diffservcode_rev: str


@final
class PerIpShaperObject:
    """Typed FortiObject for firewall/shaper/per_ip_shaper with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Traffic shaper name.
    name: str
    # Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit.
    max_bandwidth: int
    # Unit of measurement for maximum bandwidth for this shaper (Kbps, Mbps or Gbps).
    bandwidth_unit: Literal["kbps", "mbps", "gbps"]
    # Maximum number of concurrent sessions allowed by this shaper (0 - 2097000). 0 me
    max_concurrent_session: int
    # Maximum number of concurrent TCP sessions allowed by this shaper (0 - 2097000).
    max_concurrent_tcp_session: int
    # Maximum number of concurrent UDP sessions allowed by this shaper (0 - 2097000).
    max_concurrent_udp_session: int
    # Enable/disable changing the Forward (original) DiffServ setting applied to traff
    diffserv_forward: Literal["enable", "disable"]
    # Enable/disable changing the Reverse (reply) DiffServ setting applied to traffic
    diffserv_reverse: Literal["enable", "disable"]
    # Forward (original) DiffServ setting to be applied to traffic accepted by this sh
    diffservcode_forward: str
    # Reverse (reply) DiffServ setting to be applied to traffic accepted by this shape
    diffservcode_rev: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> PerIpShaperPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class PerIpShaper:
    """
    Configure per-IP traffic shaper.
    
    Path: firewall/shaper/per_ip_shaper
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PerIpShaperObject: ...
    
    # Single object (mkey/name provided as keyword arg)
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PerIpShaperObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[PerIpShaperObject]: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> PerIpShaperResponse: ...
    
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> PerIpShaperResponse: ...
    
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[PerIpShaperResponse]: ...
    
    # Default overload for dict mode
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
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
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
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> PerIpShaperObject | list[PerIpShaperObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PerIpShaperObject: ...
    
    @overload
    def post(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PerIpShaperObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PerIpShaperObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> dict[str, Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> dict[str, Any]: ...
    
    @staticmethod
    def schema() -> dict[str, Any]: ...


__all__ = [
    "PerIpShaper",
    "PerIpShaperPayload",
    "PerIpShaperObject",
]