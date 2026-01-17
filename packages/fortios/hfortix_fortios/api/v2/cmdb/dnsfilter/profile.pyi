""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: dnsfilter/profile
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

class ProfileExternalipblocklistItem:
    """Nested item for external-ip-blocklist field - supports attribute access."""
    name: str


class ProfileDnstranslationItem:
    """Nested item for dns-translation field - supports attribute access."""
    id: int
    addr_type: Literal["ipv4", "ipv6"]
    src: str
    dst: str
    netmask: str
    status: Literal["enable", "disable"]
    src6: str
    dst6: str
    prefix: int


class ProfileTransparentdnsdatabaseItem:
    """Nested item for transparent-dns-database field - supports attribute access."""
    name: str


class ProfilePayload(TypedDict, total=False):
    """Payload type for Profile operations."""
    name: str
    comment: str
    domain_filter: str
    ftgd_dns: str
    log_all_domain: Literal["enable", "disable"]
    sdns_ftgd_err_log: Literal["enable", "disable"]
    sdns_domain_log: Literal["enable", "disable"]
    block_action: Literal["block", "redirect", "block-sevrfail"]
    redirect_portal: str
    redirect_portal6: str
    block_botnet: Literal["disable", "enable"]
    safe_search: Literal["disable", "enable"]
    youtube_restrict: Literal["strict", "moderate", "none"]
    external_ip_blocklist: str | list[str] | list[dict[str, Any]] | list[ProfileExternalipblocklistItem]
    dns_translation: str | list[str] | list[dict[str, Any]] | list[ProfileDnstranslationItem]
    transparent_dns_database: str | list[str] | list[dict[str, Any]] | list[ProfileTransparentdnsdatabaseItem]
    strip_ech: Literal["disable", "enable"]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ProfileResponse(TypedDict, total=False):
    """Response type for Profile - use with .dict property for typed dict access."""
    name: str
    comment: str
    domain_filter: str
    ftgd_dns: str
    log_all_domain: Literal["enable", "disable"]
    sdns_ftgd_err_log: Literal["enable", "disable"]
    sdns_domain_log: Literal["enable", "disable"]
    block_action: Literal["block", "redirect", "block-sevrfail"]
    redirect_portal: str
    redirect_portal6: str
    block_botnet: Literal["disable", "enable"]
    safe_search: Literal["disable", "enable"]
    youtube_restrict: Literal["strict", "moderate", "none"]
    external_ip_blocklist: list[ProfileExternalipblocklistItem]
    dns_translation: list[ProfileDnstranslationItem]
    transparent_dns_database: list[ProfileTransparentdnsdatabaseItem]
    strip_ech: Literal["disable", "enable"]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ProfileObject(FortiObject):
    """Typed FortiObject for Profile with field access."""
    name: str
    comment: str
    domain_filter: str
    ftgd_dns: str
    log_all_domain: Literal["enable", "disable"]
    sdns_ftgd_err_log: Literal["enable", "disable"]
    sdns_domain_log: Literal["enable", "disable"]
    block_action: Literal["block", "redirect", "block-sevrfail"]
    redirect_portal: str
    redirect_portal6: str
    block_botnet: Literal["disable", "enable"]
    safe_search: Literal["disable", "enable"]
    youtube_restrict: Literal["strict", "moderate", "none"]
    external_ip_blocklist: list[ProfileExternalipblocklistItem]
    dns_translation: list[ProfileDnstranslationItem]
    transparent_dns_database: list[ProfileTransparentdnsdatabaseItem]
    strip_ech: Literal["disable", "enable"]


# ================================================================
# Main Endpoint Class
# ================================================================

class Profile:
    """
    
    Endpoint: dnsfilter/profile
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
        comment: str | None = ...,
        domain_filter: str | None = ...,
        ftgd_dns: str | None = ...,
        log_all_domain: Literal["enable", "disable"] | None = ...,
        sdns_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        sdns_domain_log: Literal["enable", "disable"] | None = ...,
        block_action: Literal["block", "redirect", "block-sevrfail"] | None = ...,
        redirect_portal: str | None = ...,
        redirect_portal6: str | None = ...,
        block_botnet: Literal["disable", "enable"] | None = ...,
        safe_search: Literal["disable", "enable"] | None = ...,
        youtube_restrict: Literal["strict", "moderate", "none"] | None = ...,
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | list[ProfileExternalipblocklistItem] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | list[ProfileDnstranslationItem] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | list[ProfileTransparentdnsdatabaseItem] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
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
        comment: str | None = ...,
        domain_filter: str | None = ...,
        ftgd_dns: str | None = ...,
        log_all_domain: Literal["enable", "disable"] | None = ...,
        sdns_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        sdns_domain_log: Literal["enable", "disable"] | None = ...,
        block_action: Literal["block", "redirect", "block-sevrfail"] | None = ...,
        redirect_portal: str | None = ...,
        redirect_portal6: str | None = ...,
        block_botnet: Literal["disable", "enable"] | None = ...,
        safe_search: Literal["disable", "enable"] | None = ...,
        youtube_restrict: Literal["strict", "moderate", "none"] | None = ...,
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | list[ProfileExternalipblocklistItem] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | list[ProfileDnstranslationItem] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | list[ProfileTransparentdnsdatabaseItem] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
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
        comment: str | None = ...,
        domain_filter: str | None = ...,
        ftgd_dns: str | None = ...,
        log_all_domain: Literal["enable", "disable"] | None = ...,
        sdns_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        sdns_domain_log: Literal["enable", "disable"] | None = ...,
        block_action: Literal["block", "redirect", "block-sevrfail"] | None = ...,
        redirect_portal: str | None = ...,
        redirect_portal6: str | None = ...,
        block_botnet: Literal["disable", "enable"] | None = ...,
        safe_search: Literal["disable", "enable"] | None = ...,
        youtube_restrict: Literal["strict", "moderate", "none"] | None = ...,
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | list[ProfileExternalipblocklistItem] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | list[ProfileDnstranslationItem] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | list[ProfileTransparentdnsdatabaseItem] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
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