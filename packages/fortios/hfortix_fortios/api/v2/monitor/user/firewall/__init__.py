"""FortiOS CMDB - Firewall category"""

from .auth import Auth
from .deauth import Deauth

__all__ = [
    "Auth",
    "Deauth",
    "Firewall",
]


class Firewall:
    """Firewall endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Firewall endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.auth = Auth(client)
        self.deauth = Deauth(client)
