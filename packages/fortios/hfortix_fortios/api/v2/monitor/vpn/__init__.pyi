"""Type stubs for VPN category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import ike
    from . import ipsec
    from . import ssl


class Vpn:
    """Type stub for Vpn."""

    ike: ike.Ike
    ipsec: ipsec.Ipsec
    ssl: ssl.Ssl

    def __init__(self, client: IHTTPClient) -> None: ...
