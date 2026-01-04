"""Type stubs for SYSTEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import accprofile
    from . import acme
    from . import admin
    from . import affinity_interrupt
    from . import affinity_packet_redistribution
    from . import alarm
    from . import alias
    from . import api_user
    from . import arp_table
    from . import auto_install
    from . import auto_script
    from . import automation_action
    from . import automation_condition
    from . import automation_destination
    from . import automation_stitch
    from . import automation_trigger
    from . import autoupdate
    from . import central_management
    from . import cloud_service
    from . import console
    from . import csf
    from . import custom_language
    from . import ddns
    from . import dedicated_mgmt
    from . import device_upgrade
    from . import device_upgrade_exemptions
    from . import dhcp
    from . import dhcp6
    from . import dns
    from . import dns64
    from . import dns_database
    from . import dns_server
    from . import dscp_based_priority
    from . import email_server
    from . import evpn
    from . import external_resource
    from . import fabric_vpn
    from . import federated_upgrade
    from . import fips_cc
    from . import fortiguard
    from . import fortisandbox
    from . import fsso_polling
    from . import ftm_push
    from . import geneve
    from . import geoip_country
    from . import geoip_override
    from . import global_setting
    from . import gre_tunnel
    from . import ha
    from . import ha_monitor
    from . import health_check_fortiguard
    from . import ike
    from . import interface
    from . import ipam
    from . import ipip_tunnel
    from . import ips
    from . import ips_urlfilter_dns
    from . import ips_urlfilter_dns6
    from . import ipsec_aggregate
    from . import ipv6_neighbor_cache
    from . import ipv6_tunnel
    from . import link_monitor
    from . import lldp
    from . import lte_modem
    from . import mac_address_table
    from . import mobile_tunnel
    from . import modem
    from . import nd_proxy
    from . import netflow
    from . import network_visibility
    from . import ngfw_settings
    from . import np6xlite
    from . import npu
    from . import ntp
    from . import object_tagging
    from . import password_policy
    from . import password_policy_guest_admin
    from . import pcp_server
    from . import physical_switch
    from . import pppoe_interface
    from . import probe_response
    from . import proxy_arp
    from . import ptp
    from . import replacemsg
    from . import replacemsg_group
    from . import replacemsg_image
    from . import resource_limits
    from . import saml
    from . import sdn_connector
    from . import sdn_proxy
    from . import sdn_vpn
    from . import sdwan
    from . import security_rating
    from . import session_helper
    from . import session_ttl
    from . import settings
    from . import sflow
    from . import sit_tunnel
    from . import sms_server
    from . import snmp
    from . import sov_sase
    from . import speed_test_schedule
    from . import speed_test_server
    from . import speed_test_setting
    from . import ssh_config
    from . import sso_admin
    from . import sso_forticloud_admin
    from . import sso_fortigate_cloud_admin
    from . import standalone_cluster
    from . import storage
    from . import stp
    from . import switch_interface
    from . import timezone
    from . import tos_based_priority
    from . import vdom
    from . import vdom_dns
    from . import vdom_exception
    from . import vdom_link
    from . import vdom_netflow
    from . import vdom_property
    from . import vdom_radius_server
    from . import vdom_sflow
    from . import virtual_switch
    from . import virtual_wire_pair
    from . import vne_interface
    from . import vxlan
    from . import wccp
    from . import x3g_modem
    from . import x3g_modem_custom
    from . import zone


class System:
    """Type stub for System."""

    autoupdate: autoupdate.Autoupdate
    dhcp: dhcp.Dhcp
    dhcp6: dhcp6.Dhcp6
    lldp: lldp.Lldp
    replacemsg: replacemsg.Replacemsg
    security_rating: security_rating.SecurityRating
    snmp: snmp.Snmp
    x3g_modem: x3g_modem.X3gModem
    accprofile: accprofile.Accprofile
    acme: acme.Acme
    admin: admin.Admin
    affinity_interrupt: affinity_interrupt.AffinityInterrupt
    affinity_packet_redistribution: affinity_packet_redistribution.AffinityPacketRedistribution
    alarm: alarm.Alarm
    alias: alias.Alias
    api_user: api_user.ApiUser
    arp_table: arp_table.ArpTable
    auto_install: auto_install.AutoInstall
    auto_script: auto_script.AutoScript
    automation_action: automation_action.AutomationAction
    automation_condition: automation_condition.AutomationCondition
    automation_destination: automation_destination.AutomationDestination
    automation_stitch: automation_stitch.AutomationStitch
    automation_trigger: automation_trigger.AutomationTrigger
    central_management: central_management.CentralManagement
    cloud_service: cloud_service.CloudService
    console: console.Console
    csf: csf.Csf
    custom_language: custom_language.CustomLanguage
    ddns: ddns.Ddns
    dedicated_mgmt: dedicated_mgmt.DedicatedMgmt
    device_upgrade: device_upgrade.DeviceUpgrade
    device_upgrade_exemptions: device_upgrade_exemptions.DeviceUpgradeExemptions
    dns: dns.Dns
    dns64: dns64.Dns64
    dns_database: dns_database.DnsDatabase
    dns_server: dns_server.DnsServer
    dscp_based_priority: dscp_based_priority.DscpBasedPriority
    email_server: email_server.EmailServer
    evpn: evpn.Evpn
    external_resource: external_resource.ExternalResource
    fabric_vpn: fabric_vpn.FabricVpn
    federated_upgrade: federated_upgrade.FederatedUpgrade
    fips_cc: fips_cc.FipsCc
    fortiguard: fortiguard.Fortiguard
    fortisandbox: fortisandbox.Fortisandbox
    fsso_polling: fsso_polling.FssoPolling
    ftm_push: ftm_push.FtmPush
    geneve: geneve.Geneve
    geoip_country: geoip_country.GeoipCountry
    geoip_override: geoip_override.GeoipOverride
    global_setting: global_setting.GlobalSetting
    gre_tunnel: gre_tunnel.GreTunnel
    ha: ha.Ha
    ha_monitor: ha_monitor.HaMonitor
    health_check_fortiguard: health_check_fortiguard.HealthCheckFortiguard
    ike: ike.Ike
    interface: interface.Interface
    ipam: ipam.Ipam
    ipip_tunnel: ipip_tunnel.IpipTunnel
    ips: ips.Ips
    ips_urlfilter_dns: ips_urlfilter_dns.IpsUrlfilterDns
    ips_urlfilter_dns6: ips_urlfilter_dns6.IpsUrlfilterDns6
    ipsec_aggregate: ipsec_aggregate.IpsecAggregate
    ipv6_neighbor_cache: ipv6_neighbor_cache.Ipv6NeighborCache
    ipv6_tunnel: ipv6_tunnel.Ipv6Tunnel
    link_monitor: link_monitor.LinkMonitor
    lte_modem: lte_modem.LteModem
    mac_address_table: mac_address_table.MacAddressTable
    mobile_tunnel: mobile_tunnel.MobileTunnel
    modem: modem.Modem
    nd_proxy: nd_proxy.NdProxy
    netflow: netflow.Netflow
    network_visibility: network_visibility.NetworkVisibility
    ngfw_settings: ngfw_settings.NgfwSettings
    np6xlite: np6xlite.Np6xlite
    npu: npu.Npu
    ntp: ntp.Ntp
    object_tagging: object_tagging.ObjectTagging
    password_policy: password_policy.PasswordPolicy
    password_policy_guest_admin: password_policy_guest_admin.PasswordPolicyGuestAdmin
    pcp_server: pcp_server.PcpServer
    physical_switch: physical_switch.PhysicalSwitch
    pppoe_interface: pppoe_interface.PppoeInterface
    probe_response: probe_response.ProbeResponse
    proxy_arp: proxy_arp.ProxyArp
    ptp: ptp.Ptp
    replacemsg_group: replacemsg_group.ReplacemsgGroup
    replacemsg_image: replacemsg_image.ReplacemsgImage
    resource_limits: resource_limits.ResourceLimits
    saml: saml.Saml
    sdn_connector: sdn_connector.SdnConnector
    sdn_proxy: sdn_proxy.SdnProxy
    sdn_vpn: sdn_vpn.SdnVpn
    sdwan: sdwan.Sdwan
    session_helper: session_helper.SessionHelper
    session_ttl: session_ttl.SessionTtl
    settings: settings.Settings
    sflow: sflow.Sflow
    sit_tunnel: sit_tunnel.SitTunnel
    sms_server: sms_server.SmsServer
    sov_sase: sov_sase.SovSase
    speed_test_schedule: speed_test_schedule.SpeedTestSchedule
    speed_test_server: speed_test_server.SpeedTestServer
    speed_test_setting: speed_test_setting.SpeedTestSetting
    ssh_config: ssh_config.SshConfig
    sso_admin: sso_admin.SsoAdmin
    sso_forticloud_admin: sso_forticloud_admin.SsoForticloudAdmin
    sso_fortigate_cloud_admin: sso_fortigate_cloud_admin.SsoFortigateCloudAdmin
    standalone_cluster: standalone_cluster.StandaloneCluster
    storage: storage.Storage
    stp: stp.Stp
    switch_interface: switch_interface.SwitchInterface
    timezone: timezone.Timezone
    tos_based_priority: tos_based_priority.TosBasedPriority
    vdom: vdom.Vdom
    vdom_dns: vdom_dns.VdomDns
    vdom_exception: vdom_exception.VdomException
    vdom_link: vdom_link.VdomLink
    vdom_netflow: vdom_netflow.VdomNetflow
    vdom_property: vdom_property.VdomProperty
    vdom_radius_server: vdom_radius_server.VdomRadiusServer
    vdom_sflow: vdom_sflow.VdomSflow
    virtual_switch: virtual_switch.VirtualSwitch
    virtual_wire_pair: virtual_wire_pair.VirtualWirePair
    vne_interface: vne_interface.VneInterface
    vxlan: vxlan.Vxlan
    wccp: wccp.Wccp
    x3g_modem_custom: x3g_modem_custom.X3gModemCustom
    zone: zone.Zone

    def __init__(self, client: IHTTPClient) -> None: ...
