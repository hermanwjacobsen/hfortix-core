"""FortiOS CMDB - Crl category"""

from .import_setting import ImportSetting

__all__ = [
    "Crl",
    "ImportSetting",
]


class Crl:
    """Crl endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Crl endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.import_setting = ImportSetting(client)
