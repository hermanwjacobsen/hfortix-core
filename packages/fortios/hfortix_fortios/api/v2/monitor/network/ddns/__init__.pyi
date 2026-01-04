"""Type stubs for DDNS category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import lookup


class Ddns:
    """Type stub for Ddns."""

    lookup: lookup.Lookup

    def __init__(self, client: IHTTPClient) -> None: ...
