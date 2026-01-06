"""Validation helpers for user/group - Auto-generated"""

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
    "id": 0,
    "group-type": "firewall",
    "authtimeout": 0,
    "auth-concurrent-override": "disable",
    "auth-concurrent-value": 0,
    "http-digest-realm": "",
    "sso-attribute-value": "",
    "user-id": "email",
    "password": "auto-generate",
    "user-name": "disable",
    "sponsor": "optional",
    "company": "optional",
    "email": "enable",
    "mobile-phone": "disable",
    "sms-server": "fortiguard",
    "sms-custom-server": "",
    "expire-type": "immediately",
    "expire": 14400,
    "max-accounts": 0,
    "multiple-guest-add": "disable",
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
    "name": "string",  # Group name.
    "id": "integer",  # Group ID.
    "group-type": "option",  # Set the group to be for firewall authentication, FSSO, RSSO,
    "authtimeout": "integer",  # Authentication timeout in minutes for this user group. 0 to 
    "auth-concurrent-override": "option",  # Enable/disable overriding the global number of concurrent au
    "auth-concurrent-value": "integer",  # Maximum number of concurrent authenticated connections per u
    "http-digest-realm": "string",  # Realm attribute for MD5-digest authentication.
    "sso-attribute-value": "string",  # RADIUS attribute value.
    "member": "string",  # Names of users, peers, LDAP severs, RADIUS servers or extern
    "match": "string",  # Group matches.
    "user-id": "option",  # Guest user ID type.
    "password": "option",  # Guest user password type.
    "user-name": "option",  # Enable/disable the guest user name entry.
    "sponsor": "option",  # Set the action for the sponsor guest user field.
    "company": "option",  # Set the action for the company guest user field.
    "email": "option",  # Enable/disable the guest user email address field.
    "mobile-phone": "option",  # Enable/disable the guest user mobile phone number field.
    "sms-server": "option",  # Send SMS through FortiGuard or other external server.
    "sms-custom-server": "string",  # SMS server.
    "expire-type": "option",  # Determine when the expiration countdown begins.
    "expire": "integer",  # Time in seconds before guest user accounts expire (1 - 31536
    "max-accounts": "integer",  # Maximum number of guest accounts that can be created for thi
    "multiple-guest-add": "option",  # Enable/disable addition of multiple guests.
    "guest": "string",  # Guest User.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Group name.",
    "id": "Group ID.",
    "group-type": "Set the group to be for firewall authentication, FSSO, RSSO, or guest users.",
    "authtimeout": "Authentication timeout in minutes for this user group. 0 to use the global user setting auth-timeout.",
    "auth-concurrent-override": "Enable/disable overriding the global number of concurrent authentication sessions for this user group.",
    "auth-concurrent-value": "Maximum number of concurrent authenticated connections per user (0 - 100).",
    "http-digest-realm": "Realm attribute for MD5-digest authentication.",
    "sso-attribute-value": "RADIUS attribute value.",
    "member": "Names of users, peers, LDAP severs, RADIUS servers or external idp servers to add to the user group.",
    "match": "Group matches.",
    "user-id": "Guest user ID type.",
    "password": "Guest user password type.",
    "user-name": "Enable/disable the guest user name entry.",
    "sponsor": "Set the action for the sponsor guest user field.",
    "company": "Set the action for the company guest user field.",
    "email": "Enable/disable the guest user email address field.",
    "mobile-phone": "Enable/disable the guest user mobile phone number field.",
    "sms-server": "Send SMS through FortiGuard or other external server.",
    "sms-custom-server": "SMS server.",
    "expire-type": "Determine when the expiration countdown begins.",
    "expire": "Time in seconds before guest user accounts expire (1 - 31536000).",
    "max-accounts": "Maximum number of guest accounts that can be created for this group (0 means unlimited).",
    "multiple-guest-add": "Enable/disable addition of multiple guests.",
    "guest": "Guest User.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "authtimeout": {"type": "integer", "min": 0, "max": 43200},
    "auth-concurrent-value": {"type": "integer", "min": 0, "max": 100},
    "http-digest-realm": {"type": "string", "max_length": 35},
    "sso-attribute-value": {"type": "string", "max_length": 511},
    "sms-custom-server": {"type": "string", "max_length": 35},
    "expire": {"type": "integer", "min": 1, "max": 31536000},
    "max-accounts": {"type": "integer", "min": 0, "max": 500},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "member": {
        "name": {
            "type": "string",
            "help": "Group member name.",
            "required": True,
            "default": "",
            "max_length": 511,
        },
    },
    "match": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "server-name": {
            "type": "string",
            "help": "Name of remote auth server.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "group-name": {
            "type": "string",
            "help": "Name of matching user or group on remote authentication server or SCIM.",
            "required": True,
            "default": "",
            "max_length": 511,
        },
    },
    "guest": {
        "id": {
            "type": "integer",
            "help": "Guest ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "user-id": {
            "type": "string",
            "help": "Guest ID.",
            "default": "",
            "max_length": 64,
        },
        "name": {
            "type": "string",
            "help": "Guest name.",
            "default": "",
            "max_length": 64,
        },
        "password": {
            "type": "password",
            "help": "Guest password.",
            "max_length": 128,
        },
        "mobile-phone": {
            "type": "string",
            "help": "Mobile phone.",
            "default": "",
            "max_length": 35,
        },
        "sponsor": {
            "type": "string",
            "help": "Set the action for the sponsor guest user field.",
            "default": "",
            "max_length": 35,
        },
        "company": {
            "type": "string",
            "help": "Set the action for the company guest user field.",
            "default": "",
            "max_length": 35,
        },
        "email": {
            "type": "string",
            "help": "Email.",
            "default": "",
            "max_length": 64,
        },
        "expiration": {
            "type": "user",
            "help": "Expire time.",
            "default": "",
        },
        "comment": {
            "type": "var-string",
            "help": "Comment.",
            "max_length": 255,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_GROUP_TYPE = [
    "firewall",  # Firewall.
    "fsso-service",  # Fortinet Single Sign-On Service.
    "rsso",  # RADIUS based Single Sign-On Service.
    "guest",  # Guest.
]
VALID_BODY_AUTH_CONCURRENT_OVERRIDE = [
    "enable",  # Enable auth-concurrent-override.
    "disable",  # Disable auth-concurrent-override.
]
VALID_BODY_USER_ID = [
    "email",  # Email address.
    "auto-generate",  # Automatically generate.
    "specify",  # Specify.
]
VALID_BODY_PASSWORD = [
    "auto-generate",  # Automatically generate.
    "specify",  # Specify.
    "disable",  # Disable.
]
VALID_BODY_USER_NAME = [
    "disable",  # Disable setting.
    "enable",  # Enable setting.
]
VALID_BODY_SPONSOR = [
    "optional",  # Optional.
    "mandatory",  # Mandatory.
    "disabled",  # Disabled.
]
VALID_BODY_COMPANY = [
    "optional",  # Optional.
    "mandatory",  # Mandatory.
    "disabled",  # Disabled.
]
VALID_BODY_EMAIL = [
    "disable",  # Disable setting.
    "enable",  # Enable setting.
]
VALID_BODY_MOBILE_PHONE = [
    "disable",  # Disable setting.
    "enable",  # Enable setting.
]
VALID_BODY_SMS_SERVER = [
    "fortiguard",  # Send SMS by FortiGuard.
    "custom",  # Send SMS by custom server.
]
VALID_BODY_EXPIRE_TYPE = [
    "immediately",  # Immediately.
    "first-successful-login",  # First successful login.
]
VALID_BODY_MULTIPLE_GUEST_ADD = [
    "disable",  # Disable setting.
    "enable",  # Enable setting.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_group_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for user/group."""
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
    """Validate required fields for user/group."""
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


def validate_user_group_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new user/group object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "group-type" in payload:
        value = payload["group-type"]
        if value not in VALID_BODY_GROUP_TYPE:
            desc = FIELD_DESCRIPTIONS.get("group-type", "")
            error_msg = f"Invalid value for 'group-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GROUP_TYPE)}"
            error_msg += f"\n  → Example: group-type='{{ VALID_BODY_GROUP_TYPE[0] }}'"
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
    if "user-id" in payload:
        value = payload["user-id"]
        if value not in VALID_BODY_USER_ID:
            desc = FIELD_DESCRIPTIONS.get("user-id", "")
            error_msg = f"Invalid value for 'user-id': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USER_ID)}"
            error_msg += f"\n  → Example: user-id='{{ VALID_BODY_USER_ID[0] }}'"
            return (False, error_msg)
    if "password" in payload:
        value = payload["password"]
        if value not in VALID_BODY_PASSWORD:
            desc = FIELD_DESCRIPTIONS.get("password", "")
            error_msg = f"Invalid value for 'password': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PASSWORD)}"
            error_msg += f"\n  → Example: password='{{ VALID_BODY_PASSWORD[0] }}'"
            return (False, error_msg)
    if "user-name" in payload:
        value = payload["user-name"]
        if value not in VALID_BODY_USER_NAME:
            desc = FIELD_DESCRIPTIONS.get("user-name", "")
            error_msg = f"Invalid value for 'user-name': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USER_NAME)}"
            error_msg += f"\n  → Example: user-name='{{ VALID_BODY_USER_NAME[0] }}'"
            return (False, error_msg)
    if "sponsor" in payload:
        value = payload["sponsor"]
        if value not in VALID_BODY_SPONSOR:
            desc = FIELD_DESCRIPTIONS.get("sponsor", "")
            error_msg = f"Invalid value for 'sponsor': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPONSOR)}"
            error_msg += f"\n  → Example: sponsor='{{ VALID_BODY_SPONSOR[0] }}'"
            return (False, error_msg)
    if "company" in payload:
        value = payload["company"]
        if value not in VALID_BODY_COMPANY:
            desc = FIELD_DESCRIPTIONS.get("company", "")
            error_msg = f"Invalid value for 'company': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_COMPANY)}"
            error_msg += f"\n  → Example: company='{{ VALID_BODY_COMPANY[0] }}'"
            return (False, error_msg)
    if "email" in payload:
        value = payload["email"]
        if value not in VALID_BODY_EMAIL:
            desc = FIELD_DESCRIPTIONS.get("email", "")
            error_msg = f"Invalid value for 'email': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EMAIL)}"
            error_msg += f"\n  → Example: email='{{ VALID_BODY_EMAIL[0] }}'"
            return (False, error_msg)
    if "mobile-phone" in payload:
        value = payload["mobile-phone"]
        if value not in VALID_BODY_MOBILE_PHONE:
            desc = FIELD_DESCRIPTIONS.get("mobile-phone", "")
            error_msg = f"Invalid value for 'mobile-phone': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MOBILE_PHONE)}"
            error_msg += f"\n  → Example: mobile-phone='{{ VALID_BODY_MOBILE_PHONE[0] }}'"
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
    if "expire-type" in payload:
        value = payload["expire-type"]
        if value not in VALID_BODY_EXPIRE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("expire-type", "")
            error_msg = f"Invalid value for 'expire-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXPIRE_TYPE)}"
            error_msg += f"\n  → Example: expire-type='{{ VALID_BODY_EXPIRE_TYPE[0] }}'"
            return (False, error_msg)
    if "multiple-guest-add" in payload:
        value = payload["multiple-guest-add"]
        if value not in VALID_BODY_MULTIPLE_GUEST_ADD:
            desc = FIELD_DESCRIPTIONS.get("multiple-guest-add", "")
            error_msg = f"Invalid value for 'multiple-guest-add': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTIPLE_GUEST_ADD)}"
            error_msg += f"\n  → Example: multiple-guest-add='{{ VALID_BODY_MULTIPLE_GUEST_ADD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_group_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update user/group."""
    # Step 1: Validate enum values
    if "group-type" in payload:
        value = payload["group-type"]
        if value not in VALID_BODY_GROUP_TYPE:
            return (
                False,
                f"Invalid value for 'group-type'='{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_TYPE)}",
            )
    if "auth-concurrent-override" in payload:
        value = payload["auth-concurrent-override"]
        if value not in VALID_BODY_AUTH_CONCURRENT_OVERRIDE:
            return (
                False,
                f"Invalid value for 'auth-concurrent-override'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_CONCURRENT_OVERRIDE)}",
            )
    if "user-id" in payload:
        value = payload["user-id"]
        if value not in VALID_BODY_USER_ID:
            return (
                False,
                f"Invalid value for 'user-id'='{value}'. Must be one of: {', '.join(VALID_BODY_USER_ID)}",
            )
    if "password" in payload:
        value = payload["password"]
        if value not in VALID_BODY_PASSWORD:
            return (
                False,
                f"Invalid value for 'password'='{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD)}",
            )
    if "user-name" in payload:
        value = payload["user-name"]
        if value not in VALID_BODY_USER_NAME:
            return (
                False,
                f"Invalid value for 'user-name'='{value}'. Must be one of: {', '.join(VALID_BODY_USER_NAME)}",
            )
    if "sponsor" in payload:
        value = payload["sponsor"]
        if value not in VALID_BODY_SPONSOR:
            return (
                False,
                f"Invalid value for 'sponsor'='{value}'. Must be one of: {', '.join(VALID_BODY_SPONSOR)}",
            )
    if "company" in payload:
        value = payload["company"]
        if value not in VALID_BODY_COMPANY:
            return (
                False,
                f"Invalid value for 'company'='{value}'. Must be one of: {', '.join(VALID_BODY_COMPANY)}",
            )
    if "email" in payload:
        value = payload["email"]
        if value not in VALID_BODY_EMAIL:
            return (
                False,
                f"Invalid value for 'email'='{value}'. Must be one of: {', '.join(VALID_BODY_EMAIL)}",
            )
    if "mobile-phone" in payload:
        value = payload["mobile-phone"]
        if value not in VALID_BODY_MOBILE_PHONE:
            return (
                False,
                f"Invalid value for 'mobile-phone'='{value}'. Must be one of: {', '.join(VALID_BODY_MOBILE_PHONE)}",
            )
    if "sms-server" in payload:
        value = payload["sms-server"]
        if value not in VALID_BODY_SMS_SERVER:
            return (
                False,
                f"Invalid value for 'sms-server'='{value}'. Must be one of: {', '.join(VALID_BODY_SMS_SERVER)}",
            )
    if "expire-type" in payload:
        value = payload["expire-type"]
        if value not in VALID_BODY_EXPIRE_TYPE:
            return (
                False,
                f"Invalid value for 'expire-type'='{value}'. Must be one of: {', '.join(VALID_BODY_EXPIRE_TYPE)}",
            )
    if "multiple-guest-add" in payload:
        value = payload["multiple-guest-add"]
        if value not in VALID_BODY_MULTIPLE_GUEST_ADD:
            return (
                False,
                f"Invalid value for 'multiple-guest-add'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTIPLE_GUEST_ADD)}",
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
    "endpoint": "user/group",
    "category": "cmdb",
    "api_path": "user/group",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure user groups.",
    "total_fields": 24,
    "required_fields_count": 0,
    "fields_with_defaults_count": 21,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
