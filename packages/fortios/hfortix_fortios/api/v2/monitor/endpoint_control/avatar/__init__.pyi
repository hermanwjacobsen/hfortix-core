"""Type stubs for AVATAR category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import download


class Avatar:
    """Type stub for Avatar."""

    download: download.Download

    def __init__(self, client: IHTTPClient) -> None: ...
