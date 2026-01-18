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

class ProfileSignatureDict(TypedDict, total=False):
    """Nested object type for signature field."""
    main_class: str | list[str]
    disabled_sub_class: str | list[str]
    disabled_signature: str | list[str]
    credit_card_detection_threshold: int
    custom_signature: str | list[str]


class ProfileConstraintDict(TypedDict, total=False):
    """Nested object type for constraint field."""
    header_length: str
    content_length: str
    param_length: str
    line_length: str
    url_param_length: str
    version: str
    method: str
    hostname: str
    malformed: str
    max_cookie: str
    max_header_line: str
    max_url_param: str
    max_range_segment: str
    exception: str | list[str]


class ProfileMethodDict(TypedDict, total=False):
    """Nested object type for method field."""
    status: Literal["enable", "disable"]
    log: Literal["enable", "disable"]
    severity: Literal["high", "medium", "low"]
    default_allowed_methods: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "others"]
    method_policy: str | list[str]


class ProfileAddresslistDict(TypedDict, total=False):
    """Nested object type for address-list field."""
    status: Literal["enable", "disable"]
    blocked_log: Literal["enable", "disable"]
    severity: Literal["high", "medium", "low"]
    trusted_address: str | list[str]
    blocked_address: str | list[str]


class ProfileUrlaccessItem(TypedDict, total=False):
    """Nested item for url-access field."""
    id: int
    address: str
    action: Literal["bypass", "permit", "block"]
    log: Literal["enable", "disable"]
    severity: Literal["high", "medium", "low"]
    access_pattern: str | list[str]


class ProfilePayload(TypedDict, total=False):
    """Payload type for Profile operations."""
    name: str
    external: Literal["disable", "enable"]
    extended_log: Literal["enable", "disable"]
    signature: ProfileSignatureDict
    constraint: ProfileConstraintDict
    method: ProfileMethodDict
    address_list: ProfileAddresslistDict
    url_access: str | list[str] | list[ProfileUrlaccessItem]
    comment: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ProfileResponse(TypedDict, total=False):
    """Response type for Profile - use with .dict property for typed dict access."""
    name: str
    external: Literal["disable", "enable"]
    extended_log: Literal["enable", "disable"]
    signature: ProfileSignatureDict
    constraint: ProfileConstraintDict
    method: ProfileMethodDict
    address_list: ProfileAddresslistDict
    url_access: list[ProfileUrlaccessItem]
    comment: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ProfileSignatureObject(FortiObject):
    """Nested object for signature field with attribute access."""
    main_class: str | list[str]
    disabled_sub_class: str | list[str]
    disabled_signature: str | list[str]
    credit_card_detection_threshold: int
    custom_signature: str | list[str]


class ProfileConstraintObject(FortiObject):
    """Nested object for constraint field with attribute access."""
    header_length: str
    content_length: str
    param_length: str
    line_length: str
    url_param_length: str
    version: str
    method: str
    hostname: str
    malformed: str
    max_cookie: str
    max_header_line: str
    max_url_param: str
    max_range_segment: str
    exception: str | list[str]


class ProfileMethodObject(FortiObject):
    """Nested object for method field with attribute access."""
    status: Literal["enable", "disable"]
    log: Literal["enable", "disable"]
    severity: Literal["high", "medium", "low"]
    default_allowed_methods: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "others"]
    method_policy: str | list[str]


class ProfileAddresslistObject(FortiObject):
    """Nested object for address-list field with attribute access."""
    status: Literal["enable", "disable"]
    blocked_log: Literal["enable", "disable"]
    severity: Literal["high", "medium", "low"]
    trusted_address: str | list[str]
    blocked_address: str | list[str]


class ProfileObject(FortiObject):
    """Typed FortiObject for Profile with field access."""
    name: str
    external: Literal["disable", "enable"]
    extended_log: Literal["enable", "disable"]
    signature: ProfileSignatureObject
    constraint: ProfileConstraintObject
    method: ProfileMethodObject
    address_list: ProfileAddresslistObject
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
        signature: ProfileSignatureDict | None = ...,
        constraint: ProfileConstraintDict | None = ...,
        method: ProfileMethodDict | None = ...,
        address_list: ProfileAddresslistDict | None = ...,
        url_access: str | list[str] | list[ProfileUrlaccessItem] | None = ...,
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
        signature: ProfileSignatureDict | None = ...,
        constraint: ProfileConstraintDict | None = ...,
        method: ProfileMethodDict | None = ...,
        address_list: ProfileAddresslistDict | None = ...,
        url_access: str | list[str] | list[ProfileUrlaccessItem] | None = ...,
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
        signature: ProfileSignatureDict | None = ...,
        constraint: ProfileConstraintDict | None = ...,
        method: ProfileMethodDict | None = ...,
        address_list: ProfileAddresslistDict | None = ...,
        url_access: str | list[str] | list[ProfileUrlaccessItem] | None = ...,
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