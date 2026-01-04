"""FortiOS CMDB - Csf category"""

from .register_appliance import RegisterAppliance

__all__ = [
    "Csf",
    "RegisterAppliance",
]


class Csf:
    """Csf endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Csf endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.register_appliance = RegisterAppliance(client)
