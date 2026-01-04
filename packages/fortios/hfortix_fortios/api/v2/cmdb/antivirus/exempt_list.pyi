from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ExemptListPayload(TypedDict, total=False):
    """
    Type hints for antivirus/exempt_list payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ExemptListPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Table entry name.
    comment: NotRequired[str]  # Comment.
    hash_type: NotRequired[Literal["md5", "sha1", "sha256"]]  # Hash type.
    hash: str  # Hash value to be matched.
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable table entry.


class ExemptList:
    """
    Configure a list of hashes to be exempt from AV scanning.
    
    Path: antivirus/exempt_list
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
        payload_dict: ExemptListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        hash_type: Literal["md5", "sha1", "sha256"] | None = ...,
        hash: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ExemptListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        hash_type: Literal["md5", "sha1", "sha256"] | None = ...,
        hash: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
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
        payload_dict: ExemptListPayload | None = ...,
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