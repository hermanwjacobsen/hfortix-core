from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class FortilinkSettingsPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/fortilink_settings payload fields.
    
    Configure integrated FortiLink settings for FortiSwitch.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: fortilink)

    **Usage:**
        payload: FortilinkSettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # FortiLink settings name.
    fortilink: NotRequired[str]  # FortiLink interface to which this fortilink-setting belongs.
    inactive_timer: NotRequired[int]  # Time interval(minutes) to be included in the inactive device
    link_down_flush: NotRequired[Literal["disable", "enable"]]  # Clear NAC and dynamic devices on switch ports on link down e
    access_vlan_mode: NotRequired[Literal["legacy", "fail-open", "fail-close"]]  # Intra VLAN traffic behavior with loss of connection to the F
    nac_ports: NotRequired[str]  # NAC specific configuration.


class FortilinkSettingsObject(FortiObject[FortilinkSettingsPayload]):
    """Typed FortiObject for switch_controller/fortilink_settings with IDE autocomplete support."""
    
    # FortiLink settings name.
    name: str
    # FortiLink interface to which this fortilink-setting belongs.
    fortilink: str
    # Time interval(minutes) to be included in the inactive devices expiry calculation
    inactive_timer: int
    # Clear NAC and dynamic devices on switch ports on link down event.
    link_down_flush: Literal["disable", "enable"]
    # Intra VLAN traffic behavior with loss of connection to the FortiGate.
    access_vlan_mode: Literal["legacy", "fail-open", "fail-close"]
    # NAC specific configuration.
    nac_ports: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortilinkSettingsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class FortilinkSettings:
    """
    Configure integrated FortiLink settings for FortiSwitch.
    
    Path: switch_controller/fortilink_settings
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
    ) -> FortilinkSettingsObject: ...
    
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
    ) -> list[FortilinkSettingsObject]: ...
    
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
    ) -> FortilinkSettingsObject | list[FortilinkSettingsObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: FortilinkSettingsPayload | None = ...,
        name: str | None = ...,
        fortilink: str | None = ...,
        inactive_timer: int | None = ...,
        link_down_flush: Literal["disable", "enable"] | None = ...,
        access_vlan_mode: Literal["legacy", "fail-open", "fail-close"] | None = ...,
        nac_ports: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FortilinkSettingsObject: ...
    
    @overload
    def post(
        self,
        payload_dict: FortilinkSettingsPayload | None = ...,
        name: str | None = ...,
        fortilink: str | None = ...,
        inactive_timer: int | None = ...,
        link_down_flush: Literal["disable", "enable"] | None = ...,
        access_vlan_mode: Literal["legacy", "fail-open", "fail-close"] | None = ...,
        nac_ports: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: FortilinkSettingsPayload | None = ...,
        name: str | None = ...,
        fortilink: str | None = ...,
        inactive_timer: int | None = ...,
        link_down_flush: Literal["disable", "enable"] | None = ...,
        access_vlan_mode: Literal["legacy", "fail-open", "fail-close"] | None = ...,
        nac_ports: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: FortilinkSettingsPayload | None = ...,
        name: str | None = ...,
        fortilink: str | None = ...,
        inactive_timer: int | None = ...,
        link_down_flush: Literal["disable", "enable"] | None = ...,
        access_vlan_mode: Literal["legacy", "fail-open", "fail-close"] | None = ...,
        nac_ports: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FortilinkSettingsPayload | None = ...,
        name: str | None = ...,
        fortilink: str | None = ...,
        inactive_timer: int | None = ...,
        link_down_flush: Literal["disable", "enable"] | None = ...,
        access_vlan_mode: Literal["legacy", "fail-open", "fail-close"] | None = ...,
        nac_ports: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FortilinkSettingsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FortilinkSettingsPayload | None = ...,
        name: str | None = ...,
        fortilink: str | None = ...,
        inactive_timer: int | None = ...,
        link_down_flush: Literal["disable", "enable"] | None = ...,
        access_vlan_mode: Literal["legacy", "fail-open", "fail-close"] | None = ...,
        nac_ports: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: FortilinkSettingsPayload | None = ...,
        name: str | None = ...,
        fortilink: str | None = ...,
        inactive_timer: int | None = ...,
        link_down_flush: Literal["disable", "enable"] | None = ...,
        access_vlan_mode: Literal["legacy", "fail-open", "fail-close"] | None = ...,
        nac_ports: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: FortilinkSettingsPayload | None = ...,
        name: str | None = ...,
        fortilink: str | None = ...,
        inactive_timer: int | None = ...,
        link_down_flush: Literal["disable", "enable"] | None = ...,
        access_vlan_mode: Literal["legacy", "fail-open", "fail-close"] | None = ...,
        nac_ports: str | None = ...,
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
    ) -> FortilinkSettingsObject: ...
    
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
        payload_dict: FortilinkSettingsPayload | None = ...,
        name: str | None = ...,
        fortilink: str | None = ...,
        inactive_timer: int | None = ...,
        link_down_flush: Literal["disable", "enable"] | None = ...,
        access_vlan_mode: Literal["legacy", "fail-open", "fail-close"] | None = ...,
        nac_ports: str | None = ...,
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
    "FortilinkSettings",
    "FortilinkSettingsPayload",
    "FortilinkSettingsObject",
]