"""Type stubs for ICAP category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import profile
    from . import server
    from . import server_group


class Icap:
    """Type stub for Icap."""

    profile: profile.Profile
    server: server.Server
    server_group: server_group.ServerGroup

    def __init__(self, client: IHTTPClient) -> None: ...
