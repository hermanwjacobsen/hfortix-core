"""Type stubs for WEBCACHE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import stats


class Webcache:
    """Type stub for Webcache."""

    stats: stats.Stats

    def __init__(self, client: IHTTPClient) -> None: ...
