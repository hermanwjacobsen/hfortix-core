"""FortiOS CMDB - Firmware category"""

from .download import Download
from .push import Push
from .upload import Upload

__all__ = [
    "Download",
    "Firmware",
    "Push",
    "Upload",
]


class Firmware:
    """Firmware endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Firmware endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.download = Download(client)
        self.push = Push(client)
        self.upload = Upload(client)
