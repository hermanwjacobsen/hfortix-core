"""Type stubs for BOTNET category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .stat import Stat


class Botnet:
    """Type stub for Botnet."""

    stat: Stat

    def __init__(self, client: IHTTPClient) -> None: ...
