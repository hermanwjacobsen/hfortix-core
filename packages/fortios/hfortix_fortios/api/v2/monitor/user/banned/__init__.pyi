"""Type stubs for BANNED category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .add_users import AddUsers
    from .check import Check
    from .clear_all import ClearAll
    from .clear_users import ClearUsers


class Banned:
    """Type stub for Banned."""

    add_users: AddUsers
    check: Check
    clear_all: ClearAll
    clear_users: ClearUsers

    def __init__(self, client: IHTTPClient) -> None: ...
