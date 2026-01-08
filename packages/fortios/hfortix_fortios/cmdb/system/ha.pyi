from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class HaPayload(TypedDict, total=False):
    """
    Type hints for system/ha payload fields.
    
    Configure HA.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: monitor, pingserver-monitor-interface, session-sync-dev)

    **Usage:**
        payload: HaPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    group_id: NotRequired[int]  # HA group ID  (0 - 1023;  or 0 - 7 when there are more than 2
    group_name: NotRequired[str]  # Cluster group name. Must be the same for all members.
    mode: NotRequired[Literal["standalone", "a-a", "a-p"]]  # HA mode. Must be the same for all members. FGSP requires sta
    sync_packet_balance: NotRequired[Literal["enable", "disable"]]  # Enable/disable HA packet distribution to multiple CPUs.
    password: NotRequired[str]  # Cluster password. Must be the same for all members.
    key: NotRequired[str]  # Key.
    hbdev: NotRequired[list[dict[str, Any]]]  # Heartbeat interfaces. Must be the same for all members.
    auto_virtual_mac_interface: NotRequired[list[dict[str, Any]]]  # The physical interface that will be assigned an auto-generat
    backup_hbdev: NotRequired[list[dict[str, Any]]]  # Backup heartbeat interfaces. Must be the same for all member
    unicast_hb: NotRequired[Literal["enable", "disable"]]  # Enable/disable unicast heartbeat.
    unicast_hb_peerip: NotRequired[str]  # Unicast heartbeat peer IP.
    unicast_hb_netmask: NotRequired[str]  # Unicast heartbeat netmask.
    session_sync_dev: NotRequired[list[dict[str, Any]]]  # Offload session-sync process to kernel and sync sessions usi
    route_ttl: NotRequired[int]  # TTL for primary unit routes (5 - 3600 sec). Increase to main
    route_wait: NotRequired[int]  # Time to wait before sending new routes to the cluster (0 - 3
    route_hold: NotRequired[int]  # Time to wait between routing table updates to the cluster (0
    multicast_ttl: NotRequired[int]  # HA multicast TTL on primary (5 - 3600 sec).
    evpn_ttl: NotRequired[int]  # HA EVPN FDB TTL on primary box (5 - 3600 sec).
    load_balance_all: NotRequired[Literal["enable", "disable"]]  # Enable to load balance TCP sessions. Disable to load balance
    sync_config: NotRequired[Literal["enable", "disable"]]  # Enable/disable configuration synchronization.
    encryption: NotRequired[Literal["enable", "disable"]]  # Enable/disable heartbeat message encryption.
    authentication: NotRequired[Literal["enable", "disable"]]  # Enable/disable heartbeat message authentication.
    hb_interval: NotRequired[int]  # Time between sending heartbeat packets (1 - 20). Increase to
    hb_interval_in_milliseconds: NotRequired[Literal["100ms", "10ms"]]  # Units of heartbeat interval time between sending heartbeat p
    hb_lost_threshold: NotRequired[int]  # Number of lost heartbeats to signal a failure (1 - 60). Incr
    hello_holddown: NotRequired[int]  # Time to wait before changing from hello to work state (5 - 3
    gratuitous_arps: NotRequired[Literal["enable", "disable"]]  # Enable/disable gratuitous ARPs. Disable if link-failed-signa
    arps: NotRequired[int]  # Number of gratuitous ARPs (1 - 60). Lower to reduce traffic.
    arps_interval: NotRequired[int]  # Time between gratuitous ARPs  (1 - 20 sec). Lower to reduce 
    session_pickup: NotRequired[Literal["enable", "disable"]]  # Enable/disable session pickup. Enabling it can reduce sessio
    session_pickup_connectionless: NotRequired[Literal["enable", "disable"]]  # Enable/disable UDP and ICMP session sync.
    session_pickup_expectation: NotRequired[Literal["enable", "disable"]]  # Enable/disable session helper expectation session sync for F
    session_pickup_nat: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT session sync for FGSP.
    session_pickup_delay: NotRequired[Literal["enable", "disable"]]  # Enable to sync sessions longer than 30 sec. Only longer live
    link_failed_signal: NotRequired[Literal["enable", "disable"]]  # Enable to shut down all interfaces for 1 sec after a failove
    upgrade_mode: NotRequired[Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"]]  # The mode to upgrade a cluster.
    uninterruptible_primary_wait: NotRequired[int]  # Number of minutes the primary HA unit waits before the secon
    standalone_mgmt_vdom: NotRequired[Literal["enable", "disable"]]  # Enable/disable standalone management VDOM.
    ha_mgmt_status: NotRequired[Literal["enable", "disable"]]  # Enable to reserve interfaces to manage individual cluster un
    ha_mgmt_interfaces: NotRequired[list[dict[str, Any]]]  # Reserve interfaces to manage individual cluster units.
    ha_eth_type: NotRequired[str]  # HA heartbeat packet Ethertype (4-digit hex).
    hc_eth_type: NotRequired[str]  # Transparent mode HA heartbeat packet Ethertype (4-digit hex)
    l2ep_eth_type: NotRequired[str]  # Telnet session HA heartbeat packet Ethertype (4-digit hex).
    ha_uptime_diff_margin: NotRequired[int]  # Normally you would only reduce this value for failover testi
    standalone_config_sync: NotRequired[Literal["enable", "disable"]]  # Enable/disable FGSP configuration synchronization.
    unicast_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable unicast connection.
    unicast_gateway: NotRequired[str]  # Default route gateway for unicast interface.
    unicast_peers: NotRequired[list[dict[str, Any]]]  # Number of unicast peers.
    schedule: NotRequired[Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"]]  # Type of A-A load balancing. Use none if you have external lo
    weight: NotRequired[str]  # Weight-round-robin weight for each cluster unit. Syntax <pri
    cpu_threshold: NotRequired[str]  # Dynamic weighted load balancing CPU usage weight and high an
    memory_threshold: NotRequired[str]  # Dynamic weighted load balancing memory usage weight and high
    http_proxy_threshold: NotRequired[str]  # Dynamic weighted load balancing weight and high and low numb
    ftp_proxy_threshold: NotRequired[str]  # Dynamic weighted load balancing weight and high and low numb
    imap_proxy_threshold: NotRequired[str]  # Dynamic weighted load balancing weight and high and low numb
    nntp_proxy_threshold: NotRequired[str]  # Dynamic weighted load balancing weight and high and low numb
    pop3_proxy_threshold: NotRequired[str]  # Dynamic weighted load balancing weight and high and low numb
    smtp_proxy_threshold: NotRequired[str]  # Dynamic weighted load balancing weight and high and low numb
    override: NotRequired[Literal["enable", "disable"]]  # Enable and increase the priority of the unit that should alw
    priority: NotRequired[int]  # Increase the priority to select the primary unit (0 - 255).
    override_wait_time: NotRequired[int]  # Delay negotiating if override is enabled (0 - 3600 sec). Red
    monitor: NotRequired[list[dict[str, Any]]]  # Interfaces to check for port monitoring (or link failure).
    pingserver_monitor_interface: NotRequired[list[dict[str, Any]]]  # Interfaces to check for remote IP monitoring.
    pingserver_failover_threshold: NotRequired[int]  # Remote IP monitoring failover threshold (0 - 50).
    pingserver_secondary_force_reset: NotRequired[Literal["enable", "disable"]]  # Enable to force the cluster to negotiate after a remote IP m
    pingserver_flip_timeout: NotRequired[int]  # Time to wait in minutes before renegotiating after a remote 
    vcluster_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable virtual cluster for virtual clustering.
    vcluster: NotRequired[list[dict[str, Any]]]  # Virtual cluster table.
    ha_direct: NotRequired[Literal["enable", "disable"]]  # Enable/disable using ha-mgmt interface for syslog, remote au
    ssd_failover: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic HA failover on SSD disk failure.
    memory_compatible_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable memory compatible mode.
    memory_based_failover: NotRequired[Literal["enable", "disable"]]  # Enable/disable memory based failover.
    memory_failover_threshold: NotRequired[int]  # Memory usage threshold to trigger memory based failover (0 m
    memory_failover_monitor_period: NotRequired[int]  # Duration of high memory usage before memory based failover i
    memory_failover_sample_rate: NotRequired[int]  # Rate at which memory usage is sampled in order to measure me
    memory_failover_flip_timeout: NotRequired[int]  # Time to wait between subsequent memory based failovers in mi
    failover_hold_time: NotRequired[int]  # Time to wait before failover (0 - 300 sec, default = 0), to 
    check_secondary_dev_health: NotRequired[Literal["enable", "disable"]]  # Enable/disable secondary dev health check for session load-b
    ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"]  # IPsec phase2 proposal.
    bounce_intf_upon_failover: NotRequired[Literal["enable", "disable"]]  # Enable/disable notification of kernel to bring down and up a
    status: NotRequired[str]  # list ha status information


class HaObject(FortiObject[HaPayload]):
    """Typed FortiObject for system/ha with IDE autocomplete support."""
    
    # HA group ID  (0 - 1023;  or 0 - 7 when there are more than 2 vclusters). Must be
    group_id: int
    # Cluster group name. Must be the same for all members.
    group_name: str
    # HA mode. Must be the same for all members. FGSP requires standalone.
    mode: Literal["standalone", "a-a", "a-p"]
    # Enable/disable HA packet distribution to multiple CPUs.
    sync_packet_balance: Literal["enable", "disable"]
    # Cluster password. Must be the same for all members.
    password: str
    # Key.
    key: str
    # Heartbeat interfaces. Must be the same for all members.
    hbdev: list[str]  # Auto-flattened from member_table
    # The physical interface that will be assigned an auto-generated virtual MAC addre
    auto_virtual_mac_interface: list[str]  # Auto-flattened from member_table
    # Backup heartbeat interfaces. Must be the same for all members.
    backup_hbdev: list[str]  # Auto-flattened from member_table
    # Enable/disable unicast heartbeat.
    unicast_hb: Literal["enable", "disable"]
    # Unicast heartbeat peer IP.
    unicast_hb_peerip: str
    # Unicast heartbeat netmask.
    unicast_hb_netmask: str
    # Offload session-sync process to kernel and sync sessions using connected interfa
    session_sync_dev: list[str]  # Auto-flattened from member_table
    # TTL for primary unit routes (5 - 3600 sec). Increase to maintain active routes d
    route_ttl: int
    # Time to wait before sending new routes to the cluster (0 - 3600 sec).
    route_wait: int
    # Time to wait between routing table updates to the cluster (0 - 3600 sec).
    route_hold: int
    # HA multicast TTL on primary (5 - 3600 sec).
    multicast_ttl: int
    # HA EVPN FDB TTL on primary box (5 - 3600 sec).
    evpn_ttl: int
    # Enable to load balance TCP sessions. Disable to load balance proxy sessions only
    load_balance_all: Literal["enable", "disable"]
    # Enable/disable configuration synchronization.
    sync_config: Literal["enable", "disable"]
    # Enable/disable heartbeat message encryption.
    encryption: Literal["enable", "disable"]
    # Enable/disable heartbeat message authentication.
    authentication: Literal["enable", "disable"]
    # Time between sending heartbeat packets (1 - 20). Increase to reduce false positi
    hb_interval: int
    # Units of heartbeat interval time between sending heartbeat packets. Default is 1
    hb_interval_in_milliseconds: Literal["100ms", "10ms"]
    # Number of lost heartbeats to signal a failure (1 - 60). Increase to reduce false
    hb_lost_threshold: int
    # Time to wait before changing from hello to work state (5 - 300 sec).
    hello_holddown: int
    # Enable/disable gratuitous ARPs. Disable if link-failed-signal enabled.
    gratuitous_arps: Literal["enable", "disable"]
    # Number of gratuitous ARPs (1 - 60). Lower to reduce traffic. Higher to reduce fa
    arps: int
    # Time between gratuitous ARPs  (1 - 20 sec). Lower to reduce failover time. Highe
    arps_interval: int
    # Enable/disable session pickup. Enabling it can reduce session down time when fai
    session_pickup: Literal["enable", "disable"]
    # Enable/disable UDP and ICMP session sync.
    session_pickup_connectionless: Literal["enable", "disable"]
    # Enable/disable session helper expectation session sync for FGSP.
    session_pickup_expectation: Literal["enable", "disable"]
    # Enable/disable NAT session sync for FGSP.
    session_pickup_nat: Literal["enable", "disable"]
    # Enable to sync sessions longer than 30 sec. Only longer lived sessions need to b
    session_pickup_delay: Literal["enable", "disable"]
    # Enable to shut down all interfaces for 1 sec after a failover. Use if gratuitous
    link_failed_signal: Literal["enable", "disable"]
    # The mode to upgrade a cluster.
    upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"]
    # Number of minutes the primary HA unit waits before the secondary HA unit is cons
    uninterruptible_primary_wait: int
    # Enable/disable standalone management VDOM.
    standalone_mgmt_vdom: Literal["enable", "disable"]
    # Enable to reserve interfaces to manage individual cluster units.
    ha_mgmt_status: Literal["enable", "disable"]
    # Reserve interfaces to manage individual cluster units.
    ha_mgmt_interfaces: list[str]  # Auto-flattened from member_table
    # HA heartbeat packet Ethertype (4-digit hex).
    ha_eth_type: str
    # Transparent mode HA heartbeat packet Ethertype (4-digit hex).
    hc_eth_type: str
    # Telnet session HA heartbeat packet Ethertype (4-digit hex).
    l2ep_eth_type: str
    # Normally you would only reduce this value for failover testing.
    ha_uptime_diff_margin: int
    # Enable/disable FGSP configuration synchronization.
    standalone_config_sync: Literal["enable", "disable"]
    # Enable/disable unicast connection.
    unicast_status: Literal["enable", "disable"]
    # Default route gateway for unicast interface.
    unicast_gateway: str
    # Number of unicast peers.
    unicast_peers: list[str]  # Auto-flattened from member_table
    # Type of A-A load balancing. Use none if you have external load balancers.
    schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"]
    # Weight-round-robin weight for each cluster unit. Syntax <priority> <weight>.
    weight: str
    # Dynamic weighted load balancing CPU usage weight and high and low thresholds.
    cpu_threshold: str
    # Dynamic weighted load balancing memory usage weight and high and low thresholds.
    memory_threshold: str
    # Dynamic weighted load balancing weight and high and low number of HTTP proxy ses
    http_proxy_threshold: str
    # Dynamic weighted load balancing weight and high and low number of FTP proxy sess
    ftp_proxy_threshold: str
    # Dynamic weighted load balancing weight and high and low number of IMAP proxy ses
    imap_proxy_threshold: str
    # Dynamic weighted load balancing weight and high and low number of NNTP proxy ses
    nntp_proxy_threshold: str
    # Dynamic weighted load balancing weight and high and low number of POP3 proxy ses
    pop3_proxy_threshold: str
    # Dynamic weighted load balancing weight and high and low number of SMTP proxy ses
    smtp_proxy_threshold: str
    # Enable and increase the priority of the unit that should always be primary (mast
    override: Literal["enable", "disable"]
    # Increase the priority to select the primary unit (0 - 255).
    priority: int
    # Delay negotiating if override is enabled (0 - 3600 sec). Reduces how often the c
    override_wait_time: int
    # Interfaces to check for port monitoring (or link failure).
    monitor: list[str]  # Auto-flattened from member_table
    # Interfaces to check for remote IP monitoring.
    pingserver_monitor_interface: list[str]  # Auto-flattened from member_table
    # Remote IP monitoring failover threshold (0 - 50).
    pingserver_failover_threshold: int
    # Enable to force the cluster to negotiate after a remote IP monitoring failover.
    pingserver_secondary_force_reset: Literal["enable", "disable"]
    # Time to wait in minutes before renegotiating after a remote IP monitoring failov
    pingserver_flip_timeout: int
    # Enable/disable virtual cluster for virtual clustering.
    vcluster_status: Literal["enable", "disable"]
    # Virtual cluster table.
    vcluster: list[str]  # Auto-flattened from member_table
    # Enable/disable using ha-mgmt interface for syslog, remote authentication (RADIUS
    ha_direct: Literal["enable", "disable"]
    # Enable/disable automatic HA failover on SSD disk failure.
    ssd_failover: Literal["enable", "disable"]
    # Enable/disable memory compatible mode.
    memory_compatible_mode: Literal["enable", "disable"]
    # Enable/disable memory based failover.
    memory_based_failover: Literal["enable", "disable"]
    # Memory usage threshold to trigger memory based failover (0 means using conserve 
    memory_failover_threshold: int
    # Duration of high memory usage before memory based failover is triggered in secon
    memory_failover_monitor_period: int
    # Rate at which memory usage is sampled in order to measure memory usage in second
    memory_failover_sample_rate: int
    # Time to wait between subsequent memory based failovers in minutes (6 - 214748364
    memory_failover_flip_timeout: int
    # Time to wait before failover (0 - 300 sec, default = 0), to avoid flip.
    failover_hold_time: int
    # Enable/disable secondary dev health check for session load-balance in HA A-A mod
    check_secondary_dev_health: Literal["enable", "disable"]
    # IPsec phase2 proposal.
    ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"]
    # Enable/disable notification of kernel to bring down and up all monitored interfa
    bounce_intf_upon_failover: Literal["enable", "disable"]
    # list ha status information
    status: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> HaPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ha:
    """
    Configure HA.
    
    Path: system/ha
    Category: cmdb
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
    ) -> HaObject: ...
    
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
    ) -> HaObject: ...
    
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
    ) -> HaObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | list[str] | list[dict[str, Any]] | None = ...,
        route_ttl: int | None = ...,
        route_wait: int | None = ...,
        route_hold: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_ttl: int | None = ...,
        load_balance_all: Literal["enable", "disable"] | None = ...,
        sync_config: Literal["enable", "disable"] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        hb_interval: int | None = ...,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = ...,
        hb_lost_threshold: int | None = ...,
        hello_holddown: int | None = ...,
        gratuitous_arps: Literal["enable", "disable"] | None = ...,
        arps: int | None = ...,
        arps_interval: int | None = ...,
        session_pickup: Literal["enable", "disable"] | None = ...,
        session_pickup_connectionless: Literal["enable", "disable"] | None = ...,
        session_pickup_expectation: Literal["enable", "disable"] | None = ...,
        session_pickup_nat: Literal["enable", "disable"] | None = ...,
        session_pickup_delay: Literal["enable", "disable"] | None = ...,
        link_failed_signal: Literal["enable", "disable"] | None = ...,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = ...,
        uninterruptible_primary_wait: int | None = ...,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        ha_mgmt_status: Literal["enable", "disable"] | None = ...,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = ...,
        weight: str | None = ...,
        cpu_threshold: str | None = ...,
        memory_threshold: str | None = ...,
        http_proxy_threshold: str | None = ...,
        ftp_proxy_threshold: str | None = ...,
        imap_proxy_threshold: str | None = ...,
        nntp_proxy_threshold: str | None = ...,
        pop3_proxy_threshold: str | None = ...,
        smtp_proxy_threshold: str | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        priority: int | None = ...,
        override_wait_time: int | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        pingserver_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        ssd_failover: Literal["enable", "disable"] | None = ...,
        memory_compatible_mode: Literal["enable", "disable"] | None = ...,
        memory_based_failover: Literal["enable", "disable"] | None = ...,
        memory_failover_threshold: int | None = ...,
        memory_failover_monitor_period: int | None = ...,
        memory_failover_sample_rate: int | None = ...,
        memory_failover_flip_timeout: int | None = ...,
        failover_hold_time: int | None = ...,
        check_secondary_dev_health: Literal["enable", "disable"] | None = ...,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | list[dict[str, Any]] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> HaObject: ...
    
    @overload
    def put(
        self,
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | list[str] | list[dict[str, Any]] | None = ...,
        route_ttl: int | None = ...,
        route_wait: int | None = ...,
        route_hold: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_ttl: int | None = ...,
        load_balance_all: Literal["enable", "disable"] | None = ...,
        sync_config: Literal["enable", "disable"] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        hb_interval: int | None = ...,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = ...,
        hb_lost_threshold: int | None = ...,
        hello_holddown: int | None = ...,
        gratuitous_arps: Literal["enable", "disable"] | None = ...,
        arps: int | None = ...,
        arps_interval: int | None = ...,
        session_pickup: Literal["enable", "disable"] | None = ...,
        session_pickup_connectionless: Literal["enable", "disable"] | None = ...,
        session_pickup_expectation: Literal["enable", "disable"] | None = ...,
        session_pickup_nat: Literal["enable", "disable"] | None = ...,
        session_pickup_delay: Literal["enable", "disable"] | None = ...,
        link_failed_signal: Literal["enable", "disable"] | None = ...,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = ...,
        uninterruptible_primary_wait: int | None = ...,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        ha_mgmt_status: Literal["enable", "disable"] | None = ...,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = ...,
        weight: str | None = ...,
        cpu_threshold: str | None = ...,
        memory_threshold: str | None = ...,
        http_proxy_threshold: str | None = ...,
        ftp_proxy_threshold: str | None = ...,
        imap_proxy_threshold: str | None = ...,
        nntp_proxy_threshold: str | None = ...,
        pop3_proxy_threshold: str | None = ...,
        smtp_proxy_threshold: str | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        priority: int | None = ...,
        override_wait_time: int | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        pingserver_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        ssd_failover: Literal["enable", "disable"] | None = ...,
        memory_compatible_mode: Literal["enable", "disable"] | None = ...,
        memory_based_failover: Literal["enable", "disable"] | None = ...,
        memory_failover_threshold: int | None = ...,
        memory_failover_monitor_period: int | None = ...,
        memory_failover_sample_rate: int | None = ...,
        memory_failover_flip_timeout: int | None = ...,
        failover_hold_time: int | None = ...,
        check_secondary_dev_health: Literal["enable", "disable"] | None = ...,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | list[dict[str, Any]] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | list[str] | list[dict[str, Any]] | None = ...,
        route_ttl: int | None = ...,
        route_wait: int | None = ...,
        route_hold: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_ttl: int | None = ...,
        load_balance_all: Literal["enable", "disable"] | None = ...,
        sync_config: Literal["enable", "disable"] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        hb_interval: int | None = ...,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = ...,
        hb_lost_threshold: int | None = ...,
        hello_holddown: int | None = ...,
        gratuitous_arps: Literal["enable", "disable"] | None = ...,
        arps: int | None = ...,
        arps_interval: int | None = ...,
        session_pickup: Literal["enable", "disable"] | None = ...,
        session_pickup_connectionless: Literal["enable", "disable"] | None = ...,
        session_pickup_expectation: Literal["enable", "disable"] | None = ...,
        session_pickup_nat: Literal["enable", "disable"] | None = ...,
        session_pickup_delay: Literal["enable", "disable"] | None = ...,
        link_failed_signal: Literal["enable", "disable"] | None = ...,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = ...,
        uninterruptible_primary_wait: int | None = ...,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        ha_mgmt_status: Literal["enable", "disable"] | None = ...,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = ...,
        weight: str | None = ...,
        cpu_threshold: str | None = ...,
        memory_threshold: str | None = ...,
        http_proxy_threshold: str | None = ...,
        ftp_proxy_threshold: str | None = ...,
        imap_proxy_threshold: str | None = ...,
        nntp_proxy_threshold: str | None = ...,
        pop3_proxy_threshold: str | None = ...,
        smtp_proxy_threshold: str | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        priority: int | None = ...,
        override_wait_time: int | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        pingserver_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        ssd_failover: Literal["enable", "disable"] | None = ...,
        memory_compatible_mode: Literal["enable", "disable"] | None = ...,
        memory_based_failover: Literal["enable", "disable"] | None = ...,
        memory_failover_threshold: int | None = ...,
        memory_failover_monitor_period: int | None = ...,
        memory_failover_sample_rate: int | None = ...,
        memory_failover_flip_timeout: int | None = ...,
        failover_hold_time: int | None = ...,
        check_secondary_dev_health: Literal["enable", "disable"] | None = ...,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | list[dict[str, Any]] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | list[str] | list[dict[str, Any]] | None = ...,
        route_ttl: int | None = ...,
        route_wait: int | None = ...,
        route_hold: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_ttl: int | None = ...,
        load_balance_all: Literal["enable", "disable"] | None = ...,
        sync_config: Literal["enable", "disable"] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        hb_interval: int | None = ...,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = ...,
        hb_lost_threshold: int | None = ...,
        hello_holddown: int | None = ...,
        gratuitous_arps: Literal["enable", "disable"] | None = ...,
        arps: int | None = ...,
        arps_interval: int | None = ...,
        session_pickup: Literal["enable", "disable"] | None = ...,
        session_pickup_connectionless: Literal["enable", "disable"] | None = ...,
        session_pickup_expectation: Literal["enable", "disable"] | None = ...,
        session_pickup_nat: Literal["enable", "disable"] | None = ...,
        session_pickup_delay: Literal["enable", "disable"] | None = ...,
        link_failed_signal: Literal["enable", "disable"] | None = ...,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = ...,
        uninterruptible_primary_wait: int | None = ...,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        ha_mgmt_status: Literal["enable", "disable"] | None = ...,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = ...,
        weight: str | None = ...,
        cpu_threshold: str | None = ...,
        memory_threshold: str | None = ...,
        http_proxy_threshold: str | None = ...,
        ftp_proxy_threshold: str | None = ...,
        imap_proxy_threshold: str | None = ...,
        nntp_proxy_threshold: str | None = ...,
        pop3_proxy_threshold: str | None = ...,
        smtp_proxy_threshold: str | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        priority: int | None = ...,
        override_wait_time: int | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        pingserver_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        ssd_failover: Literal["enable", "disable"] | None = ...,
        memory_compatible_mode: Literal["enable", "disable"] | None = ...,
        memory_based_failover: Literal["enable", "disable"] | None = ...,
        memory_failover_threshold: int | None = ...,
        memory_failover_monitor_period: int | None = ...,
        memory_failover_sample_rate: int | None = ...,
        memory_failover_flip_timeout: int | None = ...,
        failover_hold_time: int | None = ...,
        check_secondary_dev_health: Literal["enable", "disable"] | None = ...,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | list[dict[str, Any]] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
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
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        auto_virtual_mac_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        backup_hbdev: str | list[str] | list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | list[str] | list[dict[str, Any]] | None = ...,
        route_ttl: int | None = ...,
        route_wait: int | None = ...,
        route_hold: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_ttl: int | None = ...,
        load_balance_all: Literal["enable", "disable"] | None = ...,
        sync_config: Literal["enable", "disable"] | None = ...,
        encryption: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        hb_interval: int | None = ...,
        hb_interval_in_milliseconds: Literal["100ms", "10ms"] | None = ...,
        hb_lost_threshold: int | None = ...,
        hello_holddown: int | None = ...,
        gratuitous_arps: Literal["enable", "disable"] | None = ...,
        arps: int | None = ...,
        arps_interval: int | None = ...,
        session_pickup: Literal["enable", "disable"] | None = ...,
        session_pickup_connectionless: Literal["enable", "disable"] | None = ...,
        session_pickup_expectation: Literal["enable", "disable"] | None = ...,
        session_pickup_nat: Literal["enable", "disable"] | None = ...,
        session_pickup_delay: Literal["enable", "disable"] | None = ...,
        link_failed_signal: Literal["enable", "disable"] | None = ...,
        upgrade_mode: Literal["simultaneous", "uninterruptible", "local-only", "secondary-only"] | None = ...,
        uninterruptible_primary_wait: int | None = ...,
        standalone_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        ha_mgmt_status: Literal["enable", "disable"] | None = ...,
        ha_mgmt_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: Literal["none", "leastconnection", "round-robin", "weight-round-robin", "random", "ip", "ipport"] | None = ...,
        weight: str | None = ...,
        cpu_threshold: str | None = ...,
        memory_threshold: str | None = ...,
        http_proxy_threshold: str | None = ...,
        ftp_proxy_threshold: str | None = ...,
        imap_proxy_threshold: str | None = ...,
        nntp_proxy_threshold: str | None = ...,
        pop3_proxy_threshold: str | None = ...,
        smtp_proxy_threshold: str | None = ...,
        override: Literal["enable", "disable"] | None = ...,
        priority: int | None = ...,
        override_wait_time: int | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        pingserver_monitor_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: str | list[str] | list[dict[str, Any]] | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        ssd_failover: Literal["enable", "disable"] | None = ...,
        memory_compatible_mode: Literal["enable", "disable"] | None = ...,
        memory_based_failover: Literal["enable", "disable"] | None = ...,
        memory_failover_threshold: int | None = ...,
        memory_failover_monitor_period: int | None = ...,
        memory_failover_sample_rate: int | None = ...,
        memory_failover_flip_timeout: int | None = ...,
        failover_hold_time: int | None = ...,
        check_secondary_dev_health: Literal["enable", "disable"] | None = ...,
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | list[str] | list[dict[str, Any]] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
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
    "Ha",
    "HaPayload",
    "HaObject",
]