"""FortiOS CMDB - Ipsec category"""

from .tunnel_down import TunnelDown
from .tunnel_reset_stats import TunnelResetStats
from .tunnel_up import TunnelUp

__all__ = [
    "Ipsec",
    "TunnelDown",
    "TunnelResetStats",
    "TunnelUp",
]


class Ipsec:
    """Ipsec endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Ipsec endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.tunnel_down = TunnelDown(client)
        self.tunnel_reset_stats = TunnelResetStats(client)
        self.tunnel_up = TunnelUp(client)
