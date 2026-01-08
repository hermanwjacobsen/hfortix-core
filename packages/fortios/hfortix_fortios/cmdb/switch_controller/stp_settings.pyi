from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class StpSettingsPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/stp_settings payload fields.
    
    Configure FortiSwitch spanning tree protocol (STP).
    
    **Usage:**
        payload: StpSettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Name of global STP settings configuration.
    revision: NotRequired[int]  # STP revision number (0 - 65535).
    hello_time: NotRequired[int]  # Period of time between successive STP frame Bridge Protocol 
    forward_time: NotRequired[int]  # Period of time a port is in listening and learning state (4 
    max_age: NotRequired[int]  # Maximum time before a bridge port expires its configuration 
    max_hops: NotRequired[int]  # Maximum number of hops between the root bridge and the furth
    pending_timer: NotRequired[int]  # Pending time (1 - 15 sec, default = 4).


class StpSettingsObject(FortiObject[StpSettingsPayload]):
    """Typed FortiObject for switch_controller/stp_settings with IDE autocomplete support."""
    
    # Name of global STP settings configuration.
    name: str
    # STP revision number (0 - 65535).
    revision: int
    # Period of time between successive STP frame Bridge Protocol Data Units (BPDUs) s
    hello_time: int
    # Period of time a port is in listening and learning state (4 - 30 sec, default = 
    forward_time: int
    # Maximum time before a bridge port expires its configuration BPDU information (6 
    max_age: int
    # Maximum number of hops between the root bridge and the furthest bridge (1- 40, d
    max_hops: int
    # Pending time (1 - 15 sec, default = 4).
    pending_timer: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> StpSettingsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class StpSettings:
    """
    Configure FortiSwitch spanning tree protocol (STP).
    
    Path: switch_controller/stp_settings
    Category: cmdb
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
    ) -> StpSettingsObject: ...
    
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
    ) -> StpSettingsObject: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> StpSettingsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: StpSettingsPayload | None = ...,
        name: str | None = ...,
        revision: int | None = ...,
        hello_time: int | None = ...,
        forward_time: int | None = ...,
        max_age: int | None = ...,
        max_hops: int | None = ...,
        pending_timer: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> StpSettingsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: StpSettingsPayload | None = ...,
        name: str | None = ...,
        revision: int | None = ...,
        hello_time: int | None = ...,
        forward_time: int | None = ...,
        max_age: int | None = ...,
        max_hops: int | None = ...,
        pending_timer: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: StpSettingsPayload | None = ...,
        name: str | None = ...,
        revision: int | None = ...,
        hello_time: int | None = ...,
        forward_time: int | None = ...,
        max_age: int | None = ...,
        max_hops: int | None = ...,
        pending_timer: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: StpSettingsPayload | None = ...,
        name: str | None = ...,
        revision: int | None = ...,
        hello_time: int | None = ...,
        forward_time: int | None = ...,
        max_age: int | None = ...,
        max_hops: int | None = ...,
        pending_timer: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: StpSettingsPayload | None = ...,
        name: str | None = ...,
        revision: int | None = ...,
        hello_time: int | None = ...,
        forward_time: int | None = ...,
        max_age: int | None = ...,
        max_hops: int | None = ...,
        pending_timer: int | None = ...,
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
    "StpSettings",
    "StpSettingsPayload",
    "StpSettingsObject",
]