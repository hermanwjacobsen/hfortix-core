"""FortiOS CMDB - Network category"""

from . import ddns
from . import debug_flow
from .arp import Arp
from .dns import Dns
from .fortiguard import Fortiguard
from .lldp import Lldp
from .reverse_ip_lookup import ReverseIpLookup

__all__ = [
    "Arp",
    "Ddns",
    "DebugFlow",
    "Dns",
    "Fortiguard",
    "Lldp",
    "Network",
    "ReverseIpLookup",
]


class Network:
    """Network endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Network endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.ddns = ddns.Ddns(client)
        self.debug_flow = debug_flow.DebugFlow(client)
        self.arp = Arp(client)
        self.dns = Dns(client)
        self.fortiguard = Fortiguard(client)
        self.lldp = Lldp(client)
        self.reverse_ip_lookup = ReverseIpLookup(client)
