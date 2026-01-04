"""FortiOS CMDB - Modem category"""

from .connect import Connect
from .disconnect import Disconnect
from .reset import Reset
from .update import Update

__all__ = [
    "Connect",
    "Disconnect",
    "Modem",
    "Reset",
    "Update",
]


class Modem:
    """Modem endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Modem endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.connect = Connect(client)
        self.disconnect = Disconnect(client)
        self.reset = Reset(client)
        self.update = Update(client)
