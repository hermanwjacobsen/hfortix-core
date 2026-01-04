"""FortiOS CMDB - Log category"""

from . import disk
from . import fortianalyzer
from . import forticloud
from . import log
from . import memory
from .search import Search

__all__ = [
    "Disk",
    "Fortianalyzer",
    "Forticloud",
    "Log",
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
        self.disk = disk.Disk(client)
        self.fortianalyzer = fortianalyzer.Fortianalyzer(client)
        self.forticloud = forticloud.Forticloud(client)
        self.log = log.Log(client)
        self.memory = memory.Memory(client)
        self.search = Search(client)
