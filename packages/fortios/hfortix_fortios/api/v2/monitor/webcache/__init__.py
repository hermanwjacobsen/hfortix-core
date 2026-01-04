"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .stats import Stats
from .stats_base import Stats

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Webcache:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.stats = Stats(client)
        self.stats = Stats(client)
