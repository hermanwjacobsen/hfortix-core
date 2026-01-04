from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ShapingPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/shaping_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class ShapingPolicy:
    """
    Configure shaping policies.
    
    Path: firewall/shaping_policy
    Category: cmdb
    Primary Key: id
    """
    
    def get(
        self,
        id: int | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        srcaddr: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        srcaddr6: list[dict[str, Any]] | None = ...,
        dstaddr6: list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: list[dict[str, Any]] | None = ...,
        internet_service_group: list[dict[str, Any]] | None = ...,
        internet_service_custom: list[dict[str, Any]] | None = ...,
        internet_service_custom_group: list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: list[dict[str, Any]] | None = ...,
        internet_service_src_group: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        srcaddr: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        srcaddr6: list[dict[str, Any]] | None = ...,
        dstaddr6: list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: list[dict[str, Any]] | None = ...,
        internet_service_group: list[dict[str, Any]] | None = ...,
        internet_service_custom: list[dict[str, Any]] | None = ...,
        internet_service_custom_group: list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: list[dict[str, Any]] | None = ...,
        internet_service_src_group: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: ShapingPolicyPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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