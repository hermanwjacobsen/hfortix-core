""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: casb/user_activity
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

class UserActivityMatchItem(TypedDict, total=False):
    """Nested item for match field."""
    id: int
    strategy: Literal["and", "or"]
    rules: str | list[str]
    tenant_extraction: str


class UserActivityControloptionsItem(TypedDict, total=False):
    """Nested item for control-options field."""
    name: str
    status: Literal["enable", "disable"]
    operations: str | list[str]


class UserActivityPayload(TypedDict, total=False):
    """Payload type for UserActivity operations."""
    name: str
    uuid: str
    status: Literal["enable", "disable"]
    description: str
    type: Literal["built-in", "customized"]
    casb_name: str
    application: str
    category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"]
    match_strategy: Literal["and", "or"]
    match: str | list[str] | list[UserActivityMatchItem]
    control_options: str | list[str] | list[UserActivityControloptionsItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class UserActivityResponse(TypedDict, total=False):
    """Response type for UserActivity - use with .dict property for typed dict access."""
    name: str
    uuid: str
    status: Literal["enable", "disable"]
    description: str
    type: Literal["built-in", "customized"]
    casb_name: str
    application: str
    category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"]
    match_strategy: Literal["and", "or"]
    match: list[UserActivityMatchItem]
    control_options: list[UserActivityControloptionsItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class UserActivityObject(FortiObject):
    """Typed FortiObject for UserActivity with field access."""
    name: str
    uuid: str
    status: Literal["enable", "disable"]
    description: str
    type: Literal["built-in", "customized"]
    casb_name: str
    application: str
    category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"]
    match_strategy: Literal["and", "or"]
    match: list[UserActivityMatchItem]
    control_options: list[UserActivityControloptionsItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class UserActivity:
    """
    
    Endpoint: casb/user_activity
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
    ) -> UserActivityObject: ...
    
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
    ) -> FortiObjectList[UserActivityObject]: ...
    
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
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[UserActivityMatchItem] | None = ...,
        control_options: str | list[str] | list[UserActivityControloptionsItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> UserActivityObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[UserActivityMatchItem] | None = ...,
        control_options: str | list[str] | list[UserActivityControloptionsItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> UserActivityObject: ...

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
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[UserActivityMatchItem] | None = ...,
        control_options: str | list[str] | list[UserActivityControloptionsItem] | None = ...,
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
    "UserActivity",
    "UserActivityPayload",
    "UserActivityResponse",
    "UserActivityObject",
]