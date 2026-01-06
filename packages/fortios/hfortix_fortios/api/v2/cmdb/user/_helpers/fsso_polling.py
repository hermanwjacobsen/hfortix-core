"""Validation helpers for user/fsso_polling - Auto-generated"""

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
    "server",  # Host name or IP address of the Active Directory server.
    "user",  # User name required to log into this Active Directory server.
    "ldap-server",  # LDAP server name used in LDAP connection strings.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
    "status": "enable",
    "server": "",
    "default-domain": "",
    "port": 0,
    "user": "",
    "ldap-server": "",
    "logon-history": 8,
    "polling-frequency": 10,
    "smbv1": "disable",
    "smb-ntlmv1-auth": "disable",
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
    "id": "integer",  # Active Directory server ID.
    "status": "option",  # Enable/disable polling for the status of this Active Directo
    "server": "string",  # Host name or IP address of the Active Directory server.
    "default-domain": "string",  # Default domain managed by this Active Directory server.
    "port": "integer",  # Port to communicate with this Active Directory server.
    "user": "string",  # User name required to log into this Active Directory server.
    "password": "password",  # Password required to log into this Active Directory server.
    "ldap-server": "string",  # LDAP server name used in LDAP connection strings.
    "logon-history": "integer",  # Number of hours of logon history to keep, 0 means keep all h
    "polling-frequency": "integer",  # Polling frequency (every 1 to 30 seconds).
    "adgrp": "string",  # LDAP Group Info.
    "smbv1": "option",  # Enable/disable support of SMBv1 for Samba.
    "smb-ntlmv1-auth": "option",  # Enable/disable support of NTLMv1 for Samba authentication.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "Active Directory server ID.",
    "status": "Enable/disable polling for the status of this Active Directory server.",
    "server": "Host name or IP address of the Active Directory server.",
    "default-domain": "Default domain managed by this Active Directory server.",
    "port": "Port to communicate with this Active Directory server.",
    "user": "User name required to log into this Active Directory server.",
    "password": "Password required to log into this Active Directory server.",
    "ldap-server": "LDAP server name used in LDAP connection strings.",
    "logon-history": "Number of hours of logon history to keep, 0 means keep all history.",
    "polling-frequency": "Polling frequency (every 1 to 30 seconds).",
    "adgrp": "LDAP Group Info.",
    "smbv1": "Enable/disable support of SMBv1 for Samba.",
    "smb-ntlmv1-auth": "Enable/disable support of NTLMv1 for Samba authentication.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "server": {"type": "string", "max_length": 63},
    "default-domain": {"type": "string", "max_length": 35},
    "port": {"type": "integer", "min": 0, "max": 65535},
    "user": {"type": "string", "max_length": 35},
    "ldap-server": {"type": "string", "max_length": 35},
    "logon-history": {"type": "integer", "min": 0, "max": 48},
    "polling-frequency": {"type": "integer", "min": 1, "max": 30},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "adgrp": {
        "name": {
            "type": "string",
            "help": "Name.",
            "required": True,
            "default": "",
            "max_length": 511,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_SMBV1 = [
    "enable",  # Enable support of SMBv1 for Samba.
    "disable",  # Disable support of SMBv1 for Samba.
]
VALID_BODY_SMB_NTLMV1_AUTH = [
    "enable",  # Enable support of NTLMv1 for Samba authentication.
    "disable",  # Disable support of NTLMv1 for Samba authentication.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_fsso_polling_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for user/fsso_polling."""
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
    """Validate required fields for user/fsso_polling."""
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


def validate_user_fsso_polling_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new user/fsso_polling object."""
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
    if "smbv1" in payload:
        value = payload["smbv1"]
        if value not in VALID_BODY_SMBV1:
            desc = FIELD_DESCRIPTIONS.get("smbv1", "")
            error_msg = f"Invalid value for 'smbv1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SMBV1)}"
            error_msg += f"\n  → Example: smbv1='{{ VALID_BODY_SMBV1[0] }}'"
            return (False, error_msg)
    if "smb-ntlmv1-auth" in payload:
        value = payload["smb-ntlmv1-auth"]
        if value not in VALID_BODY_SMB_NTLMV1_AUTH:
            desc = FIELD_DESCRIPTIONS.get("smb-ntlmv1-auth", "")
            error_msg = f"Invalid value for 'smb-ntlmv1-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SMB_NTLMV1_AUTH)}"
            error_msg += f"\n  → Example: smb-ntlmv1-auth='{{ VALID_BODY_SMB_NTLMV1_AUTH[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_fsso_polling_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update user/fsso_polling."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "smbv1" in payload:
        value = payload["smbv1"]
        if value not in VALID_BODY_SMBV1:
            return (
                False,
                f"Invalid value for 'smbv1'='{value}'. Must be one of: {', '.join(VALID_BODY_SMBV1)}",
            )
    if "smb-ntlmv1-auth" in payload:
        value = payload["smb-ntlmv1-auth"]
        if value not in VALID_BODY_SMB_NTLMV1_AUTH:
            return (
                False,
                f"Invalid value for 'smb-ntlmv1-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_SMB_NTLMV1_AUTH)}",
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
    "endpoint": "user/fsso_polling",
    "category": "cmdb",
    "api_path": "user/fsso-polling",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure FSSO active directory servers for polling mode.",
    "total_fields": 13,
    "required_fields_count": 3,
    "fields_with_defaults_count": 11,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
