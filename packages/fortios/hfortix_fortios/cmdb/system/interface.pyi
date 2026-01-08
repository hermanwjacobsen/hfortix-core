from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class InterfacePayload(TypedDict, total=False):
    """
    Type hints for system/interface payload fields.
    
    Configure interfaces.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: eap-ca-cert)
        - :class:`~.certificate.local.LocalEndpoint` (via: eap-user-cert)
        - :class:`~.firewall.shaping-profile.ShapingProfileEndpoint` (via: egress-shaping-profile, ingress-shaping-profile)
        - :class:`~.switch-controller.fortilink-settings.FortilinkSettingsEndpoint` (via: switch-controller-dynamic, switch-controller-nac)
        - :class:`~.switch-controller.traffic-policy.TrafficPolicyEndpoint` (via: switch-controller-traffic-policy)
        - :class:`~.system.interface.InterfaceEndpoint` (via: dhcp-relay-interface, interface)
        - :class:`~.system.lldp.network-policy.NetworkPolicyEndpoint` (via: lldp-network-policy)
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)
        - :class:`~.user.saml.SamlEndpoint` (via: ike-saml-server)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: auth-cert)

    **Usage:**
        payload: InterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Name.
    vdom: str  # Interface is in this virtual domain (VDOM).
    vrf: NotRequired[int]  # Virtual Routing Forwarding ID.
    cli_conn_status: NotRequired[int]  # CLI connection status.
    fortilink: NotRequired[Literal["enable", "disable"]]  # Enable FortiLink to dedicate this interface to manage other 
    switch_controller_source_ip: NotRequired[Literal["outbound", "fixed"]]  # Source IP address used in FortiLink over L3 connections.
    mode: NotRequired[Literal["static", "dhcp", "pppoe"]]  # Addressing mode (static, DHCP, PPPoE).
    client_options: NotRequired[list[dict[str, Any]]]  # DHCP client options.
    distance: NotRequired[int]  # Distance for routes learned through PPPoE or DHCP, lower dis
    priority: NotRequired[int]  # Priority of learned routes.
    dhcp_relay_interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    dhcp_relay_interface: str  # Specify outgoing interface to reach server.
    dhcp_relay_vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    dhcp_broadcast_flag: NotRequired[Literal["disable", "enable"]]  # Enable/disable setting of the broadcast flag in messages sen
    dhcp_relay_service: NotRequired[Literal["disable", "enable"]]  # Enable/disable allowing this interface to act as a DHCP rela
    dhcp_relay_ip: NotRequired[list[dict[str, Any]]]  # DHCP relay IP address.
    dhcp_relay_source_ip: NotRequired[str]  # IP address used by the DHCP relay as its source IP.
    dhcp_relay_circuit_id: NotRequired[str]  # DHCP relay circuit ID.
    dhcp_relay_link_selection: NotRequired[str]  # DHCP relay link selection.
    dhcp_relay_request_all_server: NotRequired[Literal["disable", "enable"]]  # Enable/disable sending of DHCP requests to all servers.
    dhcp_relay_allow_no_end_option: NotRequired[Literal["disable", "enable"]]  # Enable/disable relaying DHCP messages with no end option.
    dhcp_relay_type: NotRequired[Literal["regular", "ipsec"]]  # DHCP relay type (regular or IPsec).
    dhcp_smart_relay: NotRequired[Literal["disable", "enable"]]  # Enable/disable DHCP smart relay.
    dhcp_relay_agent_option: NotRequired[Literal["enable", "disable"]]  # Enable/disable DHCP relay agent option.
    dhcp_classless_route_addition: NotRequired[Literal["enable", "disable"]]  # Enable/disable addition of classless static routes retrieved
    management_ip: NotRequired[str]  # High Availability in-band management IP address of this inte
    ip: NotRequired[str]  # Interface IPv4 address and subnet mask, syntax: X.X.X.X/24.
    allowaccess: NotRequired[Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"]]  # Permitted types of management access to this interface.
    gwdetect: NotRequired[Literal["enable", "disable"]]  # Enable/disable detect gateway alive for first.
    ping_serv_status: NotRequired[int]  # PING server status.
    detectserver: NotRequired[str]  # Gateway's ping server for this IP.
    detectprotocol: NotRequired[Literal["ping", "tcp-echo", "udp-echo"]]  # Protocols used to detect the server.
    ha_priority: NotRequired[int]  # HA election priority for the PING server.
    fail_detect: NotRequired[Literal["enable", "disable"]]  # Enable/disable fail detection features for this interface.
    fail_detect_option: NotRequired[Literal["detectserver", "link-down"]]  # Options for detecting that this interface has failed.
    fail_alert_method: NotRequired[Literal["link-failed-signal", "link-down"]]  # Select link-failed-signal or link-down method to alert about
    fail_action_on_extender: NotRequired[Literal["soft-restart", "hard-restart", "reboot"]]  # Action on FortiExtender when interface fail.
    fail_alert_interfaces: NotRequired[list[dict[str, Any]]]  # Names of the FortiGate interfaces to which the link failure 
    dhcp_client_identifier: NotRequired[str]  # DHCP client identifier.
    dhcp_renew_time: NotRequired[int]  # DHCP renew time in seconds (300-604800), 0 means use the ren
    ipunnumbered: NotRequired[str]  # Unnumbered IP used for PPPoE interfaces for which no unique 
    username: NotRequired[str]  # Username of the PPPoE account, provided by your ISP.
    pppoe_egress_cos: NotRequired[Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"]]  # CoS in VLAN tag for outgoing PPPoE/PPP packets.
    pppoe_unnumbered_negotiate: NotRequired[Literal["enable", "disable"]]  # Enable/disable PPPoE unnumbered negotiation.
    password: NotRequired[str]  # PPPoE account's password.
    idle_timeout: NotRequired[int]  # PPPoE auto disconnect after idle timeout seconds, 0 means no
    multilink: NotRequired[Literal["enable", "disable"]]  # Enable/disable PPP multilink support.
    mrru: NotRequired[int]  # PPP MRRU (296 - 65535, default = 1500).
    detected_peer_mtu: NotRequired[int]  # MTU of detected peer (0 - 4294967295).
    disc_retry_timeout: NotRequired[int]  # Time in seconds to wait before retrying to start a PPPoE dis
    padt_retry_timeout: NotRequired[int]  # PPPoE Active Discovery Terminate (PADT) used to terminate se
    service_name: NotRequired[str]  # PPPoE service name.
    ac_name: NotRequired[str]  # PPPoE server name.
    lcp_echo_interval: NotRequired[int]  # Time in seconds between PPPoE Link Control Protocol (LCP) ec
    lcp_max_echo_fails: NotRequired[int]  # Maximum missed LCP echo messages before disconnect.
    defaultgw: NotRequired[Literal["enable", "disable"]]  # Enable to get the gateway IP from the DHCP or PPPoE server.
    dns_server_override: NotRequired[Literal["enable", "disable"]]  # Enable/disable use DNS acquired by DHCP or PPPoE.
    dns_server_protocol: NotRequired[Literal["cleartext", "dot", "doh"]]  # DNS transport protocols.
    auth_type: NotRequired[Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]]  # PPP authentication type to use.
    pptp_client: NotRequired[Literal["enable", "disable"]]  # Enable/disable PPTP client.
    pptp_user: NotRequired[str]  # PPTP user name.
    pptp_password: NotRequired[str]  # PPTP password.
    pptp_server_ip: NotRequired[str]  # PPTP server IP address.
    pptp_auth_type: NotRequired[Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]]  # PPTP authentication type.
    pptp_timeout: NotRequired[int]  # Idle timer in minutes (0 for disabled).
    arpforward: NotRequired[Literal["enable", "disable"]]  # Enable/disable ARP forwarding.
    ndiscforward: NotRequired[Literal["enable", "disable"]]  # Enable/disable NDISC forwarding.
    broadcast_forward: NotRequired[Literal["enable", "disable"]]  # Enable/disable broadcast forwarding.
    bfd: NotRequired[Literal["global", "enable", "disable"]]  # Bidirectional Forwarding Detection (BFD) settings.
    bfd_desired_min_tx: NotRequired[int]  # BFD desired minimal transmit interval.
    bfd_detect_mult: NotRequired[int]  # BFD detection multiplier.
    bfd_required_min_rx: NotRequired[int]  # BFD required minimal receive interval.
    l2forward: NotRequired[Literal["enable", "disable"]]  # Enable/disable l2 forwarding.
    icmp_send_redirect: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending of ICMP redirects.
    icmp_accept_redirect: NotRequired[Literal["enable", "disable"]]  # Enable/disable ICMP accept redirect.
    reachable_time: NotRequired[int]  # IPv4 reachable time in milliseconds (30000 - 3600000, defaul
    vlanforward: NotRequired[Literal["enable", "disable"]]  # Enable/disable traffic forwarding between VLANs on this inte
    stpforward: NotRequired[Literal["enable", "disable"]]  # Enable/disable STP forwarding.
    stpforward_mode: NotRequired[Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"]]  # Configure STP forwarding mode.
    ips_sniffer_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable the use of this interface as a one-armed snif
    ident_accept: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication for this interface.
    ipmac: NotRequired[Literal["enable", "disable"]]  # Enable/disable IP/MAC binding.
    subst: NotRequired[Literal["enable", "disable"]]  # Enable to always send packets from this interface to a desti
    macaddr: NotRequired[str]  # Change the interface's MAC address.
    virtual_mac: NotRequired[str]  # Change the interface's virtual MAC address.
    substitute_dst_mac: NotRequired[str]  # Destination MAC address that all packets are sent to from th
    speed: NotRequired[Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"]]  # Interface speed. The default setting and the options availab
    status: NotRequired[Literal["up", "down"]]  # Bring the interface up or shut the interface down.
    netbios_forward: NotRequired[Literal["disable", "enable"]]  # Enable/disable NETBIOS forwarding.
    wins_ip: NotRequired[str]  # WINS server IP.
    type: NotRequired[Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"]]  # Interface type.
    dedicated_to: NotRequired[Literal["none", "management"]]  # Configure interface for single purpose.
    trust_ip_1: NotRequired[str]  # Trusted host for dedicated management traffic (0.0.0.0/24 fo
    trust_ip_2: NotRequired[str]  # Trusted host for dedicated management traffic (0.0.0.0/24 fo
    trust_ip_3: NotRequired[str]  # Trusted host for dedicated management traffic (0.0.0.0/24 fo
    trust_ip6_1: NotRequired[str]  # Trusted IPv6 host for dedicated management traffic (::/0 for
    trust_ip6_2: NotRequired[str]  # Trusted IPv6 host for dedicated management traffic (::/0 for
    trust_ip6_3: NotRequired[str]  # Trusted IPv6 host for dedicated management traffic (::/0 for
    ring_rx: NotRequired[int]  # RX ring size.
    ring_tx: NotRequired[int]  # TX ring size.
    wccp: NotRequired[Literal["enable", "disable"]]  # Enable/disable WCCP on this interface. Used for encapsulated
    netflow_sampler: NotRequired[Literal["disable", "tx", "rx", "both"]]  # Enable/disable NetFlow on this interface and set the data th
    netflow_sample_rate: NotRequired[int]  # NetFlow sample rate.  Sample one packet every configured num
    netflow_sampler_id: NotRequired[int]  # Netflow sampler ID.
    sflow_sampler: NotRequired[Literal["enable", "disable"]]  # Enable/disable sFlow on this interface.
    drop_fragment: NotRequired[Literal["enable", "disable"]]  # Enable/disable drop fragment packets.
    src_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable source IP check.
    sample_rate: NotRequired[int]  # sFlow sample rate (10 - 99999).
    polling_interval: NotRequired[int]  # sFlow polling interval in seconds (1 - 255).
    sample_direction: NotRequired[Literal["tx", "rx", "both"]]  # Data that NetFlow collects (rx, tx, or both).
    explicit_web_proxy: NotRequired[Literal["enable", "disable"]]  # Enable/disable the explicit web proxy on this interface.
    explicit_ftp_proxy: NotRequired[Literal["enable", "disable"]]  # Enable/disable the explicit FTP proxy on this interface.
    proxy_captive_portal: NotRequired[Literal["enable", "disable"]]  # Enable/disable proxy captive portal on this interface.
    tcp_mss: NotRequired[int]  # TCP maximum segment size. 0 means do not change segment size
    inbandwidth: NotRequired[int]  # Bandwidth limit for incoming traffic (0 - 80000000 kbps), 0 
    outbandwidth: NotRequired[int]  # Bandwidth limit for outgoing traffic (0 - 80000000 kbps).
    egress_shaping_profile: NotRequired[str]  # Outgoing traffic shaping profile.
    ingress_shaping_profile: NotRequired[str]  # Incoming traffic shaping profile.
    spillover_threshold: NotRequired[int]  # Egress Spillover threshold (0 - 16776000 kbps), 0 means unli
    ingress_spillover_threshold: NotRequired[int]  # Ingress Spillover threshold (0 - 16776000 kbps), 0 means unl
    weight: NotRequired[int]  # Default weight for static routes (if route has no weight con
    interface: str  # Interface name.
    external: NotRequired[Literal["enable", "disable"]]  # Enable/disable identifying the interface as an external inte
    mtu_override: NotRequired[Literal["enable", "disable"]]  # Enable to set a custom MTU for this interface.
    mtu: NotRequired[int]  # MTU value for this interface.
    vlan_protocol: NotRequired[Literal["8021q", "8021ad"]]  # Ethernet protocol of VLAN.
    vlanid: NotRequired[int]  # VLAN ID (1 - 4094).
    forward_domain: NotRequired[int]  # Transparent mode forward domain.
    remote_ip: NotRequired[str]  # Remote IP address of tunnel.
    member: NotRequired[list[dict[str, Any]]]  # Physical interfaces that belong to the aggregate or redundan
    lacp_mode: NotRequired[Literal["static", "passive", "active"]]  # LACP mode.
    lacp_ha_secondary: NotRequired[Literal["enable", "disable"]]  # LACP HA secondary member.
    system_id_type: NotRequired[Literal["auto", "user"]]  # Method in which system ID is generated.
    system_id: str  # Define a system ID for the aggregate interface.
    lacp_speed: NotRequired[Literal["slow", "fast"]]  # How often the interface sends LACP messages.
    min_links: NotRequired[int]  # Minimum number of aggregated ports that must be up.
    min_links_down: NotRequired[Literal["operational", "administrative"]]  # Action to take when less than the configured minimum number 
    algorithm: NotRequired[Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"]]  # Frame distribution algorithm.
    link_up_delay: NotRequired[int]  # Number of milliseconds to wait before considering a link is 
    aggregate_type: NotRequired[Literal["physical", "vxlan"]]  # Type of aggregation.
    priority_override: NotRequired[Literal["enable", "disable"]]  # Enable/disable fail back to higher priority port once recove
    aggregate: NotRequired[str]  # Aggregate interface.
    redundant_interface: NotRequired[str]  # Redundant interface.
    devindex: NotRequired[int]  # Device Index.
    vindex: NotRequired[int]  # Switch control interface VLAN ID.
    switch: NotRequired[str]  # Contained in switch.
    description: NotRequired[str]  # Description.
    alias: NotRequired[str]  # Alias will be displayed with the interface name to make it e
    security_mode: NotRequired[Literal["none", "captive-portal", "802.1X"]]  # Turn on captive portal authentication for this interface.
    security_mac_auth_bypass: NotRequired[Literal["mac-auth-only", "enable", "disable"]]  # Enable/disable MAC authentication bypass.
    security_ip_auth_bypass: NotRequired[Literal["enable", "disable"]]  # Enable/disable IP authentication bypass.
    security_external_web: NotRequired[str]  # URL of external authentication web server.
    security_external_logout: NotRequired[str]  # URL of external authentication logout server.
    replacemsg_override_group: NotRequired[str]  # Replacement message override group.
    security_redirect_url: NotRequired[str]  # URL redirection after disclaimer/authentication.
    auth_cert: NotRequired[str]  # HTTPS server certificate.
    auth_portal_addr: NotRequired[str]  # Address of captive portal.
    security_exempt_list: NotRequired[str]  # Name of security-exempt-list.
    security_groups: NotRequired[list[dict[str, Any]]]  # User groups that can authenticate with the captive portal.
    ike_saml_server: NotRequired[str]  # Configure IKE authentication SAML server.
    device_identification: NotRequired[Literal["enable", "disable"]]  # Enable/disable passively gathering of device identity inform
    exclude_signatures: NotRequired[Literal["iot", "ot"]]  # Exclude IOT or OT application signatures.
    device_user_identification: NotRequired[Literal["enable", "disable"]]  # Enable/disable passive gathering of user identity informatio
    lldp_reception: NotRequired[Literal["enable", "disable", "vdom"]]  # Enable/disable Link Layer Discovery Protocol (LLDP) receptio
    lldp_transmission: NotRequired[Literal["enable", "disable", "vdom"]]  # Enable/disable Link Layer Discovery Protocol (LLDP) transmis
    lldp_network_policy: NotRequired[str]  # LLDP-MED network policy profile.
    estimated_upstream_bandwidth: NotRequired[int]  # Estimated maximum upstream bandwidth (kbps). Used to estimat
    estimated_downstream_bandwidth: NotRequired[int]  # Estimated maximum downstream bandwidth (kbps). Used to estim
    measured_upstream_bandwidth: NotRequired[int]  # Measured upstream bandwidth (kbps).
    measured_downstream_bandwidth: NotRequired[int]  # Measured downstream bandwidth (kbps).
    bandwidth_measure_time: NotRequired[int]  # Bandwidth measure time.
    monitor_bandwidth: NotRequired[Literal["enable", "disable"]]  # Enable monitoring bandwidth on this interface.
    vrrp_virtual_mac: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of virtual MAC for VRRP.
    vrrp: NotRequired[list[dict[str, Any]]]  # VRRP configuration.
    phy_setting: NotRequired[str]  # PHY settings
    role: NotRequired[Literal["lan", "wan", "dmz", "undefined"]]  # Interface role.
    snmp_index: NotRequired[int]  # Permanent SNMP Index of the interface.
    secondary_IP: NotRequired[Literal["enable", "disable"]]  # Enable/disable adding a secondary IP to this interface.
    secondaryip: NotRequired[list[dict[str, Any]]]  # Second IP address of interface.
    preserve_session_route: NotRequired[Literal["enable", "disable"]]  # Enable/disable preservation of session route when dirty.
    auto_auth_extension_device: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic authorization of dedicated Fortinet
    ap_discover: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic registration of unknown FortiAP dev
    fortilink_neighbor_detect: NotRequired[Literal["lldp", "fortilink"]]  # Protocol for FortiGate neighbor discovery.
    ip_managed_by_fortiipam: NotRequired[Literal["inherit-global", "enable", "disable"]]  # Enable/disable automatic IP address assignment of this inter
    managed_subnetwork_size: NotRequired[Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"]]  # Number of IP addresses to be allocated by FortiIPAM and used
    fortilink_split_interface: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiLink split interface to connect member l
    internal: NotRequired[int]  # Implicitly created.
    fortilink_backup_link: NotRequired[int]  # FortiLink split interface backup link.
    switch_controller_access_vlan: NotRequired[Literal["enable", "disable"]]  # Block FortiSwitch port-to-port traffic.
    switch_controller_traffic_policy: NotRequired[str]  # Switch controller traffic policy for the VLAN.
    switch_controller_rspan_mode: NotRequired[Literal["disable", "enable"]]  # Stop Layer2 MAC learning and interception of BPDUs and other
    switch_controller_netflow_collect: NotRequired[Literal["disable", "enable"]]  # NetFlow collection and processing.
    switch_controller_mgmt_vlan: NotRequired[int]  # VLAN to use for FortiLink management purposes.
    switch_controller_igmp_snooping: NotRequired[Literal["enable", "disable"]]  # Switch controller IGMP snooping.
    switch_controller_igmp_snooping_proxy: NotRequired[Literal["enable", "disable"]]  # Switch controller IGMP snooping proxy.
    switch_controller_igmp_snooping_fast_leave: NotRequired[Literal["enable", "disable"]]  # Switch controller IGMP snooping fast-leave.
    switch_controller_dhcp_snooping: NotRequired[Literal["enable", "disable"]]  # Switch controller DHCP snooping.
    switch_controller_dhcp_snooping_verify_mac: NotRequired[Literal["enable", "disable"]]  # Switch controller DHCP snooping verify MAC.
    switch_controller_dhcp_snooping_option82: NotRequired[Literal["enable", "disable"]]  # Switch controller DHCP snooping option82.
    dhcp_snooping_server_list: NotRequired[list[dict[str, Any]]]  # Configure DHCP server access list.
    switch_controller_arp_inspection: NotRequired[Literal["enable", "disable", "monitor"]]  # Enable/disable/Monitor FortiSwitch ARP inspection.
    switch_controller_learning_limit: NotRequired[int]  # Limit the number of dynamic MAC addresses on this VLAN (1 - 
    switch_controller_nac: NotRequired[str]  # Integrated FortiLink settings for managed FortiSwitch.
    switch_controller_dynamic: NotRequired[str]  # Integrated FortiLink settings for managed FortiSwitch.
    switch_controller_feature: NotRequired[Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"]]  # Interface's purpose when assigning traffic (read only).
    switch_controller_iot_scanning: NotRequired[Literal["enable", "disable"]]  # Enable/disable managed FortiSwitch IoT scanning.
    switch_controller_offload: NotRequired[Literal["enable", "disable"]]  # Enable/disable managed FortiSwitch routing offload.
    switch_controller_offload_ip: NotRequired[str]  # IP for routing offload on FortiSwitch.
    switch_controller_offload_gw: NotRequired[Literal["enable", "disable"]]  # Enable/disable managed FortiSwitch routing offload gateway.
    swc_vlan: NotRequired[int]  # Creation status for switch-controller VLANs.
    swc_first_create: NotRequired[int]  # Initial create for switch-controller VLANs.
    color: NotRequired[int]  # Color of icon on the GUI.
    tagging: NotRequired[list[dict[str, Any]]]  # Config object tagging.
    eap_supplicant: NotRequired[Literal["enable", "disable"]]  # Enable/disable EAP-Supplicant.
    eap_method: NotRequired[Literal["tls", "peap"]]  # EAP method.
    eap_identity: NotRequired[str]  # EAP identity.
    eap_password: NotRequired[str]  # EAP password.
    eap_ca_cert: NotRequired[str]  # EAP CA certificate name.
    eap_user_cert: NotRequired[str]  # EAP user certificate name.
    default_purdue_level: NotRequired[Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]]  # default purdue level of device detected on this interface.
    ipv6: NotRequired[str]  # IPv6 of interface.
    physical: NotRequired[str]  # Print physical interface information.


class InterfaceObject(FortiObject[InterfacePayload]):
    """Typed FortiObject for system/interface with IDE autocomplete support."""
    
    # Name.
    name: str
    # Interface is in this virtual domain (VDOM).
    vdom: str
    # Virtual Routing Forwarding ID.
    vrf: int
    # CLI connection status.
    cli_conn_status: int
    # Enable FortiLink to dedicate this interface to manage other Fortinet devices.
    fortilink: Literal["enable", "disable"]
    # Source IP address used in FortiLink over L3 connections.
    switch_controller_source_ip: Literal["outbound", "fixed"]
    # Addressing mode (static, DHCP, PPPoE).
    mode: Literal["static", "dhcp", "pppoe"]
    # DHCP client options.
    client_options: list[str]  # Auto-flattened from member_table
    # Distance for routes learned through PPPoE or DHCP, lower distance indicates pref
    distance: int
    # Priority of learned routes.
    priority: int
    # Specify how to select outgoing interface to reach server.
    dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    dhcp_relay_interface: str
    # VRF ID used for connection to server.
    dhcp_relay_vrf_select: int
    # Enable/disable setting of the broadcast flag in messages sent by the DHCP client
    dhcp_broadcast_flag: Literal["disable", "enable"]
    # Enable/disable allowing this interface to act as a DHCP relay.
    dhcp_relay_service: Literal["disable", "enable"]
    # DHCP relay IP address.
    dhcp_relay_ip: list[str]  # Auto-flattened from member_table
    # IP address used by the DHCP relay as its source IP.
    dhcp_relay_source_ip: str
    # DHCP relay circuit ID.
    dhcp_relay_circuit_id: str
    # DHCP relay link selection.
    dhcp_relay_link_selection: str
    # Enable/disable sending of DHCP requests to all servers.
    dhcp_relay_request_all_server: Literal["disable", "enable"]
    # Enable/disable relaying DHCP messages with no end option.
    dhcp_relay_allow_no_end_option: Literal["disable", "enable"]
    # DHCP relay type (regular or IPsec).
    dhcp_relay_type: Literal["regular", "ipsec"]
    # Enable/disable DHCP smart relay.
    dhcp_smart_relay: Literal["disable", "enable"]
    # Enable/disable DHCP relay agent option.
    dhcp_relay_agent_option: Literal["enable", "disable"]
    # Enable/disable addition of classless static routes retrieved from DHCP server.
    dhcp_classless_route_addition: Literal["enable", "disable"]
    # High Availability in-band management IP address of this interface.
    management_ip: str
    # Interface IPv4 address and subnet mask, syntax: X.X.X.X/24.
    ip: str
    # Permitted types of management access to this interface.
    allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"]
    # Enable/disable detect gateway alive for first.
    gwdetect: Literal["enable", "disable"]
    # PING server status.
    ping_serv_status: int
    # Gateway's ping server for this IP.
    detectserver: str
    # Protocols used to detect the server.
    detectprotocol: Literal["ping", "tcp-echo", "udp-echo"]
    # HA election priority for the PING server.
    ha_priority: int
    # Enable/disable fail detection features for this interface.
    fail_detect: Literal["enable", "disable"]
    # Options for detecting that this interface has failed.
    fail_detect_option: Literal["detectserver", "link-down"]
    # Select link-failed-signal or link-down method to alert about a failed link.
    fail_alert_method: Literal["link-failed-signal", "link-down"]
    # Action on FortiExtender when interface fail.
    fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"]
    # Names of the FortiGate interfaces to which the link failure alert is sent.
    fail_alert_interfaces: list[str]  # Auto-flattened from member_table
    # DHCP client identifier.
    dhcp_client_identifier: str
    # DHCP renew time in seconds (300-604800), 0 means use the renew time provided by 
    dhcp_renew_time: int
    # Unnumbered IP used for PPPoE interfaces for which no unique local address is pro
    ipunnumbered: str
    # Username of the PPPoE account, provided by your ISP.
    username: str
    # CoS in VLAN tag for outgoing PPPoE/PPP packets.
    pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"]
    # Enable/disable PPPoE unnumbered negotiation.
    pppoe_unnumbered_negotiate: Literal["enable", "disable"]
    # PPPoE account's password.
    password: str
    # PPPoE auto disconnect after idle timeout seconds, 0 means no timeout.
    idle_timeout: int
    # Enable/disable PPP multilink support.
    multilink: Literal["enable", "disable"]
    # PPP MRRU (296 - 65535, default = 1500).
    mrru: int
    # MTU of detected peer (0 - 4294967295).
    detected_peer_mtu: int
    # Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no t
    disc_retry_timeout: int
    # PPPoE Active Discovery Terminate (PADT) used to terminate sessions after an idle
    padt_retry_timeout: int
    # PPPoE service name.
    service_name: str
    # PPPoE server name.
    ac_name: str
    # Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.
    lcp_echo_interval: int
    # Maximum missed LCP echo messages before disconnect.
    lcp_max_echo_fails: int
    # Enable to get the gateway IP from the DHCP or PPPoE server.
    defaultgw: Literal["enable", "disable"]
    # Enable/disable use DNS acquired by DHCP or PPPoE.
    dns_server_override: Literal["enable", "disable"]
    # DNS transport protocols.
    dns_server_protocol: Literal["cleartext", "dot", "doh"]
    # PPP authentication type to use.
    auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]
    # Enable/disable PPTP client.
    pptp_client: Literal["enable", "disable"]
    # PPTP user name.
    pptp_user: str
    # PPTP password.
    pptp_password: str
    # PPTP server IP address.
    pptp_server_ip: str
    # PPTP authentication type.
    pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]
    # Idle timer in minutes (0 for disabled).
    pptp_timeout: int
    # Enable/disable ARP forwarding.
    arpforward: Literal["enable", "disable"]
    # Enable/disable NDISC forwarding.
    ndiscforward: Literal["enable", "disable"]
    # Enable/disable broadcast forwarding.
    broadcast_forward: Literal["enable", "disable"]
    # Bidirectional Forwarding Detection (BFD) settings.
    bfd: Literal["global", "enable", "disable"]
    # BFD desired minimal transmit interval.
    bfd_desired_min_tx: int
    # BFD detection multiplier.
    bfd_detect_mult: int
    # BFD required minimal receive interval.
    bfd_required_min_rx: int
    # Enable/disable l2 forwarding.
    l2forward: Literal["enable", "disable"]
    # Enable/disable sending of ICMP redirects.
    icmp_send_redirect: Literal["enable", "disable"]
    # Enable/disable ICMP accept redirect.
    icmp_accept_redirect: Literal["enable", "disable"]
    # IPv4 reachable time in milliseconds (30000 - 3600000, default = 30000).
    reachable_time: int
    # Enable/disable traffic forwarding between VLANs on this interface.
    vlanforward: Literal["enable", "disable"]
    # Enable/disable STP forwarding.
    stpforward: Literal["enable", "disable"]
    # Configure STP forwarding mode.
    stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"]
    # Enable/disable the use of this interface as a one-armed sniffer.
    ips_sniffer_mode: Literal["enable", "disable"]
    # Enable/disable authentication for this interface.
    ident_accept: Literal["enable", "disable"]
    # Enable/disable IP/MAC binding.
    ipmac: Literal["enable", "disable"]
    # Enable to always send packets from this interface to a destination MAC address.
    subst: Literal["enable", "disable"]
    # Change the interface's MAC address.
    macaddr: str
    # Change the interface's virtual MAC address.
    virtual_mac: str
    # Destination MAC address that all packets are sent to from this interface.
    substitute_dst_mac: str
    # Interface speed. The default setting and the options available depend on the int
    speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"]
    # Bring the interface up or shut the interface down.
    status: Literal["up", "down"]
    # Enable/disable NETBIOS forwarding.
    netbios_forward: Literal["disable", "enable"]
    # WINS server IP.
    wins_ip: str
    # Interface type.
    type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"]
    # Configure interface for single purpose.
    dedicated_to: Literal["none", "management"]
    # Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
    trust_ip_1: str
    # Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
    trust_ip_2: str
    # Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
    trust_ip_3: str
    # Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).
    trust_ip6_1: str
    # Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).
    trust_ip6_2: str
    # Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).
    trust_ip6_3: str
    # RX ring size.
    ring_rx: int
    # TX ring size.
    ring_tx: int
    # Enable/disable WCCP on this interface. Used for encapsulated WCCP communication 
    wccp: Literal["enable", "disable"]
    # Enable/disable NetFlow on this interface and set the data that NetFlow collects 
    netflow_sampler: Literal["disable", "tx", "rx", "both"]
    # NetFlow sample rate.  Sample one packet every configured number of packets
(1 - 
    netflow_sample_rate: int
    # Netflow sampler ID.
    netflow_sampler_id: int
    # Enable/disable sFlow on this interface.
    sflow_sampler: Literal["enable", "disable"]
    # Enable/disable drop fragment packets.
    drop_fragment: Literal["enable", "disable"]
    # Enable/disable source IP check.
    src_check: Literal["enable", "disable"]
    # sFlow sample rate (10 - 99999).
    sample_rate: int
    # sFlow polling interval in seconds (1 - 255).
    polling_interval: int
    # Data that NetFlow collects (rx, tx, or both).
    sample_direction: Literal["tx", "rx", "both"]
    # Enable/disable the explicit web proxy on this interface.
    explicit_web_proxy: Literal["enable", "disable"]
    # Enable/disable the explicit FTP proxy on this interface.
    explicit_ftp_proxy: Literal["enable", "disable"]
    # Enable/disable proxy captive portal on this interface.
    proxy_captive_portal: Literal["enable", "disable"]
    # TCP maximum segment size. 0 means do not change segment size.
    tcp_mss: int
    # Bandwidth limit for incoming traffic (0 - 80000000 kbps), 0 means unlimited.
    inbandwidth: int
    # Bandwidth limit for outgoing traffic (0 - 80000000 kbps).
    outbandwidth: int
    # Outgoing traffic shaping profile.
    egress_shaping_profile: str
    # Incoming traffic shaping profile.
    ingress_shaping_profile: str
    # Egress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.
    spillover_threshold: int
    # Ingress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.
    ingress_spillover_threshold: int
    # Default weight for static routes (if route has no weight configured).
    weight: int
    # Interface name.
    interface: str
    # Enable/disable identifying the interface as an external interface (which usually
    external: Literal["enable", "disable"]
    # Enable to set a custom MTU for this interface.
    mtu_override: Literal["enable", "disable"]
    # MTU value for this interface.
    mtu: int
    # Ethernet protocol of VLAN.
    vlan_protocol: Literal["8021q", "8021ad"]
    # VLAN ID (1 - 4094).
    vlanid: int
    # Transparent mode forward domain.
    forward_domain: int
    # Remote IP address of tunnel.
    remote_ip: str
    # Physical interfaces that belong to the aggregate or redundant interface.
    member: list[str]  # Auto-flattened from member_table
    # LACP mode.
    lacp_mode: Literal["static", "passive", "active"]
    # LACP HA secondary member.
    lacp_ha_secondary: Literal["enable", "disable"]
    # Method in which system ID is generated.
    system_id_type: Literal["auto", "user"]
    # Define a system ID for the aggregate interface.
    system_id: str
    # How often the interface sends LACP messages.
    lacp_speed: Literal["slow", "fast"]
    # Minimum number of aggregated ports that must be up.
    min_links: int
    # Action to take when less than the configured minimum number of links are active.
    min_links_down: Literal["operational", "administrative"]
    # Frame distribution algorithm.
    algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"]
    # Number of milliseconds to wait before considering a link is up.
    link_up_delay: int
    # Type of aggregation.
    aggregate_type: Literal["physical", "vxlan"]
    # Enable/disable fail back to higher priority port once recovered.
    priority_override: Literal["enable", "disable"]
    # Aggregate interface.
    aggregate: str
    # Redundant interface.
    redundant_interface: str
    # Device Index.
    devindex: int
    # Switch control interface VLAN ID.
    vindex: int
    # Contained in switch.
    switch: str
    # Description.
    description: str
    # Alias will be displayed with the interface name to make it easier to distinguish
    alias: str
    # Turn on captive portal authentication for this interface.
    security_mode: Literal["none", "captive-portal", "802.1X"]
    # Enable/disable MAC authentication bypass.
    security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"]
    # Enable/disable IP authentication bypass.
    security_ip_auth_bypass: Literal["enable", "disable"]
    # URL of external authentication web server.
    security_external_web: str
    # URL of external authentication logout server.
    security_external_logout: str
    # Replacement message override group.
    replacemsg_override_group: str
    # URL redirection after disclaimer/authentication.
    security_redirect_url: str
    # HTTPS server certificate.
    auth_cert: str
    # Address of captive portal.
    auth_portal_addr: str
    # Name of security-exempt-list.
    security_exempt_list: str
    # User groups that can authenticate with the captive portal.
    security_groups: list[str]  # Auto-flattened from member_table
    # Configure IKE authentication SAML server.
    ike_saml_server: str
    # Enable/disable passively gathering of device identity information about the devi
    device_identification: Literal["enable", "disable"]
    # Exclude IOT or OT application signatures.
    exclude_signatures: Literal["iot", "ot"]
    # Enable/disable passive gathering of user identity information about users on thi
    device_user_identification: Literal["enable", "disable"]
    # Enable/disable Link Layer Discovery Protocol (LLDP) reception.
    lldp_reception: Literal["enable", "disable", "vdom"]
    # Enable/disable Link Layer Discovery Protocol (LLDP) transmission.
    lldp_transmission: Literal["enable", "disable", "vdom"]
    # LLDP-MED network policy profile.
    lldp_network_policy: str
    # Estimated maximum upstream bandwidth (kbps). Used to estimate link utilization.
    estimated_upstream_bandwidth: int
    # Estimated maximum downstream bandwidth (kbps). Used to estimate link utilization
    estimated_downstream_bandwidth: int
    # Measured upstream bandwidth (kbps).
    measured_upstream_bandwidth: int
    # Measured downstream bandwidth (kbps).
    measured_downstream_bandwidth: int
    # Bandwidth measure time.
    bandwidth_measure_time: int
    # Enable monitoring bandwidth on this interface.
    monitor_bandwidth: Literal["enable", "disable"]
    # Enable/disable use of virtual MAC for VRRP.
    vrrp_virtual_mac: Literal["enable", "disable"]
    # VRRP configuration.
    vrrp: list[str]  # Auto-flattened from member_table
    # PHY settings
    phy_setting: str
    # Interface role.
    role: Literal["lan", "wan", "dmz", "undefined"]
    # Permanent SNMP Index of the interface.
    snmp_index: int
    # Enable/disable adding a secondary IP to this interface.
    secondary_IP: Literal["enable", "disable"]
    # Second IP address of interface.
    secondaryip: list[str]  # Auto-flattened from member_table
    # Enable/disable preservation of session route when dirty.
    preserve_session_route: Literal["enable", "disable"]
    # Enable/disable automatic authorization of dedicated Fortinet extension device on
    auto_auth_extension_device: Literal["enable", "disable"]
    # Enable/disable automatic registration of unknown FortiAP devices.
    ap_discover: Literal["enable", "disable"]
    # Protocol for FortiGate neighbor discovery.
    fortilink_neighbor_detect: Literal["lldp", "fortilink"]
    # Enable/disable automatic IP address assignment of this interface by FortiIPAM.
    ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"]
    # Number of IP addresses to be allocated by FortiIPAM and used by this FortiGate u
    managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"]
    # Enable/disable FortiLink split interface to connect member link to different For
    fortilink_split_interface: Literal["enable", "disable"]
    # Implicitly created.
    internal: int
    # FortiLink split interface backup link.
    fortilink_backup_link: int
    # Block FortiSwitch port-to-port traffic.
    switch_controller_access_vlan: Literal["enable", "disable"]
    # Switch controller traffic policy for the VLAN.
    switch_controller_traffic_policy: str
    # Stop Layer2 MAC learning and interception of BPDUs and other packets on this int
    switch_controller_rspan_mode: Literal["disable", "enable"]
    # NetFlow collection and processing.
    switch_controller_netflow_collect: Literal["disable", "enable"]
    # VLAN to use for FortiLink management purposes.
    switch_controller_mgmt_vlan: int
    # Switch controller IGMP snooping.
    switch_controller_igmp_snooping: Literal["enable", "disable"]
    # Switch controller IGMP snooping proxy.
    switch_controller_igmp_snooping_proxy: Literal["enable", "disable"]
    # Switch controller IGMP snooping fast-leave.
    switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"]
    # Switch controller DHCP snooping.
    switch_controller_dhcp_snooping: Literal["enable", "disable"]
    # Switch controller DHCP snooping verify MAC.
    switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"]
    # Switch controller DHCP snooping option82.
    switch_controller_dhcp_snooping_option82: Literal["enable", "disable"]
    # Configure DHCP server access list.
    dhcp_snooping_server_list: list[str]  # Auto-flattened from member_table
    # Enable/disable/Monitor FortiSwitch ARP inspection.
    switch_controller_arp_inspection: Literal["enable", "disable", "monitor"]
    # Limit the number of dynamic MAC addresses on this VLAN (1 - 128, 0 = no limit, d
    switch_controller_learning_limit: int
    # Integrated FortiLink settings for managed FortiSwitch.
    switch_controller_nac: str
    # Integrated FortiLink settings for managed FortiSwitch.
    switch_controller_dynamic: str
    # Interface's purpose when assigning traffic (read only).
    switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"]
    # Enable/disable managed FortiSwitch IoT scanning.
    switch_controller_iot_scanning: Literal["enable", "disable"]
    # Enable/disable managed FortiSwitch routing offload.
    switch_controller_offload: Literal["enable", "disable"]
    # IP for routing offload on FortiSwitch.
    switch_controller_offload_ip: str
    # Enable/disable managed FortiSwitch routing offload gateway.
    switch_controller_offload_gw: Literal["enable", "disable"]
    # Creation status for switch-controller VLANs.
    swc_vlan: int
    # Initial create for switch-controller VLANs.
    swc_first_create: int
    # Color of icon on the GUI.
    color: int
    # Config object tagging.
    tagging: list[str]  # Auto-flattened from member_table
    # Enable/disable EAP-Supplicant.
    eap_supplicant: Literal["enable", "disable"]
    # EAP method.
    eap_method: Literal["tls", "peap"]
    # EAP identity.
    eap_identity: str
    # EAP password.
    eap_password: str
    # EAP CA certificate name.
    eap_ca_cert: str
    # EAP user certificate name.
    eap_user_cert: str
    # default purdue level of device detected on this interface.
    default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
    # IPv6 of interface.
    ipv6: str
    # Print physical interface information.
    physical: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> InterfacePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Interface:
    """
    Configure interfaces.
    
    Path: system/interface
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
    ) -> InterfaceObject: ...
    
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
    ) -> list[InterfaceObject]: ...
    
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
    ) -> InterfaceObject | list[InterfaceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | list[dict[str, Any]] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | list[dict[str, Any]] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | list[dict[str, Any]] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | list[dict[str, Any]] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> InterfaceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | list[dict[str, Any]] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | list[dict[str, Any]] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | list[dict[str, Any]] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | list[dict[str, Any]] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | list[dict[str, Any]] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | list[dict[str, Any]] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | list[dict[str, Any]] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | list[dict[str, Any]] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | list[dict[str, Any]] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | list[dict[str, Any]] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | list[dict[str, Any]] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | list[dict[str, Any]] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | list[dict[str, Any]] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | list[dict[str, Any]] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | list[dict[str, Any]] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | list[dict[str, Any]] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> InterfaceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | list[dict[str, Any]] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | list[dict[str, Any]] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | list[dict[str, Any]] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | list[dict[str, Any]] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | list[dict[str, Any]] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | list[dict[str, Any]] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | list[dict[str, Any]] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | list[dict[str, Any]] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | list[dict[str, Any]] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | list[dict[str, Any]] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | list[dict[str, Any]] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | list[dict[str, Any]] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
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
    ) -> InterfaceObject: ...
    
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
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | list[dict[str, Any]] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | list[dict[str, Any]] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | list[dict[str, Any]] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | list[dict[str, Any]] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
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
    "Interface",
    "InterfacePayload",
    "InterfaceObject",
]