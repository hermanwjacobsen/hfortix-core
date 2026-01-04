"""FortiOS CMDB - VlanProbe category"""

from .start import Start
from .stop import Stop

__all__ = [
    "Start",
    "Stop",
    "VlanProbe",
]


class VlanProbe:
    """VlanProbe endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """VlanProbe endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.start = Start(client)
        self.stop = Stop(client)
