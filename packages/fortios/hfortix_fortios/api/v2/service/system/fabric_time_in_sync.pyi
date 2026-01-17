""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: system/fabric_time_in_sync
Category: service
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

class FabricTimeInSyncPayload(TypedDict, total=False):
    """Payload type for FabricTimeInSync operations."""
    utc: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class FabricTimeInSyncResponse(TypedDict, total=False):
    """Response type for FabricTimeInSync - use with .dict property for typed dict access."""
    utc: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class FabricTimeInSyncObject(FortiObject):
    """Typed FortiObject for FabricTimeInSync with field access."""
    utc: str


# ================================================================
# Main Endpoint Class
# ================================================================

class FabricTimeInSync:
    """
    
    Endpoint: system/fabric_time_in_sync
    Category: service
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
        utc: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FabricTimeInSyncObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: FabricTimeInSyncPayload | None = ...,
        utc: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FabricTimeInSyncObject: ...


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
        payload_dict: FabricTimeInSyncPayload | None = ...,
        utc: str | None = ...,
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
    "FabricTimeInSync",
    "FabricTimeInSyncPayload",
    "FabricTimeInSyncResponse",
    "FabricTimeInSyncObject",
]