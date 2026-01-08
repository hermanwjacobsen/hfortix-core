from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class Ospf6Payload(TypedDict, total=False):
    """
    Type hints for router/ospf6 payload fields.
    
    Configure IPv6 OSPF.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.router.route-map.RouteMapEndpoint` (via: default-information-route-map)

    **Usage:**
        payload: Ospf6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    abr_type: NotRequired[Literal["cisco", "ibm", "standard"]]  # Area border router type.
    auto_cost_ref_bandwidth: NotRequired[int]  # Reference bandwidth in terms of megabits per second.
    default_information_originate: NotRequired[Literal["enable", "always", "disable"]]  # Enable/disable generation of default route.
    log_neighbour_changes: NotRequired[Literal["enable", "disable"]]  # Log OSPFv3 neighbor changes.
    default_information_metric: NotRequired[int]  # Default information metric.
    default_information_metric_type: NotRequired[Literal["1", "2"]]  # Default information metric type.
    default_information_route_map: NotRequired[str]  # Default information route map.
    default_metric: NotRequired[int]  # Default metric of redistribute routes.
    router_id: str  # A.B.C.D, in IPv4 address format.
    spf_timers: NotRequired[str]  # SPF calculation frequency.
    bfd: NotRequired[Literal["enable", "disable"]]  # Enable/disable Bidirectional Forwarding Detection (BFD).
    restart_mode: NotRequired[Literal["none", "graceful-restart"]]  # OSPFv3 restart mode (graceful or none).
    restart_period: NotRequired[int]  # Graceful restart period in seconds.
    restart_on_topology_change: NotRequired[Literal["enable", "disable"]]  # Enable/disable continuing graceful restart upon topology cha
    area: NotRequired[list[dict[str, Any]]]  # OSPF6 area configuration.
    ospf6_interface: NotRequired[list[dict[str, Any]]]  # OSPF6 interface configuration.
    redistribute: NotRequired[list[dict[str, Any]]]  # Redistribute configuration.
    passive_interface: NotRequired[list[dict[str, Any]]]  # Passive interface configuration.
    summary_address: NotRequired[list[dict[str, Any]]]  # IPv6 address summary configuration.


class Ospf6Object(FortiObject[Ospf6Payload]):
    """Typed FortiObject for router/ospf6 with IDE autocomplete support."""
    
    # Area border router type.
    abr_type: Literal["cisco", "ibm", "standard"]
    # Reference bandwidth in terms of megabits per second.
    auto_cost_ref_bandwidth: int
    # Enable/disable generation of default route.
    default_information_originate: Literal["enable", "always", "disable"]
    # Log OSPFv3 neighbor changes.
    log_neighbour_changes: Literal["enable", "disable"]
    # Default information metric.
    default_information_metric: int
    # Default information metric type.
    default_information_metric_type: Literal["1", "2"]
    # Default information route map.
    default_information_route_map: str
    # Default metric of redistribute routes.
    default_metric: int
    # A.B.C.D, in IPv4 address format.
    router_id: str
    # SPF calculation frequency.
    spf_timers: str
    # Enable/disable Bidirectional Forwarding Detection (BFD).
    bfd: Literal["enable", "disable"]
    # OSPFv3 restart mode (graceful or none).
    restart_mode: Literal["none", "graceful-restart"]
    # Graceful restart period in seconds.
    restart_period: int
    # Enable/disable continuing graceful restart upon topology change.
    restart_on_topology_change: Literal["enable", "disable"]
    # OSPF6 area configuration.
    area: list[str]  # Auto-flattened from member_table
    # OSPF6 interface configuration.
    ospf6_interface: list[str]  # Auto-flattened from member_table
    # Redistribute configuration.
    redistribute: list[str]  # Auto-flattened from member_table
    # Passive interface configuration.
    passive_interface: list[str]  # Auto-flattened from member_table
    # IPv6 address summary configuration.
    summary_address: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> Ospf6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ospf6:
    """
    Configure IPv6 OSPF.
    
    Path: router/ospf6
    Category: cmdb
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Ospf6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Ospf6",
    "Ospf6Payload",
    "Ospf6Object",
]