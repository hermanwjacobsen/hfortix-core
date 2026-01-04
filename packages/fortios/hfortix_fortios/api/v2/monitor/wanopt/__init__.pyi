"""Type stubs for WANOPT category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import history
    from . import peer_stats
    from . import webcache


class Wanopt:
    """Type stub for Wanopt."""

    history: history.History
    peer_stats: peer_stats.PeerStats
    webcache: webcache.Webcache

    def __init__(self, client: IHTTPClient) -> None: ...
