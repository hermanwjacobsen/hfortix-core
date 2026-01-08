from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class TrafficShaperPayload(TypedDict, total=False):
    """
    Type hints for firewall/shaper/traffic_shaper payload fields.
    
    Configure shared traffic shaper.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.traffic-class.TrafficClassEndpoint` (via: exceed-class-id)

    **Usage:**
        payload: TrafficShaperPayload = {
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


class TrafficShaperObject(FortiObject[TrafficShaperPayload]):
    """Typed FortiObject for firewall/shaper/traffic_shaper with IDE autocomplete support."""
    
    # Traffic shaper name.
    name: str
    # Amount of bandwidth guaranteed for this shaper (0 - 80000000). Units depend on t
    guaranteed_bandwidth: int
    # Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit. 
    maximum_bandwidth: int
    # Unit of measurement for guaranteed and maximum bandwidth for this shaper (Kbps, 
    bandwidth_unit: Literal["kbps", "mbps", "gbps"]
    # Higher priority traffic is more likely to be forwarded without delays and withou
    priority: Literal["low", "medium", "high"]
    # Enable/disable applying a separate shaper for each policy. For example, if enabl
    per_policy: Literal["disable", "enable"]
    # Enable/disable changing the DiffServ setting applied to traffic accepted by this
    diffserv: Literal["enable", "disable"]
    # DiffServ setting to be applied to traffic accepted by this shaper.
    diffservcode: str
    # Select DSCP marking method.
    dscp_marking_method: Literal["multi-stage", "static"]
    # Exceed bandwidth used for DSCP/VLAN CoS multi-stage marking. Units depend on the
    exceed_bandwidth: int
    # DSCP mark for traffic in guaranteed-bandwidth and exceed-bandwidth.
    exceed_dscp: str
    # DSCP mark for traffic in exceed-bandwidth and maximum-bandwidth.
    maximum_dscp: str
    # Enable/disable VLAN CoS marking.
    cos_marking: Literal["enable", "disable"]
    # Select VLAN CoS marking method.
    cos_marking_method: Literal["multi-stage", "static"]
    # VLAN CoS mark.
    cos: str
    # VLAN CoS mark for traffic in [guaranteed-bandwidth, exceed-bandwidth].
    exceed_cos: str
    # VLAN CoS mark for traffic in [exceed-bandwidth, maximum-bandwidth].
    maximum_cos: str
    # Per-packet size overhead used in rate computations.
    overhead: int
    # Class ID for traffic in guaranteed-bandwidth and maximum-bandwidth.
    exceed_class_id: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> TrafficShaperPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class TrafficShaper:
    """
    Configure shared traffic shaper.
    
    Path: firewall/shaper/traffic_shaper
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        name: str,
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
    ) -> TrafficShaperObject: ...
    
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
    ) -> list[TrafficShaperObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
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
        name: str,
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
        name: None = None,
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
        name: str | None = ...,
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
        name: str | None = ...,
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
    ) -> TrafficShaperObject | list[TrafficShaperObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TrafficShaperObject: ...
    
    @overload
    def post(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TrafficShaperObject: ...
    
    @overload
    def put(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TrafficShaperObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
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
    "TrafficShaper",
    "TrafficShaperPayload",
    "TrafficShaperObject",
]