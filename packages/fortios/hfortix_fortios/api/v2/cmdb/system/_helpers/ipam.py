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
            "options": [{"help": "Match any interface role.", "label": "Any", "name": "any"}, {"help": "Match interface role lan.", "label": "Lan", "name": "lan"}, {"help": "Match interface role wan.", "label": "Wan", "name": "wan"}, {"help": "Match interface role dmz.", "label": "Dmz", "name": "dmz"}, {"help": "Match interface role undefined.", "label": "Undefined", "name": "undefined"}],
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
            "options": [{"help": "Enable DHCP server on matched IPAM interface.", "label": "Enable", "name": "enable"}, {"help": "Disable DHCP server on matched IPAM interface.", "label": "Disable", "name": "disable"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable integration with IP address management services.
    "disable",  # Disable integration with IP address management services.
]
VALID_BODY_SERVER_TYPE = [
    "fabric-root",  # Use the IPAM server running on the Security Fabric root.
]
VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION = [
    "disable",  # Disable automatic conflict resolution.
    "enable",  # Enable automatic conflict resolution.
]
VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH = [
    "disable",  # Disable requiring subnet sizes to match.
    "enable",  # Enable requiring subnet sizes to match.
]
VALID_BODY_MANAGE_LAN_ADDRESSES = [
    "disable",  # Disable LAN interface address management by default.
    "enable",  # Enable LAN interface address management by default.
]
VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES = [
    "disable",  # Disable FortiExtender LAN extension interface address management by default.
    "enable",  # Enable FortiExtender LAN extension interface address management by default.
]
VALID_BODY_MANAGE_SSID_ADDRESSES = [
    "disable",  # Disable FortiAP SSID address management by default.
    "enable",  # Enable FortiAP SSID address management by default.
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
    """Validate required fields for system/ipam."""
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


def validate_system_ipam_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/ipam object."""
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
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            desc = FIELD_DESCRIPTIONS.get("server-type", "")
            error_msg = f"Invalid value for 'server-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_TYPE)}"
            error_msg += f"\n  → Example: server-type='{{ VALID_BODY_SERVER_TYPE[0] }}'"
            return (False, error_msg)
    if "automatic-conflict-resolution" in payload:
        value = payload["automatic-conflict-resolution"]
        if value not in VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION:
            desc = FIELD_DESCRIPTIONS.get("automatic-conflict-resolution", "")
            error_msg = f"Invalid value for 'automatic-conflict-resolution': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION)}"
            error_msg += f"\n  → Example: automatic-conflict-resolution='{{ VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION[0] }}'"
            return (False, error_msg)
    if "require-subnet-size-match" in payload:
        value = payload["require-subnet-size-match"]
        if value not in VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH:
            desc = FIELD_DESCRIPTIONS.get("require-subnet-size-match", "")
            error_msg = f"Invalid value for 'require-subnet-size-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH)}"
            error_msg += f"\n  → Example: require-subnet-size-match='{{ VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH[0] }}'"
            return (False, error_msg)
    if "manage-lan-addresses" in payload:
        value = payload["manage-lan-addresses"]
        if value not in VALID_BODY_MANAGE_LAN_ADDRESSES:
            desc = FIELD_DESCRIPTIONS.get("manage-lan-addresses", "")
            error_msg = f"Invalid value for 'manage-lan-addresses': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MANAGE_LAN_ADDRESSES)}"
            error_msg += f"\n  → Example: manage-lan-addresses='{{ VALID_BODY_MANAGE_LAN_ADDRESSES[0] }}'"
            return (False, error_msg)
    if "manage-lan-extension-addresses" in payload:
        value = payload["manage-lan-extension-addresses"]
        if value not in VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES:
            desc = FIELD_DESCRIPTIONS.get("manage-lan-extension-addresses", "")
            error_msg = f"Invalid value for 'manage-lan-extension-addresses': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES)}"
            error_msg += f"\n  → Example: manage-lan-extension-addresses='{{ VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES[0] }}'"
            return (False, error_msg)
    if "manage-ssid-addresses" in payload:
        value = payload["manage-ssid-addresses"]
        if value not in VALID_BODY_MANAGE_SSID_ADDRESSES:
            desc = FIELD_DESCRIPTIONS.get("manage-ssid-addresses", "")
            error_msg = f"Invalid value for 'manage-ssid-addresses': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MANAGE_SSID_ADDRESSES)}"
            error_msg += f"\n  → Example: manage-ssid-addresses='{{ VALID_BODY_MANAGE_SSID_ADDRESSES[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_ipam_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/ipam."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "server-type" in payload:
        value = payload["server-type"]
        if value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid value for 'server-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )
    if "automatic-conflict-resolution" in payload:
        value = payload["automatic-conflict-resolution"]
        if value not in VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION:
            return (
                False,
                f"Invalid value for 'automatic-conflict-resolution'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTOMATIC_CONFLICT_RESOLUTION)}",
            )
    if "require-subnet-size-match" in payload:
        value = payload["require-subnet-size-match"]
        if value not in VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH:
            return (
                False,
                f"Invalid value for 'require-subnet-size-match'='{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_SUBNET_SIZE_MATCH)}",
            )
    if "manage-lan-addresses" in payload:
        value = payload["manage-lan-addresses"]
        if value not in VALID_BODY_MANAGE_LAN_ADDRESSES:
            return (
                False,
                f"Invalid value for 'manage-lan-addresses'='{value}'. Must be one of: {', '.join(VALID_BODY_MANAGE_LAN_ADDRESSES)}",
            )
    if "manage-lan-extension-addresses" in payload:
        value = payload["manage-lan-extension-addresses"]
        if value not in VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES:
            return (
                False,
                f"Invalid value for 'manage-lan-extension-addresses'='{value}'. Must be one of: {', '.join(VALID_BODY_MANAGE_LAN_EXTENSION_ADDRESSES)}",
            )
    if "manage-ssid-addresses" in payload:
        value = payload["manage-ssid-addresses"]
        if value not in VALID_BODY_MANAGE_SSID_ADDRESSES:
            return (
                False,
                f"Invalid value for 'manage-ssid-addresses'='{value}'. Must be one of: {', '.join(VALID_BODY_MANAGE_SSID_ADDRESSES)}",
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
