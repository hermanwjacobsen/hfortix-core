"""Type stubs for PACFILE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import download
    from . import upload


class Pacfile:
    """Type stub for Pacfile."""

    download: download.Download
    upload: upload.Upload

    def __init__(self, client: IHTTPClient) -> None: ...
