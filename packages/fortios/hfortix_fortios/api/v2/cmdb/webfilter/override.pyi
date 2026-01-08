from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class OverridePayload(TypedDict, total=False):
    """
    Type hints for webfilter/override payload fields.
    
    Configure FortiGuard Web Filter administrative overrides.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.group.GroupEndpoint` (via: user-group)
        - :class:`~.webfilter.profile.ProfileEndpoint` (via: new-profile, old-profile)

    **Usage:**
        payload: OverridePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Override rule ID.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable override rule.
    scope: NotRequired[Literal["user", "user-group", "ip", "ip6"]]  # Override either the specific user, user group, IPv4 address,
    ip: str  # IPv4 address which the override applies.
    user: str  # Name of the user which the override applies.
    user_group: str  # Specify the user group for which the override applies.
    old_profile: str  # Name of the web filter profile which the override applies.
    new_profile: str  # Name of the new web filter profile used by the override.
    ip6: str  # IPv6 address which the override applies.
    expires: str  # Override expiration date and time, from 5 minutes to 365 fro
    initiator: NotRequired[str]  # Initiating user of override (read-only setting).

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class OverrideResponse(TypedDict):
    """
    Type hints for webfilter/override API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int
    status: Literal["enable", "disable"]
    scope: Literal["user", "user-group", "ip", "ip6"]
    ip: str
    user: str
    user_group: str
    old_profile: str
    new_profile: str
    ip6: str
    expires: str
    initiator: str


@final
class OverrideObject:
    """Typed FortiObject for webfilter/override with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Override rule ID.
    id: int
    # Enable/disable override rule.
    status: Literal["enable", "disable"]
    # Override either the specific user, user group, IPv4 address, or IPv6 address.
    scope: Literal["user", "user-group", "ip", "ip6"]
    # IPv4 address which the override applies.
    ip: str
    # Name of the user which the override applies.
    user: str
    # Specify the user group for which the override applies.
    user_group: str
    # Name of the web filter profile which the override applies.
    old_profile: str
    # Name of the new web filter profile used by the override.
    new_profile: str
    # IPv6 address which the override applies.
    ip6: str
    # Override expiration date and time, from 5 minutes to 365 from now
    expires: str
    # Initiating user of override (read-only setting).
    initiator: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> OverridePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Override:
    """
    Configure FortiGuard Web Filter administrative overrides.
    
    Path: webfilter/override
    Category: cmdb
    Primary Key: id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        id: int,
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
    ) -> OverrideObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        id: int,
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
    ) -> OverrideObject: ...
    
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
    ) -> list[OverrideObject]: ...
    
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int,
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
    ) -> OverrideResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        id: int,
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
    ) -> OverrideResponse: ...
    
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
    ) -> list[OverrideResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int | None = ...,
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
    ) -> OverrideObject | list[OverrideObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> OverrideObject: ...
    
    @overload
    def post(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> OverrideObject: ...
    
    @overload
    def put(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> OverrideObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        scope: Literal["user", "user-group", "ip", "ip6"] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
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
    "Override",
    "OverridePayload",
    "OverrideObject",
]