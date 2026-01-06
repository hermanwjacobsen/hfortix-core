from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class InternetServiceNamePayload(TypedDict, total=False):
    """
    Type hints for firewall/internet_service_name payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: InternetServiceNamePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Internet Service name.
    type: NotRequired[Literal[{"description": "Automatically generated Internet Service", "help": "Automatically generated Internet Service.", "label": "Default", "name": "default"}, {"description": "Geography location based Internet Service", "help": "Geography location based Internet Service.", "label": "Location", "name": "location"}]]  # Internet Service name type.
    internet_service_id: int  # Internet Service ID.
    country_id: NotRequired[int]  # Country or Area ID.
    region_id: NotRequired[int]  # Region ID.
    city_id: NotRequired[int]  # City ID.


class InternetServiceName:
    """
    Define internet service names.
    
    Path: firewall/internet_service_name
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
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal[{"description": "Automatically generated Internet Service", "help": "Automatically generated Internet Service.", "label": "Default", "name": "default"}, {"description": "Geography location based Internet Service", "help": "Geography location based Internet Service.", "label": "Location", "name": "location"}] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: InternetServiceNamePayload | None = ...,
        name: str | None = ...,
        type: Literal[{"description": "Automatically generated Internet Service", "help": "Automatically generated Internet Service.", "label": "Default", "name": "default"}, {"description": "Geography location based Internet Service", "help": "Geography location based Internet Service.", "label": "Location", "name": "location"}] | None = ...,
        internet_service_id: int | None = ...,
        country_id: int | None = ...,
        region_id: int | None = ...,
        city_id: int | None = ...,
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
        payload_dict: InternetServiceNamePayload | None = ...,
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
    "InternetServiceName",
    "InternetServiceNamePayload",
]