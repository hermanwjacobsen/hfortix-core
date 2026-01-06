"""Validation helpers for user/scim - Auto-generated"""

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
    "name",  # SCIM client name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "id": 0,
    "status": "disable",
    "base-url": "",
    "auth-method": "token",
    "token-certificate": "",
    "certificate": "",
    "client-identity-check": "enable",
    "cascade": "disable",
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
    "name": "string",  # SCIM client name.
    "id": "integer",  # SCIM client ID.
    "status": "option",  # Enable/disable System for Cross-domain Identity Management (
    "base-url": "string",  # Server URL to receive SCIM create, read, update, delete (CRU
    "auth-method": "option",  # TLS client authentication methods (default = bearer token).
    "token-certificate": "string",  # Certificate for token verification.
    "secret": "password",  # Secret for token verification or base authentication.
    "certificate": "string",  # Certificate for client verification during TLS handshake.
    "client-identity-check": "option",  # Enable/disable client identity check.
    "cascade": "option",  # Enable/disable to follow SCIM users/groups changes in IDP.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "SCIM client name.",
    "id": "SCIM client ID.",
    "status": "Enable/disable System for Cross-domain Identity Management (SCIM).",
    "base-url": "Server URL to receive SCIM create, read, update, delete (CRUD) requests.",
    "auth-method": "TLS client authentication methods (default = bearer token).",
    "token-certificate": "Certificate for token verification.",
    "secret": "Secret for token verification or base authentication.",
    "certificate": "Certificate for client verification during TLS handshake.",
    "client-identity-check": "Enable/disable client identity check.",
    "cascade": "Enable/disable to follow SCIM users/groups changes in IDP.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "base-url": {"type": "string", "max_length": 127},
    "token-certificate": {"type": "string", "max_length": 79},
    "certificate": {"type": "string", "max_length": 79},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable System for Cross-domain Identity Management (SCIM).
    "disable",  # Disable System for Cross-domain Identity Management (SCIM).
]
VALID_BODY_AUTH_METHOD = [
    "token",  # Bearer token.
    "base",  # Base.
]
VALID_BODY_CLIENT_IDENTITY_CHECK = [
    "enable",  # Enable client identity check.
    "disable",  # Disable client identity check.
]
VALID_BODY_CASCADE = [
    "disable",  # Disable setting.
    "enable",  # Enable setting.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_scim_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for user/scim."""
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
    """Validate required fields for user/scim."""
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


def validate_user_scim_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new user/scim object."""
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
    if "auth-method" in payload:
        value = payload["auth-method"]
        if value not in VALID_BODY_AUTH_METHOD:
            desc = FIELD_DESCRIPTIONS.get("auth-method", "")
            error_msg = f"Invalid value for 'auth-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_METHOD)}"
            error_msg += f"\n  → Example: auth-method='{{ VALID_BODY_AUTH_METHOD[0] }}'"
            return (False, error_msg)
    if "client-identity-check" in payload:
        value = payload["client-identity-check"]
        if value not in VALID_BODY_CLIENT_IDENTITY_CHECK:
            desc = FIELD_DESCRIPTIONS.get("client-identity-check", "")
            error_msg = f"Invalid value for 'client-identity-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLIENT_IDENTITY_CHECK)}"
            error_msg += f"\n  → Example: client-identity-check='{{ VALID_BODY_CLIENT_IDENTITY_CHECK[0] }}'"
            return (False, error_msg)
    if "cascade" in payload:
        value = payload["cascade"]
        if value not in VALID_BODY_CASCADE:
            desc = FIELD_DESCRIPTIONS.get("cascade", "")
            error_msg = f"Invalid value for 'cascade': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CASCADE)}"
            error_msg += f"\n  → Example: cascade='{{ VALID_BODY_CASCADE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_scim_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update user/scim."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "auth-method" in payload:
        value = payload["auth-method"]
        if value not in VALID_BODY_AUTH_METHOD:
            return (
                False,
                f"Invalid value for 'auth-method'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_METHOD)}",
            )
    if "client-identity-check" in payload:
        value = payload["client-identity-check"]
        if value not in VALID_BODY_CLIENT_IDENTITY_CHECK:
            return (
                False,
                f"Invalid value for 'client-identity-check'='{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_IDENTITY_CHECK)}",
            )
    if "cascade" in payload:
        value = payload["cascade"]
        if value not in VALID_BODY_CASCADE:
            return (
                False,
                f"Invalid value for 'cascade'='{value}'. Must be one of: {', '.join(VALID_BODY_CASCADE)}",
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
    "endpoint": "user/scim",
    "category": "cmdb",
    "api_path": "user/scim",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure SCIM client entries.",
    "total_fields": 10,
    "required_fields_count": 1,
    "fields_with_defaults_count": 9,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
