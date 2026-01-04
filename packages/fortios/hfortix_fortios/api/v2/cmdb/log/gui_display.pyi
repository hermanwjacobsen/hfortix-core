from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class GuiDisplayPayload(TypedDict, total=False):
    """
    Type hints for log/gui_display payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: GuiDisplayPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    resolve_hosts: NotRequired[Literal["enable", "disable"]]  # Enable/disable resolving IP addresses to hostname in log mes
    resolve_apps: NotRequired[Literal["enable", "disable"]]  # Resolve unknown applications on the GUI using Fortinet's rem
    fortiview_unscanned_apps: NotRequired[Literal["enable", "disable"]]  # Enable/disable showing unscanned traffic in FortiView applic


class GuiDisplay:
    """
    Configure how log messages are displayed on the GUI.
    
    Path: log/gui_display
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
        payload_dict: GuiDisplayPayload | None = ...,
        resolve_hosts: Literal["enable", "disable"] | None = ...,
        resolve_apps: Literal["enable", "disable"] | None = ...,
        fortiview_unscanned_apps: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: GuiDisplayPayload | None = ...,
        resolve_hosts: Literal["enable", "disable"] | None = ...,
        resolve_apps: Literal["enable", "disable"] | None = ...,
        fortiview_unscanned_apps: Literal["enable", "disable"] | None = ...,
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
        payload_dict: GuiDisplayPayload | None = ...,
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