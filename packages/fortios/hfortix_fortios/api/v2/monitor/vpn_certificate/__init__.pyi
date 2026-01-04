"""Type stubs for VPN_CERTIFICATE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import ca
    from . import cert_name_available
    from . import crl
    from . import csr
    from . import local
    from . import remote


class VpnCertificate:
    """Type stub for VpnCertificate."""

    ca: ca.Ca
    crl: crl.Crl
    csr: csr.Csr
    local: local.Local
    remote: remote.Remote
    cert_name_available: cert_name_available.CertNameAvailable

    def __init__(self, client: IHTTPClient) -> None: ...
