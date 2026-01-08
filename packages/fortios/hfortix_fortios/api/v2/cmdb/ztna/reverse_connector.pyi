from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ReverseConnectorPayload(TypedDict, total=False):
    """
    Type hints for ztna/reverse_connector payload fields.
    
    Configure ZTNA Reverse-Connector.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: trusted-server-ca)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: certificate)

    **Usage:**
        payload: ReverseConnectorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Reverse-Connector name
    status: NotRequired[Literal["enable", "disable"]]  # Reverse-Connector status.
    address: str  # Connector service edge adress(IP or FQDN).
    port: NotRequired[int]  # Port number that traffic uses to connect to connector servic
    health_check_interval: NotRequired[int]  # Health check interval in seconds
    ssl_max_version: NotRequired[Literal["tls-1.1", "tls-1.2", "tls-1.3"]]  # Highest TLS version acceptable from a server.
    certificate: NotRequired[str]  # The name of the certificate to use for SSL handshake.
    trusted_server_ca: NotRequired[str]  # Trusted Server CA certificate used by SSL connection.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class ReverseConnectorResponse(TypedDict):
    """
    Type hints for ztna/reverse_connector API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    status: Literal["enable", "disable"]
    address: str
    port: int
    health_check_interval: int
    ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"]
    certificate: str
    trusted_server_ca: str


@final
class ReverseConnectorObject:
    """Typed FortiObject for ztna/reverse_connector with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Reverse-Connector name
    name: str
    # Reverse-Connector status.
    status: Literal["enable", "disable"]
    # Connector service edge adress(IP or FQDN).
    address: str
    # Port number that traffic uses to connect to connector service edge(0 - 65535;).
    port: int
    # Health check interval in seconds (0 - 600, default = 60, 0 = disable).
    health_check_interval: int
    # Highest TLS version acceptable from a server.
    ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"]
    # The name of the certificate to use for SSL handshake.
    certificate: str
    # Trusted Server CA certificate used by SSL connection.
    trusted_server_ca: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ReverseConnectorPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class ReverseConnector:
    """
    Configure ZTNA Reverse-Connector.
    
    Path: ztna/reverse_connector
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
    ) -> ReverseConnectorObject: ...
    
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
    ) -> ReverseConnectorObject: ...
    
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
    ) -> list[ReverseConnectorObject]: ...
    
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
    ) -> ReverseConnectorResponse: ...
    
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
    ) -> ReverseConnectorResponse: ...
    
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
    ) -> list[ReverseConnectorResponse]: ...
    
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
    ) -> ReverseConnectorObject | list[ReverseConnectorObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ReverseConnectorObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ReverseConnectorObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
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
    ) -> ReverseConnectorObject: ...
    
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
        payload_dict: ReverseConnectorPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        address: str | None = ...,
        port: int | None = ...,
        health_check_interval: int | None = ...,
        ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        certificate: str | None = ...,
        trusted_server_ca: str | None = ...,
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
    "ReverseConnector",
    "ReverseConnectorPayload",
    "ReverseConnectorObject",
]