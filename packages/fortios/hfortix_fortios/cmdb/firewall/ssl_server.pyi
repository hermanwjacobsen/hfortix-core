from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SslServerPayload(TypedDict, total=False):
    """
    Type hints for firewall/ssl_server payload fields.
    
    Configure SSL servers.
    
    **Usage:**
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


class SslServerObject(FortiObject[SslServerPayload]):
    """Typed FortiObject for firewall/ssl_server with IDE autocomplete support."""
    
    # Server name.
    name: str
    # IPv4 address of the SSL server.
    ip: str
    # Server service port (1 - 65535, default = 443).
    port: int
    # SSL/TLS mode for encryption and decryption of traffic.
    ssl_mode: Literal["half", "full"]
    # Enable/disable adding an X-Forwarded-Proto header to forwarded requests.
    add_header_x_forwarded_proto: Literal["enable", "disable"]
    # Mapped server service port (1 - 65535, default = 80).
    mapped_port: int
    # List of certificate names to use for SSL connections to this server. (default = 
    ssl_cert: list[str]  # Auto-flattened from member_table
    # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 204
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]
    # Relative strength of encryption algorithms accepted in negotiation.
    ssl_algorithm: Literal["high", "medium", "low"]
    # Allow or block client renegotiation by server.
    ssl_client_renegotiation: Literal["allow", "deny", "secure"]
    # Lowest SSL/TLS version to negotiate.
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Highest SSL/TLS version to negotiate.
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Enable/disable sending empty fragments to avoid attack on CBC IV.
    ssl_send_empty_frags: Literal["enable", "disable"]
    # Enable/disable rewriting the URL.
    url_rewrite: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SslServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SslServer:
    """
    Configure SSL servers.
    
    Path: firewall/ssl_server
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
    ) -> SslServerObject: ...
    
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
    ) -> list[SslServerObject]: ...
    
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
    ) -> SslServerObject | list[SslServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SslServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SslServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
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
    ) -> SslServerObject: ...
    
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
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
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
    "SslServer",
    "SslServerPayload",
    "SslServerObject",
]