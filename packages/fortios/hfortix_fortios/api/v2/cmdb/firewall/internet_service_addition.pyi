""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/internet_service_addition
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

class InternetServiceAdditionEntryItem:
    """Nested item for entry field - supports attribute access."""
    id: int
    addr_mode: Literal["ipv4", "ipv6"]
    protocol: int
    port_range: str | list[str]


class InternetServiceAdditionPayload(TypedDict, total=False):
    """Payload type for InternetServiceAddition operations."""
    id: int
    comment: str
    entry: str | list[str] | list[dict[str, Any]] | list[InternetServiceAdditionEntryItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class InternetServiceAdditionResponse(TypedDict, total=False):
    """Response type for InternetServiceAddition - use with .dict property for typed dict access."""
    id: int
    comment: str
    entry: list[InternetServiceAdditionEntryItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class InternetServiceAdditionObject(FortiObject):
    """Typed FortiObject for InternetServiceAddition with field access."""
    id: int
    comment: str
    entry: list[InternetServiceAdditionEntryItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class InternetServiceAddition:
    """
    
    Endpoint: firewall/internet_service_addition
    Category: cmdb
    MKey: id
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
        id: int,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> InternetServiceAdditionObject: ...
    
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObjectList[InternetServiceAdditionObject]: ...
    
    def get_schema(
        self,
        format: str = ...,
    ) -> FortiObject: ...

    # ================================================================
    # POST Method
    # ================================================================
    
    def post(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[dict[str, Any]] | list[InternetServiceAdditionEntryItem] | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> InternetServiceAdditionObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[dict[str, Any]] | list[InternetServiceAdditionEntryItem] | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> InternetServiceAdditionObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        id: int | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
    def exists(
        self,
        id: int,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[dict[str, Any]] | list[InternetServiceAdditionEntryItem] | None = ...,
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
    "InternetServiceAddition",
    "InternetServiceAdditionPayload",
    "InternetServiceAdditionResponse",
    "InternetServiceAdditionObject",
]