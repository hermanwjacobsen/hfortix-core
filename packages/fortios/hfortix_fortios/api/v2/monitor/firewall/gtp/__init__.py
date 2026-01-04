"""FortiOS CMDB - Gtp category"""

from .flush import Flush

__all__ = [
    "Flush",
    "Gtp",
]


class Gtp:
    """Gtp endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Gtp endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.flush = Flush(client)
