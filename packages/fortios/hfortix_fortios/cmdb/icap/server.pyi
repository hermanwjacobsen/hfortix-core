from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ServerPayload(TypedDict, total=False):
    """
    Type hints for icap/server payload fields.
    
    Configure ICAP servers.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: ssl-cert)

    **Usage:**
        payload: ServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Server name.
    addr_type: NotRequired[Literal["ip4", "ip6", "fqdn"]]  # Address type of the remote ICAP server: IPv4, IPv6 or FQDN.
    ip_address: str  # IPv4 address of the ICAP server.
    ip6_address: str  # IPv6 address of the ICAP server.
    fqdn: NotRequired[str]  # ICAP remote server Fully Qualified Domain Name (FQDN).
    port: NotRequired[int]  # ICAP server port.
    max_connections: NotRequired[int]  # Maximum number of concurrent connections to ICAP server (unl
    secure: NotRequired[Literal["disable", "enable"]]  # Enable/disable secure connection to ICAP server.
    ssl_cert: NotRequired[str]  # CA certificate name.
    healthcheck: NotRequired[Literal["disable", "enable"]]  # Enable/disable ICAP remote server health checking. Attempts 
    healthcheck_service: str  # ICAP Service name to use for health checks.


class ServerObject(FortiObject[ServerPayload]):
    """Typed FortiObject for icap/server with IDE autocomplete support."""
    
    # Server name.
    name: str
    # Address type of the remote ICAP server: IPv4, IPv6 or FQDN.
    addr_type: Literal["ip4", "ip6", "fqdn"]
    # IPv4 address of the ICAP server.
    ip_address: str
    # IPv6 address of the ICAP server.
    ip6_address: str
    # ICAP remote server Fully Qualified Domain Name (FQDN).
    fqdn: str
    # ICAP server port.
    port: int
    # Maximum number of concurrent connections to ICAP server (unlimited = 0, default 
    max_connections: int
    # Enable/disable secure connection to ICAP server.
    secure: Literal["disable", "enable"]
    # CA certificate name.
    ssl_cert: str
    # Enable/disable ICAP remote server health checking. Attempts to connect to the re
    healthcheck: Literal["disable", "enable"]
    # ICAP Service name to use for health checks.
    healthcheck_service: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Server:
    """
    Configure ICAP servers.
    
    Path: icap/server
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
    ) -> ServerObject: ...
    
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
    ) -> list[ServerObject]: ...
    
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
    ) -> ServerObject | list[ServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip4", "ip6", "fqdn"] | None = ...,
        ip_address: str | None = ...,
        ip6_address: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        max_connections: int | None = ...,
        secure: Literal["disable", "enable"] | None = ...,
        ssl_cert: str | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        healthcheck_service: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip4", "ip6", "fqdn"] | None = ...,
        ip_address: str | None = ...,
        ip6_address: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        max_connections: int | None = ...,
        secure: Literal["disable", "enable"] | None = ...,
        ssl_cert: str | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        healthcheck_service: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip4", "ip6", "fqdn"] | None = ...,
        ip_address: str | None = ...,
        ip6_address: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        max_connections: int | None = ...,
        secure: Literal["disable", "enable"] | None = ...,
        ssl_cert: str | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        healthcheck_service: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip4", "ip6", "fqdn"] | None = ...,
        ip_address: str | None = ...,
        ip6_address: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        max_connections: int | None = ...,
        secure: Literal["disable", "enable"] | None = ...,
        ssl_cert: str | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        healthcheck_service: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip4", "ip6", "fqdn"] | None = ...,
        ip_address: str | None = ...,
        ip6_address: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        max_connections: int | None = ...,
        secure: Literal["disable", "enable"] | None = ...,
        ssl_cert: str | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        healthcheck_service: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip4", "ip6", "fqdn"] | None = ...,
        ip_address: str | None = ...,
        ip6_address: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        max_connections: int | None = ...,
        secure: Literal["disable", "enable"] | None = ...,
        ssl_cert: str | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        healthcheck_service: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip4", "ip6", "fqdn"] | None = ...,
        ip_address: str | None = ...,
        ip6_address: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        max_connections: int | None = ...,
        secure: Literal["disable", "enable"] | None = ...,
        ssl_cert: str | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        healthcheck_service: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip4", "ip6", "fqdn"] | None = ...,
        ip_address: str | None = ...,
        ip6_address: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        max_connections: int | None = ...,
        secure: Literal["disable", "enable"] | None = ...,
        ssl_cert: str | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        healthcheck_service: str | None = ...,
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
    ) -> ServerObject: ...
    
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
        payload_dict: ServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip4", "ip6", "fqdn"] | None = ...,
        ip_address: str | None = ...,
        ip6_address: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        max_connections: int | None = ...,
        secure: Literal["disable", "enable"] | None = ...,
        ssl_cert: str | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        healthcheck_service: str | None = ...,
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
    "Server",
    "ServerPayload",
    "ServerObject",
]