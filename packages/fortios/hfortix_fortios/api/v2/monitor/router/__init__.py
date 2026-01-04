"""FortiOS CMDB - Router category"""

from . import bgp
from . import lookup
from .charts import Charts
from .ipv4 import Ipv4
from .ipv6 import Ipv6
from .lookup_policy import LookupPolicy
from .ospf import Ospf
from .policy import Policy
from .policy6 import Policy6
from .sdwan import Sdwan
from .statistics import Statistics

__all__ = [
    "Bgp",
    "Charts",
    "Ipv4",
    "Ipv6",
    "Lookup",
    "LookupPolicy",
    "Ospf",
    "Policy",
    "Policy6",
    "Router",
    "Sdwan",
    "Statistics",
]


class Router:
    """Router endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Router endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.bgp = bgp.Bgp(client)
        self.lookup = lookup.Lookup(client)
        self.charts = Charts(client)
        self.ipv4 = Ipv4(client)
        self.ipv6 = Ipv6(client)
        self.lookup_policy = LookupPolicy(client)
        self.ospf = Ospf(client)
        self.policy = Policy(client)
        self.policy6 = Policy6(client)
        self.sdwan = Sdwan(client)
        self.statistics = Statistics(client)
