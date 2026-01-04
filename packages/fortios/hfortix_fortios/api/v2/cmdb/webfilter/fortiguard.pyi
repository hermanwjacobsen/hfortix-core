from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FortiguardPayload(TypedDict, total=False):
    """
    Type hints for webfilter/fortiguard payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FortiguardPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    cache_mode: NotRequired[Literal["ttl", "db-ver"]]  # Cache entry expiration mode.
    cache_prefix_match: NotRequired[Literal["enable", "disable"]]  # Enable/disable prefix matching in the cache.
    cache_mem_permille: NotRequired[int]  # Maximum permille of available memory allocated to caching (1
    ovrd_auth_port_http: NotRequired[int]  # Port to use for FortiGuard Web Filter HTTP override authenti
    ovrd_auth_port_https: NotRequired[int]  # Port to use for FortiGuard Web Filter HTTPS override authent
    ovrd_auth_port_https_flow: NotRequired[int]  # Port to use for FortiGuard Web Filter HTTPS override authent
    ovrd_auth_port_warning: NotRequired[int]  # Port to use for FortiGuard Web Filter Warning override authe
    ovrd_auth_https: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of HTTPS for override authentication.
    warn_auth_https: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of HTTPS for warning and authentication.
    close_ports: NotRequired[Literal["enable", "disable"]]  # Close ports used for HTTP/HTTPS override authentication and 
    request_packet_size_limit: NotRequired[int]  # Limit size of URL request packets sent to FortiGuard server 
    embed_image: NotRequired[Literal["enable", "disable"]]  # Enable/disable embedding images into replacement messages (d


class Fortiguard:
    """
    Configure FortiGuard Web Filter service.
    
    Path: webfilter/fortiguard
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
        payload_dict: FortiguardPayload | None = ...,
        cache_mode: Literal["ttl", "db-ver"] | None = ...,
        cache_prefix_match: Literal["enable", "disable"] | None = ...,
        cache_mem_permille: int | None = ...,
        ovrd_auth_port_http: int | None = ...,
        ovrd_auth_port_https: int | None = ...,
        ovrd_auth_port_https_flow: int | None = ...,
        ovrd_auth_port_warning: int | None = ...,
        ovrd_auth_https: Literal["enable", "disable"] | None = ...,
        warn_auth_https: Literal["enable", "disable"] | None = ...,
        close_ports: Literal["enable", "disable"] | None = ...,
        request_packet_size_limit: int | None = ...,
        embed_image: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        cache_mode: Literal["ttl", "db-ver"] | None = ...,
        cache_prefix_match: Literal["enable", "disable"] | None = ...,
        cache_mem_permille: int | None = ...,
        ovrd_auth_port_http: int | None = ...,
        ovrd_auth_port_https: int | None = ...,
        ovrd_auth_port_https_flow: int | None = ...,
        ovrd_auth_port_warning: int | None = ...,
        ovrd_auth_https: Literal["enable", "disable"] | None = ...,
        warn_auth_https: Literal["enable", "disable"] | None = ...,
        close_ports: Literal["enable", "disable"] | None = ...,
        request_packet_size_limit: int | None = ...,
        embed_image: Literal["enable", "disable"] | None = ...,
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
        payload_dict: FortiguardPayload | None = ...,
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