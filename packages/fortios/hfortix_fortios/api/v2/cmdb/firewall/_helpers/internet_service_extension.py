"""Validation helpers for firewall/internet_service_extension - Auto-generated"""

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
    "id": "integer",  # Internet Service ID in the Internet Service database.
    "comment": "var-string",  # Comment.
    "entry": "string",  # Entries added to the Internet Service extension database.
    "disable-entry": "string",  # Disable entries in the Internet Service database.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "Internet Service ID in the Internet Service database.",
    "comment": "Comment.",
    "entry": "Entries added to the Internet Service extension database.",
    "disable-entry": "Disable entries in the Internet Service database.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "entry": {
        "id": {
            "type": "integer",
            "help": "Entry ID(1-255).",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "addr-mode": {
            "type": "option",
            "help": "Address mode (IPv4 or IPv6).",
            "default": "ipv4",
            "options": [{"help": "IPv4 mode.", "label": "Ipv4", "name": "ipv4"}, {"help": "IPv6 mode.", "label": "Ipv6", "name": "ipv6"}],
        },
        "protocol": {
            "type": "integer",
            "help": "Integer value for the protocol type as defined by IANA (0 - 255).",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "port-range": {
            "type": "string",
            "help": "Port ranges in the custom entry.",
        },
        "dst": {
            "type": "string",
            "help": "Destination address or address group name.",
        },
        "dst6": {
            "type": "string",
            "help": "Destination address6 or address6 group name.",
        },
    },
    "disable-entry": {
        "id": {
            "type": "integer",
            "help": "Disable entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "addr-mode": {
            "type": "option",
            "help": "Address mode (IPv4 or IPv6).",
            "default": "ipv4",
            "options": [{"help": "IPv4 mode.", "label": "Ipv4", "name": "ipv4"}, {"help": "IPv6 mode.", "label": "Ipv6", "name": "ipv6"}],
        },
        "protocol": {
            "type": "integer",
            "help": "Integer value for the protocol type as defined by IANA (0 - 255).",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "port-range": {
            "type": "string",
            "help": "Port ranges in the disable entry.",
        },
        "ip-range": {
            "type": "string",
            "help": "IPv4 ranges in the disable entry.",
        },
        "ip6-range": {
            "type": "string",
            "help": "IPv6 ranges in the disable entry.",
        },
    },
}


# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_internet_service_extension_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/internet_service_extension."""
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
    """Validate required fields for firewall/internet_service_extension."""
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


def validate_firewall_internet_service_extension_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/internet_service_extension object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_internet_service_extension_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/internet_service_extension."""
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
    "endpoint": "firewall/internet_service_extension",
    "category": "cmdb",
    "api_path": "firewall/internet-service-extension",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure Internet Services Extension.",
    "total_fields": 4,
    "required_fields_count": 0,
    "fields_with_defaults_count": 1,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
