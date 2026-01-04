"""Type stubs for ROUTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import bgp
    from . import charts
    from . import ipv4
    from . import ipv6
    from . import lookup
    from . import lookup_policy
    from . import ospf
    from . import policy
    from . import policy6
    from . import sdwan
    from . import statistics


class Router:
    """Type stub for Router."""

    bgp: bgp.Bgp
    lookup: lookup.Lookup
    charts: charts.Charts
    ipv4: ipv4.Ipv4
    ipv6: ipv6.Ipv6
    lookup_policy: lookup_policy.LookupPolicy
    ospf: ospf.Ospf
    policy: policy.Policy
    policy6: policy6.Policy6
    sdwan: sdwan.Sdwan
    statistics: statistics.Statistics

    def __init__(self, client: IHTTPClient) -> None: ...
