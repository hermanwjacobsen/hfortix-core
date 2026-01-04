from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class WispPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/wisp payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: WispPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Server name.
    comment: NotRequired[str]  # Comment.
    outgoing_ip: NotRequired[str]  # WISP outgoing IP address.
    server_ip: str  # WISP server IP address.
    server_port: int  # WISP server port (1 - 65535, default = 15868).
    max_connections: NotRequired[int]  # Maximum number of web proxy WISP connections (4 - 4096, defa
    timeout: NotRequired[int]  # Period of time before WISP requests time out (1 - 15 sec, de


class Wisp:
    """
    Configure Websense Integrated Services Protocol (WISP) servers.
    
    Path: web_proxy/wisp
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
        payload_dict: WispPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        outgoing_ip: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        max_connections: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: WispPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        outgoing_ip: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        max_connections: int | None = ...,
        timeout: int | None = ...,
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
        payload_dict: WispPayload | None = ...,
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