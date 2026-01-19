""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: user/firewall/deauth
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

class DeauthPayload(TypedDict, total=False):
    """Payload type for Deauth operations."""
    user_type: str
    id: int
    ip: str
    ip_version: str
    method: str
    all: bool
    users: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class DeauthResponse(TypedDict, total=False):
    """Response type for Deauth - use with .dict property for typed dict access."""
    user_type: str
    id: int
    ip: str
    ip_version: str
    method: str
    all: bool
    users: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class DeauthObject(FortiObject):
    """Typed FortiObject for Deauth with field access."""
    user_type: str
    id: int
    ip: str
    ip_version: str
    method: str
    all: bool
    users: str


# ================================================================
# Main Endpoint Class
# ================================================================

class Deauth:
    """
    
    Endpoint: user/firewall/deauth
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
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> DeauthObject: ...
    

    # ================================================================
    # POST Method
    # ================================================================
    
    def post(
        self,
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: bool | None = ...,
        users: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> DeauthObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: bool | None = ...,
        users: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> DeauthObject: ...


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
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: str | None = ...,
        users: str | None = ...,
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
    "Deauth",
    "DeauthPayload",
    "DeauthResponse",
    "DeauthObject",
]