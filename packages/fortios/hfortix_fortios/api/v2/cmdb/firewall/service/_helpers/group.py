"""Validation helpers for firewall/service/group - Auto-generated"""

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
    "name",  # Service group name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "uuid": "00000000-0000-0000-0000-000000000000",
    "proxy": "disable",
    "color": 0,
    "fabric-object": "disable",
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
    "name": "string",  # Service group name.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "proxy": "option",  # Enable/disable web proxy service group.
    "member": "string",  # Service objects contained within the group.
    "comment": "var-string",  # Comment.
    "color": "integer",  # Color of icon on the GUI.
    "fabric-object": "option",  # Security Fabric global object setting.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Service group name.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "proxy": "Enable/disable web proxy service group.",
    "member": "Service objects contained within the group.",
    "comment": "Comment.",
    "color": "Color of icon on the GUI.",
    "fabric-object": "Security Fabric global object setting.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "color": {"type": "integer", "min": 0, "max": 32},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "member": {
        "name": {
            "type": "string",
            "help": "Service or service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_PROXY = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_FABRIC_OBJECT = [
    "enable",  # Object is set as a security fabric-wide global object.
    "disable",  # Object is local to this security fabric member.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_service_group_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/service/group."""
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
    """Validate required fields for firewall/service/group."""
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


def validate_firewall_service_group_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/service/group object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "proxy" in payload:
        value = payload["proxy"]
        if value not in VALID_BODY_PROXY:
            desc = FIELD_DESCRIPTIONS.get("proxy", "")
            error_msg = f"Invalid value for 'proxy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROXY)}"
            error_msg += f"\n  → Example: proxy='{{ VALID_BODY_PROXY[0] }}'"
            return (False, error_msg)
    if "fabric-object" in payload:
        value = payload["fabric-object"]
        if value not in VALID_BODY_FABRIC_OBJECT:
            desc = FIELD_DESCRIPTIONS.get("fabric-object", "")
            error_msg = f"Invalid value for 'fabric-object': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FABRIC_OBJECT)}"
            error_msg += f"\n  → Example: fabric-object='{{ VALID_BODY_FABRIC_OBJECT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_service_group_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/service/group."""
    # Step 1: Validate enum values
    if "proxy" in payload:
        value = payload["proxy"]
        if value not in VALID_BODY_PROXY:
            return (
                False,
                f"Invalid value for 'proxy'='{value}'. Must be one of: {', '.join(VALID_BODY_PROXY)}",
            )
    if "fabric-object" in payload:
        value = payload["fabric-object"]
        if value not in VALID_BODY_FABRIC_OBJECT:
            return (
                False,
                f"Invalid value for 'fabric-object'='{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_OBJECT)}",
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
    "endpoint": "firewall/service/group",
    "category": "cmdb",
    "api_path": "firewall.service/group",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure service groups.",
    "total_fields": 7,
    "required_fields_count": 1,
    "fields_with_defaults_count": 5,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
