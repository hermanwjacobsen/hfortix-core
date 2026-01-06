"""FortiOS CMDB - Ssl category"""

from .clear_tunnel import ClearTunnel
from .delete import Delete
from .stats import Stats

__all__ = [
    "ClearTunnel",
    "Delete",
    "Ssl",
    "Stats",
]


class Ssl:
    """Ssl endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Ssl endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.clear_tunnel = ClearTunnel(client)
        self.delete = Delete(client)
        self.stats = Stats(client)
