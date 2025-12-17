"""
FortiOS System API

System configuration endpoints for FortiOS including:
- Network interfaces
- Admin users and access profiles
- Global settings
- DNS, NTP, and time configuration
- High Availability (HA)
- SNMP monitoring
- DHCP/DHCPv6 servers
- Automation (actions, triggers, stitches)
- Tunnels (GRE, IPIP, IPv6, VXLAN, GENEVE)
- VDOMs and virtual networking
- Security services (FortiGuard, FortiSandbox, IPS)
- And 100+ more system configuration endpoints
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient


# Nested sub-category: system.3g-modem/*
class _Modem3g:
    """3G MODEM configuration sub-category"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def custom(self):
        """3G MODEM custom configuration"""
        from .modem_3g_custom import Modem3gCustom

        return Modem3gCustom(self._client)


# Nested sub-category: system.autoupdate/*
class _Autoupdate:
    """Auto-update configuration sub-category"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def schedule(self):
        """Update schedule configuration"""
        from .autoupdate_schedule import AutoupdateSchedule

        return AutoupdateSchedule(self._client)


# Nested sub-category: system.dhcp/*
class _Dhcp:
    """DHCP configuration sub-category"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def server(self):
        """DHCP servers configuration"""
        from .dhcp_server import DhcpServer

        return DhcpServer(self._client)


# Nested sub-category: system.dhcp6/*
class _Dhcp6:
    """DHCPv6 configuration sub-category"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def server(self):
        """DHCPv6 servers configuration"""
        from .dhcp6_server import Dhcp6Server

        return Dhcp6Server(self._client)


# Nested sub-category: system.lldp/*
class _Lldp:
    """LLDP configuration sub-category"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def network_policy(self):
        """LLDP network policy configuration"""
        from .lldp_network_policy import LldpNetworkPolicy

        return LldpNetworkPolicy(self._client)


# Nested sub-category: system.replacemsg/*
class _Replacemsg:
    """Replacement messages sub-category"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def admin(self):
        """Admin replacement messages"""
        from .replacemsg_admin import ReplacemsgAdmin

        return ReplacemsgAdmin(self._client)

    @property
    def alertmail(self):
        """Alert mail replacement messages"""
        from .replacemsg_alertmail import ReplacemsgAlertmail

        return ReplacemsgAlertmail(self._client)

    @property
    def auth(self):
        """Authentication replacement messages"""
        from .replacemsg_auth import ReplacemsgAuth

        return ReplacemsgAuth(self._client)

    @property
    def automation(self):
        """Automation replacement messages"""
        from .replacemsg_automation import ReplacemsgAutomation

        return ReplacemsgAutomation(self._client)

    @property
    def fortiguard_wf(self):
        """FortiGuard web filter replacement messages"""
        from .replacemsg_fortiguard_wf import ReplacemsgFortiguardWf

        return ReplacemsgFortiguardWf(self._client)

    @property
    def http(self):
        """HTTP replacement messages"""
        from .replacemsg_http import ReplacemsgHttp

        return ReplacemsgHttp(self._client)

    @property
    def mail(self):
        """Mail replacement messages"""
        from .replacemsg_mail import ReplacemsgMail

        return ReplacemsgMail(self._client)

    @property
    def nac_quar(self):
        """NAC quarantine replacement messages"""
        from .replacemsg_nac_quar import ReplacemsgNacQuar

        return ReplacemsgNacQuar(self._client)

    @property
    def spam(self):
        """Spam replacement messages"""
        from .replacemsg_spam import ReplacemsgSpam

        return ReplacemsgSpam(self._client)

    @property
    def sslvpn(self):
        """SSL VPN replacement messages"""
        from .replacemsg_sslvpn import ReplacemsgSslvpn

        return ReplacemsgSslvpn(self._client)

    @property
    def traffic_quota(self):
        """Traffic quota replacement messages"""
        from .replacemsg_traffic_quota import ReplacemsgTrafficQuota

        return ReplacemsgTrafficQuota(self._client)

    @property
    def utm(self):
        """UTM replacement messages"""
        from .replacemsg_utm import ReplacemsgUtm

        return ReplacemsgUtm(self._client)


# Nested sub-category: system.security-rating/*
class _SecurityRating:
    """Security Rating sub-category"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def controls(self):
        """Security Rating controls configuration"""
        from .security_rating_controls import SecurityRatingControls

        return SecurityRatingControls(self._client)

    @property
    def settings(self):
        """Security Rating settings configuration"""
        from .security_rating_settings import SecurityRatingSettings

        return SecurityRatingSettings(self._client)


# Nested sub-category: system.snmp/*
class _Snmp:
    """SNMP configuration sub-category"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def community(self):
        """SNMP community configuration"""
        from .snmp_community import SnmpCommunity

        return SnmpCommunity(self._client)

    @property
    def mib_view(self):
        """SNMP MIB view configuration"""
        from .snmp_mib_view import SnmpMibView

        return SnmpMibView(self._client)

    @property
    def rmon_stat(self):
        """SNMP RMON statistics configuration"""
        from .snmp_rmon_stat import SnmpRmonStat

        return SnmpRmonStat(self._client)

    @property
    def sysinfo(self):
        """SNMP system info configuration"""
        from .snmp_sysinfo import SnmpSysinfo

        return SnmpSysinfo(self._client)

    @property
    def user(self):
        """SNMP user configuration"""
        from .snmp_user import SnmpUser

        return SnmpUser(self._client)


# Main System category class
class System:
    """
    FortiOS System Configuration API
    
    Provides access to all system configuration endpoints including:
    - Core system: interface, admin, global, dns, ntp, ha
    - Sub-categories: snmp, dhcp, dhcp6, lldp, replacemsg, security_rating
    - Automation: actions, triggers, stitches, conditions
    - Tunnels: GRE, IPIP, IPv6, VXLAN, GENEVE
    - Virtual networking: VDOMs, virtual switches, zones
    - Security services: FortiGuard, FortiSandbox, IPS
    - And 100+ more system configuration endpoints
    
    Usage:
        >>> # Access nested sub-categories
        >>> fgt.api.cmdb.system.snmp.community.list()
        >>> fgt.api.cmdb.system.dhcp.server.create(name='dhcp1')
        >>> 
        >>> # Access direct endpoints
        >>> fgt.api.cmdb.system.interface.list()
        >>> fgt.api.cmdb.system.admin.create(name='admin1')
    """

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client
        
        # Initialize nested sub-categories
        self._modem_3g = _Modem3g(client)
        self._autoupdate = _Autoupdate(client)
        self._dhcp = _Dhcp(client)
        self._dhcp6 = _Dhcp6(client)
        self._lldp = _Lldp(client)
        self._replacemsg = _Replacemsg(client)
        self._security_rating = _SecurityRating(client)
        self._snmp = _Snmp(client)

    # Nested sub-categories properties
    @property
    def modem_3g(self) -> _Modem3g:
        """3G MODEM configuration (system.3g-modem/*)"""
        return self._modem_3g

    @property
    def autoupdate(self) -> _Autoupdate:
        """Auto-update configuration (system.autoupdate/*)"""
        return self._autoupdate

    @property
    def dhcp(self) -> _Dhcp:
        """DHCP configuration (system.dhcp/*)"""
        return self._dhcp

    @property
    def dhcp6(self) -> _Dhcp6:
        """DHCPv6 configuration (system.dhcp6/*)"""
        return self._dhcp6

    @property
    def lldp(self) -> _Lldp:
        """LLDP configuration (system.lldp/*)"""
        return self._lldp

    @property
    def replacemsg(self) -> _Replacemsg:
        """Replacement messages (system.replacemsg/*)"""
        return self._replacemsg

    @property
    def security_rating(self) -> _SecurityRating:
        """Security Rating configuration (system.security-rating/*)"""
        return self._security_rating

    @property
    def snmp(self) -> _Snmp:
        """SNMP configuration (system.snmp/*)"""
        return self._snmp

    # Direct endpoint properties (lazy-loaded)
    # Critical/Most Used Endpoints
    @property
    def interface(self):
        """Network interfaces configuration"""
        from .interface import Interface

        return Interface(self._client)

    @property
    def admin(self):
        """Admin users configuration"""
        from .admin import Admin

        return Admin(self._client)

    @property
    def global_settings(self):
        """Global system settings (singleton)"""
        from .global_settings import GlobalSettings

        return GlobalSettings(self._client)

    @property
    def dns(self):
        """DNS configuration (singleton)"""
        from .dns import Dns

        return Dns(self._client)

    @property
    def ntp(self):
        """NTP configuration (singleton)"""
        from .ntp import Ntp

        return Ntp(self._client)

    @property
    def ha(self):
        """High Availability configuration (singleton)"""
        from .ha import Ha

        return Ha(self._client)

    @property
    def accprofile(self):
        """Access profiles for system administrators"""
        from .accprofile import Accprofile

        return Accprofile(self._client)

    @property
    def api_user(self):
        """API users configuration"""
        from .api_user import ApiUser

        return ApiUser(self._client)

    @property
    def settings(self):
        """VDOM settings (singleton)"""
        from .settings import Settings

        return Settings(self._client)

    @property
    def zone(self):
        """Zone configuration"""
        from .zone import Zone

        return Zone(self._client)

    # Automation Endpoints
    @property
    def automation_action(self):
        """Automation actions"""
        from .automation_action import AutomationAction

        return AutomationAction(self._client)

    @property
    def automation_condition(self):
        """Automation conditions"""
        from .automation_condition import AutomationCondition

        return AutomationCondition(self._client)

    @property
    def automation_destination(self):
        """Automation destinations"""
        from .automation_destination import AutomationDestination

        return AutomationDestination(self._client)

    @property
    def automation_stitch(self):
        """Automation stitches"""
        from .automation_stitch import AutomationStitch

        return AutomationStitch(self._client)

    @property
    def automation_trigger(self):
        """Automation triggers"""
        from .automation_trigger import AutomationTrigger

        return AutomationTrigger(self._client)

    # Tunnel Endpoints
    @property
    def gre_tunnel(self):
        """GRE tunnel configuration"""
        from .gre_tunnel import GreTunnel

        return GreTunnel(self._client)

    @property
    def ipip_tunnel(self):
        """IPIP tunnel configuration"""
        from .ipip_tunnel import IpipTunnel

        return IpipTunnel(self._client)

    @property
    def ipv6_tunnel(self):
        """IPv6 tunnel configuration"""
        from .ipv6_tunnel import Ipv6Tunnel

        return Ipv6Tunnel(self._client)

    @property
    def sit_tunnel(self):
        """SIT tunnel configuration"""
        from .sit_tunnel import SitTunnel

        return SitTunnel(self._client)

    @property
    def vxlan(self):
        """VXLAN devices configuration"""
        from .vxlan import Vxlan

        return Vxlan(self._client)

    @property
    def geneve(self):
        """GENEVE devices configuration"""
        from .geneve import Geneve

        return Geneve(self._client)

    @property
    def mobile_tunnel(self):
        """Mobile tunnel configuration"""
        from .mobile_tunnel import MobileTunnel

        return MobileTunnel(self._client)

    # SDN/Cloud Endpoints
    @property
    def sdn_connector(self):
        """SDN connector configuration"""
        from .sdn_connector import SdnConnector

        return SdnConnector(self._client)

    @property
    def sdn_proxy(self):
        """SDN proxy configuration"""
        from .sdn_proxy import SdnProxy

        return SdnProxy(self._client)

    @property
    def sdn_vpn(self):
        """SDN VPN configuration"""
        from .sdn_vpn import SdnVpn

        return SdnVpn(self._client)

    @property
    def cloud_service(self):
        """Cloud service configuration"""
        from .cloud_service import CloudService

        return CloudService(self._client)

    # VDOM Endpoints
    @property
    def vdom(self):
        """Virtual domain configuration"""
        from .vdom import Vdom

        return Vdom(self._client)

    @property
    def vdom_dns(self):
        """VDOM DNS configuration (singleton)"""
        from .vdom_dns import VdomDns

        return VdomDns(self._client)

    @property
    def vdom_exception(self):
        """VDOM exception configuration"""
        from .vdom_exception import VdomException

        return VdomException(self._client)

    @property
    def vdom_link(self):
        """VDOM link configuration"""
        from .vdom_link import VdomLink

        return VdomLink(self._client)

    @property
    def vdom_netflow(self):
        """VDOM NetFlow configuration (singleton)"""
        from .vdom_netflow import VdomNetflow

        return VdomNetflow(self._client)

    @property
    def vdom_property(self):
        """VDOM property configuration"""
        from .vdom_property import VdomProperty

        return VdomProperty(self._client)

    @property
    def vdom_radius_server(self):
        """VDOM RADIUS server configuration"""
        from .vdom_radius_server import VdomRadiusServer

        return VdomRadiusServer(self._client)

    @property
    def vdom_sflow(self):
        """VDOM sFlow configuration (singleton)"""
        from .vdom_sflow import VdomSflow

        return VdomSflow(self._client)

    @property
    def virtual_switch(self):
        """Virtual switch configuration"""
        from .virtual_switch import VirtualSwitch

        return VirtualSwitch(self._client)

    @property
    def virtual_wire_pair(self):
        """Virtual wire pair configuration"""
        from .virtual_wire_pair import VirtualWirePair

        return VirtualWirePair(self._client)

    # Network/Switch Endpoints
    @property
    def switch_interface(self):
        """Software switch interface configuration"""
        from .switch_interface import SwitchInterface

        return SwitchInterface(self._client)

    @property
    def physical_switch(self):
        """Physical switch configuration"""
        from .physical_switch import PhysicalSwitch

        return PhysicalSwitch(self._client)

    @property
    def pppoe_interface(self):
        """PPPoE interface configuration"""
        from .pppoe_interface import PppoeInterface

        return PppoeInterface(self._client)

    @property
    def mac_address_table(self):
        """MAC address table configuration"""
        from .mac_address_table import MacAddressTable

        return MacAddressTable(self._client)

    @property
    def arp_table(self):
        """ARP table configuration"""
        from .arp_table import ArpTable

        return ArpTable(self._client)

    @property
    def ipv6_neighbor_cache(self):
        """IPv6 neighbor cache configuration"""
        from .ipv6_neighbor_cache import Ipv6NeighborCache

        return Ipv6NeighborCache(self._client)

    @property
    def link_monitor(self):
        """Link health monitor configuration"""
        from .link_monitor import LinkMonitor

        return LinkMonitor(self._client)

    @property
    def vne_interface(self):
        """VNE interface configuration"""
        from .vne_interface import VneInterface

        return VneInterface(self._client)

    # Security/Policy Endpoints
    @property
    def ipsec_aggregate(self):
        """IPsec aggregate configuration"""
        from .ipsec_aggregate import IpsecAggregate

        return IpsecAggregate(self._client)

    @property
    def ike(self):
        """IKE global attributes (singleton)"""
        from .ike import Ike

        return Ike(self._client)

    @property
    def fortiguard(self):
        """FortiGuard services configuration (singleton)"""
        from .fortiguard import Fortiguard

        return Fortiguard(self._client)

    @property
    def fortisandbox(self):
        """FortiSandbox configuration (singleton)"""
        from .fortisandbox import Fortisandbox

        return Fortisandbox(self._client)

    @property
    def csf(self):
        """Security Fabric configuration (singleton)"""
        from .csf import Csf

        return Csf(self._client)

    @property
    def standalone_cluster(self):
        """Standalone cluster configuration (singleton)"""
        from .standalone_cluster import StandaloneCluster

        return StandaloneCluster(self._client)

    @property
    def session_helper(self):
        """Session helper configuration"""
        from .session_helper import SessionHelper

        return SessionHelper(self._client)

    @property
    def session_ttl(self):
        """Session TTL configuration (singleton)"""
        from .session_ttl import SessionTtl

        return SessionTtl(self._client)

    # Monitoring/Logging Endpoints
    @property
    def netflow(self):
        """NetFlow configuration (singleton)"""
        from .netflow import Netflow

        return Netflow(self._client)

    @property
    def sflow(self):
        """sFlow configuration (singleton)"""
        from .sflow import Sflow

        return Sflow(self._client)

    @property
    def network_visibility(self):
        """Network visibility configuration (singleton)"""
        from .network_visibility import NetworkVisibility

        return NetworkVisibility(self._client)

    @property
    def probe_response(self):
        """Probe response configuration (singleton)"""
        from .probe_response import ProbeResponse

        return ProbeResponse(self._client)

    @property
    def alarm(self):
        """Alarm configuration (singleton)"""
        from .alarm import Alarm

        return Alarm(self._client)

    @property
    def replacemsg_group(self):
        """Replacement message groups"""
        from .replacemsg_group import ReplacemsgGroup

        return ReplacemsgGroup(self._client)

    @property
    def replacemsg_image(self):
        """Replacement message images"""
        from .replacemsg_image import ReplacemsgImage

        return ReplacemsgImage(self._client)

    @property
    def email_server(self):
        """Email server configuration (singleton)"""
        from .email_server import EmailServer

        return EmailServer(self._client)

    @property
    def sms_server(self):
        """SMS server configuration"""
        from .sms_server import SmsServer

        return SmsServer(self._client)

    @property
    def wccp(self):
        """WCCP configuration"""
        from .wccp import Wccp

        return Wccp(self._client)

    # SSO/Authentication Endpoints
    @property
    def fsso_polling(self):
        """FSSO polling configuration (singleton)"""
        from .fsso_polling import FssoPolling

        return FssoPolling(self._client)

    @property
    def ftm_push(self):
        """FortiToken Mobile push configuration (singleton)"""
        from .ftm_push import FtmPush

        return FtmPush(self._client)

    @property
    def saml(self):
        """SAML authentication configuration (singleton)"""
        from .saml import Saml

        return Saml(self._client)

    @property
    def sso_admin(self):
        """SSO admin users"""
        from .sso_admin import SsoAdmin

        return SsoAdmin(self._client)

    @property
    def sso_forticloud_admin(self):
        """FortiCloud SSO admin users"""
        from .sso_forticloud_admin import SsoForticloudAdmin

        return SsoForticloudAdmin(self._client)

    @property
    def sso_fortigate_cloud_admin(self):
        """FortiGate Cloud SSO admin users"""
        from .sso_fortigate_cloud_admin import SsoFortigateCloudAdmin

        return SsoFortigateCloudAdmin(self._client)

    # System Configuration Endpoints
    @property
    def alias(self):
        """Alias command configuration"""
        from .alias import Alias

        return Alias(self._client)

    @property
    def custom_language(self):
        """Custom language configuration"""
        from .custom_language import CustomLanguage

        return CustomLanguage(self._client)

    @property
    def ddns(self):
        """DDNS configuration"""
        from .ddns import Ddns

        return Ddns(self._client)

    @property
    def dns_database(self):
        """DNS database configuration"""
        from .dns_database import DnsDatabase

        return DnsDatabase(self._client)

    @property
    def dns_server(self):
        """DNS server configuration"""
        from .dns_server import DnsServer

        return DnsServer(self._client)

    @property
    def dns64(self):
        """DNS64 configuration (singleton)"""
        from .dns64 import Dns64

        return Dns64(self._client)

    @property
    def external_resource(self):
        """External resource configuration"""
        from .external_resource import ExternalResource

        return ExternalResource(self._client)

    @property
    def geoip_country(self):
        """GeoIP country configuration"""
        from .geoip_country import GeoipCountry

        return GeoipCountry(self._client)

    @property
    def geoip_override(self):
        """GeoIP override configuration"""
        from .geoip_override import GeoipOverride

        return GeoipOverride(self._client)

    @property
    def object_tagging(self):
        """Object tagging configuration"""
        from .object_tagging import ObjectTagging

        return ObjectTagging(self._client)

    @property
    def storage(self):
        """Logical storage configuration"""
        from .storage import Storage

        return Storage(self._client)

    @property
    def timezone(self):
        """Timezone configuration"""
        from .timezone import Timezone

        return Timezone(self._client)

    @property
    def console(self):
        """Console configuration (singleton)"""
        from .console import Console

        return Console(self._client)

    @property
    def ssh_config(self):
        """SSH configuration (singleton)"""
        from .ssh_config import SshConfig

        return SshConfig(self._client)

    @property
    def dedicated_mgmt(self):
        """Dedicated management configuration (singleton)"""
        from .dedicated_mgmt import DedicatedMgmt

        return DedicatedMgmt(self._client)

    # Performance/QoS Endpoints
    @property
    def dscp_based_priority(self):
        """DSCP-based priority configuration"""
        from .dscp_based_priority import DscpBasedPriority

        return DscpBasedPriority(self._client)

    @property
    def tos_based_priority(self):
        """ToS-based priority configuration"""
        from .tos_based_priority import TosBasedPriority

        return TosBasedPriority(self._client)

    @property
    def affinity_interrupt(self):
        """Interrupt affinity configuration"""
        from .affinity_interrupt import AffinityInterrupt

        return AffinityInterrupt(self._client)

    @property
    def affinity_packet_redistribution(self):
        """Packet redistribution affinity configuration"""
        from .affinity_packet_redistribution import AffinityPacketRedistribution

        return AffinityPacketRedistribution(self._client)

    @property
    def np6xlite(self):
        """NP6XLITE attributes configuration"""
        from .np6xlite import Np6xlite

        return Np6xlite(self._client)

    @property
    def npu(self):
        """NPU attributes configuration (singleton)"""
        from .npu import Npu

        return Npu(self._client)

    # Miscellaneous Endpoints
    @property
    def acme(self):
        """ACME client configuration (singleton)"""
        from .acme import Acme

        return Acme(self._client)

    @property
    def auto_install(self):
        """USB auto installation configuration (singleton)"""
        from .auto_install import AutoInstall

        return AutoInstall(self._client)

    @property
    def auto_script(self):
        """Auto script configuration"""
        from .auto_script import AutoScript

        return AutoScript(self._client)

    @property
    def central_management(self):
        """Central management configuration (singleton)"""
        from .central_management import CentralManagement

        return CentralManagement(self._client)

    @property
    def device_upgrade(self):
        """Device upgrade configuration"""
        from .device_upgrade import DeviceUpgrade

        return DeviceUpgrade(self._client)

    @property
    def device_upgrade_exemptions(self):
        """Device upgrade exemptions"""
        from .device_upgrade_exemptions import DeviceUpgradeExemptions

        return DeviceUpgradeExemptions(self._client)

    @property
    def evpn(self):
        """EVPN instance configuration"""
        from .evpn import Evpn

        return Evpn(self._client)

    @property
    def fabric_vpn(self):
        """Fabric VPN configuration (singleton)"""
        from .fabric_vpn import FabricVpn

        return FabricVpn(self._client)

    @property
    def federated_upgrade(self):
        """Federated upgrade configuration (singleton)"""
        from .federated_upgrade import FederatedUpgrade

        return FederatedUpgrade(self._client)

    @property
    def fips_cc(self):
        """FIPS-CC mode configuration (singleton)"""
        from .fips_cc import FipsCc

        return FipsCc(self._client)

    @property
    def ha_monitor(self):
        """HA monitor configuration (singleton)"""
        from .ha_monitor import HaMonitor

        return HaMonitor(self._client)

    @property
    def health_check_fortiguard(self):
        """FortiGuard health check configuration"""
        from .health_check_fortiguard import HealthCheckFortiguard

        return HealthCheckFortiguard(self._client)

    @property
    def ipam(self):
        """IPAM configuration (singleton)"""
        from .ipam import Ipam

        return Ipam(self._client)

    @property
    def ips(self):
        """IPS system settings (singleton)"""
        from .ips import Ips

        return Ips(self._client)

    @property
    def ips_urlfilter_dns(self):
        """IPS URL filter DNS servers"""
        from .ips_urlfilter_dns import IpsUrlfilterDns

        return IpsUrlfilterDns(self._client)

    @property
    def ips_urlfilter_dns6(self):
        """IPS URL filter IPv6 DNS servers"""
        from .ips_urlfilter_dns6 import IpsUrlfilterDns6

        return IpsUrlfilterDns6(self._client)

    @property
    def lte_modem(self):
        """LTE/WIMAX modem configuration (singleton)"""
        from .lte_modem import LteModem

        return LteModem(self._client)

    @property
    def modem(self):
        """MODEM configuration (singleton)"""
        from .modem import Modem

        return Modem(self._client)

    @property
    def nd_proxy(self):
        """ND proxy configuration (singleton)"""
        from .nd_proxy import NdProxy

        return NdProxy(self._client)

    @property
    def ngfw_settings(self):
        """NGFW settings (singleton)"""
        from .ngfw_settings import NgfwSettings

        return NgfwSettings(self._client)

    @property
    def password_policy(self):
        """Password policy configuration (singleton)"""
        from .password_policy import PasswordPolicy

        return PasswordPolicy(self._client)

    @property
    def password_policy_guest_admin(self):
        """Guest admin password policy configuration (singleton)"""
        from .password_policy_guest_admin import PasswordPolicyGuestAdmin

        return PasswordPolicyGuestAdmin(self._client)

    @property
    def pcp_server(self):
        """PCP server configuration (singleton)"""
        from .pcp_server import PcpServer

        return PcpServer(self._client)

    @property
    def ptp(self):
        """PTP configuration (singleton)"""
        from .ptp import Ptp

        return Ptp(self._client)

    @property
    def proxy_arp(self):
        """Proxy ARP configuration"""
        from .proxy_arp import ProxyArp

        return ProxyArp(self._client)

    @property
    def resource_limits(self):
        """Resource limits configuration (singleton)"""
        from .resource_limits import ResourceLimits

        return ResourceLimits(self._client)

    @property
    def sdwan(self):
        """SD-WAN configuration (singleton)"""
        from .sdwan import Sdwan

        return Sdwan(self._client)

    @property
    def sov_sase(self):
        """Sovereign SASE configuration (singleton)"""
        from .sov_sase import SovSase

        return SovSase(self._client)

    @property
    def speed_test_schedule(self):
        """Speed test schedule configuration"""
        from .speed_test_schedule import SpeedTestSchedule

        return SpeedTestSchedule(self._client)

    @property
    def speed_test_server(self):
        """Speed test server configuration"""
        from .speed_test_server import SpeedTestServer

        return SpeedTestServer(self._client)

    @property
    def speed_test_setting(self):
        """Speed test settings (singleton)"""
        from .speed_test_setting import SpeedTestSetting

        return SpeedTestSetting(self._client)

    @property
    def stp(self):
        """STP configuration (singleton)"""
        from .stp import Stp

        return Stp(self._client)

    def __dir__(self):
        """Custom dir() to show all available endpoints"""
        return [
            # Nested sub-categories
            "modem_3g",
            "autoupdate",
            "dhcp",
            "dhcp6",
            "lldp",
            "replacemsg",
            "security_rating",
            "snmp",
            # Critical/Most Used
            "interface",
            "admin",
            "global_settings",
            "dns",
            "ntp",
            "ha",
            "accprofile",
            "api_user",
            "settings",
            "zone",
            # Automation
            "automation_action",
            "automation_condition",
            "automation_destination",
            "automation_stitch",
            "automation_trigger",
            # Tunnels
            "gre_tunnel",
            "ipip_tunnel",
            "ipv6_tunnel",
            "sit_tunnel",
            "vxlan",
            "geneve",
            "mobile_tunnel",
            # SDN/Cloud
            "sdn_connector",
            "sdn_proxy",
            "sdn_vpn",
            "cloud_service",
            # VDOM
            "vdom",
            "vdom_dns",
            "vdom_exception",
            "vdom_link",
            "vdom_netflow",
            "vdom_property",
            "vdom_radius_server",
            "vdom_sflow",
            "virtual_switch",
            "virtual_wire_pair",
            # Network/Switch
            "switch_interface",
            "physical_switch",
            "pppoe_interface",
            "mac_address_table",
            "arp_table",
            "ipv6_neighbor_cache",
            "link_monitor",
            "vne_interface",
            # Security/Policy
            "ipsec_aggregate",
            "ike",
            "fortiguard",
            "fortisandbox",
            "csf",
            "standalone_cluster",
            "session_helper",
            "session_ttl",
            # Monitoring/Logging
            "netflow",
            "sflow",
            "network_visibility",
            "probe_response",
            "alarm",
            "replacemsg_group",
            "replacemsg_image",
            "email_server",
            "sms_server",
            "wccp",
            # SSO/Authentication
            "fsso_polling",
            "ftm_push",
            "saml",
            "sso_admin",
            "sso_forticloud_admin",
            "sso_fortigate_cloud_admin",
            # System Configuration
            "alias",
            "custom_language",
            "ddns",
            "dns_database",
            "dns_server",
            "dns64",
            "external_resource",
            "geoip_country",
            "geoip_override",
            "object_tagging",
            "storage",
            "timezone",
            "console",
            "ssh_config",
            "dedicated_mgmt",
            # Performance/QoS
            "dscp_based_priority",
            "tos_based_priority",
            "affinity_interrupt",
            "affinity_packet_redistribution",
            "np6xlite",
            "npu",
            # Miscellaneous
            "acme",
            "auto_install",
            "auto_script",
            "central_management",
            "device_upgrade",
            "device_upgrade_exemptions",
            "evpn",
            "fabric_vpn",
            "federated_upgrade",
            "fips_cc",
            "ha_monitor",
            "health_check_fortiguard",
            "ipam",
            "ips",
            "ips_urlfilter_dns",
            "ips_urlfilter_dns6",
            "lte_modem",
            "modem",
            "nd_proxy",
            "ngfw_settings",
            "password_policy",
            "password_policy_guest_admin",
            "pcp_server",
            "ptp",
            "proxy_arp",
            "resource_limits",
            "sdwan",
            "sov_sase",
            "speed_test_schedule",
            "speed_test_server",
            "speed_test_setting",
            "stp",
        ]
