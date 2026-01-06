"""Type stubs for EXTENDER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .diagnose import Diagnose
    from .modem_firmware import ModemFirmware
    from .reset import Reset
    from .upgrade import Upgrade


class Extender:
    """Type stub for Extender."""

    diagnose: Diagnose
    modem_firmware: ModemFirmware
    reset: Reset
    upgrade: Upgrade

    def __init__(self, client: IHTTPClient) -> None: ...
