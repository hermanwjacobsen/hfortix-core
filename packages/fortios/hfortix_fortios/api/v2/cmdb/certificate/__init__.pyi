"""Type stubs for CERTIFICATE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import ca
    from . import crl
    from . import hsm_local
    from . import local
    from . import remote


class Certificate:
    """Type stub for Certificate."""

    ca: ca.Ca
    crl: crl.Crl
    hsm_local: hsm_local.HsmLocal
    local: local.Local
    remote: remote.Remote

    def __init__(self, client: IHTTPClient) -> None: ...
