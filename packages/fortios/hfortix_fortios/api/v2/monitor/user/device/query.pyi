""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: user/device/query
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

class QueryPayload(TypedDict, total=False):
    """Payload type for Query operations."""
    timestamp_from: int
    timestamp_to: int
    filters: str
    query_type: str
    view_type: str
    query_id: int
    cache_query: str
    key_only: str
    filter_logic: str
    total_only: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class QueryResponse(TypedDict, total=False):
    """Response type for Query - use with .dict property for typed dict access."""
    timestamp_from: int
    timestamp_to: int
    filters: str
    query_type: str
    view_type: str
    query_id: int
    cache_query: str
    key_only: str
    filter_logic: str
    total_only: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class QueryObject(FortiObject):
    """Typed FortiObject for Query with field access."""
    timestamp_from: int
    timestamp_to: int
    filters: str
    query_type: str
    view_type: str
    query_id: int
    cache_query: str
    key_only: str
    filter_logic: str
    total_only: str


# ================================================================
# Main Endpoint Class
# ================================================================

class Query:
    """
    
    Endpoint: user/device/query
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
        timestamp_from: int | None = ...,
        timestamp_to: int | None = ...,
        filters: Literal["exact", "contains", "greaterThanEqualTo", "lessThanEqualTo"] | None = ...,
        query_type: Literal["latest", "unified_latest", "unified_history"] | None = ...,
        view_type: Literal["device", "fortiswitch_client", "forticlient", "iot_vuln_info"] | None = ...,
        query_id: int | None = ...,
        cache_query: bool | None = ...,
        key_only: bool | None = ...,
        filter_logic: Literal["and", "or"] | None = ...,
        total_only: bool | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> QueryObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: QueryPayload | None = ...,
        timestamp_from: int | None = ...,
        timestamp_to: int | None = ...,
        filters: str | None = ...,
        query_type: str | None = ...,
        view_type: str | None = ...,
        query_id: int | None = ...,
        cache_query: str | None = ...,
        key_only: str | None = ...,
        filter_logic: str | None = ...,
        total_only: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> QueryObject: ...


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
        payload_dict: QueryPayload | None = ...,
        timestamp_from: int | None = ...,
        timestamp_to: int | None = ...,
        filters: str | None = ...,
        query_type: str | None = ...,
        view_type: str | None = ...,
        query_id: int | None = ...,
        cache_query: str | None = ...,
        key_only: str | None = ...,
        filter_logic: str | None = ...,
        total_only: str | None = ...,
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
    "Query",
    "QueryPayload",
    "QueryResponse",
    "QueryObject",
]