""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/proxy_policy
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

class ProxyPolicyAccessproxyItem:
    """Nested item for access-proxy field - supports attribute access."""
    name: str


class ProxyPolicyAccessproxy6Item:
    """Nested item for access-proxy6 field - supports attribute access."""
    name: str


class ProxyPolicyZtnaproxyItem:
    """Nested item for ztna-proxy field - supports attribute access."""
    name: str


class ProxyPolicySrcintfItem:
    """Nested item for srcintf field - supports attribute access."""
    name: str


class ProxyPolicyDstintfItem:
    """Nested item for dstintf field - supports attribute access."""
    name: str


class ProxyPolicySrcaddrItem:
    """Nested item for srcaddr field - supports attribute access."""
    name: str


class ProxyPolicyPoolnameItem:
    """Nested item for poolname field - supports attribute access."""
    name: str


class ProxyPolicyPoolname6Item:
    """Nested item for poolname6 field - supports attribute access."""
    name: str


class ProxyPolicyDstaddrItem:
    """Nested item for dstaddr field - supports attribute access."""
    name: str


class ProxyPolicyZtnaemstagItem:
    """Nested item for ztna-ems-tag field - supports attribute access."""
    name: str


class ProxyPolicyUrlriskItem:
    """Nested item for url-risk field - supports attribute access."""
    name: str


class ProxyPolicyInternetservicenameItem:
    """Nested item for internet-service-name field - supports attribute access."""
    name: str


class ProxyPolicyInternetservicegroupItem:
    """Nested item for internet-service-group field - supports attribute access."""
    name: str


class ProxyPolicyInternetservicecustomItem:
    """Nested item for internet-service-custom field - supports attribute access."""
    name: str


class ProxyPolicyInternetservicecustomgroupItem:
    """Nested item for internet-service-custom-group field - supports attribute access."""
    name: str


class ProxyPolicyInternetservicefortiguardItem:
    """Nested item for internet-service-fortiguard field - supports attribute access."""
    name: str


class ProxyPolicyInternetservice6nameItem:
    """Nested item for internet-service6-name field - supports attribute access."""
    name: str


class ProxyPolicyInternetservice6groupItem:
    """Nested item for internet-service6-group field - supports attribute access."""
    name: str


class ProxyPolicyInternetservice6customItem:
    """Nested item for internet-service6-custom field - supports attribute access."""
    name: str


class ProxyPolicyInternetservice6customgroupItem:
    """Nested item for internet-service6-custom-group field - supports attribute access."""
    name: str


class ProxyPolicyInternetservice6fortiguardItem:
    """Nested item for internet-service6-fortiguard field - supports attribute access."""
    name: str


class ProxyPolicyServiceItem:
    """Nested item for service field - supports attribute access."""
    name: str


class ProxyPolicySrcaddr6Item:
    """Nested item for srcaddr6 field - supports attribute access."""
    name: str


class ProxyPolicyDstaddr6Item:
    """Nested item for dstaddr6 field - supports attribute access."""
    name: str


class ProxyPolicyGroupsItem:
    """Nested item for groups field - supports attribute access."""
    name: str


class ProxyPolicyUsersItem:
    """Nested item for users field - supports attribute access."""
    name: str


class ProxyPolicyPayload(TypedDict, total=False):
    """Payload type for ProxyPolicy operations."""
    uuid: str
    policyid: int
    name: str
    proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"]
    access_proxy: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyAccessproxyItem]
    access_proxy6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyAccessproxy6Item]
    ztna_proxy: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyZtnaproxyItem]
    srcintf: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcintfItem]
    dstintf: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstintfItem]
    srcaddr: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcaddrItem]
    poolname: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyPoolnameItem]
    poolname6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyPoolname6Item]
    dstaddr: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstaddrItem]
    ztna_ems_tag: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyZtnaemstagItem]
    ztna_tags_match_logic: Literal["or", "and"]
    device_ownership: Literal["enable", "disable"]
    url_risk: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyUrlriskItem]
    internet_service: Literal["enable", "disable"]
    internet_service_negate: Literal["enable", "disable"]
    internet_service_name: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicenameItem]
    internet_service_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicegroupItem]
    internet_service_custom: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicecustomItem]
    internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicecustomgroupItem]
    internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicefortiguardItem]
    internet_service6: Literal["enable", "disable"]
    internet_service6_negate: Literal["enable", "disable"]
    internet_service6_name: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6nameItem]
    internet_service6_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6groupItem]
    internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6customItem]
    internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6customgroupItem]
    internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6fortiguardItem]
    service: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyServiceItem]
    srcaddr_negate: Literal["enable", "disable"]
    dstaddr_negate: Literal["enable", "disable"]
    ztna_ems_tag_negate: Literal["enable", "disable"]
    service_negate: Literal["enable", "disable"]
    action: Literal["accept", "deny", "redirect", "isolate"]
    status: Literal["enable", "disable"]
    schedule: str
    logtraffic: Literal["all", "utm", "disable"]
    session_ttl: int
    srcaddr6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcaddr6Item]
    dstaddr6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstaddr6Item]
    groups: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyGroupsItem]
    users: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyUsersItem]
    http_tunnel_auth: Literal["enable", "disable"]
    ssh_policy_redirect: Literal["enable", "disable"]
    webproxy_forward_server: str
    isolator_server: str
    webproxy_profile: str
    transparent: Literal["enable", "disable"]
    webcache: Literal["enable", "disable"]
    webcache_https: Literal["disable", "enable"]
    disclaimer: Literal["disable", "domain", "policy", "user"]
    utm_status: Literal["enable", "disable"]
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
    ips_voip_filter: str
    sctp_filter_profile: str
    icap_profile: str
    videofilter_profile: str
    waf_profile: str
    ssh_filter_profile: str
    casb_profile: str
    replacemsg_override_group: str
    logtraffic_start: Literal["enable", "disable"]
    log_http_transaction: Literal["enable", "disable"]
    comments: str
    block_notification: Literal["enable", "disable"]
    redirect_url: str
    https_sub_category: Literal["enable", "disable"]
    decrypted_traffic_mirror: str
    detect_https_in_http_request: Literal["enable", "disable"]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ProxyPolicyResponse(TypedDict, total=False):
    """Response type for ProxyPolicy - use with .dict property for typed dict access."""
    uuid: str
    policyid: int
    name: str
    proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"]
    access_proxy: list[ProxyPolicyAccessproxyItem]
    access_proxy6: list[ProxyPolicyAccessproxy6Item]
    ztna_proxy: list[ProxyPolicyZtnaproxyItem]
    srcintf: list[ProxyPolicySrcintfItem]
    dstintf: list[ProxyPolicyDstintfItem]
    srcaddr: list[ProxyPolicySrcaddrItem]
    poolname: list[ProxyPolicyPoolnameItem]
    poolname6: list[ProxyPolicyPoolname6Item]
    dstaddr: list[ProxyPolicyDstaddrItem]
    ztna_ems_tag: list[ProxyPolicyZtnaemstagItem]
    ztna_tags_match_logic: Literal["or", "and"]
    device_ownership: Literal["enable", "disable"]
    url_risk: list[ProxyPolicyUrlriskItem]
    internet_service: Literal["enable", "disable"]
    internet_service_negate: Literal["enable", "disable"]
    internet_service_name: list[ProxyPolicyInternetservicenameItem]
    internet_service_group: list[ProxyPolicyInternetservicegroupItem]
    internet_service_custom: list[ProxyPolicyInternetservicecustomItem]
    internet_service_custom_group: list[ProxyPolicyInternetservicecustomgroupItem]
    internet_service_fortiguard: list[ProxyPolicyInternetservicefortiguardItem]
    internet_service6: Literal["enable", "disable"]
    internet_service6_negate: Literal["enable", "disable"]
    internet_service6_name: list[ProxyPolicyInternetservice6nameItem]
    internet_service6_group: list[ProxyPolicyInternetservice6groupItem]
    internet_service6_custom: list[ProxyPolicyInternetservice6customItem]
    internet_service6_custom_group: list[ProxyPolicyInternetservice6customgroupItem]
    internet_service6_fortiguard: list[ProxyPolicyInternetservice6fortiguardItem]
    service: list[ProxyPolicyServiceItem]
    srcaddr_negate: Literal["enable", "disable"]
    dstaddr_negate: Literal["enable", "disable"]
    ztna_ems_tag_negate: Literal["enable", "disable"]
    service_negate: Literal["enable", "disable"]
    action: Literal["accept", "deny", "redirect", "isolate"]
    status: Literal["enable", "disable"]
    schedule: str
    logtraffic: Literal["all", "utm", "disable"]
    session_ttl: int
    srcaddr6: list[ProxyPolicySrcaddr6Item]
    dstaddr6: list[ProxyPolicyDstaddr6Item]
    groups: list[ProxyPolicyGroupsItem]
    users: list[ProxyPolicyUsersItem]
    http_tunnel_auth: Literal["enable", "disable"]
    ssh_policy_redirect: Literal["enable", "disable"]
    webproxy_forward_server: str
    isolator_server: str
    webproxy_profile: str
    transparent: Literal["enable", "disable"]
    webcache: Literal["enable", "disable"]
    webcache_https: Literal["disable", "enable"]
    disclaimer: Literal["disable", "domain", "policy", "user"]
    utm_status: Literal["enable", "disable"]
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
    ips_voip_filter: str
    sctp_filter_profile: str
    icap_profile: str
    videofilter_profile: str
    waf_profile: str
    ssh_filter_profile: str
    casb_profile: str
    replacemsg_override_group: str
    logtraffic_start: Literal["enable", "disable"]
    log_http_transaction: Literal["enable", "disable"]
    comments: str
    block_notification: Literal["enable", "disable"]
    redirect_url: str
    https_sub_category: Literal["enable", "disable"]
    decrypted_traffic_mirror: str
    detect_https_in_http_request: Literal["enable", "disable"]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ProxyPolicyObject(FortiObject):
    """Typed FortiObject for ProxyPolicy with field access."""
    uuid: str
    policyid: int
    name: str
    proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"]
    access_proxy: list[ProxyPolicyAccessproxyItem]
    access_proxy6: list[ProxyPolicyAccessproxy6Item]
    ztna_proxy: list[ProxyPolicyZtnaproxyItem]
    srcintf: list[ProxyPolicySrcintfItem]
    dstintf: list[ProxyPolicyDstintfItem]
    srcaddr: list[ProxyPolicySrcaddrItem]
    poolname: list[ProxyPolicyPoolnameItem]
    poolname6: list[ProxyPolicyPoolname6Item]
    dstaddr: list[ProxyPolicyDstaddrItem]
    ztna_ems_tag: list[ProxyPolicyZtnaemstagItem]
    ztna_tags_match_logic: Literal["or", "and"]
    device_ownership: Literal["enable", "disable"]
    url_risk: list[ProxyPolicyUrlriskItem]
    internet_service: Literal["enable", "disable"]
    internet_service_negate: Literal["enable", "disable"]
    internet_service_name: list[ProxyPolicyInternetservicenameItem]
    internet_service_group: list[ProxyPolicyInternetservicegroupItem]
    internet_service_custom: list[ProxyPolicyInternetservicecustomItem]
    internet_service_custom_group: list[ProxyPolicyInternetservicecustomgroupItem]
    internet_service_fortiguard: list[ProxyPolicyInternetservicefortiguardItem]
    internet_service6: Literal["enable", "disable"]
    internet_service6_negate: Literal["enable", "disable"]
    internet_service6_name: list[ProxyPolicyInternetservice6nameItem]
    internet_service6_group: list[ProxyPolicyInternetservice6groupItem]
    internet_service6_custom: list[ProxyPolicyInternetservice6customItem]
    internet_service6_custom_group: list[ProxyPolicyInternetservice6customgroupItem]
    internet_service6_fortiguard: list[ProxyPolicyInternetservice6fortiguardItem]
    service: list[ProxyPolicyServiceItem]
    srcaddr_negate: Literal["enable", "disable"]
    dstaddr_negate: Literal["enable", "disable"]
    ztna_ems_tag_negate: Literal["enable", "disable"]
    service_negate: Literal["enable", "disable"]
    action: Literal["accept", "deny", "redirect", "isolate"]
    status: Literal["enable", "disable"]
    schedule: str
    logtraffic: Literal["all", "utm", "disable"]
    session_ttl: int
    srcaddr6: list[ProxyPolicySrcaddr6Item]
    dstaddr6: list[ProxyPolicyDstaddr6Item]
    groups: list[ProxyPolicyGroupsItem]
    users: list[ProxyPolicyUsersItem]
    http_tunnel_auth: Literal["enable", "disable"]
    ssh_policy_redirect: Literal["enable", "disable"]
    webproxy_forward_server: str
    isolator_server: str
    webproxy_profile: str
    transparent: Literal["enable", "disable"]
    webcache: Literal["enable", "disable"]
    webcache_https: Literal["disable", "enable"]
    disclaimer: Literal["disable", "domain", "policy", "user"]
    utm_status: Literal["enable", "disable"]
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
    ips_voip_filter: str
    sctp_filter_profile: str
    icap_profile: str
    videofilter_profile: str
    waf_profile: str
    ssh_filter_profile: str
    casb_profile: str
    replacemsg_override_group: str
    logtraffic_start: Literal["enable", "disable"]
    log_http_transaction: Literal["enable", "disable"]
    comments: str
    block_notification: Literal["enable", "disable"]
    redirect_url: str
    https_sub_category: Literal["enable", "disable"]
    decrypted_traffic_mirror: str
    detect_https_in_http_request: Literal["enable", "disable"]


# ================================================================
# Main Endpoint Class
# ================================================================

class ProxyPolicy:
    """
    
    Endpoint: firewall/proxy_policy
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
    ) -> ProxyPolicyObject: ...
    
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
    ) -> FortiObjectList[ProxyPolicyObject]: ...
    
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
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyAccessproxyItem] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyAccessproxy6Item] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyZtnaproxyItem] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstintfItem] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcaddrItem] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyPoolnameItem] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyPoolname6Item] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstaddrItem] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyZtnaemstagItem] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyUrlriskItem] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicenameItem] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicecustomItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicefortiguardItem] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6nameItem] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6groupItem] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6customItem] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6customgroupItem] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6fortiguardItem] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyServiceItem] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcaddr6Item] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstaddr6Item] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyGroupsItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyUsersItem] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ProxyPolicyObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyAccessproxyItem] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyAccessproxy6Item] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyZtnaproxyItem] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstintfItem] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcaddrItem] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyPoolnameItem] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyPoolname6Item] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstaddrItem] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyZtnaemstagItem] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyUrlriskItem] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicenameItem] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicecustomItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicefortiguardItem] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6nameItem] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6groupItem] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6customItem] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6customgroupItem] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6fortiguardItem] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyServiceItem] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcaddr6Item] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstaddr6Item] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyGroupsItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyUsersItem] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ProxyPolicyObject: ...

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
        payload_dict: ProxyPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = ...,
        access_proxy: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyAccessproxyItem] | None = ...,
        access_proxy6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyAccessproxy6Item] | None = ...,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyZtnaproxyItem] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstintfItem] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcaddrItem] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyPoolnameItem] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyPoolname6Item] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstaddrItem] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyZtnaemstagItem] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        device_ownership: Literal["enable", "disable"] | None = ...,
        url_risk: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyUrlriskItem] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicenameItem] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicecustomItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservicefortiguardItem] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6nameItem] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6groupItem] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6customItem] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6customgroupItem] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyInternetservice6fortiguardItem] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyServiceItem] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        session_ttl: int | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicySrcaddr6Item] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyDstaddr6Item] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyGroupsItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[ProxyPolicyUsersItem] | None = ...,
        http_tunnel_auth: Literal["enable", "disable"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        isolator_server: str | None = ...,
        webproxy_profile: str | None = ...,
        transparent: Literal["enable", "disable"] | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
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
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        replacemsg_override_group: str | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        redirect_url: str | None = ...,
        https_sub_category: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        detect_https_in_http_request: Literal["enable", "disable"] | None = ...,
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
    "ProxyPolicy",
    "ProxyPolicyPayload",
    "ProxyPolicyResponse",
    "ProxyPolicyObject",
]