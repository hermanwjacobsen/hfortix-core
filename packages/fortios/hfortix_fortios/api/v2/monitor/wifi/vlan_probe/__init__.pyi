"""Type stubs for VLAN_PROBE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .start import Start
    from .stop import Stop


class VlanProbe:
    """Type stub for VlanProbe."""

    start: Start
    stop: Stop

    def __init__(self, client: IHTTPClient) -> None: ...
