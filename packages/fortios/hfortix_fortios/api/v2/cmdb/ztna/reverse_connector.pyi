from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ReverseConnectorPayload(TypedDict, total=False):
    """
    Type hints for ztna/reverse_connector payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ReverseConnectorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Reverse-Connector name
    status: NotRequired[Literal["enable", "disable"]]  # Reverse-Connector status.
    address: str  # Connector service edge adress(IP or FQDN).
    port: NotRequired[int]  # Port number that traffic uses to connect to connector servic
    health_check_interval: NotRequired[int]  # Health check interval in seconds (0 - 600, default = 60, 0 =
    ssl_max_version: NotRequired[Literal["tls-1.1", "tls-1.2", "tls-1.3"]]  # Highest TLS version acceptable from a server.
    certificate: NotRequired[str]  # The name of the certificate to use for SSL handshake.
    trusted_server_ca: NotRequired[str]  # Trusted Server CA certificate used by SSL connection.


class ReverseConnector:
    """
    Configure ZTNA Reverse-Connector.
    
    Path: ztna/reverse_connector
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        payload_dict: ReverseConnectorPayload | None = ...,
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