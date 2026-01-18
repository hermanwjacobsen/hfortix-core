""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: system/sdwan
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

class SdwanFailalertinterfacesItem(TypedDict, total=False):
    """Nested item for fail-alert-interfaces field."""
    name: str


class SdwanZoneItem(TypedDict, total=False):
    """Nested item for zone field."""
    name: str
    advpn_select: Literal["enable", "disable"]
    advpn_health_check: str
    service_sla_tie_break: Literal["cfg-order", "fib-best-match", "priority", "input-device"]
    minimum_sla_meet_members: int


class SdwanMembersItem(TypedDict, total=False):
    """Nested item for members field."""
    seq_num: int
    interface: str
    zone: str
    gateway: str
    preferred_source: str
    source: str
    gateway6: str
    source6: str
    cost: int
    weight: int
    priority: int
    priority6: int
    priority_in_sla: int
    priority_out_sla: int
    spillover_threshold: int
    ingress_spillover_threshold: int
    volume_ratio: int
    status: Literal["disable", "enable"]
    transport_group: int
    comment: str


class SdwanHealthcheckItem(TypedDict, total=False):
    """Nested item for health-check field."""
    name: str
    fortiguard: Literal["disable", "enable"]
    fortiguard_name: str
    probe_packets: Literal["disable", "enable"]
    addr_mode: Literal["ipv4", "ipv6"]
    system_dns: Literal["disable", "enable"]
    server: str | list[str]
    detect_mode: Literal["active", "passive", "prefer-passive", "remote", "agent-based"]
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"]
    port: int
    quality_measured_method: Literal["half-open", "half-close"]
    security_mode: Literal["none", "authentication"]
    user: str
    password: str
    packet_size: int
    ha_priority: int
    ftp_mode: Literal["passive", "port"]
    ftp_file: str
    http_get: str
    http_agent: str
    http_match: str
    dns_request_domain: str
    dns_match_ip: str
    interval: int
    probe_timeout: int
    agent_probe_timeout: int
    remote_probe_timeout: int
    failtime: int
    recoverytime: int
    probe_count: int
    diffservcode: str
    update_cascade_interface: Literal["enable", "disable"]
    update_static_route: Literal["enable", "disable"]
    update_bgp_route: Literal["enable", "disable"]
    embed_measured_health: Literal["enable", "disable"]
    sla_id_redistribute: int
    sla_fail_log_period: int
    sla_pass_log_period: int
    threshold_warning_packetloss: int
    threshold_alert_packetloss: int
    threshold_warning_latency: int
    threshold_alert_latency: int
    threshold_warning_jitter: int
    threshold_alert_jitter: int
    vrf: int
    source: str
    source6: str
    members: str | list[str]
    mos_codec: Literal["g711", "g722", "g729"]
    class_id: int
    packet_loss_weight: int
    latency_weight: int
    jitter_weight: int
    bandwidth_weight: int
    sla: str | list[str]


class SdwanServiceItem(TypedDict, total=False):
    """Nested item for service field."""
    id: int
    name: str
    addr_mode: Literal["ipv4", "ipv6"]
    load_balance: Literal["enable", "disable"]
    input_device: str | list[str]
    input_device_negate: Literal["enable", "disable"]
    input_zone: str | list[str]
    mode: Literal["auto", "manual", "priority", "sla"]
    zone_mode: Literal["enable", "disable"]
    minimum_sla_meet_members: int
    hash_mode: Literal["round-robin", "source-ip-based", "source-dest-ip-based", "inbandwidth", "outbandwidth", "bibandwidth"]
    shortcut_priority: Literal["enable", "disable", "auto"]
    role: Literal["standalone", "primary", "secondary"]
    standalone_action: Literal["enable", "disable"]
    quality_link: int
    tos: str
    tos_mask: str
    protocol: int
    start_port: int
    end_port: int
    start_src_port: int
    end_src_port: int
    dst: str | list[str]
    dst_negate: Literal["enable", "disable"]
    src: str | list[str]
    dst6: str | list[str]
    src6: str | list[str]
    src_negate: Literal["enable", "disable"]
    users: str | list[str]
    groups: str | list[str]
    internet_service: Literal["enable", "disable"]
    internet_service_custom: str | list[str]
    internet_service_custom_group: str | list[str]
    internet_service_fortiguard: str | list[str]
    internet_service_name: str | list[str]
    internet_service_group: str | list[str]
    internet_service_app_ctrl: str | list[str]
    internet_service_app_ctrl_group: str | list[str]
    internet_service_app_ctrl_category: str | list[str]
    health_check: str | list[str]
    link_cost_factor: Literal["latency", "jitter", "packet-loss", "inbandwidth", "outbandwidth", "bibandwidth", "custom-profile-1"]
    packet_loss_weight: int
    latency_weight: int
    jitter_weight: int
    bandwidth_weight: int
    link_cost_threshold: int
    hold_down_time: int
    sla_stickiness: Literal["enable", "disable"]
    dscp_forward: Literal["enable", "disable"]
    dscp_reverse: Literal["enable", "disable"]
    dscp_forward_tag: str
    dscp_reverse_tag: str
    sla: str | list[str]
    priority_members: str | list[str]
    priority_zone: str | list[str]
    status: Literal["enable", "disable"]
    gateway: Literal["enable", "disable"]
    default: Literal["enable", "disable"]
    sla_compare_method: Literal["order", "number"]
    fib_best_match_force: Literal["disable", "enable"]
    tie_break: Literal["zone", "cfg-order", "fib-best-match", "priority", "input-device"]
    use_shortcut_sla: Literal["enable", "disable"]
    passive_measurement: Literal["enable", "disable"]
    agent_exclusive: Literal["enable", "disable"]
    shortcut: Literal["enable", "disable"]
    comment: str


class SdwanNeighborItem(TypedDict, total=False):
    """Nested item for neighbor field."""
    ip: str
    member: str | list[str]
    service_id: int
    minimum_sla_meet_members: int
    mode: Literal["sla", "speedtest"]
    role: Literal["standalone", "primary", "secondary"]
    route_metric: Literal["preferable", "priority"]
    health_check: str
    sla_id: int


class SdwanDuplicationItem(TypedDict, total=False):
    """Nested item for duplication field."""
    id: int
    service_id: str | list[str]
    srcaddr: str | list[str]
    dstaddr: str | list[str]
    srcaddr6: str | list[str]
    dstaddr6: str | list[str]
    srcintf: str | list[str]
    dstintf: str | list[str]
    service: str | list[str]
    packet_duplication: Literal["disable", "force", "on-demand"]
    sla_match_service: Literal["enable", "disable"]
    packet_de_duplication: Literal["enable", "disable"]


class SdwanPayload(TypedDict, total=False):
    """Payload type for Sdwan operations."""
    status: Literal["disable", "enable"]
    load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"]
    speedtest_bypass_routing: Literal["disable", "enable"]
    duplication_max_num: int
    duplication_max_discrepancy: int
    neighbor_hold_down: Literal["enable", "disable"]
    neighbor_hold_down_time: int
    app_perf_log_period: int
    neighbor_hold_boot_time: int
    fail_detect: Literal["enable", "disable"]
    fail_alert_interfaces: str | list[str] | list[SdwanFailalertinterfacesItem]
    zone: str | list[str] | list[SdwanZoneItem]
    members: str | list[str] | list[SdwanMembersItem]
    health_check: str | list[str] | list[SdwanHealthcheckItem]
    service: str | list[str] | list[SdwanServiceItem]
    neighbor: str | list[str] | list[SdwanNeighborItem]
    duplication: str | list[str] | list[SdwanDuplicationItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class SdwanResponse(TypedDict, total=False):
    """Response type for Sdwan - use with .dict property for typed dict access."""
    status: Literal["disable", "enable"]
    load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"]
    speedtest_bypass_routing: Literal["disable", "enable"]
    duplication_max_num: int
    duplication_max_discrepancy: int
    neighbor_hold_down: Literal["enable", "disable"]
    neighbor_hold_down_time: int
    app_perf_log_period: int
    neighbor_hold_boot_time: int
    fail_detect: Literal["enable", "disable"]
    fail_alert_interfaces: list[SdwanFailalertinterfacesItem]
    zone: list[SdwanZoneItem]
    members: list[SdwanMembersItem]
    health_check: list[SdwanHealthcheckItem]
    service: list[SdwanServiceItem]
    neighbor: list[SdwanNeighborItem]
    duplication: list[SdwanDuplicationItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class SdwanObject(FortiObject):
    """Typed FortiObject for Sdwan with field access."""
    status: Literal["disable", "enable"]
    load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"]
    speedtest_bypass_routing: Literal["disable", "enable"]
    duplication_max_num: int
    duplication_max_discrepancy: int
    neighbor_hold_down: Literal["enable", "disable"]
    neighbor_hold_down_time: int
    app_perf_log_period: int
    neighbor_hold_boot_time: int
    fail_detect: Literal["enable", "disable"]
    fail_alert_interfaces: list[SdwanFailalertinterfacesItem]
    zone: list[SdwanZoneItem]
    members: list[SdwanMembersItem]
    health_check: list[SdwanHealthcheckItem]
    service: list[SdwanServiceItem]
    neighbor: list[SdwanNeighborItem]
    duplication: list[SdwanDuplicationItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class Sdwan:
    """
    
    Endpoint: system/sdwan
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
    ) -> SdwanObject: ...
    
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
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[SdwanFailalertinterfacesItem] | None = ...,
        zone: str | list[str] | list[SdwanZoneItem] | None = ...,
        members: str | list[str] | list[SdwanMembersItem] | None = ...,
        health_check: str | list[str] | list[SdwanHealthcheckItem] | None = ...,
        service: str | list[str] | list[SdwanServiceItem] | None = ...,
        neighbor: str | list[str] | list[SdwanNeighborItem] | None = ...,
        duplication: str | list[str] | list[SdwanDuplicationItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> SdwanObject: ...


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
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[SdwanFailalertinterfacesItem] | None = ...,
        zone: str | list[str] | list[SdwanZoneItem] | None = ...,
        members: str | list[str] | list[SdwanMembersItem] | None = ...,
        health_check: str | list[str] | list[SdwanHealthcheckItem] | None = ...,
        service: str | list[str] | list[SdwanServiceItem] | None = ...,
        neighbor: str | list[str] | list[SdwanNeighborItem] | None = ...,
        duplication: str | list[str] | list[SdwanDuplicationItem] | None = ...,
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
    "Sdwan",
    "SdwanPayload",
    "SdwanResponse",
    "SdwanObject",
]