"""FortiOS CMDB - Csf category"""

from .pending_authorizations import PendingAuthorizations
from .register_appliance import RegisterAppliance

__all__ = [
    "Csf",
    "PendingAuthorizations",
    "RegisterAppliance",
]


class Csf:
    """Csf endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Csf endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.pending_authorizations = PendingAuthorizations(client)
        self.register_appliance = RegisterAppliance(client)
