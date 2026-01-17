""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/security_policy
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

class SecurityPolicySrcintfItem:
    """Nested item for srcintf field - supports attribute access."""
    name: str


class SecurityPolicyDstintfItem:
    """Nested item for dstintf field - supports attribute access."""
    name: str


class SecurityPolicySrcaddrItem:
    """Nested item for srcaddr field - supports attribute access."""
    name: str


class SecurityPolicyDstaddrItem:
    """Nested item for dstaddr field - supports attribute access."""
    name: str


class SecurityPolicySrcaddr6Item:
    """Nested item for srcaddr6 field - supports attribute access."""
    name: str


class SecurityPolicyDstaddr6Item:
    """Nested item for dstaddr6 field - supports attribute access."""
    name: str


class SecurityPolicyInternetservicenameItem:
    """Nested item for internet-service-name field - supports attribute access."""
    name: str


class SecurityPolicyInternetservicegroupItem:
    """Nested item for internet-service-group field - supports attribute access."""
    name: str


class SecurityPolicyInternetservicecustomItem:
    """Nested item for internet-service-custom field - supports attribute access."""
    name: str


class SecurityPolicyInternetservicecustomgroupItem:
    """Nested item for internet-service-custom-group field - supports attribute access."""
    name: str


class SecurityPolicyInternetservicefortiguardItem:
    """Nested item for internet-service-fortiguard field - supports attribute access."""
    name: str


class SecurityPolicyInternetservicesrcnameItem:
    """Nested item for internet-service-src-name field - supports attribute access."""
    name: str


class SecurityPolicyInternetservicesrcgroupItem:
    """Nested item for internet-service-src-group field - supports attribute access."""
    name: str


class SecurityPolicyInternetservicesrccustomItem:
    """Nested item for internet-service-src-custom field - supports attribute access."""
    name: str


class SecurityPolicyInternetservicesrccustomgroupItem:
    """Nested item for internet-service-src-custom-group field - supports attribute access."""
    name: str


class SecurityPolicyInternetservicesrcfortiguardItem:
    """Nested item for internet-service-src-fortiguard field - supports attribute access."""
    name: str


class SecurityPolicyInternetservice6nameItem:
    """Nested item for internet-service6-name field - supports attribute access."""
    name: str


class SecurityPolicyInternetservice6groupItem:
    """Nested item for internet-service6-group field - supports attribute access."""
    name: str


class SecurityPolicyInternetservice6customItem:
    """Nested item for internet-service6-custom field - supports attribute access."""
    name: str


class SecurityPolicyInternetservice6customgroupItem:
    """Nested item for internet-service6-custom-group field - supports attribute access."""
    name: str


class SecurityPolicyInternetservice6fortiguardItem:
    """Nested item for internet-service6-fortiguard field - supports attribute access."""
    name: str


class SecurityPolicyInternetservice6srcnameItem:
    """Nested item for internet-service6-src-name field - supports attribute access."""
    name: str


class SecurityPolicyInternetservice6srcgroupItem:
    """Nested item for internet-service6-src-group field - supports attribute access."""
    name: str


class SecurityPolicyInternetservice6srccustomItem:
    """Nested item for internet-service6-src-custom field - supports attribute access."""
    name: str


class SecurityPolicyInternetservice6srccustomgroupItem:
    """Nested item for internet-service6-src-custom-group field - supports attribute access."""
    name: str


class SecurityPolicyInternetservice6srcfortiguardItem:
    """Nested item for internet-service6-src-fortiguard field - supports attribute access."""
    name: str


class SecurityPolicyServiceItem:
    """Nested item for service field - supports attribute access."""
    name: str


class SecurityPolicyApplicationItem:
    """Nested item for application field - supports attribute access."""
    id: int


class SecurityPolicyAppcategoryItem:
    """Nested item for app-category field - supports attribute access."""
    id: int


class SecurityPolicyAppgroupItem:
    """Nested item for app-group field - supports attribute access."""
    name: str


class SecurityPolicyGroupsItem:
    """Nested item for groups field - supports attribute access."""
    name: str


class SecurityPolicyUsersItem:
    """Nested item for users field - supports attribute access."""
    name: str


class SecurityPolicyFssogroupsItem:
    """Nested item for fsso-groups field - supports attribute access."""
    name: str


class SecurityPolicyPayload(TypedDict, total=False):
    """Payload type for SecurityPolicy operations."""
    uuid: str
    policyid: int
    name: str
    comments: str
    srcintf: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcintfItem]
    dstintf: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstintfItem]
    srcaddr: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcaddrItem]
    srcaddr_negate: Literal["enable", "disable"]
    dstaddr: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstaddrItem]
    dstaddr_negate: Literal["enable", "disable"]
    srcaddr6: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcaddr6Item]
    srcaddr6_negate: Literal["enable", "disable"]
    dstaddr6: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstaddr6Item]
    dstaddr6_negate: Literal["enable", "disable"]
    internet_service: Literal["enable", "disable"]
    internet_service_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicenameItem]
    internet_service_negate: Literal["enable", "disable"]
    internet_service_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicegroupItem]
    internet_service_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicecustomItem]
    internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicecustomgroupItem]
    internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicefortiguardItem]
    internet_service_src: Literal["enable", "disable"]
    internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcnameItem]
    internet_service_src_negate: Literal["enable", "disable"]
    internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcgroupItem]
    internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrccustomItem]
    internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrccustomgroupItem]
    internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcfortiguardItem]
    internet_service6: Literal["enable", "disable"]
    internet_service6_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6nameItem]
    internet_service6_negate: Literal["enable", "disable"]
    internet_service6_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6groupItem]
    internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6customItem]
    internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6customgroupItem]
    internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6fortiguardItem]
    internet_service6_src: Literal["enable", "disable"]
    internet_service6_src_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcnameItem]
    internet_service6_src_negate: Literal["enable", "disable"]
    internet_service6_src_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcgroupItem]
    internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srccustomItem]
    internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srccustomgroupItem]
    internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcfortiguardItem]
    enforce_default_app_port: Literal["enable", "disable"]
    service: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyServiceItem]
    service_negate: Literal["enable", "disable"]
    action: Literal["accept", "deny"]
    send_deny_packet: Literal["disable", "enable"]
    schedule: str
    status: Literal["enable", "disable"]
    logtraffic: Literal["all", "utm", "disable"]
    learning_mode: Literal["enable", "disable"]
    nat46: Literal["enable", "disable"]
    nat64: Literal["enable", "disable"]
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
    ssh_filter_profile: str
    casb_profile: str
    application: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyApplicationItem]
    app_category: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyAppcategoryItem]
    url_category: str | list[str]
    app_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyAppgroupItem]
    groups: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyGroupsItem]
    users: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyUsersItem]
    fsso_groups: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyFssogroupsItem]


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class SecurityPolicyResponse(TypedDict, total=False):
    """Response type for SecurityPolicy - use with .dict property for typed dict access."""
    uuid: str
    policyid: int
    name: str
    comments: str
    srcintf: list[SecurityPolicySrcintfItem]
    dstintf: list[SecurityPolicyDstintfItem]
    srcaddr: list[SecurityPolicySrcaddrItem]
    srcaddr_negate: Literal["enable", "disable"]
    dstaddr: list[SecurityPolicyDstaddrItem]
    dstaddr_negate: Literal["enable", "disable"]
    srcaddr6: list[SecurityPolicySrcaddr6Item]
    srcaddr6_negate: Literal["enable", "disable"]
    dstaddr6: list[SecurityPolicyDstaddr6Item]
    dstaddr6_negate: Literal["enable", "disable"]
    internet_service: Literal["enable", "disable"]
    internet_service_name: list[SecurityPolicyInternetservicenameItem]
    internet_service_negate: Literal["enable", "disable"]
    internet_service_group: list[SecurityPolicyInternetservicegroupItem]
    internet_service_custom: list[SecurityPolicyInternetservicecustomItem]
    internet_service_custom_group: list[SecurityPolicyInternetservicecustomgroupItem]
    internet_service_fortiguard: list[SecurityPolicyInternetservicefortiguardItem]
    internet_service_src: Literal["enable", "disable"]
    internet_service_src_name: list[SecurityPolicyInternetservicesrcnameItem]
    internet_service_src_negate: Literal["enable", "disable"]
    internet_service_src_group: list[SecurityPolicyInternetservicesrcgroupItem]
    internet_service_src_custom: list[SecurityPolicyInternetservicesrccustomItem]
    internet_service_src_custom_group: list[SecurityPolicyInternetservicesrccustomgroupItem]
    internet_service_src_fortiguard: list[SecurityPolicyInternetservicesrcfortiguardItem]
    internet_service6: Literal["enable", "disable"]
    internet_service6_name: list[SecurityPolicyInternetservice6nameItem]
    internet_service6_negate: Literal["enable", "disable"]
    internet_service6_group: list[SecurityPolicyInternetservice6groupItem]
    internet_service6_custom: list[SecurityPolicyInternetservice6customItem]
    internet_service6_custom_group: list[SecurityPolicyInternetservice6customgroupItem]
    internet_service6_fortiguard: list[SecurityPolicyInternetservice6fortiguardItem]
    internet_service6_src: Literal["enable", "disable"]
    internet_service6_src_name: list[SecurityPolicyInternetservice6srcnameItem]
    internet_service6_src_negate: Literal["enable", "disable"]
    internet_service6_src_group: list[SecurityPolicyInternetservice6srcgroupItem]
    internet_service6_src_custom: list[SecurityPolicyInternetservice6srccustomItem]
    internet_service6_src_custom_group: list[SecurityPolicyInternetservice6srccustomgroupItem]
    internet_service6_src_fortiguard: list[SecurityPolicyInternetservice6srcfortiguardItem]
    enforce_default_app_port: Literal["enable", "disable"]
    service: list[SecurityPolicyServiceItem]
    service_negate: Literal["enable", "disable"]
    action: Literal["accept", "deny"]
    send_deny_packet: Literal["disable", "enable"]
    schedule: str
    status: Literal["enable", "disable"]
    logtraffic: Literal["all", "utm", "disable"]
    learning_mode: Literal["enable", "disable"]
    nat46: Literal["enable", "disable"]
    nat64: Literal["enable", "disable"]
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
    ssh_filter_profile: str
    casb_profile: str
    application: list[SecurityPolicyApplicationItem]
    app_category: list[SecurityPolicyAppcategoryItem]
    url_category: str | list[str]
    app_group: list[SecurityPolicyAppgroupItem]
    groups: list[SecurityPolicyGroupsItem]
    users: list[SecurityPolicyUsersItem]
    fsso_groups: list[SecurityPolicyFssogroupsItem]


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class SecurityPolicyObject(FortiObject):
    """Typed FortiObject for SecurityPolicy with field access."""
    uuid: str
    policyid: int
    name: str
    comments: str
    srcintf: list[SecurityPolicySrcintfItem]
    dstintf: list[SecurityPolicyDstintfItem]
    srcaddr: list[SecurityPolicySrcaddrItem]
    srcaddr_negate: Literal["enable", "disable"]
    dstaddr: list[SecurityPolicyDstaddrItem]
    dstaddr_negate: Literal["enable", "disable"]
    srcaddr6: list[SecurityPolicySrcaddr6Item]
    srcaddr6_negate: Literal["enable", "disable"]
    dstaddr6: list[SecurityPolicyDstaddr6Item]
    dstaddr6_negate: Literal["enable", "disable"]
    internet_service: Literal["enable", "disable"]
    internet_service_name: list[SecurityPolicyInternetservicenameItem]
    internet_service_negate: Literal["enable", "disable"]
    internet_service_group: list[SecurityPolicyInternetservicegroupItem]
    internet_service_custom: list[SecurityPolicyInternetservicecustomItem]
    internet_service_custom_group: list[SecurityPolicyInternetservicecustomgroupItem]
    internet_service_fortiguard: list[SecurityPolicyInternetservicefortiguardItem]
    internet_service_src: Literal["enable", "disable"]
    internet_service_src_name: list[SecurityPolicyInternetservicesrcnameItem]
    internet_service_src_negate: Literal["enable", "disable"]
    internet_service_src_group: list[SecurityPolicyInternetservicesrcgroupItem]
    internet_service_src_custom: list[SecurityPolicyInternetservicesrccustomItem]
    internet_service_src_custom_group: list[SecurityPolicyInternetservicesrccustomgroupItem]
    internet_service_src_fortiguard: list[SecurityPolicyInternetservicesrcfortiguardItem]
    internet_service6: Literal["enable", "disable"]
    internet_service6_name: list[SecurityPolicyInternetservice6nameItem]
    internet_service6_negate: Literal["enable", "disable"]
    internet_service6_group: list[SecurityPolicyInternetservice6groupItem]
    internet_service6_custom: list[SecurityPolicyInternetservice6customItem]
    internet_service6_custom_group: list[SecurityPolicyInternetservice6customgroupItem]
    internet_service6_fortiguard: list[SecurityPolicyInternetservice6fortiguardItem]
    internet_service6_src: Literal["enable", "disable"]
    internet_service6_src_name: list[SecurityPolicyInternetservice6srcnameItem]
    internet_service6_src_negate: Literal["enable", "disable"]
    internet_service6_src_group: list[SecurityPolicyInternetservice6srcgroupItem]
    internet_service6_src_custom: list[SecurityPolicyInternetservice6srccustomItem]
    internet_service6_src_custom_group: list[SecurityPolicyInternetservice6srccustomgroupItem]
    internet_service6_src_fortiguard: list[SecurityPolicyInternetservice6srcfortiguardItem]
    enforce_default_app_port: Literal["enable", "disable"]
    service: list[SecurityPolicyServiceItem]
    service_negate: Literal["enable", "disable"]
    action: Literal["accept", "deny"]
    send_deny_packet: Literal["disable", "enable"]
    schedule: str
    status: Literal["enable", "disable"]
    logtraffic: Literal["all", "utm", "disable"]
    learning_mode: Literal["enable", "disable"]
    nat46: Literal["enable", "disable"]
    nat64: Literal["enable", "disable"]
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
    ssh_filter_profile: str
    casb_profile: str
    application: list[SecurityPolicyApplicationItem]
    app_category: list[SecurityPolicyAppcategoryItem]
    url_category: str | list[str]
    app_group: list[SecurityPolicyAppgroupItem]
    groups: list[SecurityPolicyGroupsItem]
    users: list[SecurityPolicyUsersItem]
    fsso_groups: list[SecurityPolicyFssogroupsItem]


# ================================================================
# Main Endpoint Class
# ================================================================

class SecurityPolicy:
    """
    
    Endpoint: firewall/security_policy
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
    ) -> SecurityPolicyObject: ...
    
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
    ) -> FortiObjectList[SecurityPolicyObject]: ...
    
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
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstintfItem] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcaddrItem] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstaddrItem] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcaddr6Item] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstaddr6Item] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicenameItem] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicecustomItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicefortiguardItem] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcnameItem] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcgroupItem] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrccustomItem] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrccustomgroupItem] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcfortiguardItem] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6nameItem] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6groupItem] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6customItem] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6customgroupItem] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6fortiguardItem] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcnameItem] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcgroupItem] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srccustomItem] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srccustomgroupItem] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcfortiguardItem] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyServiceItem] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
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
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyApplicationItem] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyAppcategoryItem] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyAppgroupItem] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyGroupsItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyUsersItem] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyFssogroupsItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> SecurityPolicyObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstintfItem] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcaddrItem] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstaddrItem] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcaddr6Item] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstaddr6Item] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicenameItem] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicecustomItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicefortiguardItem] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcnameItem] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcgroupItem] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrccustomItem] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrccustomgroupItem] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcfortiguardItem] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6nameItem] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6groupItem] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6customItem] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6customgroupItem] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6fortiguardItem] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcnameItem] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcgroupItem] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srccustomItem] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srccustomgroupItem] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcfortiguardItem] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyServiceItem] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
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
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyApplicationItem] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyAppcategoryItem] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyAppgroupItem] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyGroupsItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyUsersItem] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyFssogroupsItem] | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> SecurityPolicyObject: ...

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
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstintfItem] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcaddrItem] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstaddrItem] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[SecurityPolicySrcaddr6Item] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyDstaddr6Item] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicenameItem] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicecustomItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicefortiguardItem] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcnameItem] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcgroupItem] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrccustomItem] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrccustomgroupItem] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservicesrcfortiguardItem] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6nameItem] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6groupItem] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6customItem] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6customgroupItem] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6fortiguardItem] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcnameItem] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcgroupItem] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srccustomItem] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srccustomgroupItem] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyInternetservice6srcfortiguardItem] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyServiceItem] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
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
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyApplicationItem] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyAppcategoryItem] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyAppgroupItem] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyGroupsItem] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyUsersItem] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | list[SecurityPolicyFssogroupsItem] | None = ...,
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
    "SecurityPolicy",
    "SecurityPolicyPayload",
    "SecurityPolicyResponse",
    "SecurityPolicyObject",
]