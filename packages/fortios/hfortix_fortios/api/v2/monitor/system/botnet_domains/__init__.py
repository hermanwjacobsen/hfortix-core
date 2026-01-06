"""FortiOS CMDB - BotnetDomains category"""

from .hits import Hits
from .stat import Stat

__all__ = [
    "BotnetDomains",
    "Hits",
    "Stat",
]


class BotnetDomains:
    """BotnetDomains endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """BotnetDomains endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.hits = Hits(client)
        self.stat = Stat(client)
