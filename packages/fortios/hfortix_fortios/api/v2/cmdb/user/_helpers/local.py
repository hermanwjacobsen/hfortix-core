"""Validation helpers for user/local - Auto-generated"""

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
    "passwd",  # User's password.
    "ldap-server",  # Name of LDAP server with which the user must authenticate.
    "radius-server",  # Name of RADIUS server with which the user must authenticate.
    "tacacs+-server",  # Name of TACACS+ server with which the user must authenticate.
    "saml-server",  # Name of SAML server with which the user must authenticate.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "id": 0,
    "status": "enable",
    "type": "password",
    "ldap-server": "",
    "radius-server": "",
    "tacacs+-server": "",
    "saml-server": "",
    "two-factor": "disable",
    "two-factor-authentication": "",
    "two-factor-notification": "",
    "fortitoken": "",
    "email-to": "",
    "sms-server": "fortiguard",
    "sms-custom-server": "",
    "sms-phone": "",
    "passwd-policy": "",
    "passwd-time": "",
    "authtimeout": 0,
    "workstation": "",
    "auth-concurrent-override": "disable",
    "auth-concurrent-value": 0,
    "ppk-identity": "",
    "qkd-profile": "",
    "username-sensitivity": "enable",
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
    "name": "string",  # Local user name.
    "id": "integer",  # User ID.
    "status": "option",  # Enable/disable allowing the local user to authenticate with 
    "type": "option",  # Authentication method.
    "passwd": "password",  # User's password.
    "ldap-server": "string",  # Name of LDAP server with which the user must authenticate.
    "radius-server": "string",  # Name of RADIUS server with which the user must authenticate.
    "tacacs+-server": "string",  # Name of TACACS+ server with which the user must authenticate
    "saml-server": "string",  # Name of SAML server with which the user must authenticate.
    "two-factor": "option",  # Enable/disable two-factor authentication.
    "two-factor-authentication": "option",  # Authentication method by FortiToken Cloud.
    "two-factor-notification": "option",  # Notification method for user activation by FortiToken Cloud.
    "fortitoken": "string",  # Two-factor recipient's FortiToken serial number.
    "email-to": "string",  # Two-factor recipient's email address.
    "sms-server": "option",  # Send SMS through FortiGuard or other external server.
    "sms-custom-server": "string",  # Two-factor recipient's SMS server.
    "sms-phone": "string",  # Two-factor recipient's mobile phone number.
    "passwd-policy": "string",  # Password policy to apply to this user, as defined in config 
    "passwd-time": "user",  # Time of the last password update.
    "authtimeout": "integer",  # Time in minutes before the authentication timeout for a user
    "workstation": "string",  # Name of the remote user workstation, if you want to limit th
    "auth-concurrent-override": "option",  # Enable/disable overriding the policy-auth-concurrent under c
    "auth-concurrent-value": "integer",  # Maximum number of concurrent logins permitted from the same 
    "ppk-secret": "password-3",  # IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal
    "ppk-identity": "string",  # IKEv2 Postquantum Preshared Key Identity.
    "qkd-profile": "string",  # Quantum Key Distribution (QKD) profile.
    "username-sensitivity": "option",  # Enable/disable case and accent sensitivity when performing u
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Local user name.",
    "id": "User ID.",
    "status": "Enable/disable allowing the local user to authenticate with the FortiGate unit.",
    "type": "Authentication method.",
    "passwd": "User's password.",
    "ldap-server": "Name of LDAP server with which the user must authenticate.",
    "radius-server": "Name of RADIUS server with which the user must authenticate.",
    "tacacs+-server": "Name of TACACS+ server with which the user must authenticate.",
    "saml-server": "Name of SAML server with which the user must authenticate.",
    "two-factor": "Enable/disable two-factor authentication.",
    "two-factor-authentication": "Authentication method by FortiToken Cloud.",
    "two-factor-notification": "Notification method for user activation by FortiToken Cloud.",
    "fortitoken": "Two-factor recipient's FortiToken serial number.",
    "email-to": "Two-factor recipient's email address.",
    "sms-server": "Send SMS through FortiGuard or other external server.",
    "sms-custom-server": "Two-factor recipient's SMS server.",
    "sms-phone": "Two-factor recipient's mobile phone number.",
    "passwd-policy": "Password policy to apply to this user, as defined in config user password-policy.",
    "passwd-time": "Time of the last password update.",
    "authtimeout": "Time in minutes before the authentication timeout for a user is reached.",
    "workstation": "Name of the remote user workstation, if you want to limit the user to authenticate only from a particular workstation.",
    "auth-concurrent-override": "Enable/disable overriding the policy-auth-concurrent under config system global.",
    "auth-concurrent-value": "Maximum number of concurrent logins permitted from the same user.",
    "ppk-secret": "IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x).",
    "ppk-identity": "IKEv2 Postquantum Preshared Key Identity.",
    "qkd-profile": "Quantum Key Distribution (QKD) profile.",
    "username-sensitivity": "Enable/disable case and accent sensitivity when performing username matching (accents are stripped and case is ignored when disabled).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 64},
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "ldap-server": {"type": "string", "max_length": 35},
    "radius-server": {"type": "string", "max_length": 35},
    "tacacs+-server": {"type": "string", "max_length": 35},
    "saml-server": {"type": "string", "max_length": 35},
    "fortitoken": {"type": "string", "max_length": 16},
    "email-to": {"type": "string", "max_length": 63},
    "sms-custom-server": {"type": "string", "max_length": 35},
    "sms-phone": {"type": "string", "max_length": 15},
    "passwd-policy": {"type": "string", "max_length": 35},
    "authtimeout": {"type": "integer", "min": 0, "max": 1440},
    "workstation": {"type": "string", "max_length": 35},
    "auth-concurrent-value": {"type": "integer", "min": 0, "max": 100},
    "ppk-identity": {"type": "string", "max_length": 35},
    "qkd-profile": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable user.
    "disable",  # Disable user.
]
VALID_BODY_TYPE = [
    "password",  # Password authentication.
    "radius",  # RADIUS server authentication.
    "tacacs+",  # TACACS+ server authentication.
    "ldap",  # LDAP server authentication.
    "saml",  # SAML server authentication.
]
VALID_BODY_TWO_FACTOR = [
    "disable",  # disable
    "fortitoken",  # FortiToken
    "fortitoken-cloud",  # FortiToken Cloud Service.
    "email",  # Email authentication code.
    "sms",  # SMS authentication code.
]
VALID_BODY_TWO_FACTOR_AUTHENTICATION = [
    "fortitoken",  # FortiToken authentication.
    "email",  # Email one time password.
    "sms",  # SMS one time password.
]
VALID_BODY_TWO_FACTOR_NOTIFICATION = [
    "email",  # Email notification for activation code.
    "sms",  # SMS notification for activation code.
]
VALID_BODY_SMS_SERVER = [
    "fortiguard",  # Send SMS by FortiGuard.
    "custom",  # Send SMS by custom server.
]
VALID_BODY_AUTH_CONCURRENT_OVERRIDE = [
    "enable",  # Enable auth-concurrent-override.
    "disable",  # Disable auth-concurrent-override.
]
VALID_BODY_USERNAME_SENSITIVITY = [
    "disable",  # Ignore case and accents. Username at prompt not required to match case or accents.
    "enable",  # Do not ignore case and accents. Username at prompt must be an exact match.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_local_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for user/local."""
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
    """Validate required fields for user/local."""
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


def validate_user_local_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new user/local object."""
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
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "two-factor" in payload:
        value = payload["two-factor"]
        if value not in VALID_BODY_TWO_FACTOR:
            desc = FIELD_DESCRIPTIONS.get("two-factor", "")
            error_msg = f"Invalid value for 'two-factor': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TWO_FACTOR)}"
            error_msg += f"\n  → Example: two-factor='{{ VALID_BODY_TWO_FACTOR[0] }}'"
            return (False, error_msg)
    if "two-factor-authentication" in payload:
        value = payload["two-factor-authentication"]
        if value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("two-factor-authentication", "")
            error_msg = f"Invalid value for 'two-factor-authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TWO_FACTOR_AUTHENTICATION)}"
            error_msg += f"\n  → Example: two-factor-authentication='{{ VALID_BODY_TWO_FACTOR_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "two-factor-notification" in payload:
        value = payload["two-factor-notification"]
        if value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            desc = FIELD_DESCRIPTIONS.get("two-factor-notification", "")
            error_msg = f"Invalid value for 'two-factor-notification': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TWO_FACTOR_NOTIFICATION)}"
            error_msg += f"\n  → Example: two-factor-notification='{{ VALID_BODY_TWO_FACTOR_NOTIFICATION[0] }}'"
            return (False, error_msg)
    if "sms-server" in payload:
        value = payload["sms-server"]
        if value not in VALID_BODY_SMS_SERVER:
            desc = FIELD_DESCRIPTIONS.get("sms-server", "")
            error_msg = f"Invalid value for 'sms-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SMS_SERVER)}"
            error_msg += f"\n  → Example: sms-server='{{ VALID_BODY_SMS_SERVER[0] }}'"
            return (False, error_msg)
    if "auth-concurrent-override" in payload:
        value = payload["auth-concurrent-override"]
        if value not in VALID_BODY_AUTH_CONCURRENT_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("auth-concurrent-override", "")
            error_msg = f"Invalid value for 'auth-concurrent-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_CONCURRENT_OVERRIDE)}"
            error_msg += f"\n  → Example: auth-concurrent-override='{{ VALID_BODY_AUTH_CONCURRENT_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "username-sensitivity" in payload:
        value = payload["username-sensitivity"]
        if value not in VALID_BODY_USERNAME_SENSITIVITY:
            desc = FIELD_DESCRIPTIONS.get("username-sensitivity", "")
            error_msg = f"Invalid value for 'username-sensitivity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USERNAME_SENSITIVITY)}"
            error_msg += f"\n  → Example: username-sensitivity='{{ VALID_BODY_USERNAME_SENSITIVITY[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_local_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update user/local."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "two-factor" in payload:
        value = payload["two-factor"]
        if value not in VALID_BODY_TWO_FACTOR:
            return (
                False,
                f"Invalid value for 'two-factor'='{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR)}",
            )
    if "two-factor-authentication" in payload:
        value = payload["two-factor-authentication"]
        if value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'two-factor-authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_AUTHENTICATION)}",
            )
    if "two-factor-notification" in payload:
        value = payload["two-factor-notification"]
        if value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            return (
                False,
                f"Invalid value for 'two-factor-notification'='{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_NOTIFICATION)}",
            )
    if "sms-server" in payload:
        value = payload["sms-server"]
        if value not in VALID_BODY_SMS_SERVER:
            return (
                False,
                f"Invalid value for 'sms-server'='{value}'. Must be one of: {', '.join(VALID_BODY_SMS_SERVER)}",
            )
    if "auth-concurrent-override" in payload:
        value = payload["auth-concurrent-override"]
        if value not in VALID_BODY_AUTH_CONCURRENT_OVERRIDE:
            return (
                False,
                f"Invalid value for 'auth-concurrent-override'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_CONCURRENT_OVERRIDE)}",
            )
    if "username-sensitivity" in payload:
        value = payload["username-sensitivity"]
        if value not in VALID_BODY_USERNAME_SENSITIVITY:
            return (
                False,
                f"Invalid value for 'username-sensitivity'='{value}'. Must be one of: {', '.join(VALID_BODY_USERNAME_SENSITIVITY)}",
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
    "endpoint": "user/local",
    "category": "cmdb",
    "api_path": "user/local",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure local users.",
    "total_fields": 27,
    "required_fields_count": 5,
    "fields_with_defaults_count": 25,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
