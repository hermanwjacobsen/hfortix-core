"""FortiOS CMDB - Policy category"""

from .clear_counters import ClearCounters
from .reset import Reset
from .update_global_label import UpdateGlobalLabel

__all__ = [
    "ClearCounters",
    "Policy",
    "Reset",
    "UpdateGlobalLabel",
]


class Policy:
    """Policy endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Policy endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.clear_counters = ClearCounters(client)
        self.reset = Reset(client)
        self.update_global_label = UpdateGlobalLabel(client)
