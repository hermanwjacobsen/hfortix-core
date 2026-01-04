from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FlowTrackingPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/flow_tracking payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FlowTrackingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    sample_mode: NotRequired[Literal["local", "perimeter", "device-ingress"]]  # Configure sample mode for the flow tracking.
    sample_rate: NotRequired[int]  # Configure sample rate for the perimeter and device-ingress s
    format: NotRequired[Literal["netflow1", "netflow5", "netflow9", "ipfix"]]  # Configure flow tracking protocol.
    collectors: NotRequired[list[dict[str, Any]]]  # Configure collectors for the flow.
    level: NotRequired[Literal["vlan", "ip", "port", "proto", "mac"]]  # Configure flow tracking level.
    max_export_pkt_size: NotRequired[int]  # Configure flow max export packet size (512-9216, default=512
    template_export_period: NotRequired[int]  # Configure template export period (1-60, default=5 minutes).
    timeout_general: NotRequired[int]  # Configure flow session general timeout (60-604800, default=3
    timeout_icmp: NotRequired[int]  # Configure flow session ICMP timeout (60-604800, default=300 
    timeout_max: NotRequired[int]  # Configure flow session max timeout (60-604800, default=60480
    timeout_tcp: NotRequired[int]  # Configure flow session TCP timeout (60-604800, default=3600 
    timeout_tcp_fin: NotRequired[int]  # Configure flow session TCP FIN timeout (60-604800, default=3
    timeout_tcp_rst: NotRequired[int]  # Configure flow session TCP RST timeout (60-604800, default=1
    timeout_udp: NotRequired[int]  # Configure flow session UDP timeout (60-604800, default=300 s
    aggregates: NotRequired[list[dict[str, Any]]]  # Configure aggregates in which all traffic sessions matching 


class FlowTracking:
    """
    Configure FortiSwitch flow tracking and export via ipfix/netflow.
    
    Path: switch_controller/flow_tracking
    Category: cmdb
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def post(
        self,
        payload_dict: FlowTrackingPayload | None = ...,
        sample_mode: Literal["local", "perimeter", "device-ingress"] | None = ...,
        sample_rate: int | None = ...,
        format: Literal["netflow1", "netflow5", "netflow9", "ipfix"] | None = ...,
        collectors: list[dict[str, Any]] | None = ...,
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
        aggregates: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FlowTrackingPayload | None = ...,
        sample_mode: Literal["local", "perimeter", "device-ingress"] | None = ...,
        sample_rate: int | None = ...,
        format: Literal["netflow1", "netflow5", "netflow9", "ipfix"] | None = ...,
        collectors: list[dict[str, Any]] | None = ...,
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
        aggregates: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: FlowTrackingPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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