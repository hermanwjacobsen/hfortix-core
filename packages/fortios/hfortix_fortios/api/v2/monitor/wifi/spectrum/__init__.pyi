"""Type stubs for SPECTRUM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .keep_alive import KeepAlive
    from .start import Start
    from .stop import Stop


class Spectrum:
    """Type stub for Spectrum."""

    keep_alive: KeepAlive
    start: Start
    stop: Stop

    def __init__(self, client: IHTTPClient) -> None: ...
