"""Validation helpers for firewall/ipmacbinding/setting - Auto-generated"""

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
    "bindthroughfw": "disable",
    "bindtofw": "disable",
    "undefinedhost": "block",
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
    "bindthroughfw": "option",  # Enable/disable use of IP/MAC binding to filter packets that 
    "bindtofw": "option",  # Enable/disable use of IP/MAC binding to filter packets that 
    "undefinedhost": "option",  # Select action to take on packets with IP/MAC addresses not i
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "bindthroughfw": "Enable/disable use of IP/MAC binding to filter packets that would normally go through the firewall.",
    "bindtofw": "Enable/disable use of IP/MAC binding to filter packets that would normally go to the firewall.",
    "undefinedhost": "Select action to take on packets with IP/MAC addresses not in the binding list (default = block).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_BINDTHROUGHFW = [
    "enable",  # Enable IP/MAC binding for packets that would normally go through the firewall.
    "disable",  # Disable IP/MAC binding for packets that would normally go through the firewall.
]
VALID_BODY_BINDTOFW = [
    "enable",  # Enable IP/MAC binding for packets that would normally go to the firewall.
    "disable",  # Disable IP/MAC binding for packets that would normally go to the firewall.
]
VALID_BODY_UNDEFINEDHOST = [
    "allow",  # Allow packets from MAC addresses not in the IP/MAC list.
    "block",  # Block packets from MAC addresses not in the IP/MAC list.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_ipmacbinding_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/ipmacbinding/setting."""
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
    """Validate required fields for firewall/ipmacbinding/setting."""
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


def validate_firewall_ipmacbinding_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/ipmacbinding/setting object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "bindthroughfw" in payload:
        value = payload["bindthroughfw"]
        if value not in VALID_BODY_BINDTHROUGHFW:
            desc = FIELD_DESCRIPTIONS.get("bindthroughfw", "")
            error_msg = f"Invalid value for 'bindthroughfw': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BINDTHROUGHFW)}"
            error_msg += f"\n  → Example: bindthroughfw='{{ VALID_BODY_BINDTHROUGHFW[0] }}'"
            return (False, error_msg)
    if "bindtofw" in payload:
        value = payload["bindtofw"]
        if value not in VALID_BODY_BINDTOFW:
            desc = FIELD_DESCRIPTIONS.get("bindtofw", "")
            error_msg = f"Invalid value for 'bindtofw': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BINDTOFW)}"
            error_msg += f"\n  → Example: bindtofw='{{ VALID_BODY_BINDTOFW[0] }}'"
            return (False, error_msg)
    if "undefinedhost" in payload:
        value = payload["undefinedhost"]
        if value not in VALID_BODY_UNDEFINEDHOST:
            desc = FIELD_DESCRIPTIONS.get("undefinedhost", "")
            error_msg = f"Invalid value for 'undefinedhost': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UNDEFINEDHOST)}"
            error_msg += f"\n  → Example: undefinedhost='{{ VALID_BODY_UNDEFINEDHOST[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_ipmacbinding_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/ipmacbinding/setting."""
    # Step 1: Validate enum values
    if "bindthroughfw" in payload:
        value = payload["bindthroughfw"]
        if value not in VALID_BODY_BINDTHROUGHFW:
            return (
                False,
                f"Invalid value for 'bindthroughfw'='{value}'. Must be one of: {', '.join(VALID_BODY_BINDTHROUGHFW)}",
            )
    if "bindtofw" in payload:
        value = payload["bindtofw"]
        if value not in VALID_BODY_BINDTOFW:
            return (
                False,
                f"Invalid value for 'bindtofw'='{value}'. Must be one of: {', '.join(VALID_BODY_BINDTOFW)}",
            )
    if "undefinedhost" in payload:
        value = payload["undefinedhost"]
        if value not in VALID_BODY_UNDEFINEDHOST:
            return (
                False,
                f"Invalid value for 'undefinedhost'='{value}'. Must be one of: {', '.join(VALID_BODY_UNDEFINEDHOST)}",
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
    "endpoint": "firewall/ipmacbinding/setting",
    "category": "cmdb",
    "api_path": "firewall.ipmacbinding/setting",
    "help": "Configure IP to MAC binding settings.",
    "total_fields": 3,
    "required_fields_count": 0,
    "fields_with_defaults_count": 3,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
