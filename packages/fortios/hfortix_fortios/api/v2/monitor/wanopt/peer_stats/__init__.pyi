"""Type stubs for PEER_STATS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .reset import Reset


class PeerStats:
    """Type stub for PeerStats."""

    reset: Reset

    def __init__(self, client: IHTTPClient) -> None: ...
