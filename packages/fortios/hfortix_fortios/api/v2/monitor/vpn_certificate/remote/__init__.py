"""FortiOS CMDB - Remote category"""

from .import_setting import ImportSetting

__all__ = [
    "ImportSetting",
    "Remote",
]


class Remote:
    """Remote endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Remote endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.import_setting = ImportSetting(client)
