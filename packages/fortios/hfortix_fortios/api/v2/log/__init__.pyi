"""Type stubs for LOG category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import disk
    from . import fortianalyzer
    from . import forticloud
    from . import memory
    from . import search


class Log:
    """Type stub for Log."""

    disk: disk.Disk
    fortianalyzer: fortianalyzer.Fortianalyzer
    forticloud: forticloud.Forticloud
    memory: memory.Memory
    search: search.Search

    def __init__(self, client: IHTTPClient) -> None: ...
