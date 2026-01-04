"""
FortiOS API v2 - cmdb endpoints.

Auto-generated from FortiOS 7.6 schemas.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient


class CMDB:
    """CMDB category endpoints."""
    
    def __init__(self, client: "IHTTPClient"):
        """Initialize CMDB endpoints."""
        from . import (
            alertemail,
            antivirus,
            application,
            authentication,
            automation,
            casb,
            certificate,
            diameter_filter,
            dlp,
            dnsfilter,
            emailfilter,
            endpoint_control,
            extension_controller,
            file_filter,
            firewall,
            ftp_proxy,
            icap,
            ips,
            log,
            report,
            router,
            rule,
            sctp_filter,
            switch_controller,
            system,
            user,
            videofilter,
            virtual_patch,
            voip,
            vpn,
            waf,
            web_proxy,
            webfilter,
            wireless_controller,
            ztna,
        )
        
        self.alertemail = alertemail.Alertemail(client)
        self.antivirus = antivirus.Antivirus(client)
        self.application = application.Application(client)
        self.authentication = authentication.Authentication(client)
        self.automation = automation.Automation(client)
        self.casb = casb.Casb(client)
        self.certificate = certificate.Certificate(client)
        self.diameter_filter = diameter_filter.DiameterFilter(client)
        self.dlp = dlp.Dlp(client)
        self.dnsfilter = dnsfilter.Dnsfilter(client)
        self.emailfilter = emailfilter.Emailfilter(client)
        self.endpoint_control = endpoint_control.EndpointControl(client)
        self.extension_controller = extension_controller.ExtensionController(client)
        self.file_filter = file_filter.FileFilter(client)
        self.firewall = firewall.Firewall(client)
        self.ftp_proxy = ftp_proxy.FtpProxy(client)
        self.icap = icap.Icap(client)
        self.ips = ips.Ips(client)
        self.log = log.Log(client)
        self.report = report.Report(client)
        self.router = router.Router(client)
        self.rule = rule.Rule(client)
        self.sctp_filter = sctp_filter.SctpFilter(client)
        self.switch_controller = switch_controller.SwitchController(client)
        self.system = system.System(client)
        self.user = user.User(client)
        self.videofilter = videofilter.Videofilter(client)
        self.virtual_patch = virtual_patch.VirtualPatch(client)
        self.voip = voip.Voip(client)
        self.vpn = vpn.Vpn(client)
        self.waf = waf.Waf(client)
        self.web_proxy = web_proxy.WebProxy(client)
        self.webfilter = webfilter.Webfilter(client)
        self.wireless_controller = wireless_controller.WirelessController(client)
        self.ztna = ztna.Ztna(client)


__all__ = ["CMDB"]
