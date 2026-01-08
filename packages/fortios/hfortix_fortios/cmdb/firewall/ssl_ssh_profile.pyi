from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SslSshProfilePayload(TypedDict, total=False):
    """
    Type hints for firewall/ssl_ssh_profile payload fields.
    
    Configure SSL/SSH protocol options.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.vpn.certificate.hsm-local.HsmLocalEndpoint` (via: caname, untrusted-caname)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: caname, untrusted-caname)

    **Usage:**
        payload: SslSshProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name.
    comment: NotRequired[str]  # Optional comments.
    ssl: NotRequired[str]  # Configure SSL options.
    https: NotRequired[str]  # Configure HTTPS options.
    ftps: NotRequired[str]  # Configure FTPS options.
    imaps: NotRequired[str]  # Configure IMAPS options.
    pop3s: NotRequired[str]  # Configure POP3S options.
    smtps: NotRequired[str]  # Configure SMTPS options.
    ssh: NotRequired[str]  # Configure SSH options.
    dot: NotRequired[str]  # Configure DNS over TLS options.
    allowlist: NotRequired[Literal["enable", "disable"]]  # Enable/disable exempting servers by FortiGuard allowlist.
    block_blocklisted_certificates: NotRequired[Literal["disable", "enable"]]  # Enable/disable blocking SSL-based botnet communication by Fo
    ssl_exempt: NotRequired[list[dict[str, Any]]]  # Servers to exempt from SSL inspection.
    ech_outer_sni: NotRequired[list[dict[str, Any]]]  # ClientHelloOuter SNIs to be blocked.
    server_cert_mode: Literal["re-sign", "replace"]  # Re-sign or replace the server's certificate.
    use_ssl_server: NotRequired[Literal["disable", "enable"]]  # Enable/disable the use of SSL server table for SSL offloadin
    caname: str  # CA certificate used by SSL Inspection.
    untrusted_caname: str  # Untrusted CA certificate used by SSL Inspection.
    server_cert: NotRequired[list[dict[str, Any]]]  # Certificate used by SSL Inspection to replace server certifi
    ssl_server: list[dict[str, Any]]  # SSL server settings used for client certificate request.
    ssl_exemption_ip_rating: NotRequired[Literal["enable", "disable"]]  # Enable/disable IP based URL rating.
    ssl_exemption_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging of SSL exemptions.
    ssl_anomaly_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging of SSL anomalies.
    ssl_negotiation_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging of SSL negotiation events.
    ssl_server_cert_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging of server certificate information.
    ssl_handshake_log: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging of TLS handshakes.
    rpc_over_https: NotRequired[Literal["enable", "disable"]]  # Enable/disable inspection of RPC over HTTPS.
    mapi_over_https: NotRequired[Literal["enable", "disable"]]  # Enable/disable inspection of MAPI over HTTPS.
    supported_alpn: NotRequired[Literal["http1-1", "http2", "all", "none"]]  # Configure ALPN option.


class SslSshProfileObject(FortiObject[SslSshProfilePayload]):
    """Typed FortiObject for firewall/ssl_ssh_profile with IDE autocomplete support."""
    
    # Name.
    name: str
    # Optional comments.
    comment: str
    # Configure SSL options.
    ssl: str
    # Configure HTTPS options.
    https: str
    # Configure FTPS options.
    ftps: str
    # Configure IMAPS options.
    imaps: str
    # Configure POP3S options.
    pop3s: str
    # Configure SMTPS options.
    smtps: str
    # Configure SSH options.
    ssh: str
    # Configure DNS over TLS options.
    dot: str
    # Enable/disable exempting servers by FortiGuard allowlist.
    allowlist: Literal["enable", "disable"]
    # Enable/disable blocking SSL-based botnet communication by FortiGuard certificate
    block_blocklisted_certificates: Literal["disable", "enable"]
    # Servers to exempt from SSL inspection.
    ssl_exempt: list[str]  # Auto-flattened from member_table
    # ClientHelloOuter SNIs to be blocked.
    ech_outer_sni: list[str]  # Auto-flattened from member_table
    # Re-sign or replace the server's certificate.
    server_cert_mode: Literal["re-sign", "replace"]
    # Enable/disable the use of SSL server table for SSL offloading.
    use_ssl_server: Literal["disable", "enable"]
    # CA certificate used by SSL Inspection.
    caname: str
    # Untrusted CA certificate used by SSL Inspection.
    untrusted_caname: str
    # Certificate used by SSL Inspection to replace server certificate.
    server_cert: list[str]  # Auto-flattened from member_table
    # SSL server settings used for client certificate request.
    ssl_server: list[str]  # Auto-flattened from member_table
    # Enable/disable IP based URL rating.
    ssl_exemption_ip_rating: Literal["enable", "disable"]
    # Enable/disable logging of SSL exemptions.
    ssl_exemption_log: Literal["disable", "enable"]
    # Enable/disable logging of SSL anomalies.
    ssl_anomaly_log: Literal["disable", "enable"]
    # Enable/disable logging of SSL negotiation events.
    ssl_negotiation_log: Literal["disable", "enable"]
    # Enable/disable logging of server certificate information.
    ssl_server_cert_log: Literal["disable", "enable"]
    # Enable/disable logging of TLS handshakes.
    ssl_handshake_log: Literal["disable", "enable"]
    # Enable/disable inspection of RPC over HTTPS.
    rpc_over_https: Literal["enable", "disable"]
    # Enable/disable inspection of MAPI over HTTPS.
    mapi_over_https: Literal["enable", "disable"]
    # Configure ALPN option.
    supported_alpn: Literal["http1-1", "http2", "all", "none"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SslSshProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SslSshProfile:
    """
    Configure SSL/SSH protocol options.
    
    Path: firewall/ssl_ssh_profile
    Category: cmdb
    Primary Key: name
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
    ) -> SslSshProfileObject: ...
    
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
    ) -> list[SslSshProfileObject]: ...
    
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
    ) -> SslSshProfileObject | list[SslSshProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SslSshProfileObject: ...
    
    @overload
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
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SslSshProfileObject: ...
    
    @overload
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
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> SslSshProfileObject: ...
    
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
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "SslSshProfile",
    "SslSshProfilePayload",
    "SslSshProfileObject",
]