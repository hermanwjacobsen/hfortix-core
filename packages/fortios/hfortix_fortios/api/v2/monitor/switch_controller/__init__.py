"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .detected_device import DetectedDevice
from .fsw_firmware import FswFirmware
from .fsw_firmware_base import FswFirmware
from .known_nac_device_criteria_list import KnownNacDeviceCriteriaList
from .matched_devices import MatchedDevices

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class SwitchController:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.detected_device = DetectedDevice(client)
        self.fsw_firmware = FswFirmware(client)
        self.fsw_firmware = FswFirmware(client)
        self.known_nac_device_criteria_list = KnownNacDeviceCriteriaList(client)
        self.matched_devices = MatchedDevices(client)
