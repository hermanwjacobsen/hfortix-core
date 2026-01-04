"""FortiOS CMDB - Acl6 category"""

from .clear_counters import ClearCounters

__all__ = [
    "Acl6",
    "ClearCounters",
]


class Acl6:
    """Acl6 endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Acl6 endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.clear_counters = ClearCounters(client)
