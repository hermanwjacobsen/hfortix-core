from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Ospf6Payload(TypedDict, total=False):
    """
    Type hints for router/ospf6 payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Ospf6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    abr_type: NotRequired[Literal[{"description": "Cisco", "help": "Cisco.", "label": "Cisco", "name": "cisco"}, {"description": "IBM", "help": "IBM.", "label": "Ibm", "name": "ibm"}, {"description": "Standard", "help": "Standard.", "label": "Standard", "name": "standard"}]]  # Area border router type.
    auto_cost_ref_bandwidth: NotRequired[int]  # Reference bandwidth in terms of megabits per second.
    default_information_originate: NotRequired[Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Always advertise the default router", "help": "Always advertise the default router.", "label": "Always", "name": "always"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}]]  # Enable/disable generation of default route.
    log_neighbour_changes: NotRequired[Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}]]  # Log OSPFv3 neighbor changes.
    default_information_metric: NotRequired[int]  # Default information metric.
    default_information_metric_type: NotRequired[Literal[{"description": "Type 1", "help": "Type 1.", "label": "1", "name": "1"}, {"description": "Type 2", "help": "Type 2.", "label": "2", "name": "2"}]]  # Default information metric type.
    default_information_route_map: NotRequired[str]  # Default information route map.
    default_metric: NotRequired[int]  # Default metric of redistribute routes.
    router_id: str  # A.B.C.D, in IPv4 address format.
    spf_timers: NotRequired[str]  # SPF calculation frequency.
    bfd: NotRequired[Literal[{"description": "Enable Bidirectional Forwarding Detection (BFD)", "help": "Enable Bidirectional Forwarding Detection (BFD).", "label": "Enable", "name": "enable"}, {"description": "Disable Bidirectional Forwarding Detection (BFD)", "help": "Disable Bidirectional Forwarding Detection (BFD).", "label": "Disable", "name": "disable"}]]  # Enable/disable Bidirectional Forwarding Detection (BFD).
    restart_mode: NotRequired[Literal[{"description": "Disable hitless restart", "help": "Disable hitless restart.", "label": "None", "name": "none"}, {"description": "Enable graceful restart mode", "help": "Enable graceful restart mode.", "label": "Graceful Restart", "name": "graceful-restart"}]]  # OSPFv3 restart mode (graceful or none).
    restart_period: NotRequired[int]  # Graceful restart period in seconds.
    restart_on_topology_change: NotRequired[Literal[{"description": "Continue graceful restart upon topology change", "help": "Continue graceful restart upon topology change.", "label": "Enable", "name": "enable"}, {"description": "Exit graceful restart upon topology change", "help": "Exit graceful restart upon topology change.", "label": "Disable", "name": "disable"}]]  # Enable/disable continuing graceful restart upon topology cha
    area: NotRequired[list[dict[str, Any]]]  # OSPF6 area configuration.
    ospf6_interface: NotRequired[list[dict[str, Any]]]  # OSPF6 interface configuration.
    redistribute: NotRequired[list[dict[str, Any]]]  # Redistribute configuration.
    passive_interface: NotRequired[list[dict[str, Any]]]  # Passive interface configuration.
    summary_address: NotRequired[list[dict[str, Any]]]  # IPv6 address summary configuration.


class Ospf6:
    """
    Configure IPv6 OSPF.
    
    Path: router/ospf6
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
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal[{"description": "Cisco", "help": "Cisco.", "label": "Cisco", "name": "cisco"}, {"description": "IBM", "help": "IBM.", "label": "Ibm", "name": "ibm"}, {"description": "Standard", "help": "Standard.", "label": "Standard", "name": "standard"}] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Always advertise the default router", "help": "Always advertise the default router.", "label": "Always", "name": "always"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}] | None = ...,
        log_neighbour_changes: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal[{"description": "Type 1", "help": "Type 1.", "label": "1", "name": "1"}, {"description": "Type 2", "help": "Type 2.", "label": "2", "name": "2"}] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal[{"description": "Enable Bidirectional Forwarding Detection (BFD)", "help": "Enable Bidirectional Forwarding Detection (BFD).", "label": "Enable", "name": "enable"}, {"description": "Disable Bidirectional Forwarding Detection (BFD)", "help": "Disable Bidirectional Forwarding Detection (BFD).", "label": "Disable", "name": "disable"}] | None = ...,
        restart_mode: Literal[{"description": "Disable hitless restart", "help": "Disable hitless restart.", "label": "None", "name": "none"}, {"description": "Enable graceful restart mode", "help": "Enable graceful restart mode.", "label": "Graceful Restart", "name": "graceful-restart"}] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal[{"description": "Continue graceful restart upon topology change", "help": "Continue graceful restart upon topology change.", "label": "Enable", "name": "enable"}, {"description": "Exit graceful restart upon topology change", "help": "Exit graceful restart upon topology change.", "label": "Disable", "name": "disable"}] | None = ...,
        area: list[dict[str, Any]] | None = ...,
        ospf6_interface: list[dict[str, Any]] | None = ...,
        redistribute: list[dict[str, Any]] | None = ...,
        passive_interface: list[dict[str, Any]] | None = ...,
        summary_address: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal[{"description": "Cisco", "help": "Cisco.", "label": "Cisco", "name": "cisco"}, {"description": "IBM", "help": "IBM.", "label": "Ibm", "name": "ibm"}, {"description": "Standard", "help": "Standard.", "label": "Standard", "name": "standard"}] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Always advertise the default router", "help": "Always advertise the default router.", "label": "Always", "name": "always"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}] | None = ...,
        log_neighbour_changes: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal[{"description": "Type 1", "help": "Type 1.", "label": "1", "name": "1"}, {"description": "Type 2", "help": "Type 2.", "label": "2", "name": "2"}] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal[{"description": "Enable Bidirectional Forwarding Detection (BFD)", "help": "Enable Bidirectional Forwarding Detection (BFD).", "label": "Enable", "name": "enable"}, {"description": "Disable Bidirectional Forwarding Detection (BFD)", "help": "Disable Bidirectional Forwarding Detection (BFD).", "label": "Disable", "name": "disable"}] | None = ...,
        restart_mode: Literal[{"description": "Disable hitless restart", "help": "Disable hitless restart.", "label": "None", "name": "none"}, {"description": "Enable graceful restart mode", "help": "Enable graceful restart mode.", "label": "Graceful Restart", "name": "graceful-restart"}] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal[{"description": "Continue graceful restart upon topology change", "help": "Continue graceful restart upon topology change.", "label": "Enable", "name": "enable"}, {"description": "Exit graceful restart upon topology change", "help": "Exit graceful restart upon topology change.", "label": "Disable", "name": "disable"}] | None = ...,
        area: list[dict[str, Any]] | None = ...,
        ospf6_interface: list[dict[str, Any]] | None = ...,
        redistribute: list[dict[str, Any]] | None = ...,
        passive_interface: list[dict[str, Any]] | None = ...,
        summary_address: list[dict[str, Any]] | None = ...,
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
        payload_dict: Ospf6Payload | None = ...,
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


__all__ = [
    "Ospf6",
    "Ospf6Payload",
]