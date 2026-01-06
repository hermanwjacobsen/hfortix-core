"""FortiOS CMDB - RogueAp category"""

from .clear_all import ClearAll
from .set_status import SetStatus

__all__ = [
    "ClearAll",
    "RogueAp",
    "SetStatus",
]


class RogueAp:
    """RogueAp endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """RogueAp endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.clear_all = ClearAll(client)
        self.set_status = SetStatus(client)
