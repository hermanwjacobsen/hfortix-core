"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .history import History
from .history_base import History
from .peer_stats import PeerStats
from .peer_stats_base import PeerStats
from .webcache import Webcache
from .webcache_base import Webcache

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Wanopt:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.history = History(client)
        self.history = History(client)
        self.peer_stats = PeerStats(client)
        self.peer_stats = PeerStats(client)
        self.webcache = Webcache(client)
        self.webcache = Webcache(client)
