"""Type stubs for BLACKLISTED_CERTIFICATES category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .statistics import Statistics


class BlacklistedCertificates:
    """Type stub for BlacklistedCertificates."""

    statistics: Statistics

    def __init__(self, client: IHTTPClient) -> None: ...
