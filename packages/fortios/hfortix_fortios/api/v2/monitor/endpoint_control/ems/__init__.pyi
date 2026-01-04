"""Type stubs for EMS category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import cert_status
    from . import status
    from . import unverify_cert
    from . import verify_cert


class Ems:
    """Type stub for Ems."""

    cert_status: cert_status.CertStatus
    status: status.Status
    unverify_cert: unverify_cert.UnverifyCert
    verify_cert: verify_cert.VerifyCert

    def __init__(self, client: IHTTPClient) -> None: ...
