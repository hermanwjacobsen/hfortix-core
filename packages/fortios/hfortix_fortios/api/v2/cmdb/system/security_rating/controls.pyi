from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ControlsPayload(TypedDict, total=False):
    """
    Type hints for system/security_rating/controls payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ControlsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Security Rating control name.
    display_report: Literal[{"description": "Enable displaying the Security Rating control in the default report", "help": "Enable displaying the Security Rating control in the default report.", "label": "Enable", "name": "enable"}, {"description": "Disable displaying the Security Rating control in the default report", "help": "Disable displaying the Security Rating control in the default report.", "label": "Disable", "name": "disable"}]  # Enable/disable displaying the Security Rating control in the
    display_insight: Literal[{"description": "Enable displaying the Security Rating control as an insight across the GUI", "help": "Enable displaying the Security Rating control as an insight across the GUI.", "label": "Enable", "name": "enable"}, {"description": "Disable displaying the Security Rating control as an insight across the GUI", "help": "Disable displaying the Security Rating control as an insight across the GUI.", "label": "Disable", "name": "disable"}]  # Enable/disable displaying the Security Rating control as an 


class Controls:
    """
    Settings for individual Security Rating controls.
    
    Path: system/security_rating/controls
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
        payload_dict: ControlsPayload | None = ...,
        name: str | None = ...,
        display_report: Literal[{"description": "Enable displaying the Security Rating control in the default report", "help": "Enable displaying the Security Rating control in the default report.", "label": "Enable", "name": "enable"}, {"description": "Disable displaying the Security Rating control in the default report", "help": "Disable displaying the Security Rating control in the default report.", "label": "Disable", "name": "disable"}] | None = ...,
        display_insight: Literal[{"description": "Enable displaying the Security Rating control as an insight across the GUI", "help": "Enable displaying the Security Rating control as an insight across the GUI.", "label": "Enable", "name": "enable"}, {"description": "Disable displaying the Security Rating control as an insight across the GUI", "help": "Disable displaying the Security Rating control as an insight across the GUI.", "label": "Disable", "name": "disable"}] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ControlsPayload | None = ...,
        name: str | None = ...,
        display_report: Literal[{"description": "Enable displaying the Security Rating control in the default report", "help": "Enable displaying the Security Rating control in the default report.", "label": "Enable", "name": "enable"}, {"description": "Disable displaying the Security Rating control in the default report", "help": "Disable displaying the Security Rating control in the default report.", "label": "Disable", "name": "disable"}] | None = ...,
        display_insight: Literal[{"description": "Enable displaying the Security Rating control as an insight across the GUI", "help": "Enable displaying the Security Rating control as an insight across the GUI.", "label": "Enable", "name": "enable"}, {"description": "Disable displaying the Security Rating control as an insight across the GUI", "help": "Disable displaying the Security Rating control as an insight across the GUI.", "label": "Disable", "name": "disable"}] | None = ...,
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
        payload_dict: ControlsPayload | None = ...,
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
    "Controls",
    "ControlsPayload",
]