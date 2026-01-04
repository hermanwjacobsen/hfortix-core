"""FortiOS CMDB - Shaper category"""

from .multi_class_shaper import MultiClassShaper
from .reset import Reset

__all__ = [
    "MultiClassShaper",
    "Reset",
    "Shaper",
]


class Shaper:
    """Shaper endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Shaper endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.multi_class_shaper = MultiClassShaper(client)
        self.reset = Reset(client)
