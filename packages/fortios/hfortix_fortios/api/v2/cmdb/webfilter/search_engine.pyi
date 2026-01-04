from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SearchEnginePayload(TypedDict, total=False):
    """
    Type hints for webfilter/search_engine payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SearchEnginePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Search engine name.
    hostname: NotRequired[str]  # Hostname (regular expression).
    url: NotRequired[str]  # URL (regular expression).
    query: NotRequired[str]  # Code used to prefix a query (must end with an equals charact
    safesearch: NotRequired[Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"]]  # Safe search method. You can disable safe search, add the saf
    charset: NotRequired[Literal["utf-8", "gb2312"]]  # Search engine charset.
    safesearch_str: NotRequired[str]  # Safe search parameter used in the URL in URL mode. In transl


class SearchEngine:
    """
    Configure web filter search engines.
    
    Path: webfilter/search_engine
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
        payload_dict: SearchEnginePayload | None = ...,
        name: str | None = ...,
        hostname: str | None = ...,
        url: str | None = ...,
        query: str | None = ...,
        safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"] | None = ...,
        charset: Literal["utf-8", "gb2312"] | None = ...,
        safesearch_str: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SearchEnginePayload | None = ...,
        name: str | None = ...,
        hostname: str | None = ...,
        url: str | None = ...,
        query: str | None = ...,
        safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"] | None = ...,
        charset: Literal["utf-8", "gb2312"] | None = ...,
        safesearch_str: str | None = ...,
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
        payload_dict: SearchEnginePayload | None = ...,
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