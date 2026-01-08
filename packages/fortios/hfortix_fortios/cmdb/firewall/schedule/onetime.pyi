from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class OnetimePayload(TypedDict, total=False):
    """
    Type hints for firewall/schedule/onetime payload fields.
    
    Onetime schedule configuration.
    
    **Usage:**
        payload: OnetimePayload = {
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


class OnetimeObject(FortiObject[OnetimePayload]):
    """Typed FortiObject for firewall/schedule/onetime with IDE autocomplete support."""
    
    # Onetime schedule name.
    name: str
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Schedule start date and time, format hh:mm yyyy/mm/dd.
    start: str
    # Schedule start date and time, in epoch format.
    start_utc: str
    # Schedule end date and time, format hh:mm yyyy/mm/dd.
    end: str
    # Schedule end date and time, in epoch format.
    end_utc: str
    # Color of icon on the GUI.
    color: int
    # Write an event log message this many days before the schedule expires.
    expiration_days: int
    # Security Fabric global object setting.
    fabric_object: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> OnetimePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Onetime:
    """
    Onetime schedule configuration.
    
    Path: firewall/schedule/onetime
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
    ) -> OnetimeObject: ...
    
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
    ) -> list[OnetimeObject]: ...
    
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
    ) -> OnetimeObject | list[OnetimeObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: OnetimePayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> OnetimeObject: ...
    
    @overload
    def post(
        self,
        payload_dict: OnetimePayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: OnetimePayload | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: OnetimePayload | None = ...,
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: OnetimePayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> OnetimeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: OnetimePayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: OnetimePayload | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: OnetimePayload | None = ...,
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
    ) -> OnetimeObject: ...
    
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
        payload_dict: OnetimePayload | None = ...,
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
    "Onetime",
    "OnetimePayload",
    "OnetimeObject",
]