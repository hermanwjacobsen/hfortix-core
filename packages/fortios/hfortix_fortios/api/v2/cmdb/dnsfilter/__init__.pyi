"""Type stubs for DNSFILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import domain_filter
    from . import profile


class Dnsfilter:
    """Type stub for Dnsfilter."""

    domain_filter: domain_filter.DomainFilter
    profile: profile.Profile

    def __init__(self, client: IHTTPClient) -> None: ...
