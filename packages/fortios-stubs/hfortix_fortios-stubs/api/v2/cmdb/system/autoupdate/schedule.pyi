from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SchedulePayload(TypedDict, total=False):
    """
    Type hints for system/autoupdate/schedule payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SchedulePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}]  # Enable/disable scheduled updates.
    frequency: Literal[{"description": "Time interval", "help": "Time interval.", "label": "Every", "name": "every"}, {"description": "Every day", "help": "Every day.", "label": "Daily", "name": "daily"}, {"description": "Every week", "help": "Every week.", "label": "Weekly", "name": "weekly"}, {"description": "Update automatically within every one hour period", "help": "Update automatically within every one hour period.", "label": "Automatic", "name": "automatic"}]  # Update frequency.
    time: str  # Update time.
    day: Literal[{"description": "Update every Sunday", "help": "Update every Sunday.", "label": "Sunday", "name": "Sunday"}, {"description": "Update every Monday", "help": "Update every Monday.", "label": "Monday", "name": "Monday"}, {"description": "Update every Tuesday", "help": "Update every Tuesday.", "label": "Tuesday", "name": "Tuesday"}, {"description": "Update every Wednesday", "help": "Update every Wednesday.", "label": "Wednesday", "name": "Wednesday"}, {"description": "Update every Thursday", "help": "Update every Thursday.", "label": "Thursday", "name": "Thursday"}, {"description": "Update every Friday", "help": "Update every Friday.", "label": "Friday", "name": "Friday"}, {"description": "Update every Saturday", "help": "Update every Saturday.", "label": "Saturday", "name": "Saturday"}]  # Update day.


class Schedule:
    """
    Configure update schedule.
    
    Path: system/autoupdate/schedule
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
        payload_dict: SchedulePayload | None = ...,
        status: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}] | None = ...,
        frequency: Literal[{"description": "Time interval", "help": "Time interval.", "label": "Every", "name": "every"}, {"description": "Every day", "help": "Every day.", "label": "Daily", "name": "daily"}, {"description": "Every week", "help": "Every week.", "label": "Weekly", "name": "weekly"}, {"description": "Update automatically within every one hour period", "help": "Update automatically within every one hour period.", "label": "Automatic", "name": "automatic"}] | None = ...,
        time: str | None = ...,
        day: Literal[{"description": "Update every Sunday", "help": "Update every Sunday.", "label": "Sunday", "name": "Sunday"}, {"description": "Update every Monday", "help": "Update every Monday.", "label": "Monday", "name": "Monday"}, {"description": "Update every Tuesday", "help": "Update every Tuesday.", "label": "Tuesday", "name": "Tuesday"}, {"description": "Update every Wednesday", "help": "Update every Wednesday.", "label": "Wednesday", "name": "Wednesday"}, {"description": "Update every Thursday", "help": "Update every Thursday.", "label": "Thursday", "name": "Thursday"}, {"description": "Update every Friday", "help": "Update every Friday.", "label": "Friday", "name": "Friday"}, {"description": "Update every Saturday", "help": "Update every Saturday.", "label": "Saturday", "name": "Saturday"}] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SchedulePayload | None = ...,
        status: Literal[{"description": "Enable setting", "help": "Enable setting.", "label": "Enable", "name": "enable"}, {"description": "Disable setting", "help": "Disable setting.", "label": "Disable", "name": "disable"}] | None = ...,
        frequency: Literal[{"description": "Time interval", "help": "Time interval.", "label": "Every", "name": "every"}, {"description": "Every day", "help": "Every day.", "label": "Daily", "name": "daily"}, {"description": "Every week", "help": "Every week.", "label": "Weekly", "name": "weekly"}, {"description": "Update automatically within every one hour period", "help": "Update automatically within every one hour period.", "label": "Automatic", "name": "automatic"}] | None = ...,
        time: str | None = ...,
        day: Literal[{"description": "Update every Sunday", "help": "Update every Sunday.", "label": "Sunday", "name": "Sunday"}, {"description": "Update every Monday", "help": "Update every Monday.", "label": "Monday", "name": "Monday"}, {"description": "Update every Tuesday", "help": "Update every Tuesday.", "label": "Tuesday", "name": "Tuesday"}, {"description": "Update every Wednesday", "help": "Update every Wednesday.", "label": "Wednesday", "name": "Wednesday"}, {"description": "Update every Thursday", "help": "Update every Thursday.", "label": "Thursday", "name": "Thursday"}, {"description": "Update every Friday", "help": "Update every Friday.", "label": "Friday", "name": "Friday"}, {"description": "Update every Saturday", "help": "Update every Saturday.", "label": "Saturday", "name": "Saturday"}] | None = ...,
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
        payload_dict: SchedulePayload | None = ...,
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
    "Schedule",
    "SchedulePayload",
]