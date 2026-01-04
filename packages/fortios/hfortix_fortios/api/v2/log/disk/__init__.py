"""FortiOS CMDB - Disk category"""

from . import virus

__all__ = [
    "Disk",
    "Virus",
]


class Disk:
    """Disk endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Disk endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.virus = virus.Virus(client)
