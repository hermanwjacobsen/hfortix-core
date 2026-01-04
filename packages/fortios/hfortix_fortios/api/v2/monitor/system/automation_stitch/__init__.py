"""FortiOS CMDB - AutomationStitch category"""

from .test import Test
from .webhook import Webhook

__all__ = [
    "AutomationStitch",
    "Test",
    "Webhook",
]


class AutomationStitch:
    """AutomationStitch endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """AutomationStitch endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.test = Test(client)
        self.webhook = Webhook(client)
