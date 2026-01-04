"""Type stubs for SNMP category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import community
    from . import mib_view
    from . import rmon_stat
    from . import sysinfo
    from . import user


class Snmp:
    """Type stub for Snmp."""

    community: community.Community
    mib_view: mib_view.MibView
    rmon_stat: rmon_stat.RmonStat
    sysinfo: sysinfo.Sysinfo
    user: user.User

    def __init__(self, client: IHTTPClient) -> None: ...
