from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AccessProxyPayload(TypedDict, total=False):
    """
    Type hints for firewall/access_proxy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AccessProxyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Access Proxy name.
    vip: str  # Virtual IP name.
    auth_portal: NotRequired[Literal["disable", "enable"]]  # Enable/disable authentication portal.
    auth_virtual_host: NotRequired[str]  # Virtual host for authentication portal.
    log_blocked_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging of blocked traffic.
    add_vhost_domain_to_dnsdb: NotRequired[Literal["enable", "disable"]]  # Enable/disable adding vhost/domain to dnsdb for ztna dox tun
    svr_pool_multiplex: NotRequired[Literal["enable", "disable"]]  # Enable/disable server pool multiplexing (default = disable).
    svr_pool_ttl: NotRequired[int]  # Time-to-live in the server pool for idle connections to serv
    svr_pool_server_max_request: NotRequired[int]  # Maximum number of requests that servers in server pool handl
    svr_pool_server_max_concurrent_request: NotRequired[int]  # Maximum number of concurrent requests that servers in server
    decrypted_traffic_mirror: NotRequired[str]  # Decrypted traffic mirror.
    api_gateway: NotRequired[list[dict[str, Any]]]  # Set IPv4 API Gateway.
    api_gateway6: NotRequired[list[dict[str, Any]]]  # Set IPv6 API Gateway.


class AccessProxy:
    """
    Configure IPv4 access proxy.
    
    Path: firewall/access_proxy
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
        payload_dict: AccessProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: list[dict[str, Any]] | None = ...,
        api_gateway6: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AccessProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
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
        payload_dict: AccessProxyPayload | None = ...,
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