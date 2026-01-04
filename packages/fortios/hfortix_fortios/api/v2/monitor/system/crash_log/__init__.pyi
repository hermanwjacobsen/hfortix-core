"""Type stubs for CRASH_LOG category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import clear
    from . import download


class CrashLog:
    """Type stub for CrashLog."""

    clear: clear.Clear
    download: download.Download

    def __init__(self, client: IHTTPClient) -> None: ...
