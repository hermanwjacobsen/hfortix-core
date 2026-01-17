""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/central_snat_map
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

class CentralSnatMapSrcintfItem:
    """Nested item for srcintf field - supports attribute access."""
    name: str


class CentralSnatMapDstintfItem:
    """Nested item for dstintf field - supports attribute access."""
    name: str


class CentralSnatMapOrigaddrItem:
    """Nested item for orig-addr field - supports attribute access."""
    name: str


class CentralSnatMapOrigaddr6Item:
    """Nested item for orig-addr6 field - supports attribute access."""
    name: str


class CentralSnatMapDstaddrItem:
    """Nested item for dst-addr field - supports attribute access."""
    name: str


class CentralSnatMapDstaddr6Item:
    """Nested item for dst-addr6 field - supports attribute access."""
    name: str


class CentralSnatMapNatippoolItem:
    """Nested item for nat-ippool field - supports attribute access."""
    name: str


class CentralSnatMapNatippool6Item:
    """Nested item for nat-ippool6 field - supports attribute access."""
    name: str


class CentralSnatMapPayload(TypedDict, total=False):
    """Payload type for CentralSnatMap operations."""
    policyid: int
    uuid: str
    status: Literal["enable", "disable"]
    type: Literal["ipv4", "ipv6"]
    srcintf: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapSrcintfItem]
    dstintf: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstintfItem]
    orig_addr: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapOrigaddrItem]
    orig_addr6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapOrigaddr6Item]
    dst_addr: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstaddrItem]
    dst_addr6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstaddr6Item]
    protocol: int
    orig_port: str
    nat: Literal["disable", "enable"]
    nat46: Literal["enable", "disable"]
    nat64: Literal["enable", "disable"]
    nat_ippool: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapNatippoolItem]
    nat_ippool6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapNatippool6Item]
    port_preserve: Literal["enable", "disable"]
    port_random: Literal["enable", "disable"]
    nat_port: str
    dst_port: str
    comments: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class CentralSnatMapResponse(TypedDict, total=False):
    """Response type for CentralSnatMap - use with .dict property for typed dict access."""
    policyid: int
    uuid: str
    status: Literal["enable", "disable"]
    type: Literal["ipv4", "ipv6"]
    srcintf: list[CentralSnatMapSrcintfItem]
    dstintf: list[CentralSnatMapDstintfItem]
    orig_addr: list[CentralSnatMapOrigaddrItem]
    orig_addr6: list[CentralSnatMapOrigaddr6Item]
    dst_addr: list[CentralSnatMapDstaddrItem]
    dst_addr6: list[CentralSnatMapDstaddr6Item]
    protocol: int
    orig_port: str
    nat: Literal["disable", "enable"]
    nat46: Literal["enable", "disable"]
    nat64: Literal["enable", "disable"]
    nat_ippool: list[CentralSnatMapNatippoolItem]
    nat_ippool6: list[CentralSnatMapNatippool6Item]
    port_preserve: Literal["enable", "disable"]
    port_random: Literal["enable", "disable"]
    nat_port: str
    dst_port: str
    comments: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class CentralSnatMapObject(FortiObject):
    """Typed FortiObject for CentralSnatMap with field access."""
    policyid: int
    uuid: str
    status: Literal["enable", "disable"]
    type: Literal["ipv4", "ipv6"]
    srcintf: list[CentralSnatMapSrcintfItem]
    dstintf: list[CentralSnatMapDstintfItem]
    orig_addr: list[CentralSnatMapOrigaddrItem]
    orig_addr6: list[CentralSnatMapOrigaddr6Item]
    dst_addr: list[CentralSnatMapDstaddrItem]
    dst_addr6: list[CentralSnatMapDstaddr6Item]
    protocol: int
    orig_port: str
    nat: Literal["disable", "enable"]
    nat46: Literal["enable", "disable"]
    nat64: Literal["enable", "disable"]
    nat_ippool: list[CentralSnatMapNatippoolItem]
    nat_ippool6: list[CentralSnatMapNatippool6Item]
    port_preserve: Literal["enable", "disable"]
    port_random: Literal["enable", "disable"]
    nat_port: str
    dst_port: str
    comments: str


# ================================================================
# Main Endpoint Class
# ================================================================

class CentralSnatMap:
    """
    
    Endpoint: firewall/central_snat_map
    Category: cmdb
    MKey: policyid
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
        policyid: int,
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
    ) -> CentralSnatMapObject: ...
    
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
    ) -> FortiObjectList[CentralSnatMapObject]: ...
    
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
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> CentralSnatMapObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> CentralSnatMapObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
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
    "CentralSnatMap",
    "CentralSnatMapPayload",
    "CentralSnatMapResponse",
    "CentralSnatMapObject",
]