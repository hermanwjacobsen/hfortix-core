"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .charts import Charts
from .ipv4 import Ipv4
from .ipv6 import Ipv6
from .policy import Policy
from .policy6 import Policy6
from .statistics import Statistics

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Router:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.charts = Charts(client)
        self.ipv4 = Ipv4(client)
        self.ipv6 = Ipv6(client)
        self.policy = Policy(client)
        self.policy6 = Policy6(client)
        self.statistics = Statistics(client)
