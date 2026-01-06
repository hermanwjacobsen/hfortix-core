"""FortiOS CMDB - Fsso category"""

from .refresh_server import RefreshServer

__all__ = [
    "Fsso",
    "RefreshServer",
]


class Fsso:
    """Fsso endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Fsso endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.refresh_server = RefreshServer(client)
