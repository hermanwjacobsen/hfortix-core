""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: vpn_certificate/local/import_
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

class ImportPayload(TypedDict, total=False):
    """Payload type for Import operations."""
    type: str
    certname: str
    password: str
    key_file_content: str
    scope: str
    acme_domain: str
    acme_email: str
    acme_ca_url: str
    acme_rsa_key_size: int
    acme_renew_window: int
    file_content: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ImportResponse(TypedDict, total=False):
    """Response type for Import - use with .dict property for typed dict access."""
    type: str
    certname: str
    password: str
    key_file_content: str
    scope: str
    acme_domain: str
    acme_email: str
    acme_ca_url: str
    acme_rsa_key_size: int
    acme_renew_window: int
    file_content: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ImportObject(FortiObject):
    """Typed FortiObject for Import with field access."""
    type: str
    certname: str
    password: str
    key_file_content: str
    scope: str
    acme_domain: str
    acme_email: str
    acme_ca_url: str
    acme_rsa_key_size: int
    acme_renew_window: int
    file_content: str


# ================================================================
# Main Endpoint Class
# ================================================================

class Import:
    """
    
    Endpoint: vpn_certificate/local/import_
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
    ) -> ImportObject: ...
    

    # ================================================================
    # POST Method
    # ================================================================
    
    def post(
        self,
        payload_dict: ImportPayload | None = ...,
        type: str | None = ...,
        certname: str | None = ...,
        password: str | None = ...,
        key_file_content: str | None = ...,
        scope: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_ca_url: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ImportObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: ImportPayload | None = ...,
        type: str | None = ...,
        certname: str | None = ...,
        password: str | None = ...,
        key_file_content: str | None = ...,
        scope: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_ca_url: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ImportObject: ...


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
        payload_dict: ImportPayload | None = ...,
        type: str | None = ...,
        certname: str | None = ...,
        password: str | None = ...,
        key_file_content: str | None = ...,
        scope: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_ca_url: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        file_content: str | None = ...,
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
    "Import",
    "ImportPayload",
    "ImportResponse",
    "ImportObject",
]