"""Type stubs for SESSION category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import close
    from . import close_all
    from . import close_multiple


class Session:
    """Type stub for Session."""

    close: close.Close
    close_all: close_all.CloseAll
    close_multiple: close_multiple.CloseMultiple

    def __init__(self, client: IHTTPClient) -> None: ...
