""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: router/ripng
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

class RipngDistanceItem:
    """Nested item for distance field - supports attribute access."""
    id: int
    distance: int
    prefix6: str
    access_list6: str


class RipngDistributelistItem:
    """Nested item for distribute-list field - supports attribute access."""
    id: int
    status: Literal["enable", "disable"]
    direction: Literal["in", "out"]
    listname: str
    interface: str


class RipngNeighborItem:
    """Nested item for neighbor field - supports attribute access."""
    id: int
    ip6: str
    interface: str


class RipngNetworkItem:
    """Nested item for network field - supports attribute access."""
    id: int
    prefix: str


class RipngAggregateaddressItem:
    """Nested item for aggregate-address field - supports attribute access."""
    id: int
    prefix6: str


class RipngOffsetlistItem:
    """Nested item for offset-list field - supports attribute access."""
    id: int
    status: Literal["enable", "disable"]
    direction: Literal["in", "out"]
    access_list6: str
    offset: int
    interface: str


class RipngPassiveinterfaceItem:
    """Nested item for passive-interface field - supports attribute access."""
    name: str


class RipngRedistributeItem:
    """Nested item for redistribute field - supports attribute access."""
    name: str
    status: Literal["enable", "disable"]
    metric: int
    routemap: str


class RipngInterfaceItem:
    """Nested item for interface field - supports attribute access."""
    name: str
    split_horizon_status: Literal["enable", "disable"]
    split_horizon: Literal["poisoned", "regular"]
    flags: int


class RipngPayload(TypedDict, total=False):
    """Payload type for Ripng operations."""
    default_information_originate: Literal["enable", "disable"]
    default_metric: int
    max_out_metric: int
    distance: str | list[str] | list[dict[str, Any]] | list[RipngDistanceItem]
    distribute_list: str | list[str] | list[dict[str, Any]] | list[RipngDistributelistItem]
    neighbor: str | list[str] | list[dict[str, Any]] | list[RipngNeighborItem]
    network: str | list[str] | list[dict[str, Any]] | list[RipngNetworkItem]
    aggregate_address: str | list[str] | list[dict[str, Any]] | list[RipngAggregateaddressItem]
    offset_list: str | list[str] | list[dict[str, Any]] | list[RipngOffsetlistItem]
    passive_interface: str | list[str] | list[dict[str, Any]] | list[RipngPassiveinterfaceItem]
    redistribute: str | list[str] | list[dict[str, Any]] | list[RipngRedistributeItem]
    update_timer: int
    timeout_timer: int
    garbage_timer: int
    interface: str | list[str] | list[dict[str, Any]] | list[RipngInterfaceItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class RipngResponse(TypedDict, total=False):
    """Response type for Ripng - use with .dict property for typed dict access."""
    default_information_originate: Literal["enable", "disable"]
    default_metric: int
    max_out_metric: int
    distance: list[RipngDistanceItem]
    distribute_list: list[RipngDistributelistItem]
    neighbor: list[RipngNeighborItem]
    network: list[RipngNetworkItem]
    aggregate_address: list[RipngAggregateaddressItem]
    offset_list: list[RipngOffsetlistItem]
    passive_interface: list[RipngPassiveinterfaceItem]
    redistribute: list[RipngRedistributeItem]
    update_timer: int
    timeout_timer: int
    garbage_timer: int
    interface: list[RipngInterfaceItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class RipngObject(FortiObject):
    """Typed FortiObject for Ripng with field access."""
    default_information_originate: Literal["enable", "disable"]
    default_metric: int
    max_out_metric: int
    distance: list[RipngDistanceItem]
    distribute_list: list[RipngDistributelistItem]
    neighbor: list[RipngNeighborItem]
    network: list[RipngNetworkItem]
    aggregate_address: list[RipngAggregateaddressItem]
    offset_list: list[RipngOffsetlistItem]
    passive_interface: list[RipngPassiveinterfaceItem]
    redistribute: list[RipngRedistributeItem]
    update_timer: int
    timeout_timer: int
    garbage_timer: int
    interface: list[RipngInterfaceItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class Ripng:
    """
    
    Endpoint: router/ripng
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
    ) -> RipngObject: ...
    
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
        payload_dict: RipngPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | list[RipngDistanceItem] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | list[RipngDistributelistItem] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | list[RipngNeighborItem] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | list[RipngNetworkItem] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | list[RipngAggregateaddressItem] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | list[RipngOffsetlistItem] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | list[RipngPassiveinterfaceItem] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | list[RipngRedistributeItem] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | list[RipngInterfaceItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> RipngObject: ...


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
        payload_dict: RipngPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | list[RipngDistanceItem] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | list[RipngDistributelistItem] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | list[RipngNeighborItem] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | list[RipngNetworkItem] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | list[RipngAggregateaddressItem] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | list[RipngOffsetlistItem] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | list[RipngPassiveinterfaceItem] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | list[RipngRedistributeItem] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | list[RipngInterfaceItem] | None = ...,
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
    "Ripng",
    "RipngPayload",
    "RipngResponse",
    "RipngObject",
]