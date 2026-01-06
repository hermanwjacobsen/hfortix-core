"""Type stubs for MODEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .connect import Connect
    from .disconnect import Disconnect
    from .reset import Reset
    from .update import Update


class Modem:
    """Type stub for Modem."""

    connect: Connect
    disconnect: Disconnect
    reset: Reset
    update: Update

    def __init__(self, client: IHTTPClient) -> None: ...
