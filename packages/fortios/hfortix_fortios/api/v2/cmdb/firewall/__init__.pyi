"""Type stubs for FIREWALL category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import DoS_policy
    from . import DoS_policy6
    from . import access_proxy
    from . import access_proxy6
    from . import access_proxy_ssh_client_cert
    from . import access_proxy_virtual_host
    from . import address
    from . import address6
    from . import address6_template
    from . import addrgrp
    from . import addrgrp6
    from . import auth_portal
    from . import central_snat_map
    from . import city
    from . import country
    from . import decrypted_traffic_mirror
    from . import dnstranslation
    from . import global_setting
    from . import identity_based_route
    from . import interface_policy
    from . import interface_policy6
    from . import internet_service
    from . import internet_service_addition
    from . import internet_service_append
    from . import internet_service_botnet
    from . import internet_service_custom
    from . import internet_service_custom_group
    from . import internet_service_definition
    from . import internet_service_extension
    from . import internet_service_fortiguard
    from . import internet_service_group
    from . import internet_service_ipbl_reason
    from . import internet_service_ipbl_vendor
    from . import internet_service_list
    from . import internet_service_name
    from . import internet_service_owner
    from . import internet_service_reputation
    from . import internet_service_sld
    from . import internet_service_subapp
    from . import ip_translation
    from . import ipmacbinding
    from . import ippool
    from . import ippool6
    from . import ldb_monitor
    from . import local_in_policy
    from . import local_in_policy6
    from . import multicast_address
    from . import multicast_address6
    from . import multicast_policy
    from . import multicast_policy6
    from . import network_service_dynamic
    from . import on_demand_sniffer
    from . import policy
    from . import profile_group
    from . import profile_protocol_options
    from . import proxy_address
    from . import proxy_addrgrp
    from . import proxy_policy
    from . import region
    from . import schedule
    from . import security_policy
    from . import service
    from . import shaper
    from . import shaping_policy
    from . import shaping_profile
    from . import sniffer
    from . import ssh
    from . import ssl
    from . import ssl_server
    from . import ssl_ssh_profile
    from . import traffic_class
    from . import ttl_policy
    from . import vendor_mac
    from . import vendor_mac_summary
    from . import vip
    from . import vip6
    from . import vipgrp
    from . import vipgrp6
    from . import wildcard_fqdn


class Firewall:
    """Type stub for Firewall."""

    ipmacbinding: ipmacbinding.Ipmacbinding
    schedule: schedule.Schedule
    service: service.Service
    shaper: shaper.Shaper
    ssh: ssh.Ssh
    ssl: ssl.Ssl
    wildcard_fqdn: wildcard_fqdn.WildcardFqdn
    DoS_policy: DoS_policy.DosPolicy
    DoS_policy6: DoS_policy6.DosPolicy6
    access_proxy: access_proxy.AccessProxy
    access_proxy6: access_proxy6.AccessProxy6
    access_proxy_ssh_client_cert: access_proxy_ssh_client_cert.AccessProxySshClientCert
    access_proxy_virtual_host: access_proxy_virtual_host.AccessProxyVirtualHost
    address: address.Address
    address6: address6.Address6
    address6_template: address6_template.Address6Template
    addrgrp: addrgrp.Addrgrp
    addrgrp6: addrgrp6.Addrgrp6
    auth_portal: auth_portal.AuthPortal
    central_snat_map: central_snat_map.CentralSnatMap
    city: city.City
    country: country.Country
    decrypted_traffic_mirror: decrypted_traffic_mirror.DecryptedTrafficMirror
    dnstranslation: dnstranslation.Dnstranslation
    global_setting: global_setting.GlobalSetting
    identity_based_route: identity_based_route.IdentityBasedRoute
    interface_policy: interface_policy.InterfacePolicy
    interface_policy6: interface_policy6.InterfacePolicy6
    internet_service: internet_service.InternetService
    internet_service_addition: internet_service_addition.InternetServiceAddition
    internet_service_append: internet_service_append.InternetServiceAppend
    internet_service_botnet: internet_service_botnet.InternetServiceBotnet
    internet_service_custom: internet_service_custom.InternetServiceCustom
    internet_service_custom_group: internet_service_custom_group.InternetServiceCustomGroup
    internet_service_definition: internet_service_definition.InternetServiceDefinition
    internet_service_extension: internet_service_extension.InternetServiceExtension
    internet_service_fortiguard: internet_service_fortiguard.InternetServiceFortiguard
    internet_service_group: internet_service_group.InternetServiceGroup
    internet_service_ipbl_reason: internet_service_ipbl_reason.InternetServiceIpblReason
    internet_service_ipbl_vendor: internet_service_ipbl_vendor.InternetServiceIpblVendor
    internet_service_list: internet_service_list.InternetServiceList
    internet_service_name: internet_service_name.InternetServiceName
    internet_service_owner: internet_service_owner.InternetServiceOwner
    internet_service_reputation: internet_service_reputation.InternetServiceReputation
    internet_service_sld: internet_service_sld.InternetServiceSld
    internet_service_subapp: internet_service_subapp.InternetServiceSubapp
    ip_translation: ip_translation.IpTranslation
    ippool: ippool.Ippool
    ippool6: ippool6.Ippool6
    ldb_monitor: ldb_monitor.LdbMonitor
    local_in_policy: local_in_policy.LocalInPolicy
    local_in_policy6: local_in_policy6.LocalInPolicy6
    multicast_address: multicast_address.MulticastAddress
    multicast_address6: multicast_address6.MulticastAddress6
    multicast_policy: multicast_policy.MulticastPolicy
    multicast_policy6: multicast_policy6.MulticastPolicy6
    network_service_dynamic: network_service_dynamic.NetworkServiceDynamic
    on_demand_sniffer: on_demand_sniffer.OnDemandSniffer
    policy: policy.Policy
    profile_group: profile_group.ProfileGroup
    profile_protocol_options: profile_protocol_options.ProfileProtocolOptions
    proxy_address: proxy_address.ProxyAddress
    proxy_addrgrp: proxy_addrgrp.ProxyAddrgrp
    proxy_policy: proxy_policy.ProxyPolicy
    region: region.Region
    security_policy: security_policy.SecurityPolicy
    shaping_policy: shaping_policy.ShapingPolicy
    shaping_profile: shaping_profile.ShapingProfile
    sniffer: sniffer.Sniffer
    ssl_server: ssl_server.SslServer
    ssl_ssh_profile: ssl_ssh_profile.SslSshProfile
    traffic_class: traffic_class.TrafficClass
    ttl_policy: ttl_policy.TtlPolicy
    vendor_mac: vendor_mac.VendorMac
    vendor_mac_summary: vendor_mac_summary.VendorMacSummary
    vip: vip.Vip
    vip6: vip6.Vip6
    vipgrp: vipgrp.Vipgrp
    vipgrp6: vipgrp6.Vipgrp6

    def __init__(self, client: IHTTPClient) -> None: ...
