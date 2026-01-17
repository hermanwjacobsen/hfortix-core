""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: registration/forticloud/register_device
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

class RegisterDevicePayload(TypedDict, total=False):
    """Payload type for RegisterDevice operations."""
    serial: str
    email: str
    password: str
    reseller: str
    reseller_id: int
    country: str
    is_government: str
    agreement_accepted: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class RegisterDeviceResponse(TypedDict, total=False):
    """Response type for RegisterDevice - use with .dict property for typed dict access."""
    serial: str
    email: str
    password: str
    reseller: str
    reseller_id: int
    country: str
    is_government: str
    agreement_accepted: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class RegisterDeviceObject(FortiObject):
    """Typed FortiObject for RegisterDevice with field access."""
    email: str
    password: str
    reseller: str
    reseller_id: int
    country: str
    is_government: str
    agreement_accepted: str


# ================================================================
# Main Endpoint Class
# ================================================================

class RegisterDevice:
    """
    
    Endpoint: registration/forticloud/register_device
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
    ) -> RegisterDeviceObject: ...
    

    # ================================================================
    # POST Method
    # ================================================================
    
    def post(
        self,
        payload_dict: RegisterDevicePayload | None = ...,
        serial: str | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        reseller: str | None = ...,
        reseller_id: int | None = ...,
        country: str | None = ...,
        is_government: str | None = ...,
        agreement_accepted: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> RegisterDeviceObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: RegisterDevicePayload | None = ...,
        serial: str | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        reseller: str | None = ...,
        reseller_id: int | None = ...,
        country: str | None = ...,
        is_government: str | None = ...,
        agreement_accepted: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> RegisterDeviceObject: ...


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
        payload_dict: RegisterDevicePayload | None = ...,
        serial: str | None = ...,
        email: str | None = ...,
        password: str | None = ...,
        reseller: str | None = ...,
        reseller_id: int | None = ...,
        country: str | None = ...,
        is_government: str | None = ...,
        agreement_accepted: str | None = ...,
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
    "RegisterDevice",
    "RegisterDevicePayload",
    "RegisterDeviceResponse",
    "RegisterDeviceObject",
]