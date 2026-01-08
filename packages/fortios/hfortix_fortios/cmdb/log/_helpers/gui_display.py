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

# Import central validation functions (avoid duplication across 1,062 files)
from hfortix_fortios._helpers.validation import (
    validate_required_fields as _validate_required_fields,
    validate_enum_field as _validate_enum_field,
    validate_query_parameter as _validate_query_parameter,
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
    "enable",
    "disable",
]
VALID_BODY_RESOLVE_APPS = [
    "enable",
    "disable",
]
VALID_BODY_FORTIVIEW_UNSCANNED_APPS = [
    "enable",
    "disable",
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
    # Validate query parameters using central function
    if "action" in params:
        is_valid, error = _validate_query_parameter(
            "action",
            params.get("action"),
            VALID_QUERY_ACTION
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_log_gui_display_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new log/gui_display object."""
    # Step 1: Validate required fields using central function
    is_valid, error = _validate_required_fields(
        payload,
        REQUIRED_FIELDS,
        FIELD_DESCRIPTIONS
    )
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values using central function
    if "resolve-hosts" in payload:
        is_valid, error = _validate_enum_field(
            "resolve-hosts",
            payload["resolve-hosts"],
            VALID_BODY_RESOLVE_HOSTS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "resolve-apps" in payload:
        is_valid, error = _validate_enum_field(
            "resolve-apps",
            payload["resolve-apps"],
            VALID_BODY_RESOLVE_APPS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "fortiview-unscanned-apps" in payload:
        is_valid, error = _validate_enum_field(
            "fortiview-unscanned-apps",
            payload["fortiview-unscanned-apps"],
            VALID_BODY_FORTIVIEW_UNSCANNED_APPS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_gui_display_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update log/gui_display."""
    # Validate enum values using central function
    if "resolve-hosts" in payload:
        is_valid, error = _validate_enum_field(
            "resolve-hosts",
            payload["resolve-hosts"],
            VALID_BODY_RESOLVE_HOSTS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "resolve-apps" in payload:
        is_valid, error = _validate_enum_field(
            "resolve-apps",
            payload["resolve-apps"],
            VALID_BODY_RESOLVE_APPS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "fortiview-unscanned-apps" in payload:
        is_valid, error = _validate_enum_field(
            "fortiview-unscanned-apps",
            payload["fortiview-unscanned-apps"],
            VALID_BODY_FORTIVIEW_UNSCANNED_APPS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

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
