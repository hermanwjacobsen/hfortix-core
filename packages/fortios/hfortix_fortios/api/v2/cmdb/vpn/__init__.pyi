"""Type stubs for VPN category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import certificate
    from . import ipsec
    from . import kmip_server
    from . import l2tp
    from . import pptp
    from . import qkd


class Vpn:
    """Type stub for Vpn."""

    certificate: certificate.Certificate
    ipsec: ipsec.Ipsec
    kmip_server: kmip_server.KmipServer
    l2tp: l2tp.L2tp
    pptp: pptp.Pptp
    qkd: qkd.Qkd

    def __init__(self, client: IHTTPClient) -> None: ...
