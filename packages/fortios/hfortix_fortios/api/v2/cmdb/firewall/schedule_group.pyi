from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ScheduleGroupPayload(TypedDict, total=False):
    """
    Type hints for firewall/schedule_group payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ScheduleGroupPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Schedule group name.
    member: list[dict[str, Any]]  # Schedules added to the schedule group.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    color: NotRequired[int]  # Color of icon on the GUI.
    fabric_object: NotRequired[Literal["enable", "disable"]]  # Security Fabric global object setting.


class ScheduleGroup:
    """
    Schedule group configuration.
    
    Path: firewall/schedule_group
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
        payload_dict: ScheduleGroupPayload | None = ...,
        name: str | None = ...,
        member: list[dict[str, Any]] | None = ...,
        uuid: str | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ScheduleGroupPayload | None = ...,
        name: str | None = ...,
        member: list[dict[str, Any]] | None = ...,
        uuid: str | None = ...,
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
        payload_dict: ScheduleGroupPayload | None = ...,
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