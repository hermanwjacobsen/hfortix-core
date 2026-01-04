"""Type stubs for MONITOR category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import azure
    from . import casb
    from . import endpoint_control
    from . import extender_controller
    from . import extension_controller
    from . import firewall
    from . import firmware
    from . import fortiguard
    from . import fortiview
    from . import geoip
    from . import ips
    from . import license
    from . import log
    from . import network
    from . import registration
    from . import router
    from . import sdwan
    from . import service
    from . import switch_controller
    from . import system
    from . import user
    from . import utm
    from . import videofilter
    from . import virtual_wan
    from . import vpn
    from . import vpn_certificate
    from . import wanopt
    from . import web_ui
    from . import webcache
    from . import webfilter
    from . import webproxy
    from . import wifi


class Monitor:
    """Type stub for Monitor."""

    azure: azure.Azure
    casb: casb.Casb
    endpoint_control: endpoint_control.EndpointControl
    extender_controller: extender_controller.ExtenderController
    extension_controller: extension_controller.ExtensionController
    firewall: firewall.Firewall
    firmware: firmware.Firmware
    fortiguard: fortiguard.Fortiguard
    fortiview: fortiview.Fortiview
    geoip: geoip.Geoip
    ips: ips.Ips
    license: license.License
    log: log.Log
    network: network.Network
    registration: registration.Registration
    router: router.Router
    sdwan: sdwan.Sdwan
    service: service.Service
    switch_controller: switch_controller.SwitchController
    system: system.System
    user: user.User
    utm: utm.Utm
    videofilter: videofilter.Videofilter
    virtual_wan: virtual_wan.VirtualWan
    vpn: vpn.Vpn
    vpn_certificate: vpn_certificate.VpnCertificate
    wanopt: wanopt.Wanopt
    web_ui: web_ui.WebUi
    webcache: webcache.Webcache
    webfilter: webfilter.Webfilter
    webproxy: webproxy.Webproxy
    wifi: wifi.Wifi

    def __init__(self, client: IHTTPClient) -> None: ...
