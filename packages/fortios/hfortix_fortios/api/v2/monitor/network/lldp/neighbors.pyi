""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: network/lldp/neighbors
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

class NeighborsPayload(TypedDict, total=False):
    """Payload type for Neighbors operations."""
    scope: Literal["vdom", "global"]
    port: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class NeighborsResponse(TypedDict, total=False):
    """Response type for Neighbors - use with .dict property for typed dict access."""
    scope: Literal["vdom", "global"]
    port: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class NeighborsObject(FortiObject):
    """Typed FortiObject for Neighbors with field access."""
    scope: Literal["vdom", "global"]
    port: str


# ================================================================
# Main Endpoint Class
# ================================================================

class Neighbors:
    """
    
    Endpoint: network/lldp/neighbors
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
        port: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> NeighborsObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: NeighborsPayload | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        port: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> NeighborsObject: ...


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
        payload_dict: NeighborsPayload | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        port: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject[Any]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> list[str] | list[dict[str, Any]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject[Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject[Any]: ...
    
    @staticmethod
    def schema() -> FortiObject[Any]: ...


__all__ = [
    "Neighbors",
    "NeighborsPayload",
    "NeighborsResponse",
    "NeighborsObject",
]