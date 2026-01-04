"""Type stubs for X5G_MODEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import status


class X5gModem:
    """Type stub for X5gModem."""

    status: status.Status

    def __init__(self, client: IHTTPClient) -> None: ...
