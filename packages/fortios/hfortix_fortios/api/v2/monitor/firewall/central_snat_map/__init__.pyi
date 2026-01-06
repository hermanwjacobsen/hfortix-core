"""Type stubs for CENTRAL_SNAT_MAP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .clear_counters import ClearCounters
    from .reset import Reset


class CentralSnatMap:
    """Type stub for CentralSnatMap."""

    clear_counters: ClearCounters
    reset: Reset

    def __init__(self, client: IHTTPClient) -> None: ...
