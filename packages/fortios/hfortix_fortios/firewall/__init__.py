"""Firewall convenience wrappers for FortiOS API."""

from .firewallPolicy import FirewallPolicy
from .ipmacBindingSetting import IPMACBindingSetting
from .ipmacBindingTable import IPMACBindingTable
from .scheduleGroup import ScheduleGroup
from .scheduleOnetime import ScheduleOnetime
from .scheduleRecurring import ScheduleRecurring
from .serviceCategory import ServiceCategory
from .serviceCustom import ServiceCustom
from .serviceGroup import ServiceGroup
from .shaperPerIp import ShaperPerIp
from .sshHostKey import SSHHostKey
from .sshLocalCa import SSHLocalCA
from .sshLocalKey import SSHLocalKey
from .sshSetting import SSHSetting
from .sslSetting import SSLSetting
from .trafficShaper import TrafficShaper
from .wildcardFqdnCustom import WildcardFqdnCustom
from .wildcardFqdnGroup import WildcardFqdnGroup

__all__ = [
    "FirewallPolicy",
    "IPMACBindingSetting",
    "IPMACBindingTable",
    "ScheduleGroup",
    "ScheduleOnetime",
    "ScheduleRecurring",
    "ServiceCategory",
    "ServiceCustom",
    "ServiceGroup",
    "ShaperPerIp",
    "SSHHostKey",
    "SSHLocalCA",
    "SSHLocalKey",
    "SSHSetting",
    "SSLSetting",
    "TrafficShaper",
    "WildcardFqdnCustom",
    "WildcardFqdnGroup",
]
