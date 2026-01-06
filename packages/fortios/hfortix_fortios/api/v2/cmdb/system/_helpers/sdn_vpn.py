"""Validation helpers for system/sdn_vpn - Auto-generated"""

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
    "sdn",  # SDN connector name.
    "vgw-id",  # Virtual private gateway id.
    "tgw-id",  # Transit gateway id.
    "tunnel-interface",  # Tunnel interface with public IP.
    "internal-interface",  # Internal interface with local subnet.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "sdn": "",
    "remote-type": "vgw",
    "routing-type": "dynamic",
    "vgw-id": "",
    "tgw-id": "",
    "subnet-id": "",
    "bgp-as": 65000,
    "cgw-gateway": "0.0.0.0",
    "nat-traversal": "enable",
    "tunnel-interface": "",
    "internal-interface": "",
    "local-cidr": "0.0.0.0 0.0.0.0",
    "remote-cidr": "0.0.0.0 0.0.0.0",
    "cgw-name": "",
    "type": 0,
    "status": 0,
    "code": 0,
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
    "name": "string",  # Public cloud VPN name.
    "sdn": "string",  # SDN connector name.
    "remote-type": "option",  # Type of remote device.
    "routing-type": "option",  # Type of routing.
    "vgw-id": "string",  # Virtual private gateway id.
    "tgw-id": "string",  # Transit gateway id.
    "subnet-id": "string",  # AWS subnet id for TGW route propagation.
    "bgp-as": "integer",  # BGP Router AS number.
    "cgw-gateway": "ipv4-address-any",  # Public IP address of the customer gateway.
    "nat-traversal": "option",  # Enable/disable use for NAT traversal. Please enable if your 
    "tunnel-interface": "string",  # Tunnel interface with public IP.
    "internal-interface": "string",  # Internal interface with local subnet.
    "local-cidr": "ipv4-classnet",  # Local subnet address and subnet mask.
    "remote-cidr": "ipv4-classnet",  # Remote subnet address and subnet mask.
    "cgw-name": "string",  # AWS customer gateway name to be created.
    "psksecret": "password-3",  # Pre-shared secret for PSK authentication. Auto-generated if 
    "type": "integer",  # SDN VPN type.
    "status": "integer",  # SDN VPN status.
    "code": "integer",  # SDN VPN error code.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Public cloud VPN name.",
    "sdn": "SDN connector name.",
    "remote-type": "Type of remote device.",
    "routing-type": "Type of routing.",
    "vgw-id": "Virtual private gateway id.",
    "tgw-id": "Transit gateway id.",
    "subnet-id": "AWS subnet id for TGW route propagation.",
    "bgp-as": "BGP Router AS number.",
    "cgw-gateway": "Public IP address of the customer gateway.",
    "nat-traversal": "Enable/disable use for NAT traversal. Please enable if your FortiGate device is behind a NAT/PAT device.",
    "tunnel-interface": "Tunnel interface with public IP.",
    "internal-interface": "Internal interface with local subnet.",
    "local-cidr": "Local subnet address and subnet mask.",
    "remote-cidr": "Remote subnet address and subnet mask.",
    "cgw-name": "AWS customer gateway name to be created.",
    "psksecret": "Pre-shared secret for PSK authentication. Auto-generated if not specified",
    "type": "SDN VPN type.",
    "status": "SDN VPN status.",
    "code": "SDN VPN error code.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "sdn": {"type": "string", "max_length": 35},
    "vgw-id": {"type": "string", "max_length": 63},
    "tgw-id": {"type": "string", "max_length": 63},
    "subnet-id": {"type": "string", "max_length": 63},
    "bgp-as": {"type": "integer", "min": 1, "max": 4294967295},
    "tunnel-interface": {"type": "string", "max_length": 15},
    "internal-interface": {"type": "string", "max_length": 15},
    "cgw-name": {"type": "string", "max_length": 35},
    "type": {"type": "integer", "min": 0, "max": 65535},
    "status": {"type": "integer", "min": 0, "max": 255},
    "code": {"type": "integer", "min": 0, "max": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_REMOTE_TYPE = [
    "vgw",  # Virtual private gateway.
    "tgw",  # Transit gateway.
]
VALID_BODY_ROUTING_TYPE = [
    "static",  # Static routing.
    "dynamic",  # Dynamic routing.
]
VALID_BODY_NAT_TRAVERSAL = [
    "disable",  # Disable NAT traversal.
    "enable",  # Enable NAT traversal.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_sdn_vpn_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/sdn_vpn."""
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
    """Validate required fields for system/sdn_vpn."""
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


def validate_system_sdn_vpn_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/sdn_vpn object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "remote-type" in payload:
        value = payload["remote-type"]
        if value not in VALID_BODY_REMOTE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("remote-type", "")
            error_msg = f"Invalid value for 'remote-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REMOTE_TYPE)}"
            error_msg += f"\n  → Example: remote-type='{{ VALID_BODY_REMOTE_TYPE[0] }}'"
            return (False, error_msg)
    if "routing-type" in payload:
        value = payload["routing-type"]
        if value not in VALID_BODY_ROUTING_TYPE:
            desc = FIELD_DESCRIPTIONS.get("routing-type", "")
            error_msg = f"Invalid value for 'routing-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROUTING_TYPE)}"
            error_msg += f"\n  → Example: routing-type='{{ VALID_BODY_ROUTING_TYPE[0] }}'"
            return (False, error_msg)
    if "nat-traversal" in payload:
        value = payload["nat-traversal"]
        if value not in VALID_BODY_NAT_TRAVERSAL:
            desc = FIELD_DESCRIPTIONS.get("nat-traversal", "")
            error_msg = f"Invalid value for 'nat-traversal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT_TRAVERSAL)}"
            error_msg += f"\n  → Example: nat-traversal='{{ VALID_BODY_NAT_TRAVERSAL[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_sdn_vpn_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/sdn_vpn."""
    # Step 1: Validate enum values
    if "remote-type" in payload:
        value = payload["remote-type"]
        if value not in VALID_BODY_REMOTE_TYPE:
            return (
                False,
                f"Invalid value for 'remote-type'='{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_TYPE)}",
            )
    if "routing-type" in payload:
        value = payload["routing-type"]
        if value not in VALID_BODY_ROUTING_TYPE:
            return (
                False,
                f"Invalid value for 'routing-type'='{value}'. Must be one of: {', '.join(VALID_BODY_ROUTING_TYPE)}",
            )
    if "nat-traversal" in payload:
        value = payload["nat-traversal"]
        if value not in VALID_BODY_NAT_TRAVERSAL:
            return (
                False,
                f"Invalid value for 'nat-traversal'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT_TRAVERSAL)}",
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
    "endpoint": "system/sdn_vpn",
    "category": "cmdb",
    "api_path": "system/sdn-vpn",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure public cloud VPN service.",
    "total_fields": 19,
    "required_fields_count": 5,
    "fields_with_defaults_count": 18,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
