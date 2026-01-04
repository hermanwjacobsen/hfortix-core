"""Type stubs for SYSTEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import acme_certificate_status
    from . import acquired_dns
    from . import admin
    from . import api_user
    from . import automation_action
    from . import automation_stitch
    from . import available_certificates
    from . import available_interfaces
    from . import botnet
    from . import botnet_domains
    from . import central_management
    from . import certificate
    from . import change_password
    from . import check_port_availability
    from . import cluster
    from . import com_log
    from . import config
    from . import config_error_log
    from . import config_revision
    from . import config_script
    from . import config_sync
    from . import crash_log
    from . import csf
    from . import current_admins
    from . import debug
    from . import dhcp
    from . import dhcp6
    from . import disconnect_admins
    from . import external_resource
    from . import firmware
    from . import fortiguard
    from . import fortimanager
    from . import fsck
    from . import global_resources
    from . import global_search
    from . import ha_backup_hb_used
    from . import ha_checksums
    from . import ha_history
    from . import ha_hw_interface
    from . import ha_nonsync_checksums
    from . import ha_peer
    from . import ha_statistics
    from . import ha_table_checksums
    from . import hscalefw_license
    from . import interface
    from . import interface_connected_admins_info
    from . import ipam
    from . import ipconf
    from . import link_monitor
    from . import logdisk
    from . import lte_modem
    from . import modem
    from . import monitor_sensor
    from . import ntp
    from . import object
    from . import os
    from . import password_policy_conform
    from . import performance
    from . import private_data_encryption
    from . import process
    from . import resolve_fqdn
    from . import resource
    from . import running_processes
    from . import sandbox
    from . import sdn_connector
    from . import sensor_info
    from . import status
    from . import storage
    from . import time
    from . import timezone
    from . import traffic_history
    from . import trusted_cert_authorities
    from . import upgrade_report
    from . import usb_device
    from . import usb_log
    from . import vdom_link
    from . import vdom_resource
    from . import vm_information
    from . import vmlicense
    from . import x3g_modem
    from . import x5g_modem


class System:
    """Type stub for System."""

    admin: admin.Admin
    api_user: api_user.ApiUser
    automation_stitch: automation_stitch.AutomationStitch
    certificate: certificate.Certificate
    change_password: change_password.ChangePassword
    cluster: cluster.Cluster
    com_log: com_log.ComLog
    config: config.Config
    config_error_log: config_error_log.ConfigErrorLog
    config_revision: config_revision.ConfigRevision
    config_script: config_script.ConfigScript
    config_sync: config_sync.ConfigSync
    crash_log: crash_log.CrashLog
    csf: csf.Csf
    debug: debug.Debug
    dhcp: dhcp.Dhcp
    dhcp6: dhcp6.Dhcp6
    disconnect_admins: disconnect_admins.DisconnectAdmins
    external_resource: external_resource.ExternalResource
    firmware: firmware.Firmware
    fortiguard: fortiguard.Fortiguard
    fortimanager: fortimanager.Fortimanager
    fsck: fsck.Fsck
    ha_peer: ha_peer.HaPeer
    hscalefw_license: hscalefw_license.HscalefwLicense
    interface: interface.Interface
    ipam: ipam.Ipam
    logdisk: logdisk.Logdisk
    lte_modem: lte_modem.LteModem
    modem: modem.Modem
    object: object.Object
    os: os.Os
    password_policy_conform: password_policy_conform.PasswordPolicyConform
    private_data_encryption: private_data_encryption.PrivateDataEncryption
    process: process.Process
    sdn_connector: sdn_connector.SdnConnector
    time: time.Time
    traffic_history: traffic_history.TrafficHistory
    upgrade_report: upgrade_report.UpgradeReport
    usb_device: usb_device.UsbDevice
    usb_log: usb_log.UsbLog
    vmlicense: vmlicense.Vmlicense
    x5g_modem: x5g_modem.X5gModem
    acme_certificate_status: acme_certificate_status.AcmeCertificateStatus
    acquired_dns: acquired_dns.AcquiredDns
    automation_action: automation_action.AutomationAction
    available_certificates: available_certificates.AvailableCertificates
    available_interfaces: available_interfaces.AvailableInterfaces
    botnet: botnet.Botnet
    botnet_domains: botnet_domains.BotnetDomains
    central_management: central_management.CentralManagement
    check_port_availability: check_port_availability.CheckPortAvailability
    current_admins: current_admins.CurrentAdmins
    global_resources: global_resources.GlobalResources
    global_search: global_search.GlobalSearch
    ha_backup_hb_used: ha_backup_hb_used.HaBackupHbUsed
    ha_checksums: ha_checksums.HaChecksums
    ha_history: ha_history.HaHistory
    ha_hw_interface: ha_hw_interface.HaHwInterface
    ha_nonsync_checksums: ha_nonsync_checksums.HaNonsyncChecksums
    ha_statistics: ha_statistics.HaStatistics
    ha_table_checksums: ha_table_checksums.HaTableChecksums
    interface_connected_admins_info: interface_connected_admins_info.InterfaceConnectedAdminsInfo
    ipconf: ipconf.Ipconf
    link_monitor: link_monitor.LinkMonitor
    monitor_sensor: monitor_sensor.MonitorSensor
    ntp: ntp.Ntp
    performance: performance.Performance
    resolve_fqdn: resolve_fqdn.ResolveFqdn
    resource: resource.Resource
    running_processes: running_processes.RunningProcesses
    sandbox: sandbox.Sandbox
    sensor_info: sensor_info.SensorInfo
    status: status.Status
    storage: storage.Storage
    timezone: timezone.Timezone
    trusted_cert_authorities: trusted_cert_authorities.TrustedCertAuthorities
    vdom_link: vdom_link.VdomLink
    vdom_resource: vdom_resource.VdomResource
    vm_information: vm_information.VmInformation
    x3g_modem: x3g_modem.X3gModem

    def __init__(self, client: IHTTPClient) -> None: ...
