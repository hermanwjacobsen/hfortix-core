from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class WccpPayload(TypedDict, total=False):
    """
    Type hints for system/wccp payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: WccpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    service_id: NotRequired[str]  # Service ID.
    router_id: NotRequired[str]  # IP address known to all cache engines. If all cache engines 
    cache_id: NotRequired[str]  # IP address known to all routers. If the addresses are the sa
    group_address: NotRequired[str]  # IP multicast address used by the cache routers. For the Fort
    server_list: NotRequired[str]  # IP addresses and netmasks for up to four cache servers.
    router_list: NotRequired[str]  # IP addresses of one or more WCCP routers.
    ports_defined: NotRequired[Literal["source", "destination"]]  # Match method.
    server_type: NotRequired[Literal["forward", "proxy"]]  # Cache server type.
    ports: NotRequired[str]  # Service ports.
    authentication: NotRequired[Literal["enable", "disable"]]  # Enable/disable MD5 authentication.
    password: NotRequired[str]  # Password for MD5 authentication.
    forward_method: NotRequired[Literal["GRE", "L2", "any"]]  # Method used to forward traffic to the cache servers.
    cache_engine_method: NotRequired[Literal["GRE", "L2"]]  # Method used to forward traffic to the routers or to return t
    service_type: NotRequired[Literal["auto", "standard", "dynamic"]]  # WCCP service type used by the cache server for logical inter
    primary_hash: NotRequired[Literal["src-ip", "dst-ip", "src-port", "dst-port"]]  # Hash method.
    priority: NotRequired[int]  # Service priority.
    protocol: NotRequired[int]  # Service protocol.
    assignment_weight: NotRequired[int]  # Assignment of hash weight/ratio for the WCCP cache engine.
    assignment_bucket_format: NotRequired[Literal["wccp-v2", "cisco-implementation"]]  # Assignment bucket format for the WCCP cache engine.
    return_method: NotRequired[Literal["GRE", "L2", "any"]]  # Method used to decline a redirected packet and return it to 
    assignment_method: NotRequired[Literal["HASH", "MASK", "any"]]  # Hash key assignment preference.
    assignment_srcaddr_mask: NotRequired[str]  # Assignment source address mask.
    assignment_dstaddr_mask: NotRequired[str]  # Assignment destination address mask.


class Wccp:
    """
    Configure WCCP.
    
    Path: system/wccp
    Category: cmdb
    Primary Key: service-id
    """
    
    def get(
        self,
        service_id: str | None = ...,
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
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | None = ...,
        router_list: str | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | None = ...,
        router_list: str | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        service_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        service_id: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: WccpPayload | None = ...,
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