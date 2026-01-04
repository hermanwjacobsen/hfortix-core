"""Type stubs for EXTENDER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import diagnose
    from . import modem_firmware
    from . import reset
    from . import upgrade


class Extender:
    """Type stub for Extender."""

    diagnose: diagnose.Diagnose
    modem_firmware: modem_firmware.ModemFirmware
    reset: reset.Reset
    upgrade: upgrade.Upgrade

    def __init__(self, client: IHTTPClient) -> None: ...
