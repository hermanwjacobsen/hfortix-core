"""FortiOS CMDB - Ipam category"""

from .utilization import Utilization

__all__ = [
    "Ipam",
    "Utilization",
]


class Ipam:
    """Ipam endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Ipam endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.utilization = Utilization(client)
