"""
Validation helpers for system/device_upgrade endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification
Customize as needed for endpoint-specific business logic.
"""

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
#
# 1. FALSE POSITIVES: Some fields marked "required" have default values,
#    meaning they're optional (filtered out by generator)
#
# 2. CONDITIONAL REQUIREMENTS: Many endpoints require EITHER field A OR field B:
#    - firewall.policy: requires (srcaddr + dstaddr) OR (srcaddr6 + dstaddr6)
#    - These conditional requirements cannot be expressed in a simple list
#
# 3. SPECIALIZED FEATURES: Fields for WAN optimization, VPN, NAT64, etc.
#    are marked "required" but only apply when using those features
#
# The REQUIRED_FIELDS list below is INFORMATIONAL ONLY and shows fields that:
# - Are marked required in the schema
# - Don't have non-empty default values
# - Aren't specialized feature fields
#
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
    """
    Validate GET request parameters for system/device_upgrade.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_device_upgrade_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by serial
        >>> is_valid, error = validate_system_device_upgrade_get(serial="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_device_upgrade_get(
        ...     filters={"format": "name|type"}
        ... )
        >>> assert is_valid == True
    """
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
    """
    Validate required fields for system/device_upgrade.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "test"}
        >>> is_valid, error = validate_required_fields(payload)
    """
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
    """
    Validate POST request to create new system/device_upgrade object.

    This validator performs two-stage validation:
    1. Required fields check (schema-based)
    2. Field value validation (enums, ranges, formats)

    Args:
        payload: Request body data with configuration
        **params: Query parameters (vdom, etc.)

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if payload is valid, False otherwise
        - error_message: None if valid, detailed error string if invalid

    Examples:
        >>> # ✅ Valid - Minimal required fields
        >>> payload = {
        ...     "known-ha-members": True,  # Known members of the HA cluster. If a member is mi
        ...     "serial": True,  # Serial number of the node to include.
        ... }
        >>> is_valid, error = validate_system_device_upgrade_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "known-ha-members": True,
        ...     "status": "{'name': 'disabled', 'help': 'No federated upgrade has been configured.', 'label': 'Disabled', 'description': 'No federated upgrade has been configured'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_device_upgrade_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_system_device_upgrade_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_device_upgrade_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
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
    """
    Validate PUT request to update system/device_upgrade.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_device_upgrade_put(payload)
    """
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
# Provide programmatic access to field metadata for IDE autocomplete,
# documentation generation, and dynamic validation
# ============================================================================


def get_field_description(field_name: str) -> str | None:
    """
    Get description/help text for a field.

    Args:
        field_name: Name of the field

    Returns:
        Description text or None if field doesn't exist

    Example:
        >>> desc = get_field_description("name")
        >>> print(desc)
    """
    return FIELD_DESCRIPTIONS.get(field_name)


def get_field_type(field_name: str) -> str | None:
    """
    Get the type of a field.

    Args:
        field_name: Name of the field

    Returns:
        Field type (e.g., "string", "integer", "option") or None

    Example:
        >>> field_type = get_field_type("status")
        >>> print(field_type)  # "option"
    """
    return FIELD_TYPES.get(field_name)


def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """
    Get constraints for a field (min/max values, string length).

    Args:
        field_name: Name of the field

    Returns:
        Constraint dict or None

    Example:
        >>> constraints = get_field_constraints("port")
        >>> print(constraints)  # {"type": "integer", "min": 1, "max": 65535}
    """
    return FIELD_CONSTRAINTS.get(field_name)


def get_field_default(field_name: str) -> Any | None:
    """
    Get default value for a field.

    Args:
        field_name: Name of the field

    Returns:
        Default value or None if no default

    Example:
        >>> default = get_field_default("status")
        >>> print(default)  # "enable"
    """
    return FIELDS_WITH_DEFAULTS.get(field_name)


def get_field_options(field_name: str) -> list[str] | None:
    """
    Get valid enum options for a field.

    Args:
        field_name: Name of the field

    Returns:
        List of valid values or None if not an enum field

    Example:
        >>> options = get_field_options("status")
        >>> print(options)  # ["enable", "disable"]
    """
    # Construct the constant name from field name
    # Replace all non-alphanumeric characters with underscores for valid Python identifiers
    import re
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', field_name)
    constant_name = f"VALID_BODY_{safe_name.upper()}"
    return globals().get(constant_name)


def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """
    Get schema for nested table/list fields.

    Args:
        field_name: Name of the parent field

    Returns:
        Dict mapping child field names to their metadata

    Example:
        >>> nested = get_nested_schema("members")
        >>> if nested:
        ...     for child_field, child_meta in nested.items():
        ...         print(f"{child_field}: {child_meta['type']}")
    """
    return NESTED_SCHEMAS.get(field_name)


def get_all_fields() -> list[str]:
    """
    Get list of all field names.

    Returns:
        List of all field names in the schema

    Example:
        >>> fields = get_all_fields()
        >>> print(len(fields))
    """
    return list(FIELD_TYPES.keys())


def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """
    Get complete metadata for a field (type, description, constraints, defaults, options).

    Args:
        field_name: Name of the field

    Returns:
        Dict with all available metadata or None if field doesn't exist

    Example:
        >>> meta = get_field_metadata("status")
        >>> print(meta)
        >>> # {
        >>> #   "type": "option",
        >>> #   "description": "Enable/disable this feature",
        >>> #   "default": "enable",
        >>> #   "options": ["enable", "disable"]
        >>> # }
    """
    if field_name not in FIELD_TYPES:
        return None

    metadata = {
        "name": field_name,
        "type": FIELD_TYPES[field_name],
    }

    # Add description if available
    if field_name in FIELD_DESCRIPTIONS:
        metadata["description"] = FIELD_DESCRIPTIONS[field_name]

    # Add constraints if available
    if field_name in FIELD_CONSTRAINTS:
        metadata["constraints"] = FIELD_CONSTRAINTS[field_name]

    # Add default if available
    if field_name in FIELDS_WITH_DEFAULTS:
        metadata["default"] = FIELDS_WITH_DEFAULTS[field_name]

    # Add required flag
    metadata["required"] = field_name in REQUIRED_FIELDS

    # Add options if available
    options = get_field_options(field_name)
    if options:
        metadata["options"] = options

    # Add nested schema if available
    nested = get_nested_schema(field_name)
    if nested:
        metadata["nested_schema"] = nested

    return metadata


def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """
    Validate a single field value against its constraints.

    Args:
        field_name: Name of the field
        value: Value to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_field_value("status", "enable")
        >>> if not is_valid:
        ...     print(error)
    """
    # Get field metadata
    field_type = get_field_type(field_name)
    if field_type is None:
        return (False, f"Unknown field: '{field_name}' (not defined in schema)")

    # Get field description for better error context
    description = get_field_description(field_name)

    # Validate enum values
    options = get_field_options(field_name)
    if options and value not in options:
        error_msg = f"Invalid value for '{field_name}': {repr(value)}"
        if description:
            error_msg += f"\n  → Description: {description}"
        error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in options)}"
        if options:
            error_msg += f"\n  → Example: {field_name}={repr(options[0])}"
        return (False, error_msg)

    # Validate constraints
    constraints = get_field_constraints(field_name)
    if constraints:
        constraint_type = constraints.get("type")

        if constraint_type == "integer":
            if not isinstance(value, int):
                error_msg = f"Field '{field_name}' must be an integer"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            min_val = constraints.get("min")
            max_val = constraints.get("max")

            if min_val is not None and value < min_val:
                error_msg = f"Field '{field_name}' value {value} is below minimum {min_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if max_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

            if max_val is not None and value > max_val:
                error_msg = f"Field '{field_name}' value {value} exceeds maximum {max_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if min_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

        elif constraint_type == "string":
            if not isinstance(value, str):
                error_msg = f"Field '{field_name}' must be a string"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            max_length = constraints.get("max_length")
            if max_length and len(value) > max_length:
                error_msg = f"Field '{field_name}' length {len(value)} exceeds maximum {max_length}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → Your value: {repr(value[:50])}{'...' if len(value) > 50 else ''}"
                return (False, error_msg)

    return (True, None)


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
    """
    Get information about this endpoint schema.

    Returns:
        Dict with schema metadata

    Example:
        >>> info = get_schema_info()
        >>> print(f"Endpoint: {info['endpoint']}")
        >>> print(f"Total fields: {info['total_fields']}")
    """
    return SCHEMA_INFO.copy()
