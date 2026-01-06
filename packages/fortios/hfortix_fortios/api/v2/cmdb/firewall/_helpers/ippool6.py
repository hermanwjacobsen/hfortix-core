"""Validation helpers for firewall/ippool6 - Auto-generated"""

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
    "name": "",
    "type": "overload",
    "startip": "::",
    "endip": "::",
    "internal-prefix": "::/0",
    "external-prefix": "::/0",
    "nat46": "disable",
    "add-nat46-route": "enable",
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
    "name": "string",  # IPv6 IP pool name.
    "type": "option",  # Configure IPv6 pool type (overload or NPTv6).
    "startip": "ipv6-address",  # First IPv6 address (inclusive) in the range for the address 
    "endip": "ipv6-address",  # Final IPv6 address (inclusive) in the range for the address 
    "internal-prefix": "ipv6-network",  # Internal NPTv6 prefix length (32 - 64).
    "external-prefix": "ipv6-network",  # External NPTv6 prefix length (32 - 64).
    "comments": "var-string",  # Comment.
    "nat46": "option",  # Enable/disable NAT46.
    "add-nat46-route": "option",  # Enable/disable adding NAT46 route.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "IPv6 IP pool name.",
    "type": "Configure IPv6 pool type (overload or NPTv6).",
    "startip": "First IPv6 address (inclusive) in the range for the address pool (format = xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx, default = ::).",
    "endip": "Final IPv6 address (inclusive) in the range for the address pool (format = xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx, default = ::).",
    "internal-prefix": "Internal NPTv6 prefix length (32 - 64).",
    "external-prefix": "External NPTv6 prefix length (32 - 64).",
    "comments": "Comment.",
    "nat46": "Enable/disable NAT46.",
    "add-nat46-route": "Enable/disable adding NAT46 route.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "overload",  # IPv6 addresses in the IP pool can be shared by clients.
    "nptv6",  # NPTv6 one to one mapping.
]
VALID_BODY_NAT46 = [
    "disable",  # Disable NAT46.
    "enable",  # Enable NAT46.
]
VALID_BODY_ADD_NAT46_ROUTE = [
    "disable",  # Disable adding NAT46 route.
    "enable",  # Enable adding NAT46 route.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_ippool6_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/ippool6."""
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
    """Validate required fields for firewall/ippool6."""
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


def validate_firewall_ippool6_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/ippool6 object."""
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
    if "nat46" in payload:
        value = payload["nat46"]
        if value not in VALID_BODY_NAT46:
            desc = FIELD_DESCRIPTIONS.get("nat46", "")
            error_msg = f"Invalid value for 'nat46': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT46)}"
            error_msg += f"\n  → Example: nat46='{{ VALID_BODY_NAT46[0] }}'"
            return (False, error_msg)
    if "add-nat46-route" in payload:
        value = payload["add-nat46-route"]
        if value not in VALID_BODY_ADD_NAT46_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("add-nat46-route", "")
            error_msg = f"Invalid value for 'add-nat46-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADD_NAT46_ROUTE)}"
            error_msg += f"\n  → Example: add-nat46-route='{{ VALID_BODY_ADD_NAT46_ROUTE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_ippool6_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/ippool6."""
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "nat46" in payload:
        value = payload["nat46"]
        if value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid value for 'nat46'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )
    if "add-nat46-route" in payload:
        value = payload["add-nat46-route"]
        if value not in VALID_BODY_ADD_NAT46_ROUTE:
            return (
                False,
                f"Invalid value for 'add-nat46-route'='{value}'. Must be one of: {', '.join(VALID_BODY_ADD_NAT46_ROUTE)}",
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
    "endpoint": "firewall/ippool6",
    "category": "cmdb",
    "api_path": "firewall/ippool6",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure IPv6 IP pools.",
    "total_fields": 9,
    "required_fields_count": 0,
    "fields_with_defaults_count": 8,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
