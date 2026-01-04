"""Type stubs for POLICY category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import clear_counters
    from . import reset
    from . import update_global_label


class Policy:
    """Type stub for Policy."""

    clear_counters: clear_counters.ClearCounters
    reset: reset.Reset
    update_global_label: update_global_label.UpdateGlobalLabel

    def __init__(self, client: IHTTPClient) -> None: ...
