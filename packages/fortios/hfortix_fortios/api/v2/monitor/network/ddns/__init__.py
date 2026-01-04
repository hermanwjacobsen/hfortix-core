"""FortiOS CMDB - Ddns category"""

from .lookup import Lookup

__all__ = [
    "Ddns",
    "Lookup",
]


class Ddns:
    """Ddns endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Ddns endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.lookup = Lookup(client)
