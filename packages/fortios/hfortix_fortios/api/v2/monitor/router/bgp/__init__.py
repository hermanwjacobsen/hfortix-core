"""FortiOS CMDB - Bgp category"""

from .clear_soft_in import ClearSoftIn
from .clear_soft_out import ClearSoftOut
from .soft_reset_neighbor import SoftResetNeighbor

__all__ = [
    "Bgp",
    "ClearSoftIn",
    "ClearSoftOut",
    "SoftResetNeighbor",
]


class Bgp:
    """Bgp endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Bgp endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.clear_soft_in = ClearSoftIn(client)
        self.clear_soft_out = ClearSoftOut(client)
        self.soft_reset_neighbor = SoftResetNeighbor(client)
