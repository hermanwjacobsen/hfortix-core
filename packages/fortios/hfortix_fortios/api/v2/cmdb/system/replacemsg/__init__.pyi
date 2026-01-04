"""Type stubs for REPLACEMSG category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import admin
    from . import alertmail
    from . import auth
    from . import automation
    from . import fortiguard_wf
    from . import http
    from . import mail
    from . import nac_quar
    from . import spam
    from . import sslvpn
    from . import traffic_quota
    from . import utm


class Replacemsg:
    """Type stub for Replacemsg."""

    admin: admin.Admin
    alertmail: alertmail.Alertmail
    auth: auth.Auth
    automation: automation.Automation
    fortiguard_wf: fortiguard_wf.FortiguardWf
    http: http.Http
    mail: mail.Mail
    nac_quar: nac_quar.NacQuar
    spam: spam.Spam
    sslvpn: sslvpn.Sslvpn
    traffic_quota: traffic_quota.TrafficQuota
    utm: utm.Utm

    def __init__(self, client: IHTTPClient) -> None: ...
