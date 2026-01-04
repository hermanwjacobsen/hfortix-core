"""Type stubs for SNIFFER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import delete
    from . import download
    from . import list
    from . import meta
    from . import start
    from . import stop


class Sniffer:
    """Type stub for Sniffer."""

    delete: delete.Delete
    download: download.Download
    list: list.List
    meta: meta.Meta
    start: start.Start
    stop: stop.Stop

    def __init__(self, client: IHTTPClient) -> None: ...
