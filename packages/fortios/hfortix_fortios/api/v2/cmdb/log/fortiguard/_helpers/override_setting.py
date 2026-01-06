"""Validation helpers for log/fortiguard/override_setting - Auto-generated"""

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
    "override": "disable",
    "status": "disable",
    "upload-option": "5-minute",
    "upload-interval": "daily",
    "upload-day": "",
    "upload-time": "",
    "priority": "default",
    "max-log-rate": 0,
    "access-config": "enable",
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
    "override": "option",  # Overriding FortiCloud settings for this VDOM or use global s
    "status": "option",  # Enable/disable logging to FortiCloud.
    "upload-option": "option",  # Configure how log messages are sent to FortiCloud.
    "upload-interval": "option",  # Frequency of uploading log files to FortiCloud.
    "upload-day": "user",  # Day of week to roll logs.
    "upload-time": "user",  # Time of day to roll logs (hh:mm).
    "priority": "option",  # Set log transmission priority.
    "max-log-rate": "integer",  # FortiCloud maximum log rate in MBps (0 = unlimited).
    "access-config": "option",  # Enable/disable FortiCloud access to configuration and data.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "override": "Overriding FortiCloud settings for this VDOM or use global settings.",
    "status": "Enable/disable logging to FortiCloud.",
    "upload-option": "Configure how log messages are sent to FortiCloud.",
    "upload-interval": "Frequency of uploading log files to FortiCloud.",
    "upload-day": "Day of week to roll logs.",
    "upload-time": "Time of day to roll logs (hh:mm).",
    "priority": "Set log transmission priority.",
    "max-log-rate": "FortiCloud maximum log rate in MBps (0 = unlimited).",
    "access-config": "Enable/disable FortiCloud access to configuration and data.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "max-log-rate": {"type": "integer", "min": 0, "max": 100000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_OVERRIDE = [
    "enable",  # Override FortiCloud logging settings.
    "disable",  # Use global FortiCloud logging settings.
]
VALID_BODY_STATUS = [
    "enable",  # Enable logging to FortiCloud.
    "disable",  # Disable logging to FortiCloud.
]
VALID_BODY_UPLOAD_OPTION = [
    "store-and-upload",  # Log to the hard disk and then upload logs to FortiCloud.
    "realtime",  # Log directly to FortiCloud in real time.
    "1-minute",  # Log directly to FortiCloud at 1-minute intervals.
    "5-minute",  # Log directly to FortiCloud at 5-minute intervals.
]
VALID_BODY_UPLOAD_INTERVAL = [
    "daily",  # Upload log files to FortiCloud once a day.
    "weekly",  # Upload log files to FortiCloud once a week.
    "monthly",  # Upload log files to FortiCloud once a month.
]
VALID_BODY_PRIORITY = [
    "default",  # Set FortiCloud log transmission priority to default.
    "low",  # Set FortiCloud log transmission priority to low.
]
VALID_BODY_ACCESS_CONFIG = [
    "enable",  # Enable FortiCloud access to configuration and data.
    "disable",  # Disable FortiCloud access to configuration and data.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_log_fortiguard_override_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for log/fortiguard/override_setting."""
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
    """Validate required fields for log/fortiguard/override_setting."""
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


def validate_log_fortiguard_override_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new log/fortiguard/override_setting object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "override" in payload:
        value = payload["override"]
        if value not in VALID_BODY_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("override", "")
            error_msg = f"Invalid value for 'override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE)}"
            error_msg += f"\n  → Example: override='{{ VALID_BODY_OVERRIDE[0] }}'"
            return (False, error_msg)
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
    if "upload-option" in payload:
        value = payload["upload-option"]
        if value not in VALID_BODY_UPLOAD_OPTION:
            desc = FIELD_DESCRIPTIONS.get("upload-option", "")
            error_msg = f"Invalid value for 'upload-option': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPLOAD_OPTION)}"
            error_msg += f"\n  → Example: upload-option='{{ VALID_BODY_UPLOAD_OPTION[0] }}'"
            return (False, error_msg)
    if "upload-interval" in payload:
        value = payload["upload-interval"]
        if value not in VALID_BODY_UPLOAD_INTERVAL:
            desc = FIELD_DESCRIPTIONS.get("upload-interval", "")
            error_msg = f"Invalid value for 'upload-interval': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPLOAD_INTERVAL)}"
            error_msg += f"\n  → Example: upload-interval='{{ VALID_BODY_UPLOAD_INTERVAL[0] }}'"
            return (False, error_msg)
    if "priority" in payload:
        value = payload["priority"]
        if value not in VALID_BODY_PRIORITY:
            desc = FIELD_DESCRIPTIONS.get("priority", "")
            error_msg = f"Invalid value for 'priority': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY)}"
            error_msg += f"\n  → Example: priority='{{ VALID_BODY_PRIORITY[0] }}'"
            return (False, error_msg)
    if "access-config" in payload:
        value = payload["access-config"]
        if value not in VALID_BODY_ACCESS_CONFIG:
            desc = FIELD_DESCRIPTIONS.get("access-config", "")
            error_msg = f"Invalid value for 'access-config': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCESS_CONFIG)}"
            error_msg += f"\n  → Example: access-config='{{ VALID_BODY_ACCESS_CONFIG[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_fortiguard_override_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update log/fortiguard/override_setting."""
    # Step 1: Validate enum values
    if "override" in payload:
        value = payload["override"]
        if value not in VALID_BODY_OVERRIDE:
            return (
                False,
                f"Invalid value for 'override'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE)}",
            )
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "upload-option" in payload:
        value = payload["upload-option"]
        if value not in VALID_BODY_UPLOAD_OPTION:
            return (
                False,
                f"Invalid value for 'upload-option'='{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_OPTION)}",
            )
    if "upload-interval" in payload:
        value = payload["upload-interval"]
        if value not in VALID_BODY_UPLOAD_INTERVAL:
            return (
                False,
                f"Invalid value for 'upload-interval'='{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_INTERVAL)}",
            )
    if "priority" in payload:
        value = payload["priority"]
        if value not in VALID_BODY_PRIORITY:
            return (
                False,
                f"Invalid value for 'priority'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY)}",
            )
    if "access-config" in payload:
        value = payload["access-config"]
        if value not in VALID_BODY_ACCESS_CONFIG:
            return (
                False,
                f"Invalid value for 'access-config'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_CONFIG)}",
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
    "endpoint": "log/fortiguard/override_setting",
    "category": "cmdb",
    "api_path": "log.fortiguard/override-setting",
    "help": "Override global FortiCloud logging settings for this VDOM.",
    "total_fields": 9,
    "required_fields_count": 0,
    "fields_with_defaults_count": 9,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
