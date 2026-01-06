"""Validation helpers for firewall/shaper/per_ip_shaper - Auto-generated"""

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
    "name": "",
    "max-bandwidth": 0,
    "bandwidth-unit": "kbps",
    "max-concurrent-session": 0,
    "max-concurrent-tcp-session": 0,
    "max-concurrent-udp-session": 0,
    "diffserv-forward": "disable",
    "diffserv-reverse": "disable",
    "diffservcode-forward": "",
    "diffservcode-rev": "",
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
    "name": "string",  # Traffic shaper name.
    "max-bandwidth": "integer",  # Upper bandwidth limit enforced by this shaper (0 - 80000000)
    "bandwidth-unit": "option",  # Unit of measurement for maximum bandwidth for this shaper (K
    "max-concurrent-session": "integer",  # Maximum number of concurrent sessions allowed by this shaper
    "max-concurrent-tcp-session": "integer",  # Maximum number of concurrent TCP sessions allowed by this sh
    "max-concurrent-udp-session": "integer",  # Maximum number of concurrent UDP sessions allowed by this sh
    "diffserv-forward": "option",  # Enable/disable changing the Forward (original) DiffServ sett
    "diffserv-reverse": "option",  # Enable/disable changing the Reverse (reply) DiffServ setting
    "diffservcode-forward": "user",  # Forward (original) DiffServ setting to be applied to traffic
    "diffservcode-rev": "user",  # Reverse (reply) DiffServ setting to be applied to traffic ac
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Traffic shaper name.",
    "max-bandwidth": "Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit. Units depend on the bandwidth-unit setting.",
    "bandwidth-unit": "Unit of measurement for maximum bandwidth for this shaper (Kbps, Mbps or Gbps).",
    "max-concurrent-session": "Maximum number of concurrent sessions allowed by this shaper (0 - 2097000). 0 means no limit.",
    "max-concurrent-tcp-session": "Maximum number of concurrent TCP sessions allowed by this shaper (0 - 2097000). 0 means no limit.",
    "max-concurrent-udp-session": "Maximum number of concurrent UDP sessions allowed by this shaper (0 - 2097000). 0 means no limit.",
    "diffserv-forward": "Enable/disable changing the Forward (original) DiffServ setting applied to traffic accepted by this shaper.",
    "diffserv-reverse": "Enable/disable changing the Reverse (reply) DiffServ setting applied to traffic accepted by this shaper.",
    "diffservcode-forward": "Forward (original) DiffServ setting to be applied to traffic accepted by this shaper.",
    "diffservcode-rev": "Reverse (reply) DiffServ setting to be applied to traffic accepted by this shaper.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "max-bandwidth": {"type": "integer", "min": 0, "max": 80000000},
    "max-concurrent-session": {"type": "integer", "min": 0, "max": 2097000},
    "max-concurrent-tcp-session": {"type": "integer", "min": 0, "max": 2097000},
    "max-concurrent-udp-session": {"type": "integer", "min": 0, "max": 2097000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_BANDWIDTH_UNIT = [
    "kbps",  # Kilobits per second.
    "mbps",  # Megabits per second.
    "gbps",  # Gigabits per second.
]
VALID_BODY_DIFFSERV_FORWARD = [
    "enable",  # Enable setting forward (original) traffic DiffServ.
    "disable",  # Disable setting forward (original) traffic DiffServ.
]
VALID_BODY_DIFFSERV_REVERSE = [
    "enable",  # Enable setting reverse (reply) traffic DiffServ.
    "disable",  # Disable setting reverse (reply) traffic DiffServ.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_shaper_per_ip_shaper_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/shaper/per_ip_shaper."""
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
    """Validate required fields for firewall/shaper/per_ip_shaper."""
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


def validate_firewall_shaper_per_ip_shaper_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/shaper/per_ip_shaper object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "bandwidth-unit" in payload:
        value = payload["bandwidth-unit"]
        if value not in VALID_BODY_BANDWIDTH_UNIT:
            desc = FIELD_DESCRIPTIONS.get("bandwidth-unit", "")
            error_msg = f"Invalid value for 'bandwidth-unit': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BANDWIDTH_UNIT)}"
            error_msg += f"\n  → Example: bandwidth-unit='{{ VALID_BODY_BANDWIDTH_UNIT[0] }}'"
            return (False, error_msg)
    if "diffserv-forward" in payload:
        value = payload["diffserv-forward"]
        if value not in VALID_BODY_DIFFSERV_FORWARD:
            desc = FIELD_DESCRIPTIONS.get("diffserv-forward", "")
            error_msg = f"Invalid value for 'diffserv-forward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIFFSERV_FORWARD)}"
            error_msg += f"\n  → Example: diffserv-forward='{{ VALID_BODY_DIFFSERV_FORWARD[0] }}'"
            return (False, error_msg)
    if "diffserv-reverse" in payload:
        value = payload["diffserv-reverse"]
        if value not in VALID_BODY_DIFFSERV_REVERSE:
            desc = FIELD_DESCRIPTIONS.get("diffserv-reverse", "")
            error_msg = f"Invalid value for 'diffserv-reverse': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIFFSERV_REVERSE)}"
            error_msg += f"\n  → Example: diffserv-reverse='{{ VALID_BODY_DIFFSERV_REVERSE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_shaper_per_ip_shaper_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/shaper/per_ip_shaper."""
    # Step 1: Validate enum values
    if "bandwidth-unit" in payload:
        value = payload["bandwidth-unit"]
        if value not in VALID_BODY_BANDWIDTH_UNIT:
            return (
                False,
                f"Invalid value for 'bandwidth-unit'='{value}'. Must be one of: {', '.join(VALID_BODY_BANDWIDTH_UNIT)}",
            )
    if "diffserv-forward" in payload:
        value = payload["diffserv-forward"]
        if value not in VALID_BODY_DIFFSERV_FORWARD:
            return (
                False,
                f"Invalid value for 'diffserv-forward'='{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_FORWARD)}",
            )
    if "diffserv-reverse" in payload:
        value = payload["diffserv-reverse"]
        if value not in VALID_BODY_DIFFSERV_REVERSE:
            return (
                False,
                f"Invalid value for 'diffserv-reverse'='{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_REVERSE)}",
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
    "endpoint": "firewall/shaper/per_ip_shaper",
    "category": "cmdb",
    "api_path": "firewall.shaper/per-ip-shaper",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure per-IP traffic shaper.",
    "total_fields": 10,
    "required_fields_count": 0,
    "fields_with_defaults_count": 10,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
