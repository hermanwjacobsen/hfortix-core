"""Type stubs for BGP category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import clear_soft_in
    from . import clear_soft_out
    from . import soft_reset_neighbor


class Bgp:
    """Type stub for Bgp."""

    clear_soft_in: clear_soft_in.ClearSoftIn
    clear_soft_out: clear_soft_out.ClearSoftOut
    soft_reset_neighbor: soft_reset_neighbor.SoftResetNeighbor

    def __init__(self, client: IHTTPClient) -> None: ...
