from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class FederatedUpgradePayload(TypedDict, total=False):
    """
    Type hints for system/federated_upgrade payload fields.
    
    Coordinate federated upgrades within the Security Fabric.
    
    **Usage:**
        payload: FederatedUpgradePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"]  # Current status of the upgrade.
    source: NotRequired[Literal["user", "auto-firmware-upgrade", "forced-upgrade"]]  # Source that set up the federated upgrade config.
    failure_reason: NotRequired[Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"]]  # Reason for upgrade failure.
    failure_device: NotRequired[str]  # Serial number of the node to include.
    upgrade_id: NotRequired[int]  # Unique identifier for this upgrade.
    next_path_index: int  # The index of the next image to upgrade to.
    ignore_signing_errors: NotRequired[Literal["enable", "disable"]]  # Allow/reject use of FortiGate firmware images that are unsig
    ha_reboot_controller: NotRequired[str]  # Serial number of the FortiGate unit that will control the re
    known_ha_members: list[dict[str, Any]]  # Known members of the HA cluster. If a member is missing at u
    initial_version: NotRequired[str]  # Firmware version when the upgrade was set up.
    starter_admin: NotRequired[str]  # Admin that started the upgrade.
    node_list: NotRequired[list[dict[str, Any]]]  # Nodes which will be included in the upgrade.


class FederatedUpgradeObject(FortiObject[FederatedUpgradePayload]):
    """Typed FortiObject for system/federated_upgrade with IDE autocomplete support."""
    
    # Current status of the upgrade.
    status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"]
    # Source that set up the federated upgrade config.
    source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"]
    # Reason for upgrade failure.
    failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"]
    # Serial number of the node to include.
    failure_device: str
    # Unique identifier for this upgrade.
    upgrade_id: int
    # The index of the next image to upgrade to.
    next_path_index: int
    # Allow/reject use of FortiGate firmware images that are unsigned.
    ignore_signing_errors: Literal["enable", "disable"]
    # Serial number of the FortiGate unit that will control the reboot process for the
    ha_reboot_controller: str
    # Known members of the HA cluster. If a member is missing at upgrade time, the upg
    known_ha_members: list[str]  # Auto-flattened from member_table
    # Firmware version when the upgrade was set up.
    initial_version: str
    # Admin that started the upgrade.
    starter_admin: str
    # Nodes which will be included in the upgrade.
    node_list: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FederatedUpgradePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class FederatedUpgrade:
    """
    Coordinate federated upgrades within the Security Fabric.
    
    Path: system/federated_upgrade
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
    ) -> FederatedUpgradeObject: ...
    
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
    ) -> FederatedUpgradeObject: ...
    
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
    ) -> FederatedUpgradeObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FederatedUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        failure_device: str | None = ...,
        upgrade_id: int | None = ...,
        next_path_index: int | None = ...,
        ignore_signing_errors: Literal["enable", "disable"] | None = ...,
        ha_reboot_controller: str | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        node_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FederatedUpgradeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FederatedUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        failure_device: str | None = ...,
        upgrade_id: int | None = ...,
        next_path_index: int | None = ...,
        ignore_signing_errors: Literal["enable", "disable"] | None = ...,
        ha_reboot_controller: str | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        node_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: FederatedUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        failure_device: str | None = ...,
        upgrade_id: int | None = ...,
        next_path_index: int | None = ...,
        ignore_signing_errors: Literal["enable", "disable"] | None = ...,
        ha_reboot_controller: str | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        node_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: FederatedUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        failure_device: str | None = ...,
        upgrade_id: int | None = ...,
        next_path_index: int | None = ...,
        ignore_signing_errors: Literal["enable", "disable"] | None = ...,
        ha_reboot_controller: str | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        node_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: FederatedUpgradePayload | None = ...,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = ...,
        source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"] | None = ...,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = ...,
        failure_device: str | None = ...,
        upgrade_id: int | None = ...,
        next_path_index: int | None = ...,
        ignore_signing_errors: Literal["enable", "disable"] | None = ...,
        ha_reboot_controller: str | None = ...,
        known_ha_members: str | list[str] | list[dict[str, Any]] | None = ...,
        initial_version: str | None = ...,
        starter_admin: str | None = ...,
        node_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "FederatedUpgrade",
    "FederatedUpgradePayload",
    "FederatedUpgradeObject",
]