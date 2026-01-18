""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: router/multicast
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

class MulticastPimsmglobalDict(TypedDict, total=False):
    """Nested object type for pim-sm-global field."""
    message_interval: int
    join_prune_holdtime: int
    accept_register_list: str
    accept_source_list: str
    bsr_candidate: Literal["enable", "disable"]
    bsr_interface: str
    bsr_priority: int
    bsr_hash: int
    bsr_allow_quick_refresh: Literal["enable", "disable"]
    cisco_crp_prefix: Literal["enable", "disable"]
    cisco_register_checksum: Literal["enable", "disable"]
    cisco_register_checksum_group: str
    cisco_ignore_rp_set_priority: Literal["enable", "disable"]
    register_rp_reachability: Literal["enable", "disable"]
    register_source: Literal["disable", "interface", "ip-address"]
    register_source_interface: str
    register_source_ip: str
    register_supression: int
    null_register_retries: int
    rp_register_keepalive: int
    spt_threshold: Literal["enable", "disable"]
    spt_threshold_group: str
    ssm: Literal["enable", "disable"]
    ssm_range: str
    register_rate_limit: int
    pim_use_sdwan: Literal["enable", "disable"]
    rp_address: str | list[str]


class MulticastPimsmglobalvrfItem(TypedDict, total=False):
    """Nested item for pim-sm-global-vrf field."""
    vrf: int
    bsr_candidate: Literal["enable", "disable"]
    bsr_interface: str
    bsr_priority: int
    bsr_hash: int
    bsr_allow_quick_refresh: Literal["enable", "disable"]
    cisco_crp_prefix: Literal["enable", "disable"]
    rp_address: str | list[str]


class MulticastInterfaceItem(TypedDict, total=False):
    """Nested item for interface field."""
    name: str
    ttl_threshold: int
    pim_mode: Literal["sparse-mode", "dense-mode"]
    passive: Literal["enable", "disable"]
    bfd: Literal["enable", "disable"]
    neighbour_filter: str
    hello_interval: int
    hello_holdtime: int
    cisco_exclude_genid: Literal["enable", "disable"]
    dr_priority: int
    propagation_delay: int
    state_refresh_interval: int
    rp_candidate: Literal["enable", "disable"]
    rp_candidate_group: str
    rp_candidate_priority: int
    rp_candidate_interval: int
    multicast_flow: str
    static_group: str
    rpf_nbr_fail_back: Literal["enable", "disable"]
    rpf_nbr_fail_back_filter: str
    join_group: str | list[str]
    igmp: str


class MulticastPayload(TypedDict, total=False):
    """Payload type for Multicast operations."""
    route_threshold: int
    route_limit: int
    multicast_routing: Literal["enable", "disable"]
    pim_sm_global: MulticastPimsmglobalDict
    pim_sm_global_vrf: str | list[str] | list[MulticastPimsmglobalvrfItem]
    interface: str | list[str] | list[MulticastInterfaceItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class MulticastResponse(TypedDict, total=False):
    """Response type for Multicast - use with .dict property for typed dict access."""
    route_threshold: int
    route_limit: int
    multicast_routing: Literal["enable", "disable"]
    pim_sm_global: MulticastPimsmglobalDict
    pim_sm_global_vrf: list[MulticastPimsmglobalvrfItem]
    interface: list[MulticastInterfaceItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class MulticastPimsmglobalObject(FortiObject):
    """Nested object for pim-sm-global field with attribute access."""
    message_interval: int
    join_prune_holdtime: int
    accept_register_list: str
    accept_source_list: str
    bsr_candidate: Literal["enable", "disable"]
    bsr_interface: str
    bsr_priority: int
    bsr_hash: int
    bsr_allow_quick_refresh: Literal["enable", "disable"]
    cisco_crp_prefix: Literal["enable", "disable"]
    cisco_register_checksum: Literal["enable", "disable"]
    cisco_register_checksum_group: str
    cisco_ignore_rp_set_priority: Literal["enable", "disable"]
    register_rp_reachability: Literal["enable", "disable"]
    register_source: Literal["disable", "interface", "ip-address"]
    register_source_interface: str
    register_source_ip: str
    register_supression: int
    null_register_retries: int
    rp_register_keepalive: int
    spt_threshold: Literal["enable", "disable"]
    spt_threshold_group: str
    ssm: Literal["enable", "disable"]
    ssm_range: str
    register_rate_limit: int
    pim_use_sdwan: Literal["enable", "disable"]
    rp_address: str | list[str]


class MulticastObject(FortiObject):
    """Typed FortiObject for Multicast with field access."""
    route_threshold: int
    route_limit: int
    multicast_routing: Literal["enable", "disable"]
    pim_sm_global: MulticastPimsmglobalObject
    pim_sm_global_vrf: list[MulticastPimsmglobalvrfItem]
    interface: list[MulticastInterfaceItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class Multicast:
    """
    
    Endpoint: router/multicast
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
    ) -> MulticastObject: ...
    
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
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: MulticastPimsmglobalDict | None = ...,
        pim_sm_global_vrf: str | list[str] | list[MulticastPimsmglobalvrfItem] | None = ...,
        interface: str | list[str] | list[MulticastInterfaceItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> MulticastObject: ...


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
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: MulticastPimsmglobalDict | None = ...,
        pim_sm_global_vrf: str | list[str] | list[MulticastPimsmglobalvrfItem] | None = ...,
        interface: str | list[str] | list[MulticastInterfaceItem] | None = ...,
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
    "Multicast",
    "MulticastPayload",
    "MulticastResponse",
    "MulticastObject",
]