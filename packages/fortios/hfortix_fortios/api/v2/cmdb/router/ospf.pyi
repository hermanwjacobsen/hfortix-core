from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class OspfPayload(TypedDict, total=False):
    """
    Type hints for router/ospf payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: OspfPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    abr_type: NotRequired[Literal["cisco", "ibm", "shortcut", "standard"]]  # Area border router type.
    auto_cost_ref_bandwidth: NotRequired[int]  # Reference bandwidth in terms of megabits per second.
    distance_external: NotRequired[int]  # Administrative external distance.
    distance_inter_area: NotRequired[int]  # Administrative inter-area distance.
    distance_intra_area: NotRequired[int]  # Administrative intra-area distance.
    database_overflow: NotRequired[Literal["enable", "disable"]]  # Enable/disable database overflow.
    database_overflow_max_lsas: NotRequired[int]  # Database overflow maximum LSAs.
    database_overflow_time_to_recover: NotRequired[int]  # Database overflow time to recover (sec).
    default_information_originate: NotRequired[Literal["enable", "always", "disable"]]  # Enable/disable generation of default route.
    default_information_metric: NotRequired[int]  # Default information metric.
    default_information_metric_type: NotRequired[Literal["1", "2"]]  # Default information metric type.
    default_information_route_map: NotRequired[str]  # Default information route map.
    default_metric: NotRequired[int]  # Default metric of redistribute routes.
    distance: NotRequired[int]  # Distance of the route.
    lsa_refresh_interval: NotRequired[int]  # The minimal OSPF LSA update time interval
    rfc1583_compatible: NotRequired[Literal["enable", "disable"]]  # Enable/disable RFC1583 compatibility.
    router_id: str  # Router ID.
    spf_timers: NotRequired[str]  # SPF calculation frequency.
    bfd: NotRequired[Literal["enable", "disable"]]  # Bidirectional Forwarding Detection (BFD).
    log_neighbour_changes: NotRequired[Literal["enable", "disable"]]  # Log of OSPF neighbor changes.
    distribute_list_in: NotRequired[str]  # Filter incoming routes.
    distribute_route_map_in: NotRequired[str]  # Filter incoming external routes by route-map.
    restart_mode: NotRequired[Literal["none", "lls", "graceful-restart"]]  # OSPF restart mode (graceful or LLS).
    restart_period: NotRequired[int]  # Graceful restart period.
    restart_on_topology_change: NotRequired[Literal["enable", "disable"]]  # Enable/disable continuing graceful restart upon topology cha
    area: NotRequired[list[dict[str, Any]]]  # OSPF area configuration.
    ospf_interface: NotRequired[list[dict[str, Any]]]  # OSPF interface configuration.
    network: NotRequired[list[dict[str, Any]]]  # OSPF network configuration.
    neighbor: NotRequired[list[dict[str, Any]]]  # OSPF neighbor configuration are used when OSPF runs on non-b
    passive_interface: NotRequired[list[dict[str, Any]]]  # Passive interface configuration.
    summary_address: NotRequired[list[dict[str, Any]]]  # IP address summary configuration.
    distribute_list: NotRequired[list[dict[str, Any]]]  # Distribute list configuration.
    redistribute: NotRequired[list[dict[str, Any]]]  # Redistribute configuration.


class Ospf:
    """
    Configure OSPF.
    
    Path: router/ospf
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
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
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
        payload_dict: OspfPayload | None = ...,
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