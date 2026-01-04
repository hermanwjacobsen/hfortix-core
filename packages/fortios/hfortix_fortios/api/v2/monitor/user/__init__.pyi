"""Type stubs for USER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import banned
    from . import collected_email
    from . import device
    from . import firewall
    from . import fortitoken
    from . import fortitoken_cloud
    from . import fsso
    from . import guest
    from . import info
    from . import local
    from . import password_policy_conform
    from . import proxy
    from . import query
    from . import radius
    from . import scim
    from . import tacacs_plus


class User:
    """Type stub for User."""

    banned: banned.Banned
    device: device.Device
    firewall: firewall.Firewall
    fortitoken: fortitoken.Fortitoken
    fortitoken_cloud: fortitoken_cloud.FortitokenCloud
    fsso: fsso.Fsso
    guest: guest.Guest
    info: info.Info
    local: local.Local
    password_policy_conform: password_policy_conform.PasswordPolicyConform
    query: query.Query
    radius: radius.Radius
    scim: scim.Scim
    tacacs_plus: tacacs_plus.TacacsPlus
    collected_email: collected_email.CollectedEmail
    proxy: proxy.Proxy

    def __init__(self, client: IHTTPClient) -> None: ...
