"""Type stubs for VIRTUAL_WAN category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import health_check
    from . import interface_log
    from . import members
    from . import sla_log
    from . import sladb


class VirtualWan:
    """Type stub for VirtualWan."""

    health_check: health_check.HealthCheck
    interface_log: interface_log.InterfaceLog
    members: members.Members
    sla_log: sla_log.SlaLog
    sladb: sladb.Sladb

    def __init__(self, client: IHTTPClient) -> None: ...
