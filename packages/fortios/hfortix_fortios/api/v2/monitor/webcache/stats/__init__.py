"""FortiOS CMDB - Stats category"""

from .reset import Reset

__all__ = [
    "Reset",
    "Stats",
]


class Stats:
    """Stats endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Stats endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.reset = Reset(client)
