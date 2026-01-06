"""Type stubs for FORTICLOUD category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .connection import Connection


class Forticloud:
    """Type stub for Forticloud."""

    connection: Connection

    def __init__(self, client: IHTTPClient) -> None: ...
