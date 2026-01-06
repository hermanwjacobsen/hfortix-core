"""FortiOS CMDB - ConfigScript category"""

from .delete import Delete
from .run import Run
from .upload import Upload

__all__ = [
    "ConfigScript",
    "Delete",
    "Run",
    "Upload",
]


class ConfigScript:
    """ConfigScript endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """ConfigScript endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.delete = Delete(client)
        self.run = Run(client)
        self.upload = Upload(client)
