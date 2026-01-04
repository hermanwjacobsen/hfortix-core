"""Type stubs for IPAM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import utilization


class Ipam:
    """Type stub for Ipam."""

    utilization: utilization.Utilization

    def __init__(self, client: IHTTPClient) -> None: ...
