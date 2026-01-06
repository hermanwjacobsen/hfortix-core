"""FortiOS CMDB - MaliciousUrls category"""

from .stat import Stat

__all__ = [
    "MaliciousUrls",
    "Stat",
]


class MaliciousUrls:
    """MaliciousUrls endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """MaliciousUrls endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.stat = Stat(client)
