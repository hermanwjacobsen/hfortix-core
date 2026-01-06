"""FortiOS CMDB - Ippool category"""

from .mapping import Mapping

__all__ = [
    "Ippool",
    "Mapping",
]


class Ippool:
    """Ippool endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Ippool endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.mapping = Mapping(client)
