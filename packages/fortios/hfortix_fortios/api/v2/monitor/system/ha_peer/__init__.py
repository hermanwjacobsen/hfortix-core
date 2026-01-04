"""FortiOS CMDB - HaPeer category"""

from .disconnect import Disconnect
from .update import Update

__all__ = [
    "Disconnect",
    "HaPeer",
    "Update",
]


class HaPeer:
    """HaPeer endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """HaPeer endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.disconnect = Disconnect(client)
        self.update = Update(client)
