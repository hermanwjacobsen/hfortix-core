from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class BleProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/ble_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    txpower: NotRequired[Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]]  # Transmit power level (default = 0).
    beacon_interval: NotRequired[int]  # Beacon interval (default = 100 msec).
    ble_scanning: NotRequired[Literal["enable", "disable"]]  # Enable/disable Bluetooth Low Energy (BLE) scanning.
    scan_type: NotRequired[Literal["active", "passive"]]  # Scan Type (default = active).
    scan_threshold: NotRequired[str]  # Minimum signal level/threshold in dBm required for the AP to
    scan_period: NotRequired[int]  # Scan Period (default = 4000 msec).
    scan_time: NotRequired[int]  # Scan Time (default = 1000 msec).
    scan_interval: NotRequired[int]  # Scan Interval (default = 50 msec).
    scan_window: NotRequired[int]  # Scan Windows (default = 50 msec).


class BleProfile:
    """
    Configure Bluetooth Low Energy profile.
    
    Path: wireless_controller/ble_profile
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
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"] | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: BleProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        advertising: Literal["ibeacon", "eddystone-uid", "eddystone-url"] | None = ...,
        ibeacon_uuid: str | None = ...,
        major_id: int | None = ...,
        minor_id: int | None = ...,
        eddystone_namespace: str | None = ...,
        eddystone_instance: str | None = ...,
        eddystone_url: str | None = ...,
        txpower: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"] | None = ...,
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
        payload_dict: BleProfilePayload | None = ...,
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