"""Type stubs for SYSTEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .acme_certificate_status import AcmeCertificateStatus, AcmeCertificateStatusDictMode, AcmeCertificateStatusObjectMode
    from .acquired_dns import AcquiredDns, AcquiredDnsDictMode, AcquiredDnsObjectMode
    from .available_certificates import AvailableCertificates, AvailableCertificatesDictMode, AvailableCertificatesObjectMode
    from .check_port_availability import CheckPortAvailability, CheckPortAvailabilityDictMode, CheckPortAvailabilityObjectMode
    from .current_admins import CurrentAdmins, CurrentAdminsDictMode, CurrentAdminsObjectMode
    from .global_resources import GlobalResources, GlobalResourcesDictMode, GlobalResourcesObjectMode
    from .global_search import GlobalSearch, GlobalSearchDictMode, GlobalSearchObjectMode
    from .ha_backup_hb_used import HaBackupHbUsed, HaBackupHbUsedDictMode, HaBackupHbUsedObjectMode
    from .ha_checksums import HaChecksums, HaChecksumsDictMode, HaChecksumsObjectMode
    from .ha_history import HaHistory, HaHistoryDictMode, HaHistoryObjectMode
    from .ha_hw_interface import HaHwInterface, HaHwInterfaceDictMode, HaHwInterfaceObjectMode
    from .ha_nonsync_checksums import HaNonsyncChecksums, HaNonsyncChecksumsDictMode, HaNonsyncChecksumsObjectMode
    from .ha_statistics import HaStatistics, HaStatisticsDictMode, HaStatisticsObjectMode
    from .ha_table_checksums import HaTableChecksums, HaTableChecksumsDictMode, HaTableChecksumsObjectMode
    from .interface_connected_admins_info import InterfaceConnectedAdminsInfo, InterfaceConnectedAdminsInfoDictMode, InterfaceConnectedAdminsInfoObjectMode
    from .ipconf import Ipconf, IpconfDictMode, IpconfObjectMode
    from .link_monitor import LinkMonitor, LinkMonitorDictMode, LinkMonitorObjectMode
    from .modem3g import Modem3g, Modem3gDictMode, Modem3gObjectMode
    from .monitor_sensor import MonitorSensor, MonitorSensorDictMode, MonitorSensorObjectMode
    from .resolve_fqdn import ResolveFqdn, ResolveFqdnDictMode, ResolveFqdnObjectMode
    from .running_processes import RunningProcesses, RunningProcessesDictMode, RunningProcessesObjectMode
    from .sensor_info import SensorInfo, SensorInfoDictMode, SensorInfoObjectMode
    from .status import Status, StatusDictMode, StatusObjectMode
    from .storage import Storage, StorageDictMode, StorageObjectMode
    from .timezone import Timezone, TimezoneDictMode, TimezoneObjectMode
    from .trusted_cert_authorities import TrustedCertAuthorities, TrustedCertAuthoritiesDictMode, TrustedCertAuthoritiesObjectMode
    from .vdom_link import VdomLink, VdomLinkDictMode, VdomLinkObjectMode
    from .vdom_resource import VdomResource, VdomResourceDictMode, VdomResourceObjectMode
    from .vm_information import VmInformation, VmInformationDictMode, VmInformationObjectMode
    from .admin import Admin, AdminDictMode, AdminObjectMode
    from .api_user import ApiUser, ApiUserDictMode, ApiUserObjectMode
    from .automation_action import AutomationAction, AutomationActionDictMode, AutomationActionObjectMode
    from .automation_stitch import AutomationStitch, AutomationStitchDictMode, AutomationStitchObjectMode
    from .available_interfaces import AvailableInterfaces
    from .botnet import Botnet
    from .botnet_domains import BotnetDomains
    from .central_management import CentralManagement, CentralManagementDictMode, CentralManagementObjectMode
    from .certificate import Certificate, CertificateDictMode, CertificateObjectMode
    from .change_password import ChangePassword, ChangePasswordDictMode, ChangePasswordObjectMode
    from .cluster import Cluster, ClusterDictMode, ClusterObjectMode
    from .com_log import ComLog, ComLogDictMode, ComLogObjectMode
    from .config import Config, ConfigDictMode, ConfigObjectMode
    from .config_error_log import ConfigErrorLog, ConfigErrorLogDictMode, ConfigErrorLogObjectMode
    from .config_revision import ConfigRevision
    from .config_script import ConfigScript
    from .config_sync import ConfigSync, ConfigSyncDictMode, ConfigSyncObjectMode
    from .crash_log import CrashLog, CrashLogDictMode, CrashLogObjectMode
    from .csf import Csf
    from .debug import Debug, DebugDictMode, DebugObjectMode
    from .dhcp import Dhcp
    from .dhcp6 import Dhcp6, Dhcp6DictMode, Dhcp6ObjectMode
    from .disconnect_admins import DisconnectAdmins, DisconnectAdminsDictMode, DisconnectAdminsObjectMode
    from .external_resource import ExternalResource, ExternalResourceDictMode, ExternalResourceObjectMode
    from .firmware import Firmware
    from .fortiguard import Fortiguard, FortiguardDictMode, FortiguardObjectMode
    from .fortimanager import Fortimanager, FortimanagerDictMode, FortimanagerObjectMode
    from .fsck import Fsck, FsckDictMode, FsckObjectMode
    from .ha_peer import HaPeer
    from .hscalefw_license import HscalefwLicense, HscalefwLicenseDictMode, HscalefwLicenseObjectMode
    from .interface import Interface
    from .ipam import Ipam, IpamDictMode, IpamObjectMode
    from .logdisk import Logdisk, LogdiskDictMode, LogdiskObjectMode
    from .lte_modem import LteModem, LteModemDictMode, LteModemObjectMode
    from .modem import Modem
    from .modem5g import Modem5g, Modem5gDictMode, Modem5gObjectMode
    from .ntp import Ntp, NtpDictMode, NtpObjectMode
    from .object import Object, ObjectDictMode, ObjectObjectMode
    from .os import Os, OsDictMode, OsObjectMode
    from .password_policy_conform import PasswordPolicyConform, PasswordPolicyConformDictMode, PasswordPolicyConformObjectMode
    from .performance import Performance, PerformanceDictMode, PerformanceObjectMode
    from .private_data_encryption import PrivateDataEncryption, PrivateDataEncryptionDictMode, PrivateDataEncryptionObjectMode
    from .process import Process, ProcessDictMode, ProcessObjectMode
    from .resource import Resource, ResourceDictMode, ResourceObjectMode
    from .sandbox import Sandbox, SandboxDictMode, SandboxObjectMode
    from .sdn_connector import SdnConnector, SdnConnectorDictMode, SdnConnectorObjectMode
    from .time import Time
    from .traffic_history import TrafficHistory, TrafficHistoryDictMode, TrafficHistoryObjectMode
    from .upgrade_report import UpgradeReport, UpgradeReportDictMode, UpgradeReportObjectMode
    from .usb_device import UsbDevice, UsbDeviceDictMode, UsbDeviceObjectMode
    from .usb_log import UsbLog
    from .vmlicense import Vmlicense, VmlicenseDictMode, VmlicenseObjectMode

__all__ = [
    "AcmeCertificateStatus",
    "AcquiredDns",
    "AvailableCertificates",
    "CheckPortAvailability",
    "CurrentAdmins",
    "GlobalResources",
    "GlobalSearch",
    "HaBackupHbUsed",
    "HaChecksums",
    "HaHistory",
    "HaHwInterface",
    "HaNonsyncChecksums",
    "HaStatistics",
    "HaTableChecksums",
    "InterfaceConnectedAdminsInfo",
    "Ipconf",
    "LinkMonitor",
    "Modem3g",
    "MonitorSensor",
    "ResolveFqdn",
    "RunningProcesses",
    "SensorInfo",
    "Status",
    "Storage",
    "Timezone",
    "TrustedCertAuthorities",
    "VdomLink",
    "VdomResource",
    "VmInformation",
    "SystemDictMode",
    "SystemObjectMode",
]

class SystemDictMode:
    """SYSTEM API category for dict response mode.
    
    This class is returned when the client is instantiated with response_mode="dict" (default).
    All endpoints return dict/TypedDict responses by default.
    """
    
    admin: AdminDictMode
    api_user: ApiUserDictMode
    automation_action: AutomationActionDictMode
    automation_stitch: AutomationStitchDictMode
    available_interfaces: AvailableInterfaces
    botnet: Botnet
    botnet_domains: BotnetDomains
    central_management: CentralManagementDictMode
    certificate: CertificateDictMode
    change_password: ChangePasswordDictMode
    cluster: ClusterDictMode
    com_log: ComLogDictMode
    config: ConfigDictMode
    config_error_log: ConfigErrorLogDictMode
    config_revision: ConfigRevision
    config_script: ConfigScript
    config_sync: ConfigSyncDictMode
    crash_log: CrashLogDictMode
    csf: Csf
    debug: DebugDictMode
    dhcp: Dhcp
    dhcp6: Dhcp6DictMode
    disconnect_admins: DisconnectAdminsDictMode
    external_resource: ExternalResourceDictMode
    firmware: Firmware
    fortiguard: FortiguardDictMode
    fortimanager: FortimanagerDictMode
    fsck: FsckDictMode
    ha_peer: HaPeer
    hscalefw_license: HscalefwLicenseDictMode
    interface: Interface
    ipam: IpamDictMode
    logdisk: LogdiskDictMode
    lte_modem: LteModemDictMode
    modem: Modem
    modem5g: Modem5gDictMode
    ntp: NtpDictMode
    object: ObjectDictMode
    os: OsDictMode
    password_policy_conform: PasswordPolicyConformDictMode
    performance: PerformanceDictMode
    private_data_encryption: PrivateDataEncryptionDictMode
    process: ProcessDictMode
    resource: ResourceDictMode
    sandbox: SandboxDictMode
    sdn_connector: SdnConnectorDictMode
    time: Time
    traffic_history: TrafficHistoryDictMode
    upgrade_report: UpgradeReportDictMode
    usb_device: UsbDeviceDictMode
    usb_log: UsbLog
    vmlicense: VmlicenseDictMode
    acme_certificate_status: AcmeCertificateStatusDictMode
    acquired_dns: AcquiredDnsDictMode
    available_certificates: AvailableCertificatesDictMode
    check_port_availability: CheckPortAvailabilityDictMode
    current_admins: CurrentAdminsDictMode
    global_resources: GlobalResourcesDictMode
    global_search: GlobalSearchDictMode
    ha_backup_hb_used: HaBackupHbUsedDictMode
    ha_checksums: HaChecksumsDictMode
    ha_history: HaHistoryDictMode
    ha_hw_interface: HaHwInterfaceDictMode
    ha_nonsync_checksums: HaNonsyncChecksumsDictMode
    ha_statistics: HaStatisticsDictMode
    ha_table_checksums: HaTableChecksumsDictMode
    interface_connected_admins_info: InterfaceConnectedAdminsInfoDictMode
    ipconf: IpconfDictMode
    link_monitor: LinkMonitorDictMode
    modem3g: Modem3gDictMode
    monitor_sensor: MonitorSensorDictMode
    resolve_fqdn: ResolveFqdnDictMode
    running_processes: RunningProcessesDictMode
    sensor_info: SensorInfoDictMode
    status: StatusDictMode
    storage: StorageDictMode
    timezone: TimezoneDictMode
    trusted_cert_authorities: TrustedCertAuthoritiesDictMode
    vdom_link: VdomLinkDictMode
    vdom_resource: VdomResourceDictMode
    vm_information: VmInformationDictMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize system category with HTTP client."""
        ...


class SystemObjectMode:
    """SYSTEM API category for object response mode.
    
    This class is returned when the client is instantiated with response_mode="object".
    All endpoints return FortiObject responses by default.
    """
    
    admin: AdminObjectMode
    api_user: ApiUserObjectMode
    automation_action: AutomationActionObjectMode
    automation_stitch: AutomationStitchObjectMode
    available_interfaces: AvailableInterfaces
    botnet: Botnet
    botnet_domains: BotnetDomains
    central_management: CentralManagementObjectMode
    certificate: CertificateObjectMode
    change_password: ChangePasswordObjectMode
    cluster: ClusterObjectMode
    com_log: ComLogObjectMode
    config: ConfigObjectMode
    config_error_log: ConfigErrorLogObjectMode
    config_revision: ConfigRevision
    config_script: ConfigScript
    config_sync: ConfigSyncObjectMode
    crash_log: CrashLogObjectMode
    csf: Csf
    debug: DebugObjectMode
    dhcp: Dhcp
    dhcp6: Dhcp6ObjectMode
    disconnect_admins: DisconnectAdminsObjectMode
    external_resource: ExternalResourceObjectMode
    firmware: Firmware
    fortiguard: FortiguardObjectMode
    fortimanager: FortimanagerObjectMode
    fsck: FsckObjectMode
    ha_peer: HaPeer
    hscalefw_license: HscalefwLicenseObjectMode
    interface: Interface
    ipam: IpamObjectMode
    logdisk: LogdiskObjectMode
    lte_modem: LteModemObjectMode
    modem: Modem
    modem5g: Modem5gObjectMode
    ntp: NtpObjectMode
    object: ObjectObjectMode
    os: OsObjectMode
    password_policy_conform: PasswordPolicyConformObjectMode
    performance: PerformanceObjectMode
    private_data_encryption: PrivateDataEncryptionObjectMode
    process: ProcessObjectMode
    resource: ResourceObjectMode
    sandbox: SandboxObjectMode
    sdn_connector: SdnConnectorObjectMode
    time: Time
    traffic_history: TrafficHistoryObjectMode
    upgrade_report: UpgradeReportObjectMode
    usb_device: UsbDeviceObjectMode
    usb_log: UsbLog
    vmlicense: VmlicenseObjectMode
    acme_certificate_status: AcmeCertificateStatusObjectMode
    acquired_dns: AcquiredDnsObjectMode
    available_certificates: AvailableCertificatesObjectMode
    check_port_availability: CheckPortAvailabilityObjectMode
    current_admins: CurrentAdminsObjectMode
    global_resources: GlobalResourcesObjectMode
    global_search: GlobalSearchObjectMode
    ha_backup_hb_used: HaBackupHbUsedObjectMode
    ha_checksums: HaChecksumsObjectMode
    ha_history: HaHistoryObjectMode
    ha_hw_interface: HaHwInterfaceObjectMode
    ha_nonsync_checksums: HaNonsyncChecksumsObjectMode
    ha_statistics: HaStatisticsObjectMode
    ha_table_checksums: HaTableChecksumsObjectMode
    interface_connected_admins_info: InterfaceConnectedAdminsInfoObjectMode
    ipconf: IpconfObjectMode
    link_monitor: LinkMonitorObjectMode
    modem3g: Modem3gObjectMode
    monitor_sensor: MonitorSensorObjectMode
    resolve_fqdn: ResolveFqdnObjectMode
    running_processes: RunningProcessesObjectMode
    sensor_info: SensorInfoObjectMode
    status: StatusObjectMode
    storage: StorageObjectMode
    timezone: TimezoneObjectMode
    trusted_cert_authorities: TrustedCertAuthoritiesObjectMode
    vdom_link: VdomLinkObjectMode
    vdom_resource: VdomResourceObjectMode
    vm_information: VmInformationObjectMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize system category with HTTP client."""
        ...


# Base class for backwards compatibility
class System:
    """SYSTEM API category."""
    
    admin: Admin
    api_user: ApiUser
    automation_action: AutomationAction
    automation_stitch: AutomationStitch
    available_interfaces: AvailableInterfaces
    botnet: Botnet
    botnet_domains: BotnetDomains
    central_management: CentralManagement
    certificate: Certificate
    change_password: ChangePassword
    cluster: Cluster
    com_log: ComLog
    config: Config
    config_error_log: ConfigErrorLog
    config_revision: ConfigRevision
    config_script: ConfigScript
    config_sync: ConfigSync
    crash_log: CrashLog
    csf: Csf
    debug: Debug
    dhcp: Dhcp
    dhcp6: Dhcp6
    disconnect_admins: DisconnectAdmins
    external_resource: ExternalResource
    firmware: Firmware
    fortiguard: Fortiguard
    fortimanager: Fortimanager
    fsck: Fsck
    ha_peer: HaPeer
    hscalefw_license: HscalefwLicense
    interface: Interface
    ipam: Ipam
    logdisk: Logdisk
    lte_modem: LteModem
    modem: Modem
    modem5g: Modem5g
    ntp: Ntp
    object: Object
    os: Os
    password_policy_conform: PasswordPolicyConform
    performance: Performance
    private_data_encryption: PrivateDataEncryption
    process: Process
    resource: Resource
    sandbox: Sandbox
    sdn_connector: SdnConnector
    time: Time
    traffic_history: TrafficHistory
    upgrade_report: UpgradeReport
    usb_device: UsbDevice
    usb_log: UsbLog
    vmlicense: Vmlicense
    acme_certificate_status: AcmeCertificateStatus
    acquired_dns: AcquiredDns
    available_certificates: AvailableCertificates
    check_port_availability: CheckPortAvailability
    current_admins: CurrentAdmins
    global_resources: GlobalResources
    global_search: GlobalSearch
    ha_backup_hb_used: HaBackupHbUsed
    ha_checksums: HaChecksums
    ha_history: HaHistory
    ha_hw_interface: HaHwInterface
    ha_nonsync_checksums: HaNonsyncChecksums
    ha_statistics: HaStatistics
    ha_table_checksums: HaTableChecksums
    interface_connected_admins_info: InterfaceConnectedAdminsInfo
    ipconf: Ipconf
    link_monitor: LinkMonitor
    modem3g: Modem3g
    monitor_sensor: MonitorSensor
    resolve_fqdn: ResolveFqdn
    running_processes: RunningProcesses
    sensor_info: SensorInfo
    status: Status
    storage: Storage
    timezone: Timezone
    trusted_cert_authorities: TrustedCertAuthorities
    vdom_link: VdomLink
    vdom_resource: VdomResource
    vm_information: VmInformation

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize system category with HTTP client."""
        ...
