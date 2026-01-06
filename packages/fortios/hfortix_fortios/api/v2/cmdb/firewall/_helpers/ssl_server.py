"""Validation helpers for firewall/ssl_server - Auto-generated"""

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
    "ip": "0.0.0.0",
    "port": 443,
    "ssl-mode": "full",
    "add-header-x-forwarded-proto": "enable",
    "mapped-port": 80,
    "ssl-dh-bits": "2048",
    "ssl-algorithm": "high",
    "ssl-client-renegotiation": "allow",
    "ssl-min-version": "tls-1.1",
    "ssl-max-version": "tls-1.3",
    "ssl-send-empty-frags": "enable",
    "url-rewrite": "disable",
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
    "name": "string",  # Server name.
    "ip": "ipv4-address-any",  # IPv4 address of the SSL server.
    "port": "integer",  # Server service port (1 - 65535, default = 443).
    "ssl-mode": "option",  # SSL/TLS mode for encryption and decryption of traffic.
    "add-header-x-forwarded-proto": "option",  # Enable/disable adding an X-Forwarded-Proto header to forward
    "mapped-port": "integer",  # Mapped server service port (1 - 65535, default = 80).
    "ssl-cert": "string",  # List of certificate names to use for SSL connections to this
    "ssl-dh-bits": "option",  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    "ssl-algorithm": "option",  # Relative strength of encryption algorithms accepted in negot
    "ssl-client-renegotiation": "option",  # Allow or block client renegotiation by server.
    "ssl-min-version": "option",  # Lowest SSL/TLS version to negotiate.
    "ssl-max-version": "option",  # Highest SSL/TLS version to negotiate.
    "ssl-send-empty-frags": "option",  # Enable/disable sending empty fragments to avoid attack on CB
    "url-rewrite": "option",  # Enable/disable rewriting the URL.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Server name.",
    "ip": "IPv4 address of the SSL server.",
    "port": "Server service port (1 - 65535, default = 443).",
    "ssl-mode": "SSL/TLS mode for encryption and decryption of traffic.",
    "add-header-x-forwarded-proto": "Enable/disable adding an X-Forwarded-Proto header to forwarded requests.",
    "mapped-port": "Mapped server service port (1 - 65535, default = 80).",
    "ssl-cert": "List of certificate names to use for SSL connections to this server. (default = \"Fortinet_SSL\").",
    "ssl-dh-bits": "Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048).",
    "ssl-algorithm": "Relative strength of encryption algorithms accepted in negotiation.",
    "ssl-client-renegotiation": "Allow or block client renegotiation by server.",
    "ssl-min-version": "Lowest SSL/TLS version to negotiate.",
    "ssl-max-version": "Highest SSL/TLS version to negotiate.",
    "ssl-send-empty-frags": "Enable/disable sending empty fragments to avoid attack on CBC IV.",
    "url-rewrite": "Enable/disable rewriting the URL.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "port": {"type": "integer", "min": 1, "max": 65535},
    "mapped-port": {"type": "integer", "min": 1, "max": 65535},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "ssl-cert": {
        "name": {
            "type": "string",
            "help": "Certificate list.",
            "default": "Fortinet_SSL",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_SSL_MODE = [
    "half",  # Client to FortiGate SSL.
    "full",  # Client to FortiGate and FortiGate to Server SSL.
]
VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO = [
    "enable",  # Add X-Forwarded-Proto header.
    "disable",  # Do not add X-Forwarded-Proto header.
]
VALID_BODY_SSL_DH_BITS = [
    "768",  # 768-bit Diffie-Hellman prime.
    "1024",  # 1024-bit Diffie-Hellman prime.
    "1536",  # 1536-bit Diffie-Hellman prime.
    "2048",  # 2048-bit Diffie-Hellman prime.
]
VALID_BODY_SSL_ALGORITHM = [
    "high",  # High encryption. Allow only AES and ChaCha
    "medium",  # Medium encryption. Allow AES, ChaCha, 3DES, and RC4.
    "low",  # Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.
]
VALID_BODY_SSL_CLIENT_RENEGOTIATION = [
    "allow",  # Allow a SSL client to renegotiate.
    "deny",  # Abort any SSL connection that attempts to renegotiate.
    "secure",  # Reject any SSL connection that does not offer a RFC 5746 Secure Renegotiation Indication.
]
VALID_BODY_SSL_MIN_VERSION = [
    "tls-1.0",  # TLS 1.0.
    "tls-1.1",  # TLS 1.1.
    "tls-1.2",  # TLS 1.2.
    "tls-1.3",  # TLS 1.3.
]
VALID_BODY_SSL_MAX_VERSION = [
    "tls-1.0",  # TLS 1.0.
    "tls-1.1",  # TLS 1.1.
    "tls-1.2",  # TLS 1.2.
    "tls-1.3",  # TLS 1.3.
]
VALID_BODY_SSL_SEND_EMPTY_FRAGS = [
    "enable",  # Send empty fragments.
    "disable",  # Do not send empty fragments.
]
VALID_BODY_URL_REWRITE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_ssl_server_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/ssl_server."""
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
    """Validate required fields for firewall/ssl_server."""
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


def validate_firewall_ssl_server_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/ssl_server object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "ssl-mode" in payload:
        value = payload["ssl-mode"]
        if value not in VALID_BODY_SSL_MODE:
            desc = FIELD_DESCRIPTIONS.get("ssl-mode", "")
            error_msg = f"Invalid value for 'ssl-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MODE)}"
            error_msg += f"\n  → Example: ssl-mode='{{ VALID_BODY_SSL_MODE[0] }}'"
            return (False, error_msg)
    if "add-header-x-forwarded-proto" in payload:
        value = payload["add-header-x-forwarded-proto"]
        if value not in VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO:
            desc = FIELD_DESCRIPTIONS.get("add-header-x-forwarded-proto", "")
            error_msg = f"Invalid value for 'add-header-x-forwarded-proto': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO)}"
            error_msg += f"\n  → Example: add-header-x-forwarded-proto='{{ VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO[0] }}'"
            return (False, error_msg)
    if "ssl-dh-bits" in payload:
        value = payload["ssl-dh-bits"]
        if value not in VALID_BODY_SSL_DH_BITS:
            desc = FIELD_DESCRIPTIONS.get("ssl-dh-bits", "")
            error_msg = f"Invalid value for 'ssl-dh-bits': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_DH_BITS)}"
            error_msg += f"\n  → Example: ssl-dh-bits='{{ VALID_BODY_SSL_DH_BITS[0] }}'"
            return (False, error_msg)
    if "ssl-algorithm" in payload:
        value = payload["ssl-algorithm"]
        if value not in VALID_BODY_SSL_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("ssl-algorithm", "")
            error_msg = f"Invalid value for 'ssl-algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_ALGORITHM)}"
            error_msg += f"\n  → Example: ssl-algorithm='{{ VALID_BODY_SSL_ALGORITHM[0] }}'"
            return (False, error_msg)
    if "ssl-client-renegotiation" in payload:
        value = payload["ssl-client-renegotiation"]
        if value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            desc = FIELD_DESCRIPTIONS.get("ssl-client-renegotiation", "")
            error_msg = f"Invalid value for 'ssl-client-renegotiation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_CLIENT_RENEGOTIATION)}"
            error_msg += f"\n  → Example: ssl-client-renegotiation='{{ VALID_BODY_SSL_CLIENT_RENEGOTIATION[0] }}'"
            return (False, error_msg)
    if "ssl-min-version" in payload:
        value = payload["ssl-min-version"]
        if value not in VALID_BODY_SSL_MIN_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-min-version", "")
            error_msg = f"Invalid value for 'ssl-min-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MIN_VERSION)}"
            error_msg += f"\n  → Example: ssl-min-version='{{ VALID_BODY_SSL_MIN_VERSION[0] }}'"
            return (False, error_msg)
    if "ssl-max-version" in payload:
        value = payload["ssl-max-version"]
        if value not in VALID_BODY_SSL_MAX_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-max-version", "")
            error_msg = f"Invalid value for 'ssl-max-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MAX_VERSION)}"
            error_msg += f"\n  → Example: ssl-max-version='{{ VALID_BODY_SSL_MAX_VERSION[0] }}'"
            return (False, error_msg)
    if "ssl-send-empty-frags" in payload:
        value = payload["ssl-send-empty-frags"]
        if value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            desc = FIELD_DESCRIPTIONS.get("ssl-send-empty-frags", "")
            error_msg = f"Invalid value for 'ssl-send-empty-frags': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_SEND_EMPTY_FRAGS)}"
            error_msg += f"\n  → Example: ssl-send-empty-frags='{{ VALID_BODY_SSL_SEND_EMPTY_FRAGS[0] }}'"
            return (False, error_msg)
    if "url-rewrite" in payload:
        value = payload["url-rewrite"]
        if value not in VALID_BODY_URL_REWRITE:
            desc = FIELD_DESCRIPTIONS.get("url-rewrite", "")
            error_msg = f"Invalid value for 'url-rewrite': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_URL_REWRITE)}"
            error_msg += f"\n  → Example: url-rewrite='{{ VALID_BODY_URL_REWRITE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_ssl_server_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/ssl_server."""
    # Step 1: Validate enum values
    if "ssl-mode" in payload:
        value = payload["ssl-mode"]
        if value not in VALID_BODY_SSL_MODE:
            return (
                False,
                f"Invalid value for 'ssl-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MODE)}",
            )
    if "add-header-x-forwarded-proto" in payload:
        value = payload["add-header-x-forwarded-proto"]
        if value not in VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO:
            return (
                False,
                f"Invalid value for 'add-header-x-forwarded-proto'='{value}'. Must be one of: {', '.join(VALID_BODY_ADD_HEADER_X_FORWARDED_PROTO)}",
            )
    if "ssl-dh-bits" in payload:
        value = payload["ssl-dh-bits"]
        if value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid value for 'ssl-dh-bits'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )
    if "ssl-algorithm" in payload:
        value = payload["ssl-algorithm"]
        if value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid value for 'ssl-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )
    if "ssl-client-renegotiation" in payload:
        value = payload["ssl-client-renegotiation"]
        if value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            return (
                False,
                f"Invalid value for 'ssl-client-renegotiation'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_RENEGOTIATION)}",
            )
    if "ssl-min-version" in payload:
        value = payload["ssl-min-version"]
        if value not in VALID_BODY_SSL_MIN_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-min-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_VERSION)}",
            )
    if "ssl-max-version" in payload:
        value = payload["ssl-max-version"]
        if value not in VALID_BODY_SSL_MAX_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-max-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MAX_VERSION)}",
            )
    if "ssl-send-empty-frags" in payload:
        value = payload["ssl-send-empty-frags"]
        if value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            return (
                False,
                f"Invalid value for 'ssl-send-empty-frags'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SEND_EMPTY_FRAGS)}",
            )
    if "url-rewrite" in payload:
        value = payload["url-rewrite"]
        if value not in VALID_BODY_URL_REWRITE:
            return (
                False,
                f"Invalid value for 'url-rewrite'='{value}'. Must be one of: {', '.join(VALID_BODY_URL_REWRITE)}",
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
    "endpoint": "firewall/ssl_server",
    "category": "cmdb",
    "api_path": "firewall/ssl-server",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure SSL servers.",
    "total_fields": 14,
    "required_fields_count": 0,
    "fields_with_defaults_count": 13,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
