"""Type stubs for AUTOUPDATE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import schedule


class Autoupdate:
    """Type stub for Autoupdate."""

    schedule: schedule.Schedule

    def __init__(self, client: IHTTPClient) -> None: ...
