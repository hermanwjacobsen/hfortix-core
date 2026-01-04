"""Type stubs for COM_LOG category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import download
    from . import dump
    from . import update


class ComLog:
    """Type stub for ComLog."""

    download: download.Download
    dump: dump.Dump
    update: update.Update

    def __init__(self, client: IHTTPClient) -> None: ...
