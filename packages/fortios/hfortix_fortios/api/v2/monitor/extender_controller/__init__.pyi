"""Type stubs for EXTENDER_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import extender


class ExtenderController:
    """Type stub for ExtenderController."""

    extender: extender.Extender

    def __init__(self, client: IHTTPClient) -> None: ...
