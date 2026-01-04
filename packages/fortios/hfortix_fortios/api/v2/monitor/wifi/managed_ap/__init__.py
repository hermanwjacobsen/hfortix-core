"""FortiOS CMDB - ManagedAp category"""

from .led_blink import LedBlink
from .restart import Restart
from .set_status import SetStatus

__all__ = [
    "LedBlink",
    "ManagedAp",
    "Restart",
    "SetStatus",
]


class ManagedAp:
    """ManagedAp endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """ManagedAp endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.led_blink = LedBlink(client)
        self.restart = Restart(client)
        self.set_status = SetStatus(client)
