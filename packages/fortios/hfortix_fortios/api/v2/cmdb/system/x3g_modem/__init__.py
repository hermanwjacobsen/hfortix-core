"""FortiOS CMDB - X3gModem category"""

from .custom import Custom

__all__ = [
    "Custom",
    "X3gModem",
]


class X3gModem:
    """X3gModem endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """X3gModem endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.custom = Custom(client)
