"""FortiOS CMDB - AvailableInterfaces category"""

from .meta import Meta

__all__ = [
    "AvailableInterfaces",
    "Meta",
]


class AvailableInterfaces:
    """AvailableInterfaces endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """AvailableInterfaces endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.meta = Meta(client)
