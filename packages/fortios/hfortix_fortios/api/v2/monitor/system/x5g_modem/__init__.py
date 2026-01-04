"""FortiOS CMDB - X5gModem category"""

from .status import Status

__all__ = [
    "Status",
    "X5gModem",
]


class X5gModem:
    """X5gModem endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """X5gModem endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.status = Status(client)
