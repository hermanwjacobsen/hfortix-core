from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class GlobalSettingPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/global_setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: GlobalSettingPayload = {
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
    src_affinity_exempt_addr: NotRequired[str]  # IPv4 source addresses to exempt proxy affinity.
    src_affinity_exempt_addr6: NotRequired[str]  # IPv6 source addresses to exempt proxy affinity.
    log_policy_pending: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging sessions that are pending on policy m
    log_forward_server: NotRequired[Literal["enable", "disable"]]  # Enable/disable forward server name logging in forward traffi
    log_app_id: NotRequired[Literal["enable", "disable"]]  # Enable/disable always log application type in traffic log.
    proxy_transparent_cert_inspection: NotRequired[Literal["enable", "disable"]]  # Enable/disable transparent proxy certificate inspection.
    request_obs_fold: NotRequired[Literal["replace-with-sp", "block", "keep"]]  # Action when HTTP/1.x request header contains obs-fold.


class GlobalSetting:
    """
    Configure Web proxy global settings.
    
    Path: web_proxy/global_setting
    Category: cmdb
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
        payload_dict: GlobalSettingPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | None = ...,
        learn_client_ip_srcaddr: list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | None = ...,
        src_affinity_exempt_addr6: str | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: GlobalSettingPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | None = ...,
        learn_client_ip_srcaddr: list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | None = ...,
        src_affinity_exempt_addr6: str | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
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
        payload_dict: GlobalSettingPayload | None = ...,
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
    "GlobalSetting",
    "GlobalSettingPayload",
]