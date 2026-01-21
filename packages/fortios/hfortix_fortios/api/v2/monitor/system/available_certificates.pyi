""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: system/available_certificates
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

class AvailableCertificatesPayload(TypedDict, total=False):
    """Payload type for AvailableCertificates operations."""
    scope: Literal["vdom", "global"]
    with_remote: bool
    with_ca: bool
    with_crl: bool
    mkey: str
    find_all_references: bool


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class AvailableCertificatesResponse(TypedDict, total=False):
    """Response type for AvailableCertificates - use with .dict property for typed dict access."""
    scope: Literal["vdom", "global"]
    with_remote: bool
    with_ca: bool
    with_crl: bool
    mkey: str
    find_all_references: bool


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class AvailableCertificatesObject(FortiObject):
    """Typed FortiObject for AvailableCertificates with field access."""
    scope: Literal["vdom", "global"]
    with_remote: bool
    with_ca: bool
    with_crl: bool
    find_all_references: bool


# ================================================================
# Main Endpoint Class
# ================================================================

class AvailableCertificates:
    """
    
    Endpoint: system/available_certificates
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
        with_remote: bool | None = ...,
        with_ca: bool | None = ...,
        with_crl: bool | None = ...,
        mkey: str | None = ...,
        find_all_references: bool | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> AvailableCertificatesObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: AvailableCertificatesPayload | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        with_remote: bool | None = ...,
        with_ca: bool | None = ...,
        with_crl: bool | None = ...,
        mkey: str | None = ...,
        find_all_references: bool | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> AvailableCertificatesObject: ...


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
        payload_dict: AvailableCertificatesPayload | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        with_remote: bool | None = ...,
        with_ca: bool | None = ...,
        with_crl: bool | None = ...,
        mkey: str | None = ...,
        find_all_references: bool | None = ...,
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
    "AvailableCertificates",
    "AvailableCertificatesPayload",
    "AvailableCertificatesResponse",
    "AvailableCertificatesObject",
]