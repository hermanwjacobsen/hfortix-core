"""Type stubs for APPLICATION_LIST category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import refresh


class ApplicationList:
    """Type stub for ApplicationList."""

    refresh: refresh.Refresh

    def __init__(self, client: IHTTPClient) -> None: ...
