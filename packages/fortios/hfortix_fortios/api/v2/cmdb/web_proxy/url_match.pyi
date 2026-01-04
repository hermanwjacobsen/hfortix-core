from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class UrlMatchPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/url_match payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: UrlMatchPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Configure a name for the URL to be exempted.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable exempting the URLs matching the URL pattern f
    url_pattern: str  # URL pattern to be exempted from web proxy forwarding, cachin
    forward_server: NotRequired[str]  # Forward server name.
    fast_fallback: NotRequired[str]  # Fast fallback configuration entry name.
    cache_exemption: NotRequired[Literal["enable", "disable"]]  # Enable/disable exempting this URL pattern from caching.
    comment: NotRequired[str]  # Comment.


class UrlMatch:
    """
    Exempt URLs from web proxy forwarding, caching and fast-fallback.
    
    Path: web_proxy/url_match
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
        payload_dict: UrlMatchPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        url_pattern: str | None = ...,
        forward_server: str | None = ...,
        fast_fallback: str | None = ...,
        cache_exemption: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: UrlMatchPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        url_pattern: str | None = ...,
        forward_server: str | None = ...,
        fast_fallback: str | None = ...,
        cache_exemption: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
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
        payload_dict: UrlMatchPayload | None = ...,
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