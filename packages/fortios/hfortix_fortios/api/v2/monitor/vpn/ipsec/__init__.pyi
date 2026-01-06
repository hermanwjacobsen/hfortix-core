"""Type stubs for IPSEC category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .connection_count import ConnectionCount
    from .tunnel_down import TunnelDown
    from .tunnel_reset_stats import TunnelResetStats
    from .tunnel_up import TunnelUp


class Ipsec:
    """Type stub for Ipsec."""

    connection_count: ConnectionCount
    tunnel_down: TunnelDown
    tunnel_reset_stats: TunnelResetStats
    tunnel_up: TunnelUp

    def __init__(self, client: IHTTPClient) -> None: ...
