from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ScheduleOnetimePayload(TypedDict, total=False):
    """
    Type hints for firewall/schedule_onetime payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ScheduleOnetimePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Onetime schedule name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    start: str  # Schedule start date and time, format hh:mm yyyy/mm/dd.
    start_utc: NotRequired[str]  # Schedule start date and time, in epoch format.
    end: str  # Schedule end date and time, format hh:mm yyyy/mm/dd.
    end_utc: NotRequired[str]  # Schedule end date and time, in epoch format.
    color: NotRequired[int]  # Color of icon on the GUI.
    expiration_days: NotRequired[int]  # Write an event log message this many days before the schedul
    fabric_object: NotRequired[Literal["enable", "disable"]]  # Security Fabric global object setting.


class ScheduleOnetime:
    """
    Onetime schedule configuration.
    
    Path: firewall/schedule_onetime
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
        payload_dict: ScheduleOnetimePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        start_utc: str | None = ...,
        end: str | None = ...,
        end_utc: str | None = ...,
        color: int | None = ...,
        expiration_days: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ScheduleOnetimePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        start_utc: str | None = ...,
        end: str | None = ...,
        end_utc: str | None = ...,
        color: int | None = ...,
        expiration_days: int | None = ...,
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
        payload_dict: ScheduleOnetimePayload | None = ...,
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