"""FortiOS CMDB - Vpn category"""

from .certificate_ca import CertificateCa
from .certificate_crl import CertificateCrl
from .certificate_hsm_local import CertificateHsmLocal
from .certificate_local import CertificateLocal
from .certificate_ocsp_server import CertificateOcspServer
from .certificate_remote import CertificateRemote
from .certificate_setting import CertificateSetting
from .ipsec_concentrator import IpsecConcentrator
from .ipsec_fec import IpsecFec
from .ipsec_manualkey import IpsecManualkey
from .ipsec_manualkey_interface import IpsecManualkeyInterface
from .ipsec_phase1 import IpsecPhase1
from .ipsec_phase1_interface import IpsecPhase1Interface
from .ipsec_phase2 import IpsecPhase2
from .ipsec_phase2_interface import IpsecPhase2Interface
from .kmip_server import KmipServer
from .l2tp import L2tp
from .pptp import Pptp
from .qkd import Qkd

__all__ = [
    "CertificateCa",
    "CertificateCrl",
    "CertificateHsmLocal",
    "CertificateLocal",
    "CertificateOcspServer",
    "CertificateRemote",
    "CertificateSetting",
    "IpsecConcentrator",
    "IpsecFec",
    "IpsecManualkey",
    "IpsecManualkeyInterface",
    "IpsecPhase1",
    "IpsecPhase1Interface",
    "IpsecPhase2",
    "IpsecPhase2Interface",
    "KmipServer",
    "L2tp",
    "Pptp",
    "Qkd",
    "Vpn",
]


class Vpn:
    """Vpn endpoints wrapper for CMDB API."""

    def __init__(self, client):
        """Vpn endpoints.
        
        Args:
            client: HTTP client instance for API communication
        """
        self.certificate_ca = CertificateCa(client)
        self.certificate_crl = CertificateCrl(client)
        self.certificate_hsm_local = CertificateHsmLocal(client)
        self.certificate_local = CertificateLocal(client)
        self.certificate_ocsp_server = CertificateOcspServer(client)
        self.certificate_remote = CertificateRemote(client)
        self.certificate_setting = CertificateSetting(client)
        self.ipsec_concentrator = IpsecConcentrator(client)
        self.ipsec_fec = IpsecFec(client)
        self.ipsec_manualkey = IpsecManualkey(client)
        self.ipsec_manualkey_interface = IpsecManualkeyInterface(client)
        self.ipsec_phase1 = IpsecPhase1(client)
        self.ipsec_phase1_interface = IpsecPhase1Interface(client)
        self.ipsec_phase2 = IpsecPhase2(client)
        self.ipsec_phase2_interface = IpsecPhase2Interface(client)
        self.kmip_server = KmipServer(client)
        self.l2tp = L2tp(client)
        self.pptp = Pptp(client)
        self.qkd = Qkd(client)
