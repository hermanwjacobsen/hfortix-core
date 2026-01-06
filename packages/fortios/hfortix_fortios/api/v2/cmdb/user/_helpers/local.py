"""
Validation helpers for user/local endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification
Customize as needed for endpoint-specific business logic.
"""

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
#
# 1. FALSE POSITIVES: Some fields marked "required" have default values,
#    meaning they're optional (filtered out by generator)
#
# 2. CONDITIONAL REQUIREMENTS: Many endpoints require EITHER field A OR field B:
#    - firewall.policy: requires (srcaddr + dstaddr) OR (srcaddr6 + dstaddr6)
#    - These conditional requirements cannot be expressed in a simple list
#
# 3. SPECIALIZED FEATURES: Fields for WAN optimization, VPN, NAT64, etc.
#    are marked "required" but only apply when using those features
#
# The REQUIRED_FIELDS list below is INFORMATIONAL ONLY and shows fields that:
# - Are marked required in the schema
# - Don't have non-empty default values
# - Aren't specialized feature fields
#
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
    """
    Validate GET request parameters for user/local.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_user_local_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_user_local_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_user_local_get(
        ...     filters={"format": "name|type"}
        ... )
        >>> assert is_valid == True
    """
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
    """
    Validate required fields for user/local.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "test"}
        >>> is_valid, error = validate_required_fields(payload)
    """
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
    """
    Validate POST request to create new user/local object.

    This validator performs two-stage validation:
    1. Required fields check (schema-based)
    2. Field value validation (enums, ranges, formats)

    Args:
        payload: Request body data with configuration
        **params: Query parameters (vdom, etc.)

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if payload is valid, False otherwise
        - error_message: None if valid, detailed error string if invalid

    Examples:
        >>> # ✅ Valid - Minimal required fields
        >>> payload = {
        ...     "passwd": True,  # User's password.
        ...     "ldap-server": True,  # Name of LDAP server with which the user must authe
        ... }
        >>> is_valid, error = validate_user_local_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "passwd": True,
        ...     "status": "{'name': 'enable', 'help': 'Enable user.', 'label': 'Enable', 'description': 'Enable user'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_user_local_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_user_local_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_user_local_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
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
    """
    Validate PUT request to update user/local.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_user_local_put(payload)
    """
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
# Provide programmatic access to field metadata for IDE autocomplete,
# documentation generation, and dynamic validation
# ============================================================================


def get_field_description(field_name: str) -> str | None:
    """
    Get description/help text for a field.

    Args:
        field_name: Name of the field

    Returns:
        Description text or None if field doesn't exist

    Example:
        >>> desc = get_field_description("name")
        >>> print(desc)
    """
    return FIELD_DESCRIPTIONS.get(field_name)


def get_field_type(field_name: str) -> str | None:
    """
    Get the type of a field.

    Args:
        field_name: Name of the field

    Returns:
        Field type (e.g., "string", "integer", "option") or None

    Example:
        >>> field_type = get_field_type("status")
        >>> print(field_type)  # "option"
    """
    return FIELD_TYPES.get(field_name)


def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """
    Get constraints for a field (min/max values, string length).

    Args:
        field_name: Name of the field

    Returns:
        Constraint dict or None

    Example:
        >>> constraints = get_field_constraints("port")
        >>> print(constraints)  # {"type": "integer", "min": 1, "max": 65535}
    """
    return FIELD_CONSTRAINTS.get(field_name)


def get_field_default(field_name: str) -> Any | None:
    """
    Get default value for a field.

    Args:
        field_name: Name of the field

    Returns:
        Default value or None if no default

    Example:
        >>> default = get_field_default("status")
        >>> print(default)  # "enable"
    """
    return FIELDS_WITH_DEFAULTS.get(field_name)


def get_field_options(field_name: str) -> list[str] | None:
    """
    Get valid enum options for a field.

    Args:
        field_name: Name of the field

    Returns:
        List of valid values or None if not an enum field

    Example:
        >>> options = get_field_options("status")
        >>> print(options)  # ["enable", "disable"]
    """
    # Construct the constant name from field name
    # Replace all non-alphanumeric characters with underscores for valid Python identifiers
    import re
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', field_name)
    constant_name = f"VALID_BODY_{safe_name.upper()}"
    return globals().get(constant_name)


def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """
    Get schema for nested table/list fields.

    Args:
        field_name: Name of the parent field

    Returns:
        Dict mapping child field names to their metadata

    Example:
        >>> nested = get_nested_schema("members")
        >>> if nested:
        ...     for child_field, child_meta in nested.items():
        ...         print(f"{child_field}: {child_meta['type']}")
    """
    return NESTED_SCHEMAS.get(field_name)


def get_all_fields() -> list[str]:
    """
    Get list of all field names.

    Returns:
        List of all field names in the schema

    Example:
        >>> fields = get_all_fields()
        >>> print(len(fields))
    """
    return list(FIELD_TYPES.keys())


def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """
    Get complete metadata for a field (type, description, constraints, defaults, options).

    Args:
        field_name: Name of the field

    Returns:
        Dict with all available metadata or None if field doesn't exist

    Example:
        >>> meta = get_field_metadata("status")
        >>> print(meta)
        >>> # {
        >>> #   "type": "option",
        >>> #   "description": "Enable/disable this feature",
        >>> #   "default": "enable",
        >>> #   "options": ["enable", "disable"]
        >>> # }
    """
    if field_name not in FIELD_TYPES:
        return None

    metadata = {
        "name": field_name,
        "type": FIELD_TYPES[field_name],
    }

    # Add description if available
    if field_name in FIELD_DESCRIPTIONS:
        metadata["description"] = FIELD_DESCRIPTIONS[field_name]

    # Add constraints if available
    if field_name in FIELD_CONSTRAINTS:
        metadata["constraints"] = FIELD_CONSTRAINTS[field_name]

    # Add default if available
    if field_name in FIELDS_WITH_DEFAULTS:
        metadata["default"] = FIELDS_WITH_DEFAULTS[field_name]

    # Add required flag
    metadata["required"] = field_name in REQUIRED_FIELDS

    # Add options if available
    options = get_field_options(field_name)
    if options:
        metadata["options"] = options

    # Add nested schema if available
    nested = get_nested_schema(field_name)
    if nested:
        metadata["nested_schema"] = nested

    return metadata


def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """
    Validate a single field value against its constraints.

    Args:
        field_name: Name of the field
        value: Value to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_field_value("status", "enable")
        >>> if not is_valid:
        ...     print(error)
    """
    # Get field metadata
    field_type = get_field_type(field_name)
    if field_type is None:
        return (False, f"Unknown field: '{field_name}' (not defined in schema)")

    # Get field description for better error context
    description = get_field_description(field_name)

    # Validate enum values
    options = get_field_options(field_name)
    if options and value not in options:
        error_msg = f"Invalid value for '{field_name}': {repr(value)}"
        if description:
            error_msg += f"\n  → Description: {description}"
        error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in options)}"
        if options:
            error_msg += f"\n  → Example: {field_name}={repr(options[0])}"
        return (False, error_msg)

    # Validate constraints
    constraints = get_field_constraints(field_name)
    if constraints:
        constraint_type = constraints.get("type")

        if constraint_type == "integer":
            if not isinstance(value, int):
                error_msg = f"Field '{field_name}' must be an integer"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            min_val = constraints.get("min")
            max_val = constraints.get("max")

            if min_val is not None and value < min_val:
                error_msg = f"Field '{field_name}' value {value} is below minimum {min_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if max_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

            if max_val is not None and value > max_val:
                error_msg = f"Field '{field_name}' value {value} exceeds maximum {max_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if min_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

        elif constraint_type == "string":
            if not isinstance(value, str):
                error_msg = f"Field '{field_name}' must be a string"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            max_length = constraints.get("max_length")
            if max_length and len(value) > max_length:
                error_msg = f"Field '{field_name}' length {len(value)} exceeds maximum {max_length}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → Your value: {repr(value[:50])}{'...' if len(value) > 50 else ''}"
                return (False, error_msg)

    return (True, None)


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
    """
    Get information about this endpoint schema.

    Returns:
        Dict with schema metadata

    Example:
        >>> info = get_schema_info()
        >>> print(f"Endpoint: {info['endpoint']}")
        >>> print(f"Total fields: {info['total_fields']}")
    """
    return SCHEMA_INFO.copy()
