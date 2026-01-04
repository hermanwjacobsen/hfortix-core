"""Type stubs for SWITCH_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import detected_device
    from . import fsw_firmware
    from . import isl_lockdown
    from . import known_nac_device_criteria_list
    from . import managed_switch
    from . import matched_devices
    from . import mclag_icl
    from . import nac_device
    from . import recommendation


class SwitchController:
    """Type stub for SwitchController."""

    fsw_firmware: fsw_firmware.FswFirmware
    isl_lockdown: isl_lockdown.IslLockdown
    managed_switch: managed_switch.ManagedSwitch
    mclag_icl: mclag_icl.MclagIcl
    recommendation: recommendation.Recommendation
    detected_device: detected_device.DetectedDevice
    known_nac_device_criteria_list: known_nac_device_criteria_list.KnownNacDeviceCriteriaList
    matched_devices: matched_devices.MatchedDevices
    nac_device: nac_device.NacDevice

    def __init__(self, client: IHTTPClient) -> None: ...
