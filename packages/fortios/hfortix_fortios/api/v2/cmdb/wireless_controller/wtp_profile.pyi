""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: wireless_controller/wtp_profile
Category: cmdb
"""

from __future__ import annotations

from typing import (
    Any,
    ClassVar,
    Literal,
    TypedDict,
    overload,
)

from hfortix_fortios.models import (
    FortiObject,
    FortiObjectList,
)


# ================================================================
# TypedDict Payloads
# ================================================================

class WtpProfileLedschedulesItem:
    """Nested item for led-schedules field - supports attribute access."""
    name: str


class WtpProfileDenymaclistItem:
    """Nested item for deny-mac-list field - supports attribute access."""
    id: int
    mac: str


class WtpProfileSplittunnelingaclItem:
    """Nested item for split-tunneling-acl field - supports attribute access."""
    id: int
    dest_ip: str


class WtpProfilePayload(TypedDict, total=False):
    """Payload type for WtpProfile operations."""
    name: str
    comment: str
    platform: str
    control_message_offload: str | list[str]
    bonjour_profile: str
    apcfg_profile: str
    apcfg_mesh: Literal["enable", "disable"]
    apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"]
    apcfg_mesh_ssid: str
    apcfg_mesh_eth_bridge: Literal["enable", "disable"]
    ble_profile: str
    lw_profile: str
    syslog_profile: str
    wan_port_mode: Literal["wan-lan", "wan-only"]
    lan: str
    energy_efficient_ethernet: Literal["enable", "disable"]
    led_state: Literal["enable", "disable"]
    led_schedules: str | list[str] | list[dict[str, Any]] | list[WtpProfileLedschedulesItem]
    dtls_policy: str | list[str]
    dtls_in_kernel: Literal["enable", "disable"]
    max_clients: int
    handoff_rssi: int
    handoff_sta_thresh: int
    handoff_roaming: Literal["enable", "disable"]
    deny_mac_list: str | list[str] | list[dict[str, Any]] | list[WtpProfileDenymaclistItem]
    ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"]
    ip_fragment_preventing: str | list[str]
    tun_mtu_uplink: int
    tun_mtu_downlink: int
    split_tunneling_acl_path: Literal["tunnel", "local"]
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]
    split_tunneling_acl: str | list[str] | list[dict[str, Any]] | list[WtpProfileSplittunnelingaclItem]
    allowaccess: str | list[str]
    login_passwd_change: Literal["yes", "default", "no"]
    login_passwd: str
    lldp: Literal["enable", "disable"]
    poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"]
    usb_port: Literal["enable", "disable"]
    frequency_handoff: Literal["enable", "disable"]
    ap_handoff: Literal["enable", "disable"]
    default_mesh_root: Literal["enable", "disable"]
    radio_1: str
    radio_2: str
    radio_3: str
    radio_4: str
    lbs: str
    ext_info_enable: Literal["enable", "disable"]
    indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"]
    esl_ses_dongle: str
    console_login: Literal["enable", "disable"]
    wan_port_auth: Literal["none", "802.1x"]
    wan_port_auth_usrname: str
    wan_port_auth_password: str
    wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"]
    wan_port_auth_macsec: Literal["enable", "disable"]
    apcfg_auto_cert: Literal["enable", "disable"]
    apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"]
    apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"]
    apcfg_auto_cert_est_server: str
    apcfg_auto_cert_est_ca_id: str
    apcfg_auto_cert_est_http_username: str
    apcfg_auto_cert_est_http_password: str
    apcfg_auto_cert_est_subject: str
    apcfg_auto_cert_est_subject_alt_name: str
    apcfg_auto_cert_auto_regen_days: int
    apcfg_auto_cert_est_https_ca: str
    apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"]
    apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"]
    apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"]
    apcfg_auto_cert_scep_sub_fully_dn: str
    apcfg_auto_cert_scep_url: str
    apcfg_auto_cert_scep_password: str
    apcfg_auto_cert_scep_ca_id: str
    apcfg_auto_cert_scep_subject_alt_name: str
    apcfg_auto_cert_scep_https_ca: str
    unii_4_5ghz_band: Literal["enable", "disable"]
    admin_auth_tacacs_plus: str
    admin_restrict_local: Literal["enable", "disable"]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class WtpProfileResponse(TypedDict, total=False):
    """Response type for WtpProfile - use with .dict property for typed dict access."""
    name: str
    comment: str
    platform: str
    control_message_offload: str
    bonjour_profile: str
    apcfg_profile: str
    apcfg_mesh: Literal["enable", "disable"]
    apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"]
    apcfg_mesh_ssid: str
    apcfg_mesh_eth_bridge: Literal["enable", "disable"]
    ble_profile: str
    lw_profile: str
    syslog_profile: str
    wan_port_mode: Literal["wan-lan", "wan-only"]
    lan: str
    energy_efficient_ethernet: Literal["enable", "disable"]
    led_state: Literal["enable", "disable"]
    led_schedules: list[WtpProfileLedschedulesItem]
    dtls_policy: str
    dtls_in_kernel: Literal["enable", "disable"]
    max_clients: int
    handoff_rssi: int
    handoff_sta_thresh: int
    handoff_roaming: Literal["enable", "disable"]
    deny_mac_list: list[WtpProfileDenymaclistItem]
    ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"]
    ip_fragment_preventing: str
    tun_mtu_uplink: int
    tun_mtu_downlink: int
    split_tunneling_acl_path: Literal["tunnel", "local"]
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]
    split_tunneling_acl: list[WtpProfileSplittunnelingaclItem]
    allowaccess: str
    login_passwd_change: Literal["yes", "default", "no"]
    login_passwd: str
    lldp: Literal["enable", "disable"]
    poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"]
    usb_port: Literal["enable", "disable"]
    frequency_handoff: Literal["enable", "disable"]
    ap_handoff: Literal["enable", "disable"]
    default_mesh_root: Literal["enable", "disable"]
    radio_1: str
    radio_2: str
    radio_3: str
    radio_4: str
    lbs: str
    ext_info_enable: Literal["enable", "disable"]
    indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"]
    esl_ses_dongle: str
    console_login: Literal["enable", "disable"]
    wan_port_auth: Literal["none", "802.1x"]
    wan_port_auth_usrname: str
    wan_port_auth_password: str
    wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"]
    wan_port_auth_macsec: Literal["enable", "disable"]
    apcfg_auto_cert: Literal["enable", "disable"]
    apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"]
    apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"]
    apcfg_auto_cert_est_server: str
    apcfg_auto_cert_est_ca_id: str
    apcfg_auto_cert_est_http_username: str
    apcfg_auto_cert_est_http_password: str
    apcfg_auto_cert_est_subject: str
    apcfg_auto_cert_est_subject_alt_name: str
    apcfg_auto_cert_auto_regen_days: int
    apcfg_auto_cert_est_https_ca: str
    apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"]
    apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"]
    apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"]
    apcfg_auto_cert_scep_sub_fully_dn: str
    apcfg_auto_cert_scep_url: str
    apcfg_auto_cert_scep_password: str
    apcfg_auto_cert_scep_ca_id: str
    apcfg_auto_cert_scep_subject_alt_name: str
    apcfg_auto_cert_scep_https_ca: str
    unii_4_5ghz_band: Literal["enable", "disable"]
    admin_auth_tacacs_plus: str
    admin_restrict_local: Literal["enable", "disable"]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class WtpProfileObject(FortiObject):
    """Typed FortiObject for WtpProfile with field access."""
    name: str
    comment: str
    platform: str
    control_message_offload: str
    bonjour_profile: str
    apcfg_profile: str
    apcfg_mesh: Literal["enable", "disable"]
    apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"]
    apcfg_mesh_ssid: str
    apcfg_mesh_eth_bridge: Literal["enable", "disable"]
    ble_profile: str
    lw_profile: str
    syslog_profile: str
    wan_port_mode: Literal["wan-lan", "wan-only"]
    lan: str
    energy_efficient_ethernet: Literal["enable", "disable"]
    led_state: Literal["enable", "disable"]
    led_schedules: list[WtpProfileLedschedulesItem]
    dtls_policy: str
    dtls_in_kernel: Literal["enable", "disable"]
    max_clients: int
    handoff_rssi: int
    handoff_sta_thresh: int
    handoff_roaming: Literal["enable", "disable"]
    deny_mac_list: list[WtpProfileDenymaclistItem]
    ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"]
    ip_fragment_preventing: str
    tun_mtu_uplink: int
    tun_mtu_downlink: int
    split_tunneling_acl_path: Literal["tunnel", "local"]
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]
    split_tunneling_acl: list[WtpProfileSplittunnelingaclItem]
    allowaccess: str
    login_passwd_change: Literal["yes", "default", "no"]
    login_passwd: str
    lldp: Literal["enable", "disable"]
    poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"]
    usb_port: Literal["enable", "disable"]
    frequency_handoff: Literal["enable", "disable"]
    ap_handoff: Literal["enable", "disable"]
    default_mesh_root: Literal["enable", "disable"]
    radio_1: str
    radio_2: str
    radio_3: str
    radio_4: str
    lbs: str
    ext_info_enable: Literal["enable", "disable"]
    indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"]
    esl_ses_dongle: str
    console_login: Literal["enable", "disable"]
    wan_port_auth: Literal["none", "802.1x"]
    wan_port_auth_usrname: str
    wan_port_auth_password: str
    wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"]
    wan_port_auth_macsec: Literal["enable", "disable"]
    apcfg_auto_cert: Literal["enable", "disable"]
    apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"]
    apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"]
    apcfg_auto_cert_est_server: str
    apcfg_auto_cert_est_ca_id: str
    apcfg_auto_cert_est_http_username: str
    apcfg_auto_cert_est_http_password: str
    apcfg_auto_cert_est_subject: str
    apcfg_auto_cert_est_subject_alt_name: str
    apcfg_auto_cert_auto_regen_days: int
    apcfg_auto_cert_est_https_ca: str
    apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"]
    apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"]
    apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"]
    apcfg_auto_cert_scep_sub_fully_dn: str
    apcfg_auto_cert_scep_url: str
    apcfg_auto_cert_scep_password: str
    apcfg_auto_cert_scep_ca_id: str
    apcfg_auto_cert_scep_subject_alt_name: str
    apcfg_auto_cert_scep_https_ca: str
    unii_4_5ghz_band: Literal["enable", "disable"]
    admin_auth_tacacs_plus: str
    admin_restrict_local: Literal["enable", "disable"]


# ================================================================
# Main Endpoint Class
# ================================================================

class WtpProfile:
    """
    
    Endpoint: wireless_controller/wtp_profile
    Category: cmdb
    MKey: name
    """
    
    # Class attributes for introspection
    endpoint: ClassVar[str] = ...
    path: ClassVar[str] = ...
    category: ClassVar[str] = ...
    mkey: ClassVar[str] = ...
    capabilities: ClassVar[dict[str, Any]] = ...
    
    def __init__(self, client: Any) -> None:
        """Initialize endpoint with HTTP client."""
        ...
    
    # ================================================================
    # GET Methods
    # ================================================================
    
    # CMDB with mkey - overloads for single vs list returns
    @overload
    def get(
        self,
        name: str,
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> WtpProfileObject: ...
    
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObjectList[WtpProfileObject]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...

    # ================================================================
    # POST Method
    # ================================================================
    
    def post(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: str | list[str] | None = ...,
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
        led_schedules: str | list[str] | list[dict[str, Any]] | list[WtpProfileLedschedulesItem] | None = ...,
        dtls_policy: str | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | list[WtpProfileDenymaclistItem] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: str | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | list[WtpProfileSplittunnelingaclItem] | None = ...,
        allowaccess: str | list[str] | None = ...,
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> WtpProfileObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: str | list[str] | None = ...,
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
        led_schedules: str | list[str] | list[dict[str, Any]] | list[WtpProfileLedschedulesItem] | None = ...,
        dtls_policy: str | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | list[WtpProfileDenymaclistItem] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: str | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | list[WtpProfileSplittunnelingaclItem] | None = ...,
        allowaccess: str | list[str] | None = ...,
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> WtpProfileObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
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
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
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
        led_schedules: str | list[str] | list[dict[str, Any]] | list[WtpProfileLedschedulesItem] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | list[WtpProfileDenymaclistItem] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | list[WtpProfileSplittunnelingaclItem] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
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
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> list[str] | list[dict[str, Any]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


__all__ = [
    "WtpProfile",
    "WtpProfilePayload",
    "WtpProfileResponse",
    "WtpProfileObject",
]