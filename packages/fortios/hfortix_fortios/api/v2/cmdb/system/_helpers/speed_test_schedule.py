"""
Validation helpers for system/speed_test_schedule endpoint.

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
    "schedules",  # Schedules for the interface.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "interface": "",
    "status": "enable",
    "diffserv": "",
    "server-name": "",
    "mode": "Auto",
    "dynamic-server": "disable",
    "ctrl-port": 5200,
    "server-port": 5201,
    "update-shaper": "disable",
    "update-inbandwidth": "disable",
    "update-outbandwidth": "disable",
    "update-interface-shaping": "disable",
    "update-inbandwidth-maximum": 0,
    "update-inbandwidth-minimum": 0,
    "update-outbandwidth-maximum": 0,
    "update-outbandwidth-minimum": 0,
    "expected-inbandwidth-minimum": 0,
    "expected-inbandwidth-maximum": 0,
    "expected-outbandwidth-minimum": 0,
    "expected-outbandwidth-maximum": 0,
    "retries": 5,
    "retry-pause": 300,
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
    "interface": "string",  # Interface name.
    "status": "option",  # Enable/disable scheduled speed test.
    "diffserv": "user",  # DSCP used for speed test.
    "server-name": "string",  # Speed test server name in system.speed-test-server list or l
    "mode": "option",  # Protocol Auto(default), TCP or UDP used for speed test.
    "schedules": "string",  # Schedules for the interface.
    "dynamic-server": "option",  # Enable/disable dynamic server option.
    "ctrl-port": "integer",  # Port of the controller to get access token.
    "server-port": "integer",  # Port of the server to run speed test.
    "update-shaper": "option",  # Set egress shaper based on the test result.
    "update-inbandwidth": "option",  # Enable/disable bypassing interface's inbound bandwidth setti
    "update-outbandwidth": "option",  # Enable/disable bypassing interface's outbound bandwidth sett
    "update-interface-shaping": "option",  # Enable/disable using the speedtest results as reference for 
    "update-inbandwidth-maximum": "integer",  # Maximum downloading bandwidth (kbps) to be used in a speed t
    "update-inbandwidth-minimum": "integer",  # Minimum downloading bandwidth (kbps) to be considered effect
    "update-outbandwidth-maximum": "integer",  # Maximum uploading bandwidth (kbps) to be used in a speed tes
    "update-outbandwidth-minimum": "integer",  # Minimum uploading bandwidth (kbps) to be considered effectiv
    "expected-inbandwidth-minimum": "integer",  # Set the minimum inbandwidth threshold for applying speedtest
    "expected-inbandwidth-maximum": "integer",  # Set the maximum inbandwidth threshold for applying speedtest
    "expected-outbandwidth-minimum": "integer",  # Set the minimum outbandwidth threshold for applying speedtes
    "expected-outbandwidth-maximum": "integer",  # Set the maximum outbandwidth threshold for applying speedtes
    "retries": "integer",  # Maximum number of times the FortiGate unit will attempt to c
    "retry-pause": "integer",  # Number of seconds the FortiGate pauses between successive sp
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "interface": "Interface name.",
    "status": "Enable/disable scheduled speed test.",
    "diffserv": "DSCP used for speed test.",
    "server-name": "Speed test server name in system.speed-test-server list or leave it as empty to choose default server \"FTNT_Auto\".",
    "mode": "Protocol Auto(default), TCP or UDP used for speed test.",
    "schedules": "Schedules for the interface.",
    "dynamic-server": "Enable/disable dynamic server option.",
    "ctrl-port": "Port of the controller to get access token.",
    "server-port": "Port of the server to run speed test.",
    "update-shaper": "Set egress shaper based on the test result.",
    "update-inbandwidth": "Enable/disable bypassing interface's inbound bandwidth setting.",
    "update-outbandwidth": "Enable/disable bypassing interface's outbound bandwidth setting.",
    "update-interface-shaping": "Enable/disable using the speedtest results as reference for interface shaping (overriding configured in/outbandwidth).",
    "update-inbandwidth-maximum": "Maximum downloading bandwidth (kbps) to be used in a speed test.",
    "update-inbandwidth-minimum": "Minimum downloading bandwidth (kbps) to be considered effective.",
    "update-outbandwidth-maximum": "Maximum uploading bandwidth (kbps) to be used in a speed test.",
    "update-outbandwidth-minimum": "Minimum uploading bandwidth (kbps) to be considered effective.",
    "expected-inbandwidth-minimum": "Set the minimum inbandwidth threshold for applying speedtest results on shaping-profile.",
    "expected-inbandwidth-maximum": "Set the maximum inbandwidth threshold for applying speedtest results on shaping-profile.",
    "expected-outbandwidth-minimum": "Set the minimum outbandwidth threshold for applying speedtest results on shaping-profile.",
    "expected-outbandwidth-maximum": "Set the maximum outbandwidth threshold for applying speedtest results on shaping-profile.",
    "retries": "Maximum number of times the FortiGate unit will attempt to contact the same server before considering the speed test has failed (1 - 10, default = 5).",
    "retry-pause": "Number of seconds the FortiGate pauses between successive speed tests before trying a different server (60 - 3600, default = 300).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "interface": {"type": "string", "max_length": 35},
    "server-name": {"type": "string", "max_length": 35},
    "ctrl-port": {"type": "integer", "min": 1, "max": 65535},
    "server-port": {"type": "integer", "min": 1, "max": 65535},
    "update-inbandwidth-maximum": {"type": "integer", "min": 0, "max": 16776000},
    "update-inbandwidth-minimum": {"type": "integer", "min": 0, "max": 16776000},
    "update-outbandwidth-maximum": {"type": "integer", "min": 0, "max": 16776000},
    "update-outbandwidth-minimum": {"type": "integer", "min": 0, "max": 16776000},
    "expected-inbandwidth-minimum": {"type": "integer", "min": 0, "max": 16776000},
    "expected-inbandwidth-maximum": {"type": "integer", "min": 0, "max": 16776000},
    "expected-outbandwidth-minimum": {"type": "integer", "min": 0, "max": 16776000},
    "expected-outbandwidth-maximum": {"type": "integer", "min": 0, "max": 16776000},
    "retries": {"type": "integer", "min": 1, "max": 10},
    "retry-pause": {"type": "integer", "min": 60, "max": 3600},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "schedules": {
        "name": {
            "type": "string",
            "help": "Name of a firewall recurring schedule.",
            "required": True,
            "default": "",
            "max_length": 31,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "disable",  # Disable scheduled speed test.
    "enable",  # Enable scheduled speed test.
]
VALID_BODY_MODE = [
    "UDP",  # Protocol UDP for speed test.
    "TCP",  # Protocol TCP for speed test.
    "Auto",  # Dynamically selects TCP or UDP based on the speed test setting
]
VALID_BODY_DYNAMIC_SERVER = [
    "disable",  # Disable dynamic server.
    "enable",  # Enable dynamic server.The speed test server will be found automatically.
]
VALID_BODY_UPDATE_SHAPER = [
    "disable",  # Disable updating egress shaper.
    "local",  # Update local-side egress shaper.
    "remote",  # Update remote-side egress shaper.
    "both",  # Update both local-side and remote-side egress shaper.
]
VALID_BODY_UPDATE_INBANDWIDTH = [
    "disable",  # Honor interface's inbandwidth shaping.
    "enable",  # Ignore interface's inbandwidth shaping.
]
VALID_BODY_UPDATE_OUTBANDWIDTH = [
    "disable",  # Honor interface's outbandwidth shaping.
    "enable",  # Ignore updating interface's outbandwidth shaping.
]
VALID_BODY_UPDATE_INTERFACE_SHAPING = [
    "disable",  # Disable updating interface shaping.
    "enable",  # Enable updating interface shaping.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_speed_test_schedule_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/speed_test_schedule.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_speed_test_schedule_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by interface
        >>> is_valid, error = validate_system_speed_test_schedule_get(interface="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_speed_test_schedule_get(
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
    Validate required fields for system/speed_test_schedule.

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


def validate_system_speed_test_schedule_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/speed_test_schedule object.

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
        ...     "schedules": True,  # Schedules for the interface.
        ... }
        >>> is_valid, error = validate_system_speed_test_schedule_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "schedules": True,
        ...     "status": "{'name': 'disable', 'help': 'Disable scheduled speed test.', 'label': 'Disable', 'description': 'Disable scheduled speed test'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_speed_test_schedule_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_system_speed_test_schedule_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_speed_test_schedule_post(payload)
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
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            desc = FIELD_DESCRIPTIONS.get("mode", "")
            error_msg = f"Invalid value for 'mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MODE)}"
            error_msg += f"\n  → Example: mode='{{ VALID_BODY_MODE[0] }}'"
            return (False, error_msg)
    if "dynamic-server" in payload:
        value = payload["dynamic-server"]
        if value not in VALID_BODY_DYNAMIC_SERVER:
            desc = FIELD_DESCRIPTIONS.get("dynamic-server", "")
            error_msg = f"Invalid value for 'dynamic-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DYNAMIC_SERVER)}"
            error_msg += f"\n  → Example: dynamic-server='{{ VALID_BODY_DYNAMIC_SERVER[0] }}'"
            return (False, error_msg)
    if "update-shaper" in payload:
        value = payload["update-shaper"]
        if value not in VALID_BODY_UPDATE_SHAPER:
            desc = FIELD_DESCRIPTIONS.get("update-shaper", "")
            error_msg = f"Invalid value for 'update-shaper': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_SHAPER)}"
            error_msg += f"\n  → Example: update-shaper='{{ VALID_BODY_UPDATE_SHAPER[0] }}'"
            return (False, error_msg)
    if "update-inbandwidth" in payload:
        value = payload["update-inbandwidth"]
        if value not in VALID_BODY_UPDATE_INBANDWIDTH:
            desc = FIELD_DESCRIPTIONS.get("update-inbandwidth", "")
            error_msg = f"Invalid value for 'update-inbandwidth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_INBANDWIDTH)}"
            error_msg += f"\n  → Example: update-inbandwidth='{{ VALID_BODY_UPDATE_INBANDWIDTH[0] }}'"
            return (False, error_msg)
    if "update-outbandwidth" in payload:
        value = payload["update-outbandwidth"]
        if value not in VALID_BODY_UPDATE_OUTBANDWIDTH:
            desc = FIELD_DESCRIPTIONS.get("update-outbandwidth", "")
            error_msg = f"Invalid value for 'update-outbandwidth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_OUTBANDWIDTH)}"
            error_msg += f"\n  → Example: update-outbandwidth='{{ VALID_BODY_UPDATE_OUTBANDWIDTH[0] }}'"
            return (False, error_msg)
    if "update-interface-shaping" in payload:
        value = payload["update-interface-shaping"]
        if value not in VALID_BODY_UPDATE_INTERFACE_SHAPING:
            desc = FIELD_DESCRIPTIONS.get("update-interface-shaping", "")
            error_msg = f"Invalid value for 'update-interface-shaping': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPDATE_INTERFACE_SHAPING)}"
            error_msg += f"\n  → Example: update-interface-shaping='{{ VALID_BODY_UPDATE_INTERFACE_SHAPING[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_speed_test_schedule_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/speed_test_schedule.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_speed_test_schedule_put(payload)
    """
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid value for 'mode'='{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )
    if "dynamic-server" in payload:
        value = payload["dynamic-server"]
        if value not in VALID_BODY_DYNAMIC_SERVER:
            return (
                False,
                f"Invalid value for 'dynamic-server'='{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_SERVER)}",
            )
    if "update-shaper" in payload:
        value = payload["update-shaper"]
        if value not in VALID_BODY_UPDATE_SHAPER:
            return (
                False,
                f"Invalid value for 'update-shaper'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_SHAPER)}",
            )
    if "update-inbandwidth" in payload:
        value = payload["update-inbandwidth"]
        if value not in VALID_BODY_UPDATE_INBANDWIDTH:
            return (
                False,
                f"Invalid value for 'update-inbandwidth'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_INBANDWIDTH)}",
            )
    if "update-outbandwidth" in payload:
        value = payload["update-outbandwidth"]
        if value not in VALID_BODY_UPDATE_OUTBANDWIDTH:
            return (
                False,
                f"Invalid value for 'update-outbandwidth'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_OUTBANDWIDTH)}",
            )
    if "update-interface-shaping" in payload:
        value = payload["update-interface-shaping"]
        if value not in VALID_BODY_UPDATE_INTERFACE_SHAPING:
            return (
                False,
                f"Invalid value for 'update-interface-shaping'='{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_INTERFACE_SHAPING)}",
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
    "endpoint": "system/speed_test_schedule",
    "category": "cmdb",
    "api_path": "system/speed-test-schedule",
    "mkey": "interface",
    "mkey_type": "string",
    "help": "Speed test schedule for each interface.",
    "total_fields": 23,
    "required_fields_count": 1,
    "fields_with_defaults_count": 22,
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
