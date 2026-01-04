"""FortiOS CMDB - Log category"""

from .custom_field import CustomField
from .disk_filter import DiskFilter
from .disk_setting import DiskSetting
from .eventfilter import Eventfilter
from .fortianalyzer2_filter import Fortianalyzer2Filter
from .fortianalyzer2_override_filter import Fortianalyzer2OverrideFilter
from .fortianalyzer2_override_setting import Fortianalyzer2OverrideSetting
from .fortianalyzer2_setting import Fortianalyzer2Setting
from .fortianalyzer3_filter import Fortianalyzer3Filter
from .fortianalyzer3_override_filter import Fortianalyzer3OverrideFilter
from .fortianalyzer3_override_setting import Fortianalyzer3OverrideSetting
from .fortianalyzer3_setting import Fortianalyzer3Setting
from .fortianalyzer_cloud_filter import FortianalyzerCloudFilter
from .fortianalyzer_cloud_override_filter import FortianalyzerCloudOverrideFilter
from .fortianalyzer_cloud_override_setting import FortianalyzerCloudOverrideSetting
from .fortianalyzer_cloud_setting import FortianalyzerCloudSetting
from .fortianalyzer_filter import FortianalyzerFilter
from .fortianalyzer_override_filter import FortianalyzerOverrideFilter
from .fortianalyzer_override_setting import FortianalyzerOverrideSetting
from .fortianalyzer_setting import FortianalyzerSetting
from .fortiguard_filter import FortiguardFilter
from .fortiguard_override_filter import FortiguardOverrideFilter
from .fortiguard_override_setting import FortiguardOverrideSetting
from .fortiguard_setting import FortiguardSetting
from .gui_display import GuiDisplay
from .memory_filter import MemoryFilter
from .memory_global_setting import MemoryGlobalSetting
from .memory_setting import MemorySetting
from .null_device_filter import NullDeviceFilter
from .null_device_setting import NullDeviceSetting
from .setting import Setting
from .syslogd2_filter import Syslogd2Filter
from .syslogd2_override_filter import Syslogd2OverrideFilter
from .syslogd2_override_setting import Syslogd2OverrideSetting
from .syslogd2_setting import Syslogd2Setting
from .syslogd3_filter import Syslogd3Filter
from .syslogd3_override_filter import Syslogd3OverrideFilter
from .syslogd3_override_setting import Syslogd3OverrideSetting
from .syslogd3_setting import Syslogd3Setting
from .syslogd4_filter import Syslogd4Filter
from .syslogd4_override_filter import Syslogd4OverrideFilter
from .syslogd4_override_setting import Syslogd4OverrideSetting
from .syslogd4_setting import Syslogd4Setting
from .syslogd_filter import SyslogdFilter
from .syslogd_override_filter import SyslogdOverrideFilter
from .syslogd_override_setting import SyslogdOverrideSetting
from .syslogd_setting import SyslogdSetting
from .tacacs_plusaccounting2_filter import TacacsPlusaccounting2Filter
from .tacacs_plusaccounting2_setting import TacacsPlusaccounting2Setting
from .tacacs_plusaccounting3_filter import TacacsPlusaccounting3Filter
from .tacacs_plusaccounting3_setting import TacacsPlusaccounting3Setting
from .tacacs_plusaccounting_filter import TacacsPlusaccountingFilter
from .tacacs_plusaccounting_setting import TacacsPlusaccountingSetting
from .threat_weight import ThreatWeight
from .webtrends_filter import WebtrendsFilter
from .webtrends_setting import WebtrendsSetting

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
    "Log",
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


class Log:
    """Log endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Log endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.custom_field = CustomField(client)
        self.disk_filter = DiskFilter(client)
        self.disk_setting = DiskSetting(client)
        self.eventfilter = Eventfilter(client)
        self.fortianalyzer2_filter = Fortianalyzer2Filter(client)
        self.fortianalyzer2_override_filter = Fortianalyzer2OverrideFilter(client)
        self.fortianalyzer2_override_setting = Fortianalyzer2OverrideSetting(client)
        self.fortianalyzer2_setting = Fortianalyzer2Setting(client)
        self.fortianalyzer3_filter = Fortianalyzer3Filter(client)
        self.fortianalyzer3_override_filter = Fortianalyzer3OverrideFilter(client)
        self.fortianalyzer3_override_setting = Fortianalyzer3OverrideSetting(client)
        self.fortianalyzer3_setting = Fortianalyzer3Setting(client)
        self.fortianalyzer_cloud_filter = FortianalyzerCloudFilter(client)
        self.fortianalyzer_cloud_override_filter = FortianalyzerCloudOverrideFilter(client)
        self.fortianalyzer_cloud_override_setting = FortianalyzerCloudOverrideSetting(client)
        self.fortianalyzer_cloud_setting = FortianalyzerCloudSetting(client)
        self.fortianalyzer_filter = FortianalyzerFilter(client)
        self.fortianalyzer_override_filter = FortianalyzerOverrideFilter(client)
        self.fortianalyzer_override_setting = FortianalyzerOverrideSetting(client)
        self.fortianalyzer_setting = FortianalyzerSetting(client)
        self.fortiguard_filter = FortiguardFilter(client)
        self.fortiguard_override_filter = FortiguardOverrideFilter(client)
        self.fortiguard_override_setting = FortiguardOverrideSetting(client)
        self.fortiguard_setting = FortiguardSetting(client)
        self.gui_display = GuiDisplay(client)
        self.memory_filter = MemoryFilter(client)
        self.memory_global_setting = MemoryGlobalSetting(client)
        self.memory_setting = MemorySetting(client)
        self.null_device_filter = NullDeviceFilter(client)
        self.null_device_setting = NullDeviceSetting(client)
        self.setting = Setting(client)
        self.syslogd2_filter = Syslogd2Filter(client)
        self.syslogd2_override_filter = Syslogd2OverrideFilter(client)
        self.syslogd2_override_setting = Syslogd2OverrideSetting(client)
        self.syslogd2_setting = Syslogd2Setting(client)
        self.syslogd3_filter = Syslogd3Filter(client)
        self.syslogd3_override_filter = Syslogd3OverrideFilter(client)
        self.syslogd3_override_setting = Syslogd3OverrideSetting(client)
        self.syslogd3_setting = Syslogd3Setting(client)
        self.syslogd4_filter = Syslogd4Filter(client)
        self.syslogd4_override_filter = Syslogd4OverrideFilter(client)
        self.syslogd4_override_setting = Syslogd4OverrideSetting(client)
        self.syslogd4_setting = Syslogd4Setting(client)
        self.syslogd_filter = SyslogdFilter(client)
        self.syslogd_override_filter = SyslogdOverrideFilter(client)
        self.syslogd_override_setting = SyslogdOverrideSetting(client)
        self.syslogd_setting = SyslogdSetting(client)
        self.tacacs_plusaccounting2_filter = TacacsPlusaccounting2Filter(client)
        self.tacacs_plusaccounting2_setting = TacacsPlusaccounting2Setting(client)
        self.tacacs_plusaccounting3_filter = TacacsPlusaccounting3Filter(client)
        self.tacacs_plusaccounting3_setting = TacacsPlusaccounting3Setting(client)
        self.tacacs_plusaccounting_filter = TacacsPlusaccountingFilter(client)
        self.tacacs_plusaccounting_setting = TacacsPlusaccountingSetting(client)
        self.threat_weight = ThreatWeight(client)
        self.webtrends_filter = WebtrendsFilter(client)
        self.webtrends_setting = WebtrendsSetting(client)
