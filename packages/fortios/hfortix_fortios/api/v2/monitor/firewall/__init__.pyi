"""Type stubs for FIREWALL category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import acl
    from . import acl6
    from . import address6_dynamic
    from . import address_dynamic
    from . import address_fqdns
    from . import address_fqdns6
    from . import central_snat_map
    from . import check_addrgrp_exclude_mac_member
    from . import clearpass_address
    from . import dnat
    from . import gtp
    from . import gtp_runtime_statistics
    from . import gtp_statistics
    from . import health
    from . import internet_service_basic
    from . import internet_service_details
    from . import internet_service_fqdn
    from . import internet_service_fqdn_icon_ids
    from . import internet_service_match
    from . import internet_service_reputation
    from . import ippool
    from . import load_balance
    from . import local_in
    from . import local_in6
    from . import multicast_policy
    from . import multicast_policy6
    from . import network_service_dynamic
    from . import per_ip_shaper
    from . import policy
    from . import policy_lookup
    from . import proxy
    from . import proxy_policy
    from . import saas_application
    from . import sdn_connector_filters
    from . import security_policy
    from . import session
    from . import session6
    from . import sessions
    from . import shaper
    from . import uuid_list
    from . import uuid_type_lookup
    from . import vip_overlap
    from . import ztna_firewall_policy


class Firewall:
    """Type stub for Firewall."""

    acl: acl.Acl
    acl6: acl6.Acl6
    central_snat_map: central_snat_map.CentralSnatMap
    clearpass_address: clearpass_address.ClearpassAddress
    dnat: dnat.Dnat
    gtp: gtp.Gtp
    ippool: ippool.Ippool
    multicast_policy: multicast_policy.MulticastPolicy
    multicast_policy6: multicast_policy6.MulticastPolicy6
    per_ip_shaper: per_ip_shaper.PerIpShaper
    policy: policy.Policy
    proxy: proxy.Proxy
    proxy_policy: proxy_policy.ProxyPolicy
    security_policy: security_policy.SecurityPolicy
    session: session.Session
    session6: session6.Session6
    shaper: shaper.Shaper
    ztna_firewall_policy: ztna_firewall_policy.ZtnaFirewallPolicy
    address6_dynamic: address6_dynamic.Address6Dynamic
    address_dynamic: address_dynamic.AddressDynamic
    address_fqdns: address_fqdns.AddressFqdns
    address_fqdns6: address_fqdns6.AddressFqdns6
    check_addrgrp_exclude_mac_member: check_addrgrp_exclude_mac_member.CheckAddrgrpExcludeMacMember
    gtp_runtime_statistics: gtp_runtime_statistics.GtpRuntimeStatistics
    gtp_statistics: gtp_statistics.GtpStatistics
    health: health.Health
    internet_service_basic: internet_service_basic.InternetServiceBasic
    internet_service_details: internet_service_details.InternetServiceDetails
    internet_service_fqdn: internet_service_fqdn.InternetServiceFqdn
    internet_service_fqdn_icon_ids: internet_service_fqdn_icon_ids.InternetServiceFqdnIconIds
    internet_service_match: internet_service_match.InternetServiceMatch
    internet_service_reputation: internet_service_reputation.InternetServiceReputation
    load_balance: load_balance.LoadBalance
    local_in: local_in.LocalIn
    local_in6: local_in6.LocalIn6
    network_service_dynamic: network_service_dynamic.NetworkServiceDynamic
    policy_lookup: policy_lookup.PolicyLookup
    saas_application: saas_application.SaasApplication
    sdn_connector_filters: sdn_connector_filters.SdnConnectorFilters
    sessions: sessions.Sessions
    uuid_list: uuid_list.UuidList
    uuid_type_lookup: uuid_type_lookup.UuidTypeLookup
    vip_overlap: vip_overlap.VipOverlap

    def __init__(self, client: IHTTPClient) -> None: ...
