""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: rule/otdt
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

class OtdtParametersItem:
    """Nested item for parameters field - supports attribute access."""
    name: str
    default_value: str


class OtdtMetadataItem:
    """Nested item for metadata field - supports attribute access."""
    id: int
    metaid: int
    valueid: int


class OtdtPayload(TypedDict, total=False):
    """Payload type for Otdt operations."""
    name: str
    id: int
    category: int
    popularity: int
    risk: int
    weight: int
    protocol: str
    technology: str
    behavior: str
    vendor: str
    parameters: str | list[str] | list[dict[str, Any]] | list[OtdtParametersItem]
    metadata: str | list[str] | list[dict[str, Any]] | list[OtdtMetadataItem]
    status: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class OtdtResponse(TypedDict, total=False):
    """Response type for Otdt - use with .dict property for typed dict access."""
    name: str
    id: int
    category: int
    popularity: int
    risk: int
    weight: int
    protocol: str
    technology: str
    behavior: str
    vendor: str
    parameters: list[OtdtParametersItem]
    metadata: list[OtdtMetadataItem]
    status: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class OtdtObject(FortiObject):
    """Typed FortiObject for Otdt with field access."""
    name: str
    id: int
    category: int
    popularity: int
    risk: int
    weight: int
    protocol: str
    technology: str
    behavior: str
    vendor: str
    parameters: list[OtdtParametersItem]
    metadata: list[OtdtMetadataItem]
    status: str


# ================================================================
# Main Endpoint Class
# ================================================================

class Otdt:
    """
    
    Endpoint: rule/otdt
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> OtdtObject: ...
    
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
    ) -> FortiObjectList[OtdtObject]: ...
    
    def get_schema(
        self,
        format: str = ...,
    ) -> FortiObject: ...

    # ================================================================
    # POST Method
    # ================================================================
    
    def post(
        self,
        payload_dict: OtdtPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | list[OtdtParametersItem] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | list[OtdtMetadataItem] | None = ...,
        status: str | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> OtdtObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: OtdtPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | list[OtdtParametersItem] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | list[OtdtMetadataItem] | None = ...,
        status: str | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> OtdtObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        name: str | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
    def exists(
        self,
        name: str,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: OtdtPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: str | list[str] | list[dict[str, Any]] | list[OtdtParametersItem] | None = ...,
        metadata: str | list[str] | list[dict[str, Any]] | list[OtdtMetadataItem] | None = ...,
        status: str | None = ...,
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
    "Otdt",
    "OtdtPayload",
    "OtdtResponse",
    "OtdtObject",
]