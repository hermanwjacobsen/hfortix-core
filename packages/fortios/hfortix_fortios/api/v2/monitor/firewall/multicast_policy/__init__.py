"""FortiOS CMDB - MulticastPolicy category"""

from .clear_counters import ClearCounters
from .reset import Reset

__all__ = [
    "ClearCounters",
    "MulticastPolicy",
    "Reset",
]


class MulticastPolicy:
    """MulticastPolicy endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """MulticastPolicy endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.clear_counters = ClearCounters(client)
        self.reset = Reset(client)
