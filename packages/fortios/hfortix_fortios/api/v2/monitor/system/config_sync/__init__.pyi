"""Type stubs for CONFIG_SYNC category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import status


class ConfigSync:
    """Type stub for ConfigSync."""

    status: status.Status

    def __init__(self, client: IHTTPClient) -> None: ...
