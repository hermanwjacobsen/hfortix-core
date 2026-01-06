"""Type stubs for FIRMWARE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .upgrade import Upgrade
    from .upgrade_paths import UpgradePaths


class Firmware:
    """Type stub for Firmware."""

    upgrade: Upgrade
    upgrade_paths: UpgradePaths

    def __init__(self, client: IHTTPClient) -> None: ...
