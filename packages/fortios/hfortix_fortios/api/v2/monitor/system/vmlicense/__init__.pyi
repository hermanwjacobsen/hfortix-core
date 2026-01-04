"""Type stubs for VMLICENSE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import download
    from . import download_eval
    from . import upload


class Vmlicense:
    """Type stub for Vmlicense."""

    download: download.Download
    download_eval: download_eval.DownloadEval
    upload: upload.Upload

    def __init__(self, client: IHTTPClient) -> None: ...
