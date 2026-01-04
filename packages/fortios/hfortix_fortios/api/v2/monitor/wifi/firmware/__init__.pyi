"""Type stubs for FIRMWARE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import download
    from . import push
    from . import upload


class Firmware:
    """Type stub for Firmware."""

    download: download.Download
    push: push.Push
    upload: upload.Upload

    def __init__(self, client: IHTTPClient) -> None: ...
