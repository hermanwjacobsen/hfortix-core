"""Validation helpers for log/tacacs_plusaccounting2/filter - Auto-generated"""

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
    "login-audit": "enable",
    "config-change-audit": "enable",
    "cli-cmd-audit": "disable",
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
    "login-audit": "option",  # Enable/disable TACACS+ accounting for login events audit.
    "config-change-audit": "option",  # Enable/disable TACACS+ accounting for configuration change e
    "cli-cmd-audit": "option",  # Enable/disable TACACS+ accounting for CLI commands audit.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "login-audit": "Enable/disable TACACS+ accounting for login events audit.",
    "config-change-audit": "Enable/disable TACACS+ accounting for configuration change events audit.",
    "cli-cmd-audit": "Enable/disable TACACS+ accounting for CLI commands audit.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_LOGIN_AUDIT = [
    "enable",  # Enable TACACS+ accounting for login events audit.
    "disable",  # Disable TACACS+ accounting for login events audit.
]
VALID_BODY_CONFIG_CHANGE_AUDIT = [
    "enable",  # Enable TACACS+ accounting for configuration change events audit.
    "disable",  # Disable TACACS+ accounting for configuration change events audit.
]
VALID_BODY_CLI_CMD_AUDIT = [
    "enable",  # Enable TACACS+ accounting for CLI commands audit.
    "disable",  # Disable TACACS+ accounting for CLI commands audit.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_log_tacacs_plusaccounting2_filter_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for log/tacacs_plusaccounting2/filter."""
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
    """Validate required fields for log/tacacs_plusaccounting2/filter."""
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


def validate_log_tacacs_plusaccounting2_filter_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new log/tacacs_plusaccounting2/filter object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "login-audit" in payload:
        value = payload["login-audit"]
        if value not in VALID_BODY_LOGIN_AUDIT:
            desc = FIELD_DESCRIPTIONS.get("login-audit", "")
            error_msg = f"Invalid value for 'login-audit': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGIN_AUDIT)}"
            error_msg += f"\n  → Example: login-audit='{{ VALID_BODY_LOGIN_AUDIT[0] }}'"
            return (False, error_msg)
    if "config-change-audit" in payload:
        value = payload["config-change-audit"]
        if value not in VALID_BODY_CONFIG_CHANGE_AUDIT:
            desc = FIELD_DESCRIPTIONS.get("config-change-audit", "")
            error_msg = f"Invalid value for 'config-change-audit': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CONFIG_CHANGE_AUDIT)}"
            error_msg += f"\n  → Example: config-change-audit='{{ VALID_BODY_CONFIG_CHANGE_AUDIT[0] }}'"
            return (False, error_msg)
    if "cli-cmd-audit" in payload:
        value = payload["cli-cmd-audit"]
        if value not in VALID_BODY_CLI_CMD_AUDIT:
            desc = FIELD_DESCRIPTIONS.get("cli-cmd-audit", "")
            error_msg = f"Invalid value for 'cli-cmd-audit': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLI_CMD_AUDIT)}"
            error_msg += f"\n  → Example: cli-cmd-audit='{{ VALID_BODY_CLI_CMD_AUDIT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_tacacs_plusaccounting2_filter_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update log/tacacs_plusaccounting2/filter."""
    # Step 1: Validate enum values
    if "login-audit" in payload:
        value = payload["login-audit"]
        if value not in VALID_BODY_LOGIN_AUDIT:
            return (
                False,
                f"Invalid value for 'login-audit'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_AUDIT)}",
            )
    if "config-change-audit" in payload:
        value = payload["config-change-audit"]
        if value not in VALID_BODY_CONFIG_CHANGE_AUDIT:
            return (
                False,
                f"Invalid value for 'config-change-audit'='{value}'. Must be one of: {', '.join(VALID_BODY_CONFIG_CHANGE_AUDIT)}",
            )
    if "cli-cmd-audit" in payload:
        value = payload["cli-cmd-audit"]
        if value not in VALID_BODY_CLI_CMD_AUDIT:
            return (
                False,
                f"Invalid value for 'cli-cmd-audit'='{value}'. Must be one of: {', '.join(VALID_BODY_CLI_CMD_AUDIT)}",
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
    "endpoint": "log/tacacs_plusaccounting2/filter",
    "category": "cmdb",
    "api_path": "log.tacacs+accounting2/filter",
    "help": "Settings for TACACS+ accounting events filter.",
    "total_fields": 3,
    "required_fields_count": 0,
    "fields_with_defaults_count": 3,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
