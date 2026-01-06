"""Validation helpers for dlp/dictionary - Auto-generated"""

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
    "name",  # Name of table containing the dictionary.
    "entries",  # DLP dictionary entries.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "uuid": "00000000-0000-0000-0000-000000000000",
    "name": "",
    "match-type": "match-any",
    "match-around": "disable",
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
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "name": "string",  # Name of table containing the dictionary.
    "match-type": "option",  # Logical relation between entries (default = match-any).
    "match-around": "option",  # Enable/disable match-around support.
    "comment": "var-string",  # Optional comments.
    "entries": "string",  # DLP dictionary entries.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "name": "Name of table containing the dictionary.",
    "match-type": "Logical relation between entries (default = match-any).",
    "match-around": "Enable/disable match-around support.",
    "comment": "Optional comments.",
    "entries": "DLP dictionary entries.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "entries": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "type": {
            "type": "string",
            "help": "Pattern type to match.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "pattern": {
            "type": "string",
            "help": "Pattern to match.",
            "required": True,
            "default": "",
            "max_length": 255,
        },
        "ignore-case": {
            "type": "option",
            "help": "Enable/disable ignore case.",
            "default": "disable",
            "options": [{"help": "Enable ignore case.", "label": "Enable", "name": "enable"}, {"help": "Disable ignore case.", "label": "Disable", "name": "disable"}],
        },
        "repeat": {
            "type": "option",
            "help": "Enable/disable repeat match.",
            "default": "disable",
            "options": [{"help": "Enable repeat match.", "label": "Enable", "name": "enable"}, {"help": "Disable repeat match.", "label": "Disable", "name": "disable"}],
        },
        "status": {
            "type": "option",
            "help": "Enable/disable this pattern.",
            "default": "enable",
            "options": [{"help": "Enable this pattern.", "label": "Enable", "name": "enable"}, {"help": "Disable this pattern.", "label": "Disable", "name": "disable"}],
        },
        "comment": {
            "type": "var-string",
            "help": "Optional comments.",
            "max_length": 255,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_MATCH_TYPE = [
    "match-all",  # Match all entries.
    "match-any",  # Match any entries.
]
VALID_BODY_MATCH_AROUND = [
    "enable",  # Enable match-around support.
    "disable",  # Disable match-around support.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_dlp_dictionary_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for dlp/dictionary."""
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
    """Validate required fields for dlp/dictionary."""
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


def validate_dlp_dictionary_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new dlp/dictionary object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "match-type" in payload:
        value = payload["match-type"]
        if value not in VALID_BODY_MATCH_TYPE:
            desc = FIELD_DESCRIPTIONS.get("match-type", "")
            error_msg = f"Invalid value for 'match-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MATCH_TYPE)}"
            error_msg += f"\n  → Example: match-type='{{ VALID_BODY_MATCH_TYPE[0] }}'"
            return (False, error_msg)
    if "match-around" in payload:
        value = payload["match-around"]
        if value not in VALID_BODY_MATCH_AROUND:
            desc = FIELD_DESCRIPTIONS.get("match-around", "")
            error_msg = f"Invalid value for 'match-around': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MATCH_AROUND)}"
            error_msg += f"\n  → Example: match-around='{{ VALID_BODY_MATCH_AROUND[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_dlp_dictionary_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update dlp/dictionary."""
    # Step 1: Validate enum values
    if "match-type" in payload:
        value = payload["match-type"]
        if value not in VALID_BODY_MATCH_TYPE:
            return (
                False,
                f"Invalid value for 'match-type'='{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_TYPE)}",
            )
    if "match-around" in payload:
        value = payload["match-around"]
        if value not in VALID_BODY_MATCH_AROUND:
            return (
                False,
                f"Invalid value for 'match-around'='{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_AROUND)}",
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
    "endpoint": "dlp/dictionary",
    "category": "cmdb",
    "api_path": "dlp/dictionary",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure dictionaries used by DLP blocking.",
    "total_fields": 6,
    "required_fields_count": 2,
    "fields_with_defaults_count": 4,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
