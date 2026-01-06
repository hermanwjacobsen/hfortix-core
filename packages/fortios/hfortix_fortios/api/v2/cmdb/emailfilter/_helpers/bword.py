"""Validation helpers for emailfilter/bword - Auto-generated"""

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
    "name",  # Name of table.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "name": "",
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
    "id": "integer",  # ID.
    "name": "string",  # Name of table.
    "comment": "var-string",  # Optional comments.
    "entries": "string",  # Spam filter banned word.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "ID.",
    "name": "Name of table.",
    "comment": "Optional comments.",
    "entries": "Spam filter banned word.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "name": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "entries": {
        "status": {
            "type": "option",
            "help": "Enable/disable status.",
            "required": True,
            "default": "enable",
            "options": [{"help": "Enable status.", "label": "Enable", "name": "enable"}, {"help": "Disable status.", "label": "Disable", "name": "disable"}],
        },
        "id": {
            "type": "integer",
            "help": "Banned word entry ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "pattern": {
            "type": "string",
            "help": "Pattern for the banned word.",
            "required": True,
            "default": "",
            "max_length": 127,
        },
        "pattern-type": {
            "type": "option",
            "help": "Wildcard pattern or regular expression.",
            "required": True,
            "default": "wildcard",
            "options": [{"help": "Wildcard pattern.", "label": "Wildcard", "name": "wildcard"}, {"help": "Perl regular expression.", "label": "Regexp", "name": "regexp"}],
        },
        "action": {
            "type": "option",
            "help": "Mark spam or good.",
            "required": True,
            "default": "spam",
            "options": [{"help": "Mark as spam email.", "label": "Spam", "name": "spam"}, {"help": "Mark as good email.", "label": "Clear", "name": "clear"}],
        },
        "where": {
            "type": "option",
            "help": "Component of the email to be scanned.",
            "required": True,
            "default": "all",
            "options": [{"help": "Banned word in email subject.", "label": "Subject", "name": "subject"}, {"help": "Banned word in email body.", "label": "Body", "name": "body"}, {"help": "Banned word in both subject and body.", "label": "All", "name": "all"}],
        },
        "language": {
            "type": "option",
            "help": "Language for the banned word.",
            "required": True,
            "default": "western",
            "options": [{"help": "Western.", "label": "Western", "name": "western"}, {"help": "Simplified Chinese.", "label": "Simch", "name": "simch"}, {"help": "Traditional Chinese.", "label": "Trach", "name": "trach"}, {"help": "Japanese.", "label": "Japanese", "name": "japanese"}, {"help": "Korean.", "label": "Korean", "name": "korean"}, {"help": "French.", "label": "French", "name": "french"}, {"help": "Thai.", "label": "Thai", "name": "thai"}, {"help": "Spanish.", "label": "Spanish", "name": "spanish"}],
        },
        "score": {
            "type": "integer",
            "help": "Score value.",
            "default": 10,
            "min_value": 1,
            "max_value": 99999,
        },
    },
}


# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_emailfilter_bword_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for emailfilter/bword."""
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
    """Validate required fields for emailfilter/bword."""
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


def validate_emailfilter_bword_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new emailfilter/bword object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_emailfilter_bword_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update emailfilter/bword."""
    # Step 1: Validate enum values

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
    "endpoint": "emailfilter/bword",
    "category": "cmdb",
    "api_path": "emailfilter/bword",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure AntiSpam banned word list.",
    "total_fields": 4,
    "required_fields_count": 1,
    "fields_with_defaults_count": 2,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
