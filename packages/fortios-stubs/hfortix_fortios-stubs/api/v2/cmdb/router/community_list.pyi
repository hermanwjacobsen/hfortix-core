from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class CommunityListPayload(TypedDict, total=False):
    """
    Type hints for router/community_list payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: CommunityListPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Community list name.
    type: Literal[{"description": "Standard community list type", "help": "Standard community list type.", "label": "Standard", "name": "standard"}, {"description": "Expanded community list type", "help": "Expanded community list type.", "label": "Expanded", "name": "expanded"}]  # Community list type (standard or expanded).
    rule: NotRequired[list[dict[str, Any]]]  # Community list rule.


class CommunityList:
    """
    Configure community lists.
    
    Path: router/community_list
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
        payload_dict: CommunityListPayload | None = ...,
        name: str | None = ...,
        type: Literal[{"description": "Standard community list type", "help": "Standard community list type.", "label": "Standard", "name": "standard"}, {"description": "Expanded community list type", "help": "Expanded community list type.", "label": "Expanded", "name": "expanded"}] | None = ...,
        rule: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: CommunityListPayload | None = ...,
        name: str | None = ...,
        type: Literal[{"description": "Standard community list type", "help": "Standard community list type.", "label": "Standard", "name": "standard"}, {"description": "Expanded community list type", "help": "Expanded community list type.", "label": "Expanded", "name": "expanded"}] | None = ...,
        rule: list[dict[str, Any]] | None = ...,
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
        payload_dict: CommunityListPayload | None = ...,
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
    "CommunityList",
    "CommunityListPayload",
]