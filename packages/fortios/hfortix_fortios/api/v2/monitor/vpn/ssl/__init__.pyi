"""Type stubs for SSL category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import clear_tunnel
    from . import delete


class Ssl:
    """Type stub for Ssl."""

    clear_tunnel: clear_tunnel.ClearTunnel
    delete: delete.Delete

    def __init__(self, client: IHTTPClient) -> None: ...
