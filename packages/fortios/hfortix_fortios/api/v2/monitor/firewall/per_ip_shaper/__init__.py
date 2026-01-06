"""FortiOS CMDB - PerIpShaper category"""

from .reset import Reset

__all__ = [
    "PerIpShaper",
    "Reset",
]


class PerIpShaper:
    """PerIpShaper endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """PerIpShaper endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.reset = Reset(client)
