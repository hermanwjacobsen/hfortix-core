from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ScheduleRecurringPayload(TypedDict, total=False):
    """
    Type hints for firewall/schedule_recurring payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ScheduleRecurringPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Recurring schedule name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    start: str  # Time of day to start the schedule, format hh:mm.
    end: str  # Time of day to end the schedule, format hh:mm.
    day: NotRequired[Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"]]  # One or more days of the week on which the schedule is valid.
    color: NotRequired[int]  # Color of icon on the GUI.
    fabric_object: NotRequired[Literal["enable", "disable"]]  # Security Fabric global object setting.


class ScheduleRecurring:
    """
    Recurring schedule configuration.
    
    Path: firewall/schedule_recurring
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
        payload_dict: ScheduleRecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ScheduleRecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
        payload_dict: ScheduleRecurringPayload | None = ...,
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