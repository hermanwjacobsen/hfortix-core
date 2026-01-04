"""Type stubs for SPECTRUM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import keep_alive
    from . import start
    from . import stop


class Spectrum:
    """Type stub for Spectrum."""

    keep_alive: keep_alive.KeepAlive
    start: start.Start
    stop: stop.Stop

    def __init__(self, client: IHTTPClient) -> None: ...
