"""Type stubs for FIRMWARE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import upgrade
    from . import upgrade_paths


class Firmware:
    """Type stub for Firmware."""

    upgrade: upgrade.Upgrade
    upgrade_paths: upgrade_paths.UpgradePaths

    def __init__(self, client: IHTTPClient) -> None: ...
