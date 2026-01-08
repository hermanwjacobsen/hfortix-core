from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SdwanPayload(TypedDict, total=False):
    """
    Type hints for system/sdwan payload fields.
    
    Configure redundant Internet connections with multiple outbound links and health-check profiles.
    
    **Usage:**
        payload: SdwanPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable SD-WAN.
    load_balance_mode: NotRequired[Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"]]  # Algorithm or mode to use for load balancing Internet traffic
    speedtest_bypass_routing: NotRequired[Literal["disable", "enable"]]  # Enable/disable bypass routing when speedtest on a SD-WAN mem
    duplication_max_num: NotRequired[int]  # Maximum number of interface members a packet is duplicated i
    duplication_max_discrepancy: NotRequired[int]  # Maximum discrepancy between two packets for deduplication in
    neighbor_hold_down: NotRequired[Literal["enable", "disable"]]  # Enable/disable hold switching from the secondary neighbor to
    neighbor_hold_down_time: NotRequired[int]  # Waiting period in seconds when switching from the secondary 
    app_perf_log_period: NotRequired[int]  # Time interval in seconds that application performance logs a
    neighbor_hold_boot_time: NotRequired[int]  # Waiting period in seconds when switching from the primary ne
    fail_detect: NotRequired[Literal["enable", "disable"]]  # Enable/disable SD-WAN Internet connection status checking (f
    fail_alert_interfaces: NotRequired[list[dict[str, Any]]]  # Physical interfaces that will be alerted.
    zone: NotRequired[list[dict[str, Any]]]  # Configure SD-WAN zones.
    members: NotRequired[list[dict[str, Any]]]  # FortiGate interfaces added to the SD-WAN.
    health_check: NotRequired[list[dict[str, Any]]]  # SD-WAN status checking or health checking. Identify a server
    service: NotRequired[list[dict[str, Any]]]  # Create SD-WAN rules (also called services) to control how se
    neighbor: NotRequired[list[dict[str, Any]]]  # Create SD-WAN neighbor from BGP neighbor table to control ro
    duplication: NotRequired[list[dict[str, Any]]]  # Create SD-WAN duplication rule.


class SdwanObject(FortiObject[SdwanPayload]):
    """Typed FortiObject for system/sdwan with IDE autocomplete support."""
    
    # Enable/disable SD-WAN.
    status: Literal["disable", "enable"]
    # Algorithm or mode to use for load balancing Internet traffic to SD-WAN members.
    load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"]
    # Enable/disable bypass routing when speedtest on a SD-WAN member.
    speedtest_bypass_routing: Literal["disable", "enable"]
    # Maximum number of interface members a packet is duplicated in the SD-WAN zone (2
    duplication_max_num: int
    # Maximum discrepancy between two packets for deduplication in milliseconds (250 -
    duplication_max_discrepancy: int
    # Enable/disable hold switching from the secondary neighbor to the primary neighbo
    neighbor_hold_down: Literal["enable", "disable"]
    # Waiting period in seconds when switching from the secondary neighbor to the prim
    neighbor_hold_down_time: int
    # Time interval in seconds that application performance logs are generated (0 - 36
    app_perf_log_period: int
    # Waiting period in seconds when switching from the primary neighbor to the second
    neighbor_hold_boot_time: int
    # Enable/disable SD-WAN Internet connection status checking (failure detection).
    fail_detect: Literal["enable", "disable"]
    # Physical interfaces that will be alerted.
    fail_alert_interfaces: list[str]  # Auto-flattened from member_table
    # Configure SD-WAN zones.
    zone: list[str]  # Auto-flattened from member_table
    # FortiGate interfaces added to the SD-WAN.
    members: list[str]  # Auto-flattened from member_table
    # SD-WAN status checking or health checking. Identify a server on the Internet and
    health_check: list[str]  # Auto-flattened from member_table
    # Create SD-WAN rules (also called services) to control how sessions are distribut
    service: list[str]  # Auto-flattened from member_table
    # Create SD-WAN neighbor from BGP neighbor table to control route advertisements a
    neighbor: list[str]  # Auto-flattened from member_table
    # Create SD-WAN duplication rule.
    duplication: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SdwanPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Sdwan:
    """
    Configure redundant Internet connections with multiple outbound links and health-check profiles.
    
    Path: system/sdwan
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SdwanObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Sdwan",
    "SdwanPayload",
    "SdwanObject",
]