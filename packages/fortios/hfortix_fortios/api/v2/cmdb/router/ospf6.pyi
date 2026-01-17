""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: router/ospf6
Category: cmdb
"""

from __future__ import annotations

from typing import (
    Any,
    ClassVar,
    Literal,
    TypedDict,
)

from hfortix_fortios.models import (
    FortiObject,
    FortiObjectList,
)


# ================================================================
# TypedDict Payloads
# ================================================================

class Ospf6AreaItem:
    """Nested item for area field - supports attribute access."""
    id: str
    default_cost: int
    nssa_translator_role: Literal["candidate", "never", "always"]
    stub_type: Literal["no-summary", "summary"]
    type: Literal["regular", "nssa", "stub"]
    nssa_default_information_originate: Literal["enable", "disable"]
    nssa_default_information_originate_metric: int
    nssa_default_information_originate_metric_type: Literal["1", "2"]
    nssa_redistribution: Literal["enable", "disable"]
    authentication: Literal["none", "ah", "esp"]
    key_rollover_interval: int
    ipsec_auth_alg: Literal["md5", "sha1", "sha256", "sha384", "sha512"]
    ipsec_enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256"]
    ipsec_keys: str | list[str]
    range: str | list[str]
    virtual_link: str | list[str]


class Ospf6Ospf6interfaceItem:
    """Nested item for ospf6-interface field - supports attribute access."""
    name: str
    area_id: str
    interface: str
    retransmit_interval: int
    transmit_delay: int
    cost: int
    priority: int
    dead_interval: int
    hello_interval: int
    status: Literal["disable", "enable"]
    network_type: Literal["broadcast", "point-to-point", "non-broadcast", "point-to-multipoint", "point-to-multipoint-non-broadcast"]
    bfd: Literal["global", "enable", "disable"]
    mtu: int
    mtu_ignore: Literal["enable", "disable"]
    authentication: Literal["none", "ah", "esp", "area"]
    key_rollover_interval: int
    ipsec_auth_alg: Literal["md5", "sha1", "sha256", "sha384", "sha512"]
    ipsec_enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256"]
    ipsec_keys: str | list[str]
    neighbor: str | list[str]


class Ospf6RedistributeItem:
    """Nested item for redistribute field - supports attribute access."""
    name: str
    status: Literal["enable", "disable"]
    metric: int
    routemap: str
    metric_type: Literal["1", "2"]


class Ospf6PassiveinterfaceItem:
    """Nested item for passive-interface field - supports attribute access."""
    name: str


class Ospf6SummaryaddressItem:
    """Nested item for summary-address field - supports attribute access."""
    id: int
    prefix6: str
    advertise: Literal["disable", "enable"]
    tag: int


class Ospf6Payload(TypedDict, total=False):
    """Payload type for Ospf6 operations."""
    abr_type: Literal["cisco", "ibm", "standard"]
    auto_cost_ref_bandwidth: int
    default_information_originate: Literal["enable", "always", "disable"]
    log_neighbour_changes: Literal["enable", "disable"]
    default_information_metric: int
    default_information_metric_type: Literal["1", "2"]
    default_information_route_map: str
    default_metric: int
    router_id: str
    spf_timers: str
    bfd: Literal["enable", "disable"]
    restart_mode: Literal["none", "graceful-restart"]
    restart_period: int
    restart_on_topology_change: Literal["enable", "disable"]
    area: str | list[str] | list[dict[str, Any]] | list[Ospf6AreaItem]
    ospf6_interface: str | list[str] | list[dict[str, Any]] | list[Ospf6Ospf6interfaceItem]
    redistribute: str | list[str] | list[dict[str, Any]] | list[Ospf6RedistributeItem]
    passive_interface: str | list[str] | list[dict[str, Any]] | list[Ospf6PassiveinterfaceItem]
    summary_address: str | list[str] | list[dict[str, Any]] | list[Ospf6SummaryaddressItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class Ospf6Response(TypedDict, total=False):
    """Response type for Ospf6 - use with .dict property for typed dict access."""
    abr_type: Literal["cisco", "ibm", "standard"]
    auto_cost_ref_bandwidth: int
    default_information_originate: Literal["enable", "always", "disable"]
    log_neighbour_changes: Literal["enable", "disable"]
    default_information_metric: int
    default_information_metric_type: Literal["1", "2"]
    default_information_route_map: str
    default_metric: int
    router_id: str
    spf_timers: str
    bfd: Literal["enable", "disable"]
    restart_mode: Literal["none", "graceful-restart"]
    restart_period: int
    restart_on_topology_change: Literal["enable", "disable"]
    area: list[Ospf6AreaItem]
    ospf6_interface: list[Ospf6Ospf6interfaceItem]
    redistribute: list[Ospf6RedistributeItem]
    passive_interface: list[Ospf6PassiveinterfaceItem]
    summary_address: list[Ospf6SummaryaddressItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class Ospf6Object(FortiObject):
    """Typed FortiObject for Ospf6 with field access."""
    abr_type: Literal["cisco", "ibm", "standard"]
    auto_cost_ref_bandwidth: int
    default_information_originate: Literal["enable", "always", "disable"]
    log_neighbour_changes: Literal["enable", "disable"]
    default_information_metric: int
    default_information_metric_type: Literal["1", "2"]
    default_information_route_map: str
    default_metric: int
    router_id: str
    spf_timers: str
    bfd: Literal["enable", "disable"]
    restart_mode: Literal["none", "graceful-restart"]
    restart_period: int
    restart_on_topology_change: Literal["enable", "disable"]
    area: list[Ospf6AreaItem]
    ospf6_interface: list[Ospf6Ospf6interfaceItem]
    redistribute: list[Ospf6RedistributeItem]
    passive_interface: list[Ospf6PassiveinterfaceItem]
    summary_address: list[Ospf6SummaryaddressItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class Ospf6:
    """
    
    Endpoint: router/ospf6
    Category: cmdb
    """
    
    # Class attributes for introspection
    endpoint: ClassVar[str] = ...
    path: ClassVar[str] = ...
    category: ClassVar[str] = ...
    capabilities: ClassVar[dict[str, Any]] = ...
    
    def __init__(self, client: Any) -> None:
        """Initialize endpoint with HTTP client."""
        ...
    
    # ================================================================
    # GET Methods
    # ================================================================
    
    # Singleton endpoint (no mkey)
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> Ospf6Object: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...


    # ================================================================
    # PUT Method
    # ================================================================
    
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
        area: str | list[str] | list[dict[str, Any]] | list[Ospf6AreaItem] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | list[Ospf6Ospf6interfaceItem] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | list[Ospf6RedistributeItem] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | list[Ospf6PassiveinterfaceItem] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | list[Ospf6SummaryaddressItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> Ospf6Object: ...


    # ================================================================
    # Utility Methods
    # ================================================================
    
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
        area: str | list[str] | list[dict[str, Any]] | list[Ospf6AreaItem] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | list[Ospf6Ospf6interfaceItem] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | list[Ospf6RedistributeItem] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | list[Ospf6PassiveinterfaceItem] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | list[Ospf6SummaryaddressItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> list[str] | list[dict[str, Any]]: ...
    
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


__all__ = [
    "Ospf6",
    "Ospf6Payload",
    "Ospf6Response",
    "Ospf6Object",
]