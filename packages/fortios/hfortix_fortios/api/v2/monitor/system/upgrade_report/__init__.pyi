"""Type stubs for UPGRADE_REPORT category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import exists
    from . import saved


class UpgradeReport:
    """Type stub for UpgradeReport."""

    exists: exists.Exists
    saved: saved.Saved

    def __init__(self, client: IHTTPClient) -> None: ...
