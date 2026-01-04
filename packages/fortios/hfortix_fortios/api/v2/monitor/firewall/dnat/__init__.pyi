"""Type stubs for DNAT category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import clear_counters
    from . import reset


class Dnat:
    """Type stub for Dnat."""

    clear_counters: clear_counters.ClearCounters
    reset: reset.Reset

    def __init__(self, client: IHTTPClient) -> None: ...
