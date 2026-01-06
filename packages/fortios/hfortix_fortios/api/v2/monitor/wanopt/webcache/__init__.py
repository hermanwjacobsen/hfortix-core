"""FortiOS CMDB - Webcache category"""

from .reset import Reset

__all__ = [
    "Reset",
    "Webcache",
]


class Webcache:
    """Webcache endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Webcache endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.reset = Reset(client)
