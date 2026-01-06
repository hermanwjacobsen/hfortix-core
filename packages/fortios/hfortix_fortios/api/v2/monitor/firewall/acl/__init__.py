"""FortiOS CMDB - Acl category"""

from .clear_counters import ClearCounters

__all__ = [
    "Acl",
    "ClearCounters",
]


class Acl:
    """Acl endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Acl endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.clear_counters = ClearCounters(client)
