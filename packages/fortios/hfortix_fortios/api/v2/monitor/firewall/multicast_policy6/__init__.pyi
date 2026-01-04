"""Type stubs for MULTICAST_POLICY6 category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import clear_counters
    from . import reset


class MulticastPolicy6:
    """Type stub for MulticastPolicy6."""

    clear_counters: clear_counters.ClearCounters
    reset: reset.Reset

    def __init__(self, client: IHTTPClient) -> None: ...
