"""Type stubs for SYSTEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import fabric_admin_lockout_exists_on_firmware_update
    from . import fabric_time_in_sync
    from . import psirt_vulnerabilities


class System:
    """Type stub for System."""

    fabric_admin_lockout_exists_on_firmware_update: fabric_admin_lockout_exists_on_firmware_update.FabricAdminLockoutExistsOnFirmwareUpdate
    fabric_time_in_sync: fabric_time_in_sync.FabricTimeInSync
    psirt_vulnerabilities: psirt_vulnerabilities.PsirtVulnerabilities

    def __init__(self, client: IHTTPClient) -> None: ...
