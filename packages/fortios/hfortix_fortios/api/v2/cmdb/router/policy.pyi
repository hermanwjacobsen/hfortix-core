""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: router/policy
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

class PolicyInputdeviceItem:
    """Nested item for input-device field - supports attribute access."""
    name: str


class PolicySrcItem:
    """Nested item for src field - supports attribute access."""
    subnet: str


class PolicySrcaddrItem:
    """Nested item for srcaddr field - supports attribute access."""
    name: str


class PolicyDstItem:
    """Nested item for dst field - supports attribute access."""
    subnet: str


class PolicyDstaddrItem:
    """Nested item for dstaddr field - supports attribute access."""
    name: str


class PolicyInternetserviceidItem:
    """Nested item for internet-service-id field - supports attribute access."""
    id: int


class PolicyInternetservicecustomItem:
    """Nested item for internet-service-custom field - supports attribute access."""
    name: str


class PolicyInternetservicefortiguardItem:
    """Nested item for internet-service-fortiguard field - supports attribute access."""
    name: str


class PolicyUsersItem:
    """Nested item for users field - supports attribute access."""
    name: str


class PolicyGroupsItem:
    """Nested item for groups field - supports attribute access."""
    name: str


class PolicyPayload(TypedDict, total=False):
    """Payload type for Policy operations."""
    seq_num: int
    input_device: str | list[str] | list[dict[str, Any]] | list[PolicyInputdeviceItem]
    input_device_negate: Literal["enable", "disable"]
    src: str | list[str] | list[dict[str, Any]] | list[PolicySrcItem]
    srcaddr: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddrItem]
    src_negate: Literal["enable", "disable"]
    dst: str | list[str] | list[dict[str, Any]] | list[PolicyDstItem]
    dstaddr: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddrItem]
    dst_negate: Literal["enable", "disable"]
    action: Literal["deny", "permit"]
    protocol: int
    start_port: int
    end_port: int
    start_source_port: int
    end_source_port: int
    gateway: str
    output_device: str
    tos: str
    tos_mask: str
    status: Literal["enable", "disable"]
    comments: str
    internet_service_id: str | list[str] | list[dict[str, Any]] | list[PolicyInternetserviceidItem]
    internet_service_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomItem]
    internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicefortiguardItem]
    users: str | list[str] | list[dict[str, Any]] | list[PolicyUsersItem]
    groups: str | list[str] | list[dict[str, Any]] | list[PolicyGroupsItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class PolicyResponse(TypedDict, total=False):
    """Response type for Policy - use with .dict property for typed dict access."""
    seq_num: int
    input_device: list[PolicyInputdeviceItem]
    input_device_negate: Literal["enable", "disable"]
    src: list[PolicySrcItem]
    srcaddr: list[PolicySrcaddrItem]
    src_negate: Literal["enable", "disable"]
    dst: list[PolicyDstItem]
    dstaddr: list[PolicyDstaddrItem]
    dst_negate: Literal["enable", "disable"]
    action: Literal["deny", "permit"]
    protocol: int
    start_port: int
    end_port: int
    start_source_port: int
    end_source_port: int
    gateway: str
    output_device: str
    tos: str
    tos_mask: str
    status: Literal["enable", "disable"]
    comments: str
    internet_service_id: list[PolicyInternetserviceidItem]
    internet_service_custom: list[PolicyInternetservicecustomItem]
    internet_service_fortiguard: list[PolicyInternetservicefortiguardItem]
    users: list[PolicyUsersItem]
    groups: list[PolicyGroupsItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class PolicyObject(FortiObject):
    """Typed FortiObject for Policy with field access."""
    seq_num: int
    input_device: list[PolicyInputdeviceItem]
    input_device_negate: Literal["enable", "disable"]
    src: list[PolicySrcItem]
    srcaddr: list[PolicySrcaddrItem]
    src_negate: Literal["enable", "disable"]
    dst: list[PolicyDstItem]
    dstaddr: list[PolicyDstaddrItem]
    dst_negate: Literal["enable", "disable"]
    action: Literal["deny", "permit"]
    protocol: int
    start_port: int
    end_port: int
    start_source_port: int
    end_source_port: int
    gateway: str
    output_device: str
    tos: str
    tos_mask: str
    status: Literal["enable", "disable"]
    comments: str
    internet_service_id: list[PolicyInternetserviceidItem]
    internet_service_custom: list[PolicyInternetservicecustomItem]
    internet_service_fortiguard: list[PolicyInternetservicefortiguardItem]
    users: list[PolicyUsersItem]
    groups: list[PolicyGroupsItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class Policy:
    """
    
    Endpoint: router/policy
    Category: cmdb
    MKey: seq-num
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
        seq_num: int,
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
    ) -> PolicyObject: ...
    
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
    ) -> FortiObjectList[PolicyObject]: ...
    
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
        payload_dict: PolicyPayload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | list[PolicyInputdeviceItem] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | list[PolicySrcItem] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddrItem] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | list[PolicyDstItem] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddrItem] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | list[PolicyInternetserviceidItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicefortiguardItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[PolicyUsersItem] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[PolicyGroupsItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> PolicyObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | list[PolicyInputdeviceItem] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | list[PolicySrcItem] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddrItem] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | list[PolicyDstItem] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddrItem] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | list[PolicyInternetserviceidItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicefortiguardItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[PolicyUsersItem] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[PolicyGroupsItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> PolicyObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
    def exists(
        self,
        seq_num: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: PolicyPayload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | list[PolicyInputdeviceItem] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | list[PolicySrcItem] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddrItem] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | list[PolicyDstItem] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddrItem] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | list[PolicyInternetserviceidItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicefortiguardItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[PolicyUsersItem] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[PolicyGroupsItem] | None = ...,
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
    "Policy",
    "PolicyPayload",
    "PolicyResponse",
    "PolicyObject",
]