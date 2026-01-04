"""FortiOS CMDB - PeerStats category"""

from .reset import Reset

__all__ = [
    "PeerStats",
    "Reset",
]


class PeerStats:
    """PeerStats endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """PeerStats endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.reset = Reset(client)
