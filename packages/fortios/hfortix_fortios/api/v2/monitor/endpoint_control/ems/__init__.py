"""FortiOS CMDB - Ems category"""

from .cert_status import CertStatus
from .status import Status
from .unverify_cert import UnverifyCert
from .verify_cert import VerifyCert

__all__ = [
    "CertStatus",
    "Ems",
    "Status",
    "UnverifyCert",
    "VerifyCert",
]


class Ems:
    """Ems endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Ems endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.cert_status = CertStatus(client)
        self.status = Status(client)
        self.unverify_cert = UnverifyCert(client)
        self.verify_cert = VerifyCert(client)
