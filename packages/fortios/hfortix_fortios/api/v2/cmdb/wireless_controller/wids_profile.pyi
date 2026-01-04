from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class WidsProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/wids_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: WidsProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # WIDS profile name.
    comment: NotRequired[str]  # Comment.
    sensor_mode: NotRequired[Literal["disable", "foreign", "both"]]  # Scan nearby WiFi stations (default = disable).
    ap_scan: NotRequired[Literal["disable", "enable"]]  # Enable/disable rogue AP detection.
    ap_scan_channel_list_2G_5G: NotRequired[list[dict[str, Any]]]  # Selected ap scan channel list for 2.4G and 5G bands.
    ap_scan_channel_list_6G: NotRequired[list[dict[str, Any]]]  # Selected ap scan channel list for 6G band.
    ap_bgscan_period: NotRequired[int]  # Period between background scans (10 - 3600 sec, default = 60
    ap_bgscan_intv: NotRequired[int]  # Period between successive channel scans (1 - 600 sec, defaul
    ap_bgscan_duration: NotRequired[int]  # Listen time on scanning a channel (10 - 1000 msec, default =
    ap_bgscan_idle: NotRequired[int]  # Wait time for channel inactivity before scanning this channe
    ap_bgscan_report_intv: NotRequired[int]  # Period between background scan reports (15 - 600 sec, defaul
    ap_bgscan_disable_schedules: NotRequired[list[dict[str, Any]]]  # Firewall schedules for turning off FortiAP radio background 
    ap_fgscan_report_intv: NotRequired[int]  # Period between foreground scan reports (15 - 600 sec, defaul
    ap_scan_passive: NotRequired[Literal["enable", "disable"]]  # Enable/disable passive scanning. Enable means do not send pr
    ap_scan_threshold: NotRequired[str]  # Minimum signal level/threshold in dBm required for the AP to
    ap_auto_suppress: NotRequired[Literal["enable", "disable"]]  # Enable/disable on-wire rogue AP auto-suppression (default = 
    wireless_bridge: NotRequired[Literal["enable", "disable"]]  # Enable/disable wireless bridge detection (default = disable)
    deauth_broadcast: NotRequired[Literal["enable", "disable"]]  # Enable/disable broadcasting de-authentication detection (def
    null_ssid_probe_resp: NotRequired[Literal["enable", "disable"]]  # Enable/disable null SSID probe response detection (default =
    long_duration_attack: NotRequired[Literal["enable", "disable"]]  # Enable/disable long duration attack detection based on user 
    long_duration_thresh: NotRequired[int]  # Threshold value for long duration attack detection (1000 - 3
    invalid_mac_oui: NotRequired[Literal["enable", "disable"]]  # Enable/disable invalid MAC OUI detection.
    weak_wep_iv: NotRequired[Literal["enable", "disable"]]  # Enable/disable weak WEP IV (Initialization Vector) detection
    auth_frame_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication frame flooding detection (defa
    auth_flood_time: NotRequired[int]  # Number of seconds after which a station is considered not co
    auth_flood_thresh: NotRequired[int]  # The threshold value for authentication frame flooding.
    assoc_frame_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable association frame flooding detection (default
    assoc_flood_time: NotRequired[int]  # Number of seconds after which a station is considered not co
    assoc_flood_thresh: NotRequired[int]  # The threshold value for association frame flooding.
    reassoc_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable reassociation flood detection (default = disa
    reassoc_flood_time: NotRequired[int]  # Detection Window Period.
    reassoc_flood_thresh: NotRequired[int]  # The threshold value for reassociation flood.
    probe_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable probe flood detection (default = disable).
    probe_flood_time: NotRequired[int]  # Detection Window Period.
    probe_flood_thresh: NotRequired[int]  # The threshold value for probe flood.
    bcn_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable bcn flood detection (default = disable).
    bcn_flood_time: NotRequired[int]  # Detection Window Period.
    bcn_flood_thresh: NotRequired[int]  # The threshold value for bcn flood.
    rts_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable rts flood detection (default = disable).
    rts_flood_time: NotRequired[int]  # Detection Window Period.
    rts_flood_thresh: NotRequired[int]  # The threshold value for rts flood.
    cts_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable cts flood detection (default = disable).
    cts_flood_time: NotRequired[int]  # Detection Window Period.
    cts_flood_thresh: NotRequired[int]  # The threshold value for cts flood.
    client_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable client flood detection (default = disable).
    client_flood_time: NotRequired[int]  # Detection Window Period.
    client_flood_thresh: NotRequired[int]  # The threshold value for client flood.
    block_ack_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable block_ack flood detection (default = disable)
    block_ack_flood_time: NotRequired[int]  # Detection Window Period.
    block_ack_flood_thresh: NotRequired[int]  # The threshold value for block_ack flood.
    pspoll_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable pspoll flood detection (default = disable).
    pspoll_flood_time: NotRequired[int]  # Detection Window Period.
    pspoll_flood_thresh: NotRequired[int]  # The threshold value for pspoll flood.
    netstumbler: NotRequired[Literal["enable", "disable"]]  # Enable/disable netstumbler detection (default = disable).
    netstumbler_time: NotRequired[int]  # Detection Window Period.
    netstumbler_thresh: NotRequired[int]  # The threshold value for netstumbler.
    wellenreiter: NotRequired[Literal["enable", "disable"]]  # Enable/disable wellenreiter detection (default = disable).
    wellenreiter_time: NotRequired[int]  # Detection Window Period.
    wellenreiter_thresh: NotRequired[int]  # The threshold value for wellenreiter.
    spoofed_deauth: NotRequired[Literal["enable", "disable"]]  # Enable/disable spoofed de-authentication attack detection (d
    asleap_attack: NotRequired[Literal["enable", "disable"]]  # Enable/disable asleap attack detection (default = disable).
    eapol_start_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable EAPOL-Start flooding (to AP) detection (defau
    eapol_start_thresh: NotRequired[int]  # The threshold value for EAPOL-Start flooding in specified in
    eapol_start_intv: NotRequired[int]  # The detection interval for EAPOL-Start flooding (1 - 3600 se
    eapol_logoff_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable EAPOL-Logoff flooding (to AP) detection (defa
    eapol_logoff_thresh: NotRequired[int]  # The threshold value for EAPOL-Logoff flooding in specified i
    eapol_logoff_intv: NotRequired[int]  # The detection interval for EAPOL-Logoff flooding (1 - 3600 s
    eapol_succ_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable EAPOL-Success flooding (to AP) detection (def
    eapol_succ_thresh: NotRequired[int]  # The threshold value for EAPOL-Success flooding in specified 
    eapol_succ_intv: NotRequired[int]  # The detection interval for EAPOL-Success flooding (1 - 3600 
    eapol_fail_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable EAPOL-Failure flooding (to AP) detection (def
    eapol_fail_thresh: NotRequired[int]  # The threshold value for EAPOL-Failure flooding in specified 
    eapol_fail_intv: NotRequired[int]  # The detection interval for EAPOL-Failure flooding (1 - 3600 
    eapol_pre_succ_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable premature EAPOL-Success flooding (to STA) det
    eapol_pre_succ_thresh: NotRequired[int]  # The threshold value for premature EAPOL-Success flooding in 
    eapol_pre_succ_intv: NotRequired[int]  # The detection interval for premature EAPOL-Success flooding 
    eapol_pre_fail_flood: NotRequired[Literal["enable", "disable"]]  # Enable/disable premature EAPOL-Failure flooding (to STA) det
    eapol_pre_fail_thresh: NotRequired[int]  # The threshold value for premature EAPOL-Failure flooding in 
    eapol_pre_fail_intv: NotRequired[int]  # The detection interval for premature EAPOL-Failure flooding 
    deauth_unknown_src_thresh: NotRequired[int]  # Threshold value per second to deauth unknown src for DoS att
    windows_bridge: NotRequired[Literal["enable", "disable"]]  # Enable/disable windows bridge detection (default = disable).
    disassoc_broadcast: NotRequired[Literal["enable", "disable"]]  # Enable/disable broadcast dis-association detection (default 
    ap_spoofing: NotRequired[Literal["enable", "disable"]]  # Enable/disable AP spoofing detection (default = disable).
    chan_based_mitm: NotRequired[Literal["enable", "disable"]]  # Enable/disable channel based mitm detection (default = disab
    adhoc_valid_ssid: NotRequired[Literal["enable", "disable"]]  # Enable/disable adhoc using valid SSID detection (default = d
    adhoc_network: NotRequired[Literal["enable", "disable"]]  # Enable/disable adhoc network detection (default = disable).
    eapol_key_overflow: NotRequired[Literal["enable", "disable"]]  # Enable/disable overflow EAPOL key detection (default = disab
    ap_impersonation: NotRequired[Literal["enable", "disable"]]  # Enable/disable AP impersonation detection (default = disable
    invalid_addr_combination: NotRequired[Literal["enable", "disable"]]  # Enable/disable invalid address combination detection (defaul
    beacon_wrong_channel: NotRequired[Literal["enable", "disable"]]  # Enable/disable beacon wrong channel detection (default = dis
    ht_greenfield: NotRequired[Literal["enable", "disable"]]  # Enable/disable HT greenfield detection (default = disable).
    overflow_ie: NotRequired[Literal["enable", "disable"]]  # Enable/disable overflow IE detection (default = disable).
    malformed_ht_ie: NotRequired[Literal["enable", "disable"]]  # Enable/disable malformed HT IE detection (default = disable)
    malformed_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable malformed auth frame detection (default = dis
    malformed_association: NotRequired[Literal["enable", "disable"]]  # Enable/disable malformed association request detection (defa
    ht_40mhz_intolerance: NotRequired[Literal["enable", "disable"]]  # Enable/disable HT 40 MHz intolerance detection (default = di
    valid_ssid_misuse: NotRequired[Literal["enable", "disable"]]  # Enable/disable valid SSID misuse detection (default = disabl
    valid_client_misassociation: NotRequired[Literal["enable", "disable"]]  # Enable/disable valid client misassociation detection (defaul
    hotspotter_attack: NotRequired[Literal["enable", "disable"]]  # Enable/disable hotspotter attack detection (default = disabl
    pwsave_dos_attack: NotRequired[Literal["enable", "disable"]]  # Enable/disable power save DOS attack detection (default = di
    omerta_attack: NotRequired[Literal["enable", "disable"]]  # Enable/disable omerta attack detection (default = disable).
    disconnect_station: NotRequired[Literal["enable", "disable"]]  # Enable/disable disconnect station detection (default = disab
    unencrypted_valid: NotRequired[Literal["enable", "disable"]]  # Enable/disable unencrypted valid detection (default = disabl
    fata_jack: NotRequired[Literal["enable", "disable"]]  # Enable/disable FATA-Jack detection (default = disable).
    risky_encryption: NotRequired[Literal["enable", "disable"]]  # Enable/disable Risky Encryption detection (default = disable
    fuzzed_beacon: NotRequired[Literal["enable", "disable"]]  # Enable/disable fuzzed beacon detection (default = disable).
    fuzzed_probe_request: NotRequired[Literal["enable", "disable"]]  # Enable/disable fuzzed probe request detection (default = dis
    fuzzed_probe_response: NotRequired[Literal["enable", "disable"]]  # Enable/disable fuzzed probe response detection (default = di
    air_jack: NotRequired[Literal["enable", "disable"]]  # Enable/disable AirJack detection (default = disable).
    wpa_ft_attack: NotRequired[Literal["enable", "disable"]]  # Enable/disable WPA FT attack detection (default = disable).


class WidsProfile:
    """
    Configure wireless intrusion detection system (WIDS) profiles.
    
    Path: wireless_controller/wids_profile
    Category: cmdb
    Primary Key: name
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
        payload_dict: WidsProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        sensor_mode: Literal["disable", "foreign", "both"] | None = ...,
        ap_scan: Literal["disable", "enable"] | None = ...,
        ap_scan_channel_list_2G_5G: list[dict[str, Any]] | None = ...,
        ap_scan_channel_list_6G: list[dict[str, Any]] | None = ...,
        ap_bgscan_period: int | None = ...,
        ap_bgscan_intv: int | None = ...,
        ap_bgscan_duration: int | None = ...,
        ap_bgscan_idle: int | None = ...,
        ap_bgscan_report_intv: int | None = ...,
        ap_bgscan_disable_schedules: list[dict[str, Any]] | None = ...,
        ap_fgscan_report_intv: int | None = ...,
        ap_scan_passive: Literal["enable", "disable"] | None = ...,
        ap_scan_threshold: str | None = ...,
        ap_auto_suppress: Literal["enable", "disable"] | None = ...,
        wireless_bridge: Literal["enable", "disable"] | None = ...,
        deauth_broadcast: Literal["enable", "disable"] | None = ...,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = ...,
        long_duration_attack: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: WidsProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        sensor_mode: Literal["disable", "foreign", "both"] | None = ...,
        ap_scan: Literal["disable", "enable"] | None = ...,
        ap_scan_channel_list_2G_5G: list[dict[str, Any]] | None = ...,
        ap_scan_channel_list_6G: list[dict[str, Any]] | None = ...,
        ap_bgscan_period: int | None = ...,
        ap_bgscan_intv: int | None = ...,
        ap_bgscan_duration: int | None = ...,
        ap_bgscan_idle: int | None = ...,
        ap_bgscan_report_intv: int | None = ...,
        ap_bgscan_disable_schedules: list[dict[str, Any]] | None = ...,
        ap_fgscan_report_intv: int | None = ...,
        ap_scan_passive: Literal["enable", "disable"] | None = ...,
        ap_scan_threshold: str | None = ...,
        ap_auto_suppress: Literal["enable", "disable"] | None = ...,
        wireless_bridge: Literal["enable", "disable"] | None = ...,
        deauth_broadcast: Literal["enable", "disable"] | None = ...,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = ...,
        long_duration_attack: Literal["enable", "disable"] | None = ...,
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
        payload_dict: WidsProfilePayload | None = ...,
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