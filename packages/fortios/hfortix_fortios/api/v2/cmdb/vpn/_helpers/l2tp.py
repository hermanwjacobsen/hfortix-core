"""Validation helpers for vpn/l2tp - Auto-generated"""

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
    "usrgrp",  # User group.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "status": "disable",
    "eip": "0.0.0.0",
    "sip": "0.0.0.0",
    "usrgrp": "",
    "enforce-ipsec": "disable",
    "lcp-echo-interval": 5,
    "lcp-max-echo-fails": 3,
    "hello-interval": 60,
    "compress": "disable",
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
    "status": "option",  # Enable/disable FortiGate as a L2TP gateway.
    "eip": "ipv4-address",  # End IP.
    "sip": "ipv4-address",  # Start IP.
    "usrgrp": "string",  # User group.
    "enforce-ipsec": "option",  # Enable/disable IPsec enforcement.
    "lcp-echo-interval": "integer",  # Time in seconds between PPPoE Link Control Protocol (LCP) ec
    "lcp-max-echo-fails": "integer",  # Maximum number of missed LCP echo messages before disconnect
    "hello-interval": "integer",  # L2TP hello message interval in seconds (0 - 3600 sec, defaul
    "compress": "option",  # Enable/disable data compression.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable FortiGate as a L2TP gateway.",
    "eip": "End IP.",
    "sip": "Start IP.",
    "usrgrp": "User group.",
    "enforce-ipsec": "Enable/disable IPsec enforcement.",
    "lcp-echo-interval": "Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.",
    "lcp-max-echo-fails": "Maximum number of missed LCP echo messages before disconnect.",
    "hello-interval": "L2TP hello message interval in seconds (0 - 3600 sec, default = 60).",
    "compress": "Enable/disable data compression.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "usrgrp": {"type": "string", "max_length": 35},
    "lcp-echo-interval": {"type": "integer", "min": 0, "max": 32767},
    "lcp-max-echo-fails": {"type": "integer", "min": 0, "max": 32767},
    "hello-interval": {"type": "integer", "min": 0, "max": 3600},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_ENFORCE_IPSEC = [
    "enable",  # Enable enforce-ipsec
    "disable",  # Disable enforce-ipsec
]
VALID_BODY_COMPRESS = [
    "enable",  # Enable compress
    "disable",  # Disable compress
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vpn_l2tp_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for vpn/l2tp."""
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
    """Validate required fields for vpn/l2tp."""
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


def validate_vpn_l2tp_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new vpn/l2tp object."""
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
    if "enforce-ipsec" in payload:
        value = payload["enforce-ipsec"]
        if value not in VALID_BODY_ENFORCE_IPSEC:
            desc = FIELD_DESCRIPTIONS.get("enforce-ipsec", "")
            error_msg = f"Invalid value for 'enforce-ipsec': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENFORCE_IPSEC)}"
            error_msg += f"\n  → Example: enforce-ipsec='{{ VALID_BODY_ENFORCE_IPSEC[0] }}'"
            return (False, error_msg)
    if "compress" in payload:
        value = payload["compress"]
        if value not in VALID_BODY_COMPRESS:
            desc = FIELD_DESCRIPTIONS.get("compress", "")
            error_msg = f"Invalid value for 'compress': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_COMPRESS)}"
            error_msg += f"\n  → Example: compress='{{ VALID_BODY_COMPRESS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_vpn_l2tp_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update vpn/l2tp."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "enforce-ipsec" in payload:
        value = payload["enforce-ipsec"]
        if value not in VALID_BODY_ENFORCE_IPSEC:
            return (
                False,
                f"Invalid value for 'enforce-ipsec'='{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_IPSEC)}",
            )
    if "compress" in payload:
        value = payload["compress"]
        if value not in VALID_BODY_COMPRESS:
            return (
                False,
                f"Invalid value for 'compress'='{value}'. Must be one of: {', '.join(VALID_BODY_COMPRESS)}",
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
    "endpoint": "vpn/l2tp",
    "category": "cmdb",
    "api_path": "vpn/l2tp",
    "help": "Configure L2TP.",
    "total_fields": 9,
    "required_fields_count": 1,
    "fields_with_defaults_count": 9,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
