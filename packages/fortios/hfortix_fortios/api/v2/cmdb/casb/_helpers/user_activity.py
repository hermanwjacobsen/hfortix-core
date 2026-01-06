"""Validation helpers for casb/user_activity - Auto-generated"""

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
    "application",  # CASB SaaS application name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "uuid": "",
    "status": "enable",
    "description": "",
    "type": "customized",
    "casb-name": "",
    "application": "",
    "category": "activity-control",
    "match-strategy": "or",
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
    "name": "string",  # CASB user activity name.
    "uuid": "string",  # Universally Unique Identifier (UUID; automatically assigned 
    "status": "option",  # CASB user activity status.
    "description": "string",  # CASB user activity description.
    "type": "option",  # CASB user activity type.
    "casb-name": "string",  # CASB user activity signature name.
    "application": "string",  # CASB SaaS application name.
    "category": "option",  # CASB user activity category.
    "match-strategy": "option",  # CASB user activity match strategy.
    "match": "string",  # CASB user activity match rules.
    "control-options": "string",  # CASB control options.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "CASB user activity name.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "status": "CASB user activity status.",
    "description": "CASB user activity description.",
    "type": "CASB user activity type.",
    "casb-name": "CASB user activity signature name.",
    "application": "CASB SaaS application name.",
    "category": "CASB user activity category.",
    "match-strategy": "CASB user activity match strategy.",
    "match": "CASB user activity match rules.",
    "control-options": "CASB control options.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "uuid": {"type": "string", "max_length": 36},
    "description": {"type": "string", "max_length": 63},
    "casb-name": {"type": "string", "max_length": 79},
    "application": {"type": "string", "max_length": 79},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "match": {
        "id": {
            "type": "integer",
            "help": "CASB user activity match rules ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "strategy": {
            "type": "option",
            "help": "CASB user activity rules strategy.",
            "default": "and",
            "options": [{"help": "Match user activity using a logical AND operator.", "label": "And", "name": "and"}, {"help": "Match user activity using a logical OR operator.", "label": "Or", "name": "or"}],
        },
        "rules": {
            "type": "string",
            "help": "CASB user activity rules.",
        },
        "tenant-extraction": {
            "type": "string",
            "help": "CASB user activity tenant extraction.",
        },
    },
    "control-options": {
        "name": {
            "type": "string",
            "help": "CASB control option name.",
            "default": "",
            "max_length": 79,
        },
        "status": {
            "type": "option",
            "help": "CASB control option status.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "operations": {
            "type": "string",
            "help": "CASB control option operations.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_TYPE = [
    "built-in",  # Built-in CASB user-activity.
    "customized",  # User customized CASB user-activity.
]
VALID_BODY_CATEGORY = [
    "activity-control",  # Activity control.
    "tenant-control",  # Tenant control.
    "domain-control",  # Domain control.
    "safe-search-control",  # Safe search control.
    "advanced-tenant-control",  # Advanced tenant control.
    "other",  # User customized category.
]
VALID_BODY_MATCH_STRATEGY = [
    "and",  # Match user activity using a logical AND operator.
    "or",  # Match user activity using a logical OR operator.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_casb_user_activity_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for casb/user_activity."""
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
    """Validate required fields for casb/user_activity."""
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


def validate_casb_user_activity_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new casb/user_activity object."""
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
    if "category" in payload:
        value = payload["category"]
        if value not in VALID_BODY_CATEGORY:
            desc = FIELD_DESCRIPTIONS.get("category", "")
            error_msg = f"Invalid value for 'category': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CATEGORY)}"
            error_msg += f"\n  → Example: category='{{ VALID_BODY_CATEGORY[0] }}'"
            return (False, error_msg)
    if "match-strategy" in payload:
        value = payload["match-strategy"]
        if value not in VALID_BODY_MATCH_STRATEGY:
            desc = FIELD_DESCRIPTIONS.get("match-strategy", "")
            error_msg = f"Invalid value for 'match-strategy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MATCH_STRATEGY)}"
            error_msg += f"\n  → Example: match-strategy='{{ VALID_BODY_MATCH_STRATEGY[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_casb_user_activity_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update casb/user_activity."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "category" in payload:
        value = payload["category"]
        if value not in VALID_BODY_CATEGORY:
            return (
                False,
                f"Invalid value for 'category'='{value}'. Must be one of: {', '.join(VALID_BODY_CATEGORY)}",
            )
    if "match-strategy" in payload:
        value = payload["match-strategy"]
        if value not in VALID_BODY_MATCH_STRATEGY:
            return (
                False,
                f"Invalid value for 'match-strategy'='{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_STRATEGY)}",
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
    "endpoint": "casb/user_activity",
    "category": "cmdb",
    "api_path": "casb/user-activity",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure CASB user activity.",
    "total_fields": 11,
    "required_fields_count": 1,
    "fields_with_defaults_count": 9,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
