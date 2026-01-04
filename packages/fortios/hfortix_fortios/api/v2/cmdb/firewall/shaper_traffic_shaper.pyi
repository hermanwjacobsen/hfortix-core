from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ShaperTrafficShaperPayload(TypedDict, total=False):
    """
    Type hints for firewall/shaper_traffic_shaper payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ShaperTrafficShaperPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Traffic shaper name.
    guaranteed_bandwidth: NotRequired[int]  # Amount of bandwidth guaranteed for this shaper (0 - 80000000
    maximum_bandwidth: NotRequired[int]  # Upper bandwidth limit enforced by this shaper (0 - 80000000)
    bandwidth_unit: NotRequired[Literal["kbps", "mbps", "gbps"]]  # Unit of measurement for guaranteed and maximum bandwidth for
    priority: NotRequired[Literal["low", "medium", "high"]]  # Higher priority traffic is more likely to be forwarded witho
    per_policy: NotRequired[Literal["disable", "enable"]]  # Enable/disable applying a separate shaper for each policy. F
    diffserv: NotRequired[Literal["enable", "disable"]]  # Enable/disable changing the DiffServ setting applied to traf
    diffservcode: NotRequired[str]  # DiffServ setting to be applied to traffic accepted by this s
    dscp_marking_method: NotRequired[Literal["multi-stage", "static"]]  # Select DSCP marking method.
    exceed_bandwidth: NotRequired[int]  # Exceed bandwidth used for DSCP/VLAN CoS multi-stage marking.
    exceed_dscp: NotRequired[str]  # DSCP mark for traffic in guaranteed-bandwidth and exceed-ban
    maximum_dscp: NotRequired[str]  # DSCP mark for traffic in exceed-bandwidth and maximum-bandwi
    cos_marking: NotRequired[Literal["enable", "disable"]]  # Enable/disable VLAN CoS marking.
    cos_marking_method: NotRequired[Literal["multi-stage", "static"]]  # Select VLAN CoS marking method.
    cos: NotRequired[str]  # VLAN CoS mark.
    exceed_cos: NotRequired[str]  # VLAN CoS mark for traffic in [guaranteed-bandwidth, exceed-b
    maximum_cos: NotRequired[str]  # VLAN CoS mark for traffic in [exceed-bandwidth, maximum-band
    overhead: NotRequired[int]  # Per-packet size overhead used in rate computations.
    exceed_class_id: NotRequired[int]  # Class ID for traffic in guaranteed-bandwidth and maximum-ban


class ShaperTrafficShaper:
    """
    Configure shared traffic shaper.
    
    Path: firewall/shaper_traffic_shaper
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
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
        payload_dict: ShaperTrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ShaperTrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: ShaperTrafficShaperPayload | None = ...,
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