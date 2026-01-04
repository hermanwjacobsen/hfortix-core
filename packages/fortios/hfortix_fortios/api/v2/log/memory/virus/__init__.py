"""FortiOS CMDB - Virus category"""

from .archive import Archive

__all__ = [
    "Archive",
    "Virus",
]


class Virus:
    """Virus endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Virus endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.archive = Archive(client)
