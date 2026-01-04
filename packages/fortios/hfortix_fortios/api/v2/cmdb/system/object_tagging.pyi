from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ObjectTaggingPayload(TypedDict, total=False):
    """
    Type hints for system/object_tagging payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class ObjectTagging:
    """
    Configure object tagging.
    
    Path: system/object_tagging
    Category: cmdb
    Primary Key: category
    """
    
    def get(
        self,
        category: str | None = ...,
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
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        category: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        category: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
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