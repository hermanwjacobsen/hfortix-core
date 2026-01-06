from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class RegionPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/region payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: RegionPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # FortiAP region name.
    comments: NotRequired[str]  # Comments.
    grayscale: NotRequired[Literal[{"description": "Enable region image grayscale", "help": "Enable region image grayscale.", "label": "Enable", "name": "enable"}, {"description": "Disable region image grayscale", "help": "Disable region image grayscale.", "label": "Disable", "name": "disable"}]]  # Region image grayscale.
    opacity: NotRequired[int]  # Region image opacity (0 - 100).


class Region:
    """
    Configure FortiAP regions (for floor plans and maps).
    
    Path: wireless_controller/region
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
        payload_dict: RegionPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        grayscale: Literal[{"description": "Enable region image grayscale", "help": "Enable region image grayscale.", "label": "Enable", "name": "enable"}, {"description": "Disable region image grayscale", "help": "Disable region image grayscale.", "label": "Disable", "name": "disable"}] | None = ...,
        opacity: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: RegionPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        grayscale: Literal[{"description": "Enable region image grayscale", "help": "Enable region image grayscale.", "label": "Enable", "name": "enable"}, {"description": "Disable region image grayscale", "help": "Disable region image grayscale.", "label": "Disable", "name": "disable"}] | None = ...,
        opacity: int | None = ...,
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
        payload_dict: RegionPayload | None = ...,
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
    "Region",
    "RegionPayload",
]