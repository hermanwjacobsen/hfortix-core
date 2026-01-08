from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class FlowTrackingPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/flow_tracking payload fields.
    
    Configure FortiSwitch flow tracking and export via ipfix/netflow.
    
    **Usage:**
        payload: FlowTrackingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    sample_mode: NotRequired[Literal["local", "perimeter", "device-ingress"]]  # Configure sample mode for the flow tracking.
    sample_rate: NotRequired[int]  # Configure sample rate for the perimeter and device-ingress s
    format: NotRequired[Literal["netflow1", "netflow5", "netflow9", "ipfix"]]  # Configure flow tracking protocol.
    collectors: NotRequired[list[dict[str, Any]]]  # Configure collectors for the flow.
    level: NotRequired[Literal["vlan", "ip", "port", "proto", "mac"]]  # Configure flow tracking level.
    max_export_pkt_size: NotRequired[int]  # Configure flow max export packet size
    template_export_period: NotRequired[int]  # Configure template export period (1-60, default=5 minutes).
    timeout_general: NotRequired[int]  # Configure flow session general timeout
    timeout_icmp: NotRequired[int]  # Configure flow session ICMP timeout
    timeout_max: NotRequired[int]  # Configure flow session max timeout
    timeout_tcp: NotRequired[int]  # Configure flow session TCP timeout
    timeout_tcp_fin: NotRequired[int]  # Configure flow session TCP FIN timeout
    timeout_tcp_rst: NotRequired[int]  # Configure flow session TCP RST timeout
    timeout_udp: NotRequired[int]  # Configure flow session UDP timeout
    aggregates: NotRequired[list[dict[str, Any]]]  # Configure aggregates in which all traffic sessions matching

# Nested classes for table field children

@final
class FlowTrackingCollectorsObject:
    """Typed object for collectors table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Collector name.
    name: str
    # Collector IP address.
    ip: str
    # Collector port number(0-65535, default:0, netflow:2055, ipfix:4739).
    port: int
    # Collector L4 transport protocol for exporting packets.
    transport: Literal["udp", "tcp", "sctp"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class FlowTrackingAggregatesObject:
    """Typed object for aggregates table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Aggregate id.
    id: int
    # IP address to group all matching traffic sessions to a flow.
    ip: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class FlowTrackingResponse(TypedDict):
    """
    Type hints for switch_controller/flow_tracking API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    sample_mode: Literal["local", "perimeter", "device-ingress"]
    sample_rate: int
    format: Literal["netflow1", "netflow5", "netflow9", "ipfix"]
    collectors: list[dict[str, Any]]
    level: Literal["vlan", "ip", "port", "proto", "mac"]
    max_export_pkt_size: int
    template_export_period: int
    timeout_general: int
    timeout_icmp: int
    timeout_max: int
    timeout_tcp: int
    timeout_tcp_fin: int
    timeout_tcp_rst: int
    timeout_udp: int
    aggregates: list[dict[str, Any]]


@final
class FlowTrackingObject:
    """Typed FortiObject for switch_controller/flow_tracking with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Configure sample mode for the flow tracking.
    sample_mode: Literal["local", "perimeter", "device-ingress"]
    # Configure sample rate for the perimeter and device-ingress sampling(0 - 99999).
    sample_rate: int
    # Configure flow tracking protocol.
    format: Literal["netflow1", "netflow5", "netflow9", "ipfix"]
    # Configure collectors for the flow.
    collectors: list[FlowTrackingCollectorsObject]  # Table field - list of typed objects
    # Configure flow tracking level.
    level: Literal["vlan", "ip", "port", "proto", "mac"]
    # Configure flow max export packet size (512-9216, default=512 bytes).
    max_export_pkt_size: int
    # Configure template export period (1-60, default=5 minutes).
    template_export_period: int
    # Configure flow session general timeout (60-604800, default=3600 seconds).
    timeout_general: int
    # Configure flow session ICMP timeout (60-604800, default=300 seconds).
    timeout_icmp: int
    # Configure flow session max timeout (60-604800, default=604800 seconds).
    timeout_max: int
    # Configure flow session TCP timeout (60-604800, default=3600 seconds).
    timeout_tcp: int
    # Configure flow session TCP FIN timeout (60-604800, default=300 seconds).
    timeout_tcp_fin: int
    # Configure flow session TCP RST timeout (60-604800, default=120 seconds).
    timeout_tcp_rst: int
    # Configure flow session UDP timeout (60-604800, default=300 seconds).
    timeout_udp: int
    # Configure aggregates in which all traffic sessions matching the IP Address will
    aggregates: list[FlowTrackingAggregatesObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FlowTrackingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class FlowTracking:
    """
    Configure FortiSwitch flow tracking and export via ipfix/netflow.
    
    Path: switch_controller/flow_tracking
    Category: cmdb
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
    ) -> FlowTrackingObject: ...
    
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
    ) -> FlowTrackingObject: ...
    
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
    ) -> FlowTrackingObject: ...
    
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
    ) -> FlowTrackingResponse: ...
    
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
    ) -> FlowTrackingResponse: ...
    
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
    ) -> FlowTrackingResponse: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> FlowTrackingObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FlowTrackingPayload | None = ...,
        sample_mode: Literal["local", "perimeter", "device-ingress"] | None = ...,
        sample_rate: int | None = ...,
        format: Literal["netflow1", "netflow5", "netflow9", "ipfix"] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        level: Literal["vlan", "ip", "port", "proto", "mac"] | None = ...,
        max_export_pkt_size: int | None = ...,
        template_export_period: int | None = ...,
        timeout_general: int | None = ...,
        timeout_icmp: int | None = ...,
        timeout_max: int | None = ...,
        timeout_tcp: int | None = ...,
        timeout_tcp_fin: int | None = ...,
        timeout_tcp_rst: int | None = ...,
        timeout_udp: int | None = ...,
        aggregates: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FlowTrackingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FlowTrackingPayload | None = ...,
        sample_mode: Literal["local", "perimeter", "device-ingress"] | None = ...,
        sample_rate: int | None = ...,
        format: Literal["netflow1", "netflow5", "netflow9", "ipfix"] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        level: Literal["vlan", "ip", "port", "proto", "mac"] | None = ...,
        max_export_pkt_size: int | None = ...,
        template_export_period: int | None = ...,
        timeout_general: int | None = ...,
        timeout_icmp: int | None = ...,
        timeout_max: int | None = ...,
        timeout_tcp: int | None = ...,
        timeout_tcp_fin: int | None = ...,
        timeout_tcp_rst: int | None = ...,
        timeout_udp: int | None = ...,
        aggregates: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: FlowTrackingPayload | None = ...,
        sample_mode: Literal["local", "perimeter", "device-ingress"] | None = ...,
        sample_rate: int | None = ...,
        format: Literal["netflow1", "netflow5", "netflow9", "ipfix"] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        level: Literal["vlan", "ip", "port", "proto", "mac"] | None = ...,
        max_export_pkt_size: int | None = ...,
        template_export_period: int | None = ...,
        timeout_general: int | None = ...,
        timeout_icmp: int | None = ...,
        timeout_max: int | None = ...,
        timeout_tcp: int | None = ...,
        timeout_tcp_fin: int | None = ...,
        timeout_tcp_rst: int | None = ...,
        timeout_udp: int | None = ...,
        aggregates: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: FlowTrackingPayload | None = ...,
        sample_mode: Literal["local", "perimeter", "device-ingress"] | None = ...,
        sample_rate: int | None = ...,
        format: Literal["netflow1", "netflow5", "netflow9", "ipfix"] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        level: Literal["vlan", "ip", "port", "proto", "mac"] | None = ...,
        max_export_pkt_size: int | None = ...,
        template_export_period: int | None = ...,
        timeout_general: int | None = ...,
        timeout_icmp: int | None = ...,
        timeout_max: int | None = ...,
        timeout_tcp: int | None = ...,
        timeout_tcp_fin: int | None = ...,
        timeout_tcp_rst: int | None = ...,
        timeout_udp: int | None = ...,
        aggregates: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FlowTrackingPayload | None = ...,
        sample_mode: Literal["local", "perimeter", "device-ingress"] | None = ...,
        sample_rate: int | None = ...,
        format: Literal["netflow1", "netflow5", "netflow9", "ipfix"] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        level: Literal["vlan", "ip", "port", "proto", "mac"] | None = ...,
        max_export_pkt_size: int | None = ...,
        template_export_period: int | None = ...,
        timeout_general: int | None = ...,
        timeout_icmp: int | None = ...,
        timeout_max: int | None = ...,
        timeout_tcp: int | None = ...,
        timeout_tcp_fin: int | None = ...,
        timeout_tcp_rst: int | None = ...,
        timeout_udp: int | None = ...,
        aggregates: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "FlowTracking",
    "FlowTrackingPayload",
    "FlowTrackingObject",
]