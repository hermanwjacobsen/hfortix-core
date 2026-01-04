"""Type stubs for X3G_MODEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import custom


class X3gModem:
    """Type stub for X3gModem."""

    custom: custom.Custom

    def __init__(self, client: IHTTPClient) -> None: ...
