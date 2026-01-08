from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SdwanPayload(TypedDict, total=False):
    """
    Type hints for system/sdwan payload fields.
    
    Configure redundant Internet connections with multiple outbound links and health-check profiles.
    
    **Usage:**
        payload: SdwanPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable SD-WAN.
    load_balance_mode: NotRequired[Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"]]  # Algorithm or mode to use for load balancing Internet traffic
    speedtest_bypass_routing: NotRequired[Literal["disable", "enable"]]  # Enable/disable bypass routing when speedtest on a SD-WAN mem
    duplication_max_num: NotRequired[int]  # Maximum number of interface members a packet is duplicated i
    duplication_max_discrepancy: NotRequired[int]  # Maximum discrepancy between two packets for deduplication in
    neighbor_hold_down: NotRequired[Literal["enable", "disable"]]  # Enable/disable hold switching from the secondary neighbor to
    neighbor_hold_down_time: NotRequired[int]  # Waiting period in seconds when switching from the secondary
    app_perf_log_period: NotRequired[int]  # Time interval in seconds that application performance logs a
    neighbor_hold_boot_time: NotRequired[int]  # Waiting period in seconds when switching from the primary ne
    fail_detect: NotRequired[Literal["enable", "disable"]]  # Enable/disable SD-WAN Internet connection status checking
    fail_alert_interfaces: NotRequired[list[dict[str, Any]]]  # Physical interfaces that will be alerted.
    zone: NotRequired[list[dict[str, Any]]]  # Configure SD-WAN zones.
    members: NotRequired[list[dict[str, Any]]]  # FortiGate interfaces added to the SD-WAN.
    health_check: NotRequired[list[dict[str, Any]]]  # SD-WAN status checking or health checking. Identify a server
    service: NotRequired[list[dict[str, Any]]]  # Create SD-WAN rules (also called services) to control how se
    neighbor: NotRequired[list[dict[str, Any]]]  # Create SD-WAN neighbor from BGP neighbor table to control ro
    duplication: NotRequired[list[dict[str, Any]]]  # Create SD-WAN duplication rule.

# Nested classes for table field children

@final
class SdwanFailalertinterfacesObject:
    """Typed object for fail-alert-interfaces table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Physical interface name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdwanZoneObject:
    """Typed object for zone table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Zone name.
    name: str
    # Enable/disable selection of ADVPN based on SDWAN information.
    advpn_select: Literal["enable", "disable"]
    # Health check for ADVPN local overlay link quality.
    advpn_health_check: str
    # Method of selecting member if more than one meets the SLA.
    service_sla_tie_break: Literal["cfg-order", "fib-best-match", "priority", "input-device"]
    # Minimum number of members which meet SLA when the neighbor is preferred.
    minimum_sla_meet_members: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdwanMembersObject:
    """Typed object for members table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Sequence number(1-512).
    seq_num: int
    # Interface name.
    interface: str
    # Zone name.
    zone: str
    # The default gateway for this interface. Usually the default gateway of the Inter
    gateway: str
    # Preferred source of route for this member.
    preferred_source: str
    # Source IP address used in the health-check packet to the server.
    source: str
    # IPv6 gateway.
    gateway6: str
    # Source IPv6 address used in the health-check packet to the server.
    source6: str
    # Cost of this interface for services in SLA mode (0 - 4294967295, default = 0).
    cost: int
    # Weight of this interface for weighted load balancing. (1 - 255) More traffic is
    weight: int
    # Priority of the interface for IPv4 (1 - 65535, default = 1). Used for SD-WAN rul
    priority: int
    # Priority of the interface for IPv6 (1 - 65535, default = 1024). Used for SD-WAN
    priority6: int
    # Preferred priority of routes to this member when this member is in-sla
    priority_in_sla: int
    # Preferred priority of routes to this member when this member is out-of-sla
    priority_out_sla: int
    # Egress spillover threshold for this interface (0 - 16776000 kbit/s). When this t
    spillover_threshold: int
    # Ingress spillover threshold for this interface (0 - 16776000 kbit/s). When this
    ingress_spillover_threshold: int
    # Measured volume ratio
    volume_ratio: int
    # Enable/disable this interface in the SD-WAN.
    status: Literal["disable", "enable"]
    # Measured transport group (0 - 255).
    transport_group: int
    # Comments.
    comment: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdwanHealthcheckObject:
    """Typed object for health-check table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Status check or health check name.
    name: str
    # Enable/disable use of FortiGuard predefined server.
    fortiguard: Literal["disable", "enable"]
    # Predefined health-check target name.
    fortiguard_name: str
    # Enable/disable transmission of probe packets.
    probe_packets: Literal["disable", "enable"]
    # Address mode (IPv4 or IPv6).
    addr_mode: Literal["ipv4", "ipv6"]
    # Enable/disable system DNS as the probe server.
    system_dns: Literal["disable", "enable"]
    # IP address or FQDN name of the server.
    server: str
    # The mode determining how to detect the server.
    detect_mode: Literal["active", "passive", "prefer-passive", "remote", "agent-based"]
    # Protocol used to determine if the FortiGate can communicate with the server.
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"]
    # Port number used to communicate with the server over the selected protocol
    port: int
    # Method to measure the quality of tcp-connect.
    quality_measured_method: Literal["half-open", "half-close"]
    # Twamp controller security mode.
    security_mode: Literal["none", "authentication"]
    # The user name to access probe server.
    user: str
    # TWAMP controller password in authentication mode.
    password: str
    # Packet size of a TWAMP test session. (124/158 - 1024)
    packet_size: int
    # HA election priority (1 - 50).
    ha_priority: int
    # FTP mode.
    ftp_mode: Literal["passive", "port"]
    # Full path and file name on the FTP server to download for FTP health-check to pr
    ftp_file: str
    # URL used to communicate with the server if the protocol if the protocol is HTTP.
    http_get: str
    # String in the http-agent field in the HTTP header.
    http_agent: str
    # Response string expected from the server if the protocol is HTTP.
    http_match: str
    # Fully qualified domain name to resolve for the DNS probe.
    dns_request_domain: str
    # Response IP expected from DNS server if the protocol is DNS.
    dns_match_ip: str
    # Status check interval in milliseconds, or the time between attempting to connect
    interval: int
    # Time to wait before a probe packet is considered lost
    probe_timeout: int
    # Time to wait before a probe packet is considered lost when detect-mode is agent
    agent_probe_timeout: int
    # Time to wait before a probe packet is considered lost when detect-mode is remote
    remote_probe_timeout: int
    # Number of failures before server is considered lost (1 - 3600, default = 5).
    failtime: int
    # Number of successful responses received before server is considered recovered
    recoverytime: int
    # Number of most recent probes that should be used to calculate latency and jitter
    probe_count: int
    # Differentiated services code point (DSCP) in the IP header of the probe packet.
    diffservcode: str
    # Enable/disable update cascade interface.
    update_cascade_interface: Literal["enable", "disable"]
    # Enable/disable updating the static route.
    update_static_route: Literal["enable", "disable"]
    # Enable/disable updating the BGP route.
    update_bgp_route: Literal["enable", "disable"]
    # Enable/disable embedding measured health information.
    embed_measured_health: Literal["enable", "disable"]
    # Select the ID from the SLA sub-table. The selected SLA's priority value will be
    sla_id_redistribute: int
    # Time interval in seconds that SLA fail log messages will be generated
    sla_fail_log_period: int
    # Time interval in seconds that SLA pass log messages will be generated
    sla_pass_log_period: int
    # Warning threshold for packet loss (percentage, default = 0).
    threshold_warning_packetloss: int
    # Alert threshold for packet loss (percentage, default = 0).
    threshold_alert_packetloss: int
    # Warning threshold for latency (ms, default = 0).
    threshold_warning_latency: int
    # Alert threshold for latency (ms, default = 0).
    threshold_alert_latency: int
    # Warning threshold for jitter (ms, default = 0).
    threshold_warning_jitter: int
    # Alert threshold for jitter (ms, default = 0).
    threshold_alert_jitter: int
    # Virtual Routing Forwarding ID.
    vrf: int
    # Source IP address used in the health-check packet to the server.
    source: str
    # Source IPv6 address used in the health-check packet to server.
    source6: str
    # Member sequence number list.
    members: str
    # Codec to use for MOS calculation (default = g711).
    mos_codec: Literal["g711", "g722", "g729"]
    # Traffic class ID.
    class_id: int
    # Coefficient of packet-loss in the formula of custom-profile-1.
    packet_loss_weight: int
    # Coefficient of latency in the formula of custom-profile-1.
    latency_weight: int
    # Coefficient of jitter in the formula of custom-profile-1.
    jitter_weight: int
    # Coefficient of reciprocal of available bidirectional bandwidth in the formula of
    bandwidth_weight: int
    # Service level agreement (SLA).
    sla: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdwanServiceObject:
    """Typed object for service table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SD-WAN rule ID (1 - 4000).
    id: int
    # SD-WAN rule name.
    name: str
    # Address mode (IPv4 or IPv6).
    addr_mode: Literal["ipv4", "ipv6"]
    # Enable/disable load-balance.
    load_balance: Literal["enable", "disable"]
    # Source interface name.
    input_device: str
    # Enable/disable negation of input device match.
    input_device_negate: Literal["enable", "disable"]
    # Source input-zone name.
    input_zone: str
    # Control how the SD-WAN rule sets the priority of interfaces in the SD-WAN.
    mode: Literal["auto", "manual", "priority", "sla"]
    # Enable/disable zone mode.
    zone_mode: Literal["enable", "disable"]
    # Minimum number of members which meet SLA.
    minimum_sla_meet_members: int
    # Hash algorithm for selected priority members for load balance mode.
    hash_mode: Literal["round-robin", "source-ip-based", "source-dest-ip-based", "inbandwidth", "outbandwidth", "bibandwidth"]
    # High priority of ADVPN shortcut for this service.
    shortcut_priority: Literal["enable", "disable", "auto"]
    # Service role to work with neighbor.
    role: Literal["standalone", "primary", "secondary"]
    # Enable/disable service when selected neighbor role is standalone while service r
    standalone_action: Literal["enable", "disable"]
    # Quality grade.
    quality_link: int
    # Type of service bit pattern.
    tos: str
    # Type of service evaluated bits.
    tos_mask: str
    # Protocol number.
    protocol: int
    # Start destination port number.
    start_port: int
    # End destination port number.
    end_port: int
    # Start source port number.
    start_src_port: int
    # End source port number.
    end_src_port: int
    # Destination address name.
    dst: str
    # Enable/disable negation of destination address match.
    dst_negate: Literal["enable", "disable"]
    # Source address name.
    src: str
    # Destination address6 name.
    dst6: str
    # Source address6 name.
    src6: str
    # Enable/disable negation of source address match.
    src_negate: Literal["enable", "disable"]
    # User name.
    users: str
    # User groups.
    groups: str
    # Enable/disable use of Internet service for application-based load balancing.
    internet_service: Literal["enable", "disable"]
    # Custom Internet service name list.
    internet_service_custom: str
    # Custom Internet Service group list.
    internet_service_custom_group: str
    # FortiGuard Internet service name list.
    internet_service_fortiguard: str
    # Internet service name list.
    internet_service_name: str
    # Internet Service group list.
    internet_service_group: str
    # Application control based Internet Service ID list.
    internet_service_app_ctrl: str
    # Application control based Internet Service group list.
    internet_service_app_ctrl_group: str
    # IDs of one or more application control categories.
    internet_service_app_ctrl_category: str
    # Health check list.
    health_check: str
    # Link cost factor.
    link_cost_factor: Literal["latency", "jitter", "packet-loss", "inbandwidth", "outbandwidth", "bibandwidth", "custom-profile-1"]
    # Coefficient of packet-loss in the formula of custom-profile-1.
    packet_loss_weight: int
    # Coefficient of latency in the formula of custom-profile-1.
    latency_weight: int
    # Coefficient of jitter in the formula of custom-profile-1.
    jitter_weight: int
    # Coefficient of reciprocal of available bidirectional bandwidth in the formula of
    bandwidth_weight: int
    # Percentage threshold change of link cost values that will result in policy route
    link_cost_threshold: int
    # Waiting period in seconds when switching from the back-up member to the primary
    hold_down_time: int
    # Enable/disable SLA stickiness (default = disable).
    sla_stickiness: Literal["enable", "disable"]
    # Enable/disable forward traffic DSCP tag.
    dscp_forward: Literal["enable", "disable"]
    # Enable/disable reverse traffic DSCP tag.
    dscp_reverse: Literal["enable", "disable"]
    # Forward traffic DSCP tag.
    dscp_forward_tag: str
    # Reverse traffic DSCP tag.
    dscp_reverse_tag: str
    # Service level agreement (SLA).
    sla: str
    # Member sequence number list.
    priority_members: str
    # Priority zone name list.
    priority_zone: str
    # Enable/disable SD-WAN service.
    status: Literal["enable", "disable"]
    # Enable/disable SD-WAN service gateway.
    gateway: Literal["enable", "disable"]
    # Enable/disable use of SD-WAN as default service.
    default: Literal["enable", "disable"]
    # Method to compare SLA value for SLA mode.
    sla_compare_method: Literal["order", "number"]
    # Enable/disable force using fib-best-match oif as outgoing interface.
    fib_best_match_force: Literal["disable", "enable"]
    # Method of selecting member if more than one meets the SLA.
    tie_break: Literal["zone", "cfg-order", "fib-best-match", "priority", "input-device"]
    # Enable/disable use of ADVPN shortcut for quality comparison.
    use_shortcut_sla: Literal["enable", "disable"]
    # Enable/disable passive measurement based on the service criteria.
    passive_measurement: Literal["enable", "disable"]
    # Set/unset the service as agent use exclusively.
    agent_exclusive: Literal["enable", "disable"]
    # Enable/disable shortcut for this service.
    shortcut: Literal["enable", "disable"]
    # Comments.
    comment: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdwanNeighborObject:
    """Typed object for neighbor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP/IPv6 address of neighbor or neighbor-group name.
    ip: str
    # Member sequence number list.
    member: str
    # SD-WAN service ID to work with the neighbor.
    service_id: int
    # Minimum number of members which meet SLA when the neighbor is preferred.
    minimum_sla_meet_members: int
    # What metric to select the neighbor.
    mode: Literal["sla", "speedtest"]
    # Role of neighbor.
    role: Literal["standalone", "primary", "secondary"]
    # Route-metric of neighbor.
    route_metric: Literal["preferable", "priority"]
    # SD-WAN health-check name.
    health_check: str
    # SLA ID.
    sla_id: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SdwanDuplicationObject:
    """Typed object for duplication table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Duplication rule ID (1 - 255).
    id: int
    # SD-WAN service rule ID list.
    service_id: str
    # Source address or address group names.
    srcaddr: str
    # Destination address or address group names.
    dstaddr: str
    # Source address6 or address6 group names.
    srcaddr6: str
    # Destination address6 or address6 group names.
    dstaddr6: str
    # Incoming (ingress) interfaces or zones.
    srcintf: str
    # Outgoing (egress) interfaces or zones.
    dstintf: str
    # Service and service group name.
    service: str
    # Configure packet duplication method.
    packet_duplication: Literal["disable", "force", "on-demand"]
    # Enable/disable packet duplication matching health-check SLAs in service rule.
    sla_match_service: Literal["enable", "disable"]
    # Enable/disable discarding of packets that have been duplicated.
    packet_de_duplication: Literal["enable", "disable"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SdwanResponse(TypedDict):
    """
    Type hints for system/sdwan API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["disable", "enable"]
    load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"]
    speedtest_bypass_routing: Literal["disable", "enable"]
    duplication_max_num: int
    duplication_max_discrepancy: int
    neighbor_hold_down: Literal["enable", "disable"]
    neighbor_hold_down_time: int
    app_perf_log_period: int
    neighbor_hold_boot_time: int
    fail_detect: Literal["enable", "disable"]
    fail_alert_interfaces: list[dict[str, Any]]
    zone: list[dict[str, Any]]
    members: list[dict[str, Any]]
    health_check: list[dict[str, Any]]
    service: list[dict[str, Any]]
    neighbor: list[dict[str, Any]]
    duplication: list[dict[str, Any]]


@final
class SdwanObject:
    """Typed FortiObject for system/sdwan with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable SD-WAN.
    status: Literal["disable", "enable"]
    # Algorithm or mode to use for load balancing Internet traffic to SD-WAN members.
    load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"]
    # Enable/disable bypass routing when speedtest on a SD-WAN member.
    speedtest_bypass_routing: Literal["disable", "enable"]
    # Maximum number of interface members a packet is duplicated in the SD-WAN zone
    duplication_max_num: int
    # Maximum discrepancy between two packets for deduplication in milliseconds
    duplication_max_discrepancy: int
    # Enable/disable hold switching from the secondary neighbor to the primary neighbo
    neighbor_hold_down: Literal["enable", "disable"]
    # Waiting period in seconds when switching from the secondary neighbor to the prim
    neighbor_hold_down_time: int
    # Time interval in seconds that application performance logs are generated
    app_perf_log_period: int
    # Waiting period in seconds when switching from the primary neighbor to the second
    neighbor_hold_boot_time: int
    # Enable/disable SD-WAN Internet connection status checking (failure detection).
    fail_detect: Literal["enable", "disable"]
    # Physical interfaces that will be alerted.
    fail_alert_interfaces: list[SdwanFailalertinterfacesObject]  # Table field - list of typed objects
    # Configure SD-WAN zones.
    zone: list[SdwanZoneObject]  # Table field - list of typed objects
    # FortiGate interfaces added to the SD-WAN.
    members: list[SdwanMembersObject]  # Table field - list of typed objects
    # SD-WAN status checking or health checking. Identify a server on the Internet and
    health_check: list[SdwanHealthcheckObject]  # Table field - list of typed objects
    # Create SD-WAN rules (also called services) to control how sessions are distribut
    service: list[SdwanServiceObject]  # Table field - list of typed objects
    # Create SD-WAN neighbor from BGP neighbor table to control route advertisements a
    neighbor: list[SdwanNeighborObject]  # Table field - list of typed objects
    # Create SD-WAN duplication rule.
    duplication: list[SdwanDuplicationObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SdwanPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Sdwan:
    """
    Configure redundant Internet connections with multiple outbound links and health-check profiles.
    
    Path: system/sdwan
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanResponse: ...
    
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
    ) -> SdwanResponse: ...
    
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
    ) -> SdwanResponse: ...
    
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
    ) -> SdwanObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SdwanObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Sdwan",
    "SdwanPayload",
    "SdwanObject",
]