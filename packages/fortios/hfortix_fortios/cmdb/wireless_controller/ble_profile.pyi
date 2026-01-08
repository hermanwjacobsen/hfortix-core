from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class BleProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/ble_profile payload fields.
    
    Configure Bluetooth Low Energy profile.
    
    **Usage:**
        payload: BleProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Bluetooth Low Energy profile name.
    comment: NotRequired[str]  # Comment.
    advertising: NotRequired[Literal["ibeacon", "eddystone-uid", "eddystone-url"]]  # Advertising type.
    ibeacon_uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    major_id: NotRequired[int]  # Major ID.
    minor_id: NotRequired[int]  # Minor ID.
    eddystone_namespace: NotRequired[str]  # Eddystone namespace ID.
    eddystone_instance: NotRequired[str]  # Eddystone instance ID.
    eddystone_url: NotRequired[str]  # Eddystone URL.
    txpower: NotRequired[Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]]  # Transmit power level (default = 0).
    beacon_interval: NotRequired[int]  # Beacon interval (default = 100 msec).
    ble_scanning: NotRequired[Literal["enable", "disable"]]  # Enable/disable Bluetooth Low Energy (BLE) scanning.
    scan_type: NotRequired[Literal["active", "passive"]]  # Scan Type (default = active).
    scan_threshold: NotRequired[str]  # Minimum signal level/threshold in dBm required for the AP to
    scan_period: NotRequired[int]  # Scan Period (default = 4000 msec).
    scan_time: NotRequired[int]  # Scan Time (default = 1000 msec).
    scan_interval: NotRequired[int]  # Scan Interval (default = 50 msec).
    scan_window: NotRequired[int]  # Scan Windows (default = 50 msec).


class BleProfileObject(FortiObject[BleProfilePayload]):
    """Typed FortiObject for wireless_controller/ble_profile with IDE autocomplete support."""
    
    # Bluetooth Low Energy profile name.
    name: str
    # Comment.
    comment: str
    # Advertising type.
    advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"]
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    ibeacon_uuid: str
    # Major ID.
    major_id: int
    # Minor ID.
    minor_id: int
    # Eddystone namespace ID.
    eddystone_namespace: str
    # Eddystone instance ID.
    eddystone_instance: str
    # Eddystone URL.
    eddystone_url: str
    # Transmit power level (default = 0).
    txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]
    # Beacon interval (default = 100 msec).
    beacon_interval: int
    # Enable/disable Bluetooth Low Energy (BLE) scanning.
    ble_scanning: Literal["enable", "disable"]
    # Scan Type (default = active).
    scan_type: Literal["active", "passive"]
    # Minimum signal level/threshold in dBm required for the AP to report detected BLE
    scan_threshold: str
    # Scan Period (default = 4000 msec).
    scan_period: int
    # Scan Time (default = 1000 msec).
    scan_time: int
    # Scan Interval (default = 50 msec).
    scan_interval: int
    # Scan Windows (default = 50 msec).
    scan_window: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> BleProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class BleProfile:
    """
    Configure Bluetooth Low Energy profile.
    
    Path: wireless_controller/ble_profile
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
    ) -> BleProfileObject: ...
    
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
    ) -> list[BleProfileObject]: ...
    
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
    ) -> BleProfileObject | list[BleProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | list[dict[str, Any]] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> BleProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | list[dict[str, Any]] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | list[dict[str, Any]] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | list[dict[str, Any]] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | list[dict[str, Any]] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> BleProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | list[dict[str, Any]] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | list[dict[str, Any]] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | list[dict[str, Any]] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
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
    ) -> BleProfileObject: ...
    
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
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | list[str] | list[dict[str, Any]] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] | None = ...,
        beacon_interval: int | None = ...,
        ble_scanning: Literal["enable", "disable"] | None = ...,
        scan_type: Literal["active", "passive"] | None = ...,
        scan_threshold: str | None = ...,
        scan_period: int | None = ...,
        scan_time: int | None = ...,
        scan_interval: int | None = ...,
        scan_window: int | None = ...,
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
    "BleProfile",
    "BleProfilePayload",
    "BleProfileObject",
]