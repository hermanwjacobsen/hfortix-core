"""Validation helpers for firewall/shaper/traffic_shaper - Auto-generated"""

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
    "guaranteed-bandwidth": 0,
    "maximum-bandwidth": 0,
    "bandwidth-unit": "kbps",
    "priority": "high",
    "per-policy": "disable",
    "diffserv": "disable",
    "diffservcode": "",
    "dscp-marking-method": "static",
    "exceed-bandwidth": 0,
    "exceed-dscp": "",
    "maximum-dscp": "",
    "cos-marking": "disable",
    "cos-marking-method": "static",
    "cos": "",
    "exceed-cos": "",
    "maximum-cos": "",
    "overhead": 0,
    "exceed-class-id": 0,
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
    "guaranteed-bandwidth": "integer",  # Amount of bandwidth guaranteed for this shaper (0 - 80000000
    "maximum-bandwidth": "integer",  # Upper bandwidth limit enforced by this shaper (0 - 80000000)
    "bandwidth-unit": "option",  # Unit of measurement for guaranteed and maximum bandwidth for
    "priority": "option",  # Higher priority traffic is more likely to be forwarded witho
    "per-policy": "option",  # Enable/disable applying a separate shaper for each policy. F
    "diffserv": "option",  # Enable/disable changing the DiffServ setting applied to traf
    "diffservcode": "user",  # DiffServ setting to be applied to traffic accepted by this s
    "dscp-marking-method": "option",  # Select DSCP marking method.
    "exceed-bandwidth": "integer",  # Exceed bandwidth used for DSCP/VLAN CoS multi-stage marking.
    "exceed-dscp": "user",  # DSCP mark for traffic in guaranteed-bandwidth and exceed-ban
    "maximum-dscp": "user",  # DSCP mark for traffic in exceed-bandwidth and maximum-bandwi
    "cos-marking": "option",  # Enable/disable VLAN CoS marking.
    "cos-marking-method": "option",  # Select VLAN CoS marking method.
    "cos": "user",  # VLAN CoS mark.
    "exceed-cos": "user",  # VLAN CoS mark for traffic in [guaranteed-bandwidth, exceed-b
    "maximum-cos": "user",  # VLAN CoS mark for traffic in [exceed-bandwidth, maximum-band
    "overhead": "integer",  # Per-packet size overhead used in rate computations.
    "exceed-class-id": "integer",  # Class ID for traffic in guaranteed-bandwidth and maximum-ban
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Traffic shaper name.",
    "guaranteed-bandwidth": "Amount of bandwidth guaranteed for this shaper (0 - 80000000). Units depend on the bandwidth-unit setting.",
    "maximum-bandwidth": "Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit. Units depend on the bandwidth-unit setting.",
    "bandwidth-unit": "Unit of measurement for guaranteed and maximum bandwidth for this shaper (Kbps, Mbps or Gbps).",
    "priority": "Higher priority traffic is more likely to be forwarded without delays and without compromising the guaranteed bandwidth.",
    "per-policy": "Enable/disable applying a separate shaper for each policy. For example, if enabled the guaranteed bandwidth is applied separately for each policy.",
    "diffserv": "Enable/disable changing the DiffServ setting applied to traffic accepted by this shaper.",
    "diffservcode": "DiffServ setting to be applied to traffic accepted by this shaper.",
    "dscp-marking-method": "Select DSCP marking method.",
    "exceed-bandwidth": "Exceed bandwidth used for DSCP/VLAN CoS multi-stage marking. Units depend on the bandwidth-unit setting.",
    "exceed-dscp": "DSCP mark for traffic in guaranteed-bandwidth and exceed-bandwidth.",
    "maximum-dscp": "DSCP mark for traffic in exceed-bandwidth and maximum-bandwidth.",
    "cos-marking": "Enable/disable VLAN CoS marking.",
    "cos-marking-method": "Select VLAN CoS marking method.",
    "cos": "VLAN CoS mark.",
    "exceed-cos": "VLAN CoS mark for traffic in [guaranteed-bandwidth, exceed-bandwidth].",
    "maximum-cos": "VLAN CoS mark for traffic in [exceed-bandwidth, maximum-bandwidth].",
    "overhead": "Per-packet size overhead used in rate computations.",
    "exceed-class-id": "Class ID for traffic in guaranteed-bandwidth and maximum-bandwidth.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "guaranteed-bandwidth": {"type": "integer", "min": 0, "max": 80000000},
    "maximum-bandwidth": {"type": "integer", "min": 0, "max": 80000000},
    "exceed-bandwidth": {"type": "integer", "min": 0, "max": 80000000},
    "overhead": {"type": "integer", "min": 0, "max": 100},
    "exceed-class-id": {"type": "integer", "min": 0, "max": 4294967295},
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
VALID_BODY_PRIORITY = [
    "low",  # Low priority.
    "medium",  # Medium priority.
    "high",  # High priority.
]
VALID_BODY_PER_POLICY = [
    "disable",  # All referring policies share one traffic shaper.
    "enable",  # Each referring policy has its own traffic shaper.
]
VALID_BODY_DIFFSERV = [
    "enable",  # Enable setting traffic DiffServ.
    "disable",  # Disable setting traffic DiffServ.
]
VALID_BODY_DSCP_MARKING_METHOD = [
    "multi-stage",  # Multistage marking.
    "static",  # Static marking.
]
VALID_BODY_COS_MARKING = [
    "enable",  # Enable VLAN CoS marking.
    "disable",  # Disable VLAN CoS marking.
]
VALID_BODY_COS_MARKING_METHOD = [
    "multi-stage",  # Multi stage marking.
    "static",  # Static marking.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_shaper_traffic_shaper_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/shaper/traffic_shaper."""
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
    """Validate required fields for firewall/shaper/traffic_shaper."""
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


def validate_firewall_shaper_traffic_shaper_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/shaper/traffic_shaper object."""
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
    if "priority" in payload:
        value = payload["priority"]
        if value not in VALID_BODY_PRIORITY:
            desc = FIELD_DESCRIPTIONS.get("priority", "")
            error_msg = f"Invalid value for 'priority': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY)}"
            error_msg += f"\n  → Example: priority='{{ VALID_BODY_PRIORITY[0] }}'"
            return (False, error_msg)
    if "per-policy" in payload:
        value = payload["per-policy"]
        if value not in VALID_BODY_PER_POLICY:
            desc = FIELD_DESCRIPTIONS.get("per-policy", "")
            error_msg = f"Invalid value for 'per-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PER_POLICY)}"
            error_msg += f"\n  → Example: per-policy='{{ VALID_BODY_PER_POLICY[0] }}'"
            return (False, error_msg)
    if "diffserv" in payload:
        value = payload["diffserv"]
        if value not in VALID_BODY_DIFFSERV:
            desc = FIELD_DESCRIPTIONS.get("diffserv", "")
            error_msg = f"Invalid value for 'diffserv': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIFFSERV)}"
            error_msg += f"\n  → Example: diffserv='{{ VALID_BODY_DIFFSERV[0] }}'"
            return (False, error_msg)
    if "dscp-marking-method" in payload:
        value = payload["dscp-marking-method"]
        if value not in VALID_BODY_DSCP_MARKING_METHOD:
            desc = FIELD_DESCRIPTIONS.get("dscp-marking-method", "")
            error_msg = f"Invalid value for 'dscp-marking-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DSCP_MARKING_METHOD)}"
            error_msg += f"\n  → Example: dscp-marking-method='{{ VALID_BODY_DSCP_MARKING_METHOD[0] }}'"
            return (False, error_msg)
    if "cos-marking" in payload:
        value = payload["cos-marking"]
        if value not in VALID_BODY_COS_MARKING:
            desc = FIELD_DESCRIPTIONS.get("cos-marking", "")
            error_msg = f"Invalid value for 'cos-marking': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_COS_MARKING)}"
            error_msg += f"\n  → Example: cos-marking='{{ VALID_BODY_COS_MARKING[0] }}'"
            return (False, error_msg)
    if "cos-marking-method" in payload:
        value = payload["cos-marking-method"]
        if value not in VALID_BODY_COS_MARKING_METHOD:
            desc = FIELD_DESCRIPTIONS.get("cos-marking-method", "")
            error_msg = f"Invalid value for 'cos-marking-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_COS_MARKING_METHOD)}"
            error_msg += f"\n  → Example: cos-marking-method='{{ VALID_BODY_COS_MARKING_METHOD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_shaper_traffic_shaper_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/shaper/traffic_shaper."""
    # Step 1: Validate enum values
    if "bandwidth-unit" in payload:
        value = payload["bandwidth-unit"]
        if value not in VALID_BODY_BANDWIDTH_UNIT:
            return (
                False,
                f"Invalid value for 'bandwidth-unit'='{value}'. Must be one of: {', '.join(VALID_BODY_BANDWIDTH_UNIT)}",
            )
    if "priority" in payload:
        value = payload["priority"]
        if value not in VALID_BODY_PRIORITY:
            return (
                False,
                f"Invalid value for 'priority'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY)}",
            )
    if "per-policy" in payload:
        value = payload["per-policy"]
        if value not in VALID_BODY_PER_POLICY:
            return (
                False,
                f"Invalid value for 'per-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_PER_POLICY)}",
            )
    if "diffserv" in payload:
        value = payload["diffserv"]
        if value not in VALID_BODY_DIFFSERV:
            return (
                False,
                f"Invalid value for 'diffserv'='{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV)}",
            )
    if "dscp-marking-method" in payload:
        value = payload["dscp-marking-method"]
        if value not in VALID_BODY_DSCP_MARKING_METHOD:
            return (
                False,
                f"Invalid value for 'dscp-marking-method'='{value}'. Must be one of: {', '.join(VALID_BODY_DSCP_MARKING_METHOD)}",
            )
    if "cos-marking" in payload:
        value = payload["cos-marking"]
        if value not in VALID_BODY_COS_MARKING:
            return (
                False,
                f"Invalid value for 'cos-marking'='{value}'. Must be one of: {', '.join(VALID_BODY_COS_MARKING)}",
            )
    if "cos-marking-method" in payload:
        value = payload["cos-marking-method"]
        if value not in VALID_BODY_COS_MARKING_METHOD:
            return (
                False,
                f"Invalid value for 'cos-marking-method'='{value}'. Must be one of: {', '.join(VALID_BODY_COS_MARKING_METHOD)}",
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
    "endpoint": "firewall/shaper/traffic_shaper",
    "category": "cmdb",
    "api_path": "firewall.shaper/traffic-shaper",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure shared traffic shaper.",
    "total_fields": 19,
    "required_fields_count": 0,
    "fields_with_defaults_count": 19,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
