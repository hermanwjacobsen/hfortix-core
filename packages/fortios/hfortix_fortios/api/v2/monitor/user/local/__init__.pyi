"""Type stubs for LOCAL category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import change_password


class Local:
    """Type stub for Local."""

    change_password: change_password.ChangePassword

    def __init__(self, client: IHTTPClient) -> None: ...
