"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .acquired_dns import AcquiredDns
from .available_certificates import AvailableCertificates
from .available_interfaces import AvailableInterfaces
from .available_interfaces_base import AvailableInterfaces
from .botnet import Botnet
from .botnet_base import Botnet
from .botnet_domains import BotnetDomains
from .botnet_domains_base import BotnetDomains
from .config_revision import ConfigRevision
from .config_revision_base import ConfigRevision
from .config_script import ConfigScript
from .config_script_base import ConfigScript
from .csf import Csf
from .csf_base import Csf
from .current_admins import CurrentAdmins
from .dhcp import Dhcp
from .dhcp_base import Dhcp
from .firmware import Firmware
from .firmware_base import Firmware
from .global_resources import GlobalResources
from .ha_checksums import HaChecksums
from .ha_history import HaHistory
from .ha_nonsync_checksums import HaNonsyncChecksums
from .ha_peer import HaPeer
from .ha_peer_base import HaPeer
from .ha_statistics import HaStatistics
from .interface import Interface
from .interface_base import Interface
from .link_monitor import LinkMonitor
from .running_processes import RunningProcesses
from .status import Status
from .storage import Storage
from .time import Time
from .time_base import Time
from .timezone import Timezone
from .trusted_cert_authorities import TrustedCertAuthorities
from .usb_log import UsbLog
from .usb_log_base import UsbLog
from .vdom_link import VdomLink
from .vdom_resource import VdomResource
from .vm_information import VmInformation

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class System:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.acquired_dns = AcquiredDns(client)
        self.available_certificates = AvailableCertificates(client)
        self.available_interfaces = AvailableInterfaces(client)
        self.available_interfaces = AvailableInterfaces(client)
        self.botnet = Botnet(client)
        self.botnet = Botnet(client)
        self.botnet_domains = BotnetDomains(client)
        self.botnet_domains = BotnetDomains(client)
        self.config_revision = ConfigRevision(client)
        self.config_revision = ConfigRevision(client)
        self.config_script = ConfigScript(client)
        self.config_script = ConfigScript(client)
        self.csf = Csf(client)
        self.csf = Csf(client)
        self.current_admins = CurrentAdmins(client)
        self.dhcp = Dhcp(client)
        self.dhcp = Dhcp(client)
        self.firmware = Firmware(client)
        self.firmware = Firmware(client)
        self.global_resources = GlobalResources(client)
        self.ha_checksums = HaChecksums(client)
        self.ha_history = HaHistory(client)
        self.ha_nonsync_checksums = HaNonsyncChecksums(client)
        self.ha_peer = HaPeer(client)
        self.ha_peer = HaPeer(client)
        self.ha_statistics = HaStatistics(client)
        self.interface = Interface(client)
        self.interface = Interface(client)
        self.link_monitor = LinkMonitor(client)
        self.running_processes = RunningProcesses(client)
        self.status = Status(client)
        self.storage = Storage(client)
        self.time = Time(client)
        self.time = Time(client)
        self.timezone = Timezone(client)
        self.trusted_cert_authorities = TrustedCertAuthorities(client)
        self.usb_log = UsbLog(client)
        self.usb_log = UsbLog(client)
        self.vdom_link = VdomLink(client)
        self.vdom_resource = VdomResource(client)
        self.vm_information = VmInformation(client)
