""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/dnat
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

class DnatPayload(TypedDict, total=False):
    """Payload type for Dnat operations."""
    uuid: int | str | list[int | str]
    ip_version: Literal["ipv4", "ipv6"]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class DnatResponse(TypedDict, total=False):
    """Response type for Dnat - use with .dict property for typed dict access."""
    uuid: list[str]
    ip_version: Literal["ipv4", "ipv6"]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class DnatObject(FortiObject):
    """Typed FortiObject for Dnat with field access."""
    uuid: list[str]
    ip_version: Literal["ipv4", "ipv6"]


# ================================================================
# Main Endpoint Class
# ================================================================

class Dnat:
    """
    
    Endpoint: firewall/dnat
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
        uuid: list[str] | None = ...,
        ip_version: Literal["ipv4", "ipv6"] | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> DnatObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: DnatPayload | None = ...,
        uuid: int | str | list[int | str] | None = ...,
        ip_version: Literal["ipv4", "ipv6"] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> DnatObject: ...


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
        payload_dict: DnatPayload | None = ...,
        uuid: int | str | list[int | str] | None = ...,
        ip_version: Literal["ipv4", "ipv6"] | None = ...,
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
    "Dnat",
    "DnatPayload",
    "DnatResponse",
    "DnatObject",
]