"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .ap_names import ApNames
from .ap_status import ApStatus
from .client import Client
from .client_base import Client
from .euclid import Euclid
from .euclid_base import Euclid
from .firmware import Firmware
from .firmware_base import Firmware
from .interfering_ap import InterferingAp
from .managed_ap import ManagedAp
from .managed_ap_base import ManagedAp
from .matched_devices import MatchedDevices
from .meta import Meta
from .rogue_ap import RogueAp
from .rogue_ap_base import RogueAp
from .station_capability import StationCapability
from .statistics import Statistics
from .unassociated_devices import UnassociatedDevices

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Wifi:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.ap_names = ApNames(client)
        self.ap_status = ApStatus(client)
        self.client = Client(client)
        self.client = Client(client)
        self.euclid = Euclid(client)
        self.euclid = Euclid(client)
        self.firmware = Firmware(client)
        self.firmware = Firmware(client)
        self.interfering_ap = InterferingAp(client)
        self.managed_ap = ManagedAp(client)
        self.managed_ap = ManagedAp(client)
        self.matched_devices = MatchedDevices(client)
        self.meta = Meta(client)
        self.rogue_ap = RogueAp(client)
        self.rogue_ap = RogueAp(client)
        self.station_capability = StationCapability(client)
        self.statistics = Statistics(client)
        self.unassociated_devices = UnassociatedDevices(client)
