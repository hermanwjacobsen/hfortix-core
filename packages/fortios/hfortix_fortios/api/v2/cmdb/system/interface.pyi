from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class InterfacePayload(TypedDict, total=False):
    """
    Type hints for system/interface payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    dhcp_relay_ip: NotRequired[str]  # DHCP relay IP address.
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


class Interface:
    """
    Configure interfaces.
    
    Path: system/interface
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
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
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
        payload_dict: InterfacePayload | None = ...,
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