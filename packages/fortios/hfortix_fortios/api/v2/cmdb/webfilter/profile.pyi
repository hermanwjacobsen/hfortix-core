from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for webfilter/profile payload fields.
    
    Configure Web filter profiles.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
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

# Nested classes for table field children

@final
class ProfileWispserversObject:
    """Typed object for wisp-servers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Server name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class ProfileResponse(TypedDict):
    """
    Type hints for webfilter/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comment: str
    feature_set: Literal["flow", "proxy"]
    replacemsg_group: str
    options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"]
    https_replacemsg: Literal["enable", "disable"]
    web_flow_log_encoding: Literal["utf-8", "punycode"]
    ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"]
    post_action: Literal["normal", "block"]
    override: str
    web: str
    ftgd_wf: str
    antiphish: str
    wisp: Literal["enable", "disable"]
    wisp_servers: list[dict[str, Any]]
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


@final
class ProfileObject:
    """Typed FortiObject for webfilter/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name.
    name: str
    # Optional comments.
    comment: str
    # Flow/proxy feature set.
    feature_set: Literal["flow", "proxy"]
    # Replacement message group.
    replacemsg_group: str
    # Options.
    options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"]
    # Enable replacement messages for HTTPS.
    https_replacemsg: Literal["enable", "disable"]
    # Log encoding in flow mode.
    web_flow_log_encoding: Literal["utf-8", "punycode"]
    # Permitted override types.
    ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"]
    # Action taken for HTTP POST traffic.
    post_action: Literal["normal", "block"]
    # Web Filter override settings.
    override: str
    # Web content filtering settings.
    web: str
    # FortiGuard Web Filter settings.
    ftgd_wf: str
    # AntiPhishing profile.
    antiphish: str
    # Enable/disable web proxy WISP.
    wisp: Literal["enable", "disable"]
    # WISP servers.
    wisp_servers: list[ProfileWispserversObject]  # Table field - list of typed objects
    # WISP server selection algorithm.
    wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"]
    # Enable/disable logging all URLs visited.
    log_all_url: Literal["enable", "disable"]
    # Enable/disable logging logging blocked web content.
    web_content_log: Literal["enable", "disable"]
    # Enable/disable logging ActiveX.
    web_filter_activex_log: Literal["enable", "disable"]
    # Enable/disable logging blocked commands.
    web_filter_command_block_log: Literal["enable", "disable"]
    # Enable/disable logging cookie filtering.
    web_filter_cookie_log: Literal["enable", "disable"]
    # Enable/disable logging Java applets.
    web_filter_applet_log: Literal["enable", "disable"]
    # Enable/disable logging JScripts.
    web_filter_jscript_log: Literal["enable", "disable"]
    # Enable/disable logging Java scripts.
    web_filter_js_log: Literal["enable", "disable"]
    # Enable/disable logging VBS scripts.
    web_filter_vbs_log: Literal["enable", "disable"]
    # Enable/disable logging unknown scripts.
    web_filter_unknown_log: Literal["enable", "disable"]
    # Enable/disable logging referrers.
    web_filter_referer_log: Literal["enable", "disable"]
    # Enable/disable logging blocked cookies.
    web_filter_cookie_removal_log: Literal["enable", "disable"]
    # Enable/disable logging URL filtering.
    web_url_log: Literal["enable", "disable"]
    # Enable/disable logging invalid domain names.
    web_invalid_domain_log: Literal["enable", "disable"]
    # Enable/disable logging rating errors.
    web_ftgd_err_log: Literal["enable", "disable"]
    # Enable/disable logging daily quota usage.
    web_ftgd_quota_usage: Literal["enable", "disable"]
    # Enable/disable extended logging for web filtering.
    extended_log: Literal["enable", "disable"]
    # Enable/disable extended any filter action logging for web filtering.
    web_extended_all_action_log: Literal["enable", "disable"]
    # Enable/disable logging of AntiPhishing checks.
    web_antiphishing_log: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Profile:
    """
    Configure Web filter profiles.
    
    Path: webfilter/profile
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[ProfileObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> ProfileResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> ProfileResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[ProfileResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> ProfileObject | list[ProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
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
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
    def post(
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
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
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
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
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
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
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
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
    def put(
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
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
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
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
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
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProfileObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    "ProfileObject",
]