"""Validation helpers for system/ipam - Auto-generated"""

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

# Import central validation functions (avoid duplication across 1,062 files)
from hfortix_fortios._helpers.validation import (
    validate_required_fields as _validate_required_fields,
    validate_enum_field as _validate_enum_field,
    validate_query_parameter as _validate_query_parameter,
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
    "status": "disable",
    "server-type": "fabric-root",
    "automatic-conflict-resolution": "disable",
    "require-subnet-size-match": "enable",
    "manage-lan-addresses": "enable",
    "manage-lan-extension-addresses": "enable",
    "manage-ssid-addresses": "enable",
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
    "status": "option",  # Enable/disable IP address management services.
    "server-type": "option",  # Configure the type of IPAM server to use.
    "automatic-conflict-resolution": "option",  # Enable/disable automatic conflict resolution.
    "require-subnet-size-match": "option",  # Enable/disable reassignment of subnets to make requested and
    "manage-lan-addresses": "option",  # Enable/disable default management of LAN interface addresses
    "manage-lan-extension-addresses": "option",  # Enable/disable default management of FortiExtender LAN exten
    "manage-ssid-addresses": "option",  # Enable/disable default management of FortiAP SSID addresses.
    "pools": "string",  # Configure IPAM pools.
    "rules": "string",  # Configure IPAM allocation rules.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable IP address management services.",
    "server-type": "Configure the type of IPAM server to use.",
    "automatic-conflict-resolution": "Enable/disable automatic conflict resolution.",
    "require-subnet-size-match": "Enable/disable reassignment of subnets to make requested and actual sizes match.",
    "manage-lan-addresses": "Enable/disable default management of LAN interface addresses.",
    "manage-lan-extension-addresses": "Enable/disable default management of FortiExtender LAN extension interface addresses.",
    "manage-ssid-addresses": "Enable/disable default management of FortiAP SSID addresses.",
    "pools": "Configure IPAM pools.",
    "rules": "Configure IPAM allocation rules.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "pools": {
        "name": {
            "type": "string",
            "help": "IPAM pool name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
        "description": {
            "type": "string",
            "help": "Description.",
            "default": "",
            "max_length": 127,
        },
        "subnet": {
            "type": "ipv4-classnet",
            "help": "Configure IPAM pool subnet, Class A - Class B subnet.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "exclude": {
            "type": "string",
            "help": "Configure pool exclude subnets.",
        },
    },
    "rules": {
        "name": {
            "type": "string",
            "help": "IPAM rule name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
        "description": {
            "type": "string",
            "help": "Description.",
            "default": "",
            "max_length": 127,
        },
        "device": {
            "type": "string",
            "help": "Configure serial number or wildcard of FortiGate to match.",
            "required": True,
        },
        "interface": {
            "type": "string",
            "help": "Configure name or wildcard of interface to match.",
            "required": True,
        },
        "role": {
            "type": "option",
            "help": "Configure role of interface to match.",
            "default": "any",
            "options": ["any", "lan", "wan", "dmz", "undefined"],
        },
        "pool": {
            "type": "string",
            "help": "Configure name of IPAM pool to use.",
            "required": True,
        },
        "dhcp": {
            "type": "option",
            "help": "Enable/disable DHCP server for matching IPAM interfaces.",
            "default": "disable",
            "options": ["enable", "disable"],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_SERVER_TYPE = [
    "fabric-root",
]
VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION = [
    "disable",
    "enable",
]
VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH = [
    "disable",
    "enable",
]
VALID_BODY_MANAGE_LAN_ADDRESSES = [
    "disable",
    "enable",
]
VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES = [
    "disable",
    "enable",
]
VALID_BODY_MANAGE_SSID_ADDRESSES = [
    "disable",
    "enable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_ipam_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/ipam."""
    # Validate query parameters using central function
    if "action" in params:
        is_valid, error = _validate_query_parameter(
            "action",
            params.get("action"),
            VALID_QUERY_ACTION
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_system_ipam_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/ipam object."""
    # Step 1: Validate required fields using central function
    is_valid, error = _validate_required_fields(
        payload,
        REQUIRED_FIELDS,
        FIELD_DESCRIPTIONS
    )
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values using central function
    if "status" in payload:
        is_valid, error = _validate_enum_field(
            "status",
            payload["status"],
            VALID_BODY_STATUS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "server-type" in payload:
        is_valid, error = _validate_enum_field(
            "server-type",
            payload["server-type"],
            VALID_BODY_SERVER_TYPE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "automatic-conflict-resolution" in payload:
        is_valid, error = _validate_enum_field(
            "automatic-conflict-resolution",
            payload["automatic-conflict-resolution"],
            VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "require-subnet-size-match" in payload:
        is_valid, error = _validate_enum_field(
            "require-subnet-size-match",
            payload["require-subnet-size-match"],
            VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "manage-lan-addresses" in payload:
        is_valid, error = _validate_enum_field(
            "manage-lan-addresses",
            payload["manage-lan-addresses"],
            VALID_BODY_MANAGE_LAN_ADDRESSES,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "manage-lan-extension-addresses" in payload:
        is_valid, error = _validate_enum_field(
            "manage-lan-extension-addresses",
            payload["manage-lan-extension-addresses"],
            VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "manage-ssid-addresses" in payload:
        is_valid, error = _validate_enum_field(
            "manage-ssid-addresses",
            payload["manage-ssid-addresses"],
            VALID_BODY_MANAGE_SSID_ADDRESSES,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_ipam_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/ipam."""
    # Validate enum values using central function
    if "status" in payload:
        is_valid, error = _validate_enum_field(
            "status",
            payload["status"],
            VALID_BODY_STATUS,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "server-type" in payload:
        is_valid, error = _validate_enum_field(
            "server-type",
            payload["server-type"],
            VALID_BODY_SERVER_TYPE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "automatic-conflict-resolution" in payload:
        is_valid, error = _validate_enum_field(
            "automatic-conflict-resolution",
            payload["automatic-conflict-resolution"],
            VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "require-subnet-size-match" in payload:
        is_valid, error = _validate_enum_field(
            "require-subnet-size-match",
            payload["require-subnet-size-match"],
            VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "manage-lan-addresses" in payload:
        is_valid, error = _validate_enum_field(
            "manage-lan-addresses",
            payload["manage-lan-addresses"],
            VALID_BODY_MANAGE_LAN_ADDRESSES,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "manage-lan-extension-addresses" in payload:
        is_valid, error = _validate_enum_field(
            "manage-lan-extension-addresses",
            payload["manage-lan-extension-addresses"],
            VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "manage-ssid-addresses" in payload:
        is_valid, error = _validate_enum_field(
            "manage-ssid-addresses",
            payload["manage-ssid-addresses"],
            VALID_BODY_MANAGE_SSID_ADDRESSES,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

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
    "endpoint": "system/ipam",
    "category": "cmdb",
    "api_path": "system/ipam",
    "help": "Configure IP address management services.",
    "total_fields": 9,
    "required_fields_count": 0,
    "fields_with_defaults_count": 7,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
