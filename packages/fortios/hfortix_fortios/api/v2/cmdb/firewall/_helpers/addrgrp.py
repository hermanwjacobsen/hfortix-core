"""Validation helpers for firewall/addrgrp - Auto-generated"""

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
    "name",  # Address group name.
    "exclude-member",  # Address exclusion member.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "type": "default",
    "category": "default",
    "allow-routing": "disable",
    "uuid": "00000000-0000-0000-0000-000000000000",
    "exclude": "disable",
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
    "name": "string",  # Address group name.
    "type": "option",  # Address group type.
    "category": "option",  # Address group category.
    "allow-routing": "option",  # Enable/disable use of this group in routing configurations.
    "member": "string",  # Address objects contained within the group.
    "comment": "var-string",  # Comment.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "exclude": "option",  # Enable/disable address exclusion.
    "exclude-member": "string",  # Address exclusion member.
    "color": "integer",  # Color of icon on the GUI.
    "tagging": "string",  # Config object tagging.
    "fabric-object": "option",  # Security Fabric global object setting.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Address group name.",
    "type": "Address group type.",
    "category": "Address group category.",
    "allow-routing": "Enable/disable use of this group in routing configurations.",
    "member": "Address objects contained within the group.",
    "comment": "Comment.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "exclude": "Enable/disable address exclusion.",
    "exclude-member": "Address exclusion member.",
    "color": "Color of icon on the GUI.",
    "tagging": "Config object tagging.",
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
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "exclude-member": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "tagging": {
        "name": {
            "type": "string",
            "help": "Tagging entry name.",
            "default": "",
            "max_length": 63,
        },
        "category": {
            "type": "string",
            "help": "Tag category.",
            "default": "",
            "max_length": 63,
        },
        "tags": {
            "type": "string",
            "help": "Tags.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "default",  # Default address group type (address may belong to multiple groups).
    "folder",  # Address folder group (members may not belong to any other group).
]
VALID_BODY_CATEGORY = [
    "default",  # Default address group category (cannot be used as ztna-ems-tag/ztna-geo-tag in policy).
    "ztna-ems-tag",  # Members must be ztna-ems-tag group or ems-tag address, can be used as ztna-ems-tag in policy.
    "ztna-geo-tag",  # Members must be ztna-geo-tag group or geographic address, can be used as ztna-geo-tag in policy.
]
VALID_BODY_ALLOW_ROUTING = [
    "enable",  # Enable use of this group in routing configurations.
    "disable",  # Disable use of this group in routing configurations.
]
VALID_BODY_EXCLUDE = [
    "enable",  # Enable address exclusion.
    "disable",  # Disable address exclusion.
]
VALID_BODY_FABRIC_OBJECT = [
    "enable",  # Object is set as a security fabric-wide global object.
    "disable",  # Object is local to this security fabric member.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_addrgrp_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/addrgrp."""
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
    """Validate required fields for firewall/addrgrp."""
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


def validate_firewall_addrgrp_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/addrgrp object."""
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
    if "allow-routing" in payload:
        value = payload["allow-routing"]
        if value not in VALID_BODY_ALLOW_ROUTING:
            desc = FIELD_DESCRIPTIONS.get("allow-routing", "")
            error_msg = f"Invalid value for 'allow-routing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_ROUTING)}"
            error_msg += f"\n  → Example: allow-routing='{{ VALID_BODY_ALLOW_ROUTING[0] }}'"
            return (False, error_msg)
    if "exclude" in payload:
        value = payload["exclude"]
        if value not in VALID_BODY_EXCLUDE:
            desc = FIELD_DESCRIPTIONS.get("exclude", "")
            error_msg = f"Invalid value for 'exclude': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXCLUDE)}"
            error_msg += f"\n  → Example: exclude='{{ VALID_BODY_EXCLUDE[0] }}'"
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


def validate_firewall_addrgrp_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/addrgrp."""
    # Step 1: Validate enum values
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
    if "allow-routing" in payload:
        value = payload["allow-routing"]
        if value not in VALID_BODY_ALLOW_ROUTING:
            return (
                False,
                f"Invalid value for 'allow-routing'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_ROUTING)}",
            )
    if "exclude" in payload:
        value = payload["exclude"]
        if value not in VALID_BODY_EXCLUDE:
            return (
                False,
                f"Invalid value for 'exclude'='{value}'. Must be one of: {', '.join(VALID_BODY_EXCLUDE)}",
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
    "endpoint": "firewall/addrgrp",
    "category": "cmdb",
    "api_path": "firewall/addrgrp",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure IPv4 address groups.",
    "total_fields": 12,
    "required_fields_count": 2,
    "fields_with_defaults_count": 8,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
