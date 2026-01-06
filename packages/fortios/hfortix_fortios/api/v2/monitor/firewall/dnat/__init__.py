"""FortiOS CMDB - Dnat category"""

from .clear_counters import ClearCounters
from .reset import Reset

__all__ = [
    "ClearCounters",
    "Dnat",
    "Reset",
]


class Dnat:
    """Dnat endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Dnat endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.clear_counters = ClearCounters(client)
        self.reset = Reset(client)
