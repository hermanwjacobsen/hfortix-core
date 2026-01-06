"""Validation helpers for switch_controller/qos/dot1p_map - Auto-generated"""

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
    """Validate GET request parameters for switch_controller/qos/dot1p_map."""
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
    """Validate required fields for switch_controller/qos/dot1p_map."""
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
    """Validate POST request to create new switch_controller/qos/dot1p_map object."""
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
    """Validate PUT request to update switch_controller/qos/dot1p_map."""
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
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
