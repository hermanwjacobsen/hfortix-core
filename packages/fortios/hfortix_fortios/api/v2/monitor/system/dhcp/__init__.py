"""FortiOS CMDB - Dhcp category"""

from .revoke import Revoke

__all__ = [
    "Dhcp",
    "Revoke",
]


class Dhcp:
    """Dhcp endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Dhcp endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.revoke = Revoke(client)
