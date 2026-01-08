from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class RecurringPayload(TypedDict, total=False):
    """
    Type hints for firewall/schedule/recurring payload fields.
    
    Recurring schedule configuration.
    
    **Usage:**
        payload: RecurringPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Recurring schedule name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    start: str  # Time of day to start the schedule, format hh:mm.
    end: str  # Time of day to end the schedule, format hh:mm.
    day: NotRequired[Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"]]  # One or more days of the week on which the schedule is valid.
    label_day: NotRequired[Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"]]  # Configure a window during the time of day in which the sched
    color: NotRequired[int]  # Color of icon on the GUI.
    fabric_object: NotRequired[Literal["enable", "disable"]]  # Security Fabric global object setting.


class RecurringObject(FortiObject[RecurringPayload]):
    """Typed FortiObject for firewall/schedule/recurring with IDE autocomplete support."""
    
    # Recurring schedule name.
    name: str
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Time of day to start the schedule, format hh:mm.
    start: str
    # Time of day to end the schedule, format hh:mm.
    end: str
    # One or more days of the week on which the schedule is valid. Separate the names 
    day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"]
    # Configure a window during the time of day in which the schedule job is executed.
    label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"]
    # Color of icon on the GUI.
    color: int
    # Security Fabric global object setting.
    fabric_object: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> RecurringPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Recurring:
    """
    Recurring schedule configuration.
    
    Path: firewall/schedule/recurring
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> RecurringObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[RecurringObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> RecurringObject | list[RecurringObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | list[dict[str, Any]] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RecurringObject: ...
    
    @overload
    def post(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | list[dict[str, Any]] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | list[dict[str, Any]] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | list[dict[str, Any]] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | list[dict[str, Any]] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RecurringObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | list[dict[str, Any]] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | list[dict[str, Any]] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | list[dict[str, Any]] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RecurringObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | list[dict[str, Any]] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    "Recurring",
    "RecurringPayload",
    "RecurringObject",
]