"""Validation helpers for system/storage - Auto-generated"""

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
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "default_n",
    "status": "enable",
    "media-status": "disable",
    "order": 0,
    "partition": "\u003cunknown\u003e",
    "device": "?",
    "size": 0,
    "usage": "log",
    "wanopt-mode": "mix",
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
    "name": "string",  # Storage name.
    "status": "option",  # Enable/disable storage.
    "media-status": "option",  # The physical status of current media.
    "order": "integer",  # Set storage order.
    "partition": "string",  # Label of underlying partition.
    "device": "string",  # Partition device.
    "size": "integer",  # Partition size.
    "usage": "option",  # Use hard disk for logging or WAN Optimization (default = log
    "wanopt-mode": "option",  # WAN Optimization mode (default = mix).
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Storage name.",
    "status": "Enable/disable storage.",
    "media-status": "The physical status of current media.",
    "order": "Set storage order.",
    "partition": "Label of underlying partition.",
    "device": "Partition device.",
    "size": "Partition size.",
    "usage": "Use hard disk for logging or WAN Optimization (default = log).",
    "wanopt-mode": "WAN Optimization mode (default = mix).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "order": {"type": "integer", "min": 0, "max": 255},
    "partition": {"type": "string", "max_length": 16},
    "device": {"type": "string", "max_length": 19},
    "size": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_MEDIA_STATUS = [
    "enable",  # Storage is enabled.
    "disable",  # Storage is disabled.
    "fail",  # Storage have some fail sector.
]
VALID_BODY_USAGE = [
    "log",  # Use hard disk for logging.
    "wanopt",  # Use hard disk for WAN Optimization.
]
VALID_BODY_WANOPT_MODE = [
    "mix",  # Use hard disk for WAN Optimization mix mode.
    "wanopt",  # Use hard disk for WAN Optimization wanopt mode.
    "webcache",  # Use hard disk for WAN Optimization webcache mode.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_storage_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/storage."""
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
    """Validate required fields for system/storage."""
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


def validate_system_storage_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/storage object."""
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
    if "media-status" in payload:
        value = payload["media-status"]
        if value not in VALID_BODY_MEDIA_STATUS:
            desc = FIELD_DESCRIPTIONS.get("media-status", "")
            error_msg = f"Invalid value for 'media-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MEDIA_STATUS)}"
            error_msg += f"\n  → Example: media-status='{{ VALID_BODY_MEDIA_STATUS[0] }}'"
            return (False, error_msg)
    if "usage" in payload:
        value = payload["usage"]
        if value not in VALID_BODY_USAGE:
            desc = FIELD_DESCRIPTIONS.get("usage", "")
            error_msg = f"Invalid value for 'usage': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USAGE)}"
            error_msg += f"\n  → Example: usage='{{ VALID_BODY_USAGE[0] }}'"
            return (False, error_msg)
    if "wanopt-mode" in payload:
        value = payload["wanopt-mode"]
        if value not in VALID_BODY_WANOPT_MODE:
            desc = FIELD_DESCRIPTIONS.get("wanopt-mode", "")
            error_msg = f"Invalid value for 'wanopt-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WANOPT_MODE)}"
            error_msg += f"\n  → Example: wanopt-mode='{{ VALID_BODY_WANOPT_MODE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_storage_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/storage."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "media-status" in payload:
        value = payload["media-status"]
        if value not in VALID_BODY_MEDIA_STATUS:
            return (
                False,
                f"Invalid value for 'media-status'='{value}'. Must be one of: {', '.join(VALID_BODY_MEDIA_STATUS)}",
            )
    if "usage" in payload:
        value = payload["usage"]
        if value not in VALID_BODY_USAGE:
            return (
                False,
                f"Invalid value for 'usage'='{value}'. Must be one of: {', '.join(VALID_BODY_USAGE)}",
            )
    if "wanopt-mode" in payload:
        value = payload["wanopt-mode"]
        if value not in VALID_BODY_WANOPT_MODE:
            return (
                False,
                f"Invalid value for 'wanopt-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_WANOPT_MODE)}",
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
    "endpoint": "system/storage",
    "category": "cmdb",
    "api_path": "system/storage",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure logical storage.",
    "total_fields": 9,
    "required_fields_count": 0,
    "fields_with_defaults_count": 9,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
