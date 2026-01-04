"""FortiOS CMDB - Local category"""

from .create import Create
from .import_setting import ImportSetting

__all__ = [
    "Create",
    "ImportSetting",
    "Local",
]


class Local:
    """Local endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Local endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.create = Create(client)
        self.import_setting = ImportSetting(client)
