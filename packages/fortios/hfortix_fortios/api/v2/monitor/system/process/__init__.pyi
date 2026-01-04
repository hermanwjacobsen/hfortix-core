"""Type stubs for PROCESS category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import kill


class Process:
    """Type stub for Process."""

    kill: kill.Kill

    def __init__(self, client: IHTTPClient) -> None: ...
