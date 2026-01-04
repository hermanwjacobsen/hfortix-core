"""FortiOS CMDB - ProxyPolicy category"""

from .clear_counters import ClearCounters

__all__ = [
    "ClearCounters",
    "ProxyPolicy",
]


class ProxyPolicy:
    """ProxyPolicy endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """ProxyPolicy endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.clear_counters = ClearCounters(client)
