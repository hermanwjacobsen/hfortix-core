from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class UrlMatchPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/url_match payload fields.
    
    Exempt URLs from web proxy forwarding, caching and fast-fallback.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.web-proxy.fast-fallback.FastFallbackEndpoint` (via: fast-fallback)
        - :class:`~.web-proxy.forward-server.ForwardServerEndpoint` (via: forward-server)
        - :class:`~.web-proxy.forward-server-group.ForwardServerGroupEndpoint` (via: forward-server)

    **Usage:**
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

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class UrlMatchResponse(TypedDict):
    """
    Type hints for web_proxy/url_match API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    status: Literal["enable", "disable"]
    url_pattern: str
    forward_server: str
    fast_fallback: str
    cache_exemption: Literal["enable", "disable"]
    comment: str


@final
class UrlMatchObject:
    """Typed FortiObject for web_proxy/url_match with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Configure a name for the URL to be exempted.
    name: str
    # Enable/disable exempting the URLs matching the URL pattern from web proxy forwar
    status: Literal["enable", "disable"]
    # URL pattern to be exempted from web proxy forwarding, caching and fast-fallback.
    url_pattern: str
    # Forward server name.
    forward_server: str
    # Fast fallback configuration entry name.
    fast_fallback: str
    # Enable/disable exempting this URL pattern from caching.
    cache_exemption: Literal["enable", "disable"]
    # Comment.
    comment: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> UrlMatchPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class UrlMatch:
    """
    Exempt URLs from web proxy forwarding, caching and fast-fallback.
    
    Path: web_proxy/url_match
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
    ) -> UrlMatchObject: ...
    
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
    ) -> UrlMatchObject: ...
    
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
    ) -> list[UrlMatchObject]: ...
    
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
    ) -> UrlMatchResponse: ...
    
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
    ) -> UrlMatchResponse: ...
    
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
    ) -> list[UrlMatchResponse]: ...
    
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
    ) -> UrlMatchObject | list[UrlMatchObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> UrlMatchObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> UrlMatchObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    ) -> UrlMatchObject: ...
    
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
    "UrlMatch",
    "UrlMatchPayload",
    "UrlMatchObject",
]