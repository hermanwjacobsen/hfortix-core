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

class ProfileOverrideDict(TypedDict, total=False):
    """Nested object type for override field."""
    ovrd_cookie: Literal["allow", "deny"]
    ovrd_scope: Literal["user", "user-group", "ip", "browser", "ask"]
    profile_type: Literal["list", "radius"]
    ovrd_dur_mode: Literal["constant", "ask"]
    ovrd_dur: str
    profile_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]
    ovrd_user_group: str | list[str]
    profile: str | list[str]


class ProfileWebDict(TypedDict, total=False):
    """Nested object type for web field."""
    bword_threshold: int
    bword_table: int
    urlfilter_table: int
    content_header_list: int
    blocklist: Literal["enable", "disable"]
    allowlist: Literal["exempt-av", "exempt-webcontent", "exempt-activex-java-cookie", "exempt-dlp", "exempt-rangeblock", "extended-log-others"]
    safe_search: Literal["url", "header"]
    youtube_restrict: Literal["none", "strict", "moderate"]
    vimeo_restrict: str
    log_search: Literal["enable", "disable"]
    keyword_match: str | list[str]


class ProfileFtgdwfDict(TypedDict, total=False):
    """Nested object type for ftgd-wf field."""
    options: Literal["error-allow", "rate-server-ip", "connect-request-bypass", "ftgd-disable"]
    exempt_quota: str | list[str]
    ovrd: str | list[str]
    filters: str | list[str]
    risk: str | list[str]
    quota: str | list[str]
    max_quota_timeout: int
    rate_javascript_urls: Literal["disable", "enable"]
    rate_css_urls: Literal["disable", "enable"]
    rate_crl_urls: Literal["disable", "enable"]


class ProfileAntiphishDict(TypedDict, total=False):
    """Nested object type for antiphish field."""
    status: Literal["enable", "disable"]
    default_action: Literal["exempt", "log", "block"]
    check_uri: Literal["enable", "disable"]
    check_basic_auth: Literal["enable", "disable"]
    check_username_only: Literal["enable", "disable"]
    max_body_len: int
    inspection_entries: str | list[str]
    custom_patterns: str | list[str]
    authentication: Literal["domain-controller", "ldap"]
    domain_controller: str
    ldap: str


class ProfileWispserversItem(TypedDict, total=False):
    """Nested item for wisp-servers field."""
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
    override: ProfileOverrideDict
    web: ProfileWebDict
    ftgd_wf: ProfileFtgdwfDict
    antiphish: ProfileAntiphishDict
    wisp: Literal["enable", "disable"]
    wisp_servers: str | list[str] | list[ProfileWispserversItem]
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
    override: ProfileOverrideDict
    web: ProfileWebDict
    ftgd_wf: ProfileFtgdwfDict
    antiphish: ProfileAntiphishDict
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


class ProfileOverrideObject(FortiObject):
    """Nested object for override field with attribute access."""
    ovrd_cookie: Literal["allow", "deny"]
    ovrd_scope: Literal["user", "user-group", "ip", "browser", "ask"]
    profile_type: Literal["list", "radius"]
    ovrd_dur_mode: Literal["constant", "ask"]
    ovrd_dur: str
    profile_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]
    ovrd_user_group: str | list[str]
    profile: str | list[str]


class ProfileWebObject(FortiObject):
    """Nested object for web field with attribute access."""
    bword_threshold: int
    bword_table: int
    urlfilter_table: int
    content_header_list: int
    blocklist: Literal["enable", "disable"]
    allowlist: Literal["exempt-av", "exempt-webcontent", "exempt-activex-java-cookie", "exempt-dlp", "exempt-rangeblock", "extended-log-others"]
    safe_search: Literal["url", "header"]
    youtube_restrict: Literal["none", "strict", "moderate"]
    vimeo_restrict: str
    log_search: Literal["enable", "disable"]
    keyword_match: str | list[str]


class ProfileFtgdwfObject(FortiObject):
    """Nested object for ftgd-wf field with attribute access."""
    options: Literal["error-allow", "rate-server-ip", "connect-request-bypass", "ftgd-disable"]
    exempt_quota: str | list[str]
    ovrd: str | list[str]
    filters: str | list[str]
    risk: str | list[str]
    quota: str | list[str]
    max_quota_timeout: int
    rate_javascript_urls: Literal["disable", "enable"]
    rate_css_urls: Literal["disable", "enable"]
    rate_crl_urls: Literal["disable", "enable"]


class ProfileAntiphishObject(FortiObject):
    """Nested object for antiphish field with attribute access."""
    status: Literal["enable", "disable"]
    default_action: Literal["exempt", "log", "block"]
    check_uri: Literal["enable", "disable"]
    check_basic_auth: Literal["enable", "disable"]
    check_username_only: Literal["enable", "disable"]
    max_body_len: int
    inspection_entries: str | list[str]
    custom_patterns: str | list[str]
    authentication: Literal["domain-controller", "ldap"]
    domain_controller: str
    ldap: str


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
    override: ProfileOverrideObject
    web: ProfileWebObject
    ftgd_wf: ProfileFtgdwfObject
    antiphish: ProfileAntiphishObject
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
        override: ProfileOverrideDict | None = ...,
        web: ProfileWebDict | None = ...,
        ftgd_wf: ProfileFtgdwfDict | None = ...,
        antiphish: ProfileAntiphishDict | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[ProfileWispserversItem] | None = ...,
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
        override: ProfileOverrideDict | None = ...,
        web: ProfileWebDict | None = ...,
        ftgd_wf: ProfileFtgdwfDict | None = ...,
        antiphish: ProfileAntiphishDict | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[ProfileWispserversItem] | None = ...,
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
        override: ProfileOverrideDict | None = ...,
        web: ProfileWebDict | None = ...,
        ftgd_wf: ProfileFtgdwfDict | None = ...,
        antiphish: ProfileAntiphishDict | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[ProfileWispserversItem] | None = ...,
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