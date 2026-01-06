from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class KeywordPayload(TypedDict, total=False):
    """
    Type hints for videofilter/keyword payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: KeywordPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID.
    name: str  # Name.
    comment: NotRequired[str]  # Comment.
    match: Literal[{"description": "Match any keyword", "help": "Match any keyword.", "label": "Or", "name": "or"}, {"description": "Match all keywords", "help": "Match all keywords.", "label": "And", "name": "and"}]  # Keyword matching logic.
    word: NotRequired[list[dict[str, Any]]]  # List of keywords.


class Keyword:
    """
    Configure video filter keywords.
    
    Path: videofilter/keyword
    Category: cmdb
    Primary Key: id
    """
    
    def get(
        self,
        id: int | None = ...,
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
        payload_dict: KeywordPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        match: Literal[{"description": "Match any keyword", "help": "Match any keyword.", "label": "Or", "name": "or"}, {"description": "Match all keywords", "help": "Match all keywords.", "label": "And", "name": "and"}] | None = ...,
        word: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: KeywordPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        match: Literal[{"description": "Match any keyword", "help": "Match any keyword.", "label": "Or", "name": "or"}, {"description": "Match all keywords", "help": "Match all keywords.", "label": "And", "name": "and"}] | None = ...,
        word: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: KeywordPayload | None = ...,
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


__all__ = [
    "Keyword",
    "KeywordPayload",
]