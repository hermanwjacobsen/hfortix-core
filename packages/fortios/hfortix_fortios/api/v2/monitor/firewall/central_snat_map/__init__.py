"""FortiOS CMDB - CentralSnatMap category"""

from .clear_counters import ClearCounters
from .reset import Reset

__all__ = [
    "CentralSnatMap",
    "ClearCounters",
    "Reset",
]


class CentralSnatMap:
    """CentralSnatMap endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """CentralSnatMap endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.clear_counters = ClearCounters(client)
        self.reset = Reset(client)
