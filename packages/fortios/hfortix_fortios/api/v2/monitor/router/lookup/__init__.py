"""FortiOS CMDB - Lookup category"""

from .ha_peer import HaPeer

__all__ = [
    "HaPeer",
    "Lookup",
]


class Lookup:
    """Lookup endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Lookup endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.ha_peer = HaPeer(client)
