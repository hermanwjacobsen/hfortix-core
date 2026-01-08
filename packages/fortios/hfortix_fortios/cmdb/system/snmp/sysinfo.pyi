from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SysinfoPayload(TypedDict, total=False):
    """
    Type hints for system/snmp/sysinfo payload fields.
    
    SNMP system info configuration.
    
    **Usage:**
        payload: SysinfoPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable SNMP.
    engine_id_type: NotRequired[Literal["text", "hex", "mac"]]  # Local SNMP engineID type (text/hex/mac).
    engine_id: NotRequired[str]  # Local SNMP engineID string (maximum 27 characters).
    description: NotRequired[str]  # System description.
    contact_info: NotRequired[str]  # Contact information.
    location: NotRequired[str]  # System location.
    trap_high_cpu_threshold: NotRequired[int]  # CPU usage when trap is sent.
    trap_low_memory_threshold: NotRequired[int]  # Memory usage when trap is sent.
    trap_log_full_threshold: NotRequired[int]  # Log disk usage when trap is sent.
    trap_free_memory_threshold: NotRequired[int]  # Free memory usage when trap is sent.
    trap_freeable_memory_threshold: NotRequired[int]  # Freeable memory usage when trap is sent.
    append_index: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowance of appending vdom or interface inde
    non_mgmt_vdom_query: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowance of SNMPv3 query from non-management


class SysinfoObject(FortiObject[SysinfoPayload]):
    """Typed FortiObject for system/snmp/sysinfo with IDE autocomplete support."""
    
    # Enable/disable SNMP.
    status: Literal["enable", "disable"]
    # Local SNMP engineID type (text/hex/mac).
    engine_id_type: Literal["text", "hex", "mac"]
    # Local SNMP engineID string (maximum 27 characters).
    engine_id: str
    # System description.
    description: str
    # Contact information.
    contact_info: str
    # System location.
    location: str
    # CPU usage when trap is sent.
    trap_high_cpu_threshold: int
    # Memory usage when trap is sent.
    trap_low_memory_threshold: int
    # Log disk usage when trap is sent.
    trap_log_full_threshold: int
    # Free memory usage when trap is sent.
    trap_free_memory_threshold: int
    # Freeable memory usage when trap is sent.
    trap_freeable_memory_threshold: int
    # Enable/disable allowance of appending vdom or interface index in some RFC tables
    append_index: Literal["enable", "disable"]
    # Enable/disable allowance of SNMPv3 query from non-management vdoms.
    non_mgmt_vdom_query: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SysinfoPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Sysinfo:
    """
    SNMP system info configuration.
    
    Path: system/snmp/sysinfo
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
    ) -> SysinfoObject: ...
    
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
    ) -> SysinfoObject: ...
    
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
    ) -> SysinfoObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SysinfoObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
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
        payload_dict: SysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
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
    "Sysinfo",
    "SysinfoPayload",
    "SysinfoObject",
]