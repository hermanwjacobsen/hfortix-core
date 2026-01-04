from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class WtpProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/wtp_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: WtpProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # WTP (or FortiAP or AP) profile name.
    comment: NotRequired[str]  # Comment.
    platform: NotRequired[str]  # WTP, FortiAP, or AP platform.
    control_message_offload: NotRequired[Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"]]  # Enable/disable CAPWAP control message data channel offload.
    bonjour_profile: NotRequired[str]  # Bonjour profile name.
    apcfg_profile: NotRequired[str]  # AP local configuration profile name.
    apcfg_mesh: NotRequired[Literal["enable", "disable"]]  # Enable/disable AP local mesh configuration (default = disabl
    apcfg_mesh_ap_type: NotRequired[Literal["ethernet", "mesh", "auto"]]  # Mesh AP Type (default = ethernet).
    apcfg_mesh_ssid: NotRequired[str]  #  Mesh SSID (default = none).
    apcfg_mesh_eth_bridge: NotRequired[Literal["enable", "disable"]]  # Enable/disable mesh ethernet bridge (default = disable).
    ble_profile: NotRequired[str]  # Bluetooth Low Energy profile name.
    syslog_profile: NotRequired[str]  # System log server configuration profile name.
    wan_port_mode: NotRequired[Literal["wan-lan", "wan-only"]]  # Enable/disable using a WAN port as a LAN port.
    lan: NotRequired[str]  # WTP LAN port mapping.
    energy_efficient_ethernet: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of energy efficient Ethernet on WTP.
    led_state: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of LEDs on WTP (default = enable).
    led_schedules: NotRequired[list[dict[str, Any]]]  # Recurring firewall schedules for illuminating LEDs on the Fo
    dtls_policy: NotRequired[Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"]]  # WTP data channel DTLS policy (default = clear-text).
    dtls_in_kernel: NotRequired[Literal["enable", "disable"]]  # Enable/disable data channel DTLS in kernel.
    max_clients: NotRequired[int]  # Maximum number of stations (STAs) supported by the WTP (defa
    handoff_rssi: NotRequired[int]  # Minimum received signal strength indicator (RSSI) value for 
    handoff_sta_thresh: NotRequired[int]  # Threshold value for AP handoff.
    handoff_roaming: NotRequired[Literal["enable", "disable"]]  # Enable/disable client load balancing during roaming to avoid
    deny_mac_list: NotRequired[list[dict[str, Any]]]  # List of MAC addresses that are denied access to this WTP, Fo
    ap_country: NotRequired[Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"]]  # Country in which this WTP, FortiAP, or AP will operate (defa
    ip_fragment_preventing: NotRequired[Literal["tcp-mss-adjust", "icmp-unreachable"]]  # Method(s) by which IP fragmentation is prevented for control
    tun_mtu_uplink: NotRequired[int]  # The maximum transmission unit (MTU) of uplink CAPWAP tunnel 
    tun_mtu_downlink: NotRequired[int]  # The MTU of downlink CAPWAP tunnel (576 - 1500 bytes or 0; 0 
    split_tunneling_acl_path: NotRequired[Literal["tunnel", "local"]]  # Split tunneling ACL path is local/tunnel.
    split_tunneling_acl_local_ap_subnet: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatically adding local subnetwork of Fort
    split_tunneling_acl: NotRequired[list[dict[str, Any]]]  # Split tunneling ACL filter list.
    allowaccess: NotRequired[Literal["https", "ssh", "snmp"]]  # Control management access to the managed WTP, FortiAP, or AP
    login_passwd_change: NotRequired[Literal["yes", "default", "no"]]  # Change or reset the administrator password of a managed WTP,
    login_passwd: NotRequired[str]  # Set the managed WTP, FortiAP, or AP's administrator password
    lldp: NotRequired[Literal["enable", "disable"]]  # Enable/disable Link Layer Discovery Protocol (LLDP) for the 
    poe_mode: NotRequired[Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"]]  # Set the WTP, FortiAP, or AP's PoE mode.
    usb_port: NotRequired[Literal["enable", "disable"]]  # Enable/disable USB port of the WTP (default = enable).
    frequency_handoff: NotRequired[Literal["enable", "disable"]]  # Enable/disable frequency handoff of clients to other channel
    ap_handoff: NotRequired[Literal["enable", "disable"]]  # Enable/disable AP handoff of clients to other APs (default =
    default_mesh_root: NotRequired[Literal["enable", "disable"]]  # Configure default mesh root SSID when it is not included by 
    radio_1: NotRequired[str]  # Configuration options for radio 1.
    radio_2: NotRequired[str]  # Configuration options for radio 2.
    radio_3: NotRequired[str]  # Configuration options for radio 3.
    radio_4: NotRequired[str]  # Configuration options for radio 4.
    lbs: NotRequired[str]  # Set various location based service (LBS) options.
    ext_info_enable: NotRequired[Literal["enable", "disable"]]  # Enable/disable station/VAP/radio extension information.
    indoor_outdoor_deployment: NotRequired[Literal["platform-determined", "outdoor", "indoor"]]  # Set to allow indoor/outdoor-only channels under regulatory r
    esl_ses_dongle: NotRequired[str]  # ESL SES-imagotag dongle configuration.
    console_login: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiAP console login access (default = enabl
    wan_port_auth: NotRequired[Literal["none", "802.1x"]]  # Set WAN port authentication mode (default = none).
    wan_port_auth_usrname: NotRequired[str]  # Set WAN port 802.1x supplicant user name.
    wan_port_auth_password: NotRequired[str]  # Set WAN port 802.1x supplicant password.
    wan_port_auth_methods: NotRequired[Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"]]  # WAN port 802.1x supplicant EAP methods (default = all).
    wan_port_auth_macsec: NotRequired[Literal["enable", "disable"]]  # Enable/disable WAN port 802.1x supplicant MACsec policy (def
    unii_4_5ghz_band: NotRequired[Literal["enable", "disable"]]  # Enable/disable UNII-4 5Ghz band channels (default = disable)
    admin_auth_tacacs+: NotRequired[str]  # Remote authentication server for admin user.
    admin_restrict_local: NotRequired[Literal["enable", "disable"]]  # Enable/disable local admin authentication restriction when r


class WtpProfile:
    """
    Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
    
    Path: wireless_controller/wtp_profile
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
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        lldp: Literal["enable", "disable"] | None = ...,
        poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"] | None = ...,
        usb_port: Literal["enable", "disable"] | None = ...,
        frequency_handoff: Literal["enable", "disable"] | None = ...,
        ap_handoff: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        lbs: str | None = ...,
        ext_info_enable: Literal["enable", "disable"] | None = ...,
        indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"] | None = ...,
        esl_ses_dongle: str | None = ...,
        console_login: Literal["enable", "disable"] | None = ...,
        wan_port_auth: Literal["none", "802.1x"] | None = ...,
        wan_port_auth_usrname: str | None = ...,
        wan_port_auth_password: str | None = ...,
        wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"] | None = ...,
        wan_port_auth_macsec: Literal["enable", "disable"] | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs+: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        lldp: Literal["enable", "disable"] | None = ...,
        poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"] | None = ...,
        usb_port: Literal["enable", "disable"] | None = ...,
        frequency_handoff: Literal["enable", "disable"] | None = ...,
        ap_handoff: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        lbs: str | None = ...,
        ext_info_enable: Literal["enable", "disable"] | None = ...,
        indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"] | None = ...,
        esl_ses_dongle: str | None = ...,
        console_login: Literal["enable", "disable"] | None = ...,
        wan_port_auth: Literal["none", "802.1x"] | None = ...,
        wan_port_auth_usrname: str | None = ...,
        wan_port_auth_password: str | None = ...,
        wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"] | None = ...,
        wan_port_auth_macsec: Literal["enable", "disable"] | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs+: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
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
        payload_dict: WtpProfilePayload | None = ...,
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
    "WtpProfile",
    "WtpProfilePayload",
]