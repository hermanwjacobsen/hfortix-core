"""Type stubs for DIAMETER_FILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import profile


class DiameterFilter:
    """Type stub for DiameterFilter."""

    profile: profile.Profile

    def __init__(self, client: IHTTPClient) -> None: ...
