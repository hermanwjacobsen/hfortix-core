"""Type stubs for CERTIFICATE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import download
    from . import read_info


class Certificate:
    """Type stub for Certificate."""

    download: download.Download
    read_info: read_info.ReadInfo

    def __init__(self, client: IHTTPClient) -> None: ...
