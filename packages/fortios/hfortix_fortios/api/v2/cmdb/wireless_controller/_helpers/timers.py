"""
Validation helpers for wireless_controller/timers endpoint.

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
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "echo-interval": 30,
    "nat-session-keep-alive": 0,
    "discovery-interval": 5,
    "client-idle-timeout": 300,
    "client-idle-rehome-timeout": 20,
    "auth-timeout": 5,
    "rogue-ap-log": 0,
    "fake-ap-log": 1,
    "sta-offline-cleanup": 300,
    "sta-offline-ip2mac-cleanup": 300,
    "sta-cap-cleanup": 0,
    "rogue-ap-cleanup": 0,
    "rogue-sta-cleanup": 0,
    "wids-entry-cleanup": 0,
    "ble-device-cleanup": 60,
    "sta-stats-interval": 10,
    "vap-stats-interval": 15,
    "radio-stats-interval": 15,
    "sta-capability-interval": 30,
    "sta-locate-timer": 1800,
    "ipsec-intf-cleanup": 120,
    "ble-scan-report-intv": 30,
    "drma-interval": 60,
    "ap-reboot-wait-interval1": 0,
    "ap-reboot-wait-time": "",
    "ap-reboot-wait-interval2": 0,
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
    "echo-interval": "integer",  # Time between echo requests sent by the managed WTP, AP, or F
    "nat-session-keep-alive": "integer",  # Maximal time in seconds between control requests sent by the
    "discovery-interval": "integer",  # Time between discovery requests (2 - 180 sec, default = 5).
    "client-idle-timeout": "integer",  # Time after which a client is considered idle and times out (
    "client-idle-rehome-timeout": "integer",  # Time after which a client is considered idle and disconnecte
    "auth-timeout": "integer",  # Time after which a client is considered failed in RADIUS aut
    "rogue-ap-log": "integer",  # Time between logging rogue AP messages if periodic rogue AP 
    "fake-ap-log": "integer",  # Time between recording logs about fake APs if periodic fake 
    "sta-offline-cleanup": "integer",  # Time period in seconds to keep station offline data after it
    "sta-offline-ip2mac-cleanup": "integer",  # Time period in seconds to keep station offline Ip2mac data a
    "sta-cap-cleanup": "integer",  # Time period in minutes to keep station capability data after
    "rogue-ap-cleanup": "integer",  # Time period in minutes to keep rogue AP after it is gone (de
    "rogue-sta-cleanup": "integer",  # Time period in minutes to keep rogue station after it is gon
    "wids-entry-cleanup": "integer",  # Time period in minutes to keep wids entry after it is gone (
    "ble-device-cleanup": "integer",  # Time period in minutes to keep BLE device after it is gone (
    "sta-stats-interval": "integer",  # Time between running client (station) reports (1 - 255 sec, 
    "vap-stats-interval": "integer",  # Time between running Virtual Access Point (VAP) reports (1 -
    "radio-stats-interval": "integer",  # Time between running radio reports (1 - 255 sec, default = 1
    "sta-capability-interval": "integer",  # Time between running station capability reports (1 - 255 sec
    "sta-locate-timer": "integer",  # Time between running client presence flushes to remove clien
    "ipsec-intf-cleanup": "integer",  # Time period to keep IPsec VPN interfaces up after WTP sessio
    "ble-scan-report-intv": "integer",  # Time between running Bluetooth Low Energy (BLE) reports (10 
    "drma-interval": "integer",  # Dynamic radio mode assignment (DRMA) schedule interval in mi
    "ap-reboot-wait-interval1": "integer",  # Time in minutes to wait before AP reboots when there is no c
    "ap-reboot-wait-time": "string",  # Time to reboot the AP when there is no controller detected a
    "ap-reboot-wait-interval2": "integer",  # Time in minutes to wait before AP reboots when there is no c
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "echo-interval": "Time between echo requests sent by the managed WTP, AP, or FortiAP (1 - 255 sec, default = 30).",
    "nat-session-keep-alive": "Maximal time in seconds between control requests sent by the managed WTP, AP, or FortiAP (0 - 255 sec, default = 0).",
    "discovery-interval": "Time between discovery requests (2 - 180 sec, default = 5).",
    "client-idle-timeout": "Time after which a client is considered idle and times out (20 - 3600 sec, default = 300, 0 for no timeout).",
    "client-idle-rehome-timeout": "Time after which a client is considered idle and disconnected from the home controller (2 - 3600 sec, default = 20, 0 for no timeout).",
    "auth-timeout": "Time after which a client is considered failed in RADIUS authentication and times out (5 - 30 sec, default = 5).",
    "rogue-ap-log": "Time between logging rogue AP messages if periodic rogue AP logging is configured (0 - 1440 min, default = 0).",
    "fake-ap-log": "Time between recording logs about fake APs if periodic fake AP logging is configured (1 - 1440 min, default = 1).",
    "sta-offline-cleanup": "Time period in seconds to keep station offline data after it is gone (default = 300).",
    "sta-offline-ip2mac-cleanup": "Time period in seconds to keep station offline Ip2mac data after it is gone (default = 300).",
    "sta-cap-cleanup": "Time period in minutes to keep station capability data after it is gone (default = 0).",
    "rogue-ap-cleanup": "Time period in minutes to keep rogue AP after it is gone (default = 0).",
    "rogue-sta-cleanup": "Time period in minutes to keep rogue station after it is gone (default = 0).",
    "wids-entry-cleanup": "Time period in minutes to keep wids entry after it is gone (default = 0).",
    "ble-device-cleanup": "Time period in minutes to keep BLE device after it is gone (default = 60).",
    "sta-stats-interval": "Time between running client (station) reports (1 - 255 sec, default = 10).",
    "vap-stats-interval": "Time between running Virtual Access Point (VAP) reports (1 - 255 sec, default = 15).",
    "radio-stats-interval": "Time between running radio reports (1 - 255 sec, default = 15).",
    "sta-capability-interval": "Time between running station capability reports (1 - 255 sec, default = 30).",
    "sta-locate-timer": "Time between running client presence flushes to remove clients that are listed but no longer present (0 - 86400 sec, default = 1800).",
    "ipsec-intf-cleanup": "Time period to keep IPsec VPN interfaces up after WTP sessions are disconnected (30 - 3600 sec, default = 120).",
    "ble-scan-report-intv": "Time between running Bluetooth Low Energy (BLE) reports (10 - 3600 sec, default = 30).",
    "drma-interval": "Dynamic radio mode assignment (DRMA) schedule interval in minutes (1 - 1440, default = 60).",
    "ap-reboot-wait-interval1": "Time in minutes to wait before AP reboots when there is no controller detected (5 - 65535, default = 0, 0 for no reboot).",
    "ap-reboot-wait-time": "Time to reboot the AP when there is no controller detected and standalone SSIDs are pushed to the AP in the previous session, format hh:mm.",
    "ap-reboot-wait-interval2": "Time in minutes to wait before AP reboots when there is no controller detected and standalone SSIDs are pushed to the AP in the previous session (5 - 65535, default = 0, 0 for no reboot).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "echo-interval": {"type": "integer", "min": 1, "max": 255},
    "nat-session-keep-alive": {"type": "integer", "min": 0, "max": 255},
    "discovery-interval": {"type": "integer", "min": 2, "max": 180},
    "client-idle-timeout": {"type": "integer", "min": 20, "max": 3600},
    "client-idle-rehome-timeout": {"type": "integer", "min": 2, "max": 3600},
    "auth-timeout": {"type": "integer", "min": 5, "max": 30},
    "rogue-ap-log": {"type": "integer", "min": 0, "max": 1440},
    "fake-ap-log": {"type": "integer", "min": 1, "max": 1440},
    "sta-offline-cleanup": {"type": "integer", "min": 0, "max": 4294967295},
    "sta-offline-ip2mac-cleanup": {"type": "integer", "min": 0, "max": 4294967295},
    "sta-cap-cleanup": {"type": "integer", "min": 0, "max": 4294967295},
    "rogue-ap-cleanup": {"type": "integer", "min": 0, "max": 4294967295},
    "rogue-sta-cleanup": {"type": "integer", "min": 0, "max": 4294967295},
    "wids-entry-cleanup": {"type": "integer", "min": 0, "max": 4294967295},
    "ble-device-cleanup": {"type": "integer", "min": 0, "max": 4294967295},
    "sta-stats-interval": {"type": "integer", "min": 1, "max": 255},
    "vap-stats-interval": {"type": "integer", "min": 1, "max": 255},
    "radio-stats-interval": {"type": "integer", "min": 1, "max": 255},
    "sta-capability-interval": {"type": "integer", "min": 1, "max": 255},
    "sta-locate-timer": {"type": "integer", "min": 0, "max": 86400},
    "ipsec-intf-cleanup": {"type": "integer", "min": 30, "max": 3600},
    "ble-scan-report-intv": {"type": "integer", "min": 10, "max": 3600},
    "drma-interval": {"type": "integer", "min": 1, "max": 1440},
    "ap-reboot-wait-interval1": {"type": "integer", "min": 5, "max": 65535},
    "ap-reboot-wait-time": {"type": "string", "max_length": 7},
    "ap-reboot-wait-interval2": {"type": "integer", "min": 5, "max": 65535},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_timers_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for wireless_controller/timers.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_wireless_controller_timers_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_wireless_controller_timers_get(
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
    Validate required fields for wireless_controller/timers.

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


def validate_wireless_controller_timers_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new wireless_controller/timers object.

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
        ... }
        >>> is_valid, error = validate_wireless_controller_timers_post(payload)
        >>> assert is_valid == True
        
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_wireless_controller_timers_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_timers_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update wireless_controller/timers.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_wireless_controller_timers_put(payload)
    """
    # Step 1: Validate enum values

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
    constant_name = f"VALID_BODY_{field_name.replace('-', '_').upper()}"
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
    "endpoint": "wireless_controller/timers",
    "category": "cmdb",
    "api_path": "wireless-controller/timers",
    "help": "Configure CAPWAP timers.",
    "total_fields": 26,
    "required_fields_count": 0,
    "fields_with_defaults_count": 26,
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
