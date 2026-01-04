from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SslSshProfilePayload(TypedDict, total=False):
    """
    Type hints for firewall/ssl_ssh_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class SslSshProfile:
    """
    Configure SSL/SSH protocol options.
    
    Path: firewall/ssl_ssh_profile
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
        ssl_exempt: list[dict[str, Any]] | None = ...,
        ech_outer_sni: list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: list[dict[str, Any]] | None = ...,
        ssl_server: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        ssl_exempt: list[dict[str, Any]] | None = ...,
        ech_outer_sni: list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: list[dict[str, Any]] | None = ...,
        ssl_server: list[dict[str, Any]] | None = ...,
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
        payload_dict: SslSshProfilePayload | None = ...,
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