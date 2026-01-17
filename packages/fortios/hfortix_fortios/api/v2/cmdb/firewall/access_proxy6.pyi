""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/access_proxy6
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

class AccessProxy6ApigatewayItem:
    """Nested item for api-gateway field - supports attribute access."""
    id: int
    url_map: str
    service: Literal["http", "https", "tcp-forwarding", "samlsp", "web-portal", "saas"]
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]
    virtual_host: str
    url_map_type: Literal["sub-string", "wildcard", "regex"]
    h2_support: Literal["enable", "disable"]
    h3_support: Literal["enable", "disable"]
    quic: str
    realservers: str | list[str]
    application: str | list[str]
    persistence: Literal["none", "http-cookie"]
    http_cookie_domain_from_host: Literal["disable", "enable"]
    http_cookie_domain: str
    http_cookie_path: str
    http_cookie_generation: int
    http_cookie_age: int
    http_cookie_share: Literal["disable", "same-ip"]
    https_cookie_secure: Literal["disable", "enable"]
    saml_server: str
    saml_redirect: Literal["disable", "enable"]
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]
    ssl_algorithm: Literal["high", "medium", "low"]
    ssl_cipher_suites: str | list[str]
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    ssl_renegotiation: Literal["enable", "disable"]
    ssl_vpn_web_portal: str


class AccessProxy6Apigateway6Item:
    """Nested item for api-gateway6 field - supports attribute access."""
    id: int
    url_map: str
    service: Literal["http", "https", "tcp-forwarding", "samlsp", "web-portal", "saas"]
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]
    virtual_host: str
    url_map_type: Literal["sub-string", "wildcard", "regex"]
    h2_support: Literal["enable", "disable"]
    h3_support: Literal["enable", "disable"]
    quic: str
    realservers: str | list[str]
    application: str | list[str]
    persistence: Literal["none", "http-cookie"]
    http_cookie_domain_from_host: Literal["disable", "enable"]
    http_cookie_domain: str
    http_cookie_path: str
    http_cookie_generation: int
    http_cookie_age: int
    http_cookie_share: Literal["disable", "same-ip"]
    https_cookie_secure: Literal["disable", "enable"]
    saml_server: str
    saml_redirect: Literal["disable", "enable"]
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]
    ssl_algorithm: Literal["high", "medium", "low"]
    ssl_cipher_suites: str | list[str]
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    ssl_renegotiation: Literal["enable", "disable"]
    ssl_vpn_web_portal: str


class AccessProxy6Payload(TypedDict, total=False):
    """Payload type for AccessProxy6 operations."""
    name: str
    vip: str
    auth_portal: Literal["disable", "enable"]
    auth_virtual_host: str
    log_blocked_traffic: Literal["enable", "disable"]
    add_vhost_domain_to_dnsdb: Literal["enable", "disable"]
    svr_pool_multiplex: Literal["enable", "disable"]
    svr_pool_ttl: int
    svr_pool_server_max_request: int
    svr_pool_server_max_concurrent_request: int
    decrypted_traffic_mirror: str
    api_gateway: str | list[str] | list[dict[str, Any]] | list[AccessProxy6ApigatewayItem]
    api_gateway6: str | list[str] | list[dict[str, Any]] | list[AccessProxy6Apigateway6Item]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class AccessProxy6Response(TypedDict, total=False):
    """Response type for AccessProxy6 - use with .dict property for typed dict access."""
    name: str
    vip: str
    auth_portal: Literal["disable", "enable"]
    auth_virtual_host: str
    log_blocked_traffic: Literal["enable", "disable"]
    add_vhost_domain_to_dnsdb: Literal["enable", "disable"]
    svr_pool_multiplex: Literal["enable", "disable"]
    svr_pool_ttl: int
    svr_pool_server_max_request: int
    svr_pool_server_max_concurrent_request: int
    decrypted_traffic_mirror: str
    api_gateway: list[AccessProxy6ApigatewayItem]
    api_gateway6: list[AccessProxy6Apigateway6Item]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class AccessProxy6Object(FortiObject):
    """Typed FortiObject for AccessProxy6 with field access."""
    name: str
    vip: str
    auth_portal: Literal["disable", "enable"]
    auth_virtual_host: str
    log_blocked_traffic: Literal["enable", "disable"]
    add_vhost_domain_to_dnsdb: Literal["enable", "disable"]
    svr_pool_multiplex: Literal["enable", "disable"]
    svr_pool_ttl: int
    svr_pool_server_max_request: int
    svr_pool_server_max_concurrent_request: int
    decrypted_traffic_mirror: str
    api_gateway: list[AccessProxy6ApigatewayItem]
    api_gateway6: list[AccessProxy6Apigateway6Item]


# ================================================================
# Main Endpoint Class
# ================================================================

class AccessProxy6:
    """
    
    Endpoint: firewall/access_proxy6
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
    ) -> AccessProxy6Object: ...
    
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
    ) -> FortiObjectList[AccessProxy6Object]: ...
    
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
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | list[AccessProxy6ApigatewayItem] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | list[AccessProxy6Apigateway6Item] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> AccessProxy6Object: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | list[AccessProxy6ApigatewayItem] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | list[AccessProxy6Apigateway6Item] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> AccessProxy6Object: ...

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
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | list[AccessProxy6ApigatewayItem] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | list[AccessProxy6Apigateway6Item] | None = ...,
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
    "AccessProxy6",
    "AccessProxy6Payload",
    "AccessProxy6Response",
    "AccessProxy6Object",
]