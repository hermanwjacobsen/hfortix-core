"""FortiOS CMDB - Botnet category"""

from .stat import Stat

__all__ = [
    "Botnet",
    "Stat",
]


class Botnet:
    """Botnet endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Botnet endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.stat = Stat(client)
