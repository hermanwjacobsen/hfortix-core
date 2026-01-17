""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: wireless_controller/hotspot20/h2qp_osu_provider_nai
Category: cmdb
"""

from __future__ import annotations

from typing import (
    Any,
    ClassVar,
    Literal,
    TypedDict,
    overload,
)

from hfortix_fortios.models import (
    FortiObject,
    FortiObjectList,
)


# ================================================================
# TypedDict Payloads
# ================================================================

class H2qpOsuProviderNaiNailistItem:
    """Nested item for nai-list field - supports attribute access."""
    name: str
    osu_nai: str


class H2qpOsuProviderNaiPayload(TypedDict, total=False):
    """Payload type for H2qpOsuProviderNai operations."""
    name: str
    nai_list: str | list[str] | list[dict[str, Any]] | list[H2qpOsuProviderNaiNailistItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class H2qpOsuProviderNaiResponse(TypedDict, total=False):
    """Response type for H2qpOsuProviderNai - use with .dict property for typed dict access."""
    name: str
    nai_list: list[H2qpOsuProviderNaiNailistItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class H2qpOsuProviderNaiObject(FortiObject):
    """Typed FortiObject for H2qpOsuProviderNai with field access."""
    name: str
    nai_list: list[H2qpOsuProviderNaiNailistItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class H2qpOsuProviderNai:
    """
    
    Endpoint: wireless_controller/hotspot20/h2qp_osu_provider_nai
    Category: cmdb
    MKey: name
    """
    
    # Class attributes for introspection
    endpoint: ClassVar[str] = ...
    path: ClassVar[str] = ...
    category: ClassVar[str] = ...
    mkey: ClassVar[str] = ...
    capabilities: ClassVar[dict[str, Any]] = ...
    
    def __init__(self, client: Any) -> None:
        """Initialize endpoint with HTTP client."""
        ...
    
    # ================================================================
    # GET Methods
    # ================================================================
    
    # CMDB with mkey - overloads for single vs list returns
    @overload
    def get(
        self,
        name: str,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> H2qpOsuProviderNaiObject: ...
    
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObjectList[H2qpOsuProviderNaiObject]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...

    # ================================================================
    # POST Method
    # ================================================================
    
    def post(
        self,
        payload_dict: H2qpOsuProviderNaiPayload | None = ...,
        name: str | None = ...,
        nai_list: str | list[str] | list[dict[str, Any]] | list[H2qpOsuProviderNaiNailistItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> H2qpOsuProviderNaiObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: H2qpOsuProviderNaiPayload | None = ...,
        name: str | None = ...,
        nai_list: str | list[str] | list[dict[str, Any]] | list[H2qpOsuProviderNaiNailistItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> H2qpOsuProviderNaiObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

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
        payload_dict: H2qpOsuProviderNaiPayload | None = ...,
        name: str | None = ...,
        nai_list: str | list[str] | list[dict[str, Any]] | list[H2qpOsuProviderNaiNailistItem] | None = ...,
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
    "H2qpOsuProviderNai",
    "H2qpOsuProviderNaiPayload",
    "H2qpOsuProviderNaiResponse",
    "H2qpOsuProviderNaiObject",
]