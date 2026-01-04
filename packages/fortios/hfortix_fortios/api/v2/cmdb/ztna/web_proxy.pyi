from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class WebProxyPayload(TypedDict, total=False):
    """
    Type hints for ztna/web_proxy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: WebProxyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # ZTNA proxy name.
    vip: NotRequired[str]  # Virtual IP name.
    host: NotRequired[str]  # Virtual or real host name.
    decrypted_traffic_mirror: NotRequired[str]  # Decrypted traffic mirror.
    log_blocked_traffic: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging of blocked traffic.
    auth_portal: NotRequired[Literal["disable", "enable"]]  # Enable/disable authentication portal.
    auth_virtual_host: NotRequired[str]  # Virtual host for authentication portal.
    vip6: NotRequired[str]  # Virtual IPv6 name.
    svr_pool_multiplex: NotRequired[Literal["enable", "disable"]]  # Enable/disable server pool multiplexing (default = disable).
    svr_pool_ttl: NotRequired[int]  # Time-to-live in the server pool for idle connections to serv
    svr_pool_server_max_request: NotRequired[int]  # Maximum number of requests that servers in the server pool h
    svr_pool_server_max_concurrent_request: NotRequired[int]  # Maximum number of concurrent requests that servers in the se
    api_gateway: NotRequired[list[dict[str, Any]]]  # Set IPv4 API Gateway.
    api_gateway6: NotRequired[list[dict[str, Any]]]  # Set IPv6 API Gateway.


class WebProxy:
    """
    Configure ZTNA web-proxy.
    
    Path: ztna/web_proxy
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
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: list[dict[str, Any]] | None = ...,
        api_gateway6: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: list[dict[str, Any]] | None = ...,
        api_gateway6: list[dict[str, Any]] | None = ...,
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
        payload_dict: WebProxyPayload | None = ...,
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