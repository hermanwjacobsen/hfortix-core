"""Type stubs for HA_PEER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import disconnect
    from . import update


class HaPeer:
    """Type stub for HaPeer."""

    disconnect: disconnect.Disconnect
    update: update.Update

    def __init__(self, client: IHTTPClient) -> None: ...
