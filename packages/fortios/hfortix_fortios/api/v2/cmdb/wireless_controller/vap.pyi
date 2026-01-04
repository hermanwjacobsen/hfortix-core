from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class VapPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/vap payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: VapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Virtual AP name.
    pre_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable pre-authentication, where supported by client
    external_pre_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable pre-authentication with external APs not mana
    mesh_backhaul: NotRequired[Literal["enable", "disable"]]  # Enable/disable using this VAP as a WiFi mesh backhaul (defau
    atf_weight: NotRequired[int]  # Airtime weight in percentage (default = 20).
    max_clients: NotRequired[int]  # Maximum number of clients that can connect simultaneously to
    max_clients_ap: NotRequired[int]  # Maximum number of clients that can connect simultaneously to
    ssid: NotRequired[str]  # IEEE 802.11 service set identifier (SSID) for the wireless i
    broadcast_ssid: NotRequired[Literal["enable", "disable"]]  # Enable/disable broadcasting the SSID (default = enable).
    security: NotRequired[Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"]]  # Security mode for the wireless interface (default = wpa2-onl
    pmf: NotRequired[Literal["disable", "enable", "optional"]]  # Protected Management Frames (PMF) support (default = disable
    pmf_assoc_comeback_timeout: NotRequired[int]  # Protected Management Frames (PMF) comeback maximum timeout (
    pmf_sa_query_retry_timeout: NotRequired[int]  # Protected Management Frames (PMF) SA query retry timeout int
    beacon_protection: NotRequired[Literal["disable", "enable"]]  # Enable/disable beacon protection support (default = disable)
    okc: NotRequired[Literal["disable", "enable"]]  # Enable/disable Opportunistic Key Caching (OKC) (default = en
    mbo: NotRequired[Literal["disable", "enable"]]  # Enable/disable Multiband Operation (default = disable).
    gas_comeback_delay: NotRequired[int]  # GAS comeback delay (0 or 100 - 10000 milliseconds, default =
    gas_fragmentation_limit: NotRequired[int]  # GAS fragmentation limit (512 - 4096, default = 1024).
    mbo_cell_data_conn_pref: NotRequired[Literal["excluded", "prefer-not", "prefer-use"]]  # MBO cell data connection preference (0, 1, or 255, default =
    80211k: NotRequired[Literal["disable", "enable"]]  # Enable/disable 802.11k assisted roaming (default = enable).
    80211v: NotRequired[Literal["disable", "enable"]]  # Enable/disable 802.11v assisted roaming (default = enable).
    neighbor_report_dual_band: NotRequired[Literal["disable", "enable"]]  # Enable/disable dual-band neighbor report (default = disable)
    fast_bss_transition: NotRequired[Literal["disable", "enable"]]  # Enable/disable 802.11r Fast BSS Transition (FT) (default = d
    ft_mobility_domain: NotRequired[int]  # Mobility domain identifier in FT (1 - 65535, default = 1000)
    ft_r0_key_lifetime: NotRequired[int]  # Lifetime of the PMK-R0 key in FT, 1-65535 minutes.
    ft_over_ds: NotRequired[Literal["disable", "enable"]]  # Enable/disable FT over the Distribution System (DS).
    sae_groups: NotRequired[Literal["19", "20", "21"]]  # SAE-Groups.
    owe_groups: NotRequired[Literal["19", "20", "21"]]  # OWE-Groups.
    owe_transition: NotRequired[Literal["disable", "enable"]]  # Enable/disable OWE transition mode support.
    owe_transition_ssid: NotRequired[str]  # OWE transition mode peer SSID.
    additional_akms: NotRequired[Literal["akm6", "akm24"]]  # Additional AKMs.
    eapol_key_retries: NotRequired[Literal["disable", "enable"]]  # Enable/disable retransmission of EAPOL-Key frames (message 3
    tkip_counter_measure: NotRequired[Literal["enable", "disable"]]  # Enable/disable TKIP counter measure.
    external_web: NotRequired[str]  # URL of external authentication web server.
    external_web_format: NotRequired[Literal["auto-detect", "no-query-string", "partial-query-string"]]  # URL query parameter detection (default = auto-detect).
    external_logout: NotRequired[str]  # URL of external authentication logout server.
    mac_username_delimiter: NotRequired[Literal["hyphen", "single-hyphen", "colon", "none"]]  # MAC authentication username delimiter (default = hyphen).
    mac_password_delimiter: NotRequired[Literal["hyphen", "single-hyphen", "colon", "none"]]  # MAC authentication password delimiter (default = hyphen).
    mac_calling_station_delimiter: NotRequired[Literal["hyphen", "single-hyphen", "colon", "none"]]  # MAC calling station delimiter (default = hyphen).
    mac_called_station_delimiter: NotRequired[Literal["hyphen", "single-hyphen", "colon", "none"]]  # MAC called station delimiter (default = hyphen).
    mac_case: NotRequired[Literal["uppercase", "lowercase"]]  # MAC case (default = uppercase).
    called_station_id_type: NotRequired[Literal["mac", "ip", "apname"]]  # The format type of RADIUS attribute Called-Station-Id (defau
    mac_auth_bypass: NotRequired[Literal["enable", "disable"]]  # Enable/disable MAC authentication bypass.
    radius_mac_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable RADIUS-based MAC authentication of clients (d
    radius_mac_auth_server: NotRequired[str]  # RADIUS-based MAC authentication server.
    radius_mac_auth_block_interval: NotRequired[int]  # Don't send RADIUS MAC auth request again if the client has b
    radius_mac_mpsk_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable RADIUS-based MAC authentication of clients fo
    radius_mac_mpsk_timeout: NotRequired[int]  # RADIUS MAC MPSK cache timeout interval (0 or 300 - 864000, d
    radius_mac_auth_usergroups: NotRequired[list[dict[str, Any]]]  # Selective user groups that are permitted for RADIUS mac auth
    auth: NotRequired[Literal["radius", "usergroup"]]  # Authentication protocol.
    encrypt: NotRequired[Literal["TKIP", "AES", "TKIP-AES"]]  # Encryption protocol to use (only available when security is 
    keyindex: NotRequired[int]  # WEP key index (1 - 4).
    key: NotRequired[str]  # WEP Key.
    passphrase: NotRequired[str]  # WPA pre-shared key (PSK) to be used to authenticate WiFi use
    sae_password: NotRequired[str]  # WPA3 SAE password to be used to authenticate WiFi users.
    sae_h2e_only: NotRequired[Literal["enable", "disable"]]  # Use hash-to-element-only mechanism for PWE derivation (defau
    sae_hnp_only: NotRequired[Literal["enable", "disable"]]  # Use hunting-and-pecking-only mechanism for PWE derivation (d
    sae_pk: NotRequired[Literal["enable", "disable"]]  # Enable/disable WPA3 SAE-PK (default = disable).
    sae_private_key: NotRequired[str]  # Private key used for WPA3 SAE-PK authentication.
    akm24_only: NotRequired[Literal["disable", "enable"]]  # WPA3 SAE using group-dependent hash only (default = disable)
    radius_server: NotRequired[str]  # RADIUS server to be used to authenticate WiFi users.
    nas_filter_rule: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAS filter rule support (default = disable).
    domain_name_stripping: NotRequired[Literal["disable", "enable"]]  # Enable/disable stripping domain name from identity (default 
    local_standalone: NotRequired[Literal["enable", "disable"]]  # Enable/disable AP local standalone (default = disable).
    local_standalone_nat: NotRequired[Literal["enable", "disable"]]  # Enable/disable AP local standalone NAT mode.
    ip: NotRequired[str]  # IP address and subnet mask for the local standalone NAT subn
    dhcp_lease_time: NotRequired[int]  # DHCP lease time in seconds for NAT IP address.
    local_standalone_dns: NotRequired[Literal["enable", "disable"]]  # Enable/disable AP local standalone DNS.
    local_standalone_dns_ip: NotRequired[str]  # IPv4 addresses for the local standalone DNS.
    local_lan_partition: NotRequired[Literal["enable", "disable"]]  # Enable/disable segregating client traffic to local LAN side 
    local_bridging: NotRequired[Literal["enable", "disable"]]  # Enable/disable bridging of wireless and Ethernet interfaces 
    local_lan: NotRequired[Literal["allow", "deny"]]  # Allow/deny traffic destined for a Class A, B, or C private I
    local_authentication: NotRequired[Literal["enable", "disable"]]  # Enable/disable AP local authentication.
    usergroup: NotRequired[list[dict[str, Any]]]  # Firewall user group to be used to authenticate WiFi users.
    captive_portal: NotRequired[Literal["enable", "disable"]]  # Enable/disable captive portal.
    captive_network_assistant_bypass: NotRequired[Literal["enable", "disable"]]  # Enable/disable Captive Network Assistant bypass.
    portal_message_override_group: NotRequired[str]  # Replacement message group for this VAP (only available when 
    portal_message_overrides: NotRequired[str]  # Individual message overrides.
    portal_type: NotRequired[Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"]]  # Captive portal functionality. Configure how the captive port
    selected_usergroups: NotRequired[list[dict[str, Any]]]  # Selective user groups that are permitted to authenticate.
    security_exempt_list: NotRequired[str]  # Optional security exempt list for captive portal authenticat
    security_redirect_url: NotRequired[str]  # Optional URL for redirecting users after they pass captive p
    auth_cert: NotRequired[str]  # HTTPS server certificate.
    auth_portal_addr: NotRequired[str]  # Address of captive portal.
    intra_vap_privacy: NotRequired[Literal["enable", "disable"]]  # Enable/disable blocking communication between clients on the
    schedule: NotRequired[list[dict[str, Any]]]  # Firewall schedules for enabling this VAP on the FortiAP. Thi
    ldpc: NotRequired[Literal["disable", "rx", "tx", "rxtx"]]  # VAP low-density parity-check (LDPC) coding configuration.
    high_efficiency: NotRequired[Literal["enable", "disable"]]  # Enable/disable 802.11ax high efficiency (default = enable).
    target_wake_time: NotRequired[Literal["enable", "disable"]]  # Enable/disable 802.11ax target wake time (default = enable).
    port_macauth: NotRequired[Literal["disable", "radius", "address-group"]]  # Enable/disable LAN port MAC authentication (default = disabl
    port_macauth_timeout: NotRequired[int]  # LAN port MAC authentication idle timeout value (default = 60
    port_macauth_reauth_timeout: NotRequired[int]  # LAN port MAC authentication re-authentication timeout value 
    bss_color_partial: NotRequired[Literal["enable", "disable"]]  # Enable/disable 802.11ax partial BSS color (default = enable)
    mpsk_profile: NotRequired[str]  # MPSK profile name.
    split_tunneling: NotRequired[Literal["enable", "disable"]]  # Enable/disable split tunneling (default = disable).
    nac: NotRequired[Literal["enable", "disable"]]  # Enable/disable network access control.
    nac_profile: NotRequired[str]  # NAC profile name.
    vlanid: NotRequired[int]  # Optional VLAN ID.
    vlan_auto: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic management of SSID VLAN interface.
    dynamic_vlan: NotRequired[Literal["enable", "disable"]]  # Enable/disable dynamic VLAN assignment.
    captive_portal_fw_accounting: NotRequired[Literal["enable", "disable"]]  # Enable/disable RADIUS accounting for captive portal firewall
    captive_portal_ac_name: NotRequired[str]  # Local-bridging captive portal ac-name.
    captive_portal_auth_timeout: NotRequired[int]  # Hard timeout - AP will always clear the session after timeou
    multicast_rate: NotRequired[Literal["0", "6000", "12000", "24000"]]  # Multicast rate (0, 6000, 12000, or 24000 kbps, default = 0).
    multicast_enhance: NotRequired[Literal["enable", "disable"]]  # Enable/disable converting multicast to unicast to improve pe
    igmp_snooping: NotRequired[Literal["enable", "disable"]]  # Enable/disable IGMP snooping.
    dhcp_address_enforcement: NotRequired[Literal["enable", "disable"]]  # Enable/disable DHCP address enforcement (default = disable).
    broadcast_suppression: NotRequired[Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"]]  # Optional suppression of broadcast messages. For example, you
    ipv6_rules: NotRequired[Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"]]  # Optional rules of IPv6 packets. For example, you can keep RA
    me_disable_thresh: NotRequired[int]  # Disable multicast enhancement when this many clients are rec
    mu_mimo: NotRequired[Literal["enable", "disable"]]  # Enable/disable Multi-user MIMO (default = enable).
    probe_resp_suppression: NotRequired[Literal["enable", "disable"]]  # Enable/disable probe response suppression (to ignore weak si
    probe_resp_threshold: NotRequired[str]  # Minimum signal level/threshold in dBm required for the AP re
    radio_sensitivity: NotRequired[Literal["enable", "disable"]]  # Enable/disable software radio sensitivity (to ignore weak si
    quarantine: NotRequired[Literal["enable", "disable"]]  # Enable/disable station quarantine (default = enable).
    radio_5g_threshold: NotRequired[str]  # Minimum signal level/threshold in dBm required for the AP re
    radio_2g_threshold: NotRequired[str]  # Minimum signal level/threshold in dBm required for the AP re
    vlan_name: NotRequired[list[dict[str, Any]]]  # Table for mapping VLAN name to VLAN ID.
    vlan_pooling: NotRequired[Literal["wtp-group", "round-robin", "hash", "disable"]]  # Enable/disable VLAN pooling, to allow grouping of multiple w
    vlan_pool: NotRequired[list[dict[str, Any]]]  # VLAN pool.
    dhcp_option43_insertion: NotRequired[Literal["enable", "disable"]]  # Enable/disable insertion of DHCP option 43 (default = enable
    dhcp_option82_insertion: NotRequired[Literal["enable", "disable"]]  # Enable/disable DHCP option 82 insert (default = disable).
    dhcp_option82_circuit_id_insertion: NotRequired[Literal["style-1", "style-2", "style-3", "disable"]]  # Enable/disable DHCP option 82 circuit-id insert (default = d
    dhcp_option82_remote_id_insertion: NotRequired[Literal["style-1", "disable"]]  # Enable/disable DHCP option 82 remote-id insert (default = di
    ptk_rekey: NotRequired[Literal["enable", "disable"]]  # Enable/disable PTK rekey for WPA-Enterprise security.
    ptk_rekey_intv: NotRequired[int]  # PTK rekey interval (600 - 864000 sec, default = 86400).
    gtk_rekey: NotRequired[Literal["enable", "disable"]]  # Enable/disable GTK rekey for WPA security.
    gtk_rekey_intv: NotRequired[int]  # GTK rekey interval (600 - 864000 sec, default = 86400).
    eap_reauth: NotRequired[Literal["enable", "disable"]]  # Enable/disable EAP re-authentication for WPA-Enterprise secu
    eap_reauth_intv: NotRequired[int]  # EAP re-authentication interval (1800 - 864000 sec, default =
    roaming_acct_interim_update: NotRequired[Literal["enable", "disable"]]  # Enable/disable using accounting interim update instead of ac
    qos_profile: NotRequired[str]  # Quality of service profile name.
    hotspot20_profile: NotRequired[str]  # Hotspot 2.0 profile name.
    access_control_list: NotRequired[str]  # Profile name for access-control-list.
    primary_wag_profile: NotRequired[str]  # Primary wireless access gateway profile name.
    secondary_wag_profile: NotRequired[str]  # Secondary wireless access gateway profile name.
    tunnel_echo_interval: NotRequired[int]  # The time interval to send echo to both primary and secondary
    tunnel_fallback_interval: NotRequired[int]  # The time interval for secondary tunnel to fall back to prima
    rates_11a: NotRequired[Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"]]  # Allowed data rates for 802.11a.
    rates_11bg: NotRequired[Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"]]  # Allowed data rates for 802.11b/g.
    rates_11n_ss12: NotRequired[Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"]]  # Allowed data rates for 802.11n with 1 or 2 spatial streams.
    rates_11n_ss34: NotRequired[Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"]]  # Allowed data rates for 802.11n with 3 or 4 spatial streams.
    rates_11ac_mcs_map: NotRequired[str]  # Comma separated list of max supported VHT MCS for spatial st
    rates_11ax_mcs_map: NotRequired[str]  # Comma separated list of max supported HE MCS for spatial str
    rates_11be_mcs_map: NotRequired[str]  # Comma separated list of max nss that supports EHT-MCS 0-9, 1
    rates_11be_mcs_map_160: NotRequired[str]  # Comma separated list of max nss that supports EHT-MCS 0-9, 1
    rates_11be_mcs_map_320: NotRequired[str]  # Comma separated list of max nss that supports EHT-MCS 0-9, 1
    utm_profile: NotRequired[str]  # UTM profile name.
    utm_status: NotRequired[Literal["enable", "disable"]]  # Enable to add one or more security profiles (AV, IPS, etc.) 
    utm_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable UTM logging.
    ips_sensor: NotRequired[str]  # IPS sensor name.
    application_list: NotRequired[str]  # Application control list name.
    antivirus_profile: NotRequired[str]  # AntiVirus profile name.
    webfilter_profile: NotRequired[str]  # WebFilter profile name.
    scan_botnet_connections: NotRequired[Literal["disable", "monitor", "block"]]  # Block or monitor connections to Botnet servers or disable Bo
    address_group: NotRequired[str]  # Firewall Address Group Name.
    address_group_policy: NotRequired[Literal["disable", "allow", "deny"]]  # Configure MAC address filtering policy for MAC addresses tha
    sticky_client_remove: NotRequired[Literal["enable", "disable"]]  # Enable/disable sticky client remove to maintain good signal 
    sticky_client_threshold_5g: NotRequired[str]  # Minimum signal level/threshold in dBm required for the 5G cl
    sticky_client_threshold_2g: NotRequired[str]  # Minimum signal level/threshold in dBm required for the 2G cl
    sticky_client_threshold_6g: NotRequired[str]  # Minimum signal level/threshold in dBm required for the 6G cl
    bstm_rssi_disassoc_timer: NotRequired[int]  # Time interval for client to voluntarily leave AP before forc
    bstm_load_balancing_disassoc_timer: NotRequired[int]  # Time interval for client to voluntarily leave AP before forc
    bstm_disassociation_imminent: NotRequired[Literal["enable", "disable"]]  # Enable/disable forcing of disassociation after the BSTM requ
    beacon_advertising: NotRequired[Literal["name", "model", "serial-number"]]  # Fortinet beacon advertising IE data   (default = empty).
    osen: NotRequired[Literal["enable", "disable"]]  # Enable/disable OSEN as part of key management (default = dis
    application_detection_engine: NotRequired[Literal["enable", "disable"]]  # Enable/disable application detection engine (default = disab
    application_dscp_marking: NotRequired[Literal["enable", "disable"]]  # Enable/disable application attribute based DSCP marking (def
    application_report_intv: NotRequired[int]  # Application report interval (30 - 864000 sec, default = 120)
    l3_roaming: NotRequired[Literal["enable", "disable"]]  # Enable/disable layer 3 roaming (default = disable).
    l3_roaming_mode: NotRequired[Literal["direct", "indirect"]]  # Select the way that layer 3 roaming traffic is passed (defau


class Vap:
    """
    Configure Virtual Access Points (VAPs).
    
    Path: wireless_controller/vap
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
        payload_dict: VapPayload | None = ...,
        name: str | None = ...,
        pre_auth: Literal["enable", "disable"] | None = ...,
        external_pre_auth: Literal["enable", "disable"] | None = ...,
        mesh_backhaul: Literal["enable", "disable"] | None = ...,
        atf_weight: int | None = ...,
        max_clients: int | None = ...,
        max_clients_ap: int | None = ...,
        ssid: str | None = ...,
        broadcast_ssid: Literal["enable", "disable"] | None = ...,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = ...,
        pmf: Literal["disable", "enable", "optional"] | None = ...,
        pmf_assoc_comeback_timeout: int | None = ...,
        pmf_sa_query_retry_timeout: int | None = ...,
        beacon_protection: Literal["disable", "enable"] | None = ...,
        okc: Literal["disable", "enable"] | None = ...,
        mbo: Literal["disable", "enable"] | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = ...,
        80211k: Literal["disable", "enable"] | None = ...,
        80211v: Literal["disable", "enable"] | None = ...,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = ...,
        fast_bss_transition: Literal["disable", "enable"] | None = ...,
        ft_mobility_domain: int | None = ...,
        ft_r0_key_lifetime: int | None = ...,
        ft_over_ds: Literal["disable", "enable"] | None = ...,
        sae_groups: Literal["19", "20", "21"] | None = ...,
        owe_groups: Literal["19", "20", "21"] | None = ...,
        owe_transition: Literal["disable", "enable"] | None = ...,
        owe_transition_ssid: str | None = ...,
        additional_akms: Literal["akm6", "akm24"] | None = ...,
        eapol_key_retries: Literal["disable", "enable"] | None = ...,
        tkip_counter_measure: Literal["enable", "disable"] | None = ...,
        external_web: str | None = ...,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = ...,
        external_logout: str | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = ...,
        mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_mac_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_server: str | None = ...,
        radius_mac_auth_block_interval: int | None = ...,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_mpsk_timeout: int | None = ...,
        radius_mac_auth_usergroups: list[dict[str, Any]] | None = ...,
        auth: Literal["radius", "usergroup"] | None = ...,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = ...,
        keyindex: int | None = ...,
        key: str | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        sae_h2e_only: Literal["enable", "disable"] | None = ...,
        sae_hnp_only: Literal["enable", "disable"] | None = ...,
        sae_pk: Literal["enable", "disable"] | None = ...,
        sae_private_key: str | None = ...,
        akm24_only: Literal["disable", "enable"] | None = ...,
        radius_server: str | None = ...,
        nas_filter_rule: Literal["enable", "disable"] | None = ...,
        domain_name_stripping: Literal["disable", "enable"] | None = ...,
        local_standalone: Literal["enable", "disable"] | None = ...,
        local_standalone_nat: Literal["enable", "disable"] | None = ...,
        ip: str | None = ...,
        dhcp_lease_time: int | None = ...,
        local_standalone_dns: Literal["enable", "disable"] | None = ...,
        local_standalone_dns_ip: str | None = ...,
        local_lan_partition: Literal["enable", "disable"] | None = ...,
        local_bridging: Literal["enable", "disable"] | None = ...,
        local_lan: Literal["allow", "deny"] | None = ...,
        local_authentication: Literal["enable", "disable"] | None = ...,
        usergroup: list[dict[str, Any]] | None = ...,
        captive_portal: Literal["enable", "disable"] | None = ...,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = ...,
        portal_message_override_group: str | None = ...,
        portal_message_overrides: str | None = ...,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = ...,
        selected_usergroups: list[dict[str, Any]] | None = ...,
        security_exempt_list: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        intra_vap_privacy: Literal["enable", "disable"] | None = ...,
        schedule: list[dict[str, Any]] | None = ...,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = ...,
        high_efficiency: Literal["enable", "disable"] | None = ...,
        target_wake_time: Literal["enable", "disable"] | None = ...,
        port_macauth: Literal["disable", "radius", "address-group"] | None = ...,
        port_macauth_timeout: int | None = ...,
        port_macauth_reauth_timeout: int | None = ...,
        bss_color_partial: Literal["enable", "disable"] | None = ...,
        mpsk_profile: str | None = ...,
        split_tunneling: Literal["enable", "disable"] | None = ...,
        nac: Literal["enable", "disable"] | None = ...,
        nac_profile: str | None = ...,
        vlanid: int | None = ...,
        vlan_auto: Literal["enable", "disable"] | None = ...,
        dynamic_vlan: Literal["enable", "disable"] | None = ...,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = ...,
        captive_portal_ac_name: str | None = ...,
        captive_portal_auth_timeout: int | None = ...,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = ...,
        multicast_enhance: Literal["enable", "disable"] | None = ...,
        igmp_snooping: Literal["enable", "disable"] | None = ...,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = ...,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | None = ...,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | None = ...,
        me_disable_thresh: int | None = ...,
        mu_mimo: Literal["enable", "disable"] | None = ...,
        probe_resp_suppression: Literal["enable", "disable"] | None = ...,
        probe_resp_threshold: str | None = ...,
        radio_sensitivity: Literal["enable", "disable"] | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        radio_5g_threshold: str | None = ...,
        radio_2g_threshold: str | None = ...,
        vlan_name: list[dict[str, Any]] | None = ...,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = ...,
        vlan_pool: list[dict[str, Any]] | None = ...,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = ...,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = ...,
        ptk_rekey: Literal["enable", "disable"] | None = ...,
        ptk_rekey_intv: int | None = ...,
        gtk_rekey: Literal["enable", "disable"] | None = ...,
        gtk_rekey_intv: int | None = ...,
        eap_reauth: Literal["enable", "disable"] | None = ...,
        eap_reauth_intv: int | None = ...,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = ...,
        qos_profile: str | None = ...,
        hotspot20_profile: str | None = ...,
        access_control_list: str | None = ...,
        primary_wag_profile: str | None = ...,
        secondary_wag_profile: str | None = ...,
        tunnel_echo_interval: int | None = ...,
        tunnel_fallback_interval: int | None = ...,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | None = ...,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | None = ...,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | None = ...,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | None = ...,
        rates_11ac_mcs_map: str | None = ...,
        rates_11ax_mcs_map: str | None = ...,
        rates_11be_mcs_map: str | None = ...,
        rates_11be_mcs_map_160: str | None = ...,
        rates_11be_mcs_map_320: str | None = ...,
        utm_profile: str | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        address_group: str | None = ...,
        address_group_policy: Literal["disable", "allow", "deny"] | None = ...,
        sticky_client_remove: Literal["enable", "disable"] | None = ...,
        sticky_client_threshold_5g: str | None = ...,
        sticky_client_threshold_2g: str | None = ...,
        sticky_client_threshold_6g: str | None = ...,
        bstm_rssi_disassoc_timer: int | None = ...,
        bstm_load_balancing_disassoc_timer: int | None = ...,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = ...,
        beacon_advertising: Literal["name", "model", "serial-number"] | None = ...,
        osen: Literal["enable", "disable"] | None = ...,
        application_detection_engine: Literal["enable", "disable"] | None = ...,
        application_dscp_marking: Literal["enable", "disable"] | None = ...,
        application_report_intv: int | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        l3_roaming_mode: Literal["direct", "indirect"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: VapPayload | None = ...,
        name: str | None = ...,
        pre_auth: Literal["enable", "disable"] | None = ...,
        external_pre_auth: Literal["enable", "disable"] | None = ...,
        mesh_backhaul: Literal["enable", "disable"] | None = ...,
        atf_weight: int | None = ...,
        max_clients: int | None = ...,
        max_clients_ap: int | None = ...,
        ssid: str | None = ...,
        broadcast_ssid: Literal["enable", "disable"] | None = ...,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = ...,
        pmf: Literal["disable", "enable", "optional"] | None = ...,
        pmf_assoc_comeback_timeout: int | None = ...,
        pmf_sa_query_retry_timeout: int | None = ...,
        beacon_protection: Literal["disable", "enable"] | None = ...,
        okc: Literal["disable", "enable"] | None = ...,
        mbo: Literal["disable", "enable"] | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = ...,
        80211k: Literal["disable", "enable"] | None = ...,
        80211v: Literal["disable", "enable"] | None = ...,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = ...,
        fast_bss_transition: Literal["disable", "enable"] | None = ...,
        ft_mobility_domain: int | None = ...,
        ft_r0_key_lifetime: int | None = ...,
        ft_over_ds: Literal["disable", "enable"] | None = ...,
        sae_groups: Literal["19", "20", "21"] | None = ...,
        owe_groups: Literal["19", "20", "21"] | None = ...,
        owe_transition: Literal["disable", "enable"] | None = ...,
        owe_transition_ssid: str | None = ...,
        additional_akms: Literal["akm6", "akm24"] | None = ...,
        eapol_key_retries: Literal["disable", "enable"] | None = ...,
        tkip_counter_measure: Literal["enable", "disable"] | None = ...,
        external_web: str | None = ...,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = ...,
        external_logout: str | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = ...,
        mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_mac_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_server: str | None = ...,
        radius_mac_auth_block_interval: int | None = ...,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_mpsk_timeout: int | None = ...,
        radius_mac_auth_usergroups: list[dict[str, Any]] | None = ...,
        auth: Literal["radius", "usergroup"] | None = ...,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = ...,
        keyindex: int | None = ...,
        key: str | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        sae_h2e_only: Literal["enable", "disable"] | None = ...,
        sae_hnp_only: Literal["enable", "disable"] | None = ...,
        sae_pk: Literal["enable", "disable"] | None = ...,
        sae_private_key: str | None = ...,
        akm24_only: Literal["disable", "enable"] | None = ...,
        radius_server: str | None = ...,
        nas_filter_rule: Literal["enable", "disable"] | None = ...,
        domain_name_stripping: Literal["disable", "enable"] | None = ...,
        local_standalone: Literal["enable", "disable"] | None = ...,
        local_standalone_nat: Literal["enable", "disable"] | None = ...,
        ip: str | None = ...,
        dhcp_lease_time: int | None = ...,
        local_standalone_dns: Literal["enable", "disable"] | None = ...,
        local_standalone_dns_ip: str | None = ...,
        local_lan_partition: Literal["enable", "disable"] | None = ...,
        local_bridging: Literal["enable", "disable"] | None = ...,
        local_lan: Literal["allow", "deny"] | None = ...,
        local_authentication: Literal["enable", "disable"] | None = ...,
        usergroup: list[dict[str, Any]] | None = ...,
        captive_portal: Literal["enable", "disable"] | None = ...,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = ...,
        portal_message_override_group: str | None = ...,
        portal_message_overrides: str | None = ...,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = ...,
        selected_usergroups: list[dict[str, Any]] | None = ...,
        security_exempt_list: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        intra_vap_privacy: Literal["enable", "disable"] | None = ...,
        schedule: list[dict[str, Any]] | None = ...,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = ...,
        high_efficiency: Literal["enable", "disable"] | None = ...,
        target_wake_time: Literal["enable", "disable"] | None = ...,
        port_macauth: Literal["disable", "radius", "address-group"] | None = ...,
        port_macauth_timeout: int | None = ...,
        port_macauth_reauth_timeout: int | None = ...,
        bss_color_partial: Literal["enable", "disable"] | None = ...,
        mpsk_profile: str | None = ...,
        split_tunneling: Literal["enable", "disable"] | None = ...,
        nac: Literal["enable", "disable"] | None = ...,
        nac_profile: str | None = ...,
        vlanid: int | None = ...,
        vlan_auto: Literal["enable", "disable"] | None = ...,
        dynamic_vlan: Literal["enable", "disable"] | None = ...,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = ...,
        captive_portal_ac_name: str | None = ...,
        captive_portal_auth_timeout: int | None = ...,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = ...,
        multicast_enhance: Literal["enable", "disable"] | None = ...,
        igmp_snooping: Literal["enable", "disable"] | None = ...,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = ...,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | None = ...,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | None = ...,
        me_disable_thresh: int | None = ...,
        mu_mimo: Literal["enable", "disable"] | None = ...,
        probe_resp_suppression: Literal["enable", "disable"] | None = ...,
        probe_resp_threshold: str | None = ...,
        radio_sensitivity: Literal["enable", "disable"] | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        radio_5g_threshold: str | None = ...,
        radio_2g_threshold: str | None = ...,
        vlan_name: list[dict[str, Any]] | None = ...,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = ...,
        vlan_pool: list[dict[str, Any]] | None = ...,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = ...,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = ...,
        ptk_rekey: Literal["enable", "disable"] | None = ...,
        ptk_rekey_intv: int | None = ...,
        gtk_rekey: Literal["enable", "disable"] | None = ...,
        gtk_rekey_intv: int | None = ...,
        eap_reauth: Literal["enable", "disable"] | None = ...,
        eap_reauth_intv: int | None = ...,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = ...,
        qos_profile: str | None = ...,
        hotspot20_profile: str | None = ...,
        access_control_list: str | None = ...,
        primary_wag_profile: str | None = ...,
        secondary_wag_profile: str | None = ...,
        tunnel_echo_interval: int | None = ...,
        tunnel_fallback_interval: int | None = ...,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | None = ...,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | None = ...,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | None = ...,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | None = ...,
        rates_11ac_mcs_map: str | None = ...,
        rates_11ax_mcs_map: str | None = ...,
        rates_11be_mcs_map: str | None = ...,
        rates_11be_mcs_map_160: str | None = ...,
        rates_11be_mcs_map_320: str | None = ...,
        utm_profile: str | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        address_group: str | None = ...,
        address_group_policy: Literal["disable", "allow", "deny"] | None = ...,
        sticky_client_remove: Literal["enable", "disable"] | None = ...,
        sticky_client_threshold_5g: str | None = ...,
        sticky_client_threshold_2g: str | None = ...,
        sticky_client_threshold_6g: str | None = ...,
        bstm_rssi_disassoc_timer: int | None = ...,
        bstm_load_balancing_disassoc_timer: int | None = ...,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = ...,
        beacon_advertising: Literal["name", "model", "serial-number"] | None = ...,
        osen: Literal["enable", "disable"] | None = ...,
        application_detection_engine: Literal["enable", "disable"] | None = ...,
        application_dscp_marking: Literal["enable", "disable"] | None = ...,
        application_report_intv: int | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        l3_roaming_mode: Literal["direct", "indirect"] | None = ...,
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
        payload_dict: VapPayload | None = ...,
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
    "Vap",
    "VapPayload",
]