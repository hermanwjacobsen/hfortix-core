from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class GlobalSettingPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/global_setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: GlobalSettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Name of the wireless controller.
    location: NotRequired[str]  # Description of the location of the wireless controller.
    acd_process_count: NotRequired[int]  # Configure the number cw_acd daemons for multi-core CPU suppo
    wpad_process_count: NotRequired[int]  # Wpad daemon process count for multi-core CPU support.
    image_download: NotRequired[Literal["enable", "disable"]]  # Enable/disable WTP image download at join time.
    rolling_wtp_upgrade: NotRequired[Literal["enable", "disable"]]  # Enable/disable rolling WTP upgrade (default = disable).
    rolling_wtp_upgrade_threshold: NotRequired[str]  # Minimum signal level/threshold in dBm required for the manag
    max_retransmit: NotRequired[int]  # Maximum number of tunnel packet retransmissions (0 - 64, def
    control_message_offload: NotRequired[Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"]]  # Configure CAPWAP control message data channel offload.
    data_ethernet_II: NotRequired[Literal["enable", "disable"]]  # Configure the wireless controller to use Ethernet II or 802.
    link_aggregation: NotRequired[Literal["enable", "disable"]]  # Enable/disable calculating the CAPWAP transmit hash to load 
    mesh_eth_type: NotRequired[int]  # Mesh Ethernet identifier included in backhaul packets (0 - 6
    fiapp_eth_type: NotRequired[int]  # Ethernet type for Fortinet Inter-Access Point Protocol (IAPP
    discovery_mc_addr: NotRequired[str]  # Multicast IP address for AP discovery (default = 244.0.1.140
    max_clients: NotRequired[int]  # Maximum number of clients that can connect simultaneously (d
    rogue_scan_mac_adjacency: NotRequired[int]  # Maximum numerical difference between an AP's Ethernet and wi
    ipsec_base_ip: NotRequired[str]  # Base IP address for IPsec VPN tunnels between the access poi
    wtp_share: NotRequired[Literal["enable", "disable"]]  # Enable/disable sharing of WTPs between VDOMs.
    tunnel_mode: NotRequired[Literal["compatible", "strict"]]  # Compatible/strict tunnel mode.
    nac_interval: NotRequired[int]  # Interval in seconds between two WiFi network access control 
    ap_log_server: NotRequired[Literal["enable", "disable"]]  # Enable/disable configuring FortiGate to redirect wireless ev
    ap_log_server_ip: NotRequired[str]  # IP address that FortiGate or FortiAPs send log messages to.
    ap_log_server_port: NotRequired[int]  # Port that FortiGate or FortiAPs send log messages to.
    max_sta_offline: NotRequired[int]  # Maximum number of station offline stored on the controller (
    max_sta_offline_ip2mac: NotRequired[int]  # Maximum number of station offline ip2mac stored on the contr
    max_sta_cap: NotRequired[int]  # Maximum number of station cap stored on the controller (defa
    max_sta_cap_wtp: NotRequired[int]  # Maximum number of station cap's wtp info stored on the contr
    max_rogue_ap: NotRequired[int]  # Maximum number of rogue APs stored on the controller (defaul
    max_rogue_ap_wtp: NotRequired[int]  # Maximum number of rogue AP's wtp info stored on the controll
    max_rogue_sta: NotRequired[int]  # Maximum number of rogue stations stored on the controller (d
    max_wids_entry: NotRequired[int]  # Maximum number of wids entries stored on the controller (def
    max_ble_device: NotRequired[int]  # Maximum number of BLE devices stored on the controller (defa


class GlobalSetting:
    """
    Configure wireless controller global settings.
    
    Path: wireless_controller/global_setting
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
        payload_dict: GlobalSettingPayload | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        acd_process_count: int | None = ...,
        wpad_process_count: int | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade_threshold: str | None = ...,
        max_retransmit: int | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | None = ...,
        data_ethernet_II: Literal["enable", "disable"] | None = ...,
        link_aggregation: Literal["enable", "disable"] | None = ...,
        mesh_eth_type: int | None = ...,
        fiapp_eth_type: int | None = ...,
        discovery_mc_addr: str | None = ...,
        max_clients: int | None = ...,
        rogue_scan_mac_adjacency: int | None = ...,
        ipsec_base_ip: str | None = ...,
        wtp_share: Literal["enable", "disable"] | None = ...,
        tunnel_mode: Literal["compatible", "strict"] | None = ...,
        nac_interval: int | None = ...,
        ap_log_server: Literal["enable", "disable"] | None = ...,
        ap_log_server_ip: str | None = ...,
        ap_log_server_port: int | None = ...,
        max_sta_offline: int | None = ...,
        max_sta_offline_ip2mac: int | None = ...,
        max_sta_cap: int | None = ...,
        max_sta_cap_wtp: int | None = ...,
        max_rogue_ap: int | None = ...,
        max_rogue_ap_wtp: int | None = ...,
        max_rogue_sta: int | None = ...,
        max_wids_entry: int | None = ...,
        max_ble_device: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: GlobalSettingPayload | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        acd_process_count: int | None = ...,
        wpad_process_count: int | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade_threshold: str | None = ...,
        max_retransmit: int | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | None = ...,
        data_ethernet_II: Literal["enable", "disable"] | None = ...,
        link_aggregation: Literal["enable", "disable"] | None = ...,
        mesh_eth_type: int | None = ...,
        fiapp_eth_type: int | None = ...,
        discovery_mc_addr: str | None = ...,
        max_clients: int | None = ...,
        rogue_scan_mac_adjacency: int | None = ...,
        ipsec_base_ip: str | None = ...,
        wtp_share: Literal["enable", "disable"] | None = ...,
        tunnel_mode: Literal["compatible", "strict"] | None = ...,
        nac_interval: int | None = ...,
        ap_log_server: Literal["enable", "disable"] | None = ...,
        ap_log_server_ip: str | None = ...,
        ap_log_server_port: int | None = ...,
        max_sta_offline: int | None = ...,
        max_sta_offline_ip2mac: int | None = ...,
        max_sta_cap: int | None = ...,
        max_sta_cap_wtp: int | None = ...,
        max_rogue_ap: int | None = ...,
        max_rogue_ap_wtp: int | None = ...,
        max_rogue_sta: int | None = ...,
        max_wids_entry: int | None = ...,
        max_ble_device: int | None = ...,
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
        payload_dict: GlobalSettingPayload | None = ...,
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


__all__ = [
    "GlobalSetting",
    "GlobalSettingPayload",
]