from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class FortiguardPayload(TypedDict, total=False):
    """
    Type hints for webfilter/fortiguard payload fields.
    
    Configure FortiGuard Web Filter service.
    
    **Usage:**
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


class FortiguardObject(FortiObject[FortiguardPayload]):
    """Typed FortiObject for webfilter/fortiguard with IDE autocomplete support."""
    
    # Cache entry expiration mode.
    cache_mode: Literal["ttl", "db-ver"]
    # Enable/disable prefix matching in the cache.
    cache_prefix_match: Literal["enable", "disable"]
    # Maximum permille of available memory allocated to caching (1 - 150).
    cache_mem_permille: int
    # Port to use for FortiGuard Web Filter HTTP override authentication.
    ovrd_auth_port_http: int
    # Port to use for FortiGuard Web Filter HTTPS override authentication in proxy mod
    ovrd_auth_port_https: int
    # Port to use for FortiGuard Web Filter HTTPS override authentication in flow mode
    ovrd_auth_port_https_flow: int
    # Port to use for FortiGuard Web Filter Warning override authentication.
    ovrd_auth_port_warning: int
    # Enable/disable use of HTTPS for override authentication.
    ovrd_auth_https: Literal["enable", "disable"]
    # Enable/disable use of HTTPS for warning and authentication.
    warn_auth_https: Literal["enable", "disable"]
    # Close ports used for HTTP/HTTPS override authentication and disable user overrid
    close_ports: Literal["enable", "disable"]
    # Limit size of URL request packets sent to FortiGuard server (0 for default).
    request_packet_size_limit: int
    # Enable/disable embedding images into replacement messages (default = enable).
    embed_image: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiguardPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Fortiguard:
    """
    Configure FortiGuard Web Filter service.
    
    Path: webfilter/fortiguard
    Category: cmdb
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> FortiguardObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FortiguardObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
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
    "Fortiguard",
    "FortiguardPayload",
    "FortiguardObject",
]