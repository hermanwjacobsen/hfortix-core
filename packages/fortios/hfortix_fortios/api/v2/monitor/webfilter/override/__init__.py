"""FortiOS CMDB - Override category"""

from .delete import Delete

__all__ = [
    "Delete",
    "Override",
]


class Override:
    """Override endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Override endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.delete = Delete(client)
