""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/internet_service_extension
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

class InternetServiceExtensionEntryItem(TypedDict, total=False):
    """Nested item for entry field."""
    id: int
    addr_mode: Literal["ipv4", "ipv6"]
    protocol: int
    port_range: str | list[str]
    dst: str | list[str]
    dst6: str | list[str]


class InternetServiceExtensionDisableentryItem(TypedDict, total=False):
    """Nested item for disable-entry field."""
    id: int
    addr_mode: Literal["ipv4", "ipv6"]
    protocol: int
    port_range: str | list[str]
    ip_range: str | list[str]
    ip6_range: str | list[str]


class InternetServiceExtensionPayload(TypedDict, total=False):
    """Payload type for InternetServiceExtension operations."""
    id: int
    comment: str
    entry: str | list[str] | list[InternetServiceExtensionEntryItem]
    disable_entry: str | list[str] | list[InternetServiceExtensionDisableentryItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class InternetServiceExtensionResponse(TypedDict, total=False):
    """Response type for InternetServiceExtension - use with .dict property for typed dict access."""
    id: int
    comment: str
    entry: list[InternetServiceExtensionEntryItem]
    disable_entry: list[InternetServiceExtensionDisableentryItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class InternetServiceExtensionObject(FortiObject):
    """Typed FortiObject for InternetServiceExtension with field access."""
    id: int
    comment: str
    entry: list[InternetServiceExtensionEntryItem]
    disable_entry: list[InternetServiceExtensionDisableentryItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class InternetServiceExtension:
    """
    
    Endpoint: firewall/internet_service_extension
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
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> InternetServiceExtensionObject: ...
    
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
    ) -> FortiObjectList[InternetServiceExtensionObject]: ...
    
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
        payload_dict: InternetServiceExtensionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceExtensionEntryItem] | None = ...,
        disable_entry: str | list[str] | list[InternetServiceExtensionDisableentryItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> InternetServiceExtensionObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: InternetServiceExtensionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceExtensionEntryItem] | None = ...,
        disable_entry: str | list[str] | list[InternetServiceExtensionDisableentryItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> InternetServiceExtensionObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: InternetServiceExtensionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceExtensionEntryItem] | None = ...,
        disable_entry: str | list[str] | list[InternetServiceExtensionDisableentryItem] | None = ...,
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
    "InternetServiceExtension",
    "InternetServiceExtensionPayload",
    "InternetServiceExtensionResponse",
    "InternetServiceExtensionObject",
]