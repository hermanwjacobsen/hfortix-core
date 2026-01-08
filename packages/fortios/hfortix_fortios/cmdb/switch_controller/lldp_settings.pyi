from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class LldpSettingsPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/lldp_settings payload fields.
    
    Configure FortiSwitch LLDP settings.
    
    **Usage:**
        payload: LldpSettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    tx_hold: NotRequired[int]  # Number of tx-intervals before local LLDP data expires (1 - 1
    tx_interval: NotRequired[int]  # Frequency of LLDP PDU transmission from FortiSwitch (5 - 409
    fast_start_interval: NotRequired[int]  # Frequency of LLDP PDU transmission from FortiSwitch for the 
    management_interface: NotRequired[Literal["internal", "mgmt"]]  # Primary management interface to be advertised in LLDP and CD
    device_detection: NotRequired[Literal["disable", "enable"]]  # Enable/disable dynamic detection of LLDP neighbor devices fo


class LldpSettingsObject(FortiObject[LldpSettingsPayload]):
    """Typed FortiObject for switch_controller/lldp_settings with IDE autocomplete support."""
    
    # Number of tx-intervals before local LLDP data expires (1 - 16, default = 4). Pac
    tx_hold: int
    # Frequency of LLDP PDU transmission from FortiSwitch (5 - 4095 sec, default = 30)
    tx_interval: int
    # Frequency of LLDP PDU transmission from FortiSwitch for the first 4 packets when
    fast_start_interval: int
    # Primary management interface to be advertised in LLDP and CDP PDUs.
    management_interface: Literal["internal", "mgmt"]
    # Enable/disable dynamic detection of LLDP neighbor devices for VLAN assignment.
    device_detection: Literal["disable", "enable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LldpSettingsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class LldpSettings:
    """
    Configure FortiSwitch LLDP settings.
    
    Path: switch_controller/lldp_settings
    Category: cmdb
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
    ) -> LldpSettingsObject: ...
    
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
    ) -> LldpSettingsObject: ...
    
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
    ) -> LldpSettingsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LldpSettingsPayload | None = ...,
        tx_hold: int | None = ...,
        tx_interval: int | None = ...,
        fast_start_interval: int | None = ...,
        management_interface: Literal["internal", "mgmt"] | None = ...,
        device_detection: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LldpSettingsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LldpSettingsPayload | None = ...,
        tx_hold: int | None = ...,
        tx_interval: int | None = ...,
        fast_start_interval: int | None = ...,
        management_interface: Literal["internal", "mgmt"] | None = ...,
        device_detection: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: LldpSettingsPayload | None = ...,
        tx_hold: int | None = ...,
        tx_interval: int | None = ...,
        fast_start_interval: int | None = ...,
        management_interface: Literal["internal", "mgmt"] | None = ...,
        device_detection: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: LldpSettingsPayload | None = ...,
        tx_hold: int | None = ...,
        tx_interval: int | None = ...,
        fast_start_interval: int | None = ...,
        management_interface: Literal["internal", "mgmt"] | None = ...,
        device_detection: Literal["disable", "enable"] | None = ...,
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
        payload_dict: LldpSettingsPayload | None = ...,
        tx_hold: int | None = ...,
        tx_interval: int | None = ...,
        fast_start_interval: int | None = ...,
        management_interface: Literal["internal", "mgmt"] | None = ...,
        device_detection: Literal["disable", "enable"] | None = ...,
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
    "LldpSettings",
    "LldpSettingsPayload",
    "LldpSettingsObject",
]