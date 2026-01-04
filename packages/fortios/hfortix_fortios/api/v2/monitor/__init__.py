"""
FortiOS API v2 - monitor endpoints.

Auto-generated from FortiOS 7.6 schemas.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .azure import Azure
from .casb import Casb
from .endpoint_control import EndpointControl
# TEMP DISABLED: # TEMP DISABLED: from .extender_controller import ExtenderController
from .firewall import Firewall
from .fortiguard import Fortiguard
from .fortiview import Fortiview
from .geoip import Geoip
from .ips import Ips
from .license import License
from .log import Log
from .network import Network
from .registration import Registration
from .router import Router
from .sdwan import Sdwan
from .service import Service
from .switch_controller import SwitchController
from .system import System
from .user import User
from .utm import Utm
from .videofilter import Videofilter
from .virtual_wan import VirtualWan
from .vpn import Vpn
from .vpn_certificate import VpnCertificate
from .wanopt import Wanopt
from .web_ui import WebUi
from .webcache import Webcache
from .webfilter import Webfilter
from .webproxy import Webproxy
from .wifi import Wifi


class Monitor:
    """Monitor category endpoints."""
    
    def __init__(self, client: "IHTTPClient"):
        """Initialize Monitor endpoints."""
        self.azure = Azure(client)
        self.casb = Casb(client)
        self.endpoint_control = EndpointControl(client)
# TEMP DISABLED: # TEMP DISABLED:         self.extender_controller = ExtenderController(client)
        self.firewall = Firewall(client)
        self.fortiguard = Fortiguard(client)
        self.fortiview = Fortiview(client)
        self.geoip = Geoip(client)
        self.ips = Ips(client)
        self.license = License(client)
        self.log = Log(client)
        self.network = Network(client)
        self.registration = Registration(client)
        self.router = Router(client)
        self.sdwan = Sdwan(client)
        self.service = Service(client)
        self.switch_controller = SwitchController(client)
        self.system = System(client)
        self.user = User(client)
        self.utm = Utm(client)
        self.videofilter = Videofilter(client)
        self.virtual_wan = VirtualWan(client)
        self.vpn = Vpn(client)
        self.vpn_certificate = VpnCertificate(client)
        self.wanopt = Wanopt(client)
        self.web_ui = WebUi(client)
        self.webcache = Webcache(client)
        self.webfilter = Webfilter(client)
        self.webproxy = Webproxy(client)
        self.wifi = Wifi(client)


__all__ = ["Monitor"]
