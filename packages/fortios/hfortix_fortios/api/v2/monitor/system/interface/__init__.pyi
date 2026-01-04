"""Type stubs for INTERFACE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import dhcp_renew
    from . import dhcp_status
    from . import poe
    from . import poe_usage
    from . import speed_test_status
    from . import speed_test_trigger
    from . import transceivers
    from . import wake_on_lan


class Interface:
    """Type stub for Interface."""

    dhcp_renew: dhcp_renew.DhcpRenew
    dhcp_status: dhcp_status.DhcpStatus
    poe: poe.Poe
    poe_usage: poe_usage.PoeUsage
    speed_test_status: speed_test_status.SpeedTestStatus
    speed_test_trigger: speed_test_trigger.SpeedTestTrigger
    transceivers: transceivers.Transceivers
    wake_on_lan: wake_on_lan.WakeOnLan

    def __init__(self, client: IHTTPClient) -> None: ...
