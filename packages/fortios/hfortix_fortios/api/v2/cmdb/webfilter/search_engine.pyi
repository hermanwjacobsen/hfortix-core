from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SearchEnginePayload(TypedDict, total=False):
    """
    Type hints for webfilter/search_engine payload fields.
    
    Configure web filter search engines.
    
    **Usage:**
        payload: SearchEnginePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Search engine name.
    hostname: NotRequired[str]  # Hostname (regular expression).
    url: NotRequired[str]  # URL (regular expression).
    query: NotRequired[str]  # Code used to prefix a query
    safesearch: NotRequired[Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"]]  # Safe search method. You can disable safe search, add the saf
    charset: NotRequired[Literal["utf-8", "gb2312"]]  # Search engine charset.
    safesearch_str: NotRequired[str]  # Safe search parameter used in the URL in URL mode. In transl

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class SearchEngineResponse(TypedDict):
    """
    Type hints for webfilter/search_engine API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    hostname: str
    url: str
    query: str
    safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"]
    charset: Literal["utf-8", "gb2312"]
    safesearch_str: str


@final
class SearchEngineObject:
    """Typed FortiObject for webfilter/search_engine with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Search engine name.
    name: str
    # Hostname (regular expression).
    hostname: str
    # URL (regular expression).
    url: str
    # Code used to prefix a query (must end with an equals character).
    query: str
    # Safe search method. You can disable safe search, add the safe search string to U
    safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"]
    # Search engine charset.
    charset: Literal["utf-8", "gb2312"]
    # Safe search parameter used in the URL in URL mode. In translate mode, it provide
    safesearch_str: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SearchEnginePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class SearchEngine:
    """
    Configure web filter search engines.
    
    Path: webfilter/search_engine
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SearchEngineObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SearchEngineObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[SearchEngineObject]: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> SearchEngineResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> SearchEngineResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[SearchEngineResponse]: ...
    
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
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
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
    ) -> SearchEngineObject | list[SearchEngineObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SearchEngineObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SearchEngineObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SearchEngineObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
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
    "SearchEngine",
    "SearchEnginePayload",
    "SearchEngineObject",
]