""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: webfilter/profile
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

class ProfileWispserversItem:
    """Nested item for wisp-servers field - supports attribute access."""
    name: str


class ProfilePayload(TypedDict, total=False):
    """Payload type for Profile operations."""
    name: str
    comment: str
    feature_set: Literal["flow", "proxy"]
    replacemsg_group: str
    options: str | list[str]
    https_replacemsg: Literal["enable", "disable"]
    web_flow_log_encoding: Literal["utf-8", "punycode"]
    ovrd_perm: str | list[str]
    post_action: Literal["normal", "block"]
    override: str
    web: str
    ftgd_wf: str
    antiphish: str
    wisp: Literal["enable", "disable"]
    wisp_servers: str | list[str] | list[dict[str, Any]] | list[ProfileWispserversItem]
    wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"]
    log_all_url: Literal["enable", "disable"]
    web_content_log: Literal["enable", "disable"]
    web_filter_activex_log: Literal["enable", "disable"]
    web_filter_command_block_log: Literal["enable", "disable"]
    web_filter_cookie_log: Literal["enable", "disable"]
    web_filter_applet_log: Literal["enable", "disable"]
    web_filter_jscript_log: Literal["enable", "disable"]
    web_filter_js_log: Literal["enable", "disable"]
    web_filter_vbs_log: Literal["enable", "disable"]
    web_filter_unknown_log: Literal["enable", "disable"]
    web_filter_referer_log: Literal["enable", "disable"]
    web_filter_cookie_removal_log: Literal["enable", "disable"]
    web_url_log: Literal["enable", "disable"]
    web_invalid_domain_log: Literal["enable", "disable"]
    web_ftgd_err_log: Literal["enable", "disable"]
    web_ftgd_quota_usage: Literal["enable", "disable"]
    extended_log: Literal["enable", "disable"]
    web_extended_all_action_log: Literal["enable", "disable"]
    web_antiphishing_log: Literal["enable", "disable"]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ProfileResponse(TypedDict, total=False):
    """Response type for Profile - use with .dict property for typed dict access."""
    name: str
    comment: str
    feature_set: Literal["flow", "proxy"]
    replacemsg_group: str
    options: str
    https_replacemsg: Literal["enable", "disable"]
    web_flow_log_encoding: Literal["utf-8", "punycode"]
    ovrd_perm: str
    post_action: Literal["normal", "block"]
    override: str
    web: str
    ftgd_wf: str
    antiphish: str
    wisp: Literal["enable", "disable"]
    wisp_servers: list[ProfileWispserversItem]
    wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"]
    log_all_url: Literal["enable", "disable"]
    web_content_log: Literal["enable", "disable"]
    web_filter_activex_log: Literal["enable", "disable"]
    web_filter_command_block_log: Literal["enable", "disable"]
    web_filter_cookie_log: Literal["enable", "disable"]
    web_filter_applet_log: Literal["enable", "disable"]
    web_filter_jscript_log: Literal["enable", "disable"]
    web_filter_js_log: Literal["enable", "disable"]
    web_filter_vbs_log: Literal["enable", "disable"]
    web_filter_unknown_log: Literal["enable", "disable"]
    web_filter_referer_log: Literal["enable", "disable"]
    web_filter_cookie_removal_log: Literal["enable", "disable"]
    web_url_log: Literal["enable", "disable"]
    web_invalid_domain_log: Literal["enable", "disable"]
    web_ftgd_err_log: Literal["enable", "disable"]
    web_ftgd_quota_usage: Literal["enable", "disable"]
    extended_log: Literal["enable", "disable"]
    web_extended_all_action_log: Literal["enable", "disable"]
    web_antiphishing_log: Literal["enable", "disable"]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ProfileObject(FortiObject):
    """Typed FortiObject for Profile with field access."""
    name: str
    comment: str
    feature_set: Literal["flow", "proxy"]
    replacemsg_group: str
    options: str
    https_replacemsg: Literal["enable", "disable"]
    web_flow_log_encoding: Literal["utf-8", "punycode"]
    ovrd_perm: str
    post_action: Literal["normal", "block"]
    override: str
    web: str
    ftgd_wf: str
    antiphish: str
    wisp: Literal["enable", "disable"]
    wisp_servers: list[ProfileWispserversItem]
    wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"]
    log_all_url: Literal["enable", "disable"]
    web_content_log: Literal["enable", "disable"]
    web_filter_activex_log: Literal["enable", "disable"]
    web_filter_command_block_log: Literal["enable", "disable"]
    web_filter_cookie_log: Literal["enable", "disable"]
    web_filter_applet_log: Literal["enable", "disable"]
    web_filter_jscript_log: Literal["enable", "disable"]
    web_filter_js_log: Literal["enable", "disable"]
    web_filter_vbs_log: Literal["enable", "disable"]
    web_filter_unknown_log: Literal["enable", "disable"]
    web_filter_referer_log: Literal["enable", "disable"]
    web_filter_cookie_removal_log: Literal["enable", "disable"]
    web_url_log: Literal["enable", "disable"]
    web_invalid_domain_log: Literal["enable", "disable"]
    web_ftgd_err_log: Literal["enable", "disable"]
    web_ftgd_quota_usage: Literal["enable", "disable"]
    extended_log: Literal["enable", "disable"]
    web_extended_all_action_log: Literal["enable", "disable"]
    web_antiphishing_log: Literal["enable", "disable"]


# ================================================================
# Main Endpoint Class
# ================================================================

class Profile:
    """
    
    Endpoint: webfilter/profile
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
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        options: str | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: str | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | list[ProfileWispserversItem] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
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
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        options: str | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: str | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | list[ProfileWispserversItem] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
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
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | list[ProfileWispserversItem] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
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