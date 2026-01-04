"""Type stubs for NETWORK category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import arp
    from . import ddns
    from . import debug_flow
    from . import dns
    from . import fortiguard
    from . import lldp
    from . import reverse_ip_lookup


class Network:
    """Type stub for Network."""

    ddns: ddns.Ddns
    debug_flow: debug_flow.DebugFlow
    arp: arp.Arp
    dns: dns.Dns
    fortiguard: fortiguard.Fortiguard
    lldp: lldp.Lldp
    reverse_ip_lookup: reverse_ip_lookup.ReverseIpLookup

    def __init__(self, client: IHTTPClient) -> None: ...
