"""Type stubs for IPSEC category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import tunnel_down
    from . import tunnel_reset_stats
    from . import tunnel_up


class Ipsec:
    """Type stub for Ipsec."""

    tunnel_down: tunnel_down.TunnelDown
    tunnel_reset_stats: tunnel_reset_stats.TunnelResetStats
    tunnel_up: tunnel_up.TunnelUp

    def __init__(self, client: IHTTPClient) -> None: ...
