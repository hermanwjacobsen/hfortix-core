from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class DataTypePayload(TypedDict, total=False):
    """
    Type hints for dlp/data_type payload fields.
    
    Configure predefined data type used by DLP blocking.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.dlp.dictionary.DictionaryEndpoint` (via: match-around)

    **Usage:**
        payload: DataTypePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name of table containing the data type.
    pattern: NotRequired[str]  # Regular expression pattern string without look around.
    verify: NotRequired[str]  # Regular expression pattern string used to verify the data ty
    verify2: NotRequired[str]  # Extra regular expression pattern string used to verify the d
    match_around: NotRequired[str]  # Dictionary to check whether it has a match around (Only supp
    look_back: int  # Number of characters required to save for verification (1 - 
    look_ahead: int  # Number of characters to obtain in advance for verification (
    match_back: int  # Number of characters in front for match-around (1 - 4096, de
    match_ahead: int  # Number of characters behind for match-around (1 - 4096, defa
    transform: NotRequired[str]  # Template to transform user input to a pattern using capture 
    verify_transformed_pattern: NotRequired[Literal["enable", "disable"]]  # Enable/disable verification for transformed pattern.
    comment: NotRequired[str]  # Optional comments.


class DataTypeObject(FortiObject[DataTypePayload]):
    """Typed FortiObject for dlp/data_type with IDE autocomplete support."""
    
    # Name of table containing the data type.
    name: str
    # Regular expression pattern string without look around.
    pattern: str
    # Regular expression pattern string used to verify the data type.
    verify: str
    # Extra regular expression pattern string used to verify the data type.
    verify2: str
    # Dictionary to check whether it has a match around (Only support match-any and ba
    match_around: str
    # Number of characters required to save for verification (1 - 255, default = 1).
    look_back: int
    # Number of characters to obtain in advance for verification (1 - 255, default = 1
    look_ahead: int
    # Number of characters in front for match-around (1 - 4096, default = 1).
    match_back: int
    # Number of characters behind for match-around (1 - 4096, default = 1).
    match_ahead: int
    # Template to transform user input to a pattern using capture group from 'pattern'
    transform: str
    # Enable/disable verification for transformed pattern.
    verify_transformed_pattern: Literal["enable", "disable"]
    # Optional comments.
    comment: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> DataTypePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class DataType:
    """
    Configure predefined data type used by DLP blocking.
    
    Path: dlp/data_type
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
    ) -> DataTypeObject: ...
    
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
    ) -> list[DataTypeObject]: ...
    
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
    ) -> DataTypeObject | list[DataTypeObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DataTypeObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
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
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DataTypeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
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
    ) -> DataTypeObject: ...
    
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
        payload_dict: DataTypePayload | None = ...,
        name: str | None = ...,
        pattern: str | None = ...,
        verify: str | None = ...,
        verify2: str | None = ...,
        match_around: str | None = ...,
        look_back: int | None = ...,
        look_ahead: int | None = ...,
        match_back: int | None = ...,
        match_ahead: int | None = ...,
        transform: str | None = ...,
        verify_transformed_pattern: Literal["enable", "disable"] | None = ...,
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
    "DataType",
    "DataTypePayload",
    "DataTypeObject",
]