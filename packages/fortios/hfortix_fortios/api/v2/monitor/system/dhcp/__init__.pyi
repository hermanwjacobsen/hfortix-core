"""Type stubs for DHCP category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import revoke


class Dhcp:
    """Type stub for Dhcp."""

    revoke: revoke.Revoke

    def __init__(self, client: IHTTPClient) -> None: ...
