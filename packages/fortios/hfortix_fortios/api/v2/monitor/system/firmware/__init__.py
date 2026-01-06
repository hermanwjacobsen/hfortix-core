"""FortiOS CMDB - Firmware category"""

from .upgrade import Upgrade
from .upgrade_paths import UpgradePaths

__all__ = [
    "Firmware",
    "Upgrade",
    "UpgradePaths",
]


class Firmware:
    """Firmware endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Firmware endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.upgrade = Upgrade(client)
        self.upgrade_paths = UpgradePaths(client)
