""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/ssl_ssh_profile
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

class SslSshProfileSslexemptItem:
    """Nested item for ssl-exempt field - supports attribute access."""
    id: int
    type: Literal["fortiguard-category", "address", "address6", "wildcard-fqdn", "regex"]
    fortiguard_category: int
    address: str
    address6: str
    wildcard_fqdn: str
    regex: str


class SslSshProfileEchoutersniItem:
    """Nested item for ech-outer-sni field - supports attribute access."""
    name: str
    sni: str


class SslSshProfileServercertItem:
    """Nested item for server-cert field - supports attribute access."""
    name: str


class SslSshProfileSslserverItem:
    """Nested item for ssl-server field - supports attribute access."""
    id: int
    ip: str
    https_client_certificate: Literal["bypass", "inspect", "block"]
    smtps_client_certificate: Literal["bypass", "inspect", "block"]
    pop3s_client_certificate: Literal["bypass", "inspect", "block"]
    imaps_client_certificate: Literal["bypass", "inspect", "block"]
    ftps_client_certificate: Literal["bypass", "inspect", "block"]
    ssl_other_client_certificate: Literal["bypass", "inspect", "block"]


class SslSshProfilePayload(TypedDict, total=False):
    """Payload type for SslSshProfile operations."""
    name: str
    comment: str
    ssl: str
    https: str
    ftps: str
    imaps: str
    pop3s: str
    smtps: str
    ssh: str
    dot: str
    allowlist: Literal["enable", "disable"]
    block_blocklisted_certificates: Literal["disable", "enable"]
    ssl_exempt: str | list[str] | list[dict[str, Any]] | list[SslSshProfileSslexemptItem]
    ech_outer_sni: str | list[str] | list[dict[str, Any]] | list[SslSshProfileEchoutersniItem]
    server_cert_mode: Literal["re-sign", "replace"]
    use_ssl_server: Literal["disable", "enable"]
    caname: str
    untrusted_caname: str
    server_cert: str | list[str] | list[dict[str, Any]] | list[SslSshProfileServercertItem]
    ssl_server: str | list[str] | list[dict[str, Any]] | list[SslSshProfileSslserverItem]
    ssl_exemption_ip_rating: Literal["enable", "disable"]
    ssl_exemption_log: Literal["disable", "enable"]
    ssl_anomaly_log: Literal["disable", "enable"]
    ssl_negotiation_log: Literal["disable", "enable"]
    ssl_server_cert_log: Literal["disable", "enable"]
    ssl_handshake_log: Literal["disable", "enable"]
    rpc_over_https: Literal["enable", "disable"]
    mapi_over_https: Literal["enable", "disable"]
    supported_alpn: Literal["http1-1", "http2", "all", "none"]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class SslSshProfileResponse(TypedDict, total=False):
    """Response type for SslSshProfile - use with .dict property for typed dict access."""
    name: str
    comment: str
    ssl: str
    https: str
    ftps: str
    imaps: str
    pop3s: str
    smtps: str
    ssh: str
    dot: str
    allowlist: Literal["enable", "disable"]
    block_blocklisted_certificates: Literal["disable", "enable"]
    ssl_exempt: list[SslSshProfileSslexemptItem]
    ech_outer_sni: list[SslSshProfileEchoutersniItem]
    server_cert_mode: Literal["re-sign", "replace"]
    use_ssl_server: Literal["disable", "enable"]
    caname: str
    untrusted_caname: str
    server_cert: list[SslSshProfileServercertItem]
    ssl_server: list[SslSshProfileSslserverItem]
    ssl_exemption_ip_rating: Literal["enable", "disable"]
    ssl_exemption_log: Literal["disable", "enable"]
    ssl_anomaly_log: Literal["disable", "enable"]
    ssl_negotiation_log: Literal["disable", "enable"]
    ssl_server_cert_log: Literal["disable", "enable"]
    ssl_handshake_log: Literal["disable", "enable"]
    rpc_over_https: Literal["enable", "disable"]
    mapi_over_https: Literal["enable", "disable"]
    supported_alpn: Literal["http1-1", "http2", "all", "none"]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class SslSshProfileObject(FortiObject):
    """Typed FortiObject for SslSshProfile with field access."""
    name: str
    comment: str
    ssl: str
    https: str
    ftps: str
    imaps: str
    pop3s: str
    smtps: str
    ssh: str
    dot: str
    allowlist: Literal["enable", "disable"]
    block_blocklisted_certificates: Literal["disable", "enable"]
    ssl_exempt: list[SslSshProfileSslexemptItem]
    ech_outer_sni: list[SslSshProfileEchoutersniItem]
    server_cert_mode: Literal["re-sign", "replace"]
    use_ssl_server: Literal["disable", "enable"]
    caname: str
    untrusted_caname: str
    server_cert: list[SslSshProfileServercertItem]
    ssl_server: list[SslSshProfileSslserverItem]
    ssl_exemption_ip_rating: Literal["enable", "disable"]
    ssl_exemption_log: Literal["disable", "enable"]
    ssl_anomaly_log: Literal["disable", "enable"]
    ssl_negotiation_log: Literal["disable", "enable"]
    ssl_server_cert_log: Literal["disable", "enable"]
    ssl_handshake_log: Literal["disable", "enable"]
    rpc_over_https: Literal["enable", "disable"]
    mapi_over_https: Literal["enable", "disable"]
    supported_alpn: Literal["http1-1", "http2", "all", "none"]


# ================================================================
# Main Endpoint Class
# ================================================================

class SslSshProfile:
    """
    
    Endpoint: firewall/ssl_ssh_profile
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
    ) -> SslSshProfileObject: ...
    
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
    ) -> FortiObjectList[SslSshProfileObject]: ...
    
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
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | list[SslSshProfileSslexemptItem] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | list[SslSshProfileEchoutersniItem] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | list[SslSshProfileServercertItem] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | list[SslSshProfileSslserverItem] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> SslSshProfileObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | list[SslSshProfileSslexemptItem] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | list[SslSshProfileEchoutersniItem] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | list[SslSshProfileServercertItem] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | list[SslSshProfileSslserverItem] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> SslSshProfileObject: ...

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
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | list[SslSshProfileSslexemptItem] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | list[SslSshProfileEchoutersniItem] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | list[SslSshProfileServercertItem] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | list[SslSshProfileSslserverItem] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
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
    "SslSshProfile",
    "SslSshProfilePayload",
    "SslSshProfileResponse",
    "SslSshProfileObject",
]