from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class WtpProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/wtp_profile payload fields.
    
    Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.tacacs+.TacacsPlusEndpoint` (via: admin-auth-tacacs+)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: apcfg-auto-cert-est-https-ca, apcfg-auto-cert-scep-https-ca)
        - :class:`~.wireless-controller.apcfg-profile.ApcfgProfileEndpoint` (via: apcfg-profile)
        - :class:`~.wireless-controller.ble-profile.BleProfileEndpoint` (via: ble-profile)
        - :class:`~.wireless-controller.bonjour-profile.BonjourProfileEndpoint` (via: bonjour-profile)
        - :class:`~.wireless-controller.lw-profile.LwProfileEndpoint` (via: lw-profile)
        - :class:`~.wireless-controller.syslog-profile.SyslogProfileEndpoint` (via: syslog-profile)
        - :class:`~.wireless-controller.vap.VapEndpoint` (via: apcfg-mesh-ssid)

    **Usage:**
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
    lw_profile: NotRequired[str]  # LoRaWAN profile name.
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
    apcfg_auto_cert: NotRequired[Literal["enable", "disable"]]  # Enable/disable AP local auto cert configuration (default = d
    apcfg_auto_cert_enroll_protocol: NotRequired[Literal["none", "est", "scep"]]  # Certificate enrollment protocol (default = none)
    apcfg_auto_cert_crypto_algo: NotRequired[Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"]]  # Cryptography algorithm: rsa-1024, rsa-1536, rsa-2048, rsa-40
    apcfg_auto_cert_est_server: NotRequired[str]  # Address and port for EST server (e.g. https://example.com:12
    apcfg_auto_cert_est_ca_id: NotRequired[str]  # CA identifier of the CA server for signing via EST.
    apcfg_auto_cert_est_http_username: NotRequired[str]  # HTTP Authentication username for signing via EST.
    apcfg_auto_cert_est_http_password: NotRequired[str]  # HTTP Authentication password for signing via EST.
    apcfg_auto_cert_est_subject: NotRequired[str]  # Subject e.g. "CN=User,DC=example,DC=COM" (default = CN=Forti
    apcfg_auto_cert_est_subject_alt_name: NotRequired[str]  # Subject alternative name (optional, e.g. "DNS:dns1.com,IP:19
    apcfg_auto_cert_auto_regen_days: NotRequired[int]  # Number of days to wait before expiry of an updated local cer
    apcfg_auto_cert_est_https_ca: NotRequired[str]  # PEM format https CA Certificate.
    apcfg_auto_cert_scep_keytype: NotRequired[Literal["rsa", "ec"]]  # Key type (default = rsa)
    apcfg_auto_cert_scep_keysize: NotRequired[Literal["1024", "1536", "2048", "4096"]]  # Key size: 1024, 1536, 2048, 4096 (default 2048).
    apcfg_auto_cert_scep_ec_name: NotRequired[Literal["secp256r1", "secp384r1", "secp521r1"]]  # Elliptic curve name: secp256r1, secp384r1 and secp521r1. (de
    apcfg_auto_cert_scep_sub_fully_dn: NotRequired[str]  # Full DN of the subject (e.g C=US,ST=CA,L=Sunnyvale,O=Fortine
    apcfg_auto_cert_scep_url: NotRequired[str]  # SCEP server URL.
    apcfg_auto_cert_scep_password: NotRequired[str]  # SCEP server challenge password for auto-regeneration.
    apcfg_auto_cert_scep_ca_id: NotRequired[str]  # CA identifier of the CA server for signing via SCEP.
    apcfg_auto_cert_scep_subject_alt_name: NotRequired[str]  # Subject alternative name (optional, e.g. "DNS:dns1.com,IP:19
    apcfg_auto_cert_scep_https_ca: NotRequired[str]  # PEM format https CA Certificate.
    unii_4_5ghz_band: NotRequired[Literal["enable", "disable"]]  # Enable/disable UNII-4 5Ghz band channels (default = disable)
    admin_auth_tacacs_plus: NotRequired[str]  # Remote authentication server for admin user.
    admin_restrict_local: NotRequired[Literal["enable", "disable"]]  # Enable/disable local admin authentication restriction when r


class WtpProfileObject(FortiObject[WtpProfilePayload]):
    """Typed FortiObject for wireless_controller/wtp_profile with IDE autocomplete support."""
    
    # WTP (or FortiAP or AP) profile name.
    name: str
    # Comment.
    comment: str
    # WTP, FortiAP, or AP platform.
    platform: str
    # Enable/disable CAPWAP control message data channel offload.
    control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"]
    # Bonjour profile name.
    bonjour_profile: str
    # AP local configuration profile name.
    apcfg_profile: str
    # Enable/disable AP local mesh configuration (default = disable).
    apcfg_mesh: Literal["enable", "disable"]
    # Mesh AP Type (default = ethernet).
    apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"]
    #  Mesh SSID (default = none).
    apcfg_mesh_ssid: str
    # Enable/disable mesh ethernet bridge (default = disable).
    apcfg_mesh_eth_bridge: Literal["enable", "disable"]
    # Bluetooth Low Energy profile name.
    ble_profile: str
    # LoRaWAN profile name.
    lw_profile: str
    # System log server configuration profile name.
    syslog_profile: str
    # Enable/disable using a WAN port as a LAN port.
    wan_port_mode: Literal["wan-lan", "wan-only"]
    # WTP LAN port mapping.
    lan: str
    # Enable/disable use of energy efficient Ethernet on WTP.
    energy_efficient_ethernet: Literal["enable", "disable"]
    # Enable/disable use of LEDs on WTP (default = enable).
    led_state: Literal["enable", "disable"]
    # Recurring firewall schedules for illuminating LEDs on the FortiAP. If led-state 
    led_schedules: list[str]  # Auto-flattened from member_table
    # WTP data channel DTLS policy (default = clear-text).
    dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"]
    # Enable/disable data channel DTLS in kernel.
    dtls_in_kernel: Literal["enable", "disable"]
    # Maximum number of stations (STAs) supported by the WTP (default = 0, meaning no 
    max_clients: int
    # Minimum received signal strength indicator (RSSI) value for handoff (20 - 30, de
    handoff_rssi: int
    # Threshold value for AP handoff.
    handoff_sta_thresh: int
    # Enable/disable client load balancing during roaming to avoid roaming delay (defa
    handoff_roaming: Literal["enable", "disable"]
    # List of MAC addresses that are denied access to this WTP, FortiAP, or AP.
    deny_mac_list: list[str]  # Auto-flattened from member_table
    # Country in which this WTP, FortiAP, or AP will operate (default = NA, automatica
    ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"]
    # Method(s) by which IP fragmentation is prevented for control and data packets th
    ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"]
    # The maximum transmission unit (MTU) of uplink CAPWAP tunnel (576 - 1500 bytes or
    tun_mtu_uplink: int
    # The MTU of downlink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU 
    tun_mtu_downlink: int
    # Split tunneling ACL path is local/tunnel.
    split_tunneling_acl_path: Literal["tunnel", "local"]
    # Enable/disable automatically adding local subnetwork of FortiAP to split-tunneli
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]
    # Split tunneling ACL filter list.
    split_tunneling_acl: list[str]  # Auto-flattened from member_table
    # Control management access to the managed WTP, FortiAP, or AP. Separate entries w
    allowaccess: Literal["https", "ssh", "snmp"]
    # Change or reset the administrator password of a managed WTP, FortiAP or AP (yes,
    login_passwd_change: Literal["yes", "default", "no"]
    # Set the managed WTP, FortiAP, or AP's administrator password.
    login_passwd: str
    # Enable/disable Link Layer Discovery Protocol (LLDP) for the WTP, FortiAP, or AP 
    lldp: Literal["enable", "disable"]
    # Set the WTP, FortiAP, or AP's PoE mode.
    poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"]
    # Enable/disable USB port of the WTP (default = enable).
    usb_port: Literal["enable", "disable"]
    # Enable/disable frequency handoff of clients to other channels (default = disable
    frequency_handoff: Literal["enable", "disable"]
    # Enable/disable AP handoff of clients to other APs (default = disable).
    ap_handoff: Literal["enable", "disable"]
    # Configure default mesh root SSID when it is not included by radio's SSID configu
    default_mesh_root: Literal["enable", "disable"]
    # Configuration options for radio 1.
    radio_1: str
    # Configuration options for radio 2.
    radio_2: str
    # Configuration options for radio 3.
    radio_3: str
    # Configuration options for radio 4.
    radio_4: str
    # Set various location based service (LBS) options.
    lbs: str
    # Enable/disable station/VAP/radio extension information.
    ext_info_enable: Literal["enable", "disable"]
    # Set to allow indoor/outdoor-only channels under regulatory rules (default = plat
    indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"]
    # ESL SES-imagotag dongle configuration.
    esl_ses_dongle: str
    # Enable/disable FortiAP console login access (default = enable).
    console_login: Literal["enable", "disable"]
    # Set WAN port authentication mode (default = none).
    wan_port_auth: Literal["none", "802.1x"]
    # Set WAN port 802.1x supplicant user name.
    wan_port_auth_usrname: str
    # Set WAN port 802.1x supplicant password.
    wan_port_auth_password: str
    # WAN port 802.1x supplicant EAP methods (default = all).
    wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"]
    # Enable/disable WAN port 802.1x supplicant MACsec policy (default = disable).
    wan_port_auth_macsec: Literal["enable", "disable"]
    # Enable/disable AP local auto cert configuration (default = disable).
    apcfg_auto_cert: Literal["enable", "disable"]
    # Certificate enrollment protocol (default = none)
    apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"]
    # Cryptography algorithm: rsa-1024, rsa-1536, rsa-2048, rsa-4096, ec-secp256r1, ec
    apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"]
    # Address and port for EST server (e.g. https://example.com:1234).
    apcfg_auto_cert_est_server: str
    # CA identifier of the CA server for signing via EST.
    apcfg_auto_cert_est_ca_id: str
    # HTTP Authentication username for signing via EST.
    apcfg_auto_cert_est_http_username: str
    # HTTP Authentication password for signing via EST.
    apcfg_auto_cert_est_http_password: str
    # Subject e.g. "CN=User,DC=example,DC=COM" (default = CN=FortiAP,DC=local,DC=COM)
    apcfg_auto_cert_est_subject: str
    # Subject alternative name (optional, e.g. "DNS:dns1.com,IP:192.168.1.99")
    apcfg_auto_cert_est_subject_alt_name: str
    # Number of days to wait before expiry of an updated local certificate is requeste
    apcfg_auto_cert_auto_regen_days: int
    # PEM format https CA Certificate.
    apcfg_auto_cert_est_https_ca: str
    # Key type (default = rsa)
    apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"]
    # Key size: 1024, 1536, 2048, 4096 (default 2048).
    apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"]
    # Elliptic curve name: secp256r1, secp384r1 and secp521r1. (default secp256r1).
    apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"]
    # Full DN of the subject (e.g C=US,ST=CA,L=Sunnyvale,O=Fortinet,OU=Dep1,emailAddre
    apcfg_auto_cert_scep_sub_fully_dn: str
    # SCEP server URL.
    apcfg_auto_cert_scep_url: str
    # SCEP server challenge password for auto-regeneration.
    apcfg_auto_cert_scep_password: str
    # CA identifier of the CA server for signing via SCEP.
    apcfg_auto_cert_scep_ca_id: str
    # Subject alternative name (optional, e.g. "DNS:dns1.com,IP:192.168.1.99")
    apcfg_auto_cert_scep_subject_alt_name: str
    # PEM format https CA Certificate.
    apcfg_auto_cert_scep_https_ca: str
    # Enable/disable UNII-4 5Ghz band channels (default = disable).
    unii_4_5ghz_band: Literal["enable", "disable"]
    # Remote authentication server for admin user.
    admin_auth_tacacs_plus: str
    # Enable/disable local admin authentication restriction when remote authenticator 
    admin_restrict_local: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> WtpProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class WtpProfile:
    """
    Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
    
    Path: wireless_controller/wtp_profile
    Category: cmdb
    Primary Key: name
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
    ) -> WtpProfileObject: ...
    
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
    ) -> list[WtpProfileObject]: ...
    
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
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
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
    ) -> WtpProfileObject | list[WtpProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | list[dict[str, Any]] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | list[dict[str, Any]] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | list[dict[str, Any]] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WtpProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | list[dict[str, Any]] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | list[dict[str, Any]] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | list[dict[str, Any]] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | list[dict[str, Any]] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | list[dict[str, Any]] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | list[dict[str, Any]] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | list[dict[str, Any]] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | list[dict[str, Any]] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | list[dict[str, Any]] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | list[dict[str, Any]] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | list[dict[str, Any]] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | list[dict[str, Any]] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WtpProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | list[dict[str, Any]] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | list[dict[str, Any]] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | list[dict[str, Any]] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | list[dict[str, Any]] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | list[dict[str, Any]] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | list[dict[str, Any]] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | list[dict[str, Any]] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | list[dict[str, Any]] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | list[dict[str, Any]] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WtpProfileObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | list[dict[str, Any]] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | list[dict[str, Any]] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | list[dict[str, Any]] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
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
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
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
    "WtpProfile",
    "WtpProfilePayload",
    "WtpProfileObject",
]