from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class LogPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/log payload fields.
    
    Configure wireless controller event log filters.
    
    **Usage:**
        payload: LogPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable wireless event logging.
    addrgrp_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log address group message.
    ble_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log BLE detection message.
    clb_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log client load balancing message.
    dhcp_starv_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log DHCP starvation event message.
    led_sched_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log LED schedule event message.
    radio_event_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log radio event message.
    rogue_event_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log rogue AP event message.
    sta_event_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log station event message.
    sta_locate_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log station locate message.
    wids_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log WIDS message.
    wtp_event_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log WTP event message.
    wtp_fips_event_log: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log FAP fips event message.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class LogResponse(TypedDict):
    """
    Type hints for wireless_controller/log API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]
    addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]


@final
class LogObject:
    """Typed FortiObject for wireless_controller/log with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable wireless event logging.
    status: Literal["enable", "disable"]
    # Lowest severity level to log address group message.
    addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log BLE detection message.
    ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log client load balancing message.
    clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log DHCP starvation event message.
    dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log LED schedule event message.
    led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log radio event message.
    radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log rogue AP event message.
    rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log station event message.
    sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log station locate message.
    sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log WIDS message.
    wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log WTP event message.
    wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log FAP fips event message.
    wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LogPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Log:
    """
    Configure wireless controller event log filters.
    
    Path: wireless_controller/log
    Category: cmdb
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LogObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LogObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LogObject: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> LogResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> LogResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> LogResponse: ...
    
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
    ) -> LogObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LogPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LogObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LogPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: LogPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: LogPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
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
        payload_dict: LogPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
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
    "Log",
    "LogPayload",
    "LogObject",
]