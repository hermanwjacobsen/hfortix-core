"""Validation helpers for switch_controller/qos/queue_policy - Auto-generated"""

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
    "name",  # QoS policy name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "schedule": "round-robin",
    "rate-by": "kbps",
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
    "name": "string",  # QoS policy name.
    "schedule": "option",  # COS queue scheduling.
    "rate-by": "option",  # COS queue rate by kbps or percent.
    "cos-queue": "string",  # COS queue configuration.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "QoS policy name.",
    "schedule": "COS queue scheduling.",
    "rate-by": "COS queue rate by kbps or percent.",
    "cos-queue": "COS queue configuration.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "cos-queue": {
        "name": {
            "type": "string",
            "help": "Cos queue ID.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
        "description": {
            "type": "string",
            "help": "Description of the COS queue.",
            "default": "",
            "max_length": 63,
        },
        "min-rate": {
            "type": "integer",
            "help": "Minimum rate (0 - 4294967295 kbps, 0 to disable).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "max-rate": {
            "type": "integer",
            "help": "Maximum rate (0 - 4294967295 kbps, 0 to disable).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "min-rate-percent": {
            "type": "integer",
            "help": "Minimum rate (% of link speed).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "max-rate-percent": {
            "type": "integer",
            "help": "Maximum rate (% of link speed).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "drop-policy": {
            "type": "option",
            "help": "COS queue drop policy.",
            "default": "taildrop",
            "options": [{"help": "Taildrop policy.", "label": "Taildrop", "name": "taildrop"}, {"help": "Weighted random early detection drop policy.", "label": "Weighted Random Early Detection", "name": "weighted-random-early-detection"}],
        },
        "ecn": {
            "type": "option",
            "help": "Enable/disable ECN packet marking to drop eligible packets.",
            "default": "disable",
            "options": [{"help": "Disable ECN packet marking to drop eligible packets.", "label": "Disable", "name": "disable"}, {"help": "Enable ECN packet marking to drop eligible packets.", "label": "Enable", "name": "enable"}],
        },
        "weight": {
            "type": "integer",
            "help": "Weight of weighted round robin scheduling.",
            "default": 1,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_SCHEDULE = [
    "strict",  # Strict scheduling (queue7: highest priority, queue0: lowest priority).
    "round-robin",  # Round robin scheduling.
    "weighted",  # Weighted round robin scheduling.
]
VALID_BODY_RATE_BY = [
    "kbps",  # Rate by kbps.
    "percent",  # Rate by percent.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_qos_queue_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/qos/queue_policy."""
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
    """Validate required fields for switch_controller/qos/queue_policy."""
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


def validate_switch_controller_qos_queue_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/qos/queue_policy object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "schedule" in payload:
        value = payload["schedule"]
        if value not in VALID_BODY_SCHEDULE:
            desc = FIELD_DESCRIPTIONS.get("schedule", "")
            error_msg = f"Invalid value for 'schedule': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCHEDULE)}"
            error_msg += f"\n  → Example: schedule='{{ VALID_BODY_SCHEDULE[0] }}'"
            return (False, error_msg)
    if "rate-by" in payload:
        value = payload["rate-by"]
        if value not in VALID_BODY_RATE_BY:
            desc = FIELD_DESCRIPTIONS.get("rate-by", "")
            error_msg = f"Invalid value for 'rate-by': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RATE_BY)}"
            error_msg += f"\n  → Example: rate-by='{{ VALID_BODY_RATE_BY[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_qos_queue_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/qos/queue_policy."""
    # Step 1: Validate enum values
    if "schedule" in payload:
        value = payload["schedule"]
        if value not in VALID_BODY_SCHEDULE:
            return (
                False,
                f"Invalid value for 'schedule'='{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE)}",
            )
    if "rate-by" in payload:
        value = payload["rate-by"]
        if value not in VALID_BODY_RATE_BY:
            return (
                False,
                f"Invalid value for 'rate-by'='{value}'. Must be one of: {', '.join(VALID_BODY_RATE_BY)}",
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
    "endpoint": "switch_controller/qos/queue_policy",
    "category": "cmdb",
    "api_path": "switch-controller.qos/queue-policy",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure FortiSwitch QoS egress queue policy.",
    "total_fields": 4,
    "required_fields_count": 1,
    "fields_with_defaults_count": 3,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
