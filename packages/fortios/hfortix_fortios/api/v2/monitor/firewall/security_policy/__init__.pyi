"""Type stubs for SECURITY_POLICY category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import clear_counters
    from . import update_global_label


class SecurityPolicy:
    """Type stub for SecurityPolicy."""

    clear_counters: clear_counters.ClearCounters
    update_global_label: update_global_label.UpdateGlobalLabel

    def __init__(self, client: IHTTPClient) -> None: ...
