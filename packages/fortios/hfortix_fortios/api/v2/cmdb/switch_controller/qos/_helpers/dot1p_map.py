"""
Validation helpers for switch_controller/qos/dot1p_map endpoint.

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
    "name",  # Dot1p map name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "description": "",
    "egress-pri-tagging": "disable",
    "priority-0": "queue-0",
    "priority-1": "queue-0",
    "priority-2": "queue-0",
    "priority-3": "queue-0",
    "priority-4": "queue-0",
    "priority-5": "queue-0",
    "priority-6": "queue-0",
    "priority-7": "queue-0",
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
    "name": "string",  # Dot1p map name.
    "description": "string",  # Description of the 802.1p name.
    "egress-pri-tagging": "option",  # Enable/disable egress priority-tag frame.
    "priority-0": "option",  # COS queue mapped to dot1p priority number.
    "priority-1": "option",  # COS queue mapped to dot1p priority number.
    "priority-2": "option",  # COS queue mapped to dot1p priority number.
    "priority-3": "option",  # COS queue mapped to dot1p priority number.
    "priority-4": "option",  # COS queue mapped to dot1p priority number.
    "priority-5": "option",  # COS queue mapped to dot1p priority number.
    "priority-6": "option",  # COS queue mapped to dot1p priority number.
    "priority-7": "option",  # COS queue mapped to dot1p priority number.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Dot1p map name.",
    "description": "Description of the 802.1p name.",
    "egress-pri-tagging": "Enable/disable egress priority-tag frame.",
    "priority-0": "COS queue mapped to dot1p priority number.",
    "priority-1": "COS queue mapped to dot1p priority number.",
    "priority-2": "COS queue mapped to dot1p priority number.",
    "priority-3": "COS queue mapped to dot1p priority number.",
    "priority-4": "COS queue mapped to dot1p priority number.",
    "priority-5": "COS queue mapped to dot1p priority number.",
    "priority-6": "COS queue mapped to dot1p priority number.",
    "priority-7": "COS queue mapped to dot1p priority number.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
    "description": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_EGRESS_PRI_TAGGING = [
    "disable",  # Disable egress priority tagging.
    "enable",  # Enable egress priority tagging.
]
VALID_BODY_PRIORITY_0 = [
    "queue-0",  # COS queue 0 (lowest priority).
    "queue-1",  # COS queue 1.
    "queue-2",  # COS queue 2.
    "queue-3",  # COS queue 3.
    "queue-4",  # COS queue 4.
    "queue-5",  # COS queue 5.
    "queue-6",  # COS queue 6.
    "queue-7",  # COS queue 7 (highest priority).
]
VALID_BODY_PRIORITY_1 = [
    "queue-0",  # COS queue 0 (lowest priority).
    "queue-1",  # COS queue 1.
    "queue-2",  # COS queue 2.
    "queue-3",  # COS queue 3.
    "queue-4",  # COS queue 4.
    "queue-5",  # COS queue 5.
    "queue-6",  # COS queue 6.
    "queue-7",  # COS queue 7 (highest priority).
]
VALID_BODY_PRIORITY_2 = [
    "queue-0",  # COS queue 0 (lowest priority).
    "queue-1",  # COS queue 1.
    "queue-2",  # COS queue 2.
    "queue-3",  # COS queue 3.
    "queue-4",  # COS queue 4.
    "queue-5",  # COS queue 5.
    "queue-6",  # COS queue 6.
    "queue-7",  # COS queue 7 (highest priority).
]
VALID_BODY_PRIORITY_3 = [
    "queue-0",  # COS queue 0 (lowest priority).
    "queue-1",  # COS queue 1.
    "queue-2",  # COS queue 2.
    "queue-3",  # COS queue 3.
    "queue-4",  # COS queue 4.
    "queue-5",  # COS queue 5.
    "queue-6",  # COS queue 6.
    "queue-7",  # COS queue 7 (highest priority).
]
VALID_BODY_PRIORITY_4 = [
    "queue-0",  # COS queue 0 (lowest priority).
    "queue-1",  # COS queue 1.
    "queue-2",  # COS queue 2.
    "queue-3",  # COS queue 3.
    "queue-4",  # COS queue 4.
    "queue-5",  # COS queue 5.
    "queue-6",  # COS queue 6.
    "queue-7",  # COS queue 7 (highest priority).
]
VALID_BODY_PRIORITY_5 = [
    "queue-0",  # COS queue 0 (lowest priority).
    "queue-1",  # COS queue 1.
    "queue-2",  # COS queue 2.
    "queue-3",  # COS queue 3.
    "queue-4",  # COS queue 4.
    "queue-5",  # COS queue 5.
    "queue-6",  # COS queue 6.
    "queue-7",  # COS queue 7 (highest priority).
]
VALID_BODY_PRIORITY_6 = [
    "queue-0",  # COS queue 0 (lowest priority).
    "queue-1",  # COS queue 1.
    "queue-2",  # COS queue 2.
    "queue-3",  # COS queue 3.
    "queue-4",  # COS queue 4.
    "queue-5",  # COS queue 5.
    "queue-6",  # COS queue 6.
    "queue-7",  # COS queue 7 (highest priority).
]
VALID_BODY_PRIORITY_7 = [
    "queue-0",  # COS queue 0 (lowest priority).
    "queue-1",  # COS queue 1.
    "queue-2",  # COS queue 2.
    "queue-3",  # COS queue 3.
    "queue-4",  # COS queue 4.
    "queue-5",  # COS queue 5.
    "queue-6",  # COS queue 6.
    "queue-7",  # COS queue 7 (highest priority).
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_qos_dot1p_map_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for switch_controller/qos/dot1p_map.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_switch_controller_qos_dot1p_map_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_switch_controller_qos_dot1p_map_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_switch_controller_qos_dot1p_map_get(
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
    Validate required fields for switch_controller/qos/dot1p_map.

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


def validate_switch_controller_qos_dot1p_map_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new switch_controller/qos/dot1p_map object.

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
        ...     "name": True,  # Dot1p map name.
        ... }
        >>> is_valid, error = validate_switch_controller_qos_dot1p_map_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "name": True,
        ...     "egress-pri-tagging": "{'name': 'disable', 'help': 'Disable egress priority tagging.', 'label': 'Disable', 'description': 'Disable egress priority tagging'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_switch_controller_qos_dot1p_map_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["egress-pri-tagging"] = "invalid-value"
        >>> is_valid, error = validate_switch_controller_qos_dot1p_map_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_switch_controller_qos_dot1p_map_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "egress-pri-tagging" in payload:
        value = payload["egress-pri-tagging"]
        if value not in VALID_BODY_EGRESS_PRI_TAGGING:
            desc = FIELD_DESCRIPTIONS.get("egress-pri-tagging", "")
            error_msg = f"Invalid value for 'egress-pri-tagging': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EGRESS_PRI_TAGGING)}"
            error_msg += f"\n  → Example: egress-pri-tagging='{{ VALID_BODY_EGRESS_PRI_TAGGING[0] }}'"
            return (False, error_msg)
    if "priority-0" in payload:
        value = payload["priority-0"]
        if value not in VALID_BODY_PRIORITY_0:
            desc = FIELD_DESCRIPTIONS.get("priority-0", "")
            error_msg = f"Invalid value for 'priority-0': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY_0)}"
            error_msg += f"\n  → Example: priority-0='{{ VALID_BODY_PRIORITY_0[0] }}'"
            return (False, error_msg)
    if "priority-1" in payload:
        value = payload["priority-1"]
        if value not in VALID_BODY_PRIORITY_1:
            desc = FIELD_DESCRIPTIONS.get("priority-1", "")
            error_msg = f"Invalid value for 'priority-1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY_1)}"
            error_msg += f"\n  → Example: priority-1='{{ VALID_BODY_PRIORITY_1[0] }}'"
            return (False, error_msg)
    if "priority-2" in payload:
        value = payload["priority-2"]
        if value not in VALID_BODY_PRIORITY_2:
            desc = FIELD_DESCRIPTIONS.get("priority-2", "")
            error_msg = f"Invalid value for 'priority-2': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY_2)}"
            error_msg += f"\n  → Example: priority-2='{{ VALID_BODY_PRIORITY_2[0] }}'"
            return (False, error_msg)
    if "priority-3" in payload:
        value = payload["priority-3"]
        if value not in VALID_BODY_PRIORITY_3:
            desc = FIELD_DESCRIPTIONS.get("priority-3", "")
            error_msg = f"Invalid value for 'priority-3': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY_3)}"
            error_msg += f"\n  → Example: priority-3='{{ VALID_BODY_PRIORITY_3[0] }}'"
            return (False, error_msg)
    if "priority-4" in payload:
        value = payload["priority-4"]
        if value not in VALID_BODY_PRIORITY_4:
            desc = FIELD_DESCRIPTIONS.get("priority-4", "")
            error_msg = f"Invalid value for 'priority-4': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY_4)}"
            error_msg += f"\n  → Example: priority-4='{{ VALID_BODY_PRIORITY_4[0] }}'"
            return (False, error_msg)
    if "priority-5" in payload:
        value = payload["priority-5"]
        if value not in VALID_BODY_PRIORITY_5:
            desc = FIELD_DESCRIPTIONS.get("priority-5", "")
            error_msg = f"Invalid value for 'priority-5': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY_5)}"
            error_msg += f"\n  → Example: priority-5='{{ VALID_BODY_PRIORITY_5[0] }}'"
            return (False, error_msg)
    if "priority-6" in payload:
        value = payload["priority-6"]
        if value not in VALID_BODY_PRIORITY_6:
            desc = FIELD_DESCRIPTIONS.get("priority-6", "")
            error_msg = f"Invalid value for 'priority-6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY_6)}"
            error_msg += f"\n  → Example: priority-6='{{ VALID_BODY_PRIORITY_6[0] }}'"
            return (False, error_msg)
    if "priority-7" in payload:
        value = payload["priority-7"]
        if value not in VALID_BODY_PRIORITY_7:
            desc = FIELD_DESCRIPTIONS.get("priority-7", "")
            error_msg = f"Invalid value for 'priority-7': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY_7)}"
            error_msg += f"\n  → Example: priority-7='{{ VALID_BODY_PRIORITY_7[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_qos_dot1p_map_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update switch_controller/qos/dot1p_map.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_switch_controller_qos_dot1p_map_put(payload)
    """
    # Step 1: Validate enum values
    if "egress-pri-tagging" in payload:
        value = payload["egress-pri-tagging"]
        if value not in VALID_BODY_EGRESS_PRI_TAGGING:
            return (
                False,
                f"Invalid value for 'egress-pri-tagging'='{value}'. Must be one of: {', '.join(VALID_BODY_EGRESS_PRI_TAGGING)}",
            )
    if "priority-0" in payload:
        value = payload["priority-0"]
        if value not in VALID_BODY_PRIORITY_0:
            return (
                False,
                f"Invalid value for 'priority-0'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_0)}",
            )
    if "priority-1" in payload:
        value = payload["priority-1"]
        if value not in VALID_BODY_PRIORITY_1:
            return (
                False,
                f"Invalid value for 'priority-1'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_1)}",
            )
    if "priority-2" in payload:
        value = payload["priority-2"]
        if value not in VALID_BODY_PRIORITY_2:
            return (
                False,
                f"Invalid value for 'priority-2'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_2)}",
            )
    if "priority-3" in payload:
        value = payload["priority-3"]
        if value not in VALID_BODY_PRIORITY_3:
            return (
                False,
                f"Invalid value for 'priority-3'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_3)}",
            )
    if "priority-4" in payload:
        value = payload["priority-4"]
        if value not in VALID_BODY_PRIORITY_4:
            return (
                False,
                f"Invalid value for 'priority-4'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_4)}",
            )
    if "priority-5" in payload:
        value = payload["priority-5"]
        if value not in VALID_BODY_PRIORITY_5:
            return (
                False,
                f"Invalid value for 'priority-5'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_5)}",
            )
    if "priority-6" in payload:
        value = payload["priority-6"]
        if value not in VALID_BODY_PRIORITY_6:
            return (
                False,
                f"Invalid value for 'priority-6'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_6)}",
            )
    if "priority-7" in payload:
        value = payload["priority-7"]
        if value not in VALID_BODY_PRIORITY_7:
            return (
                False,
                f"Invalid value for 'priority-7'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_7)}",
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
    "endpoint": "switch_controller/qos/dot1p_map",
    "category": "cmdb",
    "api_path": "switch-controller.qos/dot1p-map",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure FortiSwitch QoS 802.1p.",
    "total_fields": 11,
    "required_fields_count": 1,
    "fields_with_defaults_count": 11,
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
