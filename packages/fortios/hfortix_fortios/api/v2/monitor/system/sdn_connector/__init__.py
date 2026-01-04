"""FortiOS CMDB - SdnConnector category"""

from .update import Update
from .validate_gcp_key import ValidateGcpKey

__all__ = [
    "SdnConnector",
    "Update",
    "ValidateGcpKey",
]


class SdnConnector:
    """SdnConnector endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """SdnConnector endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.update = Update(client)
        self.validate_gcp_key = ValidateGcpKey(client)
