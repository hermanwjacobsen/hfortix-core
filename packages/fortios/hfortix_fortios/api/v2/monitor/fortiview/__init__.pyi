"""Type stubs for FORTIVIEW category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import historical_statistics
    from . import realtime_proxy_statistics
    from . import realtime_statistics
    from . import session


class Fortiview:
    """Type stub for Fortiview."""

    session: session.Session
    historical_statistics: historical_statistics.HistoricalStatistics
    realtime_proxy_statistics: realtime_proxy_statistics.RealtimeProxyStatistics
    realtime_statistics: realtime_statistics.RealtimeStatistics

    def __init__(self, client: IHTTPClient) -> None: ...
