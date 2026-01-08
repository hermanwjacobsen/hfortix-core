from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class WebPortalPayload(TypedDict, total=False):
    """
    Type hints for ztna/web_portal payload fields.
    
    Configure ztna web-portal.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.authentication.rule.RuleEndpoint` (via: auth-rule)
        - :class:`~.firewall.access-proxy-virtual-host.AccessProxyVirtualHostEndpoint` (via: auth-virtual-host, host)
        - :class:`~.firewall.decrypted-traffic-mirror.DecryptedTrafficMirrorEndpoint` (via: decrypted-traffic-mirror)
        - :class:`~.firewall.vip.VipEndpoint` (via: vip)
        - :class:`~.firewall.vip6.Vip6Endpoint` (via: vip6)

    **Usage:**
        payload: WebPortalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # ZTNA proxy name.
    vip: NotRequired[str]  # Virtual IP name.
    host: NotRequired[str]  # Virtual or real host name.
    decrypted_traffic_mirror: NotRequired[str]  # Decrypted traffic mirror.
    log_blocked_traffic: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging of blocked traffic.
    auth_portal: NotRequired[Literal["disable", "enable"]]  # Enable/disable authentication portal.
    auth_virtual_host: NotRequired[str]  # Virtual host for authentication portal.
    vip6: NotRequired[str]  # Virtual IPv6 name.
    auth_rule: NotRequired[str]  # Authentication Rule.
    display_bookmark: NotRequired[Literal["enable", "disable"]]  # Enable to display the web portal bookmark widget.
    focus_bookmark: NotRequired[Literal["enable", "disable"]]  # Enable to prioritize the placement of the bookmark section o
    display_status: NotRequired[Literal["enable", "disable"]]  # Enable to display the web portal status widget.
    display_history: NotRequired[Literal["enable", "disable"]]  # Enable to display the web portal user login history widget.
    policy_auth_sso: NotRequired[Literal["enable", "disable"]]  # Enable policy sso authentication.
    heading: NotRequired[str]  # Web portal heading message.
    theme: NotRequired[Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"]]  # Web portal color scheme.
    clipboard: NotRequired[Literal["enable", "disable"]]  # Enable to support RDP/VPC clipboard functionality.
    default_window_width: NotRequired[int]  # Screen width (range from 0 - 65535, default = 1024).
    default_window_height: NotRequired[int]  # Screen height (range from 0 - 65535, default = 768).
    cookie_age: NotRequired[int]  # Time in minutes that client web browsers should keep a cooki
    forticlient_download: NotRequired[Literal["enable", "disable"]]  # Enable/disable download option for FortiClient.
    customize_forticlient_download_url: NotRequired[Literal["enable", "disable"]]  # Enable support of customized download URL for FortiClient.
    windows_forticlient_download_url: NotRequired[str]  # Download URL for Windows FortiClient.
    macos_forticlient_download_url: NotRequired[str]  # Download URL for Mac FortiClient.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class WebPortalResponse(TypedDict):
    """
    Type hints for ztna/web_portal API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    vip: str
    host: str
    decrypted_traffic_mirror: str
    log_blocked_traffic: Literal["disable", "enable"]
    auth_portal: Literal["disable", "enable"]
    auth_virtual_host: str
    vip6: str
    auth_rule: str
    display_bookmark: Literal["enable", "disable"]
    focus_bookmark: Literal["enable", "disable"]
    display_status: Literal["enable", "disable"]
    display_history: Literal["enable", "disable"]
    policy_auth_sso: Literal["enable", "disable"]
    heading: str
    theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"]
    clipboard: Literal["enable", "disable"]
    default_window_width: int
    default_window_height: int
    cookie_age: int
    forticlient_download: Literal["enable", "disable"]
    customize_forticlient_download_url: Literal["enable", "disable"]
    windows_forticlient_download_url: str
    macos_forticlient_download_url: str


@final
class WebPortalObject:
    """Typed FortiObject for ztna/web_portal with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # ZTNA proxy name.
    name: str
    # Virtual IP name.
    vip: str
    # Virtual or real host name.
    host: str
    # Decrypted traffic mirror.
    decrypted_traffic_mirror: str
    # Enable/disable logging of blocked traffic.
    log_blocked_traffic: Literal["disable", "enable"]
    # Enable/disable authentication portal.
    auth_portal: Literal["disable", "enable"]
    # Virtual host for authentication portal.
    auth_virtual_host: str
    # Virtual IPv6 name.
    vip6: str
    # Authentication Rule.
    auth_rule: str
    # Enable to display the web portal bookmark widget.
    display_bookmark: Literal["enable", "disable"]
    # Enable to prioritize the placement of the bookmark section over the quick-connec
    focus_bookmark: Literal["enable", "disable"]
    # Enable to display the web portal status widget.
    display_status: Literal["enable", "disable"]
    # Enable to display the web portal user login history widget.
    display_history: Literal["enable", "disable"]
    # Enable policy sso authentication.
    policy_auth_sso: Literal["enable", "disable"]
    # Web portal heading message.
    heading: str
    # Web portal color scheme.
    theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"]
    # Enable to support RDP/VPC clipboard functionality.
    clipboard: Literal["enable", "disable"]
    # Screen width (range from 0 - 65535, default = 1024).
    default_window_width: int
    # Screen height (range from 0 - 65535, default = 768).
    default_window_height: int
    # Time in minutes that client web browsers should keep a cookie. Default is 60 min
    cookie_age: int
    # Enable/disable download option for FortiClient.
    forticlient_download: Literal["enable", "disable"]
    # Enable support of customized download URL for FortiClient.
    customize_forticlient_download_url: Literal["enable", "disable"]
    # Download URL for Windows FortiClient.
    windows_forticlient_download_url: str
    # Download URL for Mac FortiClient.
    macos_forticlient_download_url: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> WebPortalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class WebPortal:
    """
    Configure ztna web-portal.
    
    Path: ztna/web_portal
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
    ) -> WebPortalObject: ...
    
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
    ) -> WebPortalObject: ...
    
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
    ) -> list[WebPortalObject]: ...
    
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
    ) -> WebPortalResponse: ...
    
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
    ) -> WebPortalResponse: ...
    
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
    ) -> list[WebPortalResponse]: ...
    
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
    ) -> WebPortalObject | list[WebPortalObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WebPortalPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        auth_rule: str | None = ...,
        display_bookmark: Literal["enable", "disable"] | None = ...,
        focus_bookmark: Literal["enable", "disable"] | None = ...,
        display_status: Literal["enable", "disable"] | None = ...,
        display_history: Literal["enable", "disable"] | None = ...,
        policy_auth_sso: Literal["enable", "disable"] | None = ...,
        heading: str | None = ...,
        theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"] | None = ...,
        clipboard: Literal["enable", "disable"] | None = ...,
        default_window_width: int | None = ...,
        default_window_height: int | None = ...,
        cookie_age: int | None = ...,
        forticlient_download: Literal["enable", "disable"] | None = ...,
        customize_forticlient_download_url: Literal["enable", "disable"] | None = ...,
        windows_forticlient_download_url: str | None = ...,
        macos_forticlient_download_url: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WebPortalObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WebPortalPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        auth_rule: str | None = ...,
        display_bookmark: Literal["enable", "disable"] | None = ...,
        focus_bookmark: Literal["enable", "disable"] | None = ...,
        display_status: Literal["enable", "disable"] | None = ...,
        display_history: Literal["enable", "disable"] | None = ...,
        policy_auth_sso: Literal["enable", "disable"] | None = ...,
        heading: str | None = ...,
        theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"] | None = ...,
        clipboard: Literal["enable", "disable"] | None = ...,
        default_window_width: int | None = ...,
        default_window_height: int | None = ...,
        cookie_age: int | None = ...,
        forticlient_download: Literal["enable", "disable"] | None = ...,
        customize_forticlient_download_url: Literal["enable", "disable"] | None = ...,
        windows_forticlient_download_url: str | None = ...,
        macos_forticlient_download_url: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: WebPortalPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        auth_rule: str | None = ...,
        display_bookmark: Literal["enable", "disable"] | None = ...,
        focus_bookmark: Literal["enable", "disable"] | None = ...,
        display_status: Literal["enable", "disable"] | None = ...,
        display_history: Literal["enable", "disable"] | None = ...,
        policy_auth_sso: Literal["enable", "disable"] | None = ...,
        heading: str | None = ...,
        theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"] | None = ...,
        clipboard: Literal["enable", "disable"] | None = ...,
        default_window_width: int | None = ...,
        default_window_height: int | None = ...,
        cookie_age: int | None = ...,
        forticlient_download: Literal["enable", "disable"] | None = ...,
        customize_forticlient_download_url: Literal["enable", "disable"] | None = ...,
        windows_forticlient_download_url: str | None = ...,
        macos_forticlient_download_url: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: WebPortalPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        auth_rule: str | None = ...,
        display_bookmark: Literal["enable", "disable"] | None = ...,
        focus_bookmark: Literal["enable", "disable"] | None = ...,
        display_status: Literal["enable", "disable"] | None = ...,
        display_history: Literal["enable", "disable"] | None = ...,
        policy_auth_sso: Literal["enable", "disable"] | None = ...,
        heading: str | None = ...,
        theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"] | None = ...,
        clipboard: Literal["enable", "disable"] | None = ...,
        default_window_width: int | None = ...,
        default_window_height: int | None = ...,
        cookie_age: int | None = ...,
        forticlient_download: Literal["enable", "disable"] | None = ...,
        customize_forticlient_download_url: Literal["enable", "disable"] | None = ...,
        windows_forticlient_download_url: str | None = ...,
        macos_forticlient_download_url: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WebPortalPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        auth_rule: str | None = ...,
        display_bookmark: Literal["enable", "disable"] | None = ...,
        focus_bookmark: Literal["enable", "disable"] | None = ...,
        display_status: Literal["enable", "disable"] | None = ...,
        display_history: Literal["enable", "disable"] | None = ...,
        policy_auth_sso: Literal["enable", "disable"] | None = ...,
        heading: str | None = ...,
        theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"] | None = ...,
        clipboard: Literal["enable", "disable"] | None = ...,
        default_window_width: int | None = ...,
        default_window_height: int | None = ...,
        cookie_age: int | None = ...,
        forticlient_download: Literal["enable", "disable"] | None = ...,
        customize_forticlient_download_url: Literal["enable", "disable"] | None = ...,
        windows_forticlient_download_url: str | None = ...,
        macos_forticlient_download_url: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WebPortalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WebPortalPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        auth_rule: str | None = ...,
        display_bookmark: Literal["enable", "disable"] | None = ...,
        focus_bookmark: Literal["enable", "disable"] | None = ...,
        display_status: Literal["enable", "disable"] | None = ...,
        display_history: Literal["enable", "disable"] | None = ...,
        policy_auth_sso: Literal["enable", "disable"] | None = ...,
        heading: str | None = ...,
        theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"] | None = ...,
        clipboard: Literal["enable", "disable"] | None = ...,
        default_window_width: int | None = ...,
        default_window_height: int | None = ...,
        cookie_age: int | None = ...,
        forticlient_download: Literal["enable", "disable"] | None = ...,
        customize_forticlient_download_url: Literal["enable", "disable"] | None = ...,
        windows_forticlient_download_url: str | None = ...,
        macos_forticlient_download_url: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: WebPortalPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        auth_rule: str | None = ...,
        display_bookmark: Literal["enable", "disable"] | None = ...,
        focus_bookmark: Literal["enable", "disable"] | None = ...,
        display_status: Literal["enable", "disable"] | None = ...,
        display_history: Literal["enable", "disable"] | None = ...,
        policy_auth_sso: Literal["enable", "disable"] | None = ...,
        heading: str | None = ...,
        theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"] | None = ...,
        clipboard: Literal["enable", "disable"] | None = ...,
        default_window_width: int | None = ...,
        default_window_height: int | None = ...,
        cookie_age: int | None = ...,
        forticlient_download: Literal["enable", "disable"] | None = ...,
        customize_forticlient_download_url: Literal["enable", "disable"] | None = ...,
        windows_forticlient_download_url: str | None = ...,
        macos_forticlient_download_url: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: WebPortalPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        auth_rule: str | None = ...,
        display_bookmark: Literal["enable", "disable"] | None = ...,
        focus_bookmark: Literal["enable", "disable"] | None = ...,
        display_status: Literal["enable", "disable"] | None = ...,
        display_history: Literal["enable", "disable"] | None = ...,
        policy_auth_sso: Literal["enable", "disable"] | None = ...,
        heading: str | None = ...,
        theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"] | None = ...,
        clipboard: Literal["enable", "disable"] | None = ...,
        default_window_width: int | None = ...,
        default_window_height: int | None = ...,
        cookie_age: int | None = ...,
        forticlient_download: Literal["enable", "disable"] | None = ...,
        customize_forticlient_download_url: Literal["enable", "disable"] | None = ...,
        windows_forticlient_download_url: str | None = ...,
        macos_forticlient_download_url: str | None = ...,
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
    ) -> WebPortalObject: ...
    
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
        payload_dict: WebPortalPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        auth_rule: str | None = ...,
        display_bookmark: Literal["enable", "disable"] | None = ...,
        focus_bookmark: Literal["enable", "disable"] | None = ...,
        display_status: Literal["enable", "disable"] | None = ...,
        display_history: Literal["enable", "disable"] | None = ...,
        policy_auth_sso: Literal["enable", "disable"] | None = ...,
        heading: str | None = ...,
        theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "dark-matter", "onyx", "eclipse"] | None = ...,
        clipboard: Literal["enable", "disable"] | None = ...,
        default_window_width: int | None = ...,
        default_window_height: int | None = ...,
        cookie_age: int | None = ...,
        forticlient_download: Literal["enable", "disable"] | None = ...,
        customize_forticlient_download_url: Literal["enable", "disable"] | None = ...,
        windows_forticlient_download_url: str | None = ...,
        macos_forticlient_download_url: str | None = ...,
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
    "WebPortal",
    "WebPortalPayload",
    "WebPortalObject",
]