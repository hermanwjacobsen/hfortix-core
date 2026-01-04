"""FortiOS CMDB - Shaper category"""

from .reset import Reset

__all__ = [
    "Reset",
    "Shaper",
]


class Shaper:
    """Shaper endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Shaper endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.reset = Reset(client)
