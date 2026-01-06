from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class OtdtPayload(TypedDict, total=False):
    """
    Type hints for rule/otdt payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: OtdtPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Application name.
    id: NotRequired[int]  # Application ID.
    category: int  # Application category ID.
    popularity: NotRequired[int]  # Application popularity.
    risk: NotRequired[int]  # Application risk.
    weight: NotRequired[int]  # Application weight.
    protocol: NotRequired[str]  # Application protocol.
    technology: NotRequired[str]  # Application technology.
    behavior: NotRequired[str]  # Application behavior.
    vendor: NotRequired[str]  # Application vendor.
    parameters: NotRequired[list[dict[str, Any]]]  # Application parameters.
    metadata: NotRequired[list[dict[str, Any]]]  # Meta data.
    status: NotRequired[str]  # Print all OT detection rules information.


class Otdt:
    """
    Show OT detection signatures.
    
    Path: rule/otdt
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
        payload_dict: OtdtPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: list[dict[str, Any]] | None = ...,
        metadata: list[dict[str, Any]] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: OtdtPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        category: int | None = ...,
        popularity: int | None = ...,
        risk: int | None = ...,
        weight: int | None = ...,
        protocol: str | None = ...,
        technology: str | None = ...,
        behavior: str | None = ...,
        vendor: str | None = ...,
        parameters: list[dict[str, Any]] | None = ...,
        metadata: list[dict[str, Any]] | None = ...,
        status: str | None = ...,
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
        payload_dict: OtdtPayload | None = ...,
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
    "Otdt",
    "OtdtPayload",
]