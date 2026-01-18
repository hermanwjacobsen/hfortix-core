""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: system/resource/usage
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

class UsagePayload(TypedDict, total=False):
    """Payload type for Usage operations."""
    scope: str
    resource: str
    interval: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class UsageResponse(TypedDict, total=False):
    """Response type for Usage - use with .dict property for typed dict access."""
    scope: str
    resource: str
    interval: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class UsageObject(FortiObject):
    """Typed FortiObject for Usage with field access."""
    scope: str
    resource: str
    interval: str


# ================================================================
# Main Endpoint Class
# ================================================================

class Usage:
    """
    
    Endpoint: system/resource/usage
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
        scope: Literal["vdom", "global"] | None = ...,
        resource: Literal["cpu", "mem", "disk", "session", "session6", "setuprate", "setuprate6", "disk_lograte", "faz_lograte", "forticloud_lograte", "gtp_tunnel", "gtp_tunnel_setup_rate"] | None = ...,
        interval: Literal["1-min", "10-min", "30-min", "1-hour", "12-hour", "24-hour"] | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> UsageObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: UsagePayload | None = ...,
        scope: str | None = ...,
        resource: str | None = ...,
        interval: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> UsageObject: ...


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
        payload_dict: UsagePayload | None = ...,
        scope: str | None = ...,
        resource: str | None = ...,
        interval: str | None = ...,
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
    "Usage",
    "UsagePayload",
    "UsageResponse",
    "UsageObject",
]