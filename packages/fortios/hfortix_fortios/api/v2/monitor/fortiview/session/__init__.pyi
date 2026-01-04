"""Type stubs for SESSION category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import cancel


class Session:
    """Type stub for Session."""

    cancel: cancel.Cancel

    def __init__(self, client: IHTTPClient) -> None: ...
