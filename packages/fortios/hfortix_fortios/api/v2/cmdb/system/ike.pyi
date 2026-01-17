""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: system/ike
Category: cmdb
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

class IkePayload(TypedDict, total=False):
    """Payload type for Ike operations."""
    embryonic_limit: int
    dh_multiprocess: Literal["enable", "disable"]
    dh_worker_count: int
    dh_mode: Literal["software", "hardware"]
    dh_keypair_cache: Literal["enable", "disable"]
    dh_keypair_count: int
    dh_keypair_throttle: Literal["enable", "disable"]
    dh_group_1: str
    dh_group_2: str
    dh_group_5: str
    dh_group_14: str
    dh_group_15: str
    dh_group_16: str
    dh_group_17: str
    dh_group_18: str
    dh_group_19: str
    dh_group_20: str
    dh_group_21: str
    dh_group_27: str
    dh_group_28: str
    dh_group_29: str
    dh_group_30: str
    dh_group_31: str
    dh_group_32: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class IkeResponse(TypedDict, total=False):
    """Response type for Ike - use with .dict property for typed dict access."""
    embryonic_limit: int
    dh_multiprocess: Literal["enable", "disable"]
    dh_worker_count: int
    dh_mode: Literal["software", "hardware"]
    dh_keypair_cache: Literal["enable", "disable"]
    dh_keypair_count: int
    dh_keypair_throttle: Literal["enable", "disable"]
    dh_group_1: str
    dh_group_2: str
    dh_group_5: str
    dh_group_14: str
    dh_group_15: str
    dh_group_16: str
    dh_group_17: str
    dh_group_18: str
    dh_group_19: str
    dh_group_20: str
    dh_group_21: str
    dh_group_27: str
    dh_group_28: str
    dh_group_29: str
    dh_group_30: str
    dh_group_31: str
    dh_group_32: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class IkeObject(FortiObject):
    """Typed FortiObject for Ike with field access."""
    embryonic_limit: int
    dh_multiprocess: Literal["enable", "disable"]
    dh_worker_count: int
    dh_mode: Literal["software", "hardware"]
    dh_keypair_cache: Literal["enable", "disable"]
    dh_keypair_count: int
    dh_keypair_throttle: Literal["enable", "disable"]
    dh_group_1: str
    dh_group_2: str
    dh_group_5: str
    dh_group_14: str
    dh_group_15: str
    dh_group_16: str
    dh_group_17: str
    dh_group_18: str
    dh_group_19: str
    dh_group_20: str
    dh_group_21: str
    dh_group_27: str
    dh_group_28: str
    dh_group_29: str
    dh_group_30: str
    dh_group_31: str
    dh_group_32: str


# ================================================================
# Main Endpoint Class
# ================================================================

class Ike:
    """
    
    Endpoint: system/ike
    Category: cmdb
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
    
    # Singleton endpoint (no mkey)
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
    ) -> IkeObject: ...
    
    def get_schema(
        self,
        format: str = ...,
    ) -> FortiObject: ...


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> IkeObject: ...


    # ================================================================
    # Utility Methods
    # ================================================================
    
    def exists(
        self,
        name: str,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
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
    "Ike",
    "IkePayload",
    "IkeResponse",
    "IkeObject",
]