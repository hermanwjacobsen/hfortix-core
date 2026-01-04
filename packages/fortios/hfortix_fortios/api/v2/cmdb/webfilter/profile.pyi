from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for webfilter/profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name.
    comment: NotRequired[str]  # Optional comments.
    feature_set: NotRequired[Literal["flow", "proxy"]]  # Flow/proxy feature set.
    replacemsg_group: NotRequired[str]  # Replacement message group.
    options: NotRequired[Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"]]  # Options.
    https_replacemsg: NotRequired[Literal["enable", "disable"]]  # Enable replacement messages for HTTPS.
    web_flow_log_encoding: NotRequired[Literal["utf-8", "punycode"]]  # Log encoding in flow mode.
    ovrd_perm: NotRequired[Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"]]  # Permitted override types.
    post_action: NotRequired[Literal["normal", "block"]]  # Action taken for HTTP POST traffic.
    override: NotRequired[str]  # Web Filter override settings.
    web: NotRequired[str]  # Web content filtering settings.
    ftgd_wf: NotRequired[str]  # FortiGuard Web Filter settings.
    antiphish: NotRequired[str]  # AntiPhishing profile.
    wisp: NotRequired[Literal["enable", "disable"]]  # Enable/disable web proxy WISP.
    wisp_servers: NotRequired[list[dict[str, Any]]]  # WISP servers.
    wisp_algorithm: NotRequired[Literal["primary-secondary", "round-robin", "auto-learning"]]  # WISP server selection algorithm.
    log_all_url: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging all URLs visited.
    web_content_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging logging blocked web content.
    web_filter_activex_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging ActiveX.
    web_filter_command_block_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging blocked commands.
    web_filter_cookie_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging cookie filtering.
    web_filter_applet_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging Java applets.
    web_filter_jscript_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging JScripts.
    web_filter_js_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging Java scripts.
    web_filter_vbs_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging VBS scripts.
    web_filter_unknown_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging unknown scripts.
    web_filter_referer_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging referrers.
    web_filter_cookie_removal_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging blocked cookies.
    web_url_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging URL filtering.
    web_invalid_domain_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging invalid domain names.
    web_ftgd_err_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging rating errors.
    web_ftgd_quota_usage: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging daily quota usage.
    extended_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended logging for web filtering.
    web_extended_all_action_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended any filter action logging for web fi
    web_antiphishing_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging of AntiPhishing checks.


class Profile:
    """
    Configure Web filter profiles.
    
    Path: webfilter/profile
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: list[dict[str, Any]] | None = ...,
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: list[dict[str, Any]] | None = ...,
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: ProfilePayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> dict[str, Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> dict[str, Any]: ...
    
    @staticmethod
    def schema() -> dict[str, Any]: ...


__all__ = [
    "Profile",
    "ProfilePayload",
]