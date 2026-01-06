"""Validation helpers for authentication/scheme - Auto-generated"""

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
    "method",  # Authentication methods (default = basic).
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "method": "",
    "negotiate-ntlm": "enable",
    "kerberos-keytab": "",
    "domain-controller": "",
    "saml-server": "",
    "saml-timeout": 120,
    "fsso-agent-for-ntlm": "",
    "require-tfa": "disable",
    "fsso-guest": "disable",
    "user-cert": "disable",
    "cert-http-header": "disable",
    "ssh-ca": "",
    "external-idp": "",
    "group-attr-type": "display-name",
    "digest-algo": "md5 sha-256",
    "digest-rfc2069": "disable",
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
    "name": "string",  # Authentication scheme name.
    "method": "option",  # Authentication methods (default = basic).
    "negotiate-ntlm": "option",  # Enable/disable negotiate authentication for NTLM (default = 
    "kerberos-keytab": "string",  # Kerberos keytab setting.
    "domain-controller": "string",  # Domain controller setting.
    "saml-server": "string",  # SAML configuration.
    "saml-timeout": "integer",  # SAML authentication timeout in seconds.
    "fsso-agent-for-ntlm": "string",  # FSSO agent to use for NTLM authentication.
    "require-tfa": "option",  # Enable/disable two-factor authentication (default = disable)
    "fsso-guest": "option",  # Enable/disable user fsso-guest authentication (default = dis
    "user-cert": "option",  # Enable/disable authentication with user certificate (default
    "cert-http-header": "option",  # Enable/disable authentication with user certificate in Clien
    "user-database": "string",  # Authentication server to contain user information; "local-us
    "ssh-ca": "string",  # SSH CA name.
    "external-idp": "string",  # External identity provider configuration.
    "group-attr-type": "option",  # Group attribute type used to match SCIM groups (default = di
    "digest-algo": "option",  # Digest Authentication Algorithms.
    "digest-rfc2069": "option",  # Enable/disable support for the deprecated RFC2069 Digest Cli
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Authentication scheme name.",
    "method": "Authentication methods (default = basic).",
    "negotiate-ntlm": "Enable/disable negotiate authentication for NTLM (default = disable).",
    "kerberos-keytab": "Kerberos keytab setting.",
    "domain-controller": "Domain controller setting.",
    "saml-server": "SAML configuration.",
    "saml-timeout": "SAML authentication timeout in seconds.",
    "fsso-agent-for-ntlm": "FSSO agent to use for NTLM authentication.",
    "require-tfa": "Enable/disable two-factor authentication (default = disable).",
    "fsso-guest": "Enable/disable user fsso-guest authentication (default = disable).",
    "user-cert": "Enable/disable authentication with user certificate (default = disable).",
    "cert-http-header": "Enable/disable authentication with user certificate in Client-Cert HTTP header (default = disable).",
    "user-database": "Authentication server to contain user information; \"local-user-db\" (default) or \"123\" (for LDAP).",
    "ssh-ca": "SSH CA name.",
    "external-idp": "External identity provider configuration.",
    "group-attr-type": "Group attribute type used to match SCIM groups (default = display-name).",
    "digest-algo": "Digest Authentication Algorithms.",
    "digest-rfc2069": "Enable/disable support for the deprecated RFC2069 Digest Client (no cnonce field, default = disable).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "kerberos-keytab": {"type": "string", "max_length": 35},
    "domain-controller": {"type": "string", "max_length": 35},
    "saml-server": {"type": "string", "max_length": 35},
    "saml-timeout": {"type": "integer", "min": 30, "max": 1200},
    "fsso-agent-for-ntlm": {"type": "string", "max_length": 35},
    "ssh-ca": {"type": "string", "max_length": 35},
    "external-idp": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "user-database": {
        "name": {
            "type": "string",
            "help": "Authentication server name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_METHOD = [
    "ntlm",  # NTLM authentication.
    "basic",  # Basic HTTP authentication.
    "digest",  # Digest HTTP authentication.
    "form",  # Form-based HTTP authentication.
    "negotiate",  # Negotiate authentication.
    "fsso",  # Fortinet Single Sign-On (FSSO) authentication.
    "rsso",  # RADIUS Single Sign-On (RSSO) authentication.
    "ssh-publickey",  # Public key based SSH authentication.
    "cert",  # Client certificate authentication.
    "saml",  # SAML authentication.
    "entra-sso",  # Entra ID based Single Sign-On (SSO) authentication.
]
VALID_BODY_NEGOTIATE_NTLM = [
    "enable",  # Enable negotiate authentication for NTLM.
    "disable",  # Disable negotiate authentication for NTLM.
]
VALID_BODY_REQUIRE_TFA = [
    "enable",  # Enable two-factor authentication.
    "disable",  # Disable two-factor authentication.
]
VALID_BODY_FSSO_GUEST = [
    "enable",  # Enable user fsso-guest authentication.
    "disable",  # Disable user fsso-guest authentication.
]
VALID_BODY_USER_CERT = [
    "enable",  # Enable client certificate field authentication.
    "disable",  # Disable client certificate field authentication.
]
VALID_BODY_CERT_HTTP_HEADER = [
    "enable",  # Enable client certificate authentication with HTTP header (RFC9440).
    "disable",  # Disable client certificate authentication with HTTP header (RFC9440).
]
VALID_BODY_GROUP_ATTR_TYPE = [
    "display-name",  # Display name.
    "external-id",  # External ID.
]
VALID_BODY_DIGEST_ALGO = [
    "md5",  # MD5.
    "sha-256",  # SHA-256.
]
VALID_BODY_DIGEST_RFC2069 = [
    "enable",  # Enable support for the deprecated RFC2069 Digest Client (no cnonce field).
    "disable",  # Disable support for the deprecated RFC2069 Digest Client (no cnonce field).
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_authentication_scheme_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for authentication/scheme."""
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
    """Validate required fields for authentication/scheme."""
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


def validate_authentication_scheme_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new authentication/scheme object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "method" in payload:
        value = payload["method"]
        if value not in VALID_BODY_METHOD:
            desc = FIELD_DESCRIPTIONS.get("method", "")
            error_msg = f"Invalid value for 'method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_METHOD)}"
            error_msg += f"\n  → Example: method='{{ VALID_BODY_METHOD[0] }}'"
            return (False, error_msg)
    if "negotiate-ntlm" in payload:
        value = payload["negotiate-ntlm"]
        if value not in VALID_BODY_NEGOTIATE_NTLM:
            desc = FIELD_DESCRIPTIONS.get("negotiate-ntlm", "")
            error_msg = f"Invalid value for 'negotiate-ntlm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NEGOTIATE_NTLM)}"
            error_msg += f"\n  → Example: negotiate-ntlm='{{ VALID_BODY_NEGOTIATE_NTLM[0] }}'"
            return (False, error_msg)
    if "require-tfa" in payload:
        value = payload["require-tfa"]
        if value not in VALID_BODY_REQUIRE_TFA:
            desc = FIELD_DESCRIPTIONS.get("require-tfa", "")
            error_msg = f"Invalid value for 'require-tfa': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REQUIRE_TFA)}"
            error_msg += f"\n  → Example: require-tfa='{{ VALID_BODY_REQUIRE_TFA[0] }}'"
            return (False, error_msg)
    if "fsso-guest" in payload:
        value = payload["fsso-guest"]
        if value not in VALID_BODY_FSSO_GUEST:
            desc = FIELD_DESCRIPTIONS.get("fsso-guest", "")
            error_msg = f"Invalid value for 'fsso-guest': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FSSO_GUEST)}"
            error_msg += f"\n  → Example: fsso-guest='{{ VALID_BODY_FSSO_GUEST[0] }}'"
            return (False, error_msg)
    if "user-cert" in payload:
        value = payload["user-cert"]
        if value not in VALID_BODY_USER_CERT:
            desc = FIELD_DESCRIPTIONS.get("user-cert", "")
            error_msg = f"Invalid value for 'user-cert': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USER_CERT)}"
            error_msg += f"\n  → Example: user-cert='{{ VALID_BODY_USER_CERT[0] }}'"
            return (False, error_msg)
    if "cert-http-header" in payload:
        value = payload["cert-http-header"]
        if value not in VALID_BODY_CERT_HTTP_HEADER:
            desc = FIELD_DESCRIPTIONS.get("cert-http-header", "")
            error_msg = f"Invalid value for 'cert-http-header': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CERT_HTTP_HEADER)}"
            error_msg += f"\n  → Example: cert-http-header='{{ VALID_BODY_CERT_HTTP_HEADER[0] }}'"
            return (False, error_msg)
    if "group-attr-type" in payload:
        value = payload["group-attr-type"]
        if value not in VALID_BODY_GROUP_ATTR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("group-attr-type", "")
            error_msg = f"Invalid value for 'group-attr-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GROUP_ATTR_TYPE)}"
            error_msg += f"\n  → Example: group-attr-type='{{ VALID_BODY_GROUP_ATTR_TYPE[0] }}'"
            return (False, error_msg)
    if "digest-algo" in payload:
        value = payload["digest-algo"]
        if value not in VALID_BODY_DIGEST_ALGO:
            desc = FIELD_DESCRIPTIONS.get("digest-algo", "")
            error_msg = f"Invalid value for 'digest-algo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIGEST_ALGO)}"
            error_msg += f"\n  → Example: digest-algo='{{ VALID_BODY_DIGEST_ALGO[0] }}'"
            return (False, error_msg)
    if "digest-rfc2069" in payload:
        value = payload["digest-rfc2069"]
        if value not in VALID_BODY_DIGEST_RFC2069:
            desc = FIELD_DESCRIPTIONS.get("digest-rfc2069", "")
            error_msg = f"Invalid value for 'digest-rfc2069': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIGEST_RFC2069)}"
            error_msg += f"\n  → Example: digest-rfc2069='{{ VALID_BODY_DIGEST_RFC2069[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_authentication_scheme_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update authentication/scheme."""
    # Step 1: Validate enum values
    if "method" in payload:
        value = payload["method"]
        if value not in VALID_BODY_METHOD:
            return (
                False,
                f"Invalid value for 'method'='{value}'. Must be one of: {', '.join(VALID_BODY_METHOD)}",
            )
    if "negotiate-ntlm" in payload:
        value = payload["negotiate-ntlm"]
        if value not in VALID_BODY_NEGOTIATE_NTLM:
            return (
                False,
                f"Invalid value for 'negotiate-ntlm'='{value}'. Must be one of: {', '.join(VALID_BODY_NEGOTIATE_NTLM)}",
            )
    if "require-tfa" in payload:
        value = payload["require-tfa"]
        if value not in VALID_BODY_REQUIRE_TFA:
            return (
                False,
                f"Invalid value for 'require-tfa'='{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_TFA)}",
            )
    if "fsso-guest" in payload:
        value = payload["fsso-guest"]
        if value not in VALID_BODY_FSSO_GUEST:
            return (
                False,
                f"Invalid value for 'fsso-guest'='{value}'. Must be one of: {', '.join(VALID_BODY_FSSO_GUEST)}",
            )
    if "user-cert" in payload:
        value = payload["user-cert"]
        if value not in VALID_BODY_USER_CERT:
            return (
                False,
                f"Invalid value for 'user-cert'='{value}'. Must be one of: {', '.join(VALID_BODY_USER_CERT)}",
            )
    if "cert-http-header" in payload:
        value = payload["cert-http-header"]
        if value not in VALID_BODY_CERT_HTTP_HEADER:
            return (
                False,
                f"Invalid value for 'cert-http-header'='{value}'. Must be one of: {', '.join(VALID_BODY_CERT_HTTP_HEADER)}",
            )
    if "group-attr-type" in payload:
        value = payload["group-attr-type"]
        if value not in VALID_BODY_GROUP_ATTR_TYPE:
            return (
                False,
                f"Invalid value for 'group-attr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_ATTR_TYPE)}",
            )
    if "digest-algo" in payload:
        value = payload["digest-algo"]
        if value not in VALID_BODY_DIGEST_ALGO:
            return (
                False,
                f"Invalid value for 'digest-algo'='{value}'. Must be one of: {', '.join(VALID_BODY_DIGEST_ALGO)}",
            )
    if "digest-rfc2069" in payload:
        value = payload["digest-rfc2069"]
        if value not in VALID_BODY_DIGEST_RFC2069:
            return (
                False,
                f"Invalid value for 'digest-rfc2069'='{value}'. Must be one of: {', '.join(VALID_BODY_DIGEST_RFC2069)}",
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
    "endpoint": "authentication/scheme",
    "category": "cmdb",
    "api_path": "authentication/scheme",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure Authentication Schemes.",
    "total_fields": 18,
    "required_fields_count": 1,
    "fields_with_defaults_count": 17,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
