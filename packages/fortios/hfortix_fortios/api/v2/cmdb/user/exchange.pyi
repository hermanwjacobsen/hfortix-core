from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ExchangePayload(TypedDict, total=False):
    """
    Type hints for user/exchange payload fields.
    
    Configure MS Exchange server entries.
    
    **Usage:**
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
    ssl_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum SSL/TLS protocol version for HTTPS transport
    auto_discover_kdc: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic discovery of KDC IP addresses.
    kdc_ip: NotRequired[list[dict[str, Any]]]  # KDC IPv4 addresses for Kerberos authentication.

# Nested classes for table field children

@final
class ExchangeKdcipObject:
    """Typed object for kdc-ip table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # KDC IPv4 addresses for Kerberos authentication.
    ipv4: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class ExchangeResponse(TypedDict):
    """
    Type hints for user/exchange API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    server_name: str
    domain_name: str
    username: str
    password: str
    ip: str
    connect_protocol: Literal["rpc-over-tcp", "rpc-over-http", "rpc-over-https"]
    validate_server_certificate: Literal["disable", "enable"]
    auth_type: Literal["spnego", "ntlm", "kerberos"]
    auth_level: Literal["connect", "call", "packet", "integrity", "privacy"]
    http_auth_type: Literal["basic", "ntlm"]
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    auto_discover_kdc: Literal["enable", "disable"]
    kdc_ip: list[dict[str, Any]]


@final
class ExchangeObject:
    """Typed FortiObject for user/exchange with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # MS Exchange server entry name.
    name: str
    # MS Exchange server hostname.
    server_name: str
    # MS Exchange server fully qualified domain name.
    domain_name: str
    # User name used to sign in to the server. Must have proper permissions for servic
    username: str
    # Password for the specified username.
    password: str
    # Server IPv4 address.
    ip: str
    # Connection protocol used to connect to MS Exchange service.
    connect_protocol: Literal["rpc-over-tcp", "rpc-over-http", "rpc-over-https"]
    # Enable/disable exchange server certificate validation.
    validate_server_certificate: Literal["disable", "enable"]
    # Authentication security type used for the RPC protocol layer.
    auth_type: Literal["spnego", "ntlm", "kerberos"]
    # Authentication security level used for the RPC protocol layer.
    auth_level: Literal["connect", "call", "packet", "integrity", "privacy"]
    # Authentication security type used for the HTTP transport.
    http_auth_type: Literal["basic", "ntlm"]
    # Minimum SSL/TLS protocol version for HTTPS transport
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # Enable/disable automatic discovery of KDC IP addresses.
    auto_discover_kdc: Literal["enable", "disable"]
    # KDC IPv4 addresses for Kerberos authentication.
    kdc_ip: list[ExchangeKdcipObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ExchangePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Exchange:
    """
    Configure MS Exchange server entries.
    
    Path: user/exchange
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
    ) -> ExchangeObject: ...
    
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
    ) -> ExchangeObject: ...
    
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
    ) -> list[ExchangeObject]: ...
    
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
    ) -> ExchangeResponse: ...
    
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
    ) -> ExchangeResponse: ...
    
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
    ) -> list[ExchangeResponse]: ...
    
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
    ) -> ExchangeObject | list[ExchangeObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        kdc_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExchangeObject: ...
    
    @overload
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
        kdc_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        kdc_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        kdc_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        kdc_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExchangeObject: ...
    
    @overload
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
        kdc_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        kdc_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        kdc_ip: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ExchangeObject: ...
    
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
        kdc_ip: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Exchange",
    "ExchangePayload",
    "ExchangeObject",
]