"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .fabric_admin_lockout_exists_on_firmware_update import FabricAdminLockoutExistsOnFirmwareUpdate
from .fabric_time_in_sync import FabricTimeInSync

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class System:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.fabric_admin_lockout_exists_on_firmware_update = FabricAdminLockoutExistsOnFirmwareUpdate(client)
        self.fabric_time_in_sync = FabricTimeInSync(client)
