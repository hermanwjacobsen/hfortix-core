"""FortiOS CMDB - Language category"""

from .import_setting import ImportSetting

__all__ = [
    "ImportSetting",
    "Language",
]


class Language:
    """Language endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Language endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.import_setting = ImportSetting(client)
