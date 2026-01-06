"""Type stubs for POLICY category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .clear_counters import ClearCounters
    from .reset import Reset
    from .update_global_label import UpdateGlobalLabel


class Policy:
    """Type stub for Policy."""

    clear_counters: ClearCounters
    reset: Reset
    update_global_label: UpdateGlobalLabel

    def __init__(self, client: IHTTPClient) -> None: ...
