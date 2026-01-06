"""Type stubs for GTP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .flush import Flush


class Gtp:
    """Type stub for Gtp."""

    flush: Flush

    def __init__(self, client: IHTTPClient) -> None: ...
