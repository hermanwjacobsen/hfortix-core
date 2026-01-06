"""Validation helpers for switch_controller/ptp/profile - Auto-generated"""

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
    "name",  # Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "description": "",
    "mode": "transparent-e2e",
    "ptp-profile": "C37.238-2017",
    "transport": "l2-mcast",
    "domain": 254,
    "pdelay-req-interval": "1sec",
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
    "name": "string",  # Profile name.
    "description": "string",  # Description.
    "mode": "option",  # Select PTP mode.
    "ptp-profile": "option",  # Configure PTP power profile.
    "transport": "option",  # Configure PTP transport mode.
    "domain": "integer",  # Configure PTP domain value (0 - 255, default = 254).
    "pdelay-req-interval": "option",  # Configure PTP peer delay request interval.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "description": "Description.",
    "mode": "Select PTP mode.",
    "ptp-profile": "Configure PTP power profile.",
    "transport": "Configure PTP transport mode.",
    "domain": "Configure PTP domain value (0 - 255, default = 254).",
    "pdelay-req-interval": "Configure PTP peer delay request interval.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
    "description": {"type": "string", "max_length": 63},
    "domain": {"type": "integer", "min": 0, "max": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_MODE = [
    "transparent-e2e",  # End-to-end transparent clock.
    "transparent-p2p",  # Peer-to-peer transparent clock.
]
VALID_BODY_PTP_PROFILE = [
    "C37.238-2017",  # C37.238-2017 power profile.
]
VALID_BODY_TRANSPORT = [
    "l2-mcast",  # L2 multicast.
]
VALID_BODY_PDELAY_REQ_INTERVAL = [
    "1sec",  # 1 sec.
    "2sec",  # 2 sec.
    "4sec",  # 4 sec.
    "8sec",  # 8 sec.
    "16sec",  # 16 sec.
    "32sec",  # 32 sec.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_ptp_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/ptp/profile."""
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
    """Validate required fields for switch_controller/ptp/profile."""
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


def validate_switch_controller_ptp_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/ptp/profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            desc = FIELD_DESCRIPTIONS.get("mode", "")
            error_msg = f"Invalid value for 'mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MODE)}"
            error_msg += f"\n  → Example: mode='{{ VALID_BODY_MODE[0] }}'"
            return (False, error_msg)
    if "ptp-profile" in payload:
        value = payload["ptp-profile"]
        if value not in VALID_BODY_PTP_PROFILE:
            desc = FIELD_DESCRIPTIONS.get("ptp-profile", "")
            error_msg = f"Invalid value for 'ptp-profile': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PTP_PROFILE)}"
            error_msg += f"\n  → Example: ptp-profile='{{ VALID_BODY_PTP_PROFILE[0] }}'"
            return (False, error_msg)
    if "transport" in payload:
        value = payload["transport"]
        if value not in VALID_BODY_TRANSPORT:
            desc = FIELD_DESCRIPTIONS.get("transport", "")
            error_msg = f"Invalid value for 'transport': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRANSPORT)}"
            error_msg += f"\n  → Example: transport='{{ VALID_BODY_TRANSPORT[0] }}'"
            return (False, error_msg)
    if "pdelay-req-interval" in payload:
        value = payload["pdelay-req-interval"]
        if value not in VALID_BODY_PDELAY_REQ_INTERVAL:
            desc = FIELD_DESCRIPTIONS.get("pdelay-req-interval", "")
            error_msg = f"Invalid value for 'pdelay-req-interval': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PDELAY_REQ_INTERVAL)}"
            error_msg += f"\n  → Example: pdelay-req-interval='{{ VALID_BODY_PDELAY_REQ_INTERVAL[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_ptp_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/ptp/profile."""
    # Step 1: Validate enum values
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid value for 'mode'='{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )
    if "ptp-profile" in payload:
        value = payload["ptp-profile"]
        if value not in VALID_BODY_PTP_PROFILE:
            return (
                False,
                f"Invalid value for 'ptp-profile'='{value}'. Must be one of: {', '.join(VALID_BODY_PTP_PROFILE)}",
            )
    if "transport" in payload:
        value = payload["transport"]
        if value not in VALID_BODY_TRANSPORT:
            return (
                False,
                f"Invalid value for 'transport'='{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPORT)}",
            )
    if "pdelay-req-interval" in payload:
        value = payload["pdelay-req-interval"]
        if value not in VALID_BODY_PDELAY_REQ_INTERVAL:
            return (
                False,
                f"Invalid value for 'pdelay-req-interval'='{value}'. Must be one of: {', '.join(VALID_BODY_PDELAY_REQ_INTERVAL)}",
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
    "endpoint": "switch_controller/ptp/profile",
    "category": "cmdb",
    "api_path": "switch-controller.ptp/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Global PTP profile.",
    "total_fields": 7,
    "required_fields_count": 1,
    "fields_with_defaults_count": 7,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
