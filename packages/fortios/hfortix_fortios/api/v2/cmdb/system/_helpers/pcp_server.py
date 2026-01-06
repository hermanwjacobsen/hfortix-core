"""Validation helpers for system/pcp_server - Auto-generated"""

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
    "status": "option",  # Enable/disable PCP server.
    "pools": "string",  # Configure PCP pools.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable PCP server.",
    "pools": "Configure PCP pools.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "pools": {
        "name": {
            "type": "string",
            "help": "PCP pool name.",
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
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "client-subnet": {
            "type": "string",
            "help": "Subnets from which PCP requests are accepted.",
            "required": True,
        },
        "ext-intf": {
            "type": "string",
            "help": "External interface name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "arp-reply": {
            "type": "option",
            "help": "Enable to respond to ARP requests for external IP (default = enable).",
            "default": "enable",
            "options": [{"help": "Disable ARP reply.", "label": "Disable", "name": "disable"}, {"help": "Enable ARP reply.", "label": "Enable", "name": "enable"}],
        },
        "extip": {
            "type": "user",
            "help": "IP address or address range on the external interface that you want to map to an address on the internal network.",
            "required": True,
            "default": "",
        },
        "extport": {
            "type": "user",
            "help": "Incoming port number range that you want to map to a port number on the internal network.",
            "required": True,
            "default": "",
        },
        "minimal-lifetime": {
            "type": "integer",
            "help": "Minimal lifetime of a PCP mapping in seconds (60 - 300, default = 120).",
            "default": 120,
            "min_value": 60,
            "max_value": 300,
        },
        "maximal-lifetime": {
            "type": "integer",
            "help": "Maximal lifetime of a PCP mapping in seconds (3600 - 604800, default = 86400).",
            "default": 86400,
            "min_value": 3600,
            "max_value": 604800,
        },
        "client-mapping-limit": {
            "type": "integer",
            "help": "Mapping limit per client (0 - 65535, default = 0, 0 = unlimited).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "mapping-filter-limit": {
            "type": "integer",
            "help": "Filter limit per mapping (0 - 5, default = 1).",
            "default": 1,
            "min_value": 0,
            "max_value": 5,
        },
        "allow-opcode": {
            "type": "option",
            "help": "Allowed PCP opcode.",
            "default": "map peer announce",
            "options": [{"help": "Allow opcode MAP.", "label": "Map", "name": "map"}, {"help": "Allow opcode PEER.", "label": "Peer", "name": "peer"}, {"help": "Allow opcode ANNOUNCE.", "label": "Announce", "name": "announce"}],
        },
        "third-party": {
            "type": "option",
            "help": "Allow/disallow third party option.",
            "default": "disallow",
            "options": [{"help": "Allow third party option.", "label": "Allow", "name": "allow"}, {"help": "Disallow third party opiton.", "label": "Disallow", "name": "disallow"}],
        },
        "third-party-subnet": {
            "type": "string",
            "help": "Subnets from which third party requests are accepted.",
        },
        "multicast-announcement": {
            "type": "option",
            "help": "Enable/disable multicast announcements.",
            "default": "enable",
            "options": [{"help": "Enable multicast announcements.", "label": "Enable", "name": "enable"}, {"help": "Disable multicast announcements.", "label": "Disable", "name": "disable"}],
        },
        "announcement-count": {
            "type": "integer",
            "help": "Number of multicast announcements.",
            "default": 3,
            "min_value": 3,
            "max_value": 10,
        },
        "intl-intf": {
            "type": "string",
            "help": "Internal interface name.",
            "required": True,
        },
        "recycle-delay": {
            "type": "integer",
            "help": "Minimum delay (in seconds) the PCP Server will wait before recycling mappings that have expired (0 - 3600, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 3600,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable PCP Server.
    "disable",  # Disable PCP Server.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_pcp_server_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/pcp_server."""
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
    """Validate required fields for system/pcp_server."""
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


def validate_system_pcp_server_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/pcp_server object."""
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_pcp_server_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/pcp_server."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
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
    "endpoint": "system/pcp_server",
    "category": "cmdb",
    "api_path": "system/pcp-server",
    "help": "Configure PCP server information.",
    "total_fields": 2,
    "required_fields_count": 0,
    "fields_with_defaults_count": 1,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
