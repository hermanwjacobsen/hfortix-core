"""Type stubs for FSSO category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .refresh_server import RefreshServer


class Fsso:
    """Type stub for Fsso."""

    refresh_server: RefreshServer

    def __init__(self, client: IHTTPClient) -> None: ...
