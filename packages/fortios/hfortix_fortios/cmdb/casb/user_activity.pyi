from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class UserActivityPayload(TypedDict, total=False):
    """
    Type hints for casb/user_activity payload fields.
    
    Configure CASB user activity.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.casb.saas-application.SaasApplicationEndpoint` (via: application)

    **Usage:**
        payload: UserActivityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # CASB user activity name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    status: NotRequired[Literal["enable", "disable"]]  # CASB user activity status.
    description: NotRequired[str]  # CASB user activity description.
    type: NotRequired[Literal["built-in", "customized"]]  # CASB user activity type.
    casb_name: NotRequired[str]  # CASB user activity signature name.
    application: str  # CASB SaaS application name.
    category: NotRequired[Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"]]  # CASB user activity category.
    match_strategy: NotRequired[Literal["and", "or"]]  # CASB user activity match strategy.
    match: NotRequired[list[dict[str, Any]]]  # CASB user activity match rules.
    control_options: NotRequired[list[dict[str, Any]]]  # CASB control options.


class UserActivityObject(FortiObject[UserActivityPayload]):
    """Typed FortiObject for casb/user_activity with IDE autocomplete support."""
    
    # CASB user activity name.
    name: str
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # CASB user activity status.
    status: Literal["enable", "disable"]
    # CASB user activity description.
    description: str
    # CASB user activity type.
    type: Literal["built-in", "customized"]
    # CASB user activity signature name.
    casb_name: str
    # CASB SaaS application name.
    application: str
    # CASB user activity category.
    category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"]
    # CASB user activity match strategy.
    match_strategy: Literal["and", "or"]
    # CASB user activity match rules.
    match: list[str]  # Auto-flattened from member_table
    # CASB control options.
    control_options: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> UserActivityPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class UserActivity:
    """
    Configure CASB user activity.
    
    Path: casb/user_activity
    Category: cmdb
    Primary Key: name
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
    ) -> UserActivityObject: ...
    
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
    ) -> list[UserActivityObject]: ...
    
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
    ) -> UserActivityObject | list[UserActivityObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> UserActivityObject: ...
    
    @overload
    def post(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> UserActivityObject: ...
    
    @overload
    def put(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> UserActivityObject: ...
    
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
        payload_dict: UserActivityPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        description: str | None = ...,
        type: Literal["built-in", "customized"] | None = ...,
        casb_name: str | None = ...,
        application: str | None = ...,
        category: Literal["activity-control", "tenant-control", "domain-control", "safe-search-control", "advanced-tenant-control", "other"] | None = ...,
        match_strategy: Literal["and", "or"] | None = ...,
        match: str | list[str] | list[dict[str, Any]] | None = ...,
        control_options: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "UserActivity",
    "UserActivityPayload",
    "UserActivityObject",
]