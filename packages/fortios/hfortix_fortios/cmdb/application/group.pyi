from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class GroupPayload(TypedDict, total=False):
    """
    Type hints for application/group payload fields.
    
    Configure firewall application groups.
    
    **Usage:**
        payload: GroupPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Application group name.
    comment: NotRequired[str]  # Comments.
    type: NotRequired[Literal["application", "filter"]]  # Application group type.
    application: NotRequired[list[dict[str, Any]]]  # Application ID list.
    category: NotRequired[list[dict[str, Any]]]  # Application category ID list.
    risk: NotRequired[list[dict[str, Any]]]  # Risk, or impact, of allowing traffic from this application t
    protocols: NotRequired[list[dict[str, Any]]]  # Application protocol filter.
    vendor: NotRequired[list[dict[str, Any]]]  # Application vendor filter.
    technology: NotRequired[list[dict[str, Any]]]  # Application technology filter.
    behavior: NotRequired[list[dict[str, Any]]]  # Application behavior filter.
    popularity: NotRequired[Literal["1", "2", "3", "4", "5"]]  # Application popularity filter (1 - 5, from least to most pop


class GroupObject(FortiObject[GroupPayload]):
    """Typed FortiObject for application/group with IDE autocomplete support."""
    
    # Application group name.
    name: str
    # Comments.
    comment: str
    # Application group type.
    type: Literal["application", "filter"]
    # Application ID list.
    application: list[str]  # Auto-flattened from member_table
    # Application category ID list.
    category: list[str]  # Auto-flattened from member_table
    # Risk, or impact, of allowing traffic from this application to occur (1 - 5; Low,
    risk: list[str]  # Auto-flattened from member_table
    # Application protocol filter.
    protocols: list[str]  # Auto-flattened from member_table
    # Application vendor filter.
    vendor: list[str]  # Auto-flattened from member_table
    # Application technology filter.
    technology: list[str]  # Auto-flattened from member_table
    # Application behavior filter.
    behavior: list[str]  # Auto-flattened from member_table
    # Application popularity filter (1 - 5, from least to most popular).
    popularity: Literal["1", "2", "3", "4", "5"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> GroupPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Group:
    """
    Configure firewall application groups.
    
    Path: application/group
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
    ) -> GroupObject: ...
    
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
    ) -> list[GroupObject]: ...
    
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
    ) -> GroupObject | list[GroupObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        vendor: str | list[str] | list[dict[str, Any]] | None = ...,
        technology: str | list[str] | list[dict[str, Any]] | None = ...,
        behavior: str | list[str] | list[dict[str, Any]] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GroupObject: ...
    
    @overload
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        vendor: str | list[str] | list[dict[str, Any]] | None = ...,
        technology: str | list[str] | list[dict[str, Any]] | None = ...,
        behavior: str | list[str] | list[dict[str, Any]] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        vendor: str | list[str] | list[dict[str, Any]] | None = ...,
        technology: str | list[str] | list[dict[str, Any]] | None = ...,
        behavior: str | list[str] | list[dict[str, Any]] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        vendor: str | list[str] | list[dict[str, Any]] | None = ...,
        technology: str | list[str] | list[dict[str, Any]] | None = ...,
        behavior: str | list[str] | list[dict[str, Any]] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        vendor: str | list[str] | list[dict[str, Any]] | None = ...,
        technology: str | list[str] | list[dict[str, Any]] | None = ...,
        behavior: str | list[str] | list[dict[str, Any]] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GroupObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        vendor: str | list[str] | list[dict[str, Any]] | None = ...,
        technology: str | list[str] | list[dict[str, Any]] | None = ...,
        behavior: str | list[str] | list[dict[str, Any]] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        vendor: str | list[str] | list[dict[str, Any]] | None = ...,
        technology: str | list[str] | list[dict[str, Any]] | None = ...,
        behavior: str | list[str] | list[dict[str, Any]] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        vendor: str | list[str] | list[dict[str, Any]] | None = ...,
        technology: str | list[str] | list[dict[str, Any]] | None = ...,
        behavior: str | list[str] | list[dict[str, Any]] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> GroupObject: ...
    
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
        payload_dict: GroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        type: Literal["application", "filter"] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        risk: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        vendor: str | list[str] | list[dict[str, Any]] | None = ...,
        technology: str | list[str] | list[dict[str, Any]] | None = ...,
        behavior: str | list[str] | list[dict[str, Any]] | None = ...,
        popularity: Literal["1", "2", "3", "4", "5"] | list[str] | list[dict[str, Any]] | None = ...,
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
    "Group",
    "GroupPayload",
    "GroupObject",
]