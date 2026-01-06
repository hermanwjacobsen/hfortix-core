"""Validation helpers for router/static6 - Auto-generated"""

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
    "device",  # Gateway out interface or tunnel.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "seq-num": 0,
    "status": "enable",
    "dst": "::/0",
    "gateway": "::",
    "device": "",
    "devindex": 0,
    "distance": 10,
    "weight": 0,
    "priority": 1024,
    "blackhole": "disable",
    "dynamic-gateway": "disable",
    "dstaddr": "",
    "link-monitor-exempt": "disable",
    "vrf": "unspecified",
    "bfd": "disable",
    "tag": 0,
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
    "seq-num": "integer",  # Sequence number.
    "status": "option",  # Enable/disable this static route.
    "dst": "ipv6-network",  # Destination IPv6 prefix.
    "gateway": "ipv6-address",  # IPv6 address of the gateway.
    "device": "string",  # Gateway out interface or tunnel.
    "devindex": "integer",  # Device index (0 - 4294967295).
    "distance": "integer",  # Administrative distance (1 - 255).
    "weight": "integer",  # Administrative weight (0 - 255).
    "priority": "integer",  # Administrative priority (1 - 65535).
    "comment": "var-string",  # Optional comments.
    "blackhole": "option",  # Enable/disable black hole.
    "dynamic-gateway": "option",  # Enable use of dynamic gateway retrieved from Router Advertis
    "sdwan-zone": "string",  # Choose SD-WAN Zone.
    "dstaddr": "string",  # Name of firewall address or address group.
    "link-monitor-exempt": "option",  # Enable/disable withdrawal of this static route when link mon
    "vrf": "integer",  # Virtual Routing Forwarding ID.
    "bfd": "option",  # Enable/disable Bidirectional Forwarding Detection (BFD).
    "tag": "integer",  # Route tag.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "seq-num": "Sequence number.",
    "status": "Enable/disable this static route.",
    "dst": "Destination IPv6 prefix.",
    "gateway": "IPv6 address of the gateway.",
    "device": "Gateway out interface or tunnel.",
    "devindex": "Device index (0 - 4294967295).",
    "distance": "Administrative distance (1 - 255).",
    "weight": "Administrative weight (0 - 255).",
    "priority": "Administrative priority (1 - 65535).",
    "comment": "Optional comments.",
    "blackhole": "Enable/disable black hole.",
    "dynamic-gateway": "Enable use of dynamic gateway retrieved from Router Advertisement (RA).",
    "sdwan-zone": "Choose SD-WAN Zone.",
    "dstaddr": "Name of firewall address or address group.",
    "link-monitor-exempt": "Enable/disable withdrawal of this static route when link monitor or health check is down.",
    "vrf": "Virtual Routing Forwarding ID.",
    "bfd": "Enable/disable Bidirectional Forwarding Detection (BFD).",
    "tag": "Route tag.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "seq-num": {"type": "integer", "min": 0, "max": 4294967295},
    "device": {"type": "string", "max_length": 35},
    "devindex": {"type": "integer", "min": 0, "max": 4294967295},
    "distance": {"type": "integer", "min": 1, "max": 255},
    "weight": {"type": "integer", "min": 0, "max": 255},
    "priority": {"type": "integer", "min": 1, "max": 65535},
    "dstaddr": {"type": "string", "max_length": 79},
    "vrf": {"type": "integer", "min": 0, "max": 511},
    "tag": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "sdwan-zone": {
        "name": {
            "type": "string",
            "help": "SD-WAN zone name.",
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable static route.
    "disable",  # Disable static route.
]
VALID_BODY_BLACKHOLE = [
    "enable",  # Enable black hole.
    "disable",  # Disable black hole.
]
VALID_BODY_DYNAMIC_GATEWAY = [
    "enable",  # Enable dynamic gateway.
    "disable",  # Disable dynamic gateway.
]
VALID_BODY_LINK_MONITOR_EXEMPT = [
    "enable",  # Keep this static route when link monitor or health check is down.
    "disable",  # Withdraw this static route when link monitor or health check is down. (default)
]
VALID_BODY_BFD = [
    "enable",  # Enable Bidirectional Forwarding Detection (BFD).
    "disable",  # Disable Bidirectional Forwarding Detection (BFD).
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_router_static6_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for router/static6."""
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
    """Validate required fields for router/static6."""
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


def validate_router_static6_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new router/static6 object."""
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
    if "blackhole" in payload:
        value = payload["blackhole"]
        if value not in VALID_BODY_BLACKHOLE:
            desc = FIELD_DESCRIPTIONS.get("blackhole", "")
            error_msg = f"Invalid value for 'blackhole': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BLACKHOLE)}"
            error_msg += f"\n  → Example: blackhole='{{ VALID_BODY_BLACKHOLE[0] }}'"
            return (False, error_msg)
    if "dynamic-gateway" in payload:
        value = payload["dynamic-gateway"]
        if value not in VALID_BODY_DYNAMIC_GATEWAY:
            desc = FIELD_DESCRIPTIONS.get("dynamic-gateway", "")
            error_msg = f"Invalid value for 'dynamic-gateway': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DYNAMIC_GATEWAY)}"
            error_msg += f"\n  → Example: dynamic-gateway='{{ VALID_BODY_DYNAMIC_GATEWAY[0] }}'"
            return (False, error_msg)
    if "link-monitor-exempt" in payload:
        value = payload["link-monitor-exempt"]
        if value not in VALID_BODY_LINK_MONITOR_EXEMPT:
            desc = FIELD_DESCRIPTIONS.get("link-monitor-exempt", "")
            error_msg = f"Invalid value for 'link-monitor-exempt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LINK_MONITOR_EXEMPT)}"
            error_msg += f"\n  → Example: link-monitor-exempt='{{ VALID_BODY_LINK_MONITOR_EXEMPT[0] }}'"
            return (False, error_msg)
    if "bfd" in payload:
        value = payload["bfd"]
        if value not in VALID_BODY_BFD:
            desc = FIELD_DESCRIPTIONS.get("bfd", "")
            error_msg = f"Invalid value for 'bfd': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BFD)}"
            error_msg += f"\n  → Example: bfd='{{ VALID_BODY_BFD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_router_static6_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update router/static6."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "blackhole" in payload:
        value = payload["blackhole"]
        if value not in VALID_BODY_BLACKHOLE:
            return (
                False,
                f"Invalid value for 'blackhole'='{value}'. Must be one of: {', '.join(VALID_BODY_BLACKHOLE)}",
            )
    if "dynamic-gateway" in payload:
        value = payload["dynamic-gateway"]
        if value not in VALID_BODY_DYNAMIC_GATEWAY:
            return (
                False,
                f"Invalid value for 'dynamic-gateway'='{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_GATEWAY)}",
            )
    if "link-monitor-exempt" in payload:
        value = payload["link-monitor-exempt"]
        if value not in VALID_BODY_LINK_MONITOR_EXEMPT:
            return (
                False,
                f"Invalid value for 'link-monitor-exempt'='{value}'. Must be one of: {', '.join(VALID_BODY_LINK_MONITOR_EXEMPT)}",
            )
    if "bfd" in payload:
        value = payload["bfd"]
        if value not in VALID_BODY_BFD:
            return (
                False,
                f"Invalid value for 'bfd'='{value}'. Must be one of: {', '.join(VALID_BODY_BFD)}",
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
    "endpoint": "router/static6",
    "category": "cmdb",
    "api_path": "router/static6",
    "mkey": "seq-num",
    "mkey_type": "integer",
    "help": "Configure IPv6 static routing tables.",
    "total_fields": 18,
    "required_fields_count": 1,
    "fields_with_defaults_count": 16,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
