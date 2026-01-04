from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class WebPortalPayload(TypedDict, total=False):
    """
    Type hints for ztna/web_portal payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class WebPortal:
    """
    Configure ztna web-portal.
    
    Path: ztna/web_portal
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        payload_dict: WebPortalPayload | None = ...,
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