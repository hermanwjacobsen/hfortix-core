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
    "enable",
    "disable",
]
VALID_BODY_BLACKHOLE = [
    "enable",
    "disable",
]
VALID_BODY_DYNAMIC_GATEWAY = [
    "enable",
    "disable",
]
VALID_BODY_LINK_MONITOR_EXEMPT = [
    "enable",
    "disable",
]
VALID_BODY_BFD = [
    "enable",
    "disable",
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


def validate_router_static6_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new router/static6 object."""
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
    if "blackhole" in payload:
        is_valid, error = _validate_enum_field(
            "blackhole",
            payload["blackhole"],
            VALID_BODY_BLACKHOLE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "dynamic-gateway" in payload:
        is_valid, error = _validate_enum_field(
            "dynamic-gateway",
            payload["dynamic-gateway"],
            VALID_BODY_DYNAMIC_GATEWAY,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "link-monitor-exempt" in payload:
        is_valid, error = _validate_enum_field(
            "link-monitor-exempt",
            payload["link-monitor-exempt"],
            VALID_BODY_LINK_MONITOR_EXEMPT,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "bfd" in payload:
        is_valid, error = _validate_enum_field(
            "bfd",
            payload["bfd"],
            VALID_BODY_BFD,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_router_static6_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update router/static6."""
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
    if "blackhole" in payload:
        is_valid, error = _validate_enum_field(
            "blackhole",
            payload["blackhole"],
            VALID_BODY_BLACKHOLE,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "dynamic-gateway" in payload:
        is_valid, error = _validate_enum_field(
            "dynamic-gateway",
            payload["dynamic-gateway"],
            VALID_BODY_DYNAMIC_GATEWAY,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "link-monitor-exempt" in payload:
        is_valid, error = _validate_enum_field(
            "link-monitor-exempt",
            payload["link-monitor-exempt"],
            VALID_BODY_LINK_MONITOR_EXEMPT,
            FIELD_DESCRIPTIONS
        )
        if not is_valid:
            return (False, error)
    if "bfd" in payload:
        is_valid, error = _validate_enum_field(
            "bfd",
            payload["bfd"],
            VALID_BODY_BFD,
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
