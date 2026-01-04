"""Type stubs for DHCP6 category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import server


class Dhcp6:
    """Type stub for Dhcp6."""

    server: server.Server

    def __init__(self, client: IHTTPClient) -> None: ...
