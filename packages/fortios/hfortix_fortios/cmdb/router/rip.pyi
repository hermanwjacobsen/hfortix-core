from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class RipPayload(TypedDict, total=False):
    """
    Type hints for router/rip payload fields.
    
    Configure RIP.
    
    **Usage:**
        payload: RipPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    default_information_originate: NotRequired[Literal["enable", "disable"]]  # Enable/disable generation of default route.
    default_metric: NotRequired[int]  # Default metric.
    max_out_metric: NotRequired[int]  # Maximum metric allowed to output(0 means 'not set').
    distance: NotRequired[list[dict[str, Any]]]  # Distance.
    distribute_list: NotRequired[list[dict[str, Any]]]  # Distribute list.
    neighbor: NotRequired[list[dict[str, Any]]]  # Neighbor.
    network: NotRequired[list[dict[str, Any]]]  # Network.
    offset_list: NotRequired[list[dict[str, Any]]]  # Offset list.
    passive_interface: NotRequired[list[dict[str, Any]]]  # Passive interface configuration.
    redistribute: NotRequired[list[dict[str, Any]]]  # Redistribute configuration.
    update_timer: NotRequired[int]  # Update timer in seconds.
    timeout_timer: NotRequired[int]  # Timeout timer in seconds.
    garbage_timer: NotRequired[int]  # Garbage timer in seconds.
    version: NotRequired[Literal["1", "2"]]  # RIP version.
    interface: NotRequired[list[dict[str, Any]]]  # RIP interface configuration.


class RipObject(FortiObject[RipPayload]):
    """Typed FortiObject for router/rip with IDE autocomplete support."""
    
    # Enable/disable generation of default route.
    default_information_originate: Literal["enable", "disable"]
    # Default metric.
    default_metric: int
    # Maximum metric allowed to output(0 means 'not set').
    max_out_metric: int
    # Distance.
    distance: list[str]  # Auto-flattened from member_table
    # Distribute list.
    distribute_list: list[str]  # Auto-flattened from member_table
    # Neighbor.
    neighbor: list[str]  # Auto-flattened from member_table
    # Network.
    network: list[str]  # Auto-flattened from member_table
    # Offset list.
    offset_list: list[str]  # Auto-flattened from member_table
    # Passive interface configuration.
    passive_interface: list[str]  # Auto-flattened from member_table
    # Redistribute configuration.
    redistribute: list[str]  # Auto-flattened from member_table
    # Update timer in seconds.
    update_timer: int
    # Timeout timer in seconds.
    timeout_timer: int
    # Garbage timer in seconds.
    garbage_timer: int
    # RIP version.
    version: Literal["1", "2"]
    # RIP interface configuration.
    interface: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> RipPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Rip:
    """
    Configure RIP.
    
    Path: router/rip
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
    ) -> RipObject: ...
    
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
    ) -> RipObject: ...
    
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
    ) -> RipObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RipObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Rip",
    "RipPayload",
    "RipObject",
]