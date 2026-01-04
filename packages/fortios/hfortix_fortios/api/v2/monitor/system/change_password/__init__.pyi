"""Type stubs for CHANGE_PASSWORD category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import select


class ChangePassword:
    """Type stub for ChangePassword."""

    select: select.Select

    def __init__(self, client: IHTTPClient) -> None: ...
