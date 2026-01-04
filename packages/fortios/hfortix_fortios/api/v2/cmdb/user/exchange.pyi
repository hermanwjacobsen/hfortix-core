from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ExchangePayload(TypedDict, total=False):
    """
    Type hints for user/exchange payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ExchangePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # MS Exchange server entry name.
    server_name: str  # MS Exchange server hostname.
    domain_name: str  # MS Exchange server fully qualified domain name.
    username: str  # User name used to sign in to the server. Must have proper pe
    password: str  # Password for the specified username.
    ip: NotRequired[str]  # Server IPv4 address.
    connect_protocol: NotRequired[Literal["rpc-over-tcp", "rpc-over-http", "rpc-over-https"]]  # Connection protocol used to connect to MS Exchange service.
    validate_server_certificate: NotRequired[Literal["disable", "enable"]]  # Enable/disable exchange server certificate validation.
    auth_type: NotRequired[Literal["spnego", "ntlm", "kerberos"]]  # Authentication security type used for the RPC protocol layer
    auth_level: NotRequired[Literal["connect", "call", "packet", "integrity", "privacy"]]  # Authentication security level used for the RPC protocol laye
    http_auth_type: NotRequired[Literal["basic", "ntlm"]]  # Authentication security type used for the HTTP transport.
    ssl_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum SSL/TLS protocol version for HTTPS transport (defaul
    auto_discover_kdc: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic discovery of KDC IP addresses.
    kdc_ip: NotRequired[list[dict[str, Any]]]  # KDC IPv4 addresses for Kerberos authentication.


class Exchange:
    """
    Configure MS Exchange server entries.
    
    Path: user/exchange
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
        payload_dict: ExchangePayload | None = ...,
        name: str | None = ...,
        server_name: str | None = ...,
        domain_name: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip: str | None = ...,
        connect_protocol: Literal["rpc-over-tcp", "rpc-over-http", "rpc-over-https"] | None = ...,
        validate_server_certificate: Literal["disable", "enable"] | None = ...,
        auth_type: Literal["spnego", "ntlm", "kerberos"] | None = ...,
        auth_level: Literal["connect", "call", "packet", "integrity", "privacy"] | None = ...,
        http_auth_type: Literal["basic", "ntlm"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auto_discover_kdc: Literal["enable", "disable"] | None = ...,
        kdc_ip: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ExchangePayload | None = ...,
        name: str | None = ...,
        server_name: str | None = ...,
        domain_name: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        ip: str | None = ...,
        connect_protocol: Literal["rpc-over-tcp", "rpc-over-http", "rpc-over-https"] | None = ...,
        validate_server_certificate: Literal["disable", "enable"] | None = ...,
        auth_type: Literal["spnego", "ntlm", "kerberos"] | None = ...,
        auth_level: Literal["connect", "call", "packet", "integrity", "privacy"] | None = ...,
        http_auth_type: Literal["basic", "ntlm"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auto_discover_kdc: Literal["enable", "disable"] | None = ...,
        kdc_ip: list[dict[str, Any]] | None = ...,
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
        payload_dict: ExchangePayload | None = ...,
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