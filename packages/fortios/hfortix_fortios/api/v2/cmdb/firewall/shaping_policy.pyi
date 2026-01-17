""" - Type Stubs

Auto-generated stub file for type checking and IDE support.

Endpoint: firewall/shaping_policy
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

class ShapingPolicySrcaddrItem:
    """Nested item for srcaddr field - supports attribute access."""
    name: str


class ShapingPolicyDstaddrItem:
    """Nested item for dstaddr field - supports attribute access."""
    name: str


class ShapingPolicySrcaddr6Item:
    """Nested item for srcaddr6 field - supports attribute access."""
    name: str


class ShapingPolicyDstaddr6Item:
    """Nested item for dstaddr6 field - supports attribute access."""
    name: str


class ShapingPolicyInternetservicenameItem:
    """Nested item for internet-service-name field - supports attribute access."""
    name: str


class ShapingPolicyInternetservicegroupItem:
    """Nested item for internet-service-group field - supports attribute access."""
    name: str


class ShapingPolicyInternetservicecustomItem:
    """Nested item for internet-service-custom field - supports attribute access."""
    name: str


class ShapingPolicyInternetservicecustomgroupItem:
    """Nested item for internet-service-custom-group field - supports attribute access."""
    name: str


class ShapingPolicyInternetservicefortiguardItem:
    """Nested item for internet-service-fortiguard field - supports attribute access."""
    name: str


class ShapingPolicyInternetservicesrcnameItem:
    """Nested item for internet-service-src-name field - supports attribute access."""
    name: str


class ShapingPolicyInternetservicesrcgroupItem:
    """Nested item for internet-service-src-group field - supports attribute access."""
    name: str


class ShapingPolicyInternetservicesrccustomItem:
    """Nested item for internet-service-src-custom field - supports attribute access."""
    name: str


class ShapingPolicyInternetservicesrccustomgroupItem:
    """Nested item for internet-service-src-custom-group field - supports attribute access."""
    name: str


class ShapingPolicyInternetservicesrcfortiguardItem:
    """Nested item for internet-service-src-fortiguard field - supports attribute access."""
    name: str


class ShapingPolicyServiceItem:
    """Nested item for service field - supports attribute access."""
    name: str


class ShapingPolicyUsersItem:
    """Nested item for users field - supports attribute access."""
    name: str


class ShapingPolicyGroupsItem:
    """Nested item for groups field - supports attribute access."""
    name: str


class ShapingPolicyApplicationItem:
    """Nested item for application field - supports attribute access."""
    id: int


class ShapingPolicyAppcategoryItem:
    """Nested item for app-category field - supports attribute access."""
    id: int


class ShapingPolicyAppgroupItem:
    """Nested item for app-group field - supports attribute access."""
    name: str


class ShapingPolicyUrlcategoryItem:
    """Nested item for url-category field - supports attribute access."""
    id: int


class ShapingPolicySrcintfItem:
    """Nested item for srcintf field - supports attribute access."""
    name: str


class ShapingPolicyDstintfItem:
    """Nested item for dstintf field - supports attribute access."""
    name: str


class ShapingPolicyPayload(TypedDict, total=False):
    """Payload type for ShapingPolicy operations."""
    id: int
    uuid: str
    name: str
    comment: str
    status: Literal["enable", "disable"]
    ip_version: Literal["4", "6"]
    traffic_type: Literal["forwarding", "local-in", "local-out"]
    srcaddr: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcaddrItem]
    dstaddr: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstaddrItem]
    srcaddr6: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcaddr6Item]
    dstaddr6: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstaddr6Item]
    internet_service: Literal["enable", "disable"]
    internet_service_name: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicenameItem]
    internet_service_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicegroupItem]
    internet_service_custom: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicecustomItem]
    internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicecustomgroupItem]
    internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicefortiguardItem]
    internet_service_src: Literal["enable", "disable"]
    internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcnameItem]
    internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcgroupItem]
    internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrccustomItem]
    internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrccustomgroupItem]
    internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcfortiguardItem]
    service: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyServiceItem]
    schedule: str
    users: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyUsersItem]
    groups: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyGroupsItem]
    application: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyApplicationItem]
    app_category: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyAppcategoryItem]
    app_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyAppgroupItem]
    url_category: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyUrlcategoryItem]
    srcintf: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcintfItem]
    dstintf: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstintfItem]
    tos_mask: str
    tos: str
    tos_negate: Literal["enable", "disable"]
    traffic_shaper: str
    traffic_shaper_reverse: str
    per_ip_shaper: str
    class_id: int
    diffserv_forward: Literal["enable", "disable"]
    diffserv_reverse: Literal["enable", "disable"]
    diffservcode_forward: str
    diffservcode_rev: str
    cos_mask: str
    cos: str


# ================================================================
# Response Types (TypedDict for dict-style access)
# ================================================================

class ShapingPolicyResponse(TypedDict, total=False):
    """Response type for ShapingPolicy - use with .dict property for typed dict access."""
    id: int
    uuid: str
    name: str
    comment: str
    status: Literal["enable", "disable"]
    ip_version: Literal["4", "6"]
    traffic_type: Literal["forwarding", "local-in", "local-out"]
    srcaddr: list[ShapingPolicySrcaddrItem]
    dstaddr: list[ShapingPolicyDstaddrItem]
    srcaddr6: list[ShapingPolicySrcaddr6Item]
    dstaddr6: list[ShapingPolicyDstaddr6Item]
    internet_service: Literal["enable", "disable"]
    internet_service_name: list[ShapingPolicyInternetservicenameItem]
    internet_service_group: list[ShapingPolicyInternetservicegroupItem]
    internet_service_custom: list[ShapingPolicyInternetservicecustomItem]
    internet_service_custom_group: list[ShapingPolicyInternetservicecustomgroupItem]
    internet_service_fortiguard: list[ShapingPolicyInternetservicefortiguardItem]
    internet_service_src: Literal["enable", "disable"]
    internet_service_src_name: list[ShapingPolicyInternetservicesrcnameItem]
    internet_service_src_group: list[ShapingPolicyInternetservicesrcgroupItem]
    internet_service_src_custom: list[ShapingPolicyInternetservicesrccustomItem]
    internet_service_src_custom_group: list[ShapingPolicyInternetservicesrccustomgroupItem]
    internet_service_src_fortiguard: list[ShapingPolicyInternetservicesrcfortiguardItem]
    service: list[ShapingPolicyServiceItem]
    schedule: str
    users: list[ShapingPolicyUsersItem]
    groups: list[ShapingPolicyGroupsItem]
    application: list[ShapingPolicyApplicationItem]
    app_category: list[ShapingPolicyAppcategoryItem]
    app_group: list[ShapingPolicyAppgroupItem]
    url_category: list[ShapingPolicyUrlcategoryItem]
    srcintf: list[ShapingPolicySrcintfItem]
    dstintf: list[ShapingPolicyDstintfItem]
    tos_mask: str
    tos: str
    tos_negate: Literal["enable", "disable"]
    traffic_shaper: str
    traffic_shaper_reverse: str
    per_ip_shaper: str
    class_id: int
    diffserv_forward: Literal["enable", "disable"]
    diffserv_reverse: Literal["enable", "disable"]
    diffservcode_forward: str
    diffservcode_rev: str
    cos_mask: str
    cos: str


# ================================================================
# Response Types (Class for attribute access)
# ================================================================


class ShapingPolicyObject(FortiObject):
    """Typed FortiObject for ShapingPolicy with field access."""
    id: int
    uuid: str
    name: str
    comment: str
    status: Literal["enable", "disable"]
    ip_version: Literal["4", "6"]
    traffic_type: Literal["forwarding", "local-in", "local-out"]
    srcaddr: list[ShapingPolicySrcaddrItem]
    dstaddr: list[ShapingPolicyDstaddrItem]
    srcaddr6: list[ShapingPolicySrcaddr6Item]
    dstaddr6: list[ShapingPolicyDstaddr6Item]
    internet_service: Literal["enable", "disable"]
    internet_service_name: list[ShapingPolicyInternetservicenameItem]
    internet_service_group: list[ShapingPolicyInternetservicegroupItem]
    internet_service_custom: list[ShapingPolicyInternetservicecustomItem]
    internet_service_custom_group: list[ShapingPolicyInternetservicecustomgroupItem]
    internet_service_fortiguard: list[ShapingPolicyInternetservicefortiguardItem]
    internet_service_src: Literal["enable", "disable"]
    internet_service_src_name: list[ShapingPolicyInternetservicesrcnameItem]
    internet_service_src_group: list[ShapingPolicyInternetservicesrcgroupItem]
    internet_service_src_custom: list[ShapingPolicyInternetservicesrccustomItem]
    internet_service_src_custom_group: list[ShapingPolicyInternetservicesrccustomgroupItem]
    internet_service_src_fortiguard: list[ShapingPolicyInternetservicesrcfortiguardItem]
    service: list[ShapingPolicyServiceItem]
    schedule: str
    users: list[ShapingPolicyUsersItem]
    groups: list[ShapingPolicyGroupsItem]
    application: list[ShapingPolicyApplicationItem]
    app_category: list[ShapingPolicyAppcategoryItem]
    app_group: list[ShapingPolicyAppgroupItem]
    url_category: list[ShapingPolicyUrlcategoryItem]
    srcintf: list[ShapingPolicySrcintfItem]
    dstintf: list[ShapingPolicyDstintfItem]
    tos_mask: str
    tos: str
    tos_negate: Literal["enable", "disable"]
    traffic_shaper: str
    traffic_shaper_reverse: str
    per_ip_shaper: str
    class_id: int
    diffserv_forward: Literal["enable", "disable"]
    diffserv_reverse: Literal["enable", "disable"]
    diffservcode_forward: str
    diffservcode_rev: str
    cos_mask: str
    cos: str


# ================================================================
# Main Endpoint Class
# ================================================================

class ShapingPolicy:
    """
    
    Endpoint: firewall/shaping_policy
    Category: cmdb
    MKey: id
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
        id: int,
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
    ) -> ShapingPolicyObject: ...
    
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
    ) -> FortiObjectList[ShapingPolicyObject]: ...
    
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
        payload_dict: ShapingPolicyPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        traffic_type: Literal["forwarding", "local-in", "local-out"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcaddrItem] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstaddrItem] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcaddr6Item] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstaddr6Item] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicenameItem] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicecustomItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicefortiguardItem] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcnameItem] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcgroupItem] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrccustomItem] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrccustomgroupItem] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcfortiguardItem] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyServiceItem] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyUsersItem] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyGroupsItem] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyApplicationItem] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyAppcategoryItem] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyAppgroupItem] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyUrlcategoryItem] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstintfItem] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        class_id: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        cos_mask: str | None = ...,
        cos: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ShapingPolicyObject: ...

    # ================================================================
    # PUT Method
    # ================================================================
    
    def put(
        self,
        payload_dict: ShapingPolicyPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        traffic_type: Literal["forwarding", "local-in", "local-out"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcaddrItem] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstaddrItem] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcaddr6Item] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstaddr6Item] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicenameItem] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicecustomItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicefortiguardItem] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcnameItem] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcgroupItem] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrccustomItem] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrccustomgroupItem] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcfortiguardItem] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyServiceItem] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyUsersItem] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyGroupsItem] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyApplicationItem] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyAppcategoryItem] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyAppgroupItem] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyUrlcategoryItem] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstintfItem] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        class_id: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        cos_mask: str | None = ...,
        cos: str | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> ShapingPolicyObject: ...

    # ================================================================
    # DELETE Method
    # ================================================================
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        error_mode: Literal["raise", "return", "print"] | None = ...,
        error_format: Literal["detailed", "simple", "code_only"] | None = ...,
    ) -> FortiObject: ...

    # ================================================================
    # Utility Methods
    # ================================================================
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ShapingPolicyPayload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        traffic_type: Literal["forwarding", "local-in", "local-out"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcaddrItem] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstaddrItem] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcaddr6Item] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstaddr6Item] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicenameItem] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicegroupItem] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicecustomItem] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicecustomgroupItem] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicefortiguardItem] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcnameItem] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcgroupItem] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrccustomItem] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrccustomgroupItem] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyInternetservicesrcfortiguardItem] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyServiceItem] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyUsersItem] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyGroupsItem] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyApplicationItem] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyAppcategoryItem] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyAppgroupItem] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyUrlcategoryItem] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | list[ShapingPolicySrcintfItem] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | list[ShapingPolicyDstintfItem] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        class_id: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        cos_mask: str | None = ...,
        cos: str | None = ...,
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
    "ShapingPolicy",
    "ShapingPolicyPayload",
    "ShapingPolicyResponse",
    "ShapingPolicyObject",
]