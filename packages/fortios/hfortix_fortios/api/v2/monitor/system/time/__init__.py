"""FortiOS CMDB - Time category"""

from .set import Set

__all__ = [
    "Set",
    "Time",
]


class Time:
    """Time endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Time endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.set = Set(client)
