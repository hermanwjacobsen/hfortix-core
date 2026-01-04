"""Type stubs for LOG category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import custom_field
    from . import disk
    from . import eventfilter
    from . import fortianalyzer
    from . import fortianalyzer2
    from . import fortianalyzer3
    from . import fortianalyzer_cloud
    from . import fortiguard
    from . import gui_display
    from . import memory
    from . import null_device
    from . import setting
    from . import syslogd
    from . import syslogd2
    from . import syslogd3
    from . import syslogd4
    from . import tacacs_plus_accounting
    from . import tacacs_plus_accounting2
    from . import tacacs_plus_accounting3
    from . import threat_weight
    from . import webtrends


class Log:
    """Type stub for Log."""

    disk: disk.Disk
    fortianalyzer: fortianalyzer.Fortianalyzer
    fortianalyzer2: fortianalyzer2.Fortianalyzer2
    fortianalyzer3: fortianalyzer3.Fortianalyzer3
    fortianalyzer_cloud: fortianalyzer_cloud.FortianalyzerCloud
    fortiguard: fortiguard.Fortiguard
    memory: memory.Memory
    null_device: null_device.NullDevice
    syslogd: syslogd.Syslogd
    syslogd2: syslogd2.Syslogd2
    syslogd3: syslogd3.Syslogd3
    syslogd4: syslogd4.Syslogd4
    tacacs_plus_accounting: tacacs_plus_accounting.TacacsPlusAccounting
    tacacs_plus_accounting2: tacacs_plus_accounting2.TacacsPlusAccounting2
    tacacs_plus_accounting3: tacacs_plus_accounting3.TacacsPlusAccounting3
    webtrends: webtrends.Webtrends
    custom_field: custom_field.CustomField
    eventfilter: eventfilter.Eventfilter
    gui_display: gui_display.GuiDisplay
    setting: setting.Setting
    threat_weight: threat_weight.ThreatWeight

    def __init__(self, client: IHTTPClient) -> None: ...
