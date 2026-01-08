from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class DeviceUpgradePayload(TypedDict, total=False):
    """
    Type hints for system/device_upgrade payload fields.
    
    Independent upgrades for managed devices.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)

    **Usage:**
        payload: DeviceUpgradePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    vdom: NotRequired[str]  # Limit upgrade to this virtual domain (VDOM).
    status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"]  # Current status of the upgrade.
    ha_reboot_controller: NotRequired[str]  # Serial number of the FortiGate unit that will control the re
    next_path_index: int  # The index of the next image to upgrade to.
    known_ha_members: list[dict[str, Any]]  # Known members of the HA cluster. If a member is missing at u
    initial_version: NotRequired[str]  # Firmware version when the upgrade was set up.
    starter_admin: NotRequired[str]  # Admin that started the upgrade.
    serial: str  # Serial number of the node to include.
    timing: Literal["immediate", "scheduled"]  # Run immediately or at a scheduled time.
    maximum_minutes: int  # Maximum number of minutes to allow for immediate upgrade pre
    time: str  # Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UT
    setup_time: str  # Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC)
    upgrade_path: str  # Fortinet OS image versions to upgrade through in major-minor
    device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"]  # Fortinet device type.
    allow_download: NotRequired[Literal["enable", "disable"]]  # Enable/disable download firmware images.
    failure_reason: NotRequired[Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"]]  # Upgrade failure reason.


class DeviceUpgradeObject(FortiObject[DeviceUpgradePayload]):
    """Typed FortiObject for system/device_upgrade with IDE autocomplete support."""
    
    # Limit upgrade to this virtual domain (VDOM).
    vdom: str
    # Current status of the upgrade.
    status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"]
    # Serial number of the FortiGate unit that will control the reboot process for the
    ha_reboot_controller: str
    # The index of the next image to upgrade to.
    next_path_index: int
    # Known members of the HA cluster. If a member is missing at upgrade time, the upg
    known_ha_members: list[str]  # Auto-flattened from member_table
    # Firmware version when the upgrade was set up.
    initial_version: str
    # Admin that started the upgrade.
    starter_admin: str
    # Serial number of the node to include.
    serial: str
    # Run immediately or at a scheduled time.
    timing: Literal["immediate", "scheduled"]
    # Maximum number of minutes to allow for immediate upgrade preparation.
    maximum_minutes: int
    # Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UTC).
    time: str
    # Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC).
    setup_time: str
    # Fortinet OS image versions to upgrade through in major-minor-patch format, such 
    upgrade_path: str
    # Fortinet device type.
    device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"]
    # Enable/disable download firmware images.
    allow_download: Literal["enable", "disable"]
    # Upgrade failure reason.
    failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> DeviceUpgradePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class DeviceUpgrade:
    """
    Independent upgrades for managed devices.
    
    Path: system/device_upgrade
    Category: cmdb
    Primary Key: serial
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        serial: str,
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
    ) -> DeviceUpgradeObject: ...
    
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
    ) -> list[DeviceUpgradeObject]: ...
    
    @overload
    def get(
        self,
        serial: str | None = ...,
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
        serial: str,
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
        serial: None = None,
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
        serial: str | None = ...,
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
        serial: str | None = ...,
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
    ) -> DeviceUpgradeObject | list[DeviceUpgradeObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DeviceUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        ha_reboot_controller: str | None = ...,
        next_path_index: int | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        serial: str | None = ...,
        timing: Literal["immediate", "scheduled"] | None = ...,
        maximum_minutes: int | None = ...,
        time: str | None = ...,
        setup_time: str | None = ...,
        upgrade_path: str | None = ...,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = ...,
        allow_download: Literal["enable", "disable"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DeviceUpgradeObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DeviceUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        ha_reboot_controller: str | None = ...,
        next_path_index: int | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        serial: str | None = ...,
        timing: Literal["immediate", "scheduled"] | None = ...,
        maximum_minutes: int | None = ...,
        time: str | None = ...,
        setup_time: str | None = ...,
        upgrade_path: str | None = ...,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = ...,
        allow_download: Literal["enable", "disable"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: DeviceUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        ha_reboot_controller: str | None = ...,
        next_path_index: int | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        serial: str | None = ...,
        timing: Literal["immediate", "scheduled"] | None = ...,
        maximum_minutes: int | None = ...,
        time: str | None = ...,
        setup_time: str | None = ...,
        upgrade_path: str | None = ...,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = ...,
        allow_download: Literal["enable", "disable"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: DeviceUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        ha_reboot_controller: str | None = ...,
        next_path_index: int | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        serial: str | None = ...,
        timing: Literal["immediate", "scheduled"] | None = ...,
        maximum_minutes: int | None = ...,
        time: str | None = ...,
        setup_time: str | None = ...,
        upgrade_path: str | None = ...,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = ...,
        allow_download: Literal["enable", "disable"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DeviceUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        ha_reboot_controller: str | None = ...,
        next_path_index: int | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        serial: str | None = ...,
        timing: Literal["immediate", "scheduled"] | None = ...,
        maximum_minutes: int | None = ...,
        time: str | None = ...,
        setup_time: str | None = ...,
        upgrade_path: str | None = ...,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = ...,
        allow_download: Literal["enable", "disable"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DeviceUpgradeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DeviceUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        ha_reboot_controller: str | None = ...,
        next_path_index: int | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        serial: str | None = ...,
        timing: Literal["immediate", "scheduled"] | None = ...,
        maximum_minutes: int | None = ...,
        time: str | None = ...,
        setup_time: str | None = ...,
        upgrade_path: str | None = ...,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = ...,
        allow_download: Literal["enable", "disable"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: DeviceUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        ha_reboot_controller: str | None = ...,
        next_path_index: int | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        serial: str | None = ...,
        timing: Literal["immediate", "scheduled"] | None = ...,
        maximum_minutes: int | None = ...,
        time: str | None = ...,
        setup_time: str | None = ...,
        upgrade_path: str | None = ...,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = ...,
        allow_download: Literal["enable", "disable"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: DeviceUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        ha_reboot_controller: str | None = ...,
        next_path_index: int | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        serial: str | None = ...,
        timing: Literal["immediate", "scheduled"] | None = ...,
        maximum_minutes: int | None = ...,
        time: str | None = ...,
        setup_time: str | None = ...,
        upgrade_path: str | None = ...,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = ...,
        allow_download: Literal["enable", "disable"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        serial: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DeviceUpgradeObject: ...
    
    @overload
    def delete(
        self,
        serial: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        serial: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        serial: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        serial: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: DeviceUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        ha_reboot_controller: str | None = ...,
        next_path_index: int | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        serial: str | None = ...,
        timing: Literal["immediate", "scheduled"] | None = ...,
        maximum_minutes: int | None = ...,
        time: str | None = ...,
        setup_time: str | None = ...,
        upgrade_path: str | None = ...,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = ...,
        allow_download: Literal["enable", "disable"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
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
    "DeviceUpgrade",
    "DeviceUpgradePayload",
    "DeviceUpgradeObject",
]