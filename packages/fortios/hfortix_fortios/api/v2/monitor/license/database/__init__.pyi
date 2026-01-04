"""Type stubs for DATABASE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import upgrade


class Database:
    """Type stub for Database."""

    upgrade: upgrade.Upgrade

    def __init__(self, client: IHTTPClient) -> None: ...
