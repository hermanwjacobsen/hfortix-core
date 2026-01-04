from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FortishieldPayload(TypedDict, total=False):
    """
    Type hints for emailfilter/fortishield payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FortishieldPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    spam_submit_srv: str  # Hostname of the spam submission server.
    spam_submit_force: NotRequired[Literal["enable", "disable"]]  # Enable/disable force insertion of a new mime entity for the 
    spam_submit_txt2htm: NotRequired[Literal["enable", "disable"]]  # Enable/disable conversion of text email to HTML email.


class Fortishield:
    """
    Configure FortiGuard - AntiSpam.
    
    Path: emailfilter/fortishield
    Category: cmdb
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
        payload_dict: FortishieldPayload | None = ...,
        spam_submit_srv: str | None = ...,
        spam_submit_force: Literal["enable", "disable"] | None = ...,
        spam_submit_txt2htm: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FortishieldPayload | None = ...,
        spam_submit_srv: str | None = ...,
        spam_submit_force: Literal["enable", "disable"] | None = ...,
        spam_submit_txt2htm: Literal["enable", "disable"] | None = ...,
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
        payload_dict: FortishieldPayload | None = ...,
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