"""Type stubs for NETWORK category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import connect
    from . import list
    from . import scan
    from . import status


class Network:
    """Type stub for Network."""

    connect: connect.Connect
    list: list.List
    scan: scan.Scan
    status: status.Status

    def __init__(self, client: IHTTPClient) -> None: ...
