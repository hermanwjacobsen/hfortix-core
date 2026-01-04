"""
Type stubs for log category.

This file provides type hints for IDE autocomplete and type checking.

Auto-generated - do not edit manually.
Last generated: 2026-01-03T20:33:52.975834+00:00
"""

# Import all endpoint classes
from .custom_field import CustomField as CustomField
from .disk_filter import DiskFilter as DiskFilter
from .disk_setting import DiskSetting as DiskSetting
from .eventfilter import Eventfilter as Eventfilter
from .fortianalyzer2_filter import Fortianalyzer2Filter as Fortianalyzer2Filter
from .fortianalyzer2_override_filter import Fortianalyzer2OverrideFilter as Fortianalyzer2OverrideFilter
from .fortianalyzer2_override_setting import Fortianalyzer2OverrideSetting as Fortianalyzer2OverrideSetting
from .fortianalyzer2_setting import Fortianalyzer2Setting as Fortianalyzer2Setting
from .fortianalyzer3_filter import Fortianalyzer3Filter as Fortianalyzer3Filter
from .fortianalyzer3_override_filter import Fortianalyzer3OverrideFilter as Fortianalyzer3OverrideFilter
from .fortianalyzer3_override_setting import Fortianalyzer3OverrideSetting as Fortianalyzer3OverrideSetting
from .fortianalyzer3_setting import Fortianalyzer3Setting as Fortianalyzer3Setting
from .fortianalyzer_cloud_filter import FortianalyzerCloudFilter as FortianalyzerCloudFilter
from .fortianalyzer_cloud_override_filter import FortianalyzerCloudOverrideFilter as FortianalyzerCloudOverrideFilter
from .fortianalyzer_cloud_override_setting import FortianalyzerCloudOverrideSetting as FortianalyzerCloudOverrideSetting
from .fortianalyzer_cloud_setting import FortianalyzerCloudSetting as FortianalyzerCloudSetting
from .fortianalyzer_filter import FortianalyzerFilter as FortianalyzerFilter
from .fortianalyzer_override_filter import FortianalyzerOverrideFilter as FortianalyzerOverrideFilter
from .fortianalyzer_override_setting import FortianalyzerOverrideSetting as FortianalyzerOverrideSetting
from .fortianalyzer_setting import FortianalyzerSetting as FortianalyzerSetting
from .fortiguard_filter import FortiguardFilter as FortiguardFilter
from .fortiguard_override_filter import FortiguardOverrideFilter as FortiguardOverrideFilter
from .fortiguard_override_setting import FortiguardOverrideSetting as FortiguardOverrideSetting
from .fortiguard_setting import FortiguardSetting as FortiguardSetting
from .gui_display import GuiDisplay as GuiDisplay
from .memory_filter import MemoryFilter as MemoryFilter
from .memory_global_setting import MemoryGlobalSetting as MemoryGlobalSetting
from .memory_setting import MemorySetting as MemorySetting
from .null_device_filter import NullDeviceFilter as NullDeviceFilter
from .null_device_setting import NullDeviceSetting as NullDeviceSetting
from .setting import Setting as Setting
from .syslogd2_filter import Syslogd2Filter as Syslogd2Filter
from .syslogd2_override_filter import Syslogd2OverrideFilter as Syslogd2OverrideFilter
from .syslogd2_override_setting import Syslogd2OverrideSetting as Syslogd2OverrideSetting
from .syslogd2_setting import Syslogd2Setting as Syslogd2Setting
from .syslogd3_filter import Syslogd3Filter as Syslogd3Filter
from .syslogd3_override_filter import Syslogd3OverrideFilter as Syslogd3OverrideFilter
from .syslogd3_override_setting import Syslogd3OverrideSetting as Syslogd3OverrideSetting
from .syslogd3_setting import Syslogd3Setting as Syslogd3Setting
from .syslogd4_filter import Syslogd4Filter as Syslogd4Filter
from .syslogd4_override_filter import Syslogd4OverrideFilter as Syslogd4OverrideFilter
from .syslogd4_override_setting import Syslogd4OverrideSetting as Syslogd4OverrideSetting
from .syslogd4_setting import Syslogd4Setting as Syslogd4Setting
from .syslogd_filter import SyslogdFilter as SyslogdFilter
from .syslogd_override_filter import SyslogdOverrideFilter as SyslogdOverrideFilter
from .syslogd_override_setting import SyslogdOverrideSetting as SyslogdOverrideSetting
from .syslogd_setting import SyslogdSetting as SyslogdSetting
from .tacacs_plusaccounting2_filter import TacacsPlusaccounting2Filter as TacacsPlusaccounting2Filter
from .tacacs_plusaccounting2_setting import TacacsPlusaccounting2Setting as TacacsPlusaccounting2Setting
from .tacacs_plusaccounting3_filter import TacacsPlusaccounting3Filter as TacacsPlusaccounting3Filter
from .tacacs_plusaccounting3_setting import TacacsPlusaccounting3Setting as TacacsPlusaccounting3Setting
from .tacacs_plusaccounting_filter import TacacsPlusaccountingFilter as TacacsPlusaccountingFilter
from .tacacs_plusaccounting_setting import TacacsPlusaccountingSetting as TacacsPlusaccountingSetting
from .threat_weight import ThreatWeight as ThreatWeight
from .webtrends_filter import WebtrendsFilter as WebtrendsFilter
from .webtrends_setting import WebtrendsSetting as WebtrendsSetting

__all__ = [
    "CustomField",
    "DiskFilter",
    "DiskSetting",
    "Eventfilter",
    "Fortianalyzer2Filter",
    "Fortianalyzer2OverrideFilter",
    "Fortianalyzer2OverrideSetting",
    "Fortianalyzer2Setting",
    "Fortianalyzer3Filter",
    "Fortianalyzer3OverrideFilter",
    "Fortianalyzer3OverrideSetting",
    "Fortianalyzer3Setting",
    "FortianalyzerCloudFilter",
    "FortianalyzerCloudOverrideFilter",
    "FortianalyzerCloudOverrideSetting",
    "FortianalyzerCloudSetting",
    "FortianalyzerFilter",
    "FortianalyzerOverrideFilter",
    "FortianalyzerOverrideSetting",
    "FortianalyzerSetting",
    "FortiguardFilter",
    "FortiguardOverrideFilter",
    "FortiguardOverrideSetting",
    "FortiguardSetting",
    "GuiDisplay",
    "MemoryFilter",
    "MemoryGlobalSetting",
    "MemorySetting",
    "NullDeviceFilter",
    "NullDeviceSetting",
    "Setting",
    "Syslogd2Filter",
    "Syslogd2OverrideFilter",
    "Syslogd2OverrideSetting",
    "Syslogd2Setting",
    "Syslogd3Filter",
    "Syslogd3OverrideFilter",
    "Syslogd3OverrideSetting",
    "Syslogd3Setting",
    "Syslogd4Filter",
    "Syslogd4OverrideFilter",
    "Syslogd4OverrideSetting",
    "Syslogd4Setting",
    "SyslogdFilter",
    "SyslogdOverrideFilter",
    "SyslogdOverrideSetting",
    "SyslogdSetting",
    "TacacsPlusaccounting2Filter",
    "TacacsPlusaccounting2Setting",
    "TacacsPlusaccounting3Filter",
    "TacacsPlusaccounting3Setting",
    "TacacsPlusaccountingFilter",
    "TacacsPlusaccountingSetting",
    "ThreatWeight",
    "WebtrendsFilter",
    "WebtrendsSetting",
]
