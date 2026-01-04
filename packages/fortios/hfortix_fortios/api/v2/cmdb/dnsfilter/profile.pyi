from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for dnsfilter/profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name.
    comment: NotRequired[str]  # Comment.
    domain_filter: NotRequired[str]  # Domain filter settings.
    ftgd_dns: NotRequired[str]  # FortiGuard DNS Filter settings.
    log_all_domain: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging of all domains visited (detailed DNS 
    sdns_ftgd_err_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiGuard SDNS rating error logging.
    sdns_domain_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable domain filtering and botnet domain logging.
    block_action: NotRequired[Literal["block", "redirect", "block-sevrfail"]]  # Action to take for blocked domains.
    redirect_portal: NotRequired[str]  # IPv4 address of the SDNS redirect portal.
    redirect_portal6: NotRequired[str]  # IPv6 address of the SDNS redirect portal.
    block_botnet: NotRequired[Literal["disable", "enable"]]  # Enable/disable blocking botnet C&C DNS lookups.
    safe_search: NotRequired[Literal["disable", "enable"]]  # Enable/disable Google, Bing, YouTube, Qwant, DuckDuckGo safe
    youtube_restrict: NotRequired[Literal["strict", "moderate", "none"]]  # Set safe search for YouTube restriction level.
    external_ip_blocklist: NotRequired[list[dict[str, Any]]]  # One or more external IP block lists.
    dns_translation: NotRequired[list[dict[str, Any]]]  # DNS translation settings.
    transparent_dns_database: NotRequired[list[dict[str, Any]]]  # Transparent DNS database zones.
    strip_ech: NotRequired[Literal["disable", "enable"]]  # Enable/disable removal of the encrypted client hello service


class Profile:
    """
    Configure DNS domain filter profile.
    
    Path: dnsfilter/profile
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
        external_ip_blocklist: list[dict[str, Any]] | None = ...,
        dns_translation: list[dict[str, Any]] | None = ...,
        transparent_dns_database: list[dict[str, Any]] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        external_ip_blocklist: list[dict[str, Any]] | None = ...,
        dns_translation: list[dict[str, Any]] | None = ...,
        transparent_dns_database: list[dict[str, Any]] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
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