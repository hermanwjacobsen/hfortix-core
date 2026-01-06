"""Type stubs for MALICIOUS_URLS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .stat import Stat


class MaliciousUrls:
    """Type stub for MaliciousUrls."""

    stat: Stat

    def __init__(self, client: IHTTPClient) -> None: ...
