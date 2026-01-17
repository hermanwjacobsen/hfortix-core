""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: wireless_controller/hotspot20/anqp_venue_name
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

class AnqpVenueNameValuelistItem:
    """Nested item for value-list field - supports attribute access."""
    index: int
    lang: str
    value: str


class AnqpVenueNamePayload(TypedDict, total=False):
    """Payload type for AnqpVenueName operations."""
    name: str
    value_list: str | list[str] | list[dict[str, Any]] | list[AnqpVenueNameValuelistItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class AnqpVenueNameResponse(TypedDict, total=False):
    """Response type for AnqpVenueName - use with .dict property for typed dict access."""
    name: str
    value_list: list[AnqpVenueNameValuelistItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class AnqpVenueNameObject(FortiObject):
    """Typed FortiObject for AnqpVenueName with field access."""
    name: str
    value_list: list[AnqpVenueNameValuelistItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class AnqpVenueName:
    """
    
    Endpoint: wireless_controller/hotspot20/anqp_venue_name
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
    ) -> AnqpVenueNameObject: ...
    
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
    ) -> FortiObjectList[AnqpVenueNameObject]: ...
    
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
        payload_dict: AnqpVenueNamePayload | None = ...,
        name: str | None = ...,
        value_list: str | list[str] | list[dict[str, Any]] | list[AnqpVenueNameValuelistItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> AnqpVenueNameObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: AnqpVenueNamePayload | None = ...,
        name: str | None = ...,
        value_list: str | list[str] | list[dict[str, Any]] | list[AnqpVenueNameValuelistItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> AnqpVenueNameObject: ...

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
        payload_dict: AnqpVenueNamePayload | None = ...,
        name: str | None = ...,
        value_list: str | list[str] | list[dict[str, Any]] | list[AnqpVenueNameValuelistItem] | None = ...,
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
    "AnqpVenueName",
    "AnqpVenueNamePayload",
    "AnqpVenueNameResponse",
    "AnqpVenueNameObject",
]