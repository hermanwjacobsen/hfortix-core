"""FortiOS CMDB - Log category"""

from .disk import Disk
from .fortianalyzer import Fortianalyzer
from .forticloud import Forticloud
from .memory import Memory
from .search import Search

__all__ = [
    "Disk",
    "Fortianalyzer",
    "Forticloud",
    "Log",
    "Memory",
    "Search",
]


class Log:
    """Log endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Log endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.disk = Disk(client)
        self.fortianalyzer = Fortianalyzer(client)
        self.forticloud = Forticloud(client)
        self.memory = Memory(client)
        self.search = Search(client)
