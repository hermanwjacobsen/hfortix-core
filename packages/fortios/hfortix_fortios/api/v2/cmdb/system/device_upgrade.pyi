from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class DeviceUpgradePayload(TypedDict, total=False):
    """
    Type hints for system/device_upgrade payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class DeviceUpgrade:
    """
    Independent upgrades for managed devices.
    
    Path: system/device_upgrade
    Category: cmdb
    Primary Key: serial
    """
    
    def get(
        self,
        serial: str | None = ...,
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
        payload_dict: DeviceUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        ha_reboot_controller: str | None = ...,
        next_path_index: int | None = ...,
        known_ha_members: list[dict[str, Any]] | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: DeviceUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        ha_reboot_controller: str | None = ...,
        next_path_index: int | None = ...,
        known_ha_members: list[dict[str, Any]] | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        serial: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        serial: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: DeviceUpgradePayload | None = ...,
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