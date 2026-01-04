"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .health_check import HealthCheck
from .interface_log import InterfaceLog
from .members import Members
from .sla_log import SlaLog
from .sladb import Sladb

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class VirtualWan:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.health_check = HealthCheck(client)
        self.interface_log = InterfaceLog(client)
        self.members = Members(client)
        self.sla_log = SlaLog(client)
        self.sladb = Sladb(client)
