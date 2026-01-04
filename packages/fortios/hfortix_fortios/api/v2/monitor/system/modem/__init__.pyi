"""Type stubs for MODEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import connect
    from . import disconnect
    from . import reset
    from . import update


class Modem:
    """Type stub for Modem."""

    connect: connect.Connect
    disconnect: disconnect.Disconnect
    reset: reset.Reset
    update: update.Update

    def __init__(self, client: IHTTPClient) -> None: ...
