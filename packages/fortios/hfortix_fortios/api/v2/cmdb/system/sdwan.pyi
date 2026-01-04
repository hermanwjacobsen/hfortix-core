from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SdwanPayload(TypedDict, total=False):
    """
    Type hints for system/sdwan payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Sdwan:
    """
    Configure redundant Internet connections with multiple outbound links and health-check profiles.
    
    Path: system/sdwan
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
        fail_alert_interfaces: list[dict[str, Any]] | None = ...,
        zone: list[dict[str, Any]] | None = ...,
        members: list[dict[str, Any]] | None = ...,
        health_check: list[dict[str, Any]] | None = ...,
        service: list[dict[str, Any]] | None = ...,
        neighbor: list[dict[str, Any]] | None = ...,
        duplication: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        fail_alert_interfaces: list[dict[str, Any]] | None = ...,
        zone: list[dict[str, Any]] | None = ...,
        members: list[dict[str, Any]] | None = ...,
        health_check: list[dict[str, Any]] | None = ...,
        service: list[dict[str, Any]] | None = ...,
        neighbor: list[dict[str, Any]] | None = ...,
        duplication: list[dict[str, Any]] | None = ...,
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
        payload_dict: SdwanPayload | None = ...,
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