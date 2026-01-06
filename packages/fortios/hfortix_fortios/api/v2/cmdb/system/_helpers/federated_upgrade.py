"""Validation helpers for system/federated_upgrade - Auto-generated"""

from typing import Any, TypedDict, NotRequired, Literal

# Import common validators from central _helpers module
from hfortix_fortios._helpers import (
    validate_enable_disable,
    validate_integer_range,
    validate_string_length,
    validate_port_number,
    validate_ip_address,
    validate_ipv6_address,
    validate_mac_address,
)

# ============================================================================
# Required Fields Validation
# Auto-generated from schema
# ============================================================================

# ⚠️  IMPORTANT: FortiOS schemas have known issues with required field marking:

# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
    "known-ha-members",  # Known members of the HA cluster. If a member is missing at upgrade time, the upgrade will be cancelled.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "status": "disabled",
    "source": "user",
    "failure-reason": "none",
    "failure-device": "",
    "upgrade-id": 0,
    "next-path-index": 0,
    "ignore-signing-errors": "disable",
    "ha-reboot-controller": "",
    "initial-version": "",
    "starter-admin": "",
}

# ============================================================================
# Deprecated Fields
# Auto-generated from schema - warns users about deprecated fields
# ============================================================================

# Deprecated fields with migration guidance
DEPRECATED_FIELDS = {
}

# ============================================================================
# Field Metadata (Type Information & Descriptions)
# Auto-generated from schema - use for IDE autocomplete and documentation
# ============================================================================

# Field types mapping
FIELD_TYPES = {
    "status": "option",  # Current status of the upgrade.
    "source": "option",  # Source that set up the federated upgrade config.
    "failure-reason": "option",  # Reason for upgrade failure.
    "failure-device": "string",  # Serial number of the node to include.
    "upgrade-id": "integer",  # Unique identifier for this upgrade.
    "next-path-index": "integer",  # The index of the next image to upgrade to.
    "ignore-signing-errors": "option",  # Allow/reject use of FortiGate firmware images that are unsig
    "ha-reboot-controller": "string",  # Serial number of the FortiGate unit that will control the re
    "known-ha-members": "string",  # Known members of the HA cluster. If a member is missing at u
    "initial-version": "user",  # Firmware version when the upgrade was set up.
    "starter-admin": "string",  # Admin that started the upgrade.
    "node-list": "string",  # Nodes which will be included in the upgrade.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Current status of the upgrade.",
    "source": "Source that set up the federated upgrade config.",
    "failure-reason": "Reason for upgrade failure.",
    "failure-device": "Serial number of the node to include.",
    "upgrade-id": "Unique identifier for this upgrade.",
    "next-path-index": "The index of the next image to upgrade to.",
    "ignore-signing-errors": "Allow/reject use of FortiGate firmware images that are unsigned.",
    "ha-reboot-controller": "Serial number of the FortiGate unit that will control the reboot process for the federated upgrade of the HA cluster.",
    "known-ha-members": "Known members of the HA cluster. If a member is missing at upgrade time, the upgrade will be cancelled.",
    "initial-version": "Firmware version when the upgrade was set up.",
    "starter-admin": "Admin that started the upgrade.",
    "node-list": "Nodes which will be included in the upgrade.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "failure-device": {"type": "string", "max_length": 79},
    "upgrade-id": {"type": "integer", "min": 0, "max": 4294967295},
    "next-path-index": {"type": "integer", "min": 0, "max": 10},
    "ha-reboot-controller": {"type": "string", "max_length": 79},
    "starter-admin": {"type": "string", "max_length": 64},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "known-ha-members": {
        "serial": {
            "type": "string",
            "help": "Serial number of HA member",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "node-list": {
        "serial": {
            "type": "string",
            "help": "Serial number of the node to include.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
        "timing": {
            "type": "option",
            "help": "Run immediately or at a scheduled time.",
            "required": True,
            "default": "immediate",
            "options": [{"help": "Begin the upgrade immediately.", "label": "Immediate", "name": "immediate"}, {"help": "Begin the upgrade at a configured time.", "label": "Scheduled", "name": "scheduled"}],
        },
        "maximum-minutes": {
            "type": "integer",
            "help": "Maximum number of minutes to allow for immediate upgrade preparation.",
            "required": True,
            "default": 15,
            "min_value": 5,
            "max_value": 10080,
        },
        "time": {
            "type": "user",
            "help": "Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UTC).",
            "required": True,
            "default": "",
        },
        "setup-time": {
            "type": "user",
            "help": "Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC).",
            "required": True,
            "default": "",
        },
        "upgrade-path": {
            "type": "user",
            "help": "Fortinet OS image versions to upgrade through in major-minor-patch format, such as 7-0-4.",
            "required": True,
            "default": "",
        },
        "device-type": {
            "type": "option",
            "help": "Fortinet device type.",
            "required": True,
            "default": "fortigate",
            "options": [{"help": "This device is a FortiGate.", "label": "Fortigate", "name": "fortigate"}, {"help": "This device is a FortiSwitch.", "label": "Fortiswitch", "name": "fortiswitch"}, {"help": "This device is a FortiAP.", "label": "Fortiap", "name": "fortiap"}, {"help": "This device is a FortiExtender.", "label": "Fortiextender", "name": "fortiextender"}],
        },
        "allow-download": {
            "type": "option",
            "help": "Enable/disable download firmware images.",
            "default": "enable",
            "options": [{"help": "Allow download of images.", "label": "Enable", "name": "enable"}, {"help": "Disable download of images.", "label": "Disable", "name": "disable"}],
        },
        "coordinating-fortigate": {
            "type": "string",
            "help": "Serial number of the FortiGate unit that controls this device.",
            "default": "",
            "max_length": 79,
        },
        "failure-reason": {
            "type": "option",
            "help": "Upgrade failure reason.",
            "default": "none",
            "options": [{"help": "No failure.", "label": "None", "name": "none"}, {"help": "An internal error occurred.", "label": "Internal", "name": "internal"}, {"help": "The upgrade timed out.", "label": "Timeout", "name": "timeout"}, {"help": "The device type was not supported by the FortiGate.", "label": "Device Type Unsupported", "name": "device-type-unsupported"}, {"help": "The image could not be downloaded.", "label": "Download Failed", "name": "download-failed"}, {"help": "The device was disconnected from the FortiGate.", "label": "Device Missing", "name": "device-missing"}, {"help": "An image matching the device and version could not be found.", "label": "Version Unavailable", "name": "version-unavailable"}, {"help": "The image could not be pushed to the device.", "label": "Staging Failed", "name": "staging-failed"}, {"help": "The device could not be rebooted.", "label": "Reboot Failed", "name": "reboot-failed"}, {"help": "The device did not reconnect after rebooting.", "label": "Device Not Reconnected", "name": "device-not-reconnected"}, {"help": "A device in the Security Fabric tree was not ready.", "label": "Node Not Ready", "name": "node-not-ready"}, {"help": "The coordinating FortiGate did not confirm the upgrade.", "label": "No Final Confirmation", "name": "no-final-confirmation"}, {"help": "A downstream FortiGate did not initiate final confirmation.", "label": "No Confirmation Query", "name": "no-confirmation-query"}, {"help": "Configuration errors encountered during the upgrade.", "label": "Config Error Log Nonempty", "name": "config-error-log-nonempty"}, {"help": "The Security Fabric is disabled on the root FortiGate", "label": "Csf Tree Not Supported", "name": "csf-tree-not-supported"}, {"help": "Firmware changed after the upgrade was set up.", "label": "Firmware Changed", "name": "firmware-changed"}, {"help": "A device in the Security Fabric tree failed.", "label": "Node Failed", "name": "node-failed"}, {"help": "The firmware image is missing and download is not allowed", "label": "Image Missing", "name": "image-missing"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "disabled",  # No federated upgrade has been configured.
    "initialized",  # The upgrade has been configured.
    "downloading",  # The image is downloading in preparation for the upgrade.
    "device-disconnected",  # The image downloads are complete, but one or more devices have disconnected.
    "ready",  # The image download finished and the upgrade is pending.
    "coordinating",  # The upgrade is coordinating with other running upgrades.
    "staging",  # The upgrade is confirmed and images are being staged.
    "final-check",  # The upgrade is ready and final checks are in progress.
    "upgrade-devices",  # The upgrade is ready and devices are being rebooted.
    "cancelled",  # The upgrade was cancelled due to the tree not being ready.
    "confirmed",  # The upgrade was confirmed and reboots are running.
    "done",  # The upgrade completed successfully.
    "failed",  # The upgrade failed due to a local issue.
]
VALID_BODY_SOURCE = [
    "user",  # Upgrade configured based on user input.
    "auto-firmware-upgrade",  # Upgrade configured by the FortiGuard auto-firmware-upgrade feature.
    "forced-upgrade",  # Forced upgrade due to no support contract or end-of-life firmware.
]
VALID_BODY_FAILURE_REASON = [
    "none",  # No failure.
    "internal",  # An internal error occurred.
    "timeout",  # The upgrade timed out.
    "device-type-unsupported",  # The device type was not supported by the FortiGate.
    "download-failed",  # The image could not be downloaded.
    "device-missing",  # The device was disconnected from the FortiGate.
    "version-unavailable",  # An image matching the device and version could not be found.
    "staging-failed",  # The image could not be pushed to the device.
    "reboot-failed",  # The device could not be rebooted.
    "device-not-reconnected",  # The device did not reconnect after rebooting.
    "node-not-ready",  # A device in the Security Fabric tree was not ready.
    "no-final-confirmation",  # The coordinating FortiGate did not confirm the upgrade.
    "no-confirmation-query",  # A downstream FortiGate did not initiate final confirmation.
    "config-error-log-nonempty",  # Configuration errors encountered during the upgrade.
    "csf-tree-not-supported",  # The Security Fabric is disabled on the root FortiGate
    "firmware-changed",  # Firmware changed after the upgrade was set up.
    "node-failed",  # A device in the Security Fabric tree failed.
    "image-missing",  # The firmware image is missing and download is not allowed
]
VALID_BODY_IGNORE_SIGNING_ERRORS = [
    "enable",  # Allow use of FortiGate images that are unsigned.
    "disable",  # Reject use of FortiGate images that are unsigned.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_federated_upgrade_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/federated_upgrade."""
    # Validate query parameters if present
    if "action" in params:
        value = params.get("action")
        if value and value not in VALID_QUERY_ACTION:
            return (
                False,
                f"Invalid query parameter 'action'='{value}'. Must be one of: {', '.join(VALID_QUERY_ACTION)}",
            )

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_required_fields(payload: dict) -> tuple[bool, str | None]:
    """Validate required fields for system/federated_upgrade."""
    # Check always-required fields
    missing_fields = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            missing_fields.append(field)
    
    if missing_fields:
        # Build enhanced error message
        error_parts = [f"Missing required field(s): {', '.join(missing_fields)}"]
        
        # Add descriptions for first few missing fields
        for field in missing_fields[:3]:
            desc = FIELD_DESCRIPTIONS.get(field)
            if desc:
                error_parts.append(f"  • {field}: {desc}")
        
        if len(missing_fields) > 3:
            error_parts.append(f"  ... and {len(missing_fields) - 3} more")
        
        return (False, "\n".join(error_parts))

    return (True, None)


def validate_system_federated_upgrade_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/federated_upgrade object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            desc = FIELD_DESCRIPTIONS.get("status", "")
            error_msg = f"Invalid value for 'status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STATUS)}"
            error_msg += f"\n  → Example: status='{{ VALID_BODY_STATUS[0] }}'"
            return (False, error_msg)
    if "source" in payload:
        value = payload["source"]
        if value not in VALID_BODY_SOURCE:
            desc = FIELD_DESCRIPTIONS.get("source", "")
            error_msg = f"Invalid value for 'source': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SOURCE)}"
            error_msg += f"\n  → Example: source='{{ VALID_BODY_SOURCE[0] }}'"
            return (False, error_msg)
    if "failure-reason" in payload:
        value = payload["failure-reason"]
        if value not in VALID_BODY_FAILURE_REASON:
            desc = FIELD_DESCRIPTIONS.get("failure-reason", "")
            error_msg = f"Invalid value for 'failure-reason': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAILURE_REASON)}"
            error_msg += f"\n  → Example: failure-reason='{{ VALID_BODY_FAILURE_REASON[0] }}'"
            return (False, error_msg)
    if "ignore-signing-errors" in payload:
        value = payload["ignore-signing-errors"]
        if value not in VALID_BODY_IGNORE_SIGNING_ERRORS:
            desc = FIELD_DESCRIPTIONS.get("ignore-signing-errors", "")
            error_msg = f"Invalid value for 'ignore-signing-errors': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IGNORE_SIGNING_ERRORS)}"
            error_msg += f"\n  → Example: ignore-signing-errors='{{ VALID_BODY_IGNORE_SIGNING_ERRORS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_federated_upgrade_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/federated_upgrade."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "source" in payload:
        value = payload["source"]
        if value not in VALID_BODY_SOURCE:
            return (
                False,
                f"Invalid value for 'source'='{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE)}",
            )
    if "failure-reason" in payload:
        value = payload["failure-reason"]
        if value not in VALID_BODY_FAILURE_REASON:
            return (
                False,
                f"Invalid value for 'failure-reason'='{value}'. Must be one of: {', '.join(VALID_BODY_FAILURE_REASON)}",
            )
    if "ignore-signing-errors" in payload:
        value = payload["ignore-signing-errors"]
        if value not in VALID_BODY_IGNORE_SIGNING_ERRORS:
            return (
                False,
                f"Invalid value for 'ignore-signing-errors'='{value}'. Must be one of: {', '.join(VALID_BODY_IGNORE_SIGNING_ERRORS)}",
            )

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Imported from central module to avoid duplication across 1,062 files
# ============================================================================

from hfortix_fortios._helpers.metadata import (
    get_field_description as _get_field_description,
    get_field_type as _get_field_type,
    get_field_constraints as _get_field_constraints,
    get_field_default as _get_field_default,
    get_field_options as _get_field_options,
    get_nested_schema as _get_nested_schema,
    get_all_fields as _get_all_fields,
    get_field_metadata as _get_field_metadata,
    validate_field_value as _validate_field_value,
)

# Wrapper functions that bind module-specific data to central functions
def get_field_description(field_name: str) -> str | None:
    """Get description/help text for a field."""
    return _get_field_description(FIELD_DESCRIPTIONS, field_name)

def get_field_type(field_name: str) -> str | None:
    """Get the type of a field."""
    return _get_field_type(FIELD_TYPES, field_name)

def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """Get constraints for a field (min/max values, string length)."""
    return _get_field_constraints(FIELD_CONSTRAINTS, field_name)

def get_field_default(field_name: str) -> Any | None:
    """Get default value for a field."""
    return _get_field_default(FIELDS_WITH_DEFAULTS, field_name)

def get_field_options(field_name: str) -> list[str] | None:
    """Get valid enum options for a field."""
    return _get_field_options(globals(), field_name)

def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """Get schema for nested table/list fields."""
    return _get_nested_schema(NESTED_SCHEMAS, field_name)

def get_all_fields() -> list[str]:
    """Get list of all field names."""
    return _get_all_fields(FIELD_TYPES)

def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """Get complete metadata for a field (type, description, constraints, defaults, options)."""
    return _get_field_metadata(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS, REQUIRED_FIELDS, NESTED_SCHEMAS,
        globals(), field_name
    )

def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """Validate a single field value against its constraints."""
    return _validate_field_value(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        globals(), field_name, value
    )


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "system/federated_upgrade",
    "category": "cmdb",
    "api_path": "system/federated-upgrade",
    "help": "Coordinate federated upgrades within the Security Fabric.",
    "total_fields": 12,
    "required_fields_count": 1,
    "fields_with_defaults_count": 10,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
