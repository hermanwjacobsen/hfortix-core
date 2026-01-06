"""FortiOS CMDB - RegionImage category"""

from .upload import Upload

__all__ = [
    "RegionImage",
    "Upload",
]


class RegionImage:
    """RegionImage endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """RegionImage endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.upload = Upload(client)
