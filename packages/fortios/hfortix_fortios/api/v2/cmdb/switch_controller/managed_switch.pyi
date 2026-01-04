from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ManagedSwitchPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/managed_switch payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    directly_connected: NotRequired[int]  # Directly connected FortiSwitch.
    version: NotRequired[int]  # FortiSwitch version.
    max_allowed_trunk_members: NotRequired[int]  # FortiSwitch maximum allowed trunk members.
    pre_provisioned: NotRequired[int]  # Pre-provisioned managed switch.
    l3_discovered: NotRequired[int]  # Layer 3 management discovered.
    mgmt_mode: NotRequired[int]  # FortiLink management mode.
    tunnel_discovered: NotRequired[int]  # SOCKS tunnel management discovered.
    tdr_supported: NotRequired[str]  # TDR supported.
    dynamic_capability: NotRequired[str]  # List of features this FortiSwitch supports (not configurable
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
    flow_identity: NotRequired[str]  # Flow-tracking netflow ipfix switch identity in hex format(00
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
    switch_log: NotRequired[str]  # Configuration method to edit FortiSwitch logging settings (l
    remote_log: NotRequired[list[dict[str, Any]]]  # Configure logging by FortiSwitch device to a remote syslog s
    storm_control: NotRequired[str]  # Configuration method to edit FortiSwitch storm control for m
    mirror: NotRequired[list[dict[str, Any]]]  # Configuration method to edit FortiSwitch packet mirror.
    static_mac: NotRequired[list[dict[str, Any]]]  # Configuration method to edit FortiSwitch Static and Sticky M
    custom_command: NotRequired[list[dict[str, Any]]]  # Configuration method to edit FortiSwitch commands to be push
    dhcp_snooping_static_client: NotRequired[list[dict[str, Any]]]  # Configure FortiSwitch DHCP snooping static clients.
    igmp_snooping: NotRequired[str]  # Configure FortiSwitch IGMP snooping global settings.
    802_1X_settings: NotRequired[str]  # Configuration method to edit FortiSwitch 802.1X global setti
    router_vrf: NotRequired[list[dict[str, Any]]]  # Configure VRF.
    system_interface: NotRequired[list[dict[str, Any]]]  # Configure system interface on FortiSwitch.
    router_static: NotRequired[list[dict[str, Any]]]  # Configure static routes.
    system_dhcp_server: NotRequired[list[dict[str, Any]]]  # Configure DHCP servers.


class ManagedSwitch:
    """
    Configure FortiSwitch devices that are managed by this FortiGate.
    
    Path: switch_controller/managed_switch
    Category: cmdb
    Primary Key: switch-id
    """
    
    def get(
        self,
        switch_id: str | None = ...,
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
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        switch_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        switch_id: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
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