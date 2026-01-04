"""Type stubs for MONITOR category."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .azure import Azure as Azure
from .casb import Casb as Casb
from .endpoint_control import EndpointControl as EndpointControl
from .extender_controller import ExtenderController as ExtenderController
from .firewall import Firewall as Firewall
from .fortiguard import Fortiguard as Fortiguard
from .fortiview import Fortiview as Fortiview
from .geoip import Geoip as Geoip
from .ips import Ips as Ips
from .license import License as License
from .log import Log as Log
from .network import Network as Network
from .registration import Registration as Registration
from .router import Router as Router
from .sdwan import Sdwan as Sdwan
from .service import Service as Service
from .switch_controller import SwitchController as SwitchController
from .system import System as System
from .user import User as User
from .utm import Utm as Utm
from .videofilter import Videofilter as Videofilter
from .virtual_wan import VirtualWan as VirtualWan
from .vpn import Vpn as Vpn
from .vpn_certificate import VpnCertificate as VpnCertificate
from .wanopt import Wanopt as Wanopt
from .web_ui import WebUi as WebUi
from .webcache import Webcache as Webcache
from .webfilter import Webfilter as Webfilter
from .webproxy import Webproxy as Webproxy
from .wifi import Wifi as Wifi

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient


class Monitor:
    """Type stub for Monitor."""

    azure: Azure
    casb: Casb
    endpoint_control: EndpointControl
    extender_controller: ExtenderController
    firewall: Firewall
    fortiguard: Fortiguard
    fortiview: Fortiview
    geoip: Geoip
    ips: Ips
    license: License
    log: Log
    network: Network
    registration: Registration
    router: Router
    sdwan: Sdwan
    service: Service
    switch_controller: SwitchController
    system: System
    user: User
    utm: Utm
    videofilter: Videofilter
    virtual_wan: VirtualWan
    vpn: Vpn
    vpn_certificate: VpnCertificate
    wanopt: Wanopt
    web_ui: WebUi
    webcache: Webcache
    webfilter: Webfilter
    webproxy: Webproxy
    wifi: Wifi

    def __init__(self, client: IHTTPClient) -> None: ...
