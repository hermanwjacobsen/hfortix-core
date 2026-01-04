"""Type stubs for PROXY_POLICY category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import clear_counters


class ProxyPolicy:
    """Type stub for ProxyPolicy."""

    clear_counters: clear_counters.ClearCounters

    def __init__(self, client: IHTTPClient) -> None: ...
