"""Type stubs for SWITCH_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import acl
    from . import auto_config
    from . import custom_command
    from . import dynamic_port_policy
    from . import flow_tracking
    from . import fortilink_settings
    from . import global_setting
    from . import igmp_snooping
    from . import initial_config
    from . import ip_source_guard_log
    from . import lldp_profile
    from . import lldp_settings
    from . import location
    from . import mac_policy
    from . import managed_switch
    from . import network_monitor_settings
    from . import ptp
    from . import qos
    from . import remote_log
    from . import security_policy
    from . import sflow
    from . import snmp_community
    from . import snmp_sysinfo
    from . import snmp_trap_threshold
    from . import snmp_user
    from . import storm_control
    from . import storm_control_policy
    from . import stp_instance
    from . import stp_settings
    from . import switch_group
    from . import switch_interface_tag
    from . import switch_log
    from . import switch_profile
    from . import system
    from . import traffic_policy
    from . import traffic_sniffer
    from . import virtual_port_pool
    from . import vlan_policy
    from . import x802_1X_settings


class SwitchController:
    """Type stub for SwitchController."""

    acl: acl.Acl
    auto_config: auto_config.AutoConfig
    initial_config: initial_config.InitialConfig
    ptp: ptp.Ptp
    qos: qos.Qos
    security_policy: security_policy.SecurityPolicy
    custom_command: custom_command.CustomCommand
    dynamic_port_policy: dynamic_port_policy.DynamicPortPolicy
    flow_tracking: flow_tracking.FlowTracking
    fortilink_settings: fortilink_settings.FortilinkSettings
    global_setting: global_setting.GlobalSetting
    igmp_snooping: igmp_snooping.IgmpSnooping
    ip_source_guard_log: ip_source_guard_log.IpSourceGuardLog
    lldp_profile: lldp_profile.LldpProfile
    lldp_settings: lldp_settings.LldpSettings
    location: location.Location
    mac_policy: mac_policy.MacPolicy
    managed_switch: managed_switch.ManagedSwitch
    network_monitor_settings: network_monitor_settings.NetworkMonitorSettings
    remote_log: remote_log.RemoteLog
    sflow: sflow.Sflow
    snmp_community: snmp_community.SnmpCommunity
    snmp_sysinfo: snmp_sysinfo.SnmpSysinfo
    snmp_trap_threshold: snmp_trap_threshold.SnmpTrapThreshold
    snmp_user: snmp_user.SnmpUser
    storm_control: storm_control.StormControl
    storm_control_policy: storm_control_policy.StormControlPolicy
    stp_instance: stp_instance.StpInstance
    stp_settings: stp_settings.StpSettings
    switch_group: switch_group.SwitchGroup
    switch_interface_tag: switch_interface_tag.SwitchInterfaceTag
    switch_log: switch_log.SwitchLog
    switch_profile: switch_profile.SwitchProfile
    system: system.System
    traffic_policy: traffic_policy.TrafficPolicy
    traffic_sniffer: traffic_sniffer.TrafficSniffer
    virtual_port_pool: virtual_port_pool.VirtualPortPool
    vlan_policy: vlan_policy.VlanPolicy
    x802_1X_settings: x802_1X_settings.X8021xSettings

    def __init__(self, client: IHTTPClient) -> None: ...
