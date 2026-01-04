"""FortiOS CMDB - Memory category"""

from . import virus

__all__ = [
    "Memory",
    "Virus",
]


class Memory:
    """Memory endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Memory endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.virus = virus.Virus(client)
