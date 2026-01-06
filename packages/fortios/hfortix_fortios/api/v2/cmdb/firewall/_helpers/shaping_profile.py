"""Validation helpers for firewall/shaping_profile - Auto-generated"""

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
    "profile-name",  # Shaping profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "profile-name": "",
    "type": "policing",
    "npu-offloading": "enable",
    "default-class-id": 0,
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
    "profile-name": "string",  # Shaping profile name.
    "comment": "var-string",  # Comment.
    "type": "option",  # Select shaping profile type: policing / queuing.
    "npu-offloading": "option",  # Enable/disable NPU offloading.
    "default-class-id": "integer",  # Default class ID to handle unclassified packets (including a
    "shaping-entries": "string",  # Define shaping entries of this shaping profile.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "profile-name": "Shaping profile name.",
    "comment": "Comment.",
    "type": "Select shaping profile type: policing / queuing.",
    "npu-offloading": "Enable/disable NPU offloading.",
    "default-class-id": "Default class ID to handle unclassified packets (including all local traffic).",
    "shaping-entries": "Define shaping entries of this shaping profile.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "profile-name": {"type": "string", "max_length": 35},
    "default-class-id": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "shaping-entries": {
        "id": {
            "type": "integer",
            "help": "ID number.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "class-id": {
            "type": "integer",
            "help": "Class ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "priority": {
            "type": "option",
            "help": "Priority.",
            "default": "high",
            "options": [{"help": "Top priority.", "label": "Top", "name": "top"}, {"help": "Critical priority.", "label": "Critical", "name": "critical"}, {"help": "High priority.", "label": "High", "name": "high"}, {"help": "Medium priority.", "label": "Medium", "name": "medium"}, {"help": "Low priority.", "label": "Low", "name": "low"}],
        },
        "guaranteed-bandwidth-percentage": {
            "type": "integer",
            "help": "Guaranteed bandwidth in percentage.",
            "default": 0,
            "min_value": 0,
            "max_value": 100,
        },
        "maximum-bandwidth-percentage": {
            "type": "integer",
            "help": "Maximum bandwidth in percentage.",
            "default": 1,
            "min_value": 1,
            "max_value": 100,
        },
        "limit": {
            "type": "integer",
            "help": "Hard limit on the real queue size in packets.",
            "default": 100,
            "min_value": 5,
            "max_value": 10000,
        },
        "burst-in-msec": {
            "type": "integer",
            "help": "Number of bytes that can be burst at maximum-bandwidth speed. Formula: burst = maximum-bandwidth*burst-in-msec.",
            "default": 0,
            "min_value": 0,
            "max_value": 2000,
        },
        "cburst-in-msec": {
            "type": "integer",
            "help": "Number of bytes that can be burst as fast as the interface can transmit. Formula: cburst = maximum-bandwidth*cburst-in-msec.",
            "default": 0,
            "min_value": 0,
            "max_value": 2000,
        },
        "red-probability": {
            "type": "integer",
            "help": "Maximum probability (in percentage) for RED marking.",
            "default": 0,
            "min_value": 0,
            "max_value": 20,
        },
        "min": {
            "type": "integer",
            "help": "Average queue size in packets at which RED drop becomes a possibility.",
            "default": 83,
            "min_value": 3,
            "max_value": 3000,
        },
        "max": {
            "type": "integer",
            "help": "Average queue size in packets at which RED drop probability is maximal.",
            "default": 250,
            "min_value": 3,
            "max_value": 3000,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "policing",  # Enable policing mode.
    "queuing",  # Enable queuing mode.
]
VALID_BODY_NPU_OFFLOADING = [
    "disable",  # Diable shaper offloading.
    "enable",  # Enable shaper offloading.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_shaping_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/shaping_profile."""
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
    """Validate required fields for firewall/shaping_profile."""
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


def validate_firewall_shaping_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/shaping_profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "npu-offloading" in payload:
        value = payload["npu-offloading"]
        if value not in VALID_BODY_NPU_OFFLOADING:
            desc = FIELD_DESCRIPTIONS.get("npu-offloading", "")
            error_msg = f"Invalid value for 'npu-offloading': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NPU_OFFLOADING)}"
            error_msg += f"\n  → Example: npu-offloading='{{ VALID_BODY_NPU_OFFLOADING[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_shaping_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/shaping_profile."""
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "npu-offloading" in payload:
        value = payload["npu-offloading"]
        if value not in VALID_BODY_NPU_OFFLOADING:
            return (
                False,
                f"Invalid value for 'npu-offloading'='{value}'. Must be one of: {', '.join(VALID_BODY_NPU_OFFLOADING)}",
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
    "endpoint": "firewall/shaping_profile",
    "category": "cmdb",
    "api_path": "firewall/shaping-profile",
    "mkey": "profile-name",
    "mkey_type": "string",
    "help": "Configure shaping profiles.",
    "total_fields": 6,
    "required_fields_count": 1,
    "fields_with_defaults_count": 4,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
