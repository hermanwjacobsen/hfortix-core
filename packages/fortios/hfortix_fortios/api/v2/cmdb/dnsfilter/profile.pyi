from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for dnsfilter/profile payload fields.
    
    Configure DNS domain filter profile.
    
    **Usage:**
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name.
    comment: NotRequired[str]  # Comment.
    domain_filter: NotRequired[str]  # Domain filter settings.
    ftgd_dns: NotRequired[str]  # FortiGuard DNS Filter settings.
    log_all_domain: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging of all domains visited
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

# Nested classes for table field children

@final
class ProfileExternalipblocklistObject:
    """Typed object for external-ip-blocklist table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # External domain block list name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ProfileDnstranslationObject:
    """Typed object for dns-translation table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # DNS translation type (IPv4 or IPv6).
    addr_type: Literal["ipv4", "ipv6"]
    # IPv4 address or subnet on the internal network to compare with the resolved addr
    src: str
    # IPv4 address or subnet on the external network to substitute for the resolved ad
    dst: str
    # If src and dst are subnets rather than single IP addresses, enter the netmask fo
    netmask: str
    # Enable/disable this DNS translation entry.
    status: Literal["enable", "disable"]
    # IPv6 address or subnet on the internal network to compare with the resolved addr
    src6: str
    # IPv6 address or subnet on the external network to substitute for the resolved ad
    dst6: str
    # If src6 and dst6 are subnets rather than single IP addresses, enter the prefix f
    prefix: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ProfileTransparentdnsdatabaseObject:
    """Typed object for transparent-dns-database table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DNS database zone name.
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
    Type hints for dnsfilter/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
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
    external_ip_blocklist: list[dict[str, Any]]
    dns_translation: list[dict[str, Any]]
    transparent_dns_database: list[dict[str, Any]]
    strip_ech: Literal["disable", "enable"]


@final
class ProfileObject:
    """Typed FortiObject for dnsfilter/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name.
    name: str
    # Comment.
    comment: str
    # Domain filter settings.
    domain_filter: str
    # FortiGuard DNS Filter settings.
    ftgd_dns: str
    # Enable/disable logging of all domains visited (detailed DNS logging).
    log_all_domain: Literal["enable", "disable"]
    # Enable/disable FortiGuard SDNS rating error logging.
    sdns_ftgd_err_log: Literal["enable", "disable"]
    # Enable/disable domain filtering and botnet domain logging.
    sdns_domain_log: Literal["enable", "disable"]
    # Action to take for blocked domains.
    block_action: Literal["block", "redirect", "block-sevrfail"]
    # IPv4 address of the SDNS redirect portal.
    redirect_portal: str
    # IPv6 address of the SDNS redirect portal.
    redirect_portal6: str
    # Enable/disable blocking botnet C&C DNS lookups.
    block_botnet: Literal["disable", "enable"]
    # Enable/disable Google, Bing, YouTube, Qwant, DuckDuckGo safe search.
    safe_search: Literal["disable", "enable"]
    # Set safe search for YouTube restriction level.
    youtube_restrict: Literal["strict", "moderate", "none"]
    # One or more external IP block lists.
    external_ip_blocklist: list[ProfileExternalipblocklistObject]  # Table field - list of typed objects
    # DNS translation settings.
    dns_translation: list[ProfileDnstranslationObject]  # Table field - list of typed objects
    # Transparent DNS database zones.
    transparent_dns_database: list[ProfileTransparentdnsdatabaseObject]  # Table field - list of typed objects
    # Enable/disable removal of the encrypted client hello service parameter from supp
    strip_ech: Literal["disable", "enable"]
    
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
    Configure DNS domain filter profile.
    
    Path: dnsfilter/profile
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
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
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
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
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
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
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
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
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
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
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
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
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
        external_ip_blocklist: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_translation: str | list[str] | list[dict[str, Any]] | None = ...,
        transparent_dns_database: str | list[str] | list[dict[str, Any]] | None = ...,
        strip_ech: Literal["disable", "enable"] | None = ...,
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