""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: casb/attribute_match
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

class AttributeMatchMatchItem:
    """Nested item for match field - supports attribute access."""
    id: int
    rule_strategy: Literal["and", "or"]
    rule: str


class AttributeMatchPayload(TypedDict, total=False):
    """Payload type for AttributeMatch operations."""
    name: str
    application: str
    match_strategy: Literal["or", "and", "subset"]
    match: str | list[str] | list[dict[str, Any]] | list[AttributeMatchMatchItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class AttributeMatchResponse(TypedDict, total=False):
    """Response type for AttributeMatch - use with .dict property for typed dict access."""
    name: str
    application: str
    match_strategy: Literal["or", "and", "subset"]
    match: list[AttributeMatchMatchItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class AttributeMatchObject(FortiObject):
    """Typed FortiObject for AttributeMatch with field access."""
    name: str
    application: str
    match_strategy: Literal["or", "and", "subset"]
    match: list[AttributeMatchMatchItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class AttributeMatch:
    """
    
    Endpoint: casb/attribute_match
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
    ) -> AttributeMatchObject: ...
    
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
    ) -> FortiObjectList[AttributeMatchObject]: ...
    
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
        payload_dict: AttributeMatchPayload | None = ...,
        name: str | None = ...,
        application: str | None = ...,
        match_strategy: Literal["or", "and", "subset"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | list[AttributeMatchMatchItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> AttributeMatchObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: AttributeMatchPayload | None = ...,
        name: str | None = ...,
        application: str | None = ...,
        match_strategy: Literal["or", "and", "subset"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | list[AttributeMatchMatchItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> AttributeMatchObject: ...

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
        payload_dict: AttributeMatchPayload | None = ...,
        name: str | None = ...,
        application: str | None = ...,
        match_strategy: Literal["or", "and", "subset"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | list[AttributeMatchMatchItem] | None = ...,
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
    "AttributeMatch",
    "AttributeMatchPayload",
    "AttributeMatchResponse",
    "AttributeMatchObject",
]