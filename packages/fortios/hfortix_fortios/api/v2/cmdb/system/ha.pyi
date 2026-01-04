from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class HaPayload(TypedDict, total=False):
    """
    Type hints for system/ha payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    hbdev: NotRequired[str]  # Heartbeat interfaces. Must be the same for all members.
    auto_virtual_mac_interface: NotRequired[list[dict[str, Any]]]  # The physical interface that will be assigned an auto-generat
    backup_hbdev: NotRequired[list[dict[str, Any]]]  # Backup heartbeat interfaces. Must be the same for all member
    unicast_hb: NotRequired[Literal["enable", "disable"]]  # Enable/disable unicast heartbeat.
    unicast_hb_peerip: NotRequired[str]  # Unicast heartbeat peer IP.
    unicast_hb_netmask: NotRequired[str]  # Unicast heartbeat netmask.
    session_sync_dev: NotRequired[str]  # Offload session-sync process to kernel and sync sessions usi
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
    monitor: NotRequired[str]  # Interfaces to check for port monitoring (or link failure).
    pingserver_monitor_interface: NotRequired[str]  # Interfaces to check for remote IP monitoring.
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


class Ha:
    """
    Configure HA.
    
    Path: system/ha
    Category: cmdb
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
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | None = ...,
        auto_virtual_mac_interface: list[dict[str, Any]] | None = ...,
        backup_hbdev: list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | None = ...,
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
        ha_mgmt_interfaces: list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: list[dict[str, Any]] | None = ...,
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
        monitor: str | None = ...,
        pingserver_monitor_interface: str | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: list[dict[str, Any]] | None = ...,
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
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: HaPayload | None = ...,
        group_id: int | None = ...,
        group_name: str | None = ...,
        mode: Literal["standalone", "a-a", "a-p"] | None = ...,
        sync_packet_balance: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        key: str | None = ...,
        hbdev: str | None = ...,
        auto_virtual_mac_interface: list[dict[str, Any]] | None = ...,
        backup_hbdev: list[dict[str, Any]] | None = ...,
        unicast_hb: Literal["enable", "disable"] | None = ...,
        unicast_hb_peerip: str | None = ...,
        unicast_hb_netmask: str | None = ...,
        session_sync_dev: str | None = ...,
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
        ha_mgmt_interfaces: list[dict[str, Any]] | None = ...,
        ha_eth_type: str | None = ...,
        hc_eth_type: str | None = ...,
        l2ep_eth_type: str | None = ...,
        ha_uptime_diff_margin: int | None = ...,
        standalone_config_sync: Literal["enable", "disable"] | None = ...,
        unicast_status: Literal["enable", "disable"] | None = ...,
        unicast_gateway: str | None = ...,
        unicast_peers: list[dict[str, Any]] | None = ...,
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
        monitor: str | None = ...,
        pingserver_monitor_interface: str | None = ...,
        pingserver_failover_threshold: int | None = ...,
        pingserver_secondary_force_reset: Literal["enable", "disable"] | None = ...,
        pingserver_flip_timeout: int | None = ...,
        vcluster_status: Literal["enable", "disable"] | None = ...,
        vcluster: list[dict[str, Any]] | None = ...,
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
        ipsec_phase2_proposal: Literal["aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes128gcm", "aes256gcm", "chacha20poly1305"] | None = ...,
        bounce_intf_upon_failover: Literal["enable", "disable"] | None = ...,
        status: str | None = ...,
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
        payload_dict: HaPayload | None = ...,
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
    "Ha",
    "HaPayload",
]