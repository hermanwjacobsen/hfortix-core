from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ManagedSwitchPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/managed_switch payload fields.
    
    Configure FortiSwitch devices that are managed by this FortiGate.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.switch-controller.ptp.profile.ProfileEndpoint` (via: ptp-profile)
        - :class:`~.switch-controller.security-policy.local-access.LocalAccessEndpoint` (via: access-profile)
        - :class:`~.switch-controller.switch-profile.SwitchProfileEndpoint` (via: switch-profile)
        - :class:`~.system.interface.InterfaceEndpoint` (via: fsw-wan1-peer)

    **Usage:**
        payload: ManagedSwitchPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    switch_id: str  # Managed-switch name.
    sn: str  # Managed-switch serial number.
    description: NotRequired[str]  # Description.
    switch_profile: NotRequired[str]  # FortiSwitch profile.
    access_profile: NotRequired[str]  # FortiSwitch access profile.
    purdue_level: NotRequired[Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]]  # Purdue Level of this FortiSwitch.
    fsw_wan1_peer: str  # FortiSwitch WAN1 peer port.
    fsw_wan1_admin: NotRequired[Literal["discovered", "disable", "enable"]]  # FortiSwitch WAN1 admin status; enable to authorize the Forti
    poe_pre_standard_detection: NotRequired[Literal["enable", "disable"]]  # Enable/disable PoE pre-standard detection.
    dhcp_server_access_list: NotRequired[Literal["global", "enable", "disable"]]  # DHCP snooping server access list.
    poe_detection_type: NotRequired[int]  # PoE detection type for FortiSwitch.
    max_poe_budget: NotRequired[int]  # Max PoE budget for FortiSwitch.
    directly_connected: NotRequired[int]  # Directly connected FortiSwitch.
    version: NotRequired[int]  # FortiSwitch version.
    max_allowed_trunk_members: NotRequired[int]  # FortiSwitch maximum allowed trunk members.
    pre_provisioned: NotRequired[int]  # Pre-provisioned managed switch.
    l3_discovered: NotRequired[int]  # Layer 3 management discovered.
    mgmt_mode: NotRequired[int]  # FortiLink management mode.
    tunnel_discovered: NotRequired[int]  # SOCKS tunnel management discovered.
    tdr_supported: NotRequired[str]  # TDR supported.
    dynamic_capability: NotRequired[str]  # List of features this FortiSwitch supports
    switch_device_tag: NotRequired[str]  # User definable label/tag.
    switch_dhcp_opt43_key: NotRequired[str]  # DHCP option43 key.
    mclag_igmp_snooping_aware: NotRequired[Literal["enable", "disable"]]  # Enable/disable MCLAG IGMP-snooping awareness.
    dynamically_discovered: NotRequired[int]  # Dynamically discovered FortiSwitch.
    ptp_status: NotRequired[Literal["disable", "enable"]]  # Enable/disable PTP profile on this FortiSwitch.
    ptp_profile: NotRequired[str]  # PTP profile configuration.
    radius_nas_ip_override: NotRequired[Literal["disable", "enable"]]  # Use locally defined NAS-IP.
    radius_nas_ip: str  # NAS-IP address.
    route_offload: NotRequired[Literal["disable", "enable"]]  # Enable/disable route offload on this FortiSwitch.
    route_offload_mclag: NotRequired[Literal["disable", "enable"]]  # Enable/disable route offload MCLAG on this FortiSwitch.
    route_offload_router: NotRequired[list[dict[str, Any]]]  # Configure route offload MCLAG IP address.
    vlan: NotRequired[list[dict[str, Any]]]  # Configure VLAN assignment priority.
    type: NotRequired[Literal["virtual", "physical"]]  # Indication of switch type, physical or virtual.
    owner_vdom: NotRequired[str]  # VDOM which owner of port belongs to.
    flow_identity: NotRequired[str]  # Flow-tracking netflow ipfix switch identity in hex format
    staged_image_version: NotRequired[str]  # Staged image version for FortiSwitch.
    delayed_restart_trigger: NotRequired[int]  # Delayed restart triggered for this FortiSwitch.
    firmware_provision: NotRequired[Literal["enable", "disable"]]  # Enable/disable provisioning of firmware to FortiSwitches on
    firmware_provision_version: NotRequired[str]  # Firmware version to provision to this FortiSwitch on bootup
    firmware_provision_latest: NotRequired[Literal["disable", "once"]]  # Enable/disable one-time automatic provisioning of the latest
    ports: NotRequired[list[dict[str, Any]]]  # Managed-switch port list.
    ip_source_guard: NotRequired[list[dict[str, Any]]]  # IP source guard.
    stp_settings: NotRequired[str]  # Configuration method to edit Spanning Tree Protocol (STP) se
    stp_instance: NotRequired[list[dict[str, Any]]]  # Configuration method to edit Spanning Tree Protocol (STP) in
    override_snmp_sysinfo: NotRequired[Literal["disable", "enable"]]  # Enable/disable overriding the global SNMP system information
    snmp_sysinfo: NotRequired[str]  # Configuration method to edit Simple Network Management Proto
    override_snmp_trap_threshold: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the global SNMP trap threshold val
    snmp_trap_threshold: NotRequired[str]  # Configuration method to edit Simple Network Management Proto
    override_snmp_community: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the global SNMP communities.
    snmp_community: NotRequired[list[dict[str, Any]]]  # Configuration method to edit Simple Network Management Proto
    override_snmp_user: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the global SNMP users.
    snmp_user: NotRequired[list[dict[str, Any]]]  # Configuration method to edit Simple Network Management Proto
    qos_drop_policy: NotRequired[Literal["taildrop", "random-early-detection"]]  # Set QoS drop-policy.
    qos_red_probability: NotRequired[int]  # Set QoS RED/WRED drop probability.
    switch_log: NotRequired[str]  # Configuration method to edit FortiSwitch logging settings
    remote_log: NotRequired[list[dict[str, Any]]]  # Configure logging by FortiSwitch device to a remote syslog s
    storm_control: NotRequired[str]  # Configuration method to edit FortiSwitch storm control for m
    mirror: NotRequired[list[dict[str, Any]]]  # Configuration method to edit FortiSwitch packet mirror.
    static_mac: NotRequired[list[dict[str, Any]]]  # Configuration method to edit FortiSwitch Static and Sticky M
    custom_command: NotRequired[list[dict[str, Any]]]  # Configuration method to edit FortiSwitch commands to be push
    dhcp_snooping_static_client: NotRequired[list[dict[str, Any]]]  # Configure FortiSwitch DHCP snooping static clients.
    igmp_snooping: NotRequired[str]  # Configure FortiSwitch IGMP snooping global settings.
    x802_1X_settings: NotRequired[str]  # Configuration method to edit FortiSwitch 802.1X global setti
    router_vrf: NotRequired[list[dict[str, Any]]]  # Configure VRF.
    system_interface: NotRequired[list[dict[str, Any]]]  # Configure system interface on FortiSwitch.
    router_static: NotRequired[list[dict[str, Any]]]  # Configure static routes.
    system_dhcp_server: NotRequired[list[dict[str, Any]]]  # Configure DHCP servers.

# Nested classes for table field children

@final
class ManagedSwitchRouteoffloadrouterObject:
    """Typed object for route-offload-router table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VLAN name.
    vlan_name: str
    # Router IP address.
    router_ip: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchVlanObject:
    """Typed object for vlan table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VLAN name.
    vlan_name: str
    # 802.1x Radius (Tunnel-Private-Group-Id) VLANID assign-by-name priority. A smalle
    assignment_priority: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchPortsObject:
    """Typed object for ports table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Switch port name.
    port_name: str
    # Switch port name.
    port_owner: str
    # Switch id.
    switch_id: str
    # Switch port speed; default and available settings depend on hardware.
    speed: Literal["10half", "10full", "100half", "100full", "1000full", "10000full", "auto", "1000auto", "1000full-fiber", "40000full", "auto-module", "100FX-half", "100FX-full", "100000full", "2500auto", "2500full", "25000full", "50000full", "10000cr", "10000sr", "100000sr4", "100000cr4", "40000sr4", "40000cr4", "40000auto", "25000cr", "25000sr", "50000cr", "50000sr", "5000auto", "sgmii-auto"]
    # Switch port admin status: up or down.
    status: Literal["up", "down"]
    # Enable/disable PoE status.
    poe_status: Literal["enable", "disable"]
    # Enable/disable IP source guard.
    ip_source_guard: Literal["disable", "enable"]
    # Enable/disable PTP policy on this FortiSwitch port.
    ptp_status: Literal["disable", "enable"]
    # PTP policy configuration.
    ptp_policy: str
    # LACP member select mode.
    aggregator_mode: Literal["bandwidth", "count"]
    # Enable/disable flap guard.
    flapguard: Literal["enable", "disable"]
    # Number of stage change events needed within flap-duration.
    flap_rate: int
    # Period over which flap events are calculated (seconds).
    flap_duration: int
    # Flap guard disabling protection (min).
    flap_timeout: int
    # Enable/disable inter-operability with rapid PVST on this interface.
    rpvst_port: Literal["disabled", "enabled"]
    # Enable/disable PoE pre-standard detection.
    poe_pre_standard_detection: Literal["enable", "disable"]
    # Port number.
    port_number: int
    # Port prefix type.
    port_prefix_type: int
    # FortiLink uplink port.
    fortilink_port: int
    # PoE capable.
    poe_capable: int
    # Powered device capable.
    pd_capable: int
    # Stacking port.
    stacking_port: int
    # General peer to peer tunnel port.
    p2p_port: int
    # MCLAG-ICL port.
    mclag_icl_port: int
    # Peer to Peer Authenticated port.
    authenticated_port: int
    # Peer to Peer Restricted Authenticated port.
    restricted_auth_port: int
    # Peer to Peer Encrypted port.
    encrypted_port: int
    # Fiber-port.
    fiber_port: int
    # Media type.
    media_type: str
    # PoE standard supported.
    poe_standard: str
    # PoE maximum power.
    poe_max_power: str
    # PoE mode IEEE 802.3BT capable.
    poe_mode_bt_cabable: int
    # Configure PoE port mode.
    poe_port_mode: Literal["ieee802-3af", "ieee802-3at", "ieee802-3bt"]
    # Configure PoE port priority.
    poe_port_priority: Literal["critical-priority", "high-priority", "low-priority", "medium-priority"]
    # Configure PoE port power.
    poe_port_power: Literal["normal", "perpetual", "perpetual-fast"]
    # Port properties flags.
    flags: int
    # ISL local trunk name.
    isl_local_trunk_name: str
    # ISL peer port name.
    isl_peer_port_name: str
    # ISL peer device name.
    isl_peer_device_name: str
    # ISL peer device serial number.
    isl_peer_device_sn: str
    # FGT peer port name.
    fgt_peer_port_name: str
    # FGT peer device name.
    fgt_peer_device_name: str
    # Assign switch ports to a VLAN.
    vlan: str
    # Enable/disable all defined vlans on this port.
    allowed_vlans_all: Literal["enable", "disable"]
    # Configure switch port tagged VLANs.
    allowed_vlans: str
    # Configure switch port untagged VLANs.
    untagged_vlans: str
    # Interface type: physical or trunk port.
    type: Literal["physical", "trunk"]
    # Access mode of the port.
    access_mode: Literal["dynamic", "nac", "static"]
    # Matched child policy in the dynamic port policy.
    matched_dpp_policy: str
    # Matched interface tags in the dynamic port policy.
    matched_dpp_intf_tags: str
    # ACL groups on this port.
    acl_group: str
    # ACLs on this port.
    fortiswitch_acls: str
    # Trusted or untrusted DHCP-snooping interface.
    dhcp_snooping: Literal["untrusted", "trusted"]
    # Enable/disable allowance of DHCP with option-82 on untrusted interface.
    dhcp_snoop_option82_trust: Literal["enable", "disable"]
    # Configure DHCP snooping option 82 override.
    dhcp_snoop_option82_override: str
    # Trusted or untrusted dynamic ARP inspection.
    arp_inspection_trust: Literal["untrusted", "trusted"]
    # Enable/disable flooding of IGMP reports to this interface when igmp-snooping ena
    igmp_snooping_flood_reports: Literal["enable", "disable"]
    # Enable/disable flooding of IGMP snooping traffic to this interface.
    mcast_snooping_flood_traffic: Literal["enable", "disable"]
    # Enable/disable Spanning Tree Protocol (STP) on this interface.
    stp_state: Literal["enabled", "disabled"]
    # Enable/disable STP root guard on this interface.
    stp_root_guard: Literal["enabled", "disabled"]
    # Enable/disable STP BPDU guard on this interface.
    stp_bpdu_guard: Literal["enabled", "disabled"]
    # BPDU Guard disabling protection (0 - 120 min).
    stp_bpdu_guard_timeout: int
    # Enable/disable this interface as an edge port, bridging connections between work
    edge_port: Literal["enable", "disable"]
    # Configure discard mode for port.
    discard_mode: Literal["none", "all-untagged", "all-tagged"]
    # Enable/disable packet sampling on this interface.
    packet_sampler: Literal["enabled", "disabled"]
    # Packet sampling rate (0 - 99999 p/sec).
    packet_sample_rate: int
    # sFlow sampling counter polling interval in seconds (0 - 255).
    sflow_counter_interval: int
    # Packet sampling direction.
    sample_direction: Literal["tx", "rx", "both"]
    # FEC capable.
    fec_capable: int
    # State of forward error correction.
    fec_state: Literal["disabled", "cl74", "cl91", "detect-by-module"]
    # Flow control direction.
    flow_control: Literal["disable", "tx", "rx", "both"]
    # Configure ingress pause metering rate, in kbps (default = 0, disabled).
    pause_meter: int
    # Resume threshold for resuming traffic on ingress port.
    pause_meter_resume: Literal["75%", "50%", "25%"]
    # Enable/disable loop-guard on this interface, an STP optimization used to prevent
    loop_guard: Literal["enabled", "disabled"]
    # Loop-guard timeout (0 - 120 min, default = 45).
    loop_guard_timeout: int
    # Switch controller dynamic port policy from available options.
    port_policy: str
    # Switch controller QoS policy from available options.
    qos_policy: str
    # Switch controller storm control policy from available options.
    storm_control_policy: str
    # Switch controller authentication policy to apply to this managed switch from ava
    port_security_policy: str
    # Switch controller export port to pool-list.
    export_to_pool: str
    # Tag(s) associated with the interface for various features including virtual port
    interface_tags: str
    # Limit the number of dynamic MAC addresses on this Port
    learning_limit: int
    # Enable or disable sticky-mac on the interface.
    sticky_mac: Literal["enable", "disable"]
    # LLDP transmit and receive status.
    lldp_status: Literal["disable", "rx-only", "tx-only", "tx-rx"]
    # LLDP port TLV profile.
    lldp_profile: str
    # Export managed-switch port to a tenant VDOM.
    export_to: str
    # Port/Trunk MAC.
    mac_addr: str
    # Enable/Disable allow ARP monitor.
    allow_arp_monitor: Literal["disable", "enable"]
    # 802.1AD VLANs in the VDom.
    qnq: str
    # Enable/disable logging for dynamic MAC address events.
    log_mac_event: Literal["disable", "enable"]
    # Algorithm for aggregate port selection.
    port_selection_criteria: Literal["src-mac", "dst-mac", "src-dst-mac", "src-ip", "dst-ip", "src-dst-ip"]
    # Description for port.
    description: str
    # End Link Aggregation Control Protocol (LACP) messages every 30 seconds (slow) or
    lacp_speed: Literal["slow", "fast"]
    # LACP mode: ignore and do not send control messages, or negotiate 802.3ad aggrega
    mode: Literal["static", "lacp-passive", "lacp-active"]
    # Enable/disable Link Aggregation Group (LAG) bundling for non-FortiLink interface
    bundle: Literal["enable", "disable"]
    # Port behavior after it withdraws because of loss of control packets.
    member_withdrawal_behavior: Literal["forward", "block"]
    # Enable/disable multi-chassis link aggregation (MCLAG).
    mclag: Literal["enable", "disable"]
    # Minimum size of LAG bundle (1 - 24, default = 1).
    min_bundle: int
    # Maximum size of LAG bundle (1 - 24, default = 24).
    max_bundle: int
    # Aggregated LAG bundle interfaces.
    members: str
    # LACP fallback port.
    fallback_port: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchIpsourceguardObject:
    """Typed object for ip-source-guard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Ingress interface to which source guard is bound.
    port: str
    # Description.
    description: str
    # IP and MAC address configuration.
    binding_entry: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchStpinstanceObject:
    """Typed object for stp-instance table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Instance ID.
    id: str
    # Priority.
    priority: Literal["0", "4096", "8192", "12288", "16384", "20480", "24576", "28672", "32768", "36864", "40960", "45056", "49152", "53248", "57344", "61440"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchSnmpcommunityObject:
    """Typed object for snmp-community table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SNMP community ID.
    id: int
    # SNMP community name.
    name: str
    # Enable/disable this SNMP community.
    status: Literal["disable", "enable"]
    # Configure IPv4 SNMP managers (hosts).
    hosts: str
    # Enable/disable SNMP v1 queries.
    query_v1_status: Literal["disable", "enable"]
    # SNMP v1 query port (default = 161).
    query_v1_port: int
    # Enable/disable SNMP v2c queries.
    query_v2c_status: Literal["disable", "enable"]
    # SNMP v2c query port (default = 161).
    query_v2c_port: int
    # Enable/disable SNMP v1 traps.
    trap_v1_status: Literal["disable", "enable"]
    # SNMP v2c trap local port (default = 162).
    trap_v1_lport: int
    # SNMP v2c trap remote port (default = 162).
    trap_v1_rport: int
    # Enable/disable SNMP v2c traps.
    trap_v2c_status: Literal["disable", "enable"]
    # SNMP v2c trap local port (default = 162).
    trap_v2c_lport: int
    # SNMP v2c trap remote port (default = 162).
    trap_v2c_rport: int
    # SNMP notifications (traps) to send.
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchSnmpuserObject:
    """Typed object for snmp-user table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SNMP user name.
    name: str
    # Enable/disable SNMP queries for this user.
    queries: Literal["disable", "enable"]
    # SNMPv3 query port (default = 161).
    query_port: int
    # Security level for message authentication and encryption.
    security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"]
    # Authentication protocol.
    auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
    # Password for authentication protocol.
    auth_pwd: str
    # Privacy (encryption) protocol.
    priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"]
    # Password for privacy (encryption) protocol.
    priv_pwd: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchRemotelogObject:
    """Typed object for remote-log table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Remote log name.
    name: str
    # Enable/disable logging by FortiSwitch device to a remote syslog server.
    status: Literal["enable", "disable"]
    # IPv4 address of the remote syslog server.
    server: str
    # Remote syslog server listening port.
    port: int
    # Severity of logs to be transferred to remote log server.
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Enable/disable comma-separated value (CSV) strings.
    csv: Literal["enable", "disable"]
    # Facility to log to remote syslog server.
    facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchMirrorObject:
    """Typed object for mirror table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Mirror name.
    name: str
    # Active/inactive mirror configuration.
    status: Literal["active", "inactive"]
    # Enable/disable switching functionality when mirroring.
    switching_packet: Literal["enable", "disable"]
    # Destination port.
    dst: str
    # Source ingress interfaces.
    src_ingress: str
    # Source egress interfaces.
    src_egress: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchStaticmacObject:
    """Typed object for static-mac table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Type.
    type: Literal["static", "sticky"]
    # Vlan.
    vlan: str
    # MAC address.
    mac: str
    # Interface name.
    interface: str
    # Description.
    description: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchCustomcommandObject:
    """Typed object for custom-command table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # List of FortiSwitch commands.
    command_entry: str
    # Names of commands to be pushed to this FortiSwitch device, as configured under c
    command_name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchDhcpsnoopingstaticclientObject:
    """Typed object for dhcp-snooping-static-client table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Client name.
    name: str
    # VLAN name.
    vlan: str
    # Client static IP address.
    ip: str
    # Client MAC address.
    mac: str
    # Interface name.
    port: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchRoutervrfObject:
    """Typed object for router-vrf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VRF entry name.
    name: str
    # Switch ID.
    switch_id: str
    # VRF ID.
    vrfid: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchSysteminterfaceObject:
    """Typed object for system-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
    name: str
    # Switch ID.
    switch_id: str
    # Interface addressing mode.
    mode: Literal["static", "dhcp"]
    # IP and mask for this interface.
    ip: str
    # Enable/disable interface status.
    status: Literal["disable", "enable"]
    # Permitted types of management access to this interface.
    allowaccess: Literal["ping", "https", "http", "ssh", "snmp", "telnet", "radius-acct"]
    # VLAN name.
    vlan: str
    # Interface type.
    type: Literal["vlan", "physical"]
    # Interface name.
    interface: str
    # VRF for this route.
    vrf: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchRouterstaticObject:
    """Typed object for router-static table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry sequence number.
    id: int
    # Switch ID.
    switch_id: str
    # Enable/disable blackhole on this route.
    blackhole: Literal["disable", "enable"]
    # Comment.
    comment: str
    # Gateway out interface.
    device: str
    # Administrative distance for the route (1 - 255, default = 10).
    distance: int
    # Destination ip and mask for this route.
    dst: str
    # Enable/disable dynamic gateway.
    dynamic_gateway: Literal["disable", "enable"]
    # Gateway ip for this route.
    gateway: str
    # Enable/disable route status.
    status: Literal["disable", "enable"]
    # VRF for this route.
    vrf: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class ManagedSwitchSystemdhcpserverObject:
    """Typed object for system-dhcp-server table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Switch ID.
    switch_id: str
    # Enable/disable this DHCP configuration.
    status: Literal["disable", "enable"]
    # Lease time in seconds, 0 means unlimited.
    lease_time: int
    # Options for assigning DNS servers to DHCP clients.
    dns_service: Literal["local", "default", "specify"]
    # DNS server 1.
    dns_server1: str
    # DNS server 2.
    dns_server2: str
    # DNS server 3.
    dns_server3: str
    # Options for assigning Network Time Protocol (NTP) servers to DHCP clients.
    ntp_service: Literal["local", "default", "specify"]
    # NTP server 1.
    ntp_server1: str
    # NTP server 2.
    ntp_server2: str
    # NTP server 3.
    ntp_server3: str
    # Default gateway IP address assigned by the DHCP server.
    default_gateway: str
    # Netmask assigned by the DHCP server.
    netmask: str
    # DHCP server can assign IP configurations to clients connected to this interface.
    interface: str
    # DHCP IP range configuration.
    ip_range: str
    # DHCP options.
    options: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class ManagedSwitchResponse(TypedDict):
    """
    Type hints for switch_controller/managed_switch API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    switch_id: str
    sn: str
    description: str
    switch_profile: str
    access_profile: str
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
    fsw_wan1_peer: str
    fsw_wan1_admin: Literal["discovered", "disable", "enable"]
    poe_pre_standard_detection: Literal["enable", "disable"]
    dhcp_server_access_list: Literal["global", "enable", "disable"]
    poe_detection_type: int
    max_poe_budget: int
    directly_connected: int
    version: int
    max_allowed_trunk_members: int
    pre_provisioned: int
    l3_discovered: int
    mgmt_mode: int
    tunnel_discovered: int
    tdr_supported: str
    dynamic_capability: str
    switch_device_tag: str
    switch_dhcp_opt43_key: str
    mclag_igmp_snooping_aware: Literal["enable", "disable"]
    dynamically_discovered: int
    ptp_status: Literal["disable", "enable"]
    ptp_profile: str
    radius_nas_ip_override: Literal["disable", "enable"]
    radius_nas_ip: str
    route_offload: Literal["disable", "enable"]
    route_offload_mclag: Literal["disable", "enable"]
    route_offload_router: list[dict[str, Any]]
    vlan: list[dict[str, Any]]
    type: Literal["virtual", "physical"]
    owner_vdom: str
    flow_identity: str
    staged_image_version: str
    delayed_restart_trigger: int
    firmware_provision: Literal["enable", "disable"]
    firmware_provision_version: str
    firmware_provision_latest: Literal["disable", "once"]
    ports: list[dict[str, Any]]
    ip_source_guard: list[dict[str, Any]]
    stp_settings: str
    stp_instance: list[dict[str, Any]]
    override_snmp_sysinfo: Literal["disable", "enable"]
    snmp_sysinfo: str
    override_snmp_trap_threshold: Literal["enable", "disable"]
    snmp_trap_threshold: str
    override_snmp_community: Literal["enable", "disable"]
    snmp_community: list[dict[str, Any]]
    override_snmp_user: Literal["enable", "disable"]
    snmp_user: list[dict[str, Any]]
    qos_drop_policy: Literal["taildrop", "random-early-detection"]
    qos_red_probability: int
    switch_log: str
    remote_log: list[dict[str, Any]]
    storm_control: str
    mirror: list[dict[str, Any]]
    static_mac: list[dict[str, Any]]
    custom_command: list[dict[str, Any]]
    dhcp_snooping_static_client: list[dict[str, Any]]
    igmp_snooping: str
    x802_1X_settings: str
    router_vrf: list[dict[str, Any]]
    system_interface: list[dict[str, Any]]
    router_static: list[dict[str, Any]]
    system_dhcp_server: list[dict[str, Any]]


@final
class ManagedSwitchObject:
    """Typed FortiObject for switch_controller/managed_switch with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Managed-switch name.
    switch_id: str
    # Managed-switch serial number.
    sn: str
    # Description.
    description: str
    # FortiSwitch profile.
    switch_profile: str
    # FortiSwitch access profile.
    access_profile: str
    # Purdue Level of this FortiSwitch.
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
    # FortiSwitch WAN1 peer port.
    fsw_wan1_peer: str
    # FortiSwitch WAN1 admin status; enable to authorize the FortiSwitch as a managed
    fsw_wan1_admin: Literal["discovered", "disable", "enable"]
    # Enable/disable PoE pre-standard detection.
    poe_pre_standard_detection: Literal["enable", "disable"]
    # DHCP snooping server access list.
    dhcp_server_access_list: Literal["global", "enable", "disable"]
    # PoE detection type for FortiSwitch.
    poe_detection_type: int
    # Max PoE budget for FortiSwitch.
    max_poe_budget: int
    # Directly connected FortiSwitch.
    directly_connected: int
    # FortiSwitch version.
    version: int
    # FortiSwitch maximum allowed trunk members.
    max_allowed_trunk_members: int
    # Pre-provisioned managed switch.
    pre_provisioned: int
    # Layer 3 management discovered.
    l3_discovered: int
    # FortiLink management mode.
    mgmt_mode: int
    # SOCKS tunnel management discovered.
    tunnel_discovered: int
    # TDR supported.
    tdr_supported: str
    # List of features this FortiSwitch supports (not configurable) that is sent to th
    dynamic_capability: str
    # User definable label/tag.
    switch_device_tag: str
    # DHCP option43 key.
    switch_dhcp_opt43_key: str
    # Enable/disable MCLAG IGMP-snooping awareness.
    mclag_igmp_snooping_aware: Literal["enable", "disable"]
    # Dynamically discovered FortiSwitch.
    dynamically_discovered: int
    # Enable/disable PTP profile on this FortiSwitch.
    ptp_status: Literal["disable", "enable"]
    # PTP profile configuration.
    ptp_profile: str
    # Use locally defined NAS-IP.
    radius_nas_ip_override: Literal["disable", "enable"]
    # NAS-IP address.
    radius_nas_ip: str
    # Enable/disable route offload on this FortiSwitch.
    route_offload: Literal["disable", "enable"]
    # Enable/disable route offload MCLAG on this FortiSwitch.
    route_offload_mclag: Literal["disable", "enable"]
    # Configure route offload MCLAG IP address.
    route_offload_router: list[ManagedSwitchRouteoffloadrouterObject]  # Table field - list of typed objects
    # Configure VLAN assignment priority.
    vlan: list[ManagedSwitchVlanObject]  # Table field - list of typed objects
    # Indication of switch type, physical or virtual.
    type: Literal["virtual", "physical"]
    # VDOM which owner of port belongs to.
    owner_vdom: str
    # Flow-tracking netflow ipfix switch identity in hex format
    flow_identity: str
    # Staged image version for FortiSwitch.
    staged_image_version: str
    # Delayed restart triggered for this FortiSwitch.
    delayed_restart_trigger: int
    # Enable/disable provisioning of firmware to FortiSwitches on join connection.
    firmware_provision: Literal["enable", "disable"]
    # Firmware version to provision to this FortiSwitch on bootup
    firmware_provision_version: str
    # Enable/disable one-time automatic provisioning of the latest firmware version.
    firmware_provision_latest: Literal["disable", "once"]
    # Managed-switch port list.
    ports: list[ManagedSwitchPortsObject]  # Table field - list of typed objects
    # IP source guard.
    ip_source_guard: list[ManagedSwitchIpsourceguardObject]  # Table field - list of typed objects
    # Configuration method to edit Spanning Tree Protocol (STP) settings used to preve
    stp_settings: str
    # Configuration method to edit Spanning Tree Protocol (STP) instances.
    stp_instance: list[ManagedSwitchStpinstanceObject]  # Table field - list of typed objects
    # Enable/disable overriding the global SNMP system information.
    override_snmp_sysinfo: Literal["disable", "enable"]
    # Configuration method to edit Simple Network Management Protocol (SNMP) system in
    snmp_sysinfo: str
    # Enable/disable overriding the global SNMP trap threshold values.
    override_snmp_trap_threshold: Literal["enable", "disable"]
    # Configuration method to edit Simple Network Management Protocol (SNMP) trap thre
    snmp_trap_threshold: str
    # Enable/disable overriding the global SNMP communities.
    override_snmp_community: Literal["enable", "disable"]
    # Configuration method to edit Simple Network Management Protocol (SNMP) communiti
    snmp_community: list[ManagedSwitchSnmpcommunityObject]  # Table field - list of typed objects
    # Enable/disable overriding the global SNMP users.
    override_snmp_user: Literal["enable", "disable"]
    # Configuration method to edit Simple Network Management Protocol (SNMP) users.
    snmp_user: list[ManagedSwitchSnmpuserObject]  # Table field - list of typed objects
    # Set QoS drop-policy.
    qos_drop_policy: Literal["taildrop", "random-early-detection"]
    # Set QoS RED/WRED drop probability.
    qos_red_probability: int
    # Configuration method to edit FortiSwitch logging settings
    switch_log: str
    # Configure logging by FortiSwitch device to a remote syslog server.
    remote_log: list[ManagedSwitchRemotelogObject]  # Table field - list of typed objects
    # Configuration method to edit FortiSwitch storm control for measuring traffic act
    storm_control: str
    # Configuration method to edit FortiSwitch packet mirror.
    mirror: list[ManagedSwitchMirrorObject]  # Table field - list of typed objects
    # Configuration method to edit FortiSwitch Static and Sticky MAC.
    static_mac: list[ManagedSwitchStaticmacObject]  # Table field - list of typed objects
    # Configuration method to edit FortiSwitch commands to be pushed to this FortiSwit
    custom_command: list[ManagedSwitchCustomcommandObject]  # Table field - list of typed objects
    # Configure FortiSwitch DHCP snooping static clients.
    dhcp_snooping_static_client: list[ManagedSwitchDhcpsnoopingstaticclientObject]  # Table field - list of typed objects
    # Configure FortiSwitch IGMP snooping global settings.
    igmp_snooping: str
    # Configuration method to edit FortiSwitch 802.1X global settings.
    x802_1X_settings: str
    # Configure VRF.
    router_vrf: list[ManagedSwitchRoutervrfObject]  # Table field - list of typed objects
    # Configure system interface on FortiSwitch.
    system_interface: list[ManagedSwitchSysteminterfaceObject]  # Table field - list of typed objects
    # Configure static routes.
    router_static: list[ManagedSwitchRouterstaticObject]  # Table field - list of typed objects
    # Configure DHCP servers.
    system_dhcp_server: list[ManagedSwitchSystemdhcpserverObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ManagedSwitchPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class ManagedSwitch:
    """
    Configure FortiSwitch devices that are managed by this FortiGate.
    
    Path: switch_controller/managed_switch
    Category: cmdb
    Primary Key: switch-id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        switch_id: str,
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
    ) -> ManagedSwitchObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        switch_id: str,
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
    ) -> ManagedSwitchObject: ...
    
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
    ) -> list[ManagedSwitchObject]: ...
    
    @overload
    def get(
        self,
        switch_id: str | None = ...,
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
        switch_id: str,
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
    ) -> ManagedSwitchResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        switch_id: str,
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
    ) -> ManagedSwitchResponse: ...
    
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
    ) -> list[ManagedSwitchResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        switch_id: str | None = ...,
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
        switch_id: str | None = ...,
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
    ) -> ManagedSwitchObject | list[ManagedSwitchObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ManagedSwitchObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ManagedSwitchObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        switch_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ManagedSwitchObject: ...
    
    @overload
    def delete(
        self,
        switch_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        switch_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        switch_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        switch_id: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ManagedSwitch",
    "ManagedSwitchPayload",
    "ManagedSwitchObject",
]