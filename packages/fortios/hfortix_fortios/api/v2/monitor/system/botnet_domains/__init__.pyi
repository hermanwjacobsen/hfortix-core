"""Type stubs for BOTNET_DOMAINS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .hits import Hits
    from .stat import Stat


class BotnetDomains:
    """Type stub for BotnetDomains."""

    hits: Hits
    stat: Stat

    def __init__(self, client: IHTTPClient) -> None: ...
