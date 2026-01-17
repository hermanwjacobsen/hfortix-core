""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: system/interface/dhcp_status
Category: monitor
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

class DhcpStatusPayload(TypedDict, total=False):
    """Payload type for DhcpStatus operations."""
    mkey: str
    ipv6: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class DhcpStatusResponse(TypedDict, total=False):
    """Response type for DhcpStatus - use with .dict property for typed dict access."""
    mkey: str
    ipv6: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class DhcpStatusObject(FortiObject):
    """Typed FortiObject for DhcpStatus with field access."""
    ipv6: str


# ================================================================
# Main Endpoint Class
# ================================================================

class DhcpStatus:
    """
    
    Endpoint: system/interface/dhcp_status
    Category: monitor
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
    
    # Service/Monitor endpoint
    def get(
        self,
        *,
        mkey: str,
        ipv6: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> DhcpStatusObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: DhcpStatusPayload | None = ...,
        mkey: str | None = ...,
        ipv6: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> DhcpStatusObject: ...


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
        payload_dict: DhcpStatusPayload | None = ...,
        mkey: str | None = ...,
        ipv6: str | None = ...,
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
    "DhcpStatus",
    "DhcpStatusPayload",
    "DhcpStatusResponse",
    "DhcpStatusObject",
]