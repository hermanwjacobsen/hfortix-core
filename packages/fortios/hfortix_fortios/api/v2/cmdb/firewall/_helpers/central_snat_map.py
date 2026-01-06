"""Validation helpers for firewall/central_snat_map - Auto-generated"""

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
    "srcintf",  # Source interface name from available interfaces.
    "dstintf",  # Destination interface name from available interfaces.
    "orig-addr",  # IPv4 Original address.
    "orig-addr6",  # IPv6 Original address.
    "dst-addr",  # IPv4 Destination address.
    "dst-addr6",  # IPv6 Destination address.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "policyid": 0,
    "uuid": "00000000-0000-0000-0000-000000000000",
    "status": "enable",
    "type": "ipv4",
    "protocol": 0,
    "orig-port": "",
    "nat": "enable",
    "nat46": "disable",
    "nat64": "disable",
    "port-preserve": "enable",
    "port-random": "disable",
    "nat-port": "",
    "dst-port": "",
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
    "policyid": "integer",  # Policy ID.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "status": "option",  # Enable/disable the active status of this policy.
    "type": "option",  # IPv4/IPv6 source NAT.
    "srcintf": "string",  # Source interface name from available interfaces.
    "dstintf": "string",  # Destination interface name from available interfaces.
    "orig-addr": "string",  # IPv4 Original address.
    "orig-addr6": "string",  # IPv6 Original address.
    "dst-addr": "string",  # IPv4 Destination address.
    "dst-addr6": "string",  # IPv6 Destination address.
    "protocol": "integer",  # Integer value for the protocol type (0 - 255).
    "orig-port": "user",  # Original TCP port (1 to 65535, 0 means any port).
    "nat": "option",  # Enable/disable source NAT.
    "nat46": "option",  # Enable/disable NAT46.
    "nat64": "option",  # Enable/disable NAT64.
    "nat-ippool": "string",  # Name of the IP pools to be used to translate addresses from 
    "nat-ippool6": "string",  # IPv6 pools to be used for source NAT.
    "port-preserve": "option",  # Enable/disable preservation of the original source port from
    "port-random": "option",  # Enable/disable random source port selection for source NAT.
    "nat-port": "user",  # Translated port or port range (1 to 65535, 0 means any port)
    "dst-port": "user",  # Destination port or port range (1 to 65535, 0 means any port
    "comments": "var-string",  # Comment.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "policyid": "Policy ID.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "status": "Enable/disable the active status of this policy.",
    "type": "IPv4/IPv6 source NAT.",
    "srcintf": "Source interface name from available interfaces.",
    "dstintf": "Destination interface name from available interfaces.",
    "orig-addr": "IPv4 Original address.",
    "orig-addr6": "IPv6 Original address.",
    "dst-addr": "IPv4 Destination address.",
    "dst-addr6": "IPv6 Destination address.",
    "protocol": "Integer value for the protocol type (0 - 255).",
    "orig-port": "Original TCP port (1 to 65535, 0 means any port).",
    "nat": "Enable/disable source NAT.",
    "nat46": "Enable/disable NAT46.",
    "nat64": "Enable/disable NAT64.",
    "nat-ippool": "Name of the IP pools to be used to translate addresses from available IP Pools.",
    "nat-ippool6": "IPv6 pools to be used for source NAT.",
    "port-preserve": "Enable/disable preservation of the original source port from source NAT if it has not been used.",
    "port-random": "Enable/disable random source port selection for source NAT.",
    "nat-port": "Translated port or port range (1 to 65535, 0 means any port).",
    "dst-port": "Destination port or port range (1 to 65535, 0 means any port).",
    "comments": "Comment.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "policyid": {"type": "integer", "min": 0, "max": 4294967295},
    "protocol": {"type": "integer", "min": 0, "max": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "srcintf": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 79,
        },
    },
    "dstintf": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "orig-addr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "orig-addr6": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "default": "",
            "max_length": 79,
        },
    },
    "dst-addr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dst-addr6": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "default": "",
            "max_length": 79,
        },
    },
    "nat-ippool": {
        "name": {
            "type": "string",
            "help": "IP pool name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "nat-ippool6": {
        "name": {
            "type": "string",
            "help": "IPv6 pool name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable this policy.
    "disable",  # Disable this policy.
]
VALID_BODY_TYPE = [
    "ipv4",  # Perform IPv4 source NAT.
    "ipv6",  # Perform IPv6 source NAT.
]
VALID_BODY_NAT = [
    "disable",  # Disable source NAT.
    "enable",  # Enable source NAT.
]
VALID_BODY_NAT46 = [
    "enable",  # Enable NAT46.
    "disable",  # Disable NAT46.
]
VALID_BODY_NAT64 = [
    "enable",  # Enable NAT64.
    "disable",  # Disable NAT64.
]
VALID_BODY_PORT_PRESERVE = [
    "enable",  # Use the original source port if it has not been used.
    "disable",  # Source NAT always changes the source port.
]
VALID_BODY_PORT_RANDOM = [
    "enable",  # Enable random source port selection for source NAT.
    "disable",  # Disable random source port selection for source NAT.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_central_snat_map_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/central_snat_map."""
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
    """Validate required fields for firewall/central_snat_map."""
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


def validate_firewall_central_snat_map_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/central_snat_map object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            desc = FIELD_DESCRIPTIONS.get("status", "")
            error_msg = f"Invalid value for 'status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STATUS)}"
            error_msg += f"\n  → Example: status='{{ VALID_BODY_STATUS[0] }}'"
            return (False, error_msg)
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
    if "nat" in payload:
        value = payload["nat"]
        if value not in VALID_BODY_NAT:
            desc = FIELD_DESCRIPTIONS.get("nat", "")
            error_msg = f"Invalid value for 'nat': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT)}"
            error_msg += f"\n  → Example: nat='{{ VALID_BODY_NAT[0] }}'"
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
    if "nat64" in payload:
        value = payload["nat64"]
        if value not in VALID_BODY_NAT64:
            desc = FIELD_DESCRIPTIONS.get("nat64", "")
            error_msg = f"Invalid value for 'nat64': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT64)}"
            error_msg += f"\n  → Example: nat64='{{ VALID_BODY_NAT64[0] }}'"
            return (False, error_msg)
    if "port-preserve" in payload:
        value = payload["port-preserve"]
        if value not in VALID_BODY_PORT_PRESERVE:
            desc = FIELD_DESCRIPTIONS.get("port-preserve", "")
            error_msg = f"Invalid value for 'port-preserve': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORT_PRESERVE)}"
            error_msg += f"\n  → Example: port-preserve='{{ VALID_BODY_PORT_PRESERVE[0] }}'"
            return (False, error_msg)
    if "port-random" in payload:
        value = payload["port-random"]
        if value not in VALID_BODY_PORT_RANDOM:
            desc = FIELD_DESCRIPTIONS.get("port-random", "")
            error_msg = f"Invalid value for 'port-random': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORT_RANDOM)}"
            error_msg += f"\n  → Example: port-random='{{ VALID_BODY_PORT_RANDOM[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_central_snat_map_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/central_snat_map."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "nat" in payload:
        value = payload["nat"]
        if value not in VALID_BODY_NAT:
            return (
                False,
                f"Invalid value for 'nat'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT)}",
            )
    if "nat46" in payload:
        value = payload["nat46"]
        if value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid value for 'nat46'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )
    if "nat64" in payload:
        value = payload["nat64"]
        if value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid value for 'nat64'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )
    if "port-preserve" in payload:
        value = payload["port-preserve"]
        if value not in VALID_BODY_PORT_PRESERVE:
            return (
                False,
                f"Invalid value for 'port-preserve'='{value}'. Must be one of: {', '.join(VALID_BODY_PORT_PRESERVE)}",
            )
    if "port-random" in payload:
        value = payload["port-random"]
        if value not in VALID_BODY_PORT_RANDOM:
            return (
                False,
                f"Invalid value for 'port-random'='{value}'. Must be one of: {', '.join(VALID_BODY_PORT_RANDOM)}",
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
    "endpoint": "firewall/central_snat_map",
    "category": "cmdb",
    "api_path": "firewall/central-snat-map",
    "mkey": "policyid",
    "mkey_type": "integer",
    "help": "Configure IPv4 and IPv6 central SNAT policies.",
    "total_fields": 22,
    "required_fields_count": 6,
    "fields_with_defaults_count": 13,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
