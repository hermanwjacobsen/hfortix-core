"""Type stubs for LOOKUP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .ha_peer import HaPeer


class Lookup:
    """Type stub for Lookup."""

    ha_peer: HaPeer

    def __init__(self, client: IHTTPClient) -> None: ...
