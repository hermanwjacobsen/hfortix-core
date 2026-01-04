"""Type stubs for INSTALLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import download


class Installer:
    """Type stub for Installer."""

    download: download.Download

    def __init__(self, client: IHTTPClient) -> None: ...
