from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class DictionaryPayload(TypedDict, total=False):
    """
    Type hints for dlp/dictionary payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: DictionaryPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    name: str  # Name of table containing the dictionary.
    match_type: Literal["match-all", "match-any"]  # Logical relation between entries (default = match-any).
    match_around: NotRequired[Literal["enable", "disable"]]  # Enable/disable match-around support.
    comment: NotRequired[str]  # Optional comments.
    entries: list[dict[str, Any]]  # DLP dictionary entries.


class Dictionary:
    """
    Configure dictionaries used by DLP blocking.
    
    Path: dlp/dictionary
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
        payload_dict: DictionaryPayload | None = ...,
        uuid: str | None = ...,
        name: str | None = ...,
        match_type: Literal["match-all", "match-any"] | None = ...,
        match_around: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        entries: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: DictionaryPayload | None = ...,
        uuid: str | None = ...,
        name: str | None = ...,
        match_type: Literal["match-all", "match-any"] | None = ...,
        match_around: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        entries: list[dict[str, Any]] | None = ...,
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
        payload_dict: DictionaryPayload | None = ...,
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