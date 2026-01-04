"""FortiOS CMDB - Forticloud category"""

from .connection import Connection

__all__ = [
    "Connection",
    "Forticloud",
]


class Forticloud:
    """Forticloud endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Forticloud endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.connection = Connection(client)
