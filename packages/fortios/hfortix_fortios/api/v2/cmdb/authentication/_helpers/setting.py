"""Validation helpers for authentication/setting - Auto-generated"""

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
    "active-auth-scheme": "",
    "sso-auth-scheme": "",
    "update-time": "",
    "persistent-cookie": "enable",
    "ip-auth-cookie": "disable",
    "cookie-max-age": 480,
    "cookie-refresh-div": 2,
    "captive-portal-type": "fqdn",
    "captive-portal-ip": "0.0.0.0",
    "captive-portal-ip6": "::",
    "captive-portal": "",
    "captive-portal6": "",
    "cert-auth": "disable",
    "cert-captive-portal": "",
    "cert-captive-portal-ip": "0.0.0.0",
    "cert-captive-portal-port": 7832,
    "captive-portal-port": 7830,
    "auth-https": "enable",
    "captive-portal-ssl-port": 7831,
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
    "active-auth-scheme": "string",  # Active authentication method (scheme name).
    "sso-auth-scheme": "string",  # Single-Sign-On authentication method (scheme name).
    "update-time": "user",  # Time of the last update.
    "persistent-cookie": "option",  # Enable/disable persistent cookie on web portal authenticatio
    "ip-auth-cookie": "option",  # Enable/disable persistent cookie on IP based web portal auth
    "cookie-max-age": "integer",  # Persistent web portal cookie maximum age in minutes (30 - 10
    "cookie-refresh-div": "integer",  # Refresh rate divider of persistent web portal cookie (defaul
    "captive-portal-type": "option",  # Captive portal type.
    "captive-portal-ip": "ipv4-address-any",  # Captive portal IP address.
    "captive-portal-ip6": "ipv6-address",  # Captive portal IPv6 address.
    "captive-portal": "string",  # Captive portal host name.
    "captive-portal6": "string",  # IPv6 captive portal host name.
    "cert-auth": "option",  # Enable/disable redirecting certificate authentication to HTT
    "cert-captive-portal": "string",  # Certificate captive portal host name.
    "cert-captive-portal-ip": "ipv4-address-any",  # Certificate captive portal IP address.
    "cert-captive-portal-port": "integer",  # Certificate captive portal port number (1 - 65535, default =
    "captive-portal-port": "integer",  # Captive portal port number (1 - 65535, default = 7830).
    "auth-https": "option",  # Enable/disable redirecting HTTP user authentication to HTTPS
    "captive-portal-ssl-port": "integer",  # Captive portal SSL port number (1 - 65535, default = 7831).
    "user-cert-ca": "string",  # CA certificate used for client certificate verification.
    "dev-range": "string",  # Address range for the IP based device query.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "active-auth-scheme": "Active authentication method (scheme name).",
    "sso-auth-scheme": "Single-Sign-On authentication method (scheme name).",
    "update-time": "Time of the last update.",
    "persistent-cookie": "Enable/disable persistent cookie on web portal authentication (default = enable).",
    "ip-auth-cookie": "Enable/disable persistent cookie on IP based web portal authentication (default = disable).",
    "cookie-max-age": "Persistent web portal cookie maximum age in minutes (30 - 10080 (1 week), default = 480 (8 hours)).",
    "cookie-refresh-div": "Refresh rate divider of persistent web portal cookie (default = 2). Refresh value = cookie-max-age/cookie-refresh-div.",
    "captive-portal-type": "Captive portal type.",
    "captive-portal-ip": "Captive portal IP address.",
    "captive-portal-ip6": "Captive portal IPv6 address.",
    "captive-portal": "Captive portal host name.",
    "captive-portal6": "IPv6 captive portal host name.",
    "cert-auth": "Enable/disable redirecting certificate authentication to HTTPS portal.",
    "cert-captive-portal": "Certificate captive portal host name.",
    "cert-captive-portal-ip": "Certificate captive portal IP address.",
    "cert-captive-portal-port": "Certificate captive portal port number (1 - 65535, default = 7832).",
    "captive-portal-port": "Captive portal port number (1 - 65535, default = 7830).",
    "auth-https": "Enable/disable redirecting HTTP user authentication to HTTPS.",
    "captive-portal-ssl-port": "Captive portal SSL port number (1 - 65535, default = 7831).",
    "user-cert-ca": "CA certificate used for client certificate verification.",
    "dev-range": "Address range for the IP based device query.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "active-auth-scheme": {"type": "string", "max_length": 35},
    "sso-auth-scheme": {"type": "string", "max_length": 35},
    "cookie-max-age": {"type": "integer", "min": 30, "max": 10080},
    "cookie-refresh-div": {"type": "integer", "min": 2, "max": 4},
    "captive-portal": {"type": "string", "max_length": 255},
    "captive-portal6": {"type": "string", "max_length": 255},
    "cert-captive-portal": {"type": "string", "max_length": 255},
    "cert-captive-portal-port": {"type": "integer", "min": 1, "max": 65535},
    "captive-portal-port": {"type": "integer", "min": 1, "max": 65535},
    "captive-portal-ssl-port": {"type": "integer", "min": 1, "max": 65535},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "user-cert-ca": {
        "name": {
            "type": "string",
            "help": "CA certificate list.",
            "default": "",
            "max_length": 79,
        },
    },
    "dev-range": {
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
VALID_BODY_PERSISTENT_COOKIE = [
    "enable",  # Enable persistent cookie.
    "disable",  # Disable persistent cookie.
]
VALID_BODY_IP_AUTH_COOKIE = [
    "enable",  # Enable persistent cookie for IP-based authentication.
    "disable",  # Disable persistent cookie for IP-based authentication.
]
VALID_BODY_CAPTIVE_PORTAL_TYPE = [
    "fqdn",  # Use FQDN for captive portal.
    "ip",  # Use an IP address for captive portal.
]
VALID_BODY_CERT_AUTH = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_AUTH_HTTPS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_authentication_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for authentication/setting."""
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
    """Validate required fields for authentication/setting."""
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


def validate_authentication_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new authentication/setting object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "persistent-cookie" in payload:
        value = payload["persistent-cookie"]
        if value not in VALID_BODY_PERSISTENT_COOKIE:
            desc = FIELD_DESCRIPTIONS.get("persistent-cookie", "")
            error_msg = f"Invalid value for 'persistent-cookie': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERSISTENT_COOKIE)}"
            error_msg += f"\n  → Example: persistent-cookie='{{ VALID_BODY_PERSISTENT_COOKIE[0] }}'"
            return (False, error_msg)
    if "ip-auth-cookie" in payload:
        value = payload["ip-auth-cookie"]
        if value not in VALID_BODY_IP_AUTH_COOKIE:
            desc = FIELD_DESCRIPTIONS.get("ip-auth-cookie", "")
            error_msg = f"Invalid value for 'ip-auth-cookie': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_AUTH_COOKIE)}"
            error_msg += f"\n  → Example: ip-auth-cookie='{{ VALID_BODY_IP_AUTH_COOKIE[0] }}'"
            return (False, error_msg)
    if "captive-portal-type" in payload:
        value = payload["captive-portal-type"]
        if value not in VALID_BODY_CAPTIVE_PORTAL_TYPE:
            desc = FIELD_DESCRIPTIONS.get("captive-portal-type", "")
            error_msg = f"Invalid value for 'captive-portal-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CAPTIVE_PORTAL_TYPE)}"
            error_msg += f"\n  → Example: captive-portal-type='{{ VALID_BODY_CAPTIVE_PORTAL_TYPE[0] }}'"
            return (False, error_msg)
    if "cert-auth" in payload:
        value = payload["cert-auth"]
        if value not in VALID_BODY_CERT_AUTH:
            desc = FIELD_DESCRIPTIONS.get("cert-auth", "")
            error_msg = f"Invalid value for 'cert-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CERT_AUTH)}"
            error_msg += f"\n  → Example: cert-auth='{{ VALID_BODY_CERT_AUTH[0] }}'"
            return (False, error_msg)
    if "auth-https" in payload:
        value = payload["auth-https"]
        if value not in VALID_BODY_AUTH_HTTPS:
            desc = FIELD_DESCRIPTIONS.get("auth-https", "")
            error_msg = f"Invalid value for 'auth-https': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_HTTPS)}"
            error_msg += f"\n  → Example: auth-https='{{ VALID_BODY_AUTH_HTTPS[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_authentication_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update authentication/setting."""
    # Step 1: Validate enum values
    if "persistent-cookie" in payload:
        value = payload["persistent-cookie"]
        if value not in VALID_BODY_PERSISTENT_COOKIE:
            return (
                False,
                f"Invalid value for 'persistent-cookie'='{value}'. Must be one of: {', '.join(VALID_BODY_PERSISTENT_COOKIE)}",
            )
    if "ip-auth-cookie" in payload:
        value = payload["ip-auth-cookie"]
        if value not in VALID_BODY_IP_AUTH_COOKIE:
            return (
                False,
                f"Invalid value for 'ip-auth-cookie'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_AUTH_COOKIE)}",
            )
    if "captive-portal-type" in payload:
        value = payload["captive-portal-type"]
        if value not in VALID_BODY_CAPTIVE_PORTAL_TYPE:
            return (
                False,
                f"Invalid value for 'captive-portal-type'='{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL_TYPE)}",
            )
    if "cert-auth" in payload:
        value = payload["cert-auth"]
        if value not in VALID_BODY_CERT_AUTH:
            return (
                False,
                f"Invalid value for 'cert-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_CERT_AUTH)}",
            )
    if "auth-https" in payload:
        value = payload["auth-https"]
        if value not in VALID_BODY_AUTH_HTTPS:
            return (
                False,
                f"Invalid value for 'auth-https'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_HTTPS)}",
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
    "endpoint": "authentication/setting",
    "category": "cmdb",
    "api_path": "authentication/setting",
    "help": "Configure authentication setting.",
    "total_fields": 21,
    "required_fields_count": 0,
    "fields_with_defaults_count": 19,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
