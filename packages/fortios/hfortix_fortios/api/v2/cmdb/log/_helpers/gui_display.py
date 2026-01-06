"""Validation helpers for log/gui_display - Auto-generated"""

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
    "resolve-hosts": "enable",
    "resolve-apps": "enable",
    "fortiview-unscanned-apps": "disable",
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
    "resolve-hosts": "option",  # Enable/disable resolving IP addresses to hostname in log mes
    "resolve-apps": "option",  # Resolve unknown applications on the GUI using Fortinet's rem
    "fortiview-unscanned-apps": "option",  # Enable/disable showing unscanned traffic in FortiView applic
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "resolve-hosts": "Enable/disable resolving IP addresses to hostname in log messages on the GUI using reverse DNS lookup.",
    "resolve-apps": "Resolve unknown applications on the GUI using Fortinet's remote application database.",
    "fortiview-unscanned-apps": "Enable/disable showing unscanned traffic in FortiView application charts.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_RESOLVE_HOSTS = [
    "enable",  # Enable resolving IP addresses to hostnames.
    "disable",  # Disable resolving IP addresses to hostnames.
]
VALID_BODY_RESOLVE_APPS = [
    "enable",  # Enable unknown applications on the GUI.
    "disable",  # Disable unknown applications on the GUI.
]
VALID_BODY_FORTIVIEW_UNSCANNED_APPS = [
    "enable",  # Enable showing unscanned traffic.
    "disable",  # Disable showing unscanned traffic.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_log_gui_display_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for log/gui_display."""
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
    """Validate required fields for log/gui_display."""
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


def validate_log_gui_display_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new log/gui_display object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "resolve-hosts" in payload:
        value = payload["resolve-hosts"]
        if value not in VALID_BODY_RESOLVE_HOSTS:
            desc = FIELD_DESCRIPTIONS.get("resolve-hosts", "")
            error_msg = f"Invalid value for 'resolve-hosts': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESOLVE_HOSTS)}"
            error_msg += f"\n  → Example: resolve-hosts='{{ VALID_BODY_RESOLVE_HOSTS[0] }}'"
            return (False, error_msg)
    if "resolve-apps" in payload:
        value = payload["resolve-apps"]
        if value not in VALID_BODY_RESOLVE_APPS:
            desc = FIELD_DESCRIPTIONS.get("resolve-apps", "")
            error_msg = f"Invalid value for 'resolve-apps': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESOLVE_APPS)}"
            error_msg += f"\n  → Example: resolve-apps='{{ VALID_BODY_RESOLVE_APPS[0] }}'"
            return (False, error_msg)
    if "fortiview-unscanned-apps" in payload:
        value = payload["fortiview-unscanned-apps"]
        if value not in VALID_BODY_FORTIVIEW_UNSCANNED_APPS:
            desc = FIELD_DESCRIPTIONS.get("fortiview-unscanned-apps", "")
            error_msg = f"Invalid value for 'fortiview-unscanned-apps': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTIVIEW_UNSCANNED_APPS)}"
            error_msg += f"\n  → Example: fortiview-unscanned-apps='{{ VALID_BODY_FORTIVIEW_UNSCANNED_APPS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_gui_display_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update log/gui_display."""
    # Step 1: Validate enum values
    if "resolve-hosts" in payload:
        value = payload["resolve-hosts"]
        if value not in VALID_BODY_RESOLVE_HOSTS:
            return (
                False,
                f"Invalid value for 'resolve-hosts'='{value}'. Must be one of: {', '.join(VALID_BODY_RESOLVE_HOSTS)}",
            )
    if "resolve-apps" in payload:
        value = payload["resolve-apps"]
        if value not in VALID_BODY_RESOLVE_APPS:
            return (
                False,
                f"Invalid value for 'resolve-apps'='{value}'. Must be one of: {', '.join(VALID_BODY_RESOLVE_APPS)}",
            )
    if "fortiview-unscanned-apps" in payload:
        value = payload["fortiview-unscanned-apps"]
        if value not in VALID_BODY_FORTIVIEW_UNSCANNED_APPS:
            return (
                False,
                f"Invalid value for 'fortiview-unscanned-apps'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTIVIEW_UNSCANNED_APPS)}",
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
    "endpoint": "log/gui_display",
    "category": "cmdb",
    "api_path": "log/gui-display",
    "help": "Configure how log messages are displayed on the GUI.",
    "total_fields": 3,
    "required_fields_count": 0,
    "fields_with_defaults_count": 3,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
