"""FortiOS CMDB - Installer category"""

from .download import Download

__all__ = [
    "Download",
    "Installer",
]


class Installer:
    """Installer endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Installer endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.download = Download(client)
