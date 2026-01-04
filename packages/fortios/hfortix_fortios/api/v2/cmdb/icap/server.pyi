from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ServerPayload(TypedDict, total=False):
    """
    Type hints for icap/server payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Server:
    """
    Configure ICAP servers.
    
    Path: icap/server
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        payload_dict: ServerPayload | None = ...,
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