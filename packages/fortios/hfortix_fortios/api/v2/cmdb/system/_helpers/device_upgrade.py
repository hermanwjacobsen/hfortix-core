"""Validation helpers for system/device_upgrade - Auto-generated"""

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
    "serial",  # Serial number of the node to include.
    "time",  # Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UTC).
    "setup-time",  # Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC).
    "upgrade-path",  # Fortinet OS image versions to upgrade through in major-minor-patch format, such as 7-0-4.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "vdom": "",
    "status": "disabled",
    "ha-reboot-controller": "",
    "next-path-index": 0,
    "initial-version": "",
    "starter-admin": "",
    "serial": "",
    "timing": "immediate",
    "maximum-minutes": 15,
    "time": "",
    "setup-time": "",
    "upgrade-path": "",
    "device-type": "fortigate",
    "allow-download": "enable",
    "failure-reason": "none",
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
    "vdom": "string",  # Limit upgrade to this virtual domain (VDOM).
    "status": "option",  # Current status of the upgrade.
    "ha-reboot-controller": "string",  # Serial number of the FortiGate unit that will control the re
    "next-path-index": "integer",  # The index of the next image to upgrade to.
    "known-ha-members": "string",  # Known members of the HA cluster. If a member is missing at u
    "initial-version": "user",  # Firmware version when the upgrade was set up.
    "starter-admin": "string",  # Admin that started the upgrade.
    "serial": "string",  # Serial number of the node to include.
    "timing": "option",  # Run immediately or at a scheduled time.
    "maximum-minutes": "integer",  # Maximum number of minutes to allow for immediate upgrade pre
    "time": "user",  # Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UT
    "setup-time": "user",  # Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC)
    "upgrade-path": "user",  # Fortinet OS image versions to upgrade through in major-minor
    "device-type": "option",  # Fortinet device type.
    "allow-download": "option",  # Enable/disable download firmware images.
    "failure-reason": "option",  # Upgrade failure reason.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "vdom": "Limit upgrade to this virtual domain (VDOM).",
    "status": "Current status of the upgrade.",
    "ha-reboot-controller": "Serial number of the FortiGate unit that will control the reboot process for the federated upgrade of the HA cluster.",
    "next-path-index": "The index of the next image to upgrade to.",
    "known-ha-members": "Known members of the HA cluster. If a member is missing at upgrade time, the upgrade will be cancelled.",
    "initial-version": "Firmware version when the upgrade was set up.",
    "starter-admin": "Admin that started the upgrade.",
    "serial": "Serial number of the node to include.",
    "timing": "Run immediately or at a scheduled time.",
    "maximum-minutes": "Maximum number of minutes to allow for immediate upgrade preparation.",
    "time": "Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UTC).",
    "setup-time": "Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC).",
    "upgrade-path": "Fortinet OS image versions to upgrade through in major-minor-patch format, such as 7-0-4.",
    "device-type": "Fortinet device type.",
    "allow-download": "Enable/disable download firmware images.",
    "failure-reason": "Upgrade failure reason.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "vdom": {"type": "string", "max_length": 31},
    "ha-reboot-controller": {"type": "string", "max_length": 79},
    "next-path-index": {"type": "integer", "min": 0, "max": 10},
    "starter-admin": {"type": "string", "max_length": 64},
    "serial": {"type": "string", "max_length": 79},
    "maximum-minutes": {"type": "integer", "min": 5, "max": 10080},
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
VALID_BODY_TIMING = [
    "immediate",  # Begin the upgrade immediately.
    "scheduled",  # Begin the upgrade at a configured time.
]
VALID_BODY_DEVICE_TYPE = [
    "fortigate",  # This device is a FortiGate.
    "fortiswitch",  # This device is a FortiSwitch.
    "fortiap",  # This device is a FortiAP.
    "fortiextender",  # This device is a FortiExtender.
]
VALID_BODY_ALLOW_DOWNLOAD = [
    "enable",  # Allow download of images.
    "disable",  # Disable download of images.
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
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_device_upgrade_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/device_upgrade."""
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
    """Validate required fields for system/device_upgrade."""
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


def validate_system_device_upgrade_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/device_upgrade object."""
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
    if "timing" in payload:
        value = payload["timing"]
        if value not in VALID_BODY_TIMING:
            desc = FIELD_DESCRIPTIONS.get("timing", "")
            error_msg = f"Invalid value for 'timing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TIMING)}"
            error_msg += f"\n  → Example: timing='{{ VALID_BODY_TIMING[0] }}'"
            return (False, error_msg)
    if "device-type" in payload:
        value = payload["device-type"]
        if value not in VALID_BODY_DEVICE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("device-type", "")
            error_msg = f"Invalid value for 'device-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEVICE_TYPE)}"
            error_msg += f"\n  → Example: device-type='{{ VALID_BODY_DEVICE_TYPE[0] }}'"
            return (False, error_msg)
    if "allow-download" in payload:
        value = payload["allow-download"]
        if value not in VALID_BODY_ALLOW_DOWNLOAD:
            desc = FIELD_DESCRIPTIONS.get("allow-download", "")
            error_msg = f"Invalid value for 'allow-download': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_DOWNLOAD)}"
            error_msg += f"\n  → Example: allow-download='{{ VALID_BODY_ALLOW_DOWNLOAD[0] }}'"
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_device_upgrade_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/device_upgrade."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "timing" in payload:
        value = payload["timing"]
        if value not in VALID_BODY_TIMING:
            return (
                False,
                f"Invalid value for 'timing'='{value}'. Must be one of: {', '.join(VALID_BODY_TIMING)}",
            )
    if "device-type" in payload:
        value = payload["device-type"]
        if value not in VALID_BODY_DEVICE_TYPE:
            return (
                False,
                f"Invalid value for 'device-type'='{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_TYPE)}",
            )
    if "allow-download" in payload:
        value = payload["allow-download"]
        if value not in VALID_BODY_ALLOW_DOWNLOAD:
            return (
                False,
                f"Invalid value for 'allow-download'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_DOWNLOAD)}",
            )
    if "failure-reason" in payload:
        value = payload["failure-reason"]
        if value not in VALID_BODY_FAILURE_REASON:
            return (
                False,
                f"Invalid value for 'failure-reason'='{value}'. Must be one of: {', '.join(VALID_BODY_FAILURE_REASON)}",
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
    "endpoint": "system/device_upgrade",
    "category": "cmdb",
    "api_path": "system/device-upgrade",
    "mkey": "serial",
    "mkey_type": "string",
    "help": "Independent upgrades for managed devices.",
    "total_fields": 16,
    "required_fields_count": 5,
    "fields_with_defaults_count": 15,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
