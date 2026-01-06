"""FortiOS CMDB - Proxy category"""

from .count import Count

__all__ = [
    "Count",
    "Proxy",
]


class Proxy:
    """Proxy endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Proxy endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.count = Count(client)
