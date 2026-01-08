from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class GlobalPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/global_ payload fields.
    
    Configure Web proxy global settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.vpn.certificate.hsm-local.HsmLocalEndpoint` (via: ssl-ca-cert)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: ssl-ca-cert, ssl-cert)
        - :class:`~.web-proxy.profile.ProfileEndpoint` (via: webproxy-profile)

    **Usage:**
        payload: GlobalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ssl_cert: NotRequired[str]  # SSL certificate for SSL interception.
    ssl_ca_cert: NotRequired[str]  # SSL CA certificate for SSL interception.
    fast_policy_match: NotRequired[Literal["enable", "disable"]]  # Enable/disable fast matching algorithm for explicit and tran
    ldap_user_cache: NotRequired[Literal["enable", "disable"]]  # Enable/disable LDAP user cache for explicit and transparent 
    proxy_fqdn: str  # Fully Qualified Domain Name of the explicit web proxy (defau
    max_request_length: NotRequired[int]  # Maximum length of HTTP request line (2 - 64 Kbytes, default 
    max_message_length: NotRequired[int]  # Maximum length of HTTP message, not including body (16 - 256
    http2_client_window_size: NotRequired[int]  # HTTP/2 client initial window size in bytes (65535 - 21474836
    http2_server_window_size: NotRequired[int]  # HTTP/2 server initial window size in bytes (65535 - 21474836
    auth_sign_timeout: NotRequired[int]  # Proxy auth query sign timeout in seconds (30 - 3600, default
    strict_web_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable strict web checking to block web sites that s
    forward_proxy_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable forwarding proxy authentication headers.
    forward_server_affinity_timeout: NotRequired[int]  # Period of time before the source IP's traffic is no longer a
    max_waf_body_cache_length: NotRequired[int]  # Maximum length of HTTP messages processed by Web Application
    webproxy_profile: NotRequired[str]  # Name of the web proxy profile to apply when explicit proxy t
    learn_client_ip: NotRequired[Literal["enable", "disable"]]  # Enable/disable learning the client's IP address from headers
    always_learn_client_ip: NotRequired[Literal["enable", "disable"]]  # Enable/disable learning the client's IP address from headers
    learn_client_ip_from_header: NotRequired[Literal["true-client-ip", "x-real-ip", "x-forwarded-for"]]  # Learn client IP address from the specified headers.
    learn_client_ip_srcaddr: NotRequired[list[dict[str, Any]]]  # Source address name (srcaddr or srcaddr6 must be set).
    learn_client_ip_srcaddr6: NotRequired[list[dict[str, Any]]]  # IPv6 Source address name (srcaddr or srcaddr6 must be set).
    src_affinity_exempt_addr: NotRequired[list[dict[str, Any]]]  # IPv4 source addresses to exempt proxy affinity.
    src_affinity_exempt_addr6: NotRequired[list[dict[str, Any]]]  # IPv6 source addresses to exempt proxy affinity.
    policy_partial_match: NotRequired[Literal["enable", "disable"]]  # Enable/disable policy partial matching.
    log_policy_pending: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging sessions that are pending on policy m
    log_forward_server: NotRequired[Literal["enable", "disable"]]  # Enable/disable forward server name logging in forward traffi
    log_app_id: NotRequired[Literal["enable", "disable"]]  # Enable/disable always log application type in traffic log.
    proxy_transparent_cert_inspection: NotRequired[Literal["enable", "disable"]]  # Enable/disable transparent proxy certificate inspection.
    request_obs_fold: NotRequired[Literal["replace-with-sp", "block", "keep"]]  # Action when HTTP/1.x request header contains obs-fold (defau


class GlobalObject(FortiObject[GlobalPayload]):
    """Typed FortiObject for web_proxy/global_ with IDE autocomplete support."""
    
    # SSL certificate for SSL interception.
    ssl_cert: str
    # SSL CA certificate for SSL interception.
    ssl_ca_cert: str
    # Enable/disable fast matching algorithm for explicit and transparent proxy policy
    fast_policy_match: Literal["enable", "disable"]
    # Enable/disable LDAP user cache for explicit and transparent proxy user.
    ldap_user_cache: Literal["enable", "disable"]
    # Fully Qualified Domain Name of the explicit web proxy (default = default.fqdn) t
    proxy_fqdn: str
    # Maximum length of HTTP request line (2 - 64 Kbytes, default = 8).
    max_request_length: int
    # Maximum length of HTTP message, not including body (16 - 256 Kbytes, default = 3
    max_message_length: int
    # HTTP/2 client initial window size in bytes (65535 - 2147483647, default = 104857
    http2_client_window_size: int
    # HTTP/2 server initial window size in bytes (65535 - 2147483647, default = 104857
    http2_server_window_size: int
    # Proxy auth query sign timeout in seconds (30 - 3600, default = 120).
    auth_sign_timeout: int
    # Enable/disable strict web checking to block web sites that send incorrect header
    strict_web_check: Literal["enable", "disable"]
    # Enable/disable forwarding proxy authentication headers.
    forward_proxy_auth: Literal["enable", "disable"]
    # Period of time before the source IP's traffic is no longer assigned to the forwa
    forward_server_affinity_timeout: int
    # Maximum length of HTTP messages processed by Web Application Firewall (WAF) (1 -
    max_waf_body_cache_length: int
    # Name of the web proxy profile to apply when explicit proxy traffic is allowed by
    webproxy_profile: str
    # Enable/disable learning the client's IP address from headers.
    learn_client_ip: Literal["enable", "disable"]
    # Enable/disable learning the client's IP address from headers for every request.
    always_learn_client_ip: Literal["enable", "disable"]
    # Learn client IP address from the specified headers.
    learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"]
    # Source address name (srcaddr or srcaddr6 must be set).
    learn_client_ip_srcaddr: list[str]  # Auto-flattened from member_table
    # IPv6 Source address name (srcaddr or srcaddr6 must be set).
    learn_client_ip_srcaddr6: list[str]  # Auto-flattened from member_table
    # IPv4 source addresses to exempt proxy affinity.
    src_affinity_exempt_addr: list[str]  # Auto-flattened from member_table
    # IPv6 source addresses to exempt proxy affinity.
    src_affinity_exempt_addr6: list[str]  # Auto-flattened from member_table
    # Enable/disable policy partial matching.
    policy_partial_match: Literal["enable", "disable"]
    # Enable/disable logging sessions that are pending on policy matching.
    log_policy_pending: Literal["enable", "disable"]
    # Enable/disable forward server name logging in forward traffic log.
    log_forward_server: Literal["enable", "disable"]
    # Enable/disable always log application type in traffic log.
    log_app_id: Literal["enable", "disable"]
    # Enable/disable transparent proxy certificate inspection.
    proxy_transparent_cert_inspection: Literal["enable", "disable"]
    # Action when HTTP/1.x request header contains obs-fold (default = keep).
    request_obs_fold: Literal["replace-with-sp", "block", "keep"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> GlobalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Global:
    """
    Configure Web proxy global settings.
    
    Path: web_proxy/global_
    Category: cmdb
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> GlobalObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
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
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> GlobalObject: ...
    
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
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
    ) -> dict[str, Any]: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> GlobalObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        auth_sign_timeout: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        policy_partial_match: Literal["enable", "disable"] | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GlobalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        auth_sign_timeout: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        policy_partial_match: Literal["enable", "disable"] | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        auth_sign_timeout: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        policy_partial_match: Literal["enable", "disable"] | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        auth_sign_timeout: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        policy_partial_match: Literal["enable", "disable"] | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: GlobalPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        auth_sign_timeout: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        policy_partial_match: Literal["enable", "disable"] | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
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
    "Global",
    "GlobalPayload",
    "GlobalObject",
]