"""Type stubs for MULTICAST_POLICY6 category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .clear_counters import ClearCounters
    from .reset import Reset


class MulticastPolicy6:
    """Type stub for MulticastPolicy6."""

    clear_counters: ClearCounters
    reset: Reset

    def __init__(self, client: IHTTPClient) -> None: ...
