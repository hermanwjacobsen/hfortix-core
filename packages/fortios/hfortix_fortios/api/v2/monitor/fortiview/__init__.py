"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .historical_statistics import HistoricalStatistics
from .realtime_proxy_statistics import RealtimeProxyStatistics
from .realtime_statistics import RealtimeStatistics

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Fortiview:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.historical_statistics = HistoricalStatistics(client)
        self.realtime_proxy_statistics = RealtimeProxyStatistics(client)
        self.realtime_statistics = RealtimeStatistics(client)
