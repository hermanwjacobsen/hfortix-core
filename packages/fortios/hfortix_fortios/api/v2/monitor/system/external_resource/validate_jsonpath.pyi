""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: system/external_resource/validate_jsonpath
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

class ValidateJsonpathPayload(TypedDict, total=False):
    """Payload type for ValidateJsonpath operations."""
    path_name: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ValidateJsonpathResponse(TypedDict, total=False):
    """Response type for ValidateJsonpath - use with .dict property for typed dict access."""
    path_name: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ValidateJsonpathObject(FortiObject):
    """Typed FortiObject for ValidateJsonpath with field access."""
    path_name: str


# ================================================================
# Main Endpoint Class
# ================================================================

class ValidateJsonpath:
    """
    
    Endpoint: system/external_resource/validate_jsonpath
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
        path_name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ValidateJsonpathObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: ValidateJsonpathPayload | None = ...,
        path_name: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ValidateJsonpathObject: ...


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
        payload_dict: ValidateJsonpathPayload | None = ...,
        path_name: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject[Any]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> list[str] | list[dict[str, Any]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject[Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject[Any]: ...
    
    @staticmethod
    def schema() -> FortiObject[Any]: ...


__all__ = [
    "ValidateJsonpath",
    "ValidateJsonpathPayload",
    "ValidateJsonpathResponse",
    "ValidateJsonpathObject",
]