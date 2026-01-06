"""Validation helpers for system/vxlan - Auto-generated"""

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
    "interface",  # Outgoing interface for VXLAN encapsulated traffic.
    "remote-ip6",  # IPv6 IP address of the VXLAN interface on the device at the remote end of the VXLAN.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "interface": "",
    "vni": 0,
    "ip-version": "ipv4-unicast",
    "local-ip": "0.0.0.0",
    "local-ip6": "::",
    "dstport": 4789,
    "multicast-ttl": 0,
    "evpn-id": 0,
    "learn-from-traffic": "disable",
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
    "name": "string",  # VXLAN device or interface name. Must be a unique interface n
    "interface": "string",  # Outgoing interface for VXLAN encapsulated traffic.
    "vni": "integer",  # VXLAN network ID.
    "ip-version": "option",  # IP version to use for the VXLAN interface and so for communi
    "remote-ip": "string",  # IPv4 address of the VXLAN interface on the device at the rem
    "local-ip": "ipv4-address",  # IPv4 address to use as the source address for egress VXLAN p
    "remote-ip6": "string",  # IPv6 IP address of the VXLAN interface on the device at the 
    "local-ip6": "ipv6-address",  # IPv6 address to use as the source address for egress VXLAN p
    "dstport": "integer",  # VXLAN destination port (1 - 65535, default = 4789).
    "multicast-ttl": "integer",  # VXLAN multicast TTL (1-255, default = 0).
    "evpn-id": "integer",  # EVPN instance.
    "learn-from-traffic": "option",  # Enable/disable VXLAN MAC learning from traffic.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "VXLAN device or interface name. Must be a unique interface name.",
    "interface": "Outgoing interface for VXLAN encapsulated traffic.",
    "vni": "VXLAN network ID.",
    "ip-version": "IP version to use for the VXLAN interface and so for communication over the VXLAN. IPv4 or IPv6 unicast or multicast.",
    "remote-ip": "IPv4 address of the VXLAN interface on the device at the remote end of the VXLAN.",
    "local-ip": "IPv4 address to use as the source address for egress VXLAN packets.",
    "remote-ip6": "IPv6 IP address of the VXLAN interface on the device at the remote end of the VXLAN.",
    "local-ip6": "IPv6 address to use as the source address for egress VXLAN packets.",
    "dstport": "VXLAN destination port (1 - 65535, default = 4789).",
    "multicast-ttl": "VXLAN multicast TTL (1-255, default = 0).",
    "evpn-id": "EVPN instance.",
    "learn-from-traffic": "Enable/disable VXLAN MAC learning from traffic.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 15},
    "interface": {"type": "string", "max_length": 15},
    "vni": {"type": "integer", "min": 1, "max": 16777215},
    "dstport": {"type": "integer", "min": 1, "max": 65535},
    "multicast-ttl": {"type": "integer", "min": 1, "max": 255},
    "evpn-id": {"type": "integer", "min": 1, "max": 65535},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "remote-ip": {
        "ip": {
            "type": "string",
            "help": "IPv4 address.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
    },
    "remote-ip6": {
        "ip6": {
            "type": "string",
            "help": "IPv6 address.",
            "required": True,
            "default": "",
            "max_length": 45,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_IP_VERSION = [
    "ipv4-unicast",  # Use IPv4 unicast addressing over the VXLAN.
    "ipv6-unicast",  # Use IPv6 unicast addressing over the VXLAN.
    "ipv4-multicast",  # Use IPv4 multicast addressing over the VXLAN.
    "ipv6-multicast",  # Use IPv6 multicast addressing over the VXLAN.
]
VALID_BODY_LEARN_FROM_TRAFFIC = [
    "enable",  # Enable VXLAN MAC learning from traffic.
    "disable",  # Disable VXLAN MAC learning from traffic.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_vxlan_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/vxlan."""
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
    """Validate required fields for system/vxlan."""
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


def validate_system_vxlan_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/vxlan object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "ip-version" in payload:
        value = payload["ip-version"]
        if value not in VALID_BODY_IP_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ip-version", "")
            error_msg = f"Invalid value for 'ip-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_VERSION)}"
            error_msg += f"\n  → Example: ip-version='{{ VALID_BODY_IP_VERSION[0] }}'"
            return (False, error_msg)
    if "learn-from-traffic" in payload:
        value = payload["learn-from-traffic"]
        if value not in VALID_BODY_LEARN_FROM_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("learn-from-traffic", "")
            error_msg = f"Invalid value for 'learn-from-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LEARN_FROM_TRAFFIC)}"
            error_msg += f"\n  → Example: learn-from-traffic='{{ VALID_BODY_LEARN_FROM_TRAFFIC[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_vxlan_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/vxlan."""
    # Step 1: Validate enum values
    if "ip-version" in payload:
        value = payload["ip-version"]
        if value not in VALID_BODY_IP_VERSION:
            return (
                False,
                f"Invalid value for 'ip-version'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_VERSION)}",
            )
    if "learn-from-traffic" in payload:
        value = payload["learn-from-traffic"]
        if value not in VALID_BODY_LEARN_FROM_TRAFFIC:
            return (
                False,
                f"Invalid value for 'learn-from-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LEARN_FROM_TRAFFIC)}",
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
    "endpoint": "system/vxlan",
    "category": "cmdb",
    "api_path": "system/vxlan",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure VXLAN devices.",
    "total_fields": 12,
    "required_fields_count": 2,
    "fields_with_defaults_count": 10,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
