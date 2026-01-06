"""Validation helpers for system/probe_response - Auto-generated"""

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
    "port": 8008,
    "http-probe-value": "OK",
    "ttl-mode": "retain",
    "mode": "none",
    "security-mode": "none",
    "timeout": 300,
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
    "port": "integer",  # Port number to response.
    "http-probe-value": "string",  # Value to respond to the monitoring server.
    "ttl-mode": "option",  # Mode for TWAMP packet TTL modification.
    "mode": "option",  # SLA response mode.
    "security-mode": "option",  # TWAMP responder security mode.
    "password": "password",  # TWAMP responder password in authentication mode.
    "timeout": "integer",  # An inactivity timer for a twamp test session.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "port": "Port number to response.",
    "http-probe-value": "Value to respond to the monitoring server.",
    "ttl-mode": "Mode for TWAMP packet TTL modification.",
    "mode": "SLA response mode.",
    "security-mode": "TWAMP responder security mode.",
    "password": "TWAMP responder password in authentication mode.",
    "timeout": "An inactivity timer for a twamp test session.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "port": {"type": "integer", "min": 1, "max": 65535},
    "http-probe-value": {"type": "string", "max_length": 1024},
    "timeout": {"type": "integer", "min": 10, "max": 3600},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_TTL_MODE = [
    "reinit",  # Reinitialize TTL.
    "decrease",  # Decrease TTL.
    "retain",  # Retain TTL.
]
VALID_BODY_MODE = [
    "none",  # Disable probe.
    "http-probe",  # HTTP probe.
    "twamp",  # Two way active measurement protocol.
]
VALID_BODY_SECURITY_MODE = [
    "none",  # Unauthenticated mode.
    "authentication",  # Authenticated mode.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_probe_response_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/probe_response."""
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
    """Validate required fields for system/probe_response."""
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


def validate_system_probe_response_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/probe_response object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "ttl-mode" in payload:
        value = payload["ttl-mode"]
        if value not in VALID_BODY_TTL_MODE:
            desc = FIELD_DESCRIPTIONS.get("ttl-mode", "")
            error_msg = f"Invalid value for 'ttl-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TTL_MODE)}"
            error_msg += f"\n  → Example: ttl-mode='{{ VALID_BODY_TTL_MODE[0] }}'"
            return (False, error_msg)
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
    if "security-mode" in payload:
        value = payload["security-mode"]
        if value not in VALID_BODY_SECURITY_MODE:
            desc = FIELD_DESCRIPTIONS.get("security-mode", "")
            error_msg = f"Invalid value for 'security-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURITY_MODE)}"
            error_msg += f"\n  → Example: security-mode='{{ VALID_BODY_SECURITY_MODE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_probe_response_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/probe_response."""
    # Step 1: Validate enum values
    if "ttl-mode" in payload:
        value = payload["ttl-mode"]
        if value not in VALID_BODY_TTL_MODE:
            return (
                False,
                f"Invalid value for 'ttl-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_TTL_MODE)}",
            )
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid value for 'mode'='{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )
    if "security-mode" in payload:
        value = payload["security-mode"]
        if value not in VALID_BODY_SECURITY_MODE:
            return (
                False,
                f"Invalid value for 'security-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MODE)}",
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
    "endpoint": "system/probe_response",
    "category": "cmdb",
    "api_path": "system/probe-response",
    "help": "Configure system probe response.",
    "total_fields": 7,
    "required_fields_count": 0,
    "fields_with_defaults_count": 6,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
