from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class NetworkVisibilityPayload(TypedDict, total=False):
    """
    Type hints for system/network_visibility payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: NetworkVisibilityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    destination_visibility: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging of destination visibility.
    source_location: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging of source geographical location visib
    destination_hostname_visibility: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging of destination hostname visibility.
    destination_location: NotRequired[Literal["disable", "enable"]]  # Enable/disable logging of destination geographical location 


class NetworkVisibility:
    """
    Configure network visibility settings.
    
    Path: system/network_visibility
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
        payload_dict: NetworkVisibilityPayload | None = ...,
        destination_visibility: Literal["disable", "enable"] | None = ...,
        source_location: Literal["disable", "enable"] | None = ...,
        destination_hostname_visibility: Literal["disable", "enable"] | None = ...,
        destination_location: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: NetworkVisibilityPayload | None = ...,
        destination_visibility: Literal["disable", "enable"] | None = ...,
        source_location: Literal["disable", "enable"] | None = ...,
        destination_hostname_visibility: Literal["disable", "enable"] | None = ...,
        destination_location: Literal["disable", "enable"] | None = ...,
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
        payload_dict: NetworkVisibilityPayload | None = ...,
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