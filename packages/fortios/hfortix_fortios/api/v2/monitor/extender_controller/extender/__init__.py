"""FortiOS CMDB - Extender category"""

from .diagnose import Diagnose
from .modem_firmware import ModemFirmware
from .reset import Reset
from .upgrade import Upgrade

__all__ = [
    "Diagnose",
    "Extender",
    "ModemFirmware",
    "Reset",
    "Upgrade",
]


class Extender:
    """Extender endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Extender endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.diagnose = Diagnose(client)
        self.modem_firmware = ModemFirmware(client)
        self.reset = Reset(client)
        self.upgrade = Upgrade(client)
