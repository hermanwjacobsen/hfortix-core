""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: wifi/managed_ap
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

class ManagedApPayload(TypedDict, total=False):
    """Payload type for ManagedAp operations."""
    wtp_id: str
    incl_local: bool
    skip_eos: bool


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ManagedApResponse(TypedDict, total=False):
    """Response type for ManagedAp - use with .dict property for typed dict access."""
    wtp_id: str
    incl_local: bool
    skip_eos: bool


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ManagedApObject(FortiObject):
    """Typed FortiObject for ManagedAp with field access."""
    wtp_id: str
    incl_local: bool
    skip_eos: bool


# ================================================================
# Main Endpoint Class
# ================================================================

class ManagedAp:
    """
    
    Endpoint: wifi/managed_ap
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
        wtp_id: str | None = ...,
        incl_local: bool | None = ...,
        skip_eos: bool | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ManagedApObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: ManagedApPayload | None = ...,
        wtp_id: str | None = ...,
        incl_local: bool | None = ...,
        skip_eos: bool | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ManagedApObject: ...


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
        payload_dict: ManagedApPayload | None = ...,
        wtp_id: str | None = ...,
        incl_local: str | None = ...,
        skip_eos: str | None = ...,
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
    "ManagedAp",
    "ManagedApPayload",
    "ManagedApResponse",
    "ManagedApObject",
]