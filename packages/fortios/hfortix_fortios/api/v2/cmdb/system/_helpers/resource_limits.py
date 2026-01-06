"""Validation helpers for system/resource_limits - Auto-generated"""

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
    "session": "",
    "ipsec-phase1": "",
    "ipsec-phase2": "",
    "ipsec-phase1-interface": "",
    "ipsec-phase2-interface": "",
    "dialup-tunnel": "",
    "firewall-policy": "",
    "firewall-address": "",
    "firewall-addrgrp": "",
    "custom-service": "",
    "service-group": "",
    "onetime-schedule": "",
    "recurring-schedule": "",
    "user": "",
    "user-group": "",
    "sslvpn": "",
    "proxy": "",
    "log-disk-quota": 0,
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
    "session": "integer",  # Maximum number of sessions.
    "ipsec-phase1": "integer",  # Maximum number of VPN IPsec phase1 tunnels.
    "ipsec-phase2": "integer",  # Maximum number of VPN IPsec phase2 tunnels.
    "ipsec-phase1-interface": "integer",  # Maximum number of VPN IPsec phase1 interface tunnels.
    "ipsec-phase2-interface": "integer",  # Maximum number of VPN IPsec phase2 interface tunnels.
    "dialup-tunnel": "integer",  # Maximum number of dial-up tunnels.
    "firewall-policy": "integer",  # Maximum number of firewall policies (policy, DoS-policy4, Do
    "firewall-address": "integer",  # Maximum number of firewall addresses (IPv4, IPv6, multicast)
    "firewall-addrgrp": "integer",  # Maximum number of firewall address groups (IPv4, IPv6).
    "custom-service": "integer",  # Maximum number of firewall custom services.
    "service-group": "integer",  # Maximum number of firewall service groups.
    "onetime-schedule": "integer",  # Maximum number of firewall one-time schedules.
    "recurring-schedule": "integer",  # Maximum number of firewall recurring schedules.
    "user": "integer",  # Maximum number of local users.
    "user-group": "integer",  # Maximum number of user groups.
    "sslvpn": "integer",  # Maximum number of Agentless VPN.
    "proxy": "integer",  # Maximum number of concurrent proxy users.
    "log-disk-quota": "integer",  # Log disk quota in megabytes (MB).
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "session": "Maximum number of sessions.",
    "ipsec-phase1": "Maximum number of VPN IPsec phase1 tunnels.",
    "ipsec-phase2": "Maximum number of VPN IPsec phase2 tunnels.",
    "ipsec-phase1-interface": "Maximum number of VPN IPsec phase1 interface tunnels.",
    "ipsec-phase2-interface": "Maximum number of VPN IPsec phase2 interface tunnels.",
    "dialup-tunnel": "Maximum number of dial-up tunnels.",
    "firewall-policy": "Maximum number of firewall policies (policy, DoS-policy4, DoS-policy6, multicast).",
    "firewall-address": "Maximum number of firewall addresses (IPv4, IPv6, multicast).",
    "firewall-addrgrp": "Maximum number of firewall address groups (IPv4, IPv6).",
    "custom-service": "Maximum number of firewall custom services.",
    "service-group": "Maximum number of firewall service groups.",
    "onetime-schedule": "Maximum number of firewall one-time schedules.",
    "recurring-schedule": "Maximum number of firewall recurring schedules.",
    "user": "Maximum number of local users.",
    "user-group": "Maximum number of user groups.",
    "sslvpn": "Maximum number of Agentless VPN.",
    "proxy": "Maximum number of concurrent proxy users.",
    "log-disk-quota": "Log disk quota in megabytes (MB).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "session": {"type": "integer", "min": 0, "max": 4294967295},
    "ipsec-phase1": {"type": "integer", "min": 0, "max": 4294967295},
    "ipsec-phase2": {"type": "integer", "min": 0, "max": 4294967295},
    "ipsec-phase1-interface": {"type": "integer", "min": 0, "max": 4294967295},
    "ipsec-phase2-interface": {"type": "integer", "min": 0, "max": 4294967295},
    "dialup-tunnel": {"type": "integer", "min": 0, "max": 4294967295},
    "firewall-policy": {"type": "integer", "min": 0, "max": 4294967295},
    "firewall-address": {"type": "integer", "min": 0, "max": 4294967295},
    "firewall-addrgrp": {"type": "integer", "min": 0, "max": 4294967295},
    "custom-service": {"type": "integer", "min": 0, "max": 4294967295},
    "service-group": {"type": "integer", "min": 0, "max": 4294967295},
    "onetime-schedule": {"type": "integer", "min": 0, "max": 4294967295},
    "recurring-schedule": {"type": "integer", "min": 0, "max": 4294967295},
    "user": {"type": "integer", "min": 0, "max": 4294967295},
    "user-group": {"type": "integer", "min": 0, "max": 4294967295},
    "sslvpn": {"type": "integer", "min": 0, "max": 4294967295},
    "proxy": {"type": "integer", "min": 0, "max": 4294967295},
    "log-disk-quota": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_resource_limits_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/resource_limits."""
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
    """Validate required fields for system/resource_limits."""
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


def validate_system_resource_limits_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/resource_limits object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_resource_limits_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/resource_limits."""
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
    "endpoint": "system/resource_limits",
    "category": "cmdb",
    "api_path": "system/resource-limits",
    "help": "Configure resource limits.",
    "total_fields": 18,
    "required_fields_count": 0,
    "fields_with_defaults_count": 18,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
