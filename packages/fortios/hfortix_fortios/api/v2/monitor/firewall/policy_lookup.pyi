""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/policy_lookup
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

class PolicyLookupPayload(TypedDict, total=False):
    """Payload type for PolicyLookup operations."""
    ipv6: bool
    srcintf: str
    sourceport: int
    sourceip: str
    protocol: str
    dest: str
    destport: int
    icmptype: int
    icmpcode: int
    policy_type: Literal["policy", "proxy"]
    auth_type: Literal["user", "group", "saml", "ldap"]
    user_group: int | str | list[int | str]
    server_name: str
    user_db: str
    group_attr_type: Literal["name", "id"]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class PolicyLookupResponse(TypedDict, total=False):
    """Response type for PolicyLookup - use with .dict property for typed dict access."""
    ipv6: bool
    srcintf: str
    sourceport: int
    sourceip: str
    protocol: str
    dest: str
    destport: int
    icmptype: int
    icmpcode: int
    policy_type: Literal["policy", "proxy"]
    auth_type: Literal["user", "group", "saml", "ldap"]
    user_group: list[str]
    server_name: str
    user_db: str
    group_attr_type: Literal["name", "id"]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class PolicyLookupObject(FortiObject):
    """Typed FortiObject for PolicyLookup with field access."""
    ipv6: bool
    srcintf: str
    sourceport: int
    sourceip: str
    protocol: str
    dest: str
    destport: int
    icmptype: int
    icmpcode: int
    policy_type: Literal["policy", "proxy"]
    auth_type: Literal["user", "group", "saml", "ldap"]
    user_group: list[str]
    server_name: str
    user_db: str
    group_attr_type: Literal["name", "id"]


# ================================================================
# Main Endpoint Class
# ================================================================

class PolicyLookup:
    """
    
    Endpoint: firewall/policy_lookup
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
        ipv6: bool | None = ...,
        srcintf: str,
        sourceport: int | None = ...,
        sourceip: str,
        protocol: str,
        dest: str,
        destport: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        policy_type: Literal["policy", "proxy"] | None = ...,
        auth_type: Literal["user", "group", "saml", "ldap"] | None = ...,
        user_group: list[str] | None = ...,
        server_name: str | None = ...,
        user_db: str | None = ...,
        group_attr_type: Literal["name", "id"] | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> PolicyLookupObject: ...
    


    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: PolicyLookupPayload | None = ...,
        ipv6: bool | None = ...,
        srcintf: str | None = ...,
        sourceport: int | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        policy_type: Literal["policy", "proxy"] | None = ...,
        auth_type: Literal["user", "group", "saml", "ldap"] | None = ...,
        user_group: int | str | list[int | str] | None = ...,
        server_name: str | None = ...,
        user_db: str | None = ...,
        group_attr_type: Literal["name", "id"] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> PolicyLookupObject: ...


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
        payload_dict: PolicyLookupPayload | None = ...,
        ipv6: bool | None = ...,
        srcintf: str | None = ...,
        sourceport: int | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        policy_type: Literal["policy", "proxy"] | None = ...,
        auth_type: Literal["user", "group", "saml", "ldap"] | None = ...,
        user_group: int | str | list[int | str] | None = ...,
        server_name: str | None = ...,
        user_db: str | None = ...,
        group_attr_type: Literal["name", "id"] | None = ...,
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
    "PolicyLookup",
    "PolicyLookupPayload",
    "PolicyLookupResponse",
    "PolicyLookupObject",
]