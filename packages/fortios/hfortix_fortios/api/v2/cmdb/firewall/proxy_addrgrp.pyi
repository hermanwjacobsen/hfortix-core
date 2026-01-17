""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/proxy_addrgrp
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

class ProxyAddrgrpMemberItem:
    """Nested item for member field - supports attribute access."""
    name: str


class ProxyAddrgrpTaggingItem:
    """Nested item for tagging field - supports attribute access."""
    name: str
    category: str
    tags: str | list[str]


class ProxyAddrgrpPayload(TypedDict, total=False):
    """Payload type for ProxyAddrgrp operations."""
    name: str
    type: Literal["src", "dst"]
    uuid: str
    member: str | list[str] | list[dict[str, Any]] | list[ProxyAddrgrpMemberItem]
    color: int
    tagging: str | list[str] | list[dict[str, Any]] | list[ProxyAddrgrpTaggingItem]
    comment: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ProxyAddrgrpResponse(TypedDict, total=False):
    """Response type for ProxyAddrgrp - use with .dict property for typed dict access."""
    name: str
    type: Literal["src", "dst"]
    uuid: str
    member: list[ProxyAddrgrpMemberItem]
    color: int
    tagging: list[ProxyAddrgrpTaggingItem]
    comment: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ProxyAddrgrpObject(FortiObject):
    """Typed FortiObject for ProxyAddrgrp with field access."""
    name: str
    type: Literal["src", "dst"]
    uuid: str
    member: list[ProxyAddrgrpMemberItem]
    color: int
    tagging: list[ProxyAddrgrpTaggingItem]
    comment: str


# ================================================================
# Main Endpoint Class
# ================================================================

class ProxyAddrgrp:
    """
    
    Endpoint: firewall/proxy_addrgrp
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
    ) -> ProxyAddrgrpObject: ...
    
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
    ) -> FortiObjectList[ProxyAddrgrpObject]: ...
    
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
        payload_dict: ProxyAddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["src", "dst"] | None = ...,
        uuid: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | list[ProxyAddrgrpMemberItem] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | list[ProxyAddrgrpTaggingItem] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ProxyAddrgrpObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: ProxyAddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["src", "dst"] | None = ...,
        uuid: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | list[ProxyAddrgrpMemberItem] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | list[ProxyAddrgrpTaggingItem] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ProxyAddrgrpObject: ...

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
        payload_dict: ProxyAddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["src", "dst"] | None = ...,
        uuid: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | list[ProxyAddrgrpMemberItem] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | list[ProxyAddrgrpTaggingItem] | None = ...,
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
    "ProxyAddrgrp",
    "ProxyAddrgrpPayload",
    "ProxyAddrgrpResponse",
    "ProxyAddrgrpObject",
]