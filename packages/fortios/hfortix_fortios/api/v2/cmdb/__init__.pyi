"""Type stubs for CMDB category."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .alertemail import Alertemail as Alertemail
from .antivirus import Antivirus as Antivirus
from .application import Application as Application
from .authentication import Authentication as Authentication
from .automation import Automation as Automation
from .casb import Casb as Casb
from .certificate import Certificate as Certificate
from .diameter_filter import DiameterFilter as DiameterFilter
from .dlp import Dlp as Dlp
from .dnsfilter import Dnsfilter as Dnsfilter
from .emailfilter import Emailfilter as Emailfilter
from .endpoint_control import EndpointControl as EndpointControl
from .extension_controller import ExtensionController as ExtensionController
from .file_filter import FileFilter as FileFilter
from .firewall import Firewall as Firewall
from .ftp_proxy import FtpProxy as FtpProxy
from .icap import Icap as Icap
from .ips import Ips as Ips
from .log import Log as Log
from .report import Report as Report
from .router import Router as Router
from .rule import Rule as Rule
from .sctp_filter import SctpFilter as SctpFilter
from .switch_controller import SwitchController as SwitchController
from .system import System as System
from .user import User as User
from .videofilter import Videofilter as Videofilter
from .virtual_patch import VirtualPatch as VirtualPatch
from .voip import Voip as Voip
from .vpn import Vpn as Vpn
from .waf import Waf as Waf
from .web_proxy import WebProxy as WebProxy
from .webfilter import Webfilter as Webfilter
from .wireless_controller import WirelessController as WirelessController
from .ztna import Ztna as Ztna

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient


class CMDB:
    """Type stub for CMDB."""


    def __init__(self, client: IHTTPClient) -> None: ...
