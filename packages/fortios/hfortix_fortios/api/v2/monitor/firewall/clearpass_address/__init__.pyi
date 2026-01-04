"""Type stubs for CLEARPASS_ADDRESS category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import add
    from . import delete


class ClearpassAddress:
    """Type stub for ClearpassAddress."""

    add: add.Add
    delete: delete.Delete

    def __init__(self, client: IHTTPClient) -> None: ...
