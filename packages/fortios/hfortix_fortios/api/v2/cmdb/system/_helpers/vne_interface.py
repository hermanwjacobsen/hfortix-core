"""Validation helpers for system/vne_interface - Auto-generated"""

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
    "interface",  # Interface name.
    "bmr-hostname",  # BMR hostname.
    "br",  # IPv6 address or FQDN of the border relay.
    "update-url",  # URL of provisioning server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "interface": "",
    "ssl-certificate": "Fortinet_Factory",
    "auto-asic-offload": "enable",
    "ipv4-address": "0.0.0.0 0.0.0.0",
    "br": "",
    "update-url": "",
    "mode": "map-e",
    "http-username": "",
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
    "name": "string",  # VNE tunnel name.
    "interface": "string",  # Interface name.
    "ssl-certificate": "string",  # Name of local certificate for SSL connections.
    "bmr-hostname": "password",  # BMR hostname.
    "auto-asic-offload": "option",  # Enable/disable tunnel ASIC offloading.
    "ipv4-address": "ipv4-classnet-host",  # Tunnel IPv4 address and netmask.
    "br": "string",  # IPv6 address or FQDN of the border relay.
    "update-url": "string",  # URL of provisioning server.
    "mode": "option",  # VNE tunnel mode.
    "http-username": "string",  # HTTP authentication user name.
    "http-password": "password",  # HTTP authentication password.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "VNE tunnel name.",
    "interface": "Interface name.",
    "ssl-certificate": "Name of local certificate for SSL connections.",
    "bmr-hostname": "BMR hostname.",
    "auto-asic-offload": "Enable/disable tunnel ASIC offloading.",
    "ipv4-address": "Tunnel IPv4 address and netmask.",
    "br": "IPv6 address or FQDN of the border relay.",
    "update-url": "URL of provisioning server.",
    "mode": "VNE tunnel mode.",
    "http-username": "HTTP authentication user name.",
    "http-password": "HTTP authentication password.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 15},
    "interface": {"type": "string", "max_length": 15},
    "ssl-certificate": {"type": "string", "max_length": 35},
    "br": {"type": "string", "max_length": 255},
    "update-url": {"type": "string", "max_length": 511},
    "http-username": {"type": "string", "max_length": 64},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_AUTO_ASIC_OFFLOAD = [
    "enable",  # Enable auto ASIC offloading.
    "disable",  # Disable ASIC offloading.
]
VALID_BODY_MODE = [
    "map-e",  # Map-e mode.
    "fixed-ip",  # Fixed-ip mode.
    "ds-lite",  # DS-Lite mode.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_vne_interface_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/vne_interface."""
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
    """Validate required fields for system/vne_interface."""
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


def validate_system_vne_interface_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/vne_interface object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "auto-asic-offload" in payload:
        value = payload["auto-asic-offload"]
        if value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            desc = FIELD_DESCRIPTIONS.get("auto-asic-offload", "")
            error_msg = f"Invalid value for 'auto-asic-offload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_ASIC_OFFLOAD)}"
            error_msg += f"\n  → Example: auto-asic-offload='{{ VALID_BODY_AUTO_ASIC_OFFLOAD[0] }}'"
            return (False, error_msg)
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            desc = FIELD_DESCRIPTIONS.get("mode", "")
            error_msg = f"Invalid value for 'mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MODE)}"
            error_msg += f"\n  → Example: mode='{{ VALID_BODY_MODE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_vne_interface_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/vne_interface."""
    # Step 1: Validate enum values
    if "auto-asic-offload" in payload:
        value = payload["auto-asic-offload"]
        if value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            return (
                False,
                f"Invalid value for 'auto-asic-offload'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ASIC_OFFLOAD)}",
            )
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid value for 'mode'='{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
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
    "endpoint": "system/vne_interface",
    "category": "cmdb",
    "api_path": "system/vne-interface",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure virtual network enabler tunnels.",
    "total_fields": 11,
    "required_fields_count": 4,
    "fields_with_defaults_count": 9,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
