from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SwitchLogPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/switch_log payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SwitchLogPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal[{"description": "Add FortiSwitch logs to FortiGate event log", "help": "Add FortiSwitch logs to FortiGate event log.", "label": "Enable", "name": "enable"}, {"description": "Do not add  FortiSwitch logs to FortiGate event log", "help": "Do not add  FortiSwitch logs to FortiGate event log.", "label": "Disable", "name": "disable"}]]  # Enable/disable adding FortiSwitch logs to FortiGate event lo
    severity: NotRequired[Literal[{"description": "Emergency level", "help": "Emergency level.", "label": "Emergency", "name": "emergency"}, {"description": "Alert level", "help": "Alert level.", "label": "Alert", "name": "alert"}, {"description": "Critical level", "help": "Critical level.", "label": "Critical", "name": "critical"}, {"description": "Error level", "help": "Error level.", "label": "Error", "name": "error"}, {"description": "Warning level", "help": "Warning level.", "label": "Warning", "name": "warning"}, {"description": "Notification level", "help": "Notification level.", "label": "Notification", "name": "notification"}, {"description": "Information level", "help": "Information level.", "label": "Information", "name": "information"}, {"description": "Debug level", "help": "Debug level.", "label": "Debug", "name": "debug"}]]  # Severity of FortiSwitch logs that are added to the FortiGate


class SwitchLog:
    """
    Configure FortiSwitch logging (logs are transferred to and inserted into FortiGate event log).
    
    Path: switch_controller/switch_log
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
        payload_dict: SwitchLogPayload | None = ...,
        status: Literal[{"description": "Add FortiSwitch logs to FortiGate event log", "help": "Add FortiSwitch logs to FortiGate event log.", "label": "Enable", "name": "enable"}, {"description": "Do not add  FortiSwitch logs to FortiGate event log", "help": "Do not add  FortiSwitch logs to FortiGate event log.", "label": "Disable", "name": "disable"}] | None = ...,
        severity: Literal[{"description": "Emergency level", "help": "Emergency level.", "label": "Emergency", "name": "emergency"}, {"description": "Alert level", "help": "Alert level.", "label": "Alert", "name": "alert"}, {"description": "Critical level", "help": "Critical level.", "label": "Critical", "name": "critical"}, {"description": "Error level", "help": "Error level.", "label": "Error", "name": "error"}, {"description": "Warning level", "help": "Warning level.", "label": "Warning", "name": "warning"}, {"description": "Notification level", "help": "Notification level.", "label": "Notification", "name": "notification"}, {"description": "Information level", "help": "Information level.", "label": "Information", "name": "information"}, {"description": "Debug level", "help": "Debug level.", "label": "Debug", "name": "debug"}] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SwitchLogPayload | None = ...,
        status: Literal[{"description": "Add FortiSwitch logs to FortiGate event log", "help": "Add FortiSwitch logs to FortiGate event log.", "label": "Enable", "name": "enable"}, {"description": "Do not add  FortiSwitch logs to FortiGate event log", "help": "Do not add  FortiSwitch logs to FortiGate event log.", "label": "Disable", "name": "disable"}] | None = ...,
        severity: Literal[{"description": "Emergency level", "help": "Emergency level.", "label": "Emergency", "name": "emergency"}, {"description": "Alert level", "help": "Alert level.", "label": "Alert", "name": "alert"}, {"description": "Critical level", "help": "Critical level.", "label": "Critical", "name": "critical"}, {"description": "Error level", "help": "Error level.", "label": "Error", "name": "error"}, {"description": "Warning level", "help": "Warning level.", "label": "Warning", "name": "warning"}, {"description": "Notification level", "help": "Notification level.", "label": "Notification", "name": "notification"}, {"description": "Information level", "help": "Information level.", "label": "Information", "name": "information"}, {"description": "Debug level", "help": "Debug level.", "label": "Debug", "name": "debug"}] | None = ...,
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
        payload_dict: SwitchLogPayload | None = ...,
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
    "SwitchLog",
    "SwitchLogPayload",
]