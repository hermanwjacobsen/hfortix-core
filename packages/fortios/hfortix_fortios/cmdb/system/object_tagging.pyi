from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ObjectTaggingPayload(TypedDict, total=False):
    """
    Type hints for system/object_tagging payload fields.
    
    Configure object tagging.
    
    **Usage:**
        payload: ObjectTaggingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    category: NotRequired[str]  # Tag Category.
    address: NotRequired[Literal["disable", "mandatory", "optional"]]  # Address.
    device: NotRequired[Literal["disable", "mandatory", "optional"]]  # Device.
    interface: NotRequired[Literal["disable", "mandatory", "optional"]]  # Interface.
    multiple: NotRequired[Literal["enable", "disable"]]  # Allow multiple tag selection.
    color: NotRequired[int]  # Color of icon on the GUI.
    tags: NotRequired[list[dict[str, Any]]]  # Tags.


class ObjectTaggingObject(FortiObject[ObjectTaggingPayload]):
    """Typed FortiObject for system/object_tagging with IDE autocomplete support."""
    
    # Tag Category.
    category: str
    # Address.
    address: Literal["disable", "mandatory", "optional"]
    # Device.
    device: Literal["disable", "mandatory", "optional"]
    # Interface.
    interface: Literal["disable", "mandatory", "optional"]
    # Allow multiple tag selection.
    multiple: Literal["enable", "disable"]
    # Color of icon on the GUI.
    color: int
    # Tags.
    tags: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ObjectTaggingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ObjectTagging:
    """
    Configure object tagging.
    
    Path: system/object_tagging
    Category: cmdb
    Primary Key: category
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        category: str,
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
    ) -> ObjectTaggingObject: ...
    
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
    ) -> list[ObjectTaggingObject]: ...
    
    @overload
    def get(
        self,
        category: str | None = ...,
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
        category: str,
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
        category: None = None,
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
        category: str | None = ...,
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
        category: str | None = ...,
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
    ) -> ObjectTaggingObject | list[ObjectTaggingObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ObjectTaggingObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ObjectTaggingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        category: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ObjectTaggingObject: ...
    
    @overload
    def delete(
        self,
        category: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        category: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        category: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        category: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ObjectTagging",
    "ObjectTaggingPayload",
    "ObjectTaggingObject",
]