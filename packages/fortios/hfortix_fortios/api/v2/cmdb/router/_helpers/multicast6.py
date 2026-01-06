"""Validation helpers for router/multicast6 - Auto-generated"""

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
    "multicast-routing": "disable",
    "multicast-pmtu": "disable",
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
    "multicast-routing": "option",  # Enable/disable IPv6 multicast routing.
    "multicast-pmtu": "option",  # Enable/disable PMTU for IPv6 multicast.
    "interface": "string",  # Protocol Independent Multicast (PIM) interfaces.
    "pim-sm-global": "string",  # PIM sparse-mode global settings.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "multicast-routing": "Enable/disable IPv6 multicast routing.",
    "multicast-pmtu": "Enable/disable PMTU for IPv6 multicast.",
    "interface": "Protocol Independent Multicast (PIM) interfaces.",
    "pim-sm-global": "PIM sparse-mode global settings.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "interface": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 15,
        },
        "hello-interval": {
            "type": "integer",
            "help": "Interval between sending PIM hello messages in seconds (1 - 65535, default = 30).",
            "default": 30,
            "min_value": 1,
            "max_value": 65535,
        },
        "hello-holdtime": {
            "type": "integer",
            "help": "Time before old neighbor information expires in seconds (1 - 65535, default = 105).",
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
    },
    "pim-sm-global": {
        "register-rate-limit": {
            "type": "integer",
            "help": "Limit of packets/sec per source registered through this RP (0 means unlimited).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "pim-use-sdwan": {
            "type": "option",
            "help": "Enable/disable use of SDWAN when checking RPF neighbor and sending of REG packet.",
            "default": "disable",
            "options": [{"help": "Enable use of SDWAN when checking RPF neighbor and sending of REG packet.", "label": "Enable", "name": "enable"}, {"help": "Disable use of SDWAN when checking RPF neighbor and sending of REG packet.", "label": "Disable", "name": "disable"}],
        },
        "rp-address": {
            "type": "string",
            "help": "Statically configured RP addresses.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_MULTICAST_ROUTING = [
    "enable",  # Enable IPv6 multicast routing.
    "disable",  # Disable IPv6 multicast routing.
]
VALID_BODY_MULTICAST_PMTU = [
    "enable",  # Enable PMTU for IPv6 multicast.
    "disable",  # Disable PMTU for IPv6 multicast.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_router_multicast6_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for router/multicast6."""
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
    """Validate required fields for router/multicast6."""
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


def validate_router_multicast6_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new router/multicast6 object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "multicast-routing" in payload:
        value = payload["multicast-routing"]
        if value not in VALID_BODY_MULTICAST_ROUTING:
            desc = FIELD_DESCRIPTIONS.get("multicast-routing", "")
            error_msg = f"Invalid value for 'multicast-routing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTICAST_ROUTING)}"
            error_msg += f"\n  → Example: multicast-routing='{{ VALID_BODY_MULTICAST_ROUTING[0] }}'"
            return (False, error_msg)
    if "multicast-pmtu" in payload:
        value = payload["multicast-pmtu"]
        if value not in VALID_BODY_MULTICAST_PMTU:
            desc = FIELD_DESCRIPTIONS.get("multicast-pmtu", "")
            error_msg = f"Invalid value for 'multicast-pmtu': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTICAST_PMTU)}"
            error_msg += f"\n  → Example: multicast-pmtu='{{ VALID_BODY_MULTICAST_PMTU[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_router_multicast6_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update router/multicast6."""
    # Step 1: Validate enum values
    if "multicast-routing" in payload:
        value = payload["multicast-routing"]
        if value not in VALID_BODY_MULTICAST_ROUTING:
            return (
                False,
                f"Invalid value for 'multicast-routing'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_ROUTING)}",
            )
    if "multicast-pmtu" in payload:
        value = payload["multicast-pmtu"]
        if value not in VALID_BODY_MULTICAST_PMTU:
            return (
                False,
                f"Invalid value for 'multicast-pmtu'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_PMTU)}",
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
    "endpoint": "router/multicast6",
    "category": "cmdb",
    "api_path": "router/multicast6",
    "help": "Configure IPv6 multicast.",
    "total_fields": 4,
    "required_fields_count": 0,
    "fields_with_defaults_count": 2,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
