"""Validation helpers for wireless_controller/utm_profile - Auto-generated"""

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
    "comment": "",
    "utm-log": "enable",
    "ips-sensor": "",
    "application-list": "",
    "antivirus-profile": "",
    "webfilter-profile": "",
    "scan-botnet-connections": "monitor",
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
    "name": "string",  # UTM profile name.
    "comment": "string",  # Comment.
    "utm-log": "option",  # Enable/disable UTM logging.
    "ips-sensor": "string",  # IPS sensor name.
    "application-list": "string",  # Application control list name.
    "antivirus-profile": "string",  # AntiVirus profile name.
    "webfilter-profile": "string",  # WebFilter profile name.
    "scan-botnet-connections": "option",  # Block or monitor connections to Botnet servers or disable Bo
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "UTM profile name.",
    "comment": "Comment.",
    "utm-log": "Enable/disable UTM logging.",
    "ips-sensor": "IPS sensor name.",
    "application-list": "Application control list name.",
    "antivirus-profile": "AntiVirus profile name.",
    "webfilter-profile": "WebFilter profile name.",
    "scan-botnet-connections": "Block or monitor connections to Botnet servers or disable Botnet scanning.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "comment": {"type": "string", "max_length": 63},
    "ips-sensor": {"type": "string", "max_length": 47},
    "application-list": {"type": "string", "max_length": 47},
    "antivirus-profile": {"type": "string", "max_length": 47},
    "webfilter-profile": {"type": "string", "max_length": 47},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_UTM_LOG = [
    "enable",  # Enable UTM logging.
    "disable",  # Disable UTM logging.
]
VALID_BODY_SCAN_BOTNET_CONNECTIONS = [
    "disable",  # Do not scan connections to botnet servers.
    "monitor",  # Log connections to botnet servers.
    "block",  # Block connections to botnet servers.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_utm_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for wireless_controller/utm_profile."""
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
    """Validate required fields for wireless_controller/utm_profile."""
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


def validate_wireless_controller_utm_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new wireless_controller/utm_profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "utm-log" in payload:
        value = payload["utm-log"]
        if value not in VALID_BODY_UTM_LOG:
            desc = FIELD_DESCRIPTIONS.get("utm-log", "")
            error_msg = f"Invalid value for 'utm-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UTM_LOG)}"
            error_msg += f"\n  → Example: utm-log='{{ VALID_BODY_UTM_LOG[0] }}'"
            return (False, error_msg)
    if "scan-botnet-connections" in payload:
        value = payload["scan-botnet-connections"]
        if value not in VALID_BODY_SCAN_BOTNET_CONNECTIONS:
            desc = FIELD_DESCRIPTIONS.get("scan-botnet-connections", "")
            error_msg = f"Invalid value for 'scan-botnet-connections': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCAN_BOTNET_CONNECTIONS)}"
            error_msg += f"\n  → Example: scan-botnet-connections='{{ VALID_BODY_SCAN_BOTNET_CONNECTIONS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_utm_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update wireless_controller/utm_profile."""
    # Step 1: Validate enum values
    if "utm-log" in payload:
        value = payload["utm-log"]
        if value not in VALID_BODY_UTM_LOG:
            return (
                False,
                f"Invalid value for 'utm-log'='{value}'. Must be one of: {', '.join(VALID_BODY_UTM_LOG)}",
            )
    if "scan-botnet-connections" in payload:
        value = payload["scan-botnet-connections"]
        if value not in VALID_BODY_SCAN_BOTNET_CONNECTIONS:
            return (
                False,
                f"Invalid value for 'scan-botnet-connections'='{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_BOTNET_CONNECTIONS)}",
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
    "endpoint": "wireless_controller/utm_profile",
    "category": "cmdb",
    "api_path": "wireless-controller/utm-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure UTM (Unified Threat Management) profile.",
    "total_fields": 8,
    "required_fields_count": 0,
    "fields_with_defaults_count": 8,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
