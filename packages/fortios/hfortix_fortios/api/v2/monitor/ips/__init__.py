"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .anomaly import Anomaly
from .hold_signatures import HoldSignatures
from .metadata import Metadata
from .rate_based import RateBased

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Ips:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.anomaly = Anomaly(client)
        self.hold_signatures = HoldSignatures(client)
        self.metadata = Metadata(client)
        self.rate_based = RateBased(client)
