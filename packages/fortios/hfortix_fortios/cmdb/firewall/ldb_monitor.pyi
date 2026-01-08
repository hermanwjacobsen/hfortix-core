from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class LdbMonitorPayload(TypedDict, total=False):
    """
    Type hints for firewall/ldb_monitor payload fields.
    
    Configure server load balancing health monitors.
    
    **Usage:**
        payload: LdbMonitorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Monitor name.
    type: Literal["ping", "tcp", "http", "https", "dns"]  # Select the Monitor type used by the health check monitor to 
    interval: NotRequired[int]  # Time between health checks (5 - 65535 sec, default = 10).
    timeout: NotRequired[int]  # Time to wait to receive response to a health check from a se
    retry: NotRequired[int]  # Number health check attempts before the server is considered
    port: NotRequired[int]  # Service port used to perform the health check. If 0, health 
    src_ip: NotRequired[str]  # Source IP for ldb-monitor.
    http_get: NotRequired[str]  # Request URI used to send a GET request to check the health o
    http_match: NotRequired[str]  # String to match the value expected in response to an HTTP-GE
    http_max_redirects: NotRequired[int]  # The maximum number of HTTP redirects to be allowed (0 - 5, d
    dns_protocol: NotRequired[Literal["udp", "tcp"]]  # Select the protocol used by the DNS health check monitor to 
    dns_request_domain: NotRequired[str]  # Fully qualified domain name to resolve for the DNS probe.
    dns_match_ip: NotRequired[str]  # Response IP expected from DNS server.


class LdbMonitorObject(FortiObject[LdbMonitorPayload]):
    """Typed FortiObject for firewall/ldb_monitor with IDE autocomplete support."""
    
    # Monitor name.
    name: str
    # Select the Monitor type used by the health check monitor to check the health of 
    type: Literal["ping", "tcp", "http", "https", "dns"]
    # Time between health checks (5 - 65535 sec, default = 10).
    interval: int
    # Time to wait to receive response to a health check from a server. Reaching the t
    timeout: int
    # Number health check attempts before the server is considered down (1 - 255, defa
    retry: int
    # Service port used to perform the health check. If 0, health check monitor inheri
    port: int
    # Source IP for ldb-monitor.
    src_ip: str
    # Request URI used to send a GET request to check the health of an HTTP server. Op
    http_get: str
    # String to match the value expected in response to an HTTP-GET request.
    http_match: str
    # The maximum number of HTTP redirects to be allowed (0 - 5, default = 0).
    http_max_redirects: int
    # Select the protocol used by the DNS health check monitor to check the health of 
    dns_protocol: Literal["udp", "tcp"]
    # Fully qualified domain name to resolve for the DNS probe.
    dns_request_domain: str
    # Response IP expected from DNS server.
    dns_match_ip: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LdbMonitorPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class LdbMonitor:
    """
    Configure server load balancing health monitors.
    
    Path: firewall/ldb_monitor
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> LdbMonitorObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
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
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[LdbMonitorObject]: ...
    
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    ) -> LdbMonitorObject | list[LdbMonitorObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LdbMonitorObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LdbMonitorObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
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
    ) -> LdbMonitorObject: ...
    
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
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
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
    "LdbMonitor",
    "LdbMonitorPayload",
    "LdbMonitorObject",
]