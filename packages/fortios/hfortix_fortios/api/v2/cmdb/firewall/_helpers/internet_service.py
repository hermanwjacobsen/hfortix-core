"""Validation helpers for firewall/internet_service - Auto-generated"""

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
    "id": 0,
    "name": "",
    "icon-id": 0,
    "direction": "both",
    "database": "isdb",
    "ip-range-number": 0,
    "extra-ip-range-number": 0,
    "ip-number": 0,
    "ip6-range-number": 0,
    "extra-ip6-range-number": 0,
    "singularity": 0,
    "obsolete": 0,
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
    "id": "integer",  # Internet Service ID.
    "name": "string",  # Internet Service name.
    "icon-id": "integer",  # Icon ID of Internet Service.
    "direction": "option",  # How this service may be used in a firewall policy (source, d
    "database": "option",  # Database name this Internet Service belongs to.
    "ip-range-number": "integer",  # Number of IPv4 ranges.
    "extra-ip-range-number": "integer",  # Extra number of IPv4 ranges.
    "ip-number": "integer",  # Total number of IPv4 addresses.
    "ip6-range-number": "integer",  # Number of IPv6 ranges.
    "extra-ip6-range-number": "integer",  # Extra number of IPv6 ranges.
    "singularity": "integer",  # Singular level of the Internet Service.
    "obsolete": "integer",  # Indicates whether the Internet Service can be used.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "Internet Service ID.",
    "name": "Internet Service name.",
    "icon-id": "Icon ID of Internet Service.",
    "direction": "How this service may be used in a firewall policy (source, destination or both).",
    "database": "Database name this Internet Service belongs to.",
    "ip-range-number": "Number of IPv4 ranges.",
    "extra-ip-range-number": "Extra number of IPv4 ranges.",
    "ip-number": "Total number of IPv4 addresses.",
    "ip6-range-number": "Number of IPv6 ranges.",
    "extra-ip6-range-number": "Extra number of IPv6 ranges.",
    "singularity": "Singular level of the Internet Service.",
    "obsolete": "Indicates whether the Internet Service can be used.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "name": {"type": "string", "max_length": 63},
    "icon-id": {"type": "integer", "min": 0, "max": 4294967295},
    "ip-range-number": {"type": "integer", "min": 0, "max": 4294967295},
    "extra-ip-range-number": {"type": "integer", "min": 0, "max": 4294967295},
    "ip-number": {"type": "integer", "min": 0, "max": 4294967295},
    "ip6-range-number": {"type": "integer", "min": 0, "max": 4294967295},
    "extra-ip6-range-number": {"type": "integer", "min": 0, "max": 4294967295},
    "singularity": {"type": "integer", "min": 0, "max": 65535},
    "obsolete": {"type": "integer", "min": 0, "max": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_DIRECTION = [
    "src",  # As source in the firewall policy.
    "dst",  # As destination in the firewall policy.
    "both",  # Both directions in the firewall policy.
]
VALID_BODY_DATABASE = [
    "isdb",  # Internet Service Database.
    "irdb",  # Internet RRR Database.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_internet_service_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/internet_service."""
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
    """Validate required fields for firewall/internet_service."""
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


def validate_firewall_internet_service_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/internet_service object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "direction" in payload:
        value = payload["direction"]
        if value not in VALID_BODY_DIRECTION:
            desc = FIELD_DESCRIPTIONS.get("direction", "")
            error_msg = f"Invalid value for 'direction': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIRECTION)}"
            error_msg += f"\n  → Example: direction='{{ VALID_BODY_DIRECTION[0] }}'"
            return (False, error_msg)
    if "database" in payload:
        value = payload["database"]
        if value not in VALID_BODY_DATABASE:
            desc = FIELD_DESCRIPTIONS.get("database", "")
            error_msg = f"Invalid value for 'database': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DATABASE)}"
            error_msg += f"\n  → Example: database='{{ VALID_BODY_DATABASE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_internet_service_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/internet_service."""
    # Step 1: Validate enum values
    if "direction" in payload:
        value = payload["direction"]
        if value not in VALID_BODY_DIRECTION:
            return (
                False,
                f"Invalid value for 'direction'='{value}'. Must be one of: {', '.join(VALID_BODY_DIRECTION)}",
            )
    if "database" in payload:
        value = payload["database"]
        if value not in VALID_BODY_DATABASE:
            return (
                False,
                f"Invalid value for 'database'='{value}'. Must be one of: {', '.join(VALID_BODY_DATABASE)}",
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
    "endpoint": "firewall/internet_service",
    "category": "cmdb",
    "api_path": "firewall/internet-service",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Show Internet Service application.",
    "total_fields": 12,
    "required_fields_count": 0,
    "fields_with_defaults_count": 12,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
