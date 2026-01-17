""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: switch_controller/traffic_sniffer
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

class TrafficSnifferTargetmacItem:
    """Nested item for target-mac field - supports attribute access."""
    mac: str
    description: str


class TrafficSnifferTargetipItem:
    """Nested item for target-ip field - supports attribute access."""
    ip: str
    description: str


class TrafficSnifferTargetportItem:
    """Nested item for target-port field - supports attribute access."""
    switch_id: str
    description: str
    in_ports: str
    out_ports: str


class TrafficSnifferPayload(TypedDict, total=False):
    """Payload type for TrafficSniffer operations."""
    mode: Literal["erspan-auto", "rspan", "none"]
    erspan_ip: str
    target_mac: str | list[str] | list[dict[str, Any]] | list[TrafficSnifferTargetmacItem]
    target_ip: str | list[str] | list[dict[str, Any]] | list[TrafficSnifferTargetipItem]
    target_port: str | list[str] | list[dict[str, Any]] | list[TrafficSnifferTargetportItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class TrafficSnifferResponse(TypedDict, total=False):
    """Response type for TrafficSniffer - use with .dict property for typed dict access."""
    mode: Literal["erspan-auto", "rspan", "none"]
    erspan_ip: str
    target_mac: list[TrafficSnifferTargetmacItem]
    target_ip: list[TrafficSnifferTargetipItem]
    target_port: list[TrafficSnifferTargetportItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class TrafficSnifferObject(FortiObject):
    """Typed FortiObject for TrafficSniffer with field access."""
    mode: Literal["erspan-auto", "rspan", "none"]
    erspan_ip: str
    target_mac: list[TrafficSnifferTargetmacItem]
    target_ip: list[TrafficSnifferTargetipItem]
    target_port: list[TrafficSnifferTargetportItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class TrafficSniffer:
    """
    
    Endpoint: switch_controller/traffic_sniffer
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
    ) -> TrafficSnifferObject: ...
    
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
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | list[TrafficSnifferTargetmacItem] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | list[TrafficSnifferTargetipItem] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | list[TrafficSnifferTargetportItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> TrafficSnifferObject: ...


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
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | list[TrafficSnifferTargetmacItem] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | list[TrafficSnifferTargetipItem] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | list[TrafficSnifferTargetportItem] | None = ...,
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
    "TrafficSniffer",
    "TrafficSnifferPayload",
    "TrafficSnifferResponse",
    "TrafficSnifferObject",
]