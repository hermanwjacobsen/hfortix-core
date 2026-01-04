from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ExplicitPayload(TypedDict, total=False):
    """
    Type hints for ftp_proxy/explicit payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ExplicitPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the explicit FTP proxy.
    incoming_port: NotRequired[str]  # Accept incoming FTP requests on one or more ports.
    incoming_ip: NotRequired[str]  # Accept incoming FTP requests from this IP address. An interf
    outgoing_ip: NotRequired[str]  # Outgoing FTP requests will leave from this IP address. An in
    sec_default_action: NotRequired[Literal["accept", "deny"]]  # Accept or deny explicit FTP proxy sessions when no FTP proxy
    server_data_mode: NotRequired[Literal["client", "passive"]]  # Determine mode of data session on FTP server side.
    ssl: NotRequired[Literal["enable", "disable"]]  # Enable/disable the explicit FTPS proxy.
    ssl_cert: NotRequired[list[dict[str, Any]]]  # List of certificate names to use for SSL connections to this
    ssl_dh_bits: NotRequired[Literal["768", "1024", "1536", "2048"]]  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    ssl_algorithm: NotRequired[Literal["high", "medium", "low"]]  # Relative strength of encryption algorithms accepted in negot


class Explicit:
    """
    Configure explicit FTP proxy settings.
    
    Path: ftp_proxy/explicit
    Category: cmdb
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
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
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
        payload_dict: ExplicitPayload | None = ...,
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