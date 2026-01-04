from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class NgfwSettingsPayload(TypedDict, total=False):
    """
    Type hints for system/ngfw_settings payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: NgfwSettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    match_timeout: NotRequired[int]  # Number of seconds to wait before a security policy match for
    tcp_match_timeout: NotRequired[int]  # Number of seconds to wait before a security policy match for
    tcp_halfopen_match_timeout: NotRequired[int]  # Number of seconds to wait before a security policy match for


class NgfwSettings:
    """
    Configure IPS NGFW policy-mode VDOM settings.
    
    Path: system/ngfw_settings
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
        payload_dict: NgfwSettingsPayload | None = ...,
        match_timeout: int | None = ...,
        tcp_match_timeout: int | None = ...,
        tcp_halfopen_match_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: NgfwSettingsPayload | None = ...,
        match_timeout: int | None = ...,
        tcp_match_timeout: int | None = ...,
        tcp_halfopen_match_timeout: int | None = ...,
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
        payload_dict: NgfwSettingsPayload | None = ...,
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