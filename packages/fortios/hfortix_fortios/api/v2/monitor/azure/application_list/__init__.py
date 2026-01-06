"""FortiOS CMDB - ApplicationList category"""

from .refresh import Refresh

__all__ = [
    "ApplicationList",
    "Refresh",
]


class ApplicationList:
    """ApplicationList endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """ApplicationList endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.refresh = Refresh(client)
