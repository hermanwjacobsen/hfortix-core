""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: waf/profile
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

class ProfileUrlaccessItem:
    """Nested item for url-access field - supports attribute access."""
    id: int
    address: str
    action: Literal["bypass", "permit", "block"]
    log: Literal["enable", "disable"]
    severity: Literal["high", "medium", "low"]
    access_pattern: str


class ProfilePayload(TypedDict, total=False):
    """Payload type for Profile operations."""
    name: str
    external: Literal["disable", "enable"]
    extended_log: Literal["enable", "disable"]
    signature: str
    constraint: str
    method: str
    address_list: str
    url_access: str | list[str] | list[dict[str, Any]] | list[ProfileUrlaccessItem]
    comment: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ProfileResponse(TypedDict, total=False):
    """Response type for Profile - use with .dict property for typed dict access."""
    name: str
    external: Literal["disable", "enable"]
    extended_log: Literal["enable", "disable"]
    signature: str
    constraint: str
    method: str
    address_list: str
    url_access: list[ProfileUrlaccessItem]
    comment: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ProfileObject(FortiObject):
    """Typed FortiObject for Profile with field access."""
    name: str
    external: Literal["disable", "enable"]
    extended_log: Literal["enable", "disable"]
    signature: str
    constraint: str
    method: str
    address_list: str
    url_access: list[ProfileUrlaccessItem]
    comment: str


# ================================================================
# Main Endpoint Class
# ================================================================

class Profile:
    """
    
    Endpoint: waf/profile
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
    ) -> ProfileObject: ...
    
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
    ) -> FortiObjectList[ProfileObject]: ...
    
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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        external: Literal["disable", "enable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        signature: str | None = ...,
        constraint: str | None = ...,
        method: str | None = ...,
        address_list: str | None = ...,
        url_access: str | list[str] | list[dict[str, Any]] | list[ProfileUrlaccessItem] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ProfileObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        external: Literal["disable", "enable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        signature: str | None = ...,
        constraint: str | None = ...,
        method: str | None = ...,
        address_list: str | None = ...,
        url_access: str | list[str] | list[dict[str, Any]] | list[ProfileUrlaccessItem] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ProfileObject: ...

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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        external: Literal["disable", "enable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        signature: str | None = ...,
        constraint: str | None = ...,
        method: str | None = ...,
        address_list: str | None = ...,
        url_access: str | list[str] | list[dict[str, Any]] | list[ProfileUrlaccessItem] | None = ...,
        comment: str | None = ...,
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
    "Profile",
    "ProfilePayload",
    "ProfileResponse",
    "ProfileObject",
]