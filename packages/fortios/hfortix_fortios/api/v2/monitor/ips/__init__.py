"""FortiOS CMDB - Ips category"""

from .anomaly import Anomaly
from .hold_signatures import HoldSignatures
from .metadata import Metadata
from .rate_based import RateBased
from .session import Session

__all__ = [
    "Anomaly",
    "HoldSignatures",
    "Ips",
    "Metadata",
    "RateBased",
    "Session",
]


class Ips:
    """Ips endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Ips endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.anomaly = Anomaly(client)
        self.hold_signatures = HoldSignatures(client)
        self.metadata = Metadata(client)
        self.rate_based = RateBased(client)
        self.session = Session(client)
