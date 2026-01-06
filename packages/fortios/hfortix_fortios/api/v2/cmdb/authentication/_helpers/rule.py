"""Validation helpers for authentication/rule - Auto-generated"""

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
    "status": "enable",
    "protocol": "http",
    "ip-based": "enable",
    "active-auth-method": "",
    "sso-auth-method": "",
    "web-auth-cookie": "disable",
    "cors-stateful": "disable",
    "cors-depth": 3,
    "cert-auth-cookie": "enable",
    "transaction-based": "disable",
    "web-portal": "enable",
    "session-logout": "disable",
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
    "name": "string",  # Authentication rule name.
    "status": "option",  # Enable/disable this authentication rule.
    "protocol": "option",  # Authentication is required for the selected protocol (defaul
    "srcintf": "string",  # Incoming (ingress) interface.
    "srcaddr": "string",  # Authentication is required for the selected IPv4 source addr
    "dstaddr": "string",  # Select an IPv4 destination address from available options. R
    "srcaddr6": "string",  # Authentication is required for the selected IPv6 source addr
    "dstaddr6": "string",  # Select an IPv6 destination address from available options. R
    "ip-based": "option",  # Enable/disable IP-based authentication. When enabled, previo
    "active-auth-method": "string",  # Select an active authentication method.
    "sso-auth-method": "string",  # Select a single-sign on (SSO) authentication method.
    "web-auth-cookie": "option",  # Enable/disable Web authentication cookies (default = disable
    "cors-stateful": "option",  # Enable/disable allowance of CORS access (default = disable).
    "cors-depth": "integer",  # Depth to allow CORS access (default = 3).
    "cert-auth-cookie": "option",  # Enable/disable to use device certificate as authentication c
    "transaction-based": "option",  # Enable/disable transaction based authentication (default = d
    "web-portal": "option",  # Enable/disable web portal for proxy transparent policy (defa
    "comments": "var-string",  # Comment.
    "session-logout": "option",  # Enable/disable logout of a user from the current session.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Authentication rule name.",
    "status": "Enable/disable this authentication rule.",
    "protocol": "Authentication is required for the selected protocol (default = HTTP).",
    "srcintf": "Incoming (ingress) interface.",
    "srcaddr": "Authentication is required for the selected IPv4 source address.",
    "dstaddr": "Select an IPv4 destination address from available options. Required for web proxy authentication.",
    "srcaddr6": "Authentication is required for the selected IPv6 source address.",
    "dstaddr6": "Select an IPv6 destination address from available options. Required for web proxy authentication.",
    "ip-based": "Enable/disable IP-based authentication. When enabled, previously authenticated users from the same IP address will be exempted.",
    "active-auth-method": "Select an active authentication method.",
    "sso-auth-method": "Select a single-sign on (SSO) authentication method.",
    "web-auth-cookie": "Enable/disable Web authentication cookies (default = disable).",
    "cors-stateful": "Enable/disable allowance of CORS access (default = disable).",
    "cors-depth": "Depth to allow CORS access (default = 3).",
    "cert-auth-cookie": "Enable/disable to use device certificate as authentication cookie (default = enable).",
    "transaction-based": "Enable/disable transaction based authentication (default = disable).",
    "web-portal": "Enable/disable web portal for proxy transparent policy (default = enable).",
    "comments": "Comment.",
    "session-logout": "Enable/disable logout of a user from the current session.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "active-auth-method": {"type": "string", "max_length": 35},
    "sso-auth-method": {"type": "string", "max_length": 35},
    "cors-depth": {"type": "integer", "min": 1, "max": 8},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "srcintf": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 79,
        },
    },
    "srcaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dstaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "srcaddr6": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dstaddr6": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable this authentication rule.
    "disable",  # Disable this authentication rule.
]
VALID_BODY_PROTOCOL = [
    "http",  # HTTP traffic is matched and authentication is required.
    "ftp",  # FTP traffic is matched and authentication is required.
    "socks",  # SOCKS traffic is matched and authentication is required.
    "ssh",  # SSH traffic is matched and authentication is required.
    "ztna-portal",  # ZTNA portal traffic is matched and authentication is required.
]
VALID_BODY_IP_BASED = [
    "enable",  # Enable IP-based authentication.
    "disable",  # Disable IP-based authentication.
]
VALID_BODY_WEB_AUTH_COOKIE = [
    "enable",  # Enable Web authentication cookie.
    "disable",  # Disable Web authentication cookie.
]
VALID_BODY_CORS_STATEFUL = [
    "enable",  # Enable allowance of CORS access
    "disable",  # Disable allowance of CORS access
]
VALID_BODY_CERT_AUTH_COOKIE = [
    "enable",  # Enable device certificate as authentication cookie.
    "disable",  # Disable device certificate as authentication cookie.
]
VALID_BODY_TRANSACTION_BASED = [
    "enable",  # Enable transaction based authentication.
    "disable",  # Disable transaction based authentication.
]
VALID_BODY_WEB_PORTAL = [
    "enable",  # Enable web-portal.
    "disable",  # Disable web-portal.
]
VALID_BODY_SESSION_LOGOUT = [
    "enable",  # Enable logout of a user from the current session.
    "disable",  # Disable logout of a user from the current session.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_authentication_rule_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for authentication/rule."""
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
    """Validate required fields for authentication/rule."""
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


def validate_authentication_rule_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new authentication/rule object."""
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
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("protocol", "")
            error_msg = f"Invalid value for 'protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROTOCOL)}"
            error_msg += f"\n  → Example: protocol='{{ VALID_BODY_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "ip-based" in payload:
        value = payload["ip-based"]
        if value not in VALID_BODY_IP_BASED:
            desc = FIELD_DESCRIPTIONS.get("ip-based", "")
            error_msg = f"Invalid value for 'ip-based': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_BASED)}"
            error_msg += f"\n  → Example: ip-based='{{ VALID_BODY_IP_BASED[0] }}'"
            return (False, error_msg)
    if "web-auth-cookie" in payload:
        value = payload["web-auth-cookie"]
        if value not in VALID_BODY_WEB_AUTH_COOKIE:
            desc = FIELD_DESCRIPTIONS.get("web-auth-cookie", "")
            error_msg = f"Invalid value for 'web-auth-cookie': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_AUTH_COOKIE)}"
            error_msg += f"\n  → Example: web-auth-cookie='{{ VALID_BODY_WEB_AUTH_COOKIE[0] }}'"
            return (False, error_msg)
    if "cors-stateful" in payload:
        value = payload["cors-stateful"]
        if value not in VALID_BODY_CORS_STATEFUL:
            desc = FIELD_DESCRIPTIONS.get("cors-stateful", "")
            error_msg = f"Invalid value for 'cors-stateful': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CORS_STATEFUL)}"
            error_msg += f"\n  → Example: cors-stateful='{{ VALID_BODY_CORS_STATEFUL[0] }}'"
            return (False, error_msg)
    if "cert-auth-cookie" in payload:
        value = payload["cert-auth-cookie"]
        if value not in VALID_BODY_CERT_AUTH_COOKIE:
            desc = FIELD_DESCRIPTIONS.get("cert-auth-cookie", "")
            error_msg = f"Invalid value for 'cert-auth-cookie': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CERT_AUTH_COOKIE)}"
            error_msg += f"\n  → Example: cert-auth-cookie='{{ VALID_BODY_CERT_AUTH_COOKIE[0] }}'"
            return (False, error_msg)
    if "transaction-based" in payload:
        value = payload["transaction-based"]
        if value not in VALID_BODY_TRANSACTION_BASED:
            desc = FIELD_DESCRIPTIONS.get("transaction-based", "")
            error_msg = f"Invalid value for 'transaction-based': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRANSACTION_BASED)}"
            error_msg += f"\n  → Example: transaction-based='{{ VALID_BODY_TRANSACTION_BASED[0] }}'"
            return (False, error_msg)
    if "web-portal" in payload:
        value = payload["web-portal"]
        if value not in VALID_BODY_WEB_PORTAL:
            desc = FIELD_DESCRIPTIONS.get("web-portal", "")
            error_msg = f"Invalid value for 'web-portal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_PORTAL)}"
            error_msg += f"\n  → Example: web-portal='{{ VALID_BODY_WEB_PORTAL[0] }}'"
            return (False, error_msg)
    if "session-logout" in payload:
        value = payload["session-logout"]
        if value not in VALID_BODY_SESSION_LOGOUT:
            desc = FIELD_DESCRIPTIONS.get("session-logout", "")
            error_msg = f"Invalid value for 'session-logout': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SESSION_LOGOUT)}"
            error_msg += f"\n  → Example: session-logout='{{ VALID_BODY_SESSION_LOGOUT[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_authentication_rule_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update authentication/rule."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "protocol" in payload:
        value = payload["protocol"]
        if value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid value for 'protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )
    if "ip-based" in payload:
        value = payload["ip-based"]
        if value not in VALID_BODY_IP_BASED:
            return (
                False,
                f"Invalid value for 'ip-based'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_BASED)}",
            )
    if "web-auth-cookie" in payload:
        value = payload["web-auth-cookie"]
        if value not in VALID_BODY_WEB_AUTH_COOKIE:
            return (
                False,
                f"Invalid value for 'web-auth-cookie'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_AUTH_COOKIE)}",
            )
    if "cors-stateful" in payload:
        value = payload["cors-stateful"]
        if value not in VALID_BODY_CORS_STATEFUL:
            return (
                False,
                f"Invalid value for 'cors-stateful'='{value}'. Must be one of: {', '.join(VALID_BODY_CORS_STATEFUL)}",
            )
    if "cert-auth-cookie" in payload:
        value = payload["cert-auth-cookie"]
        if value not in VALID_BODY_CERT_AUTH_COOKIE:
            return (
                False,
                f"Invalid value for 'cert-auth-cookie'='{value}'. Must be one of: {', '.join(VALID_BODY_CERT_AUTH_COOKIE)}",
            )
    if "transaction-based" in payload:
        value = payload["transaction-based"]
        if value not in VALID_BODY_TRANSACTION_BASED:
            return (
                False,
                f"Invalid value for 'transaction-based'='{value}'. Must be one of: {', '.join(VALID_BODY_TRANSACTION_BASED)}",
            )
    if "web-portal" in payload:
        value = payload["web-portal"]
        if value not in VALID_BODY_WEB_PORTAL:
            return (
                False,
                f"Invalid value for 'web-portal'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_PORTAL)}",
            )
    if "session-logout" in payload:
        value = payload["session-logout"]
        if value not in VALID_BODY_SESSION_LOGOUT:
            return (
                False,
                f"Invalid value for 'session-logout'='{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_LOGOUT)}",
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
    "endpoint": "authentication/rule",
    "category": "cmdb",
    "api_path": "authentication/rule",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure Authentication Rules.",
    "total_fields": 19,
    "required_fields_count": 0,
    "fields_with_defaults_count": 13,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
