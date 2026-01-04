"""FortiOS CMDB - Ca category"""

from .import_setting import ImportSetting

__all__ = [
    "Ca",
    "ImportSetting",
]


class Ca:
    """Ca endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Ca endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.import_setting = ImportSetting(client)
