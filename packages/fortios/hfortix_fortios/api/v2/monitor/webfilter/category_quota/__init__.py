"""FortiOS CMDB - CategoryQuota category"""

from .reset import Reset

__all__ = [
    "CategoryQuota",
    "Reset",
]


class CategoryQuota:
    """CategoryQuota endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """CategoryQuota endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.reset = Reset(client)
