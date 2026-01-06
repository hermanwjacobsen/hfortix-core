"""Type stubs for SSL category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .clear_tunnel import ClearTunnel
    from .delete import Delete
    from .stats import Stats


class Ssl:
    """Type stub for Ssl."""

    clear_tunnel: ClearTunnel
    delete: Delete
    stats: Stats

    def __init__(self, client: IHTTPClient) -> None: ...
