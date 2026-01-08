from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SwitchInterfacePayload(TypedDict, total=False):
    """
    Type hints for system/switch_interface payload fields.
    
    Configure software switch interfaces by grouping physical and WiFi interfaces.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: span-dest-port)
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)

    **Usage:**
        payload: SwitchInterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Interface name
    vdom: str  # VDOM that the software switch belongs to.
    span_dest_port: NotRequired[str]  # SPAN destination port name. All traffic on the SPAN source p
    span_source_port: NotRequired[list[dict[str, Any]]]  # Physical interface name. Port spanning echoes all traffic on
    member: NotRequired[list[dict[str, Any]]]  # Names of the interfaces that belong to the virtual switch.
    type: NotRequired[Literal["switch", "hub"]]  # Type of switch based on functionality: switch for normal fun
    intra_switch_policy: NotRequired[Literal["implicit", "explicit"]]  # Allow any traffic between switch interfaces or require firew
    mac_ttl: NotRequired[int]  # Duration for which MAC addresses are held in the ARP table
    span: NotRequired[Literal["disable", "enable"]]  # Enable/disable port spanning. Port spanning echoes traffic r
    span_direction: NotRequired[Literal["rx", "tx", "both"]]  # The direction in which the SPAN port operates, either: rx, t

# Nested classes for table field children

@final
class SwitchInterfaceSpansourceportObject:
    """Typed object for span-source-port table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Physical interface name.
    interface_name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SwitchInterfaceMemberObject:
    """Typed object for member table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
    interface_name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SwitchInterfaceResponse(TypedDict):
    """
    Type hints for system/switch_interface API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    vdom: str
    span_dest_port: str
    span_source_port: list[dict[str, Any]]
    member: list[dict[str, Any]]
    type: Literal["switch", "hub"]
    intra_switch_policy: Literal["implicit", "explicit"]
    mac_ttl: int
    span: Literal["disable", "enable"]
    span_direction: Literal["rx", "tx", "both"]


@final
class SwitchInterfaceObject:
    """Typed FortiObject for system/switch_interface with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Interface name
    name: str
    # VDOM that the software switch belongs to.
    vdom: str
    # SPAN destination port name. All traffic on the SPAN source ports is echoed to th
    span_dest_port: str
    # Physical interface name. Port spanning echoes all traffic on the SPAN source por
    span_source_port: list[SwitchInterfaceSpansourceportObject]  # Table field - list of typed objects
    # Names of the interfaces that belong to the virtual switch.
    member: list[SwitchInterfaceMemberObject]  # Table field - list of typed objects
    # Type of switch based on functionality: switch for normal functionality, or hub t
    type: Literal["switch", "hub"]
    # Allow any traffic between switch interfaces or require firewall policies to allo
    intra_switch_policy: Literal["implicit", "explicit"]
    # Duration for which MAC addresses are held in the ARP table
    mac_ttl: int
    # Enable/disable port spanning. Port spanning echoes traffic received by the softw
    span: Literal["disable", "enable"]
    # The direction in which the SPAN port operates, either: rx, tx, or both.
    span_direction: Literal["rx", "tx", "both"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SwitchInterfacePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class SwitchInterface:
    """
    Configure software switch interfaces by grouping physical and WiFi interfaces.
    
    Path: system/switch_interface
    Category: cmdb
    Primary Key: name
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
    ) -> SwitchInterfaceObject: ...
    
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
    ) -> SwitchInterfaceObject: ...
    
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
    ) -> list[SwitchInterfaceObject]: ...
    
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
    ) -> SwitchInterfaceResponse: ...
    
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
    ) -> SwitchInterfaceResponse: ...
    
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
    ) -> list[SwitchInterfaceResponse]: ...
    
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
    ) -> SwitchInterfaceObject | list[SwitchInterfaceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SwitchInterfaceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SwitchInterfaceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
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
    ) -> SwitchInterfaceObject: ...
    
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
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: str | list[str] | list[dict[str, Any]] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
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
    "SwitchInterface",
    "SwitchInterfacePayload",
    "SwitchInterfaceObject",
]