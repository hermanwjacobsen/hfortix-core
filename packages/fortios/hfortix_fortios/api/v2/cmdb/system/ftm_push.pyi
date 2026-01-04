from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FtmPushPayload(TypedDict, total=False):
    """
    Type hints for system/ftm_push payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FtmPushPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    proxy: NotRequired[Literal["enable", "disable"]]  # Enable/disable communication to the proxy server in FortiGua
    interface: NotRequired[str]  # Interface of FortiToken Mobile push services server.
    server: NotRequired[str]  # IPv4 address or domain name of FortiToken Mobile push servic
    server_port: NotRequired[int]  # Port to communicate with FortiToken Mobile push services ser
    server_cert: NotRequired[str]  # Name of the server certificate to be used for SSL.
    server_ip: NotRequired[str]  # IPv4 address of FortiToken Mobile push services server (form
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the use of FortiToken Mobile push services.


class FtmPush:
    """
    Configure FortiToken Mobile push services.
    
    Path: system/ftm_push
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
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
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
        payload_dict: FtmPushPayload | None = ...,
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