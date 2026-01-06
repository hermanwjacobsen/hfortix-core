"""Validation helpers for user/password_policy - Auto-generated"""

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
    "expire-status": "disable",
    "expire-days": 180,
    "warn-days": 15,
    "expired-password-renewal": "disable",
    "minimum-length": 8,
    "min-lower-case-letter": 0,
    "min-upper-case-letter": 0,
    "min-non-alphanumeric": 0,
    "min-number": 0,
    "min-change-characters": 0,
    "reuse-password": "enable",
    "reuse-password-limit": 0,
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
    "name": "string",  # Password policy name.
    "expire-status": "option",  # Enable/disable password expiration.
    "expire-days": "integer",  # Time in days before the user's password expires.
    "warn-days": "integer",  # Time in days before a password expiration warning message is
    "expired-password-renewal": "option",  # Enable/disable renewal of a password that already is expired
    "minimum-length": "integer",  # Minimum password length (8 - 128, default = 8).
    "min-lower-case-letter": "integer",  # Minimum number of lowercase characters in password (0 - 128,
    "min-upper-case-letter": "integer",  # Minimum number of uppercase characters in password (0 - 128,
    "min-non-alphanumeric": "integer",  # Minimum number of non-alphanumeric characters in password (0
    "min-number": "integer",  # Minimum number of numeric characters in password (0 - 128, d
    "min-change-characters": "integer",  # Minimum number of unique characters in new password which do
    "reuse-password": "option",  # Enable/disable reuse of password. If both reuse-password and
    "reuse-password-limit": "integer",  # Number of times passwords can be reused (0 - 20, default = 0
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Password policy name.",
    "expire-status": "Enable/disable password expiration.",
    "expire-days": "Time in days before the user's password expires.",
    "warn-days": "Time in days before a password expiration warning message is displayed to the user upon login.",
    "expired-password-renewal": "Enable/disable renewal of a password that already is expired.",
    "minimum-length": "Minimum password length (8 - 128, default = 8).",
    "min-lower-case-letter": "Minimum number of lowercase characters in password (0 - 128, default = 0).",
    "min-upper-case-letter": "Minimum number of uppercase characters in password (0 - 128, default = 0).",
    "min-non-alphanumeric": "Minimum number of non-alphanumeric characters in password (0 - 128, default = 0).",
    "min-number": "Minimum number of numeric characters in password (0 - 128, default = 0).",
    "min-change-characters": "Minimum number of unique characters in new password which do not exist in old password (0 - 128, default = 0. This attribute overrides reuse-password if both are enabled).",
    "reuse-password": "Enable/disable reuse of password. If both reuse-password and min-change-characters are enabled, min-change-characters overrides.",
    "reuse-password-limit": "Number of times passwords can be reused (0 - 20, default = 0. If set to 0, can reuse password an unlimited number of times.).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "expire-days": {"type": "integer", "min": 0, "max": 999},
    "warn-days": {"type": "integer", "min": 0, "max": 30},
    "minimum-length": {"type": "integer", "min": 8, "max": 128},
    "min-lower-case-letter": {"type": "integer", "min": 0, "max": 128},
    "min-upper-case-letter": {"type": "integer", "min": 0, "max": 128},
    "min-non-alphanumeric": {"type": "integer", "min": 0, "max": 128},
    "min-number": {"type": "integer", "min": 0, "max": 128},
    "min-change-characters": {"type": "integer", "min": 0, "max": 128},
    "reuse-password-limit": {"type": "integer", "min": 0, "max": 20},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_EXPIRE_STATUS = [
    "enable",  # Passwords expire after expire-day days.
    "disable",  # Passwords do not expire.
]
VALID_BODY_EXPIRED_PASSWORD_RENEWAL = [
    "enable",  # Enable renewal of a password that already is expired.
    "disable",  # Disable renewal of a password that already is expired.
]
VALID_BODY_REUSE_PASSWORD = [
    "enable",  # Users are allowed to reuse the same password up to a limit.
    "disable",  # Users must create a new password.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_password_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for user/password_policy."""
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
    """Validate required fields for user/password_policy."""
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


def validate_user_password_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new user/password_policy object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "expire-status" in payload:
        value = payload["expire-status"]
        if value not in VALID_BODY_EXPIRE_STATUS:
            desc = FIELD_DESCRIPTIONS.get("expire-status", "")
            error_msg = f"Invalid value for 'expire-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXPIRE_STATUS)}"
            error_msg += f"\n  → Example: expire-status='{{ VALID_BODY_EXPIRE_STATUS[0] }}'"
            return (False, error_msg)
    if "expired-password-renewal" in payload:
        value = payload["expired-password-renewal"]
        if value not in VALID_BODY_EXPIRED_PASSWORD_RENEWAL:
            desc = FIELD_DESCRIPTIONS.get("expired-password-renewal", "")
            error_msg = f"Invalid value for 'expired-password-renewal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXPIRED_PASSWORD_RENEWAL)}"
            error_msg += f"\n  → Example: expired-password-renewal='{{ VALID_BODY_EXPIRED_PASSWORD_RENEWAL[0] }}'"
            return (False, error_msg)
    if "reuse-password" in payload:
        value = payload["reuse-password"]
        if value not in VALID_BODY_REUSE_PASSWORD:
            desc = FIELD_DESCRIPTIONS.get("reuse-password", "")
            error_msg = f"Invalid value for 'reuse-password': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REUSE_PASSWORD)}"
            error_msg += f"\n  → Example: reuse-password='{{ VALID_BODY_REUSE_PASSWORD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_password_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update user/password_policy."""
    # Step 1: Validate enum values
    if "expire-status" in payload:
        value = payload["expire-status"]
        if value not in VALID_BODY_EXPIRE_STATUS:
            return (
                False,
                f"Invalid value for 'expire-status'='{value}'. Must be one of: {', '.join(VALID_BODY_EXPIRE_STATUS)}",
            )
    if "expired-password-renewal" in payload:
        value = payload["expired-password-renewal"]
        if value not in VALID_BODY_EXPIRED_PASSWORD_RENEWAL:
            return (
                False,
                f"Invalid value for 'expired-password-renewal'='{value}'. Must be one of: {', '.join(VALID_BODY_EXPIRED_PASSWORD_RENEWAL)}",
            )
    if "reuse-password" in payload:
        value = payload["reuse-password"]
        if value not in VALID_BODY_REUSE_PASSWORD:
            return (
                False,
                f"Invalid value for 'reuse-password'='{value}'. Must be one of: {', '.join(VALID_BODY_REUSE_PASSWORD)}",
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
    "endpoint": "user/password_policy",
    "category": "cmdb",
    "api_path": "user/password-policy",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure user password policy.",
    "total_fields": 13,
    "required_fields_count": 0,
    "fields_with_defaults_count": 13,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
