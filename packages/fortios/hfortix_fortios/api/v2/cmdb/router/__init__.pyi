"""Type stubs for ROUTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import access_list
    from . import access_list6
    from . import aspath_list
    from . import auth_path
    from . import bfd
    from . import bfd6
    from . import bgp
    from . import community_list
    from . import extcommunity_list
    from . import isis
    from . import key_chain
    from . import multicast
    from . import multicast6
    from . import multicast_flow
    from . import ospf
    from . import ospf6
    from . import policy
    from . import policy6
    from . import prefix_list
    from . import prefix_list6
    from . import rip
    from . import ripng
    from . import route_map
    from . import setting
    from . import static
    from . import static6


class Router:
    """Type stub for Router."""

    access_list: access_list.AccessList
    access_list6: access_list6.AccessList6
    aspath_list: aspath_list.AspathList
    auth_path: auth_path.AuthPath
    bfd: bfd.Bfd
    bfd6: bfd6.Bfd6
    bgp: bgp.Bgp
    community_list: community_list.CommunityList
    extcommunity_list: extcommunity_list.ExtcommunityList
    isis: isis.Isis
    key_chain: key_chain.KeyChain
    multicast: multicast.Multicast
    multicast6: multicast6.Multicast6
    multicast_flow: multicast_flow.MulticastFlow
    ospf: ospf.Ospf
    ospf6: ospf6.Ospf6
    policy: policy.Policy
    policy6: policy6.Policy6
    prefix_list: prefix_list.PrefixList
    prefix_list6: prefix_list6.PrefixList6
    rip: rip.Rip
    ripng: ripng.Ripng
    route_map: route_map.RouteMap
    setting: setting.Setting
    static: static.Static
    static6: static6.Static6

    def __init__(self, client: IHTTPClient) -> None: ...
