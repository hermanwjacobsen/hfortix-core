"""Type stubs for BANNED category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import add_users
    from . import check
    from . import clear_all
    from . import clear_users


class Banned:
    """Type stub for Banned."""

    add_users: add_users.AddUsers
    check: check.Check
    clear_all: clear_all.ClearAll
    clear_users: clear_users.ClearUsers

    def __init__(self, client: IHTTPClient) -> None: ...
