""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: registration/forticloud/device_status
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

class DeviceStatusPayload(TypedDict, total=False):
    """Payload type for DeviceStatus operations."""
    serials: str
    update_cache: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class DeviceStatusResponse(TypedDict, total=False):
    """Response type for DeviceStatus - use with .dict property for typed dict access."""
    serials: str
    update_cache: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class DeviceStatusObject(FortiObject):
    """Typed FortiObject for DeviceStatus with field access."""
    serials: str
    update_cache: str


# ================================================================
# Main Endpoint Class
# ================================================================

class DeviceStatus:
    """
    
    Endpoint: registration/forticloud/device_status
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
        serials: str,
        update_cache: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> DeviceStatusObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: DeviceStatusPayload | None = ...,
        serials: str | None = ...,
        update_cache: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> DeviceStatusObject: ...


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
        payload_dict: DeviceStatusPayload | None = ...,
        serials: str | None = ...,
        update_cache: str | None = ...,
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
    "DeviceStatus",
    "DeviceStatusPayload",
    "DeviceStatusResponse",
    "DeviceStatusObject",
]