"""Type stubs for FSCK category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import start


class Fsck:
    """Type stub for Fsck."""

    start: start.Start

    def __init__(self, client: IHTTPClient) -> None: ...
