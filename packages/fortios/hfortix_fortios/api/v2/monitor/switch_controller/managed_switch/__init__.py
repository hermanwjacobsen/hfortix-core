"""FortiOS CMDB - ManagedSwitch category"""

from .bounce_port import BouncePort
from .cable_status import CableStatus
from .faceplate_xml import FaceplateXml
from .factory_reset import FactoryReset
from .poe_reset import PoeReset
from .port_stats_reset import PortStatsReset
from .restart import Restart
from .tx_rx import TxRx
from .update import Update

__all__ = [
    "BouncePort",
    "CableStatus",
    "FaceplateXml",
    "FactoryReset",
    "ManagedSwitch",
    "PoeReset",
    "PortStatsReset",
    "Restart",
    "TxRx",
    "Update",
]


class ManagedSwitch:
    """ManagedSwitch endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """ManagedSwitch endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.bounce_port = BouncePort(client)
        self.cable_status = CableStatus(client)
        self.faceplate_xml = FaceplateXml(client)
        self.factory_reset = FactoryReset(client)
        self.poe_reset = PoeReset(client)
        self.port_stats_reset = PortStatsReset(client)
        self.restart = Restart(client)
        self.tx_rx = TxRx(client)
        self.update = Update(client)
