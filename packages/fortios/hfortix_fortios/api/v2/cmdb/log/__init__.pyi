"""Type stubs for LOG category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .custom_field import CustomField, CustomFieldDictMode, CustomFieldObjectMode
    from .eventfilter import Eventfilter, EventfilterDictMode, EventfilterObjectMode
    from .gui_display import GuiDisplay, GuiDisplayDictMode, GuiDisplayObjectMode
    from .setting import Setting, SettingDictMode, SettingObjectMode
    from .threat_weight import ThreatWeight, ThreatWeightDictMode, ThreatWeightObjectMode
    from .disk import Disk, DiskDictMode, DiskObjectMode
    from .fortianalyzer import Fortianalyzer, FortianalyzerDictMode, FortianalyzerObjectMode
    from .fortianalyzer2 import Fortianalyzer2, Fortianalyzer2DictMode, Fortianalyzer2ObjectMode
    from .fortianalyzer3 import Fortianalyzer3, Fortianalyzer3DictMode, Fortianalyzer3ObjectMode
    from .fortianalyzer_cloud import FortianalyzerCloud, FortianalyzerCloudDictMode, FortianalyzerCloudObjectMode
    from .fortiguard import Fortiguard, FortiguardDictMode, FortiguardObjectMode
    from .memory import Memory, MemoryDictMode, MemoryObjectMode
    from .null_device import NullDevice, NullDeviceDictMode, NullDeviceObjectMode
    from .syslogd import Syslogd, SyslogdDictMode, SyslogdObjectMode
    from .syslogd2 import Syslogd2, Syslogd2DictMode, Syslogd2ObjectMode
    from .syslogd3 import Syslogd3, Syslogd3DictMode, Syslogd3ObjectMode
    from .syslogd4 import Syslogd4, Syslogd4DictMode, Syslogd4ObjectMode
    from .tacacs_plusaccounting import TacacsPlusaccounting, TacacsPlusaccountingDictMode, TacacsPlusaccountingObjectMode
    from .tacacs_plusaccounting2 import TacacsPlusaccounting2, TacacsPlusaccounting2DictMode, TacacsPlusaccounting2ObjectMode
    from .tacacs_plusaccounting3 import TacacsPlusaccounting3, TacacsPlusaccounting3DictMode, TacacsPlusaccounting3ObjectMode
    from .webtrends import Webtrends, WebtrendsDictMode, WebtrendsObjectMode

__all__ = [
    "CustomField",
    "Eventfilter",
    "GuiDisplay",
    "Setting",
    "ThreatWeight",
    "LogDictMode",
    "LogObjectMode",
]

class LogDictMode:
    """LOG API category for dict response mode.
    
    This class is returned when the client is instantiated with response_mode="dict" (default).
    All endpoints return dict/TypedDict responses by default.
    """
    
    disk: DiskDictMode
    fortianalyzer: FortianalyzerDictMode
    fortianalyzer2: Fortianalyzer2DictMode
    fortianalyzer3: Fortianalyzer3DictMode
    fortianalyzer_cloud: FortianalyzerCloudDictMode
    fortiguard: FortiguardDictMode
    memory: MemoryDictMode
    null_device: NullDeviceDictMode
    syslogd: SyslogdDictMode
    syslogd2: Syslogd2DictMode
    syslogd3: Syslogd3DictMode
    syslogd4: Syslogd4DictMode
    tacacs_plusaccounting: TacacsPlusaccountingDictMode
    tacacs_plusaccounting2: TacacsPlusaccounting2DictMode
    tacacs_plusaccounting3: TacacsPlusaccounting3DictMode
    webtrends: WebtrendsDictMode
    custom_field: CustomFieldDictMode
    eventfilter: EventfilterDictMode
    gui_display: GuiDisplayDictMode
    setting: SettingDictMode
    threat_weight: ThreatWeightDictMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize log category with HTTP client."""
        ...


class LogObjectMode:
    """LOG API category for object response mode.
    
    This class is returned when the client is instantiated with response_mode="object".
    All endpoints return FortiObject responses by default.
    """
    
    disk: DiskObjectMode
    fortianalyzer: FortianalyzerObjectMode
    fortianalyzer2: Fortianalyzer2ObjectMode
    fortianalyzer3: Fortianalyzer3ObjectMode
    fortianalyzer_cloud: FortianalyzerCloudObjectMode
    fortiguard: FortiguardObjectMode
    memory: MemoryObjectMode
    null_device: NullDeviceObjectMode
    syslogd: SyslogdObjectMode
    syslogd2: Syslogd2ObjectMode
    syslogd3: Syslogd3ObjectMode
    syslogd4: Syslogd4ObjectMode
    tacacs_plusaccounting: TacacsPlusaccountingObjectMode
    tacacs_plusaccounting2: TacacsPlusaccounting2ObjectMode
    tacacs_plusaccounting3: TacacsPlusaccounting3ObjectMode
    webtrends: WebtrendsObjectMode
    custom_field: CustomFieldObjectMode
    eventfilter: EventfilterObjectMode
    gui_display: GuiDisplayObjectMode
    setting: SettingObjectMode
    threat_weight: ThreatWeightObjectMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize log category with HTTP client."""
        ...


# Base class for backwards compatibility
class Log:
    """LOG API category."""
    
    disk: Disk
    fortianalyzer: Fortianalyzer
    fortianalyzer2: Fortianalyzer2
    fortianalyzer3: Fortianalyzer3
    fortianalyzer_cloud: FortianalyzerCloud
    fortiguard: Fortiguard
    memory: Memory
    null_device: NullDevice
    syslogd: Syslogd
    syslogd2: Syslogd2
    syslogd3: Syslogd3
    syslogd4: Syslogd4
    tacacs_plusaccounting: TacacsPlusaccounting
    tacacs_plusaccounting2: TacacsPlusaccounting2
    tacacs_plusaccounting3: TacacsPlusaccounting3
    webtrends: Webtrends
    custom_field: CustomField
    eventfilter: Eventfilter
    gui_display: GuiDisplay
    setting: Setting
    threat_weight: ThreatWeight

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize log category with HTTP client."""
        ...
