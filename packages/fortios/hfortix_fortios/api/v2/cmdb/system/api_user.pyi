from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ApiUserPayload(TypedDict, total=False):
    """
    Type hints for system/api_user payload fields.
    
    Configure API users.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: accprofile)

    **Usage:**
        payload: ApiUserPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # User name.
    comments: NotRequired[str]  # Comment.
    api_key: NotRequired[str]  # Admin user password.
    accprofile: str  # Admin user access profile.
    vdom: NotRequired[list[dict[str, Any]]]  # Virtual domains.
    schedule: NotRequired[str]  # Schedule name.
    cors_allow_origin: NotRequired[str]  # Value for Access-Control-Allow-Origin on API responses. Avoi
    peer_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable peer authentication.
    peer_group: str  # Peer group name.
    trusthost: NotRequired[list[dict[str, Any]]]  # Trusthost.

# Nested classes for table field children

@final
class ApiUserVdomObject:
    """Typed object for vdom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Virtual domain name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ApiUserTrusthostObject:
    """Typed object for trusthost table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Trusthost type.
    type: Literal["ipv4-trusthost", "ipv6-trusthost"]
    # IPv4 trusted host address.
    ipv4_trusthost: str
    # IPv6 trusted host address.
    ipv6_trusthost: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class ApiUserResponse(TypedDict):
    """
    Type hints for system/api_user API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comments: str
    api_key: str
    accprofile: str
    vdom: list[dict[str, Any]]
    schedule: str
    cors_allow_origin: str
    peer_auth: Literal["enable", "disable"]
    peer_group: str
    trusthost: list[dict[str, Any]]


@final
class ApiUserObject:
    """Typed FortiObject for system/api_user with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # User name.
    name: str
    # Comment.
    comments: str
    # Admin user password.
    api_key: str
    # Admin user access profile.
    accprofile: str
    # Virtual domains.
    vdom: list[ApiUserVdomObject]  # Table field - list of typed objects
    # Schedule name.
    schedule: str
    # Value for Access-Control-Allow-Origin on API responses. Avoid using '*' if possi
    cors_allow_origin: str
    # Enable/disable peer authentication.
    peer_auth: Literal["enable", "disable"]
    # Peer group name.
    peer_group: str
    # Trusthost.
    trusthost: list[ApiUserTrusthostObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ApiUserPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class ApiUser:
    """
    Configure API users.
    
    Path: system/api_user
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
    ) -> ApiUserObject: ...
    
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
    ) -> ApiUserObject: ...
    
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
    ) -> list[ApiUserObject]: ...
    
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
    ) -> ApiUserResponse: ...
    
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
    ) -> ApiUserResponse: ...
    
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
    ) -> list[ApiUserResponse]: ...
    
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
    ) -> ApiUserObject | list[ApiUserObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ApiUserObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ApiUserObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ApiUserObject: ...
    
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
        payload_dict: ApiUserPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        api_key: str | None = ...,
        accprofile: str | None = ...,
        schedule: str | None = ...,
        cors_allow_origin: str | None = ...,
        peer_auth: Literal["enable", "disable"] | None = ...,
        peer_group: str | None = ...,
        trusthost: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ApiUser",
    "ApiUserPayload",
    "ApiUserObject",
]