from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SslServerPayload(TypedDict, total=False):
    """
    Type hints for firewall/ssl_server payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SslServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Server name.
    ip: str  # IPv4 address of the SSL server.
    port: int  # Server service port (1 - 65535, default = 443).
    ssl_mode: NotRequired[Literal["half", "full"]]  # SSL/TLS mode for encryption and decryption of traffic.
    add_header_x_forwarded_proto: NotRequired[Literal["enable", "disable"]]  # Enable/disable adding an X-Forwarded-Proto header to forward
    mapped_port: int  # Mapped server service port (1 - 65535, default = 80).
    ssl_cert: NotRequired[list[dict[str, Any]]]  # List of certificate names to use for SSL connections to this
    ssl_dh_bits: NotRequired[Literal["768", "1024", "1536", "2048"]]  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    ssl_algorithm: NotRequired[Literal["high", "medium", "low"]]  # Relative strength of encryption algorithms accepted in negot
    ssl_client_renegotiation: NotRequired[Literal["allow", "deny", "secure"]]  # Allow or block client renegotiation by server.
    ssl_min_version: NotRequired[Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]]  # Lowest SSL/TLS version to negotiate.
    ssl_max_version: NotRequired[Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]]  # Highest SSL/TLS version to negotiate.
    ssl_send_empty_frags: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending empty fragments to avoid attack on CB
    url_rewrite: NotRequired[Literal["enable", "disable"]]  # Enable/disable rewriting the URL.


class SslServer:
    """
    Configure SSL servers.
    
    Path: firewall/ssl_server
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
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
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
        payload_dict: SslServerPayload | None = ...,
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