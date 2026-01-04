"""FortiOS CMDB - Euclid category"""

from .reset import Reset

__all__ = [
    "Euclid",
    "Reset",
]


class Euclid:
    """Euclid endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Euclid endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.reset = Reset(client)
