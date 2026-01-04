"""Type stubs for WIRELESS_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import access_control_list
    from . import ap_status
    from . import apcfg_profile
    from . import arrp_profile
    from . import ble_profile
    from . import bonjour_profile
    from . import global_setting
    from . import hotspot20
    from . import inter_controller
    from . import log
    from . import lw_profile
    from . import mpsk_profile
    from . import nac_profile
    from . import qos_profile
    from . import region
    from . import setting
    from . import snmp
    from . import ssid_policy
    from . import syslog_profile
    from . import timers
    from . import utm_profile
    from . import vap
    from . import vap_group
    from . import wag_profile
    from . import wids_profile
    from . import wtp
    from . import wtp_group
    from . import wtp_profile


class WirelessController:
    """Type stub for WirelessController."""

    hotspot20: hotspot20.Hotspot20
    access_control_list: access_control_list.AccessControlList
    ap_status: ap_status.ApStatus
    apcfg_profile: apcfg_profile.ApcfgProfile
    arrp_profile: arrp_profile.ArrpProfile
    ble_profile: ble_profile.BleProfile
    bonjour_profile: bonjour_profile.BonjourProfile
    global_setting: global_setting.GlobalSetting
    inter_controller: inter_controller.InterController
    log: log.Log
    lw_profile: lw_profile.LwProfile
    mpsk_profile: mpsk_profile.MpskProfile
    nac_profile: nac_profile.NacProfile
    qos_profile: qos_profile.QosProfile
    region: region.Region
    setting: setting.Setting
    snmp: snmp.Snmp
    ssid_policy: ssid_policy.SsidPolicy
    syslog_profile: syslog_profile.SyslogProfile
    timers: timers.Timers
    utm_profile: utm_profile.UtmProfile
    vap: vap.Vap
    vap_group: vap_group.VapGroup
    wag_profile: wag_profile.WagProfile
    wids_profile: wids_profile.WidsProfile
    wtp: wtp.Wtp
    wtp_group: wtp_group.WtpGroup
    wtp_profile: wtp_profile.WtpProfile

    def __init__(self, client: IHTTPClient) -> None: ...
