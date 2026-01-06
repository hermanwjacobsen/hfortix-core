"""Type stubs for AVAILABLE_INTERFACES category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .meta import Meta


class AvailableInterfaces:
    """Type stub for AvailableInterfaces."""

    meta: Meta

    def __init__(self, client: IHTTPClient) -> None: ...
