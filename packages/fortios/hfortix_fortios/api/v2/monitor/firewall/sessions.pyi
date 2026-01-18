""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/sessions
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

class SessionsPayload(TypedDict, total=False):
    """Payload type for Sessions operations."""
    ip_version: str
    count: int
    summary: str
    srcport: str
    policyid: str
    security_policyid: str
    application: str
    protocol: str
    dstport: str
    srcintf: str
    dstintf: str
    srcintfrole: str
    dstintfrole: str
    srcaddr: str
    srcaddr6: str
    srcuuid: str
    dstaddr: str
    dstaddr6: str
    dstuuid: str
    username: str
    shaper: str
    country: str
    owner: str
    natsourceaddress: str
    natsourceport: str
    since: str
    seconds: str
    fortiasic: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class SessionsResponse(TypedDict, total=False):
    """Response type for Sessions - use with .dict property for typed dict access."""
    ip_version: str
    count: int
    summary: str
    srcport: str
    policyid: str
    security_policyid: str
    application: str
    protocol: str
    dstport: str
    srcintf: str
    dstintf: str
    srcintfrole: str
    dstintfrole: str
    srcaddr: str
    srcaddr6: str
    srcuuid: str
    dstaddr: str
    dstaddr6: str
    dstuuid: str
    username: str
    shaper: str
    country: str
    owner: str
    natsourceaddress: str
    natsourceport: str
    since: str
    seconds: str
    fortiasic: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class SessionsObject(FortiObject):
    """Typed FortiObject for Sessions with field access."""
    ip_version: str
    count: int
    summary: str
    srcport: str
    policyid: str
    security_policyid: str
    application: str
    protocol: str
    dstport: str
    srcintf: str
    dstintf: str
    srcintfrole: str
    dstintfrole: str
    srcaddr: str
    srcaddr6: str
    srcuuid: str
    dstaddr: str
    dstaddr6: str
    dstuuid: str
    username: str
    shaper: str
    country: str
    owner: str
    natsourceaddress: str
    natsourceport: str
    since: str
    seconds: str
    fortiasic: str


# ================================================================
# Main Endpoint Class
# ================================================================

class Sessions:
    """
    
    Endpoint: firewall/sessions
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
        ip_version: Literal["ipv4", "ipv6", "ipboth"] | None = ...,
        count: int,
        summary: bool | None = ...,
        srcport: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        application: str | None = ...,
        protocol: Literal["all", "igmp", "tcp", "udp", "icmp", "etc"] | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcintfrole: list[str] | None = ...,
        dstintfrole: list[str] | None = ...,
        srcaddr: str | None = ...,
        srcaddr6: str | None = ...,
        srcuuid: str | None = ...,
        dstaddr: str | None = ...,
        dstaddr6: str | None = ...,
        dstuuid: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        country: str | None = ...,
        owner: str | None = ...,
        natsourceaddress: str | None = ...,
        natsourceport: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        fortiasic: str | None = ...,
        nturbo: str | None = ...,
        filter: str | list[str] | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> SessionsObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: SessionsPayload | None = ...,
        ip_version: str | None = ...,
        count: int | None = ...,
        summary: str | None = ...,
        srcport: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        application: str | None = ...,
        protocol: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintfrole: str | None = ...,
        srcaddr: str | None = ...,
        srcaddr6: str | None = ...,
        srcuuid: str | None = ...,
        dstaddr: str | None = ...,
        dstaddr6: str | None = ...,
        dstuuid: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        country: str | None = ...,
        owner: str | None = ...,
        natsourceaddress: str | None = ...,
        natsourceport: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        fortiasic: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> SessionsObject: ...


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
        payload_dict: SessionsPayload | None = ...,
        ip_version: str | None = ...,
        count: int | None = ...,
        summary: str | None = ...,
        srcport: str | None = ...,
        policyid: str | None = ...,
        security_policyid: str | None = ...,
        application: str | None = ...,
        protocol: str | None = ...,
        dstport: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcintfrole: str | None = ...,
        dstintfrole: str | None = ...,
        srcaddr: str | None = ...,
        srcaddr6: str | None = ...,
        srcuuid: str | None = ...,
        dstaddr: str | None = ...,
        dstaddr6: str | None = ...,
        dstuuid: str | None = ...,
        username: str | None = ...,
        shaper: str | None = ...,
        country: str | None = ...,
        owner: str | None = ...,
        natsourceaddress: str | None = ...,
        natsourceport: str | None = ...,
        since: str | None = ...,
        seconds: str | None = ...,
        fortiasic: str | None = ...,
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
    "Sessions",
    "SessionsPayload",
    "SessionsResponse",
    "SessionsObject",
]