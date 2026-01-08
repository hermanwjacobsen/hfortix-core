from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class VlanPolicyPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/vlan_policy payload fields.
    
    Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: fortilink, vlan)

    **Usage:**
        payload: VlanPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # VLAN policy name.
    description: NotRequired[str]  # Description for the VLAN policy.
    fortilink: str  # FortiLink interface for which this VLAN policy belongs to.
    vlan: NotRequired[str]  # Native VLAN to be applied when using this VLAN policy.
    allowed_vlans: NotRequired[list[dict[str, Any]]]  # Allowed VLANs to be applied when using this VLAN policy.
    untagged_vlans: NotRequired[list[dict[str, Any]]]  # Untagged VLANs to be applied when using this VLAN policy.
    allowed_vlans_all: NotRequired[Literal["enable", "disable"]]  # Enable/disable all defined VLANs when using this VLAN policy
    discard_mode: NotRequired[Literal["none", "all-untagged", "all-tagged"]]  # Discard mode to be applied when using this VLAN policy.

# Nested classes for table field children

@final
class VlanPolicyAllowedvlansObject:
    """Typed object for allowed-vlans table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VLAN name.
    vlan_name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class VlanPolicyUntaggedvlansObject:
    """Typed object for untagged-vlans table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VLAN name.
    vlan_name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class VlanPolicyResponse(TypedDict):
    """
    Type hints for switch_controller/vlan_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    description: str
    fortilink: str
    vlan: str
    allowed_vlans: list[dict[str, Any]]
    untagged_vlans: list[dict[str, Any]]
    allowed_vlans_all: Literal["enable", "disable"]
    discard_mode: Literal["none", "all-untagged", "all-tagged"]


@final
class VlanPolicyObject:
    """Typed FortiObject for switch_controller/vlan_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # VLAN policy name.
    name: str
    # Description for the VLAN policy.
    description: str
    # FortiLink interface for which this VLAN policy belongs to.
    fortilink: str
    # Native VLAN to be applied when using this VLAN policy.
    vlan: str
    # Allowed VLANs to be applied when using this VLAN policy.
    allowed_vlans: list[VlanPolicyAllowedvlansObject]  # Table field - list of typed objects
    # Untagged VLANs to be applied when using this VLAN policy.
    untagged_vlans: list[VlanPolicyUntaggedvlansObject]  # Table field - list of typed objects
    # Enable/disable all defined VLANs when using this VLAN policy.
    allowed_vlans_all: Literal["enable", "disable"]
    # Discard mode to be applied when using this VLAN policy.
    discard_mode: Literal["none", "all-untagged", "all-tagged"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> VlanPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class VlanPolicy:
    """
    Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.
    
    Path: switch_controller/vlan_policy
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
    ) -> VlanPolicyObject: ...
    
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
    ) -> VlanPolicyObject: ...
    
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
    ) -> list[VlanPolicyObject]: ...
    
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
    ) -> VlanPolicyResponse: ...
    
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
    ) -> VlanPolicyResponse: ...
    
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
    ) -> list[VlanPolicyResponse]: ...
    
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
    ) -> VlanPolicyObject | list[VlanPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VlanPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VlanPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
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
    ) -> VlanPolicyObject: ...
    
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
        payload_dict: VlanPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        fortilink: str | None = ...,
        vlan: str | None = ...,
        allowed_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        untagged_vlans: str | list[str] | list[dict[str, Any]] | None = ...,
        allowed_vlans_all: Literal["enable", "disable"] | None = ...,
        discard_mode: Literal["none", "all-untagged", "all-tagged"] | None = ...,
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
    "VlanPolicy",
    "VlanPolicyPayload",
    "VlanPolicyObject",
]