from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SettingsPayload(TypedDict, total=False):
    """
    Type hints for system/settings payload fields.
    
    Configure VDOM settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: device, dhcp-proxy-interface)

    **Usage:**
        payload: SettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    comments: NotRequired[str]  # VDOM comments.
    vdom_type: Literal["traffic", "lan-extension", "admin"]  # Vdom type (traffic, lan-extension or admin).
    lan_extension_controller_addr: NotRequired[str]  # Controller IP address or FQDN to connect.
    lan_extension_controller_port: NotRequired[int]  # Controller port to connect.
    opmode: Literal["nat", "transparent"]  # Firewall operation mode (NAT or Transparent).
    ngfw_mode: NotRequired[Literal["profile-based", "policy-based"]]  # Next Generation Firewall (NGFW) mode.
    http_external_dest: NotRequired[Literal["fortiweb", "forticache"]]  # Offload HTTP traffic to FortiWeb or FortiCache.
    firewall_session_dirty: NotRequired[Literal["check-all", "check-new", "check-policy-option"]]  # Select how to manage sessions affected by firewall policy co
    manageip: str  # Transparent mode IPv4 management IP address and netmask.
    gateway: NotRequired[str]  # Transparent mode IPv4 default gateway IP address.
    ip: str  # IP address and netmask.
    manageip6: NotRequired[str]  # Transparent mode IPv6 management IP address and netmask.
    gateway6: NotRequired[str]  # Transparent mode IPv6 default gateway IP address.
    ip6: NotRequired[str]  # IPv6 address prefix for NAT mode.
    device: str  # Interface to use for management access for NAT mode.
    bfd: NotRequired[Literal["enable", "disable"]]  # Enable/disable Bi-directional Forwarding Detection (BFD) on
    bfd_desired_min_tx: NotRequired[int]  # BFD desired minimal transmit interval
    bfd_required_min_rx: NotRequired[int]  # BFD required minimal receive interval
    bfd_detect_mult: NotRequired[int]  # BFD detection multiplier (1 - 50, default = 3).
    bfd_dont_enforce_src_port: NotRequired[Literal["enable", "disable"]]  # Enable to not enforce verifying the source port of BFD Packe
    utf8_spam_tagging: NotRequired[Literal["enable", "disable"]]  # Enable/disable converting antispam tags to UTF-8 for better
    wccp_cache_engine: NotRequired[Literal["enable", "disable"]]  # Enable/disable WCCP cache engine.
    vpn_stats_log: NotRequired[Literal["ipsec", "pptp", "l2tp", "ssl"]]  # Enable/disable periodic VPN log statistics for one or more t
    vpn_stats_period: NotRequired[int]  # Period to send VPN log statistics (0 or 60 - 86400 sec).
    v4_ecmp_mode: NotRequired[Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"]]  # IPv4 Equal-cost multi-path (ECMP) routing and load balancing
    mac_ttl: NotRequired[int]  # Duration of MAC addresses in Transparent mode
    fw_session_hairpin: NotRequired[Literal["enable", "disable"]]  # Enable/disable checking for a matching policy each time hair
    prp_trailer_action: NotRequired[Literal["enable", "disable"]]  # Enable/disable action to take on PRP trailer.
    snat_hairpin_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable source NAT (SNAT) for VIP hairpin traffic.
    dhcp_proxy: NotRequired[Literal["enable", "disable"]]  # Enable/disable the DHCP Proxy.
    dhcp_proxy_interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    dhcp_proxy_interface: str  # Specify outgoing interface to reach server.
    dhcp_proxy_vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    dhcp_server_ip: NotRequired[list[dict[str, Any]]]  # DHCP Server IPv4 address.
    dhcp6_server_ip: NotRequired[list[dict[str, Any]]]  # DHCPv6 server IPv6 address.
    central_nat: NotRequired[Literal["enable", "disable"]]  # Enable/disable central NAT.
    gui_default_policy_columns: NotRequired[list[dict[str, Any]]]  # Default columns to display for policy lists on GUI.
    lldp_reception: NotRequired[Literal["enable", "disable", "global"]]  # Enable/disable Link Layer Discovery Protocol (LLDP) receptio
    lldp_transmission: NotRequired[Literal["enable", "disable", "global"]]  # Enable/disable Link Layer Discovery Protocol (LLDP) transmis
    link_down_access: NotRequired[Literal["enable", "disable"]]  # Enable/disable link down access traffic.
    nat46_generate_ipv6_fragment_header: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT46 IPv6 fragment header generation.
    nat46_force_ipv4_packet_forwarding: NotRequired[Literal["enable", "disable"]]  # Enable/disable mandatory IPv4 packet forwarding in NAT46.
    nat64_force_ipv6_packet_forwarding: NotRequired[Literal["enable", "disable"]]  # Enable/disable mandatory IPv6 packet forwarding in NAT64.
    detect_unknown_esp: NotRequired[Literal["enable", "disable"]]  # Enable/disable detection of unknown ESP packets
    intree_ses_best_route: NotRequired[Literal["force", "disable"]]  # Force the intree session to always use the best route.
    auxiliary_session: NotRequired[Literal["enable", "disable"]]  # Enable/disable auxiliary session.
    asymroute: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPv4 asymmetric routing.
    asymroute_icmp: NotRequired[Literal["enable", "disable"]]  # Enable/disable ICMP asymmetric routing.
    tcp_session_without_syn: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowing TCP session without SYN flags.
    ses_denied_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable including denied session in the session table
    ses_denied_multicast_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable including denied multicast session in the ses
    strict_src_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable strict source verification.
    allow_linkdown_path: NotRequired[Literal["enable", "disable"]]  # Enable/disable link down path.
    asymroute6: NotRequired[Literal["enable", "disable"]]  # Enable/disable asymmetric IPv6 routing.
    asymroute6_icmp: NotRequired[Literal["enable", "disable"]]  # Enable/disable asymmetric ICMPv6 routing.
    sctp_session_without_init: NotRequired[Literal["enable", "disable"]]  # Enable/disable SCTP session creation without SCTP INIT.
    sip_expectation: NotRequired[Literal["enable", "disable"]]  # Enable/disable the SIP kernel session helper to create an ex
    sip_nat_trace: NotRequired[Literal["enable", "disable"]]  # Enable/disable recording the original SIP source IP address
    h323_direct_model: NotRequired[Literal["disable", "enable"]]  # Enable/disable H323 direct model.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this VDOM.
    sip_tcp_port: NotRequired[int]  # TCP port the SIP proxy monitors for SIP traffic
    sip_udp_port: NotRequired[int]  # UDP port the SIP proxy monitors for SIP traffic
    sip_ssl_port: NotRequired[int]  # TCP port the SIP proxy monitors for SIP SSL/TLS traffic
    sccp_port: NotRequired[int]  # TCP port the SCCP proxy monitors for SCCP traffic
    multicast_forward: NotRequired[Literal["enable", "disable"]]  # Enable/disable multicast forwarding.
    multicast_ttl_notchange: NotRequired[Literal["enable", "disable"]]  # Enable/disable preventing the FortiGate from changing the TT
    multicast_skip_policy: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowing multicast traffic through the FortiG
    allow_subnet_overlap: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowing interface subnets to use overlapping
    deny_tcp_with_icmp: NotRequired[Literal["enable", "disable"]]  # Enable/disable denying TCP by sending an ICMP communication
    ecmp_max_paths: NotRequired[int]  # Maximum number of Equal Cost Multi-Path (ECMP) next-hops. Se
    discovered_device_timeout: NotRequired[int]  # Timeout for discovered devices (1 - 365 days, default = 28).
    email_portal_check_dns: NotRequired[Literal["disable", "enable"]]  # Enable/disable using DNS to validate email addresses collect
    default_voip_alg_mode: NotRequired[Literal["proxy-based", "kernel-helper-based"]]  # Configure how the FortiGate handles VoIP traffic when a poli
    gui_icap: NotRequired[Literal["enable", "disable"]]  # Enable/disable ICAP on the GUI.
    gui_implicit_policy: NotRequired[Literal["enable", "disable"]]  # Enable/disable implicit firewall policies on the GUI.
    gui_dns_database: NotRequired[Literal["enable", "disable"]]  # Enable/disable DNS database settings on the GUI.
    gui_load_balance: NotRequired[Literal["enable", "disable"]]  # Enable/disable server load balancing on the GUI.
    gui_multicast_policy: NotRequired[Literal["enable", "disable"]]  # Enable/disable multicast firewall policies on the GUI.
    gui_dos_policy: NotRequired[Literal["enable", "disable"]]  # Enable/disable DoS policies on the GUI.
    gui_object_colors: NotRequired[Literal["enable", "disable"]]  # Enable/disable object colors on the GUI.
    gui_route_tag_address_creation: NotRequired[Literal["enable", "disable"]]  # Enable/disable route-tag addresses on the GUI.
    gui_voip_profile: NotRequired[Literal["enable", "disable"]]  # Enable/disable VoIP profiles on the GUI.
    gui_ap_profile: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiAP profiles on the GUI.
    gui_security_profile_group: NotRequired[Literal["enable", "disable"]]  # Enable/disable Security Profile Groups on the GUI.
    gui_local_in_policy: NotRequired[Literal["enable", "disable"]]  # Enable/disable Local-In policies on the GUI.
    gui_wanopt_cache: NotRequired[Literal["enable", "disable"]]  # Enable/disable WAN Optimization and Web Caching on the GUI.
    gui_explicit_proxy: NotRequired[Literal["enable", "disable"]]  # Enable/disable the explicit proxy on the GUI.
    gui_dynamic_routing: NotRequired[Literal["enable", "disable"]]  # Enable/disable dynamic routing on the GUI.
    gui_sslvpn_personal_bookmarks: NotRequired[Literal["enable", "disable"]]  # Enable/disable SSL-VPN personal bookmark management on the G
    gui_sslvpn_realms: NotRequired[Literal["enable", "disable"]]  # Enable/disable SSL-VPN realms on the GUI.
    gui_policy_based_ipsec: NotRequired[Literal["enable", "disable"]]  # Enable/disable policy-based IPsec VPN on the GUI.
    gui_threat_weight: NotRequired[Literal["enable", "disable"]]  # Enable/disable threat weight on the GUI.
    gui_spamfilter: NotRequired[Literal["enable", "disable"]]  # Enable/disable Antispam on the GUI.
    gui_file_filter: NotRequired[Literal["enable", "disable"]]  # Enable/disable File-filter on the GUI.
    gui_application_control: NotRequired[Literal["enable", "disable"]]  # Enable/disable application control on the GUI.
    gui_ips: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPS on the GUI.
    gui_dhcp_advanced: NotRequired[Literal["enable", "disable"]]  # Enable/disable advanced DHCP options on the GUI.
    gui_vpn: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPsec VPN settings pages on the GUI.
    gui_sslvpn: NotRequired[Literal["enable", "disable"]]  # Enable/disable SSL-VPN settings pages on the GUI.
    gui_wireless_controller: NotRequired[Literal["enable", "disable"]]  # Enable/disable the wireless controller on the GUI.
    gui_advanced_wireless_features: NotRequired[Literal["enable", "disable"]]  # Enable/disable advanced wireless features in GUI.
    gui_switch_controller: NotRequired[Literal["enable", "disable"]]  # Enable/disable the switch controller on the GUI.
    gui_fortiap_split_tunneling: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiAP split tunneling on the GUI.
    gui_webfilter_advanced: NotRequired[Literal["enable", "disable"]]  # Enable/disable advanced web filtering on the GUI.
    gui_traffic_shaping: NotRequired[Literal["enable", "disable"]]  # Enable/disable traffic shaping on the GUI.
    gui_wan_load_balancing: NotRequired[Literal["enable", "disable"]]  # Enable/disable SD-WAN on the GUI.
    gui_antivirus: NotRequired[Literal["enable", "disable"]]  # Enable/disable AntiVirus on the GUI.
    gui_webfilter: NotRequired[Literal["enable", "disable"]]  # Enable/disable Web filtering on the GUI.
    gui_videofilter: NotRequired[Literal["enable", "disable"]]  # Enable/disable Video filtering on the GUI.
    gui_dnsfilter: NotRequired[Literal["enable", "disable"]]  # Enable/disable DNS Filtering on the GUI.
    gui_waf_profile: NotRequired[Literal["enable", "disable"]]  # Enable/disable Web Application Firewall on the GUI.
    gui_dlp_profile: NotRequired[Literal["enable", "disable"]]  # Enable/disable Data Loss Prevention on the GUI.
    gui_dlp_advanced: NotRequired[Literal["enable", "disable"]]  # Enable/disable Show advanced DLP expressions on the GUI.
    gui_virtual_patch_profile: NotRequired[Literal["enable", "disable"]]  # Enable/disable Virtual Patching on the GUI.
    gui_casb: NotRequired[Literal["enable", "disable"]]  # Enable/disable Inline-CASB on the GUI.
    gui_fortiextender_controller: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiExtender on the GUI.
    gui_advanced_policy: NotRequired[Literal["enable", "disable"]]  # Enable/disable advanced policy configuration on the GUI.
    gui_allow_unnamed_policy: NotRequired[Literal["enable", "disable"]]  # Enable/disable the requirement for policy naming on the GUI.
    gui_email_collection: NotRequired[Literal["enable", "disable"]]  # Enable/disable email collection on the GUI.
    gui_multiple_interface_policy: NotRequired[Literal["enable", "disable"]]  # Enable/disable adding multiple interfaces to a policy on the
    gui_policy_disclaimer: NotRequired[Literal["enable", "disable"]]  # Enable/disable policy disclaimer on the GUI.
    gui_ztna: NotRequired[Literal["enable", "disable"]]  # Enable/disable Zero Trust Network Access features on the GUI
    gui_ot: NotRequired[Literal["enable", "disable"]]  # Enable/disable Operational technology features on the GUI.
    gui_dynamic_device_os_id: NotRequired[Literal["enable", "disable"]]  # Enable/disable Create dynamic addresses to manage known devi
    gui_gtp: NotRequired[Literal["enable", "disable"]]  # Enable/disable Manage general radio packet service (GPRS) pr
    location_id: NotRequired[str]  # Local location ID in the form of an IPv4 address.
    ike_session_resume: NotRequired[Literal["enable", "disable"]]  # Enable/disable IKEv2 session resumption (RFC 5723).
    ike_quick_crash_detect: NotRequired[Literal["enable", "disable"]]  # Enable/disable IKE quick crash detection (RFC 6290).
    ike_dn_format: NotRequired[Literal["with-space", "no-space"]]  # Configure IKE ASN.1 Distinguished Name format conventions.
    ike_port: NotRequired[int]  # UDP port for IKE/IPsec traffic (default 500).
    ike_tcp_port: NotRequired[int]  # TCP port for IKE/IPsec traffic (default 443).
    ike_policy_route: NotRequired[Literal["enable", "disable"]]  # Enable/disable IKE Policy Based Routing (PBR).
    ike_detailed_event_logs: NotRequired[Literal["disable", "enable"]]  # Enable/disable detail log for IKE events.
    block_land_attack: NotRequired[Literal["disable", "enable"]]  # Enable/disable blocking of land attacks.
    default_app_port_as_service: NotRequired[Literal["enable", "disable"]]  # Enable/disable policy service enforcement based on applicati
    fqdn_session_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable dirty session check caused by FQDN updates.
    ext_resource_session_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable dirty session check caused by external resour
    dyn_addr_session_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable dirty session check caused by dynamic address
    default_policy_expiry_days: NotRequired[int]  # Default policy expiry in days (0 - 365 days, default = 30).
    gui_enforce_change_summary: NotRequired[Literal["disable", "require", "optional"]]  # Enforce change summaries for select tables in the GUI.
    internet_service_database_cache: NotRequired[Literal["disable", "enable"]]  # Enable/disable Internet Service database caching.
    internet_service_app_ctrl_size: NotRequired[int]  # Maximum number of tuple entries

# Nested classes for table field children

@final
class SettingsGuidefaultpolicycolumnsObject:
    """Typed object for gui-default-policy-columns table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Select column name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SettingsResponse(TypedDict):
    """
    Type hints for system/settings API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    comments: str
    vdom_type: Literal["traffic", "lan-extension", "admin"]
    lan_extension_controller_addr: str
    lan_extension_controller_port: int
    opmode: Literal["nat", "transparent"]
    ngfw_mode: Literal["profile-based", "policy-based"]
    http_external_dest: Literal["fortiweb", "forticache"]
    firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"]
    manageip: str
    gateway: str
    ip: str
    manageip6: str
    gateway6: str
    ip6: str
    device: str
    bfd: Literal["enable", "disable"]
    bfd_desired_min_tx: int
    bfd_required_min_rx: int
    bfd_detect_mult: int
    bfd_dont_enforce_src_port: Literal["enable", "disable"]
    utf8_spam_tagging: Literal["enable", "disable"]
    wccp_cache_engine: Literal["enable", "disable"]
    vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"]
    vpn_stats_period: int
    v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"]
    mac_ttl: int
    fw_session_hairpin: Literal["enable", "disable"]
    prp_trailer_action: Literal["enable", "disable"]
    snat_hairpin_traffic: Literal["enable", "disable"]
    dhcp_proxy: Literal["enable", "disable"]
    dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"]
    dhcp_proxy_interface: str
    dhcp_proxy_vrf_select: int
    dhcp_server_ip: list[dict[str, Any]]
    dhcp6_server_ip: list[dict[str, Any]]
    central_nat: Literal["enable", "disable"]
    gui_default_policy_columns: list[dict[str, Any]]
    lldp_reception: Literal["enable", "disable", "global"]
    lldp_transmission: Literal["enable", "disable", "global"]
    link_down_access: Literal["enable", "disable"]
    nat46_generate_ipv6_fragment_header: Literal["enable", "disable"]
    nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"]
    nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"]
    detect_unknown_esp: Literal["enable", "disable"]
    intree_ses_best_route: Literal["force", "disable"]
    auxiliary_session: Literal["enable", "disable"]
    asymroute: Literal["enable", "disable"]
    asymroute_icmp: Literal["enable", "disable"]
    tcp_session_without_syn: Literal["enable", "disable"]
    ses_denied_traffic: Literal["enable", "disable"]
    ses_denied_multicast_traffic: Literal["enable", "disable"]
    strict_src_check: Literal["enable", "disable"]
    allow_linkdown_path: Literal["enable", "disable"]
    asymroute6: Literal["enable", "disable"]
    asymroute6_icmp: Literal["enable", "disable"]
    sctp_session_without_init: Literal["enable", "disable"]
    sip_expectation: Literal["enable", "disable"]
    sip_nat_trace: Literal["enable", "disable"]
    h323_direct_model: Literal["disable", "enable"]
    status: Literal["enable", "disable"]
    sip_tcp_port: int
    sip_udp_port: int
    sip_ssl_port: int
    sccp_port: int
    multicast_forward: Literal["enable", "disable"]
    multicast_ttl_notchange: Literal["enable", "disable"]
    multicast_skip_policy: Literal["enable", "disable"]
    allow_subnet_overlap: Literal["enable", "disable"]
    deny_tcp_with_icmp: Literal["enable", "disable"]
    ecmp_max_paths: int
    discovered_device_timeout: int
    email_portal_check_dns: Literal["disable", "enable"]
    default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"]
    gui_icap: Literal["enable", "disable"]
    gui_implicit_policy: Literal["enable", "disable"]
    gui_dns_database: Literal["enable", "disable"]
    gui_load_balance: Literal["enable", "disable"]
    gui_multicast_policy: Literal["enable", "disable"]
    gui_dos_policy: Literal["enable", "disable"]
    gui_object_colors: Literal["enable", "disable"]
    gui_route_tag_address_creation: Literal["enable", "disable"]
    gui_voip_profile: Literal["enable", "disable"]
    gui_ap_profile: Literal["enable", "disable"]
    gui_security_profile_group: Literal["enable", "disable"]
    gui_local_in_policy: Literal["enable", "disable"]
    gui_wanopt_cache: Literal["enable", "disable"]
    gui_explicit_proxy: Literal["enable", "disable"]
    gui_dynamic_routing: Literal["enable", "disable"]
    gui_sslvpn_personal_bookmarks: Literal["enable", "disable"]
    gui_sslvpn_realms: Literal["enable", "disable"]
    gui_policy_based_ipsec: Literal["enable", "disable"]
    gui_threat_weight: Literal["enable", "disable"]
    gui_spamfilter: Literal["enable", "disable"]
    gui_file_filter: Literal["enable", "disable"]
    gui_application_control: Literal["enable", "disable"]
    gui_ips: Literal["enable", "disable"]
    gui_dhcp_advanced: Literal["enable", "disable"]
    gui_vpn: Literal["enable", "disable"]
    gui_sslvpn: Literal["enable", "disable"]
    gui_wireless_controller: Literal["enable", "disable"]
    gui_advanced_wireless_features: Literal["enable", "disable"]
    gui_switch_controller: Literal["enable", "disable"]
    gui_fortiap_split_tunneling: Literal["enable", "disable"]
    gui_webfilter_advanced: Literal["enable", "disable"]
    gui_traffic_shaping: Literal["enable", "disable"]
    gui_wan_load_balancing: Literal["enable", "disable"]
    gui_antivirus: Literal["enable", "disable"]
    gui_webfilter: Literal["enable", "disable"]
    gui_videofilter: Literal["enable", "disable"]
    gui_dnsfilter: Literal["enable", "disable"]
    gui_waf_profile: Literal["enable", "disable"]
    gui_dlp_profile: Literal["enable", "disable"]
    gui_dlp_advanced: Literal["enable", "disable"]
    gui_virtual_patch_profile: Literal["enable", "disable"]
    gui_casb: Literal["enable", "disable"]
    gui_fortiextender_controller: Literal["enable", "disable"]
    gui_advanced_policy: Literal["enable", "disable"]
    gui_allow_unnamed_policy: Literal["enable", "disable"]
    gui_email_collection: Literal["enable", "disable"]
    gui_multiple_interface_policy: Literal["enable", "disable"]
    gui_policy_disclaimer: Literal["enable", "disable"]
    gui_ztna: Literal["enable", "disable"]
    gui_ot: Literal["enable", "disable"]
    gui_dynamic_device_os_id: Literal["enable", "disable"]
    gui_gtp: Literal["enable", "disable"]
    location_id: str
    ike_session_resume: Literal["enable", "disable"]
    ike_quick_crash_detect: Literal["enable", "disable"]
    ike_dn_format: Literal["with-space", "no-space"]
    ike_port: int
    ike_tcp_port: int
    ike_policy_route: Literal["enable", "disable"]
    ike_detailed_event_logs: Literal["disable", "enable"]
    block_land_attack: Literal["disable", "enable"]
    default_app_port_as_service: Literal["enable", "disable"]
    fqdn_session_check: Literal["enable", "disable"]
    ext_resource_session_check: Literal["enable", "disable"]
    dyn_addr_session_check: Literal["enable", "disable"]
    default_policy_expiry_days: int
    gui_enforce_change_summary: Literal["disable", "require", "optional"]
    internet_service_database_cache: Literal["disable", "enable"]
    internet_service_app_ctrl_size: int


@final
class SettingsObject:
    """Typed FortiObject for system/settings with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # VDOM comments.
    comments: str
    # Vdom type (traffic, lan-extension or admin).
    vdom_type: Literal["traffic", "lan-extension", "admin"]
    # Controller IP address or FQDN to connect.
    lan_extension_controller_addr: str
    # Controller port to connect.
    lan_extension_controller_port: int
    # Firewall operation mode (NAT or Transparent).
    opmode: Literal["nat", "transparent"]
    # Next Generation Firewall (NGFW) mode.
    ngfw_mode: Literal["profile-based", "policy-based"]
    # Offload HTTP traffic to FortiWeb or FortiCache.
    http_external_dest: Literal["fortiweb", "forticache"]
    # Select how to manage sessions affected by firewall policy configuration changes.
    firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"]
    # Transparent mode IPv4 management IP address and netmask.
    manageip: str
    # Transparent mode IPv4 default gateway IP address.
    gateway: str
    # IP address and netmask.
    ip: str
    # Transparent mode IPv6 management IP address and netmask.
    manageip6: str
    # Transparent mode IPv6 default gateway IP address.
    gateway6: str
    # IPv6 address prefix for NAT mode.
    ip6: str
    # Interface to use for management access for NAT mode.
    device: str
    # Enable/disable Bi-directional Forwarding Detection (BFD) on all interfaces.
    bfd: Literal["enable", "disable"]
    # BFD desired minimal transmit interval (1 - 100000 ms, default = 250).
    bfd_desired_min_tx: int
    # BFD required minimal receive interval (1 - 100000 ms, default = 250).
    bfd_required_min_rx: int
    # BFD detection multiplier (1 - 50, default = 3).
    bfd_detect_mult: int
    # Enable to not enforce verifying the source port of BFD Packets.
    bfd_dont_enforce_src_port: Literal["enable", "disable"]
    # Enable/disable converting antispam tags to UTF-8 for better non-ASCII character
    utf8_spam_tagging: Literal["enable", "disable"]
    # Enable/disable WCCP cache engine.
    wccp_cache_engine: Literal["enable", "disable"]
    # Enable/disable periodic VPN log statistics for one or more types of VPN. Separat
    vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"]
    # Period to send VPN log statistics (0 or 60 - 86400 sec).
    vpn_stats_period: int
    # IPv4 Equal-cost multi-path (ECMP) routing and load balancing mode.
    v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"]
    # Duration of MAC addresses in Transparent mode (300 - 8640000 sec, default = 300)
    mac_ttl: int
    # Enable/disable checking for a matching policy each time hairpin traffic goes thr
    fw_session_hairpin: Literal["enable", "disable"]
    # Enable/disable action to take on PRP trailer.
    prp_trailer_action: Literal["enable", "disable"]
    # Enable/disable source NAT (SNAT) for VIP hairpin traffic.
    snat_hairpin_traffic: Literal["enable", "disable"]
    # Enable/disable the DHCP Proxy.
    dhcp_proxy: Literal["enable", "disable"]
    # Specify how to select outgoing interface to reach server.
    dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    dhcp_proxy_interface: str
    # VRF ID used for connection to server.
    dhcp_proxy_vrf_select: int
    # DHCP Server IPv4 address.
    dhcp_server_ip: list[dict[str, Any]]  # Multi-value field
    # DHCPv6 server IPv6 address.
    dhcp6_server_ip: list[dict[str, Any]]  # Multi-value field
    # Enable/disable central NAT.
    central_nat: Literal["enable", "disable"]
    # Default columns to display for policy lists on GUI.
    gui_default_policy_columns: list[SettingsGuidefaultpolicycolumnsObject]  # Table field - list of typed objects
    # Enable/disable Link Layer Discovery Protocol (LLDP) reception for this VDOM or a
    lldp_reception: Literal["enable", "disable", "global"]
    # Enable/disable Link Layer Discovery Protocol (LLDP) transmission for this VDOM o
    lldp_transmission: Literal["enable", "disable", "global"]
    # Enable/disable link down access traffic.
    link_down_access: Literal["enable", "disable"]
    # Enable/disable NAT46 IPv6 fragment header generation.
    nat46_generate_ipv6_fragment_header: Literal["enable", "disable"]
    # Enable/disable mandatory IPv4 packet forwarding in NAT46.
    nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"]
    # Enable/disable mandatory IPv6 packet forwarding in NAT64.
    nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"]
    # Enable/disable detection of unknown ESP packets (default = enable).
    detect_unknown_esp: Literal["enable", "disable"]
    # Force the intree session to always use the best route.
    intree_ses_best_route: Literal["force", "disable"]
    # Enable/disable auxiliary session.
    auxiliary_session: Literal["enable", "disable"]
    # Enable/disable IPv4 asymmetric routing.
    asymroute: Literal["enable", "disable"]
    # Enable/disable ICMP asymmetric routing.
    asymroute_icmp: Literal["enable", "disable"]
    # Enable/disable allowing TCP session without SYN flags.
    tcp_session_without_syn: Literal["enable", "disable"]
    # Enable/disable including denied session in the session table.
    ses_denied_traffic: Literal["enable", "disable"]
    # Enable/disable including denied multicast session in the session table.
    ses_denied_multicast_traffic: Literal["enable", "disable"]
    # Enable/disable strict source verification.
    strict_src_check: Literal["enable", "disable"]
    # Enable/disable link down path.
    allow_linkdown_path: Literal["enable", "disable"]
    # Enable/disable asymmetric IPv6 routing.
    asymroute6: Literal["enable", "disable"]
    # Enable/disable asymmetric ICMPv6 routing.
    asymroute6_icmp: Literal["enable", "disable"]
    # Enable/disable SCTP session creation without SCTP INIT.
    sctp_session_without_init: Literal["enable", "disable"]
    # Enable/disable the SIP kernel session helper to create an expectation for port 5
    sip_expectation: Literal["enable", "disable"]
    # Enable/disable recording the original SIP source IP address when NAT is used.
    sip_nat_trace: Literal["enable", "disable"]
    # Enable/disable H323 direct model.
    h323_direct_model: Literal["disable", "enable"]
    # Enable/disable this VDOM.
    status: Literal["enable", "disable"]
    # TCP port the SIP proxy monitors for SIP traffic (0 - 65535, default = 5060).
    sip_tcp_port: int
    # UDP port the SIP proxy monitors for SIP traffic (0 - 65535, default = 5060).
    sip_udp_port: int
    # TCP port the SIP proxy monitors for SIP SSL/TLS traffic
    sip_ssl_port: int
    # TCP port the SCCP proxy monitors for SCCP traffic (0 - 65535, default = 2000).
    sccp_port: int
    # Enable/disable multicast forwarding.
    multicast_forward: Literal["enable", "disable"]
    # Enable/disable preventing the FortiGate from changing the TTL for forwarded mult
    multicast_ttl_notchange: Literal["enable", "disable"]
    # Enable/disable allowing multicast traffic through the FortiGate without a policy
    multicast_skip_policy: Literal["enable", "disable"]
    # Enable/disable allowing interface subnets to use overlapping IP addresses.
    allow_subnet_overlap: Literal["enable", "disable"]
    # Enable/disable denying TCP by sending an ICMP communication prohibited packet.
    deny_tcp_with_icmp: Literal["enable", "disable"]
    # Maximum number of Equal Cost Multi-Path (ECMP) next-hops. Set to 1 to disable EC
    ecmp_max_paths: int
    # Timeout for discovered devices (1 - 365 days, default = 28).
    discovered_device_timeout: int
    # Enable/disable using DNS to validate email addresses collected by a captive port
    email_portal_check_dns: Literal["disable", "enable"]
    # Configure how the FortiGate handles VoIP traffic when a policy that accepts the
    default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"]
    # Enable/disable ICAP on the GUI.
    gui_icap: Literal["enable", "disable"]
    # Enable/disable implicit firewall policies on the GUI.
    gui_implicit_policy: Literal["enable", "disable"]
    # Enable/disable DNS database settings on the GUI.
    gui_dns_database: Literal["enable", "disable"]
    # Enable/disable server load balancing on the GUI.
    gui_load_balance: Literal["enable", "disable"]
    # Enable/disable multicast firewall policies on the GUI.
    gui_multicast_policy: Literal["enable", "disable"]
    # Enable/disable DoS policies on the GUI.
    gui_dos_policy: Literal["enable", "disable"]
    # Enable/disable object colors on the GUI.
    gui_object_colors: Literal["enable", "disable"]
    # Enable/disable route-tag addresses on the GUI.
    gui_route_tag_address_creation: Literal["enable", "disable"]
    # Enable/disable VoIP profiles on the GUI.
    gui_voip_profile: Literal["enable", "disable"]
    # Enable/disable FortiAP profiles on the GUI.
    gui_ap_profile: Literal["enable", "disable"]
    # Enable/disable Security Profile Groups on the GUI.
    gui_security_profile_group: Literal["enable", "disable"]
    # Enable/disable Local-In policies on the GUI.
    gui_local_in_policy: Literal["enable", "disable"]
    # Enable/disable WAN Optimization and Web Caching on the GUI.
    gui_wanopt_cache: Literal["enable", "disable"]
    # Enable/disable the explicit proxy on the GUI.
    gui_explicit_proxy: Literal["enable", "disable"]
    # Enable/disable dynamic routing on the GUI.
    gui_dynamic_routing: Literal["enable", "disable"]
    # Enable/disable SSL-VPN personal bookmark management on the GUI.
    gui_sslvpn_personal_bookmarks: Literal["enable", "disable"]
    # Enable/disable SSL-VPN realms on the GUI.
    gui_sslvpn_realms: Literal["enable", "disable"]
    # Enable/disable policy-based IPsec VPN on the GUI.
    gui_policy_based_ipsec: Literal["enable", "disable"]
    # Enable/disable threat weight on the GUI.
    gui_threat_weight: Literal["enable", "disable"]
    # Enable/disable Antispam on the GUI.
    gui_spamfilter: Literal["enable", "disable"]
    # Enable/disable File-filter on the GUI.
    gui_file_filter: Literal["enable", "disable"]
    # Enable/disable application control on the GUI.
    gui_application_control: Literal["enable", "disable"]
    # Enable/disable IPS on the GUI.
    gui_ips: Literal["enable", "disable"]
    # Enable/disable advanced DHCP options on the GUI.
    gui_dhcp_advanced: Literal["enable", "disable"]
    # Enable/disable IPsec VPN settings pages on the GUI.
    gui_vpn: Literal["enable", "disable"]
    # Enable/disable SSL-VPN settings pages on the GUI.
    gui_sslvpn: Literal["enable", "disable"]
    # Enable/disable the wireless controller on the GUI.
    gui_wireless_controller: Literal["enable", "disable"]
    # Enable/disable advanced wireless features in GUI.
    gui_advanced_wireless_features: Literal["enable", "disable"]
    # Enable/disable the switch controller on the GUI.
    gui_switch_controller: Literal["enable", "disable"]
    # Enable/disable FortiAP split tunneling on the GUI.
    gui_fortiap_split_tunneling: Literal["enable", "disable"]
    # Enable/disable advanced web filtering on the GUI.
    gui_webfilter_advanced: Literal["enable", "disable"]
    # Enable/disable traffic shaping on the GUI.
    gui_traffic_shaping: Literal["enable", "disable"]
    # Enable/disable SD-WAN on the GUI.
    gui_wan_load_balancing: Literal["enable", "disable"]
    # Enable/disable AntiVirus on the GUI.
    gui_antivirus: Literal["enable", "disable"]
    # Enable/disable Web filtering on the GUI.
    gui_webfilter: Literal["enable", "disable"]
    # Enable/disable Video filtering on the GUI.
    gui_videofilter: Literal["enable", "disable"]
    # Enable/disable DNS Filtering on the GUI.
    gui_dnsfilter: Literal["enable", "disable"]
    # Enable/disable Web Application Firewall on the GUI.
    gui_waf_profile: Literal["enable", "disable"]
    # Enable/disable Data Loss Prevention on the GUI.
    gui_dlp_profile: Literal["enable", "disable"]
    # Enable/disable Show advanced DLP expressions on the GUI.
    gui_dlp_advanced: Literal["enable", "disable"]
    # Enable/disable Virtual Patching on the GUI.
    gui_virtual_patch_profile: Literal["enable", "disable"]
    # Enable/disable Inline-CASB on the GUI.
    gui_casb: Literal["enable", "disable"]
    # Enable/disable FortiExtender on the GUI.
    gui_fortiextender_controller: Literal["enable", "disable"]
    # Enable/disable advanced policy configuration on the GUI.
    gui_advanced_policy: Literal["enable", "disable"]
    # Enable/disable the requirement for policy naming on the GUI.
    gui_allow_unnamed_policy: Literal["enable", "disable"]
    # Enable/disable email collection on the GUI.
    gui_email_collection: Literal["enable", "disable"]
    # Enable/disable adding multiple interfaces to a policy on the GUI.
    gui_multiple_interface_policy: Literal["enable", "disable"]
    # Enable/disable policy disclaimer on the GUI.
    gui_policy_disclaimer: Literal["enable", "disable"]
    # Enable/disable Zero Trust Network Access features on the GUI.
    gui_ztna: Literal["enable", "disable"]
    # Enable/disable Operational technology features on the GUI.
    gui_ot: Literal["enable", "disable"]
    # Enable/disable Create dynamic addresses to manage known devices.
    gui_dynamic_device_os_id: Literal["enable", "disable"]
    # Enable/disable Manage general radio packet service (GPRS) protocols on the GUI.
    gui_gtp: Literal["enable", "disable"]
    # Local location ID in the form of an IPv4 address.
    location_id: str
    # Enable/disable IKEv2 session resumption (RFC 5723).
    ike_session_resume: Literal["enable", "disable"]
    # Enable/disable IKE quick crash detection (RFC 6290).
    ike_quick_crash_detect: Literal["enable", "disable"]
    # Configure IKE ASN.1 Distinguished Name format conventions.
    ike_dn_format: Literal["with-space", "no-space"]
    # UDP port for IKE/IPsec traffic (default 500).
    ike_port: int
    # TCP port for IKE/IPsec traffic (default 443).
    ike_tcp_port: int
    # Enable/disable IKE Policy Based Routing (PBR).
    ike_policy_route: Literal["enable", "disable"]
    # Enable/disable detail log for IKE events.
    ike_detailed_event_logs: Literal["disable", "enable"]
    # Enable/disable blocking of land attacks.
    block_land_attack: Literal["disable", "enable"]
    # Enable/disable policy service enforcement based on application default ports.
    default_app_port_as_service: Literal["enable", "disable"]
    # Enable/disable dirty session check caused by FQDN updates.
    fqdn_session_check: Literal["enable", "disable"]
    # Enable/disable dirty session check caused by external resource updates.
    ext_resource_session_check: Literal["enable", "disable"]
    # Enable/disable dirty session check caused by dynamic address updates.
    dyn_addr_session_check: Literal["enable", "disable"]
    # Default policy expiry in days (0 - 365 days, default = 30).
    default_policy_expiry_days: int
    # Enforce change summaries for select tables in the GUI.
    gui_enforce_change_summary: Literal["disable", "require", "optional"]
    # Enable/disable Internet Service database caching.
    internet_service_database_cache: Literal["disable", "enable"]
    # Maximum number of tuple entries (protocol, port, IP address, application ID) sto
    internet_service_app_ctrl_size: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SettingsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Settings:
    """
    Configure VDOM settings.
    
    Path: system/settings
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsResponse: ...
    
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
    ) -> SettingsResponse: ...
    
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
    ) -> SettingsResponse: ...
    
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
    ) -> SettingsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        comments: str | None = ...,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = ...,
        lan_extension_controller_addr: str | None = ...,
        lan_extension_controller_port: int | None = ...,
        opmode: Literal["nat", "transparent"] | None = ...,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = ...,
        http_external_dest: Literal["fortiweb", "forticache"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = ...,
        manageip: str | None = ...,
        gateway: str | None = ...,
        ip: str | None = ...,
        manageip6: str | None = ...,
        gateway6: str | None = ...,
        ip6: str | None = ...,
        device: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = ...,
        utf8_spam_tagging: Literal["enable", "disable"] | None = ...,
        wccp_cache_engine: Literal["enable", "disable"] | None = ...,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list[str] | None = ...,
        vpn_stats_period: int | None = ...,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = ...,
        mac_ttl: int | None = ...,
        fw_session_hairpin: Literal["enable", "disable"] | None = ...,
        prp_trailer_action: Literal["enable", "disable"] | None = ...,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = ...,
        dhcp_proxy: Literal["enable", "disable"] | None = ...,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_proxy_interface: str | None = ...,
        dhcp_proxy_vrf_select: int | None = ...,
        dhcp_server_ip: str | list[str] | None = ...,
        dhcp6_server_ip: str | list[str] | None = ...,
        central_nat: Literal["enable", "disable"] | None = ...,
        gui_default_policy_columns: str | list[str] | list[dict[str, Any]] | None = ...,
        lldp_reception: Literal["enable", "disable", "global"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "global"] | None = ...,
        link_down_access: Literal["enable", "disable"] | None = ...,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = ...,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = ...,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = ...,
        detect_unknown_esp: Literal["enable", "disable"] | None = ...,
        intree_ses_best_route: Literal["force", "disable"] | None = ...,
        auxiliary_session: Literal["enable", "disable"] | None = ...,
        asymroute: Literal["enable", "disable"] | None = ...,
        asymroute_icmp: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["enable", "disable"] | None = ...,
        ses_denied_traffic: Literal["enable", "disable"] | None = ...,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = ...,
        strict_src_check: Literal["enable", "disable"] | None = ...,
        allow_linkdown_path: Literal["enable", "disable"] | None = ...,
        asymroute6: Literal["enable", "disable"] | None = ...,
        asymroute6_icmp: Literal["enable", "disable"] | None = ...,
        sctp_session_without_init: Literal["enable", "disable"] | None = ...,
        sip_expectation: Literal["enable", "disable"] | None = ...,
        sip_nat_trace: Literal["enable", "disable"] | None = ...,
        h323_direct_model: Literal["disable", "enable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sip_tcp_port: int | list[int] | None = ...,
        sip_udp_port: int | list[int] | None = ...,
        sip_ssl_port: int | None = ...,
        sccp_port: int | None = ...,
        multicast_forward: Literal["enable", "disable"] | None = ...,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = ...,
        multicast_skip_policy: Literal["enable", "disable"] | None = ...,
        allow_subnet_overlap: Literal["enable", "disable"] | None = ...,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = ...,
        ecmp_max_paths: int | None = ...,
        discovered_device_timeout: int | None = ...,
        email_portal_check_dns: Literal["disable", "enable"] | None = ...,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = ...,
        gui_icap: Literal["enable", "disable"] | None = ...,
        gui_implicit_policy: Literal["enable", "disable"] | None = ...,
        gui_dns_database: Literal["enable", "disable"] | None = ...,
        gui_load_balance: Literal["enable", "disable"] | None = ...,
        gui_multicast_policy: Literal["enable", "disable"] | None = ...,
        gui_dos_policy: Literal["enable", "disable"] | None = ...,
        gui_object_colors: Literal["enable", "disable"] | None = ...,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = ...,
        gui_voip_profile: Literal["enable", "disable"] | None = ...,
        gui_ap_profile: Literal["enable", "disable"] | None = ...,
        gui_security_profile_group: Literal["enable", "disable"] | None = ...,
        gui_local_in_policy: Literal["enable", "disable"] | None = ...,
        gui_wanopt_cache: Literal["enable", "disable"] | None = ...,
        gui_explicit_proxy: Literal["enable", "disable"] | None = ...,
        gui_dynamic_routing: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = ...,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = ...,
        gui_threat_weight: Literal["enable", "disable"] | None = ...,
        gui_spamfilter: Literal["enable", "disable"] | None = ...,
        gui_file_filter: Literal["enable", "disable"] | None = ...,
        gui_application_control: Literal["enable", "disable"] | None = ...,
        gui_ips: Literal["enable", "disable"] | None = ...,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = ...,
        gui_vpn: Literal["enable", "disable"] | None = ...,
        gui_sslvpn: Literal["enable", "disable"] | None = ...,
        gui_wireless_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = ...,
        gui_switch_controller: Literal["enable", "disable"] | None = ...,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = ...,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = ...,
        gui_traffic_shaping: Literal["enable", "disable"] | None = ...,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = ...,
        gui_antivirus: Literal["enable", "disable"] | None = ...,
        gui_webfilter: Literal["enable", "disable"] | None = ...,
        gui_videofilter: Literal["enable", "disable"] | None = ...,
        gui_dnsfilter: Literal["enable", "disable"] | None = ...,
        gui_waf_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_advanced: Literal["enable", "disable"] | None = ...,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = ...,
        gui_casb: Literal["enable", "disable"] | None = ...,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_policy: Literal["enable", "disable"] | None = ...,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = ...,
        gui_email_collection: Literal["enable", "disable"] | None = ...,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = ...,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        gui_ztna: Literal["enable", "disable"] | None = ...,
        gui_ot: Literal["enable", "disable"] | None = ...,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = ...,
        gui_gtp: Literal["enable", "disable"] | None = ...,
        location_id: str | None = ...,
        ike_session_resume: Literal["enable", "disable"] | None = ...,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = ...,
        ike_dn_format: Literal["with-space", "no-space"] | None = ...,
        ike_port: int | None = ...,
        ike_tcp_port: int | None = ...,
        ike_policy_route: Literal["enable", "disable"] | None = ...,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = ...,
        block_land_attack: Literal["disable", "enable"] | None = ...,
        default_app_port_as_service: Literal["enable", "disable"] | None = ...,
        fqdn_session_check: Literal["enable", "disable"] | None = ...,
        ext_resource_session_check: Literal["enable", "disable"] | None = ...,
        dyn_addr_session_check: Literal["enable", "disable"] | None = ...,
        default_policy_expiry_days: int | None = ...,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = ...,
        internet_service_database_cache: Literal["disable", "enable"] | None = ...,
        internet_service_app_ctrl_size: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SettingsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        comments: str | None = ...,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = ...,
        lan_extension_controller_addr: str | None = ...,
        lan_extension_controller_port: int | None = ...,
        opmode: Literal["nat", "transparent"] | None = ...,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = ...,
        http_external_dest: Literal["fortiweb", "forticache"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = ...,
        manageip: str | None = ...,
        gateway: str | None = ...,
        ip: str | None = ...,
        manageip6: str | None = ...,
        gateway6: str | None = ...,
        ip6: str | None = ...,
        device: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = ...,
        utf8_spam_tagging: Literal["enable", "disable"] | None = ...,
        wccp_cache_engine: Literal["enable", "disable"] | None = ...,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list[str] | None = ...,
        vpn_stats_period: int | None = ...,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = ...,
        mac_ttl: int | None = ...,
        fw_session_hairpin: Literal["enable", "disable"] | None = ...,
        prp_trailer_action: Literal["enable", "disable"] | None = ...,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = ...,
        dhcp_proxy: Literal["enable", "disable"] | None = ...,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_proxy_interface: str | None = ...,
        dhcp_proxy_vrf_select: int | None = ...,
        dhcp_server_ip: str | list[str] | None = ...,
        dhcp6_server_ip: str | list[str] | None = ...,
        central_nat: Literal["enable", "disable"] | None = ...,
        gui_default_policy_columns: str | list[str] | list[dict[str, Any]] | None = ...,
        lldp_reception: Literal["enable", "disable", "global"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "global"] | None = ...,
        link_down_access: Literal["enable", "disable"] | None = ...,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = ...,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = ...,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = ...,
        detect_unknown_esp: Literal["enable", "disable"] | None = ...,
        intree_ses_best_route: Literal["force", "disable"] | None = ...,
        auxiliary_session: Literal["enable", "disable"] | None = ...,
        asymroute: Literal["enable", "disable"] | None = ...,
        asymroute_icmp: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["enable", "disable"] | None = ...,
        ses_denied_traffic: Literal["enable", "disable"] | None = ...,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = ...,
        strict_src_check: Literal["enable", "disable"] | None = ...,
        allow_linkdown_path: Literal["enable", "disable"] | None = ...,
        asymroute6: Literal["enable", "disable"] | None = ...,
        asymroute6_icmp: Literal["enable", "disable"] | None = ...,
        sctp_session_without_init: Literal["enable", "disable"] | None = ...,
        sip_expectation: Literal["enable", "disable"] | None = ...,
        sip_nat_trace: Literal["enable", "disable"] | None = ...,
        h323_direct_model: Literal["disable", "enable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sip_tcp_port: int | list[int] | None = ...,
        sip_udp_port: int | list[int] | None = ...,
        sip_ssl_port: int | None = ...,
        sccp_port: int | None = ...,
        multicast_forward: Literal["enable", "disable"] | None = ...,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = ...,
        multicast_skip_policy: Literal["enable", "disable"] | None = ...,
        allow_subnet_overlap: Literal["enable", "disable"] | None = ...,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = ...,
        ecmp_max_paths: int | None = ...,
        discovered_device_timeout: int | None = ...,
        email_portal_check_dns: Literal["disable", "enable"] | None = ...,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = ...,
        gui_icap: Literal["enable", "disable"] | None = ...,
        gui_implicit_policy: Literal["enable", "disable"] | None = ...,
        gui_dns_database: Literal["enable", "disable"] | None = ...,
        gui_load_balance: Literal["enable", "disable"] | None = ...,
        gui_multicast_policy: Literal["enable", "disable"] | None = ...,
        gui_dos_policy: Literal["enable", "disable"] | None = ...,
        gui_object_colors: Literal["enable", "disable"] | None = ...,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = ...,
        gui_voip_profile: Literal["enable", "disable"] | None = ...,
        gui_ap_profile: Literal["enable", "disable"] | None = ...,
        gui_security_profile_group: Literal["enable", "disable"] | None = ...,
        gui_local_in_policy: Literal["enable", "disable"] | None = ...,
        gui_wanopt_cache: Literal["enable", "disable"] | None = ...,
        gui_explicit_proxy: Literal["enable", "disable"] | None = ...,
        gui_dynamic_routing: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = ...,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = ...,
        gui_threat_weight: Literal["enable", "disable"] | None = ...,
        gui_spamfilter: Literal["enable", "disable"] | None = ...,
        gui_file_filter: Literal["enable", "disable"] | None = ...,
        gui_application_control: Literal["enable", "disable"] | None = ...,
        gui_ips: Literal["enable", "disable"] | None = ...,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = ...,
        gui_vpn: Literal["enable", "disable"] | None = ...,
        gui_sslvpn: Literal["enable", "disable"] | None = ...,
        gui_wireless_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = ...,
        gui_switch_controller: Literal["enable", "disable"] | None = ...,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = ...,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = ...,
        gui_traffic_shaping: Literal["enable", "disable"] | None = ...,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = ...,
        gui_antivirus: Literal["enable", "disable"] | None = ...,
        gui_webfilter: Literal["enable", "disable"] | None = ...,
        gui_videofilter: Literal["enable", "disable"] | None = ...,
        gui_dnsfilter: Literal["enable", "disable"] | None = ...,
        gui_waf_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_advanced: Literal["enable", "disable"] | None = ...,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = ...,
        gui_casb: Literal["enable", "disable"] | None = ...,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_policy: Literal["enable", "disable"] | None = ...,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = ...,
        gui_email_collection: Literal["enable", "disable"] | None = ...,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = ...,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        gui_ztna: Literal["enable", "disable"] | None = ...,
        gui_ot: Literal["enable", "disable"] | None = ...,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = ...,
        gui_gtp: Literal["enable", "disable"] | None = ...,
        location_id: str | None = ...,
        ike_session_resume: Literal["enable", "disable"] | None = ...,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = ...,
        ike_dn_format: Literal["with-space", "no-space"] | None = ...,
        ike_port: int | None = ...,
        ike_tcp_port: int | None = ...,
        ike_policy_route: Literal["enable", "disable"] | None = ...,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = ...,
        block_land_attack: Literal["disable", "enable"] | None = ...,
        default_app_port_as_service: Literal["enable", "disable"] | None = ...,
        fqdn_session_check: Literal["enable", "disable"] | None = ...,
        ext_resource_session_check: Literal["enable", "disable"] | None = ...,
        dyn_addr_session_check: Literal["enable", "disable"] | None = ...,
        default_policy_expiry_days: int | None = ...,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = ...,
        internet_service_database_cache: Literal["disable", "enable"] | None = ...,
        internet_service_app_ctrl_size: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        comments: str | None = ...,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = ...,
        lan_extension_controller_addr: str | None = ...,
        lan_extension_controller_port: int | None = ...,
        opmode: Literal["nat", "transparent"] | None = ...,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = ...,
        http_external_dest: Literal["fortiweb", "forticache"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = ...,
        manageip: str | None = ...,
        gateway: str | None = ...,
        ip: str | None = ...,
        manageip6: str | None = ...,
        gateway6: str | None = ...,
        ip6: str | None = ...,
        device: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = ...,
        utf8_spam_tagging: Literal["enable", "disable"] | None = ...,
        wccp_cache_engine: Literal["enable", "disable"] | None = ...,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list[str] | None = ...,
        vpn_stats_period: int | None = ...,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = ...,
        mac_ttl: int | None = ...,
        fw_session_hairpin: Literal["enable", "disable"] | None = ...,
        prp_trailer_action: Literal["enable", "disable"] | None = ...,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = ...,
        dhcp_proxy: Literal["enable", "disable"] | None = ...,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_proxy_interface: str | None = ...,
        dhcp_proxy_vrf_select: int | None = ...,
        dhcp_server_ip: str | list[str] | None = ...,
        dhcp6_server_ip: str | list[str] | None = ...,
        central_nat: Literal["enable", "disable"] | None = ...,
        gui_default_policy_columns: str | list[str] | list[dict[str, Any]] | None = ...,
        lldp_reception: Literal["enable", "disable", "global"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "global"] | None = ...,
        link_down_access: Literal["enable", "disable"] | None = ...,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = ...,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = ...,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = ...,
        detect_unknown_esp: Literal["enable", "disable"] | None = ...,
        intree_ses_best_route: Literal["force", "disable"] | None = ...,
        auxiliary_session: Literal["enable", "disable"] | None = ...,
        asymroute: Literal["enable", "disable"] | None = ...,
        asymroute_icmp: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["enable", "disable"] | None = ...,
        ses_denied_traffic: Literal["enable", "disable"] | None = ...,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = ...,
        strict_src_check: Literal["enable", "disable"] | None = ...,
        allow_linkdown_path: Literal["enable", "disable"] | None = ...,
        asymroute6: Literal["enable", "disable"] | None = ...,
        asymroute6_icmp: Literal["enable", "disable"] | None = ...,
        sctp_session_without_init: Literal["enable", "disable"] | None = ...,
        sip_expectation: Literal["enable", "disable"] | None = ...,
        sip_nat_trace: Literal["enable", "disable"] | None = ...,
        h323_direct_model: Literal["disable", "enable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sip_tcp_port: int | list[int] | None = ...,
        sip_udp_port: int | list[int] | None = ...,
        sip_ssl_port: int | None = ...,
        sccp_port: int | None = ...,
        multicast_forward: Literal["enable", "disable"] | None = ...,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = ...,
        multicast_skip_policy: Literal["enable", "disable"] | None = ...,
        allow_subnet_overlap: Literal["enable", "disable"] | None = ...,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = ...,
        ecmp_max_paths: int | None = ...,
        discovered_device_timeout: int | None = ...,
        email_portal_check_dns: Literal["disable", "enable"] | None = ...,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = ...,
        gui_icap: Literal["enable", "disable"] | None = ...,
        gui_implicit_policy: Literal["enable", "disable"] | None = ...,
        gui_dns_database: Literal["enable", "disable"] | None = ...,
        gui_load_balance: Literal["enable", "disable"] | None = ...,
        gui_multicast_policy: Literal["enable", "disable"] | None = ...,
        gui_dos_policy: Literal["enable", "disable"] | None = ...,
        gui_object_colors: Literal["enable", "disable"] | None = ...,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = ...,
        gui_voip_profile: Literal["enable", "disable"] | None = ...,
        gui_ap_profile: Literal["enable", "disable"] | None = ...,
        gui_security_profile_group: Literal["enable", "disable"] | None = ...,
        gui_local_in_policy: Literal["enable", "disable"] | None = ...,
        gui_wanopt_cache: Literal["enable", "disable"] | None = ...,
        gui_explicit_proxy: Literal["enable", "disable"] | None = ...,
        gui_dynamic_routing: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = ...,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = ...,
        gui_threat_weight: Literal["enable", "disable"] | None = ...,
        gui_spamfilter: Literal["enable", "disable"] | None = ...,
        gui_file_filter: Literal["enable", "disable"] | None = ...,
        gui_application_control: Literal["enable", "disable"] | None = ...,
        gui_ips: Literal["enable", "disable"] | None = ...,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = ...,
        gui_vpn: Literal["enable", "disable"] | None = ...,
        gui_sslvpn: Literal["enable", "disable"] | None = ...,
        gui_wireless_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = ...,
        gui_switch_controller: Literal["enable", "disable"] | None = ...,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = ...,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = ...,
        gui_traffic_shaping: Literal["enable", "disable"] | None = ...,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = ...,
        gui_antivirus: Literal["enable", "disable"] | None = ...,
        gui_webfilter: Literal["enable", "disable"] | None = ...,
        gui_videofilter: Literal["enable", "disable"] | None = ...,
        gui_dnsfilter: Literal["enable", "disable"] | None = ...,
        gui_waf_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_advanced: Literal["enable", "disable"] | None = ...,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = ...,
        gui_casb: Literal["enable", "disable"] | None = ...,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_policy: Literal["enable", "disable"] | None = ...,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = ...,
        gui_email_collection: Literal["enable", "disable"] | None = ...,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = ...,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        gui_ztna: Literal["enable", "disable"] | None = ...,
        gui_ot: Literal["enable", "disable"] | None = ...,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = ...,
        gui_gtp: Literal["enable", "disable"] | None = ...,
        location_id: str | None = ...,
        ike_session_resume: Literal["enable", "disable"] | None = ...,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = ...,
        ike_dn_format: Literal["with-space", "no-space"] | None = ...,
        ike_port: int | None = ...,
        ike_tcp_port: int | None = ...,
        ike_policy_route: Literal["enable", "disable"] | None = ...,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = ...,
        block_land_attack: Literal["disable", "enable"] | None = ...,
        default_app_port_as_service: Literal["enable", "disable"] | None = ...,
        fqdn_session_check: Literal["enable", "disable"] | None = ...,
        ext_resource_session_check: Literal["enable", "disable"] | None = ...,
        dyn_addr_session_check: Literal["enable", "disable"] | None = ...,
        default_policy_expiry_days: int | None = ...,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = ...,
        internet_service_database_cache: Literal["disable", "enable"] | None = ...,
        internet_service_app_ctrl_size: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        comments: str | None = ...,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = ...,
        lan_extension_controller_addr: str | None = ...,
        lan_extension_controller_port: int | None = ...,
        opmode: Literal["nat", "transparent"] | None = ...,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = ...,
        http_external_dest: Literal["fortiweb", "forticache"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = ...,
        manageip: str | None = ...,
        gateway: str | None = ...,
        ip: str | None = ...,
        manageip6: str | None = ...,
        gateway6: str | None = ...,
        ip6: str | None = ...,
        device: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = ...,
        utf8_spam_tagging: Literal["enable", "disable"] | None = ...,
        wccp_cache_engine: Literal["enable", "disable"] | None = ...,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list[str] | None = ...,
        vpn_stats_period: int | None = ...,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = ...,
        mac_ttl: int | None = ...,
        fw_session_hairpin: Literal["enable", "disable"] | None = ...,
        prp_trailer_action: Literal["enable", "disable"] | None = ...,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = ...,
        dhcp_proxy: Literal["enable", "disable"] | None = ...,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_proxy_interface: str | None = ...,
        dhcp_proxy_vrf_select: int | None = ...,
        dhcp_server_ip: str | list[str] | None = ...,
        dhcp6_server_ip: str | list[str] | None = ...,
        central_nat: Literal["enable", "disable"] | None = ...,
        gui_default_policy_columns: str | list[str] | list[dict[str, Any]] | None = ...,
        lldp_reception: Literal["enable", "disable", "global"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "global"] | None = ...,
        link_down_access: Literal["enable", "disable"] | None = ...,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = ...,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = ...,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = ...,
        detect_unknown_esp: Literal["enable", "disable"] | None = ...,
        intree_ses_best_route: Literal["force", "disable"] | None = ...,
        auxiliary_session: Literal["enable", "disable"] | None = ...,
        asymroute: Literal["enable", "disable"] | None = ...,
        asymroute_icmp: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["enable", "disable"] | None = ...,
        ses_denied_traffic: Literal["enable", "disable"] | None = ...,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = ...,
        strict_src_check: Literal["enable", "disable"] | None = ...,
        allow_linkdown_path: Literal["enable", "disable"] | None = ...,
        asymroute6: Literal["enable", "disable"] | None = ...,
        asymroute6_icmp: Literal["enable", "disable"] | None = ...,
        sctp_session_without_init: Literal["enable", "disable"] | None = ...,
        sip_expectation: Literal["enable", "disable"] | None = ...,
        sip_nat_trace: Literal["enable", "disable"] | None = ...,
        h323_direct_model: Literal["disable", "enable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sip_tcp_port: int | list[int] | None = ...,
        sip_udp_port: int | list[int] | None = ...,
        sip_ssl_port: int | None = ...,
        sccp_port: int | None = ...,
        multicast_forward: Literal["enable", "disable"] | None = ...,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = ...,
        multicast_skip_policy: Literal["enable", "disable"] | None = ...,
        allow_subnet_overlap: Literal["enable", "disable"] | None = ...,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = ...,
        ecmp_max_paths: int | None = ...,
        discovered_device_timeout: int | None = ...,
        email_portal_check_dns: Literal["disable", "enable"] | None = ...,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = ...,
        gui_icap: Literal["enable", "disable"] | None = ...,
        gui_implicit_policy: Literal["enable", "disable"] | None = ...,
        gui_dns_database: Literal["enable", "disable"] | None = ...,
        gui_load_balance: Literal["enable", "disable"] | None = ...,
        gui_multicast_policy: Literal["enable", "disable"] | None = ...,
        gui_dos_policy: Literal["enable", "disable"] | None = ...,
        gui_object_colors: Literal["enable", "disable"] | None = ...,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = ...,
        gui_voip_profile: Literal["enable", "disable"] | None = ...,
        gui_ap_profile: Literal["enable", "disable"] | None = ...,
        gui_security_profile_group: Literal["enable", "disable"] | None = ...,
        gui_local_in_policy: Literal["enable", "disable"] | None = ...,
        gui_wanopt_cache: Literal["enable", "disable"] | None = ...,
        gui_explicit_proxy: Literal["enable", "disable"] | None = ...,
        gui_dynamic_routing: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = ...,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = ...,
        gui_threat_weight: Literal["enable", "disable"] | None = ...,
        gui_spamfilter: Literal["enable", "disable"] | None = ...,
        gui_file_filter: Literal["enable", "disable"] | None = ...,
        gui_application_control: Literal["enable", "disable"] | None = ...,
        gui_ips: Literal["enable", "disable"] | None = ...,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = ...,
        gui_vpn: Literal["enable", "disable"] | None = ...,
        gui_sslvpn: Literal["enable", "disable"] | None = ...,
        gui_wireless_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = ...,
        gui_switch_controller: Literal["enable", "disable"] | None = ...,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = ...,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = ...,
        gui_traffic_shaping: Literal["enable", "disable"] | None = ...,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = ...,
        gui_antivirus: Literal["enable", "disable"] | None = ...,
        gui_webfilter: Literal["enable", "disable"] | None = ...,
        gui_videofilter: Literal["enable", "disable"] | None = ...,
        gui_dnsfilter: Literal["enable", "disable"] | None = ...,
        gui_waf_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_advanced: Literal["enable", "disable"] | None = ...,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = ...,
        gui_casb: Literal["enable", "disable"] | None = ...,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_policy: Literal["enable", "disable"] | None = ...,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = ...,
        gui_email_collection: Literal["enable", "disable"] | None = ...,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = ...,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        gui_ztna: Literal["enable", "disable"] | None = ...,
        gui_ot: Literal["enable", "disable"] | None = ...,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = ...,
        gui_gtp: Literal["enable", "disable"] | None = ...,
        location_id: str | None = ...,
        ike_session_resume: Literal["enable", "disable"] | None = ...,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = ...,
        ike_dn_format: Literal["with-space", "no-space"] | None = ...,
        ike_port: int | None = ...,
        ike_tcp_port: int | None = ...,
        ike_policy_route: Literal["enable", "disable"] | None = ...,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = ...,
        block_land_attack: Literal["disable", "enable"] | None = ...,
        default_app_port_as_service: Literal["enable", "disable"] | None = ...,
        fqdn_session_check: Literal["enable", "disable"] | None = ...,
        ext_resource_session_check: Literal["enable", "disable"] | None = ...,
        dyn_addr_session_check: Literal["enable", "disable"] | None = ...,
        default_policy_expiry_days: int | None = ...,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = ...,
        internet_service_database_cache: Literal["disable", "enable"] | None = ...,
        internet_service_app_ctrl_size: int | None = ...,
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
        payload_dict: SettingsPayload | None = ...,
        comments: str | None = ...,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = ...,
        lan_extension_controller_addr: str | None = ...,
        lan_extension_controller_port: int | None = ...,
        opmode: Literal["nat", "transparent"] | None = ...,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = ...,
        http_external_dest: Literal["fortiweb", "forticache"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = ...,
        manageip: str | None = ...,
        gateway: str | None = ...,
        ip: str | None = ...,
        manageip6: str | None = ...,
        gateway6: str | None = ...,
        ip6: str | None = ...,
        device: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = ...,
        utf8_spam_tagging: Literal["enable", "disable"] | None = ...,
        wccp_cache_engine: Literal["enable", "disable"] | None = ...,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list[str] | None = ...,
        vpn_stats_period: int | None = ...,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = ...,
        mac_ttl: int | None = ...,
        fw_session_hairpin: Literal["enable", "disable"] | None = ...,
        prp_trailer_action: Literal["enable", "disable"] | None = ...,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = ...,
        dhcp_proxy: Literal["enable", "disable"] | None = ...,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_proxy_interface: str | None = ...,
        dhcp_proxy_vrf_select: int | None = ...,
        dhcp_server_ip: str | list[str] | None = ...,
        dhcp6_server_ip: str | list[str] | None = ...,
        central_nat: Literal["enable", "disable"] | None = ...,
        gui_default_policy_columns: str | list[str] | list[dict[str, Any]] | None = ...,
        lldp_reception: Literal["enable", "disable", "global"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "global"] | None = ...,
        link_down_access: Literal["enable", "disable"] | None = ...,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = ...,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = ...,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = ...,
        detect_unknown_esp: Literal["enable", "disable"] | None = ...,
        intree_ses_best_route: Literal["force", "disable"] | None = ...,
        auxiliary_session: Literal["enable", "disable"] | None = ...,
        asymroute: Literal["enable", "disable"] | None = ...,
        asymroute_icmp: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["enable", "disable"] | None = ...,
        ses_denied_traffic: Literal["enable", "disable"] | None = ...,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = ...,
        strict_src_check: Literal["enable", "disable"] | None = ...,
        allow_linkdown_path: Literal["enable", "disable"] | None = ...,
        asymroute6: Literal["enable", "disable"] | None = ...,
        asymroute6_icmp: Literal["enable", "disable"] | None = ...,
        sctp_session_without_init: Literal["enable", "disable"] | None = ...,
        sip_expectation: Literal["enable", "disable"] | None = ...,
        sip_nat_trace: Literal["enable", "disable"] | None = ...,
        h323_direct_model: Literal["disable", "enable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sip_tcp_port: int | list[int] | None = ...,
        sip_udp_port: int | list[int] | None = ...,
        sip_ssl_port: int | None = ...,
        sccp_port: int | None = ...,
        multicast_forward: Literal["enable", "disable"] | None = ...,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = ...,
        multicast_skip_policy: Literal["enable", "disable"] | None = ...,
        allow_subnet_overlap: Literal["enable", "disable"] | None = ...,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = ...,
        ecmp_max_paths: int | None = ...,
        discovered_device_timeout: int | None = ...,
        email_portal_check_dns: Literal["disable", "enable"] | None = ...,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = ...,
        gui_icap: Literal["enable", "disable"] | None = ...,
        gui_implicit_policy: Literal["enable", "disable"] | None = ...,
        gui_dns_database: Literal["enable", "disable"] | None = ...,
        gui_load_balance: Literal["enable", "disable"] | None = ...,
        gui_multicast_policy: Literal["enable", "disable"] | None = ...,
        gui_dos_policy: Literal["enable", "disable"] | None = ...,
        gui_object_colors: Literal["enable", "disable"] | None = ...,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = ...,
        gui_voip_profile: Literal["enable", "disable"] | None = ...,
        gui_ap_profile: Literal["enable", "disable"] | None = ...,
        gui_security_profile_group: Literal["enable", "disable"] | None = ...,
        gui_local_in_policy: Literal["enable", "disable"] | None = ...,
        gui_wanopt_cache: Literal["enable", "disable"] | None = ...,
        gui_explicit_proxy: Literal["enable", "disable"] | None = ...,
        gui_dynamic_routing: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = ...,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = ...,
        gui_threat_weight: Literal["enable", "disable"] | None = ...,
        gui_spamfilter: Literal["enable", "disable"] | None = ...,
        gui_file_filter: Literal["enable", "disable"] | None = ...,
        gui_application_control: Literal["enable", "disable"] | None = ...,
        gui_ips: Literal["enable", "disable"] | None = ...,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = ...,
        gui_vpn: Literal["enable", "disable"] | None = ...,
        gui_sslvpn: Literal["enable", "disable"] | None = ...,
        gui_wireless_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = ...,
        gui_switch_controller: Literal["enable", "disable"] | None = ...,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = ...,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = ...,
        gui_traffic_shaping: Literal["enable", "disable"] | None = ...,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = ...,
        gui_antivirus: Literal["enable", "disable"] | None = ...,
        gui_webfilter: Literal["enable", "disable"] | None = ...,
        gui_videofilter: Literal["enable", "disable"] | None = ...,
        gui_dnsfilter: Literal["enable", "disable"] | None = ...,
        gui_waf_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_advanced: Literal["enable", "disable"] | None = ...,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = ...,
        gui_casb: Literal["enable", "disable"] | None = ...,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_policy: Literal["enable", "disable"] | None = ...,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = ...,
        gui_email_collection: Literal["enable", "disable"] | None = ...,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = ...,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        gui_ztna: Literal["enable", "disable"] | None = ...,
        gui_ot: Literal["enable", "disable"] | None = ...,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = ...,
        gui_gtp: Literal["enable", "disable"] | None = ...,
        location_id: str | None = ...,
        ike_session_resume: Literal["enable", "disable"] | None = ...,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = ...,
        ike_dn_format: Literal["with-space", "no-space"] | None = ...,
        ike_port: int | None = ...,
        ike_tcp_port: int | None = ...,
        ike_policy_route: Literal["enable", "disable"] | None = ...,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = ...,
        block_land_attack: Literal["disable", "enable"] | None = ...,
        default_app_port_as_service: Literal["enable", "disable"] | None = ...,
        fqdn_session_check: Literal["enable", "disable"] | None = ...,
        ext_resource_session_check: Literal["enable", "disable"] | None = ...,
        dyn_addr_session_check: Literal["enable", "disable"] | None = ...,
        default_policy_expiry_days: int | None = ...,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = ...,
        internet_service_database_cache: Literal["disable", "enable"] | None = ...,
        internet_service_app_ctrl_size: int | None = ...,
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
    "Settings",
    "SettingsPayload",
    "SettingsObject",
]