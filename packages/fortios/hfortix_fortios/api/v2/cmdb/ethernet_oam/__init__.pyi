"""Type stubs for ETHERNET_OAM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import cfm


class EthernetOam:
    """Type stub for EthernetOam."""

    cfm: cfm.Cfm

    def __init__(self, client: IHTTPClient) -> None: ...
