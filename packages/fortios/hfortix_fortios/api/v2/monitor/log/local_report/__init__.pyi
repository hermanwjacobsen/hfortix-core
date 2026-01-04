"""Type stubs for LOCAL_REPORT category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import delete
    from . import download


class LocalReport:
    """Type stub for LocalReport."""

    delete: delete.Delete
    download: download.Download

    def __init__(self, client: IHTTPClient) -> None: ...
