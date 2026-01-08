from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ShapingPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/shaping_policy payload fields.
    
    Configure shaping policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.schedule.group.GroupEndpoint` (via: schedule)
        - :class:`~.firewall.schedule.onetime.OnetimeEndpoint` (via: schedule)
        - :class:`~.firewall.schedule.recurring.RecurringEndpoint` (via: schedule)
        - :class:`~.firewall.shaper.per-ip-shaper.PerIpShaperEndpoint` (via: per-ip-shaper)
        - :class:`~.firewall.shaper.traffic-shaper.TrafficShaperEndpoint` (via: traffic-shaper, traffic-shaper-reverse)
        - :class:`~.firewall.traffic-class.TrafficClassEndpoint` (via: class-id)

    **Usage:**
        payload: ShapingPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Shaping policy ID (0 - 4294967295).
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    name: NotRequired[str]  # Shaping policy name.
    comment: NotRequired[str]  # Comments.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this traffic shaping policy.
    ip_version: NotRequired[Literal["4", "6"]]  # Apply this traffic shaping policy to IPv4 or IPv6 traffic.
    traffic_type: NotRequired[Literal["forwarding", "local-in", "local-out"]]  # Traffic type.
    srcaddr: list[dict[str, Any]]  # IPv4 source address and address group names.
    dstaddr: list[dict[str, Any]]  # IPv4 destination address and address group names.
    srcaddr6: list[dict[str, Any]]  # IPv6 source address and address group names.
    dstaddr6: list[dict[str, Any]]  # IPv6 destination address and address group names.
    internet_service: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services for this policy. If 
    internet_service_name: NotRequired[list[dict[str, Any]]]  # Internet Service ID.
    internet_service_group: NotRequired[list[dict[str, Any]]]  # Internet Service group name.
    internet_service_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service name.
    internet_service_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service group name.
    internet_service_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service name.
    internet_service_src: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services in source for this p
    internet_service_src_name: NotRequired[list[dict[str, Any]]]  # Internet Service source name.
    internet_service_src_group: NotRequired[list[dict[str, Any]]]  # Internet Service source group name.
    internet_service_src_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source name.
    internet_service_src_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source group name.
    internet_service_src_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service source name.
    service: list[dict[str, Any]]  # Service and service group names.
    schedule: NotRequired[str]  # Schedule name.
    users: NotRequired[list[dict[str, Any]]]  # Apply this traffic shaping policy to individual users that h
    groups: NotRequired[list[dict[str, Any]]]  # Apply this traffic shaping policy to user groups that have a
    application: NotRequired[list[dict[str, Any]]]  # IDs of one or more applications that this shaper applies app
    app_category: NotRequired[list[dict[str, Any]]]  # IDs of one or more application categories that this shaper a
    app_group: NotRequired[list[dict[str, Any]]]  # One or more application group names.
    url_category: NotRequired[list[dict[str, Any]]]  # IDs of one or more FortiGuard Web Filtering categories that 
    srcintf: NotRequired[list[dict[str, Any]]]  # One or more incoming (ingress) interfaces.
    dstintf: list[dict[str, Any]]  # One or more outgoing (egress) interfaces.
    tos_mask: NotRequired[str]  # Non-zero bit positions are used for comparison while zero bi
    tos: NotRequired[str]  # ToS (Type of Service) value used for comparison.
    tos_negate: NotRequired[Literal["enable", "disable"]]  # Enable negated TOS match.
    traffic_shaper: NotRequired[str]  # Traffic shaper to apply to traffic forwarded by the firewall
    traffic_shaper_reverse: NotRequired[str]  # Traffic shaper to apply to response traffic received by the 
    per_ip_shaper: NotRequired[str]  # Per-IP traffic shaper to apply with this policy.
    class_id: NotRequired[int]  # Traffic class ID.
    diffserv_forward: NotRequired[Literal["enable", "disable"]]  # Enable to change packet's DiffServ values to the specified d
    diffserv_reverse: NotRequired[Literal["enable", "disable"]]  # Enable to change packet's reverse (reply) DiffServ values to
    diffservcode_forward: NotRequired[str]  # Change packet's DiffServ to this value.
    diffservcode_rev: NotRequired[str]  # Change packet's reverse (reply) DiffServ to this value.
    cos_mask: NotRequired[str]  # VLAN CoS evaluated bits.
    cos: NotRequired[str]  # VLAN CoS bit pattern.


class ShapingPolicyObject(FortiObject[ShapingPolicyPayload]):
    """Typed FortiObject for firewall/shaping_policy with IDE autocomplete support."""
    
    # Shaping policy ID (0 - 4294967295).
    id: int
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Shaping policy name.
    name: str
    # Comments.
    comment: str
    # Enable/disable this traffic shaping policy.
    status: Literal["enable", "disable"]
    # Apply this traffic shaping policy to IPv4 or IPv6 traffic.
    ip_version: Literal["4", "6"]
    # Traffic type.
    traffic_type: Literal["forwarding", "local-in", "local-out"]
    # IPv4 source address and address group names.
    srcaddr: list[str]  # Auto-flattened from member_table
    # IPv4 destination address and address group names.
    dstaddr: list[str]  # Auto-flattened from member_table
    # IPv6 source address and address group names.
    srcaddr6: list[str]  # Auto-flattened from member_table
    # IPv6 destination address and address group names.
    dstaddr6: list[str]  # Auto-flattened from member_table
    # Enable/disable use of Internet Services for this policy. If enabled, destination
    internet_service: Literal["enable", "disable"]
    # Internet Service ID.
    internet_service_name: list[str]  # Auto-flattened from member_table
    # Internet Service group name.
    internet_service_group: list[str]  # Auto-flattened from member_table
    # Custom Internet Service name.
    internet_service_custom: list[str]  # Auto-flattened from member_table
    # Custom Internet Service group name.
    internet_service_custom_group: list[str]  # Auto-flattened from member_table
    # FortiGuard Internet Service name.
    internet_service_fortiguard: list[str]  # Auto-flattened from member_table
    # Enable/disable use of Internet Services in source for this policy. If enabled, s
    internet_service_src: Literal["enable", "disable"]
    # Internet Service source name.
    internet_service_src_name: list[str]  # Auto-flattened from member_table
    # Internet Service source group name.
    internet_service_src_group: list[str]  # Auto-flattened from member_table
    # Custom Internet Service source name.
    internet_service_src_custom: list[str]  # Auto-flattened from member_table
    # Custom Internet Service source group name.
    internet_service_src_custom_group: list[str]  # Auto-flattened from member_table
    # FortiGuard Internet Service source name.
    internet_service_src_fortiguard: list[str]  # Auto-flattened from member_table
    # Service and service group names.
    service: list[str]  # Auto-flattened from member_table
    # Schedule name.
    schedule: str
    # Apply this traffic shaping policy to individual users that have authenticated wi
    users: list[str]  # Auto-flattened from member_table
    # Apply this traffic shaping policy to user groups that have authenticated with th
    groups: list[str]  # Auto-flattened from member_table
    # IDs of one or more applications that this shaper applies application control tra
    application: list[str]  # Auto-flattened from member_table
    # IDs of one or more application categories that this shaper applies application c
    app_category: list[str]  # Auto-flattened from member_table
    # One or more application group names.
    app_group: list[str]  # Auto-flattened from member_table
    # IDs of one or more FortiGuard Web Filtering categories that this shaper applies 
    url_category: list[str]  # Auto-flattened from member_table
    # One or more incoming (ingress) interfaces.
    srcintf: list[str]  # Auto-flattened from member_table
    # One or more outgoing (egress) interfaces.
    dstintf: list[str]  # Auto-flattened from member_table
    # Non-zero bit positions are used for comparison while zero bit positions are igno
    tos_mask: str
    # ToS (Type of Service) value used for comparison.
    tos: str
    # Enable negated TOS match.
    tos_negate: Literal["enable", "disable"]
    # Traffic shaper to apply to traffic forwarded by the firewall policy.
    traffic_shaper: str
    # Traffic shaper to apply to response traffic received by the firewall policy.
    traffic_shaper_reverse: str
    # Per-IP traffic shaper to apply with this policy.
    per_ip_shaper: str
    # Traffic class ID.
    class_id: int
    # Enable to change packet's DiffServ values to the specified diffservcode-forward 
    diffserv_forward: Literal["enable", "disable"]
    # Enable to change packet's reverse (reply) DiffServ values to the specified diffs
    diffserv_reverse: Literal["enable", "disable"]
    # Change packet's DiffServ to this value.
    diffservcode_forward: str
    # Change packet's reverse (reply) DiffServ to this value.
    diffservcode_rev: str
    # VLAN CoS evaluated bits.
    cos_mask: str
    # VLAN CoS bit pattern.
    cos: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ShapingPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ShapingPolicy:
    """
    Configure shaping policies.
    
    Path: firewall/shaping_policy
    Category: cmdb
    Primary Key: id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> ShapingPolicyObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[ShapingPolicyObject]: ...
    
    @overload
    def get(
        self,
        id: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        id: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        id: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        id: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> ShapingPolicyObject | list[ShapingPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ShapingPolicyObject: ...
    
    @overload
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
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ShapingPolicyObject: ...
    
    @overload
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
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ShapingPolicyObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | list[dict[str, Any]] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
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
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> dict[str, Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> dict[str, Any]: ...
    
    @staticmethod
    def schema() -> dict[str, Any]: ...


__all__ = [
    "ShapingPolicy",
    "ShapingPolicyPayload",
    "ShapingPolicyObject",
]