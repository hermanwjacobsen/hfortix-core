"""Type stubs for TIME category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import set


class Time:
    """Type stub for Time."""

    set: set.Set

    def __init__(self, client: IHTTPClient) -> None: ...
