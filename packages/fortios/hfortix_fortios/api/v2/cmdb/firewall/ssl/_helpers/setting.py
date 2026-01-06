"""Validation helpers for firewall/ssl/setting - Auto-generated"""

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
    "proxy-connect-timeout": 30,
    "ssl-dh-bits": "2048",
    "ssl-send-empty-frags": "enable",
    "no-matching-cipher-action": "bypass",
    "cert-manager-cache-timeout": 72,
    "resigned-short-lived-certificate": "enable",
    "cert-cache-capacity": 200,
    "cert-cache-timeout": 10,
    "session-cache-capacity": 500,
    "session-cache-timeout": 20,
    "abbreviate-handshake": "enable",
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
    "proxy-connect-timeout": "integer",  # Time limit to make an internal connection to the appropriate
    "ssl-dh-bits": "option",  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    "ssl-send-empty-frags": "option",  # Enable/disable sending empty fragments to avoid attack on CB
    "no-matching-cipher-action": "option",  # Bypass or drop the connection when no matching cipher is fou
    "cert-manager-cache-timeout": "integer",  # Time limit for certificate manager to keep FortiGate re-sign
    "resigned-short-lived-certificate": "option",  # Enable/disable short-lived certificate.
    "cert-cache-capacity": "integer",  # Maximum capacity of the host certificate cache (0 - 500, def
    "cert-cache-timeout": "integer",  # Time limit to keep certificate cache (1 - 120 min, default =
    "session-cache-capacity": "integer",  # Capacity of the SSL session cache (--Obsolete--) (1 - 1000, 
    "session-cache-timeout": "integer",  # Time limit to keep SSL session state (1 - 60 min, default = 
    "abbreviate-handshake": "option",  # Enable/disable use of SSL abbreviated handshake.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "proxy-connect-timeout": "Time limit to make an internal connection to the appropriate proxy process (1 - 60 sec, default = 30).",
    "ssl-dh-bits": "Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048).",
    "ssl-send-empty-frags": "Enable/disable sending empty fragments to avoid attack on CBC IV (for SSL 3.0 and TLS 1.0 only).",
    "no-matching-cipher-action": "Bypass or drop the connection when no matching cipher is found.",
    "cert-manager-cache-timeout": "Time limit for certificate manager to keep FortiGate re-signed server certificate (24 - 720 hours, default = 72).",
    "resigned-short-lived-certificate": "Enable/disable short-lived certificate.",
    "cert-cache-capacity": "Maximum capacity of the host certificate cache (0 - 500, default = 200).",
    "cert-cache-timeout": "Time limit to keep certificate cache (1 - 120 min, default = 10).",
    "session-cache-capacity": "Capacity of the SSL session cache (--Obsolete--) (1 - 1000, default = 500).",
    "session-cache-timeout": "Time limit to keep SSL session state (1 - 60 min, default = 20).",
    "abbreviate-handshake": "Enable/disable use of SSL abbreviated handshake.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "proxy-connect-timeout": {"type": "integer", "min": 1, "max": 60},
    "cert-manager-cache-timeout": {"type": "integer", "min": 24, "max": 720},
    "cert-cache-capacity": {"type": "integer", "min": 0, "max": 500},
    "cert-cache-timeout": {"type": "integer", "min": 1, "max": 120},
    "session-cache-capacity": {"type": "integer", "min": 0, "max": 1000},
    "session-cache-timeout": {"type": "integer", "min": 1, "max": 60},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_SSL_DH_BITS = [
    "768",  # 768-bit Diffie-Hellman prime.
    "1024",  # 1024-bit Diffie-Hellman prime.
    "1536",  # 1536-bit Diffie-Hellman prime.
    "2048",  # 2048-bit Diffie-Hellman prime.
]
VALID_BODY_SSL_SEND_EMPTY_FRAGS = [
    "enable",  # Send empty fragments.
    "disable",  # Do not send empty fragments.
]
VALID_BODY_NO_MATCHING_CIPHER_ACTION = [
    "bypass",  # Bypass connection.
    "drop",  # Drop connection.
]
VALID_BODY_RESIGNED_SHORT_LIVED_CERTIFICATE = [
    "enable",  # Enable short-lived certificate: re-signed certificate will remain valid until either the origin server ceritificate expires or cache timeouts.
    "disable",  # Disable short-lived certificate: re-signed certificate will have the same validation period as the origin server ceritificate.
]
VALID_BODY_ABBREVIATE_HANDSHAKE = [
    "enable",  # Enable use of SSL abbreviated handshake.
    "disable",  # Disable use of SSL abbreviated handshake.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_ssl_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/ssl/setting."""
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
    """Validate required fields for firewall/ssl/setting."""
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


def validate_firewall_ssl_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/ssl/setting object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
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
    if "no-matching-cipher-action" in payload:
        value = payload["no-matching-cipher-action"]
        if value not in VALID_BODY_NO_MATCHING_CIPHER_ACTION:
            desc = FIELD_DESCRIPTIONS.get("no-matching-cipher-action", "")
            error_msg = f"Invalid value for 'no-matching-cipher-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NO_MATCHING_CIPHER_ACTION)}"
            error_msg += f"\n  → Example: no-matching-cipher-action='{{ VALID_BODY_NO_MATCHING_CIPHER_ACTION[0] }}'"
            return (False, error_msg)
    if "resigned-short-lived-certificate" in payload:
        value = payload["resigned-short-lived-certificate"]
        if value not in VALID_BODY_RESIGNED_SHORT_LIVED_CERTIFICATE:
            desc = FIELD_DESCRIPTIONS.get("resigned-short-lived-certificate", "")
            error_msg = f"Invalid value for 'resigned-short-lived-certificate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESIGNED_SHORT_LIVED_CERTIFICATE)}"
            error_msg += f"\n  → Example: resigned-short-lived-certificate='{{ VALID_BODY_RESIGNED_SHORT_LIVED_CERTIFICATE[0] }}'"
            return (False, error_msg)
    if "abbreviate-handshake" in payload:
        value = payload["abbreviate-handshake"]
        if value not in VALID_BODY_ABBREVIATE_HANDSHAKE:
            desc = FIELD_DESCRIPTIONS.get("abbreviate-handshake", "")
            error_msg = f"Invalid value for 'abbreviate-handshake': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ABBREVIATE_HANDSHAKE)}"
            error_msg += f"\n  → Example: abbreviate-handshake='{{ VALID_BODY_ABBREVIATE_HANDSHAKE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_ssl_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/ssl/setting."""
    # Step 1: Validate enum values
    if "ssl-dh-bits" in payload:
        value = payload["ssl-dh-bits"]
        if value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid value for 'ssl-dh-bits'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )
    if "ssl-send-empty-frags" in payload:
        value = payload["ssl-send-empty-frags"]
        if value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            return (
                False,
                f"Invalid value for 'ssl-send-empty-frags'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SEND_EMPTY_FRAGS)}",
            )
    if "no-matching-cipher-action" in payload:
        value = payload["no-matching-cipher-action"]
        if value not in VALID_BODY_NO_MATCHING_CIPHER_ACTION:
            return (
                False,
                f"Invalid value for 'no-matching-cipher-action'='{value}'. Must be one of: {', '.join(VALID_BODY_NO_MATCHING_CIPHER_ACTION)}",
            )
    if "resigned-short-lived-certificate" in payload:
        value = payload["resigned-short-lived-certificate"]
        if value not in VALID_BODY_RESIGNED_SHORT_LIVED_CERTIFICATE:
            return (
                False,
                f"Invalid value for 'resigned-short-lived-certificate'='{value}'. Must be one of: {', '.join(VALID_BODY_RESIGNED_SHORT_LIVED_CERTIFICATE)}",
            )
    if "abbreviate-handshake" in payload:
        value = payload["abbreviate-handshake"]
        if value not in VALID_BODY_ABBREVIATE_HANDSHAKE:
            return (
                False,
                f"Invalid value for 'abbreviate-handshake'='{value}'. Must be one of: {', '.join(VALID_BODY_ABBREVIATE_HANDSHAKE)}",
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
    "endpoint": "firewall/ssl/setting",
    "category": "cmdb",
    "api_path": "firewall.ssl/setting",
    "help": "SSL proxy settings.",
    "total_fields": 11,
    "required_fields_count": 0,
    "fields_with_defaults_count": 11,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
