"""FortiOS CMDB - Forticloud category"""

from . import virus

__all__ = [
    "Forticloud",
    "Virus",
]


class Forticloud:
    """Forticloud endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Forticloud endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.virus = virus.Virus(client)
