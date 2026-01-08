from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class TimersPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/timers payload fields.
    
    Configure CAPWAP timers.
    
    **Usage:**
        payload: TimersPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    echo_interval: NotRequired[int]  # Time between echo requests sent by the managed WTP, AP, or F
    nat_session_keep_alive: NotRequired[int]  # Maximal time in seconds between control requests sent by the
    discovery_interval: NotRequired[int]  # Time between discovery requests (2 - 180 sec, default = 5).
    client_idle_timeout: NotRequired[int]  # Time after which a client is considered idle and times out
    client_idle_rehome_timeout: NotRequired[int]  # Time after which a client is considered idle and disconnecte
    auth_timeout: NotRequired[int]  # Time after which a client is considered failed in RADIUS aut
    rogue_ap_log: NotRequired[int]  # Time between logging rogue AP messages if periodic rogue AP
    fake_ap_log: NotRequired[int]  # Time between recording logs about fake APs if periodic fake
    sta_offline_cleanup: NotRequired[int]  # Time period in seconds to keep station offline data after it
    sta_offline_ip2mac_cleanup: NotRequired[int]  # Time period in seconds to keep station offline Ip2mac data a
    sta_cap_cleanup: NotRequired[int]  # Time period in minutes to keep station capability data after
    rogue_ap_cleanup: NotRequired[int]  # Time period in minutes to keep rogue AP after it is gone
    rogue_sta_cleanup: NotRequired[int]  # Time period in minutes to keep rogue station after it is gon
    wids_entry_cleanup: NotRequired[int]  # Time period in minutes to keep wids entry after it is gone
    ble_device_cleanup: NotRequired[int]  # Time period in minutes to keep BLE device after it is gone
    sta_stats_interval: NotRequired[int]  # Time between running client (station) reports
    vap_stats_interval: NotRequired[int]  # Time between running Virtual Access Point (VAP) reports
    radio_stats_interval: NotRequired[int]  # Time between running radio reports
    sta_capability_interval: NotRequired[int]  # Time between running station capability reports
    sta_locate_timer: NotRequired[int]  # Time between running client presence flushes to remove clien
    ipsec_intf_cleanup: NotRequired[int]  # Time period to keep IPsec VPN interfaces up after WTP sessio
    ble_scan_report_intv: NotRequired[int]  # Time between running Bluetooth Low Energy (BLE) reports
    drma_interval: NotRequired[int]  # Dynamic radio mode assignment (DRMA) schedule interval in mi
    ap_reboot_wait_interval1: NotRequired[int]  # Time in minutes to wait before AP reboots when there is no c
    ap_reboot_wait_time: NotRequired[str]  # Time to reboot the AP when there is no controller detected a
    ap_reboot_wait_interval2: NotRequired[int]  # Time in minutes to wait before AP reboots when there is no c

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class TimersResponse(TypedDict):
    """
    Type hints for wireless_controller/timers API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    echo_interval: int
    nat_session_keep_alive: int
    discovery_interval: int
    client_idle_timeout: int
    client_idle_rehome_timeout: int
    auth_timeout: int
    rogue_ap_log: int
    fake_ap_log: int
    sta_offline_cleanup: int
    sta_offline_ip2mac_cleanup: int
    sta_cap_cleanup: int
    rogue_ap_cleanup: int
    rogue_sta_cleanup: int
    wids_entry_cleanup: int
    ble_device_cleanup: int
    sta_stats_interval: int
    vap_stats_interval: int
    radio_stats_interval: int
    sta_capability_interval: int
    sta_locate_timer: int
    ipsec_intf_cleanup: int
    ble_scan_report_intv: int
    drma_interval: int
    ap_reboot_wait_interval1: int
    ap_reboot_wait_time: str
    ap_reboot_wait_interval2: int


@final
class TimersObject:
    """Typed FortiObject for wireless_controller/timers with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Time between echo requests sent by the managed WTP, AP, or FortiAP
    echo_interval: int
    # Maximal time in seconds between control requests sent by the managed WTP, AP, or
    nat_session_keep_alive: int
    # Time between discovery requests (2 - 180 sec, default = 5).
    discovery_interval: int
    # Time after which a client is considered idle and times out
    client_idle_timeout: int
    # Time after which a client is considered idle and disconnected from the home cont
    client_idle_rehome_timeout: int
    # Time after which a client is considered failed in RADIUS authentication and time
    auth_timeout: int
    # Time between logging rogue AP messages if periodic rogue AP logging is configure
    rogue_ap_log: int
    # Time between recording logs about fake APs if periodic fake AP logging is config
    fake_ap_log: int
    # Time period in seconds to keep station offline data after it is gone
    sta_offline_cleanup: int
    # Time period in seconds to keep station offline Ip2mac data after it is gone
    sta_offline_ip2mac_cleanup: int
    # Time period in minutes to keep station capability data after it is gone
    sta_cap_cleanup: int
    # Time period in minutes to keep rogue AP after it is gone (default = 0).
    rogue_ap_cleanup: int
    # Time period in minutes to keep rogue station after it is gone (default = 0).
    rogue_sta_cleanup: int
    # Time period in minutes to keep wids entry after it is gone (default = 0).
    wids_entry_cleanup: int
    # Time period in minutes to keep BLE device after it is gone (default = 60).
    ble_device_cleanup: int
    # Time between running client (station) reports (1 - 255 sec, default = 10).
    sta_stats_interval: int
    # Time between running Virtual Access Point (VAP) reports
    vap_stats_interval: int
    # Time between running radio reports (1 - 255 sec, default = 15).
    radio_stats_interval: int
    # Time between running station capability reports (1 - 255 sec, default = 30).
    sta_capability_interval: int
    # Time between running client presence flushes to remove clients that are listed b
    sta_locate_timer: int
    # Time period to keep IPsec VPN interfaces up after WTP sessions are disconnected
    ipsec_intf_cleanup: int
    # Time between running Bluetooth Low Energy (BLE) reports
    ble_scan_report_intv: int
    # Dynamic radio mode assignment (DRMA) schedule interval in minutes
    drma_interval: int
    # Time in minutes to wait before AP reboots when there is no controller detected
    ap_reboot_wait_interval1: int
    # Time to reboot the AP when there is no controller detected and standalone SSIDs
    ap_reboot_wait_time: str
    # Time in minutes to wait before AP reboots when there is no controller detected a
    ap_reboot_wait_interval2: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> TimersPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Timers:
    """
    Configure CAPWAP timers.
    
    Path: wireless_controller/timers
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
    ) -> TimersObject: ...
    
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
    ) -> TimersObject: ...
    
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
    ) -> TimersObject: ...
    
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
    ) -> TimersResponse: ...
    
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
    ) -> TimersResponse: ...
    
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
    ) -> TimersResponse: ...
    
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
    ) -> TimersObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: TimersPayload | None = ...,
        echo_interval: int | None = ...,
        nat_session_keep_alive: int | None = ...,
        discovery_interval: int | None = ...,
        client_idle_timeout: int | None = ...,
        client_idle_rehome_timeout: int | None = ...,
        auth_timeout: int | None = ...,
        rogue_ap_log: int | None = ...,
        fake_ap_log: int | None = ...,
        sta_offline_cleanup: int | None = ...,
        sta_offline_ip2mac_cleanup: int | None = ...,
        sta_cap_cleanup: int | None = ...,
        rogue_ap_cleanup: int | None = ...,
        rogue_sta_cleanup: int | None = ...,
        wids_entry_cleanup: int | None = ...,
        ble_device_cleanup: int | None = ...,
        sta_stats_interval: int | None = ...,
        vap_stats_interval: int | None = ...,
        radio_stats_interval: int | None = ...,
        sta_capability_interval: int | None = ...,
        sta_locate_timer: int | None = ...,
        ipsec_intf_cleanup: int | None = ...,
        ble_scan_report_intv: int | None = ...,
        drma_interval: int | None = ...,
        ap_reboot_wait_interval1: int | None = ...,
        ap_reboot_wait_time: str | None = ...,
        ap_reboot_wait_interval2: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TimersObject: ...
    
    @overload
    def put(
        self,
        payload_dict: TimersPayload | None = ...,
        echo_interval: int | None = ...,
        nat_session_keep_alive: int | None = ...,
        discovery_interval: int | None = ...,
        client_idle_timeout: int | None = ...,
        client_idle_rehome_timeout: int | None = ...,
        auth_timeout: int | None = ...,
        rogue_ap_log: int | None = ...,
        fake_ap_log: int | None = ...,
        sta_offline_cleanup: int | None = ...,
        sta_offline_ip2mac_cleanup: int | None = ...,
        sta_cap_cleanup: int | None = ...,
        rogue_ap_cleanup: int | None = ...,
        rogue_sta_cleanup: int | None = ...,
        wids_entry_cleanup: int | None = ...,
        ble_device_cleanup: int | None = ...,
        sta_stats_interval: int | None = ...,
        vap_stats_interval: int | None = ...,
        radio_stats_interval: int | None = ...,
        sta_capability_interval: int | None = ...,
        sta_locate_timer: int | None = ...,
        ipsec_intf_cleanup: int | None = ...,
        ble_scan_report_intv: int | None = ...,
        drma_interval: int | None = ...,
        ap_reboot_wait_interval1: int | None = ...,
        ap_reboot_wait_time: str | None = ...,
        ap_reboot_wait_interval2: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: TimersPayload | None = ...,
        echo_interval: int | None = ...,
        nat_session_keep_alive: int | None = ...,
        discovery_interval: int | None = ...,
        client_idle_timeout: int | None = ...,
        client_idle_rehome_timeout: int | None = ...,
        auth_timeout: int | None = ...,
        rogue_ap_log: int | None = ...,
        fake_ap_log: int | None = ...,
        sta_offline_cleanup: int | None = ...,
        sta_offline_ip2mac_cleanup: int | None = ...,
        sta_cap_cleanup: int | None = ...,
        rogue_ap_cleanup: int | None = ...,
        rogue_sta_cleanup: int | None = ...,
        wids_entry_cleanup: int | None = ...,
        ble_device_cleanup: int | None = ...,
        sta_stats_interval: int | None = ...,
        vap_stats_interval: int | None = ...,
        radio_stats_interval: int | None = ...,
        sta_capability_interval: int | None = ...,
        sta_locate_timer: int | None = ...,
        ipsec_intf_cleanup: int | None = ...,
        ble_scan_report_intv: int | None = ...,
        drma_interval: int | None = ...,
        ap_reboot_wait_interval1: int | None = ...,
        ap_reboot_wait_time: str | None = ...,
        ap_reboot_wait_interval2: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: TimersPayload | None = ...,
        echo_interval: int | None = ...,
        nat_session_keep_alive: int | None = ...,
        discovery_interval: int | None = ...,
        client_idle_timeout: int | None = ...,
        client_idle_rehome_timeout: int | None = ...,
        auth_timeout: int | None = ...,
        rogue_ap_log: int | None = ...,
        fake_ap_log: int | None = ...,
        sta_offline_cleanup: int | None = ...,
        sta_offline_ip2mac_cleanup: int | None = ...,
        sta_cap_cleanup: int | None = ...,
        rogue_ap_cleanup: int | None = ...,
        rogue_sta_cleanup: int | None = ...,
        wids_entry_cleanup: int | None = ...,
        ble_device_cleanup: int | None = ...,
        sta_stats_interval: int | None = ...,
        vap_stats_interval: int | None = ...,
        radio_stats_interval: int | None = ...,
        sta_capability_interval: int | None = ...,
        sta_locate_timer: int | None = ...,
        ipsec_intf_cleanup: int | None = ...,
        ble_scan_report_intv: int | None = ...,
        drma_interval: int | None = ...,
        ap_reboot_wait_interval1: int | None = ...,
        ap_reboot_wait_time: str | None = ...,
        ap_reboot_wait_interval2: int | None = ...,
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
        payload_dict: TimersPayload | None = ...,
        echo_interval: int | None = ...,
        nat_session_keep_alive: int | None = ...,
        discovery_interval: int | None = ...,
        client_idle_timeout: int | None = ...,
        client_idle_rehome_timeout: int | None = ...,
        auth_timeout: int | None = ...,
        rogue_ap_log: int | None = ...,
        fake_ap_log: int | None = ...,
        sta_offline_cleanup: int | None = ...,
        sta_offline_ip2mac_cleanup: int | None = ...,
        sta_cap_cleanup: int | None = ...,
        rogue_ap_cleanup: int | None = ...,
        rogue_sta_cleanup: int | None = ...,
        wids_entry_cleanup: int | None = ...,
        ble_device_cleanup: int | None = ...,
        sta_stats_interval: int | None = ...,
        vap_stats_interval: int | None = ...,
        radio_stats_interval: int | None = ...,
        sta_capability_interval: int | None = ...,
        sta_locate_timer: int | None = ...,
        ipsec_intf_cleanup: int | None = ...,
        ble_scan_report_intv: int | None = ...,
        drma_interval: int | None = ...,
        ap_reboot_wait_interval1: int | None = ...,
        ap_reboot_wait_time: str | None = ...,
        ap_reboot_wait_interval2: int | None = ...,
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
    "Timers",
    "TimersPayload",
    "TimersObject",
]