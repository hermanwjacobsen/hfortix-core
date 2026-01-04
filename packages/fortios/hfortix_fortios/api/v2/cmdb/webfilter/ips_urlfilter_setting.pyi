from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IpsUrlfilterSettingPayload(TypedDict, total=False):
    """
    Type hints for webfilter/ips_urlfilter_setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IpsUrlfilterSettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    device: NotRequired[str]  # Interface for this route.
    distance: NotRequired[int]  # Administrative distance (1 - 255) for this route.
    gateway: NotRequired[str]  # Gateway IP address for this route.
    geo_filter: NotRequired[str]  # Filter based on geographical location. Route will NOT be ins


class IpsUrlfilterSetting:
    """
    Configure IPS URL filter settings.
    
    Path: webfilter/ips_urlfilter_setting
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
        payload_dict: IpsUrlfilterSettingPayload | None = ...,
        device: str | None = ...,
        distance: int | None = ...,
        gateway: str | None = ...,
        geo_filter: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IpsUrlfilterSettingPayload | None = ...,
        device: str | None = ...,
        distance: int | None = ...,
        gateway: str | None = ...,
        geo_filter: str | None = ...,
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
        payload_dict: IpsUrlfilterSettingPayload | None = ...,
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