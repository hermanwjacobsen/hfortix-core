""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/policy
Category: cmdb
"""

from __future__ import annotations

from typing import (
    Any,
    ClassVar,
    Literal,
    TypedDict,
    overload,
)

from hfortix_fortios.models import (
    FortiObject,
    FortiObjectList,
)


# ================================================================
# TypedDict Payloads
# ================================================================

class PolicySrcintfItem:
    """Nested item for srcintf field - supports attribute access."""
    name: str


class PolicyDstintfItem:
    """Nested item for dstintf field - supports attribute access."""
    name: str


class PolicySrcaddrItem:
    """Nested item for srcaddr field - supports attribute access."""
    name: str


class PolicyDstaddrItem:
    """Nested item for dstaddr field - supports attribute access."""
    name: str


class PolicySrcaddr6Item:
    """Nested item for srcaddr6 field - supports attribute access."""
    name: str


class PolicyDstaddr6Item:
    """Nested item for dstaddr6 field - supports attribute access."""
    name: str


class PolicyZtnaemstagItem:
    """Nested item for ztna-ems-tag field - supports attribute access."""
    name: str


class PolicyZtnaemstagsecondaryItem:
    """Nested item for ztna-ems-tag-secondary field - supports attribute access."""
    name: str


class PolicyZtnageotagItem:
    """Nested item for ztna-geo-tag field - supports attribute access."""
    name: str


class PolicyInternetservicenameItem:
    """Nested item for internet-service-name field - supports attribute access."""
    name: str


class PolicyInternetservicegroupItem:
    """Nested item for internet-service-group field - supports attribute access."""
    name: str


class PolicyInternetservicecustomItem:
    """Nested item for internet-service-custom field - supports attribute access."""
    name: str


class PolicyNetworkservicedynamicItem:
    """Nested item for network-service-dynamic field - supports attribute access."""
    name: str


class PolicyInternetservicecustomgroupItem:
    """Nested item for internet-service-custom-group field - supports attribute access."""
    name: str


class PolicyInternetservicesrcnameItem:
    """Nested item for internet-service-src-name field - supports attribute access."""
    name: str


class PolicyInternetservicesrcgroupItem:
    """Nested item for internet-service-src-group field - supports attribute access."""
    name: str


class PolicyInternetservicesrccustomItem:
    """Nested item for internet-service-src-custom field - supports attribute access."""
    name: str


class PolicyNetworkservicesrcdynamicItem:
    """Nested item for network-service-src-dynamic field - supports attribute access."""
    name: str


class PolicyInternetservicesrccustomgroupItem:
    """Nested item for internet-service-src-custom-group field - supports attribute access."""
    name: str


class PolicySrcvendormacItem:
    """Nested item for src-vendor-mac field - supports attribute access."""
    id: int


class PolicyInternetservice6nameItem:
    """Nested item for internet-service6-name field - supports attribute access."""
    name: str


class PolicyInternetservice6groupItem:
    """Nested item for internet-service6-group field - supports attribute access."""
    name: str


class PolicyInternetservice6customItem:
    """Nested item for internet-service6-custom field - supports attribute access."""
    name: str


class PolicyInternetservice6customgroupItem:
    """Nested item for internet-service6-custom-group field - supports attribute access."""
    name: str


class PolicyInternetservice6srcnameItem:
    """Nested item for internet-service6-src-name field - supports attribute access."""
    name: str


class PolicyInternetservice6srcgroupItem:
    """Nested item for internet-service6-src-group field - supports attribute access."""
    name: str


class PolicyInternetservice6srccustomItem:
    """Nested item for internet-service6-src-custom field - supports attribute access."""
    name: str


class PolicyInternetservice6srccustomgroupItem:
    """Nested item for internet-service6-src-custom-group field - supports attribute access."""
    name: str


class PolicyRtpaddrItem:
    """Nested item for rtp-addr field - supports attribute access."""
    name: str


class PolicyServiceItem:
    """Nested item for service field - supports attribute access."""
    name: str


class PolicyPcppoolnameItem:
    """Nested item for pcp-poolname field - supports attribute access."""
    name: str


class PolicyPoolnameItem:
    """Nested item for poolname field - supports attribute access."""
    name: str


class PolicyPoolname6Item:
    """Nested item for poolname6 field - supports attribute access."""
    name: str


class PolicyNtlmenabledbrowsersItem:
    """Nested item for ntlm-enabled-browsers field - supports attribute access."""
    user_agent_string: str


class PolicyGroupsItem:
    """Nested item for groups field - supports attribute access."""
    name: str


class PolicyUsersItem:
    """Nested item for users field - supports attribute access."""
    name: str


class PolicyFssogroupsItem:
    """Nested item for fsso-groups field - supports attribute access."""
    name: str


class PolicyCustomlogfieldsItem:
    """Nested item for custom-log-fields field - supports attribute access."""
    field_id: str


class PolicySgtItem:
    """Nested item for sgt field - supports attribute access."""
    id: int


class PolicyInternetservicefortiguardItem:
    """Nested item for internet-service-fortiguard field - supports attribute access."""
    name: str


class PolicyInternetservicesrcfortiguardItem:
    """Nested item for internet-service-src-fortiguard field - supports attribute access."""
    name: str


class PolicyInternetservice6fortiguardItem:
    """Nested item for internet-service6-fortiguard field - supports attribute access."""
    name: str


class PolicyInternetservice6srcfortiguardItem:
    """Nested item for internet-service6-src-fortiguard field - supports attribute access."""
    name: str


class PolicyPayload(TypedDict, total=False):
    """Payload type for Policy operations."""
    policyid: int
    status: Literal["enable", "disable"]
    name: str
    uuid: str
    srcintf: str | list[str] | list[dict[str, Any]] | list[PolicySrcintfItem]
    dstintf: str | list[str] | list[dict[str, Any]] | list[PolicyDstintfItem]
    action: Literal["accept", "deny", "ipsec"]
    nat64: Literal["enable", "disable"]
    nat46: Literal["enable", "disable"]
    ztna_status: Literal["enable", "disable"]
    ztna_device_ownership: Literal["enable", "disable"]
    srcaddr: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddrItem]
    dstaddr: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddrItem]
    srcaddr6: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddr6Item]
    dstaddr6: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddr6Item]
    ztna_ems_tag: str | list[str] | list[dict[str, Any]] | list[PolicyZtnaemstagItem]
    ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | list[PolicyZtnaemstagsecondaryItem]
    ztna_tags_match_logic: Literal["or", "and"]
    ztna_geo_tag: str | list[str] | list[dict[str, Any]] | list[PolicyZtnageotagItem]
    internet_service: Literal["enable", "disable"]
    internet_service_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicenameItem]
    internet_service_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicegroupItem]
    internet_service_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomItem]
    network_service_dynamic: str | list[str] | list[dict[str, Any]] | list[PolicyNetworkservicedynamicItem]
    internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomgroupItem]
    internet_service_src: Literal["enable", "disable"]
    internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcnameItem]
    internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcgroupItem]
    internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrccustomItem]
    network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | list[PolicyNetworkservicesrcdynamicItem]
    internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrccustomgroupItem]
    reputation_minimum: int
    reputation_direction: Literal["source", "destination"]
    src_vendor_mac: str | list[str] | list[dict[str, Any]] | list[PolicySrcvendormacItem]
    internet_service6: Literal["enable", "disable"]
    internet_service6_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6nameItem]
    internet_service6_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6groupItem]
    internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6customItem]
    internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6customgroupItem]
    internet_service6_src: Literal["enable", "disable"]
    internet_service6_src_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcnameItem]
    internet_service6_src_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcgroupItem]
    internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srccustomItem]
    internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srccustomgroupItem]
    reputation_minimum6: int
    reputation_direction6: Literal["source", "destination"]
    rtp_nat: Literal["disable", "enable"]
    rtp_addr: str | list[str] | list[dict[str, Any]] | list[PolicyRtpaddrItem]
    send_deny_packet: Literal["disable", "enable"]
    firewall_session_dirty: Literal["check-all", "check-new"]
    schedule: str
    schedule_timeout: Literal["enable", "disable"]
    policy_expiry: Literal["enable", "disable"]
    policy_expiry_date: str
    policy_expiry_date_utc: str
    service: str | list[str] | list[dict[str, Any]] | list[PolicyServiceItem]
    tos_mask: str
    tos: str
    tos_negate: Literal["enable", "disable"]
    anti_replay: Literal["enable", "disable"]
    tcp_session_without_syn: Literal["all", "data-only", "disable"]
    geoip_anycast: Literal["enable", "disable"]
    geoip_match: Literal["physical-location", "registered-location"]
    dynamic_shaping: Literal["enable", "disable"]
    passive_wan_health_measurement: Literal["enable", "disable"]
    app_monitor: Literal["enable", "disable"]
    utm_status: Literal["enable", "disable"]
    inspection_mode: Literal["proxy", "flow"]
    http_policy_redirect: Literal["enable", "disable", "legacy"]
    ssh_policy_redirect: Literal["enable", "disable"]
    ztna_policy_redirect: Literal["enable", "disable"]
    webproxy_profile: str
    profile_type: Literal["single", "group"]
    profile_group: str
    profile_protocol_options: str
    ssl_ssh_profile: str
    av_profile: str
    webfilter_profile: str
    dnsfilter_profile: str
    emailfilter_profile: str
    dlp_profile: str
    file_filter_profile: str
    ips_sensor: str
    application_list: str
    voip_profile: str
    ips_voip_filter: str
    sctp_filter_profile: str
    diameter_filter_profile: str
    virtual_patch_profile: str
    icap_profile: str
    videofilter_profile: str
    waf_profile: str
    ssh_filter_profile: str
    casb_profile: str
    logtraffic: Literal["all", "utm", "disable"]
    logtraffic_start: Literal["enable", "disable"]
    log_http_transaction: Literal["enable", "disable"]
    capture_packet: Literal["enable", "disable"]
    auto_asic_offload: Literal["enable", "disable"]
    wanopt: Literal["enable", "disable"]
    wanopt_detection: Literal["active", "passive", "off"]
    wanopt_passive_opt: Literal["default", "transparent", "non-transparent"]
    wanopt_profile: str
    wanopt_peer: str
    webcache: Literal["enable", "disable"]
    webcache_https: Literal["disable", "enable"]
    webproxy_forward_server: str
    traffic_shaper: str
    traffic_shaper_reverse: str
    per_ip_shaper: str
    nat: Literal["enable", "disable"]
    pcp_outbound: Literal["enable", "disable"]
    pcp_inbound: Literal["enable", "disable"]
    pcp_poolname: str | list[str] | list[dict[str, Any]] | list[PolicyPcppoolnameItem]
    permit_any_host: Literal["enable", "disable"]
    permit_stun_host: Literal["enable", "disable"]
    fixedport: Literal["enable", "disable"]
    port_preserve: Literal["enable", "disable"]
    port_random: Literal["enable", "disable"]
    ippool: Literal["enable", "disable"]
    poolname: str | list[str] | list[dict[str, Any]] | list[PolicyPoolnameItem]
    poolname6: str | list[str] | list[dict[str, Any]] | list[PolicyPoolname6Item]
    session_ttl: str
    vlan_cos_fwd: int
    vlan_cos_rev: int
    inbound: Literal["enable", "disable"]
    outbound: Literal["enable", "disable"]
    natinbound: Literal["enable", "disable"]
    natoutbound: Literal["enable", "disable"]
    fec: Literal["enable", "disable"]
    wccp: Literal["enable", "disable"]
    ntlm: Literal["enable", "disable"]
    ntlm_guest: Literal["enable", "disable"]
    ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | list[PolicyNtlmenabledbrowsersItem]
    fsso_agent_for_ntlm: str
    groups: str | list[str] | list[dict[str, Any]] | list[PolicyGroupsItem]
    users: str | list[str] | list[dict[str, Any]] | list[PolicyUsersItem]
    fsso_groups: str | list[str] | list[dict[str, Any]] | list[PolicyFssogroupsItem]
    auth_path: Literal["enable", "disable"]
    disclaimer: Literal["enable", "disable"]
    email_collect: Literal["enable", "disable"]
    vpntunnel: str
    natip: str
    match_vip: Literal["enable", "disable"]
    match_vip_only: Literal["enable", "disable"]
    diffserv_copy: Literal["enable", "disable"]
    diffserv_forward: Literal["enable", "disable"]
    diffserv_reverse: Literal["enable", "disable"]
    diffservcode_forward: str
    diffservcode_rev: str
    tcp_mss_sender: int
    tcp_mss_receiver: int
    comments: str
    auth_cert: str
    auth_redirect_addr: str
    redirect_url: str
    identity_based_route: str
    block_notification: Literal["enable", "disable"]
    custom_log_fields: str | list[str] | list[dict[str, Any]] | list[PolicyCustomlogfieldsItem]
    replacemsg_override_group: str
    srcaddr_negate: Literal["enable", "disable"]
    srcaddr6_negate: Literal["enable", "disable"]
    dstaddr_negate: Literal["enable", "disable"]
    dstaddr6_negate: Literal["enable", "disable"]
    ztna_ems_tag_negate: Literal["enable", "disable"]
    service_negate: Literal["enable", "disable"]
    internet_service_negate: Literal["enable", "disable"]
    internet_service_src_negate: Literal["enable", "disable"]
    internet_service6_negate: Literal["enable", "disable"]
    internet_service6_src_negate: Literal["enable", "disable"]
    timeout_send_rst: Literal["enable", "disable"]
    captive_portal_exempt: Literal["enable", "disable"]
    decrypted_traffic_mirror: str
    dsri: Literal["enable", "disable"]
    radius_mac_auth_bypass: Literal["enable", "disable"]
    radius_ip_auth_bypass: Literal["enable", "disable"]
    delay_tcp_npu_session: Literal["enable", "disable"]
    vlan_filter: str
    sgt_check: Literal["enable", "disable"]
    sgt: str | list[str] | list[dict[str, Any]] | list[PolicySgtItem]
    internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicefortiguardItem]
    internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcfortiguardItem]
    internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6fortiguardItem]
    internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcfortiguardItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class PolicyResponse(TypedDict, total=False):
    """Response type for Policy - use with .dict property for typed dict access."""
    policyid: int
    status: Literal["enable", "disable"]
    name: str
    uuid: str
    srcintf: list[PolicySrcintfItem]
    dstintf: list[PolicyDstintfItem]
    action: Literal["accept", "deny", "ipsec"]
    nat64: Literal["enable", "disable"]
    nat46: Literal["enable", "disable"]
    ztna_status: Literal["enable", "disable"]
    ztna_device_ownership: Literal["enable", "disable"]
    srcaddr: list[PolicySrcaddrItem]
    dstaddr: list[PolicyDstaddrItem]
    srcaddr6: list[PolicySrcaddr6Item]
    dstaddr6: list[PolicyDstaddr6Item]
    ztna_ems_tag: list[PolicyZtnaemstagItem]
    ztna_ems_tag_secondary: list[PolicyZtnaemstagsecondaryItem]
    ztna_tags_match_logic: Literal["or", "and"]
    ztna_geo_tag: list[PolicyZtnageotagItem]
    internet_service: Literal["enable", "disable"]
    internet_service_name: list[PolicyInternetservicenameItem]
    internet_service_group: list[PolicyInternetservicegroupItem]
    internet_service_custom: list[PolicyInternetservicecustomItem]
    network_service_dynamic: list[PolicyNetworkservicedynamicItem]
    internet_service_custom_group: list[PolicyInternetservicecustomgroupItem]
    internet_service_src: Literal["enable", "disable"]
    internet_service_src_name: list[PolicyInternetservicesrcnameItem]
    internet_service_src_group: list[PolicyInternetservicesrcgroupItem]
    internet_service_src_custom: list[PolicyInternetservicesrccustomItem]
    network_service_src_dynamic: list[PolicyNetworkservicesrcdynamicItem]
    internet_service_src_custom_group: list[PolicyInternetservicesrccustomgroupItem]
    reputation_minimum: int
    reputation_direction: Literal["source", "destination"]
    src_vendor_mac: list[PolicySrcvendormacItem]
    internet_service6: Literal["enable", "disable"]
    internet_service6_name: list[PolicyInternetservice6nameItem]
    internet_service6_group: list[PolicyInternetservice6groupItem]
    internet_service6_custom: list[PolicyInternetservice6customItem]
    internet_service6_custom_group: list[PolicyInternetservice6customgroupItem]
    internet_service6_src: Literal["enable", "disable"]
    internet_service6_src_name: list[PolicyInternetservice6srcnameItem]
    internet_service6_src_group: list[PolicyInternetservice6srcgroupItem]
    internet_service6_src_custom: list[PolicyInternetservice6srccustomItem]
    internet_service6_src_custom_group: list[PolicyInternetservice6srccustomgroupItem]
    reputation_minimum6: int
    reputation_direction6: Literal["source", "destination"]
    rtp_nat: Literal["disable", "enable"]
    rtp_addr: list[PolicyRtpaddrItem]
    send_deny_packet: Literal["disable", "enable"]
    firewall_session_dirty: Literal["check-all", "check-new"]
    schedule: str
    schedule_timeout: Literal["enable", "disable"]
    policy_expiry: Literal["enable", "disable"]
    policy_expiry_date: str
    policy_expiry_date_utc: str
    service: list[PolicyServiceItem]
    tos_mask: str
    tos: str
    tos_negate: Literal["enable", "disable"]
    anti_replay: Literal["enable", "disable"]
    tcp_session_without_syn: Literal["all", "data-only", "disable"]
    geoip_anycast: Literal["enable", "disable"]
    geoip_match: Literal["physical-location", "registered-location"]
    dynamic_shaping: Literal["enable", "disable"]
    passive_wan_health_measurement: Literal["enable", "disable"]
    app_monitor: Literal["enable", "disable"]
    utm_status: Literal["enable", "disable"]
    inspection_mode: Literal["proxy", "flow"]
    http_policy_redirect: Literal["enable", "disable", "legacy"]
    ssh_policy_redirect: Literal["enable", "disable"]
    ztna_policy_redirect: Literal["enable", "disable"]
    webproxy_profile: str
    profile_type: Literal["single", "group"]
    profile_group: str
    profile_protocol_options: str
    ssl_ssh_profile: str
    av_profile: str
    webfilter_profile: str
    dnsfilter_profile: str
    emailfilter_profile: str
    dlp_profile: str
    file_filter_profile: str
    ips_sensor: str
    application_list: str
    voip_profile: str
    ips_voip_filter: str
    sctp_filter_profile: str
    diameter_filter_profile: str
    virtual_patch_profile: str
    icap_profile: str
    videofilter_profile: str
    waf_profile: str
    ssh_filter_profile: str
    casb_profile: str
    logtraffic: Literal["all", "utm", "disable"]
    logtraffic_start: Literal["enable", "disable"]
    log_http_transaction: Literal["enable", "disable"]
    capture_packet: Literal["enable", "disable"]
    auto_asic_offload: Literal["enable", "disable"]
    wanopt: Literal["enable", "disable"]
    wanopt_detection: Literal["active", "passive", "off"]
    wanopt_passive_opt: Literal["default", "transparent", "non-transparent"]
    wanopt_profile: str
    wanopt_peer: str
    webcache: Literal["enable", "disable"]
    webcache_https: Literal["disable", "enable"]
    webproxy_forward_server: str
    traffic_shaper: str
    traffic_shaper_reverse: str
    per_ip_shaper: str
    nat: Literal["enable", "disable"]
    pcp_outbound: Literal["enable", "disable"]
    pcp_inbound: Literal["enable", "disable"]
    pcp_poolname: list[PolicyPcppoolnameItem]
    permit_any_host: Literal["enable", "disable"]
    permit_stun_host: Literal["enable", "disable"]
    fixedport: Literal["enable", "disable"]
    port_preserve: Literal["enable", "disable"]
    port_random: Literal["enable", "disable"]
    ippool: Literal["enable", "disable"]
    poolname: list[PolicyPoolnameItem]
    poolname6: list[PolicyPoolname6Item]
    session_ttl: str
    vlan_cos_fwd: int
    vlan_cos_rev: int
    inbound: Literal["enable", "disable"]
    outbound: Literal["enable", "disable"]
    natinbound: Literal["enable", "disable"]
    natoutbound: Literal["enable", "disable"]
    fec: Literal["enable", "disable"]
    wccp: Literal["enable", "disable"]
    ntlm: Literal["enable", "disable"]
    ntlm_guest: Literal["enable", "disable"]
    ntlm_enabled_browsers: list[PolicyNtlmenabledbrowsersItem]
    fsso_agent_for_ntlm: str
    groups: list[PolicyGroupsItem]
    users: list[PolicyUsersItem]
    fsso_groups: list[PolicyFssogroupsItem]
    auth_path: Literal["enable", "disable"]
    disclaimer: Literal["enable", "disable"]
    email_collect: Literal["enable", "disable"]
    vpntunnel: str
    natip: str
    match_vip: Literal["enable", "disable"]
    match_vip_only: Literal["enable", "disable"]
    diffserv_copy: Literal["enable", "disable"]
    diffserv_forward: Literal["enable", "disable"]
    diffserv_reverse: Literal["enable", "disable"]
    diffservcode_forward: str
    diffservcode_rev: str
    tcp_mss_sender: int
    tcp_mss_receiver: int
    comments: str
    auth_cert: str
    auth_redirect_addr: str
    redirect_url: str
    identity_based_route: str
    block_notification: Literal["enable", "disable"]
    custom_log_fields: list[PolicyCustomlogfieldsItem]
    replacemsg_override_group: str
    srcaddr_negate: Literal["enable", "disable"]
    srcaddr6_negate: Literal["enable", "disable"]
    dstaddr_negate: Literal["enable", "disable"]
    dstaddr6_negate: Literal["enable", "disable"]
    ztna_ems_tag_negate: Literal["enable", "disable"]
    service_negate: Literal["enable", "disable"]
    internet_service_negate: Literal["enable", "disable"]
    internet_service_src_negate: Literal["enable", "disable"]
    internet_service6_negate: Literal["enable", "disable"]
    internet_service6_src_negate: Literal["enable", "disable"]
    timeout_send_rst: Literal["enable", "disable"]
    captive_portal_exempt: Literal["enable", "disable"]
    decrypted_traffic_mirror: str
    dsri: Literal["enable", "disable"]
    radius_mac_auth_bypass: Literal["enable", "disable"]
    radius_ip_auth_bypass: Literal["enable", "disable"]
    delay_tcp_npu_session: Literal["enable", "disable"]
    vlan_filter: str
    sgt_check: Literal["enable", "disable"]
    sgt: list[PolicySgtItem]
    internet_service_fortiguard: list[PolicyInternetservicefortiguardItem]
    internet_service_src_fortiguard: list[PolicyInternetservicesrcfortiguardItem]
    internet_service6_fortiguard: list[PolicyInternetservice6fortiguardItem]
    internet_service6_src_fortiguard: list[PolicyInternetservice6srcfortiguardItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class PolicyObject(FortiObject):
    """Typed FortiObject for Policy with field access."""
    policyid: int
    status: Literal["enable", "disable"]
    name: str
    uuid: str
    srcintf: list[PolicySrcintfItem]
    dstintf: list[PolicyDstintfItem]
    action: Literal["accept", "deny", "ipsec"]
    nat64: Literal["enable", "disable"]
    nat46: Literal["enable", "disable"]
    ztna_status: Literal["enable", "disable"]
    ztna_device_ownership: Literal["enable", "disable"]
    srcaddr: list[PolicySrcaddrItem]
    dstaddr: list[PolicyDstaddrItem]
    srcaddr6: list[PolicySrcaddr6Item]
    dstaddr6: list[PolicyDstaddr6Item]
    ztna_ems_tag: list[PolicyZtnaemstagItem]
    ztna_ems_tag_secondary: list[PolicyZtnaemstagsecondaryItem]
    ztna_tags_match_logic: Literal["or", "and"]
    ztna_geo_tag: list[PolicyZtnageotagItem]
    internet_service: Literal["enable", "disable"]
    internet_service_name: list[PolicyInternetservicenameItem]
    internet_service_group: list[PolicyInternetservicegroupItem]
    internet_service_custom: list[PolicyInternetservicecustomItem]
    network_service_dynamic: list[PolicyNetworkservicedynamicItem]
    internet_service_custom_group: list[PolicyInternetservicecustomgroupItem]
    internet_service_src: Literal["enable", "disable"]
    internet_service_src_name: list[PolicyInternetservicesrcnameItem]
    internet_service_src_group: list[PolicyInternetservicesrcgroupItem]
    internet_service_src_custom: list[PolicyInternetservicesrccustomItem]
    network_service_src_dynamic: list[PolicyNetworkservicesrcdynamicItem]
    internet_service_src_custom_group: list[PolicyInternetservicesrccustomgroupItem]
    reputation_minimum: int
    reputation_direction: Literal["source", "destination"]
    src_vendor_mac: list[PolicySrcvendormacItem]
    internet_service6: Literal["enable", "disable"]
    internet_service6_name: list[PolicyInternetservice6nameItem]
    internet_service6_group: list[PolicyInternetservice6groupItem]
    internet_service6_custom: list[PolicyInternetservice6customItem]
    internet_service6_custom_group: list[PolicyInternetservice6customgroupItem]
    internet_service6_src: Literal["enable", "disable"]
    internet_service6_src_name: list[PolicyInternetservice6srcnameItem]
    internet_service6_src_group: list[PolicyInternetservice6srcgroupItem]
    internet_service6_src_custom: list[PolicyInternetservice6srccustomItem]
    internet_service6_src_custom_group: list[PolicyInternetservice6srccustomgroupItem]
    reputation_minimum6: int
    reputation_direction6: Literal["source", "destination"]
    rtp_nat: Literal["disable", "enable"]
    rtp_addr: list[PolicyRtpaddrItem]
    send_deny_packet: Literal["disable", "enable"]
    firewall_session_dirty: Literal["check-all", "check-new"]
    schedule: str
    schedule_timeout: Literal["enable", "disable"]
    policy_expiry: Literal["enable", "disable"]
    policy_expiry_date: str
    policy_expiry_date_utc: str
    service: list[PolicyServiceItem]
    tos_mask: str
    tos: str
    tos_negate: Literal["enable", "disable"]
    anti_replay: Literal["enable", "disable"]
    tcp_session_without_syn: Literal["all", "data-only", "disable"]
    geoip_anycast: Literal["enable", "disable"]
    geoip_match: Literal["physical-location", "registered-location"]
    dynamic_shaping: Literal["enable", "disable"]
    passive_wan_health_measurement: Literal["enable", "disable"]
    app_monitor: Literal["enable", "disable"]
    utm_status: Literal["enable", "disable"]
    inspection_mode: Literal["proxy", "flow"]
    http_policy_redirect: Literal["enable", "disable", "legacy"]
    ssh_policy_redirect: Literal["enable", "disable"]
    ztna_policy_redirect: Literal["enable", "disable"]
    webproxy_profile: str
    profile_type: Literal["single", "group"]
    profile_group: str
    profile_protocol_options: str
    ssl_ssh_profile: str
    av_profile: str
    webfilter_profile: str
    dnsfilter_profile: str
    emailfilter_profile: str
    dlp_profile: str
    file_filter_profile: str
    ips_sensor: str
    application_list: str
    voip_profile: str
    ips_voip_filter: str
    sctp_filter_profile: str
    diameter_filter_profile: str
    virtual_patch_profile: str
    icap_profile: str
    videofilter_profile: str
    waf_profile: str
    ssh_filter_profile: str
    casb_profile: str
    logtraffic: Literal["all", "utm", "disable"]
    logtraffic_start: Literal["enable", "disable"]
    log_http_transaction: Literal["enable", "disable"]
    capture_packet: Literal["enable", "disable"]
    auto_asic_offload: Literal["enable", "disable"]
    wanopt: Literal["enable", "disable"]
    wanopt_detection: Literal["active", "passive", "off"]
    wanopt_passive_opt: Literal["default", "transparent", "non-transparent"]
    wanopt_profile: str
    wanopt_peer: str
    webcache: Literal["enable", "disable"]
    webcache_https: Literal["disable", "enable"]
    webproxy_forward_server: str
    traffic_shaper: str
    traffic_shaper_reverse: str
    per_ip_shaper: str
    nat: Literal["enable", "disable"]
    pcp_outbound: Literal["enable", "disable"]
    pcp_inbound: Literal["enable", "disable"]
    pcp_poolname: list[PolicyPcppoolnameItem]
    permit_any_host: Literal["enable", "disable"]
    permit_stun_host: Literal["enable", "disable"]
    fixedport: Literal["enable", "disable"]
    port_preserve: Literal["enable", "disable"]
    port_random: Literal["enable", "disable"]
    ippool: Literal["enable", "disable"]
    poolname: list[PolicyPoolnameItem]
    poolname6: list[PolicyPoolname6Item]
    session_ttl: str
    vlan_cos_fwd: int
    vlan_cos_rev: int
    inbound: Literal["enable", "disable"]
    outbound: Literal["enable", "disable"]
    natinbound: Literal["enable", "disable"]
    natoutbound: Literal["enable", "disable"]
    fec: Literal["enable", "disable"]
    wccp: Literal["enable", "disable"]
    ntlm: Literal["enable", "disable"]
    ntlm_guest: Literal["enable", "disable"]
    ntlm_enabled_browsers: list[PolicyNtlmenabledbrowsersItem]
    fsso_agent_for_ntlm: str
    groups: list[PolicyGroupsItem]
    users: list[PolicyUsersItem]
    fsso_groups: list[PolicyFssogroupsItem]
    auth_path: Literal["enable", "disable"]
    disclaimer: Literal["enable", "disable"]
    email_collect: Literal["enable", "disable"]
    vpntunnel: str
    natip: str
    match_vip: Literal["enable", "disable"]
    match_vip_only: Literal["enable", "disable"]
    diffserv_copy: Literal["enable", "disable"]
    diffserv_forward: Literal["enable", "disable"]
    diffserv_reverse: Literal["enable", "disable"]
    diffservcode_forward: str
    diffservcode_rev: str
    tcp_mss_sender: int
    tcp_mss_receiver: int
    comments: str
    auth_cert: str
    auth_redirect_addr: str
    redirect_url: str
    identity_based_route: str
    block_notification: Literal["enable", "disable"]
    custom_log_fields: list[PolicyCustomlogfieldsItem]
    replacemsg_override_group: str
    srcaddr_negate: Literal["enable", "disable"]
    srcaddr6_negate: Literal["enable", "disable"]
    dstaddr_negate: Literal["enable", "disable"]
    dstaddr6_negate: Literal["enable", "disable"]
    ztna_ems_tag_negate: Literal["enable", "disable"]
    service_negate: Literal["enable", "disable"]
    internet_service_negate: Literal["enable", "disable"]
    internet_service_src_negate: Literal["enable", "disable"]
    internet_service6_negate: Literal["enable", "disable"]
    internet_service6_src_negate: Literal["enable", "disable"]
    timeout_send_rst: Literal["enable", "disable"]
    captive_portal_exempt: Literal["enable", "disable"]
    decrypted_traffic_mirror: str
    dsri: Literal["enable", "disable"]
    radius_mac_auth_bypass: Literal["enable", "disable"]
    radius_ip_auth_bypass: Literal["enable", "disable"]
    delay_tcp_npu_session: Literal["enable", "disable"]
    vlan_filter: str
    sgt_check: Literal["enable", "disable"]
    sgt: list[PolicySgtItem]
    internet_service_fortiguard: list[PolicyInternetservicefortiguardItem]
    internet_service_src_fortiguard: list[PolicyInternetservicesrcfortiguardItem]
    internet_service6_fortiguard: list[PolicyInternetservice6fortiguardItem]
    internet_service6_src_fortiguard: list[PolicyInternetservice6srcfortiguardItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class Policy:
    """
    
    Endpoint: firewall/policy
    Category: cmdb
    MKey: policyid
    """
    
    # Class attributes for introspection
    endpoint: ClassVar[str] = ...
    path: ClassVar[str] = ...
    category: ClassVar[str] = ...
    mkey: ClassVar[str] = ...
    capabilities: ClassVar[dict[str, Any]] = ...
    
    def __init__(self, client: Any) -> None:
        """Initialize endpoint with HTTP client."""
        ...
    
    # ================================================================
    # GET Methods
    # ================================================================
    
    # CMDB with mkey - overloads for single vs list returns
    @overload
    def get(
        self,
        policyid: int,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> PolicyObject: ...
    
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObjectList[PolicyObject]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...

    # ================================================================
    # POST Method
    # ================================================================
    
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[PolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[PolicyDstintfItem] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddrItem] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddrItem] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddr6Item] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddr6Item] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | list[PolicyZtnaemstagItem] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | list[PolicyZtnaemstagsecondaryItem] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | list[PolicyZtnageotagItem] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicenameItem] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomItem] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | list[PolicyNetworkservicedynamicItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcnameItem] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcgroupItem] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrccustomItem] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | list[PolicyNetworkservicesrcdynamicItem] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrccustomgroupItem] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | list[PolicySrcvendormacItem] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6nameItem] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6groupItem] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6customItem] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6customgroupItem] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcnameItem] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcgroupItem] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srccustomItem] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srccustomgroupItem] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | list[PolicyRtpaddrItem] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[PolicyServiceItem] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | list[PolicyPcppoolnameItem] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | list[PolicyPoolnameItem] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | list[PolicyPoolname6Item] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | list[PolicyNtlmenabledbrowsersItem] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[PolicyGroupsItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[PolicyUsersItem] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | list[PolicyFssogroupsItem] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | list[PolicyCustomlogfieldsItem] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | list[PolicySgtItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicefortiguardItem] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcfortiguardItem] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6fortiguardItem] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcfortiguardItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> PolicyObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[PolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[PolicyDstintfItem] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddrItem] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddrItem] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddr6Item] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddr6Item] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | list[PolicyZtnaemstagItem] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | list[PolicyZtnaemstagsecondaryItem] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | list[PolicyZtnageotagItem] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicenameItem] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomItem] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | list[PolicyNetworkservicedynamicItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcnameItem] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcgroupItem] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrccustomItem] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | list[PolicyNetworkservicesrcdynamicItem] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrccustomgroupItem] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | list[PolicySrcvendormacItem] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6nameItem] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6groupItem] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6customItem] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6customgroupItem] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcnameItem] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcgroupItem] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srccustomItem] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srccustomgroupItem] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | list[PolicyRtpaddrItem] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[PolicyServiceItem] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | list[PolicyPcppoolnameItem] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | list[PolicyPoolnameItem] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | list[PolicyPoolname6Item] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | list[PolicyNtlmenabledbrowsersItem] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[PolicyGroupsItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[PolicyUsersItem] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | list[PolicyFssogroupsItem] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | list[PolicyCustomlogfieldsItem] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | list[PolicySgtItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicefortiguardItem] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcfortiguardItem] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6fortiguardItem] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcfortiguardItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> PolicyObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[PolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[PolicyDstintfItem] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddrItem] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddrItem] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[PolicySrcaddr6Item] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[PolicyDstaddr6Item] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | list[PolicyZtnaemstagItem] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | list[PolicyZtnaemstagsecondaryItem] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | list[PolicyZtnageotagItem] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicenameItem] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomItem] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | list[PolicyNetworkservicedynamicItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcnameItem] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcgroupItem] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrccustomItem] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | list[PolicyNetworkservicesrcdynamicItem] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrccustomgroupItem] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | list[PolicySrcvendormacItem] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6nameItem] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6groupItem] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6customItem] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6customgroupItem] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcnameItem] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcgroupItem] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srccustomItem] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srccustomgroupItem] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | list[PolicyRtpaddrItem] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[PolicyServiceItem] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | list[PolicyPcppoolnameItem] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | list[PolicyPoolnameItem] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | list[PolicyPoolname6Item] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | list[PolicyNtlmenabledbrowsersItem] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[PolicyGroupsItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[PolicyUsersItem] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | list[PolicyFssogroupsItem] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | list[PolicyCustomlogfieldsItem] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | list[PolicySgtItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicefortiguardItem] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservicesrcfortiguardItem] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6fortiguardItem] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[PolicyInternetservice6srcfortiguardItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> list[str] | list[dict[str, Any]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


__all__ = [
    "Policy",
    "PolicyPayload",
    "PolicyResponse",
    "PolicyObject",
]