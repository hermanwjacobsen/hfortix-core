"""FortiOS CMDB - History category"""

from .reset import Reset

__all__ = [
    "History",
    "Reset",
]


class History:
    """History endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """History endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.reset = Reset(client)
