"""FortiOS CMDB - UsbLog category"""

from .start import Start
from .stop import Stop

__all__ = [
    "Start",
    "Stop",
    "UsbLog",
]


class UsbLog:
    """UsbLog endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """UsbLog endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.start = Start(client)
        self.stop = Stop(client)
