"""
Validation helpers for wireless_controller/arrp_profile endpoint.

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
    "name": "",
    "selection-period": 3600,
    "monitor-period": 300,
    "weight-managed-ap": 50,
    "weight-rogue-ap": 10,
    "weight-noise-floor": 40,
    "weight-channel-load": 20,
    "weight-spectral-rssi": 40,
    "weight-weather-channel": 0,
    "weight-dfs-channel": 0,
    "threshold-ap": 250,
    "threshold-noise-floor": "-85",
    "threshold-channel-load": 60,
    "threshold-spectral-rssi": "-65",
    "threshold-tx-retries": 300,
    "threshold-rx-errors": 50,
    "include-weather-channel": "enable",
    "include-dfs-channel": "enable",
    "override-darrp-optimize": "disable",
    "darrp-optimize": 86400,
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
    "name": "string",  # WiFi ARRP profile name.
    "comment": "var-string",  # Comment.
    "selection-period": "integer",  # Period in seconds to measure average channel load, noise flo
    "monitor-period": "integer",  # Period in seconds to measure average transmit retries and re
    "weight-managed-ap": "integer",  # Weight in DARRP channel score calculation for managed APs (0
    "weight-rogue-ap": "integer",  # Weight in DARRP channel score calculation for rogue APs (0 -
    "weight-noise-floor": "integer",  # Weight in DARRP channel score calculation for noise floor (0
    "weight-channel-load": "integer",  # Weight in DARRP channel score calculation for channel load (
    "weight-spectral-rssi": "integer",  # Weight in DARRP channel score calculation for spectral RSSI 
    "weight-weather-channel": "integer",  # Weight in DARRP channel score calculation for weather channe
    "weight-dfs-channel": "integer",  # Weight in DARRP channel score calculation for DFS channel (0
    "threshold-ap": "integer",  # Threshold to reject channel in DARRP channel selection phase
    "threshold-noise-floor": "string",  # Threshold in dBm to reject channel in DARRP channel selectio
    "threshold-channel-load": "integer",  # Threshold in percentage to reject channel in DARRP channel s
    "threshold-spectral-rssi": "string",  # Threshold in dBm to reject channel in DARRP channel selectio
    "threshold-tx-retries": "integer",  # Threshold in percentage for transmit retries to trigger chan
    "threshold-rx-errors": "integer",  # Threshold in percentage for receive errors to trigger channe
    "include-weather-channel": "option",  # Enable/disable use of weather channel in DARRP channel selec
    "include-dfs-channel": "option",  # Enable/disable use of DFS channel in DARRP channel selection
    "override-darrp-optimize": "option",  # Enable to override setting darrp-optimize and darrp-optimize
    "darrp-optimize": "integer",  # Time for running Distributed Automatic Radio Resource Provis
    "darrp-optimize-schedules": "string",  # Firewall schedules for DARRP running time. DARRP will run pe
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "WiFi ARRP profile name.",
    "comment": "Comment.",
    "selection-period": "Period in seconds to measure average channel load, noise floor, spectral RSSI (default = 3600).",
    "monitor-period": "Period in seconds to measure average transmit retries and receive errors (default = 300).",
    "weight-managed-ap": "Weight in DARRP channel score calculation for managed APs (0 - 2000, default = 50).",
    "weight-rogue-ap": "Weight in DARRP channel score calculation for rogue APs (0 - 2000, default = 10).",
    "weight-noise-floor": "Weight in DARRP channel score calculation for noise floor (0 - 2000, default = 40).",
    "weight-channel-load": "Weight in DARRP channel score calculation for channel load (0 - 2000, default = 20).",
    "weight-spectral-rssi": "Weight in DARRP channel score calculation for spectral RSSI (0 - 2000, default = 40).",
    "weight-weather-channel": "Weight in DARRP channel score calculation for weather channel (0 - 2000, default = 0).",
    "weight-dfs-channel": "Weight in DARRP channel score calculation for DFS channel (0 - 2000, default = 0).",
    "threshold-ap": "Threshold to reject channel in DARRP channel selection phase 1 due to surrounding APs (0 - 500, default = 250).",
    "threshold-noise-floor": "Threshold in dBm to reject channel in DARRP channel selection phase 1 due to noise floor (-95 to -20, default = -85).",
    "threshold-channel-load": "Threshold in percentage to reject channel in DARRP channel selection phase 1 due to channel load (0 - 100, default = 60).",
    "threshold-spectral-rssi": "Threshold in dBm to reject channel in DARRP channel selection phase 1 due to spectral RSSI (-95 to -20, default = -65).",
    "threshold-tx-retries": "Threshold in percentage for transmit retries to trigger channel reselection in DARRP monitor stage (0 - 1000, default = 300).",
    "threshold-rx-errors": "Threshold in percentage for receive errors to trigger channel reselection in DARRP monitor stage (0 - 100, default = 50).",
    "include-weather-channel": "Enable/disable use of weather channel in DARRP channel selection phase 1 (default = enable).",
    "include-dfs-channel": "Enable/disable use of DFS channel in DARRP channel selection phase 1 (default = enable).",
    "override-darrp-optimize": "Enable to override setting darrp-optimize and darrp-optimize-schedules (default = disable).",
    "darrp-optimize": "Time for running Distributed Automatic Radio Resource Provisioning (DARRP) optimizations (0 - 86400 sec, default = 86400, 0 = disable).",
    "darrp-optimize-schedules": "Firewall schedules for DARRP running time. DARRP will run periodically based on darrp-optimize within the schedules. Separate multiple schedule names with a space.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "selection-period": {"type": "integer", "min": 0, "max": 65535},
    "monitor-period": {"type": "integer", "min": 0, "max": 65535},
    "weight-managed-ap": {"type": "integer", "min": 0, "max": 2000},
    "weight-rogue-ap": {"type": "integer", "min": 0, "max": 2000},
    "weight-noise-floor": {"type": "integer", "min": 0, "max": 2000},
    "weight-channel-load": {"type": "integer", "min": 0, "max": 2000},
    "weight-spectral-rssi": {"type": "integer", "min": 0, "max": 2000},
    "weight-weather-channel": {"type": "integer", "min": 0, "max": 2000},
    "weight-dfs-channel": {"type": "integer", "min": 0, "max": 2000},
    "threshold-ap": {"type": "integer", "min": 0, "max": 500},
    "threshold-noise-floor": {"type": "string", "max_length": 7},
    "threshold-channel-load": {"type": "integer", "min": 0, "max": 100},
    "threshold-spectral-rssi": {"type": "string", "max_length": 7},
    "threshold-tx-retries": {"type": "integer", "min": 0, "max": 1000},
    "threshold-rx-errors": {"type": "integer", "min": 0, "max": 100},
    "darrp-optimize": {"type": "integer", "min": 0, "max": 86400},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "darrp-optimize-schedules": {
        "name": {
            "type": "string",
            "help": "Schedule name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_INCLUDE_WEATHER_CHANNEL = [
    "enable",
    "disable",
]
VALID_BODY_INCLUDE_DFS_CHANNEL = [
    "enable",
    "disable",
]
VALID_BODY_OVERRIDE_DARRP_OPTIMIZE = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_arrp_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for wireless_controller/arrp_profile.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_wireless_controller_arrp_profile_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_wireless_controller_arrp_profile_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_wireless_controller_arrp_profile_get(
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
    Validate required fields for wireless_controller/arrp_profile.

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


def validate_wireless_controller_arrp_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new wireless_controller/arrp_profile object.

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
        >>> is_valid, error = validate_wireless_controller_arrp_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "include-weather-channel": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_wireless_controller_arrp_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["include-weather-channel"] = "invalid-value"
        >>> is_valid, error = validate_wireless_controller_arrp_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_wireless_controller_arrp_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "include-weather-channel" in payload:
        value = payload["include-weather-channel"]
        if value not in VALID_BODY_INCLUDE_WEATHER_CHANNEL:
            desc = FIELD_DESCRIPTIONS.get("include-weather-channel", "")
            error_msg = f"Invalid value for 'include-weather-channel': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INCLUDE_WEATHER_CHANNEL)}"
            error_msg += f"\n  → Example: include-weather-channel='{{ VALID_BODY_INCLUDE_WEATHER_CHANNEL[0] }}'"
            return (False, error_msg)
    if "include-dfs-channel" in payload:
        value = payload["include-dfs-channel"]
        if value not in VALID_BODY_INCLUDE_DFS_CHANNEL:
            desc = FIELD_DESCRIPTIONS.get("include-dfs-channel", "")
            error_msg = f"Invalid value for 'include-dfs-channel': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INCLUDE_DFS_CHANNEL)}"
            error_msg += f"\n  → Example: include-dfs-channel='{{ VALID_BODY_INCLUDE_DFS_CHANNEL[0] }}'"
            return (False, error_msg)
    if "override-darrp-optimize" in payload:
        value = payload["override-darrp-optimize"]
        if value not in VALID_BODY_OVERRIDE_DARRP_OPTIMIZE:
            desc = FIELD_DESCRIPTIONS.get("override-darrp-optimize", "")
            error_msg = f"Invalid value for 'override-darrp-optimize': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE_DARRP_OPTIMIZE)}"
            error_msg += f"\n  → Example: override-darrp-optimize='{{ VALID_BODY_OVERRIDE_DARRP_OPTIMIZE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_arrp_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update wireless_controller/arrp_profile.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_wireless_controller_arrp_profile_put(payload)
    """
    # Step 1: Validate enum values
    if "include-weather-channel" in payload:
        value = payload["include-weather-channel"]
        if value not in VALID_BODY_INCLUDE_WEATHER_CHANNEL:
            return (
                False,
                f"Invalid value for 'include-weather-channel'='{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_WEATHER_CHANNEL)}",
            )
    if "include-dfs-channel" in payload:
        value = payload["include-dfs-channel"]
        if value not in VALID_BODY_INCLUDE_DFS_CHANNEL:
            return (
                False,
                f"Invalid value for 'include-dfs-channel'='{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_DFS_CHANNEL)}",
            )
    if "override-darrp-optimize" in payload:
        value = payload["override-darrp-optimize"]
        if value not in VALID_BODY_OVERRIDE_DARRP_OPTIMIZE:
            return (
                False,
                f"Invalid value for 'override-darrp-optimize'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_DARRP_OPTIMIZE)}",
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
    "endpoint": "wireless_controller/arrp_profile",
    "category": "cmdb",
    "api_path": "wireless-controller/arrp-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.",
    "total_fields": 22,
    "required_fields_count": 0,
    "fields_with_defaults_count": 20,
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
