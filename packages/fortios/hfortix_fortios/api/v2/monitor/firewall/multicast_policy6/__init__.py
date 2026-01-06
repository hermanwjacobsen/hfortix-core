"""FortiOS CMDB - MulticastPolicy6 category"""

from .clear_counters import ClearCounters
from .reset import Reset

__all__ = [
    "ClearCounters",
    "MulticastPolicy6",
    "Reset",
]


class MulticastPolicy6:
    """MulticastPolicy6 endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """MulticastPolicy6 endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.clear_counters = ClearCounters(client)
        self.reset = Reset(client)
