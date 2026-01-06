"""Type stubs for FIRMWARE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .download import Download
    from .push import Push
    from .upload import Upload


class Firmware:
    """Type stub for Firmware."""

    download: Download
    push: Push
    upload: Upload

    def __init__(self, client: IHTTPClient) -> None: ...
