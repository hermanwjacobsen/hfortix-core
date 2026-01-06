"""FortiOS CMDB - Client category"""

from .disassociate import Disassociate

__all__ = [
    "Client",
    "Disassociate",
]


class Client:
    """Client endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Client endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.disassociate = Disassociate(client)
