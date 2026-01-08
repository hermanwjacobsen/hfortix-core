from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class VlansPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/initial_config/vlans payload fields.
    
    Configure initial template for auto-generated VLAN interfaces.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.switch-controller.initial-config.template.TemplateEndpoint` (via: default-vlan, nac, nac-segment, +4 more)

    **Usage:**
        payload: VlansPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    optional_vlans: NotRequired[Literal["enable", "disable"]]  # Auto-generate pre-configured VLANs upon switch discovery.
    default_vlan: NotRequired[str]  # Default VLAN (native) assigned to all switch ports upon disc
    quarantine: NotRequired[str]  # VLAN for quarantined traffic.
    rspan: NotRequired[str]  # VLAN for RSPAN/ERSPAN mirrored traffic.
    voice: NotRequired[str]  # VLAN dedicated for voice devices.
    video: NotRequired[str]  # VLAN dedicated for video devices.
    nac: NotRequired[str]  # VLAN for NAC onboarding devices.
    nac_segment: NotRequired[str]  # VLAN for NAC segment primary interface.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class VlansResponse(TypedDict):
    """
    Type hints for switch_controller/initial_config/vlans API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    optional_vlans: Literal["enable", "disable"]
    default_vlan: str
    quarantine: str
    rspan: str
    voice: str
    video: str
    nac: str
    nac_segment: str


@final
class VlansObject:
    """Typed FortiObject for switch_controller/initial_config/vlans with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Auto-generate pre-configured VLANs upon switch discovery.
    optional_vlans: Literal["enable", "disable"]
    # Default VLAN (native) assigned to all switch ports upon discovery.
    default_vlan: str
    # VLAN for quarantined traffic.
    quarantine: str
    # VLAN for RSPAN/ERSPAN mirrored traffic.
    rspan: str
    # VLAN dedicated for voice devices.
    voice: str
    # VLAN dedicated for video devices.
    video: str
    # VLAN for NAC onboarding devices.
    nac: str
    # VLAN for NAC segment primary interface.
    nac_segment: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> VlansPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Vlans:
    """
    Configure initial template for auto-generated VLAN interfaces.
    
    Path: switch_controller/initial_config/vlans
    Category: cmdb
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VlansObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VlansObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VlansObject: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> VlansResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> VlansResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> VlansResponse: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> VlansObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VlansObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: VlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: VlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: VlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
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
    "Vlans",
    "VlansPayload",
    "VlansObject",
]