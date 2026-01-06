"""Validation helpers for ftp_proxy/explicit - Auto-generated"""

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
    "status": "disable",
    "incoming-port": "",
    "incoming-ip": "0.0.0.0",
    "outgoing-ip": "",
    "sec-default-action": "deny",
    "server-data-mode": "client",
    "ssl": "disable",
    "ssl-dh-bits": "2048",
    "ssl-algorithm": "high",
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
    "status": "option",  # Enable/disable the explicit FTP proxy.
    "incoming-port": "user",  # Accept incoming FTP requests on one or more ports.
    "incoming-ip": "ipv4-address-any",  # Accept incoming FTP requests from this IP address. An interf
    "outgoing-ip": "ipv4-address-any",  # Outgoing FTP requests will leave from this IP address. An in
    "sec-default-action": "option",  # Accept or deny explicit FTP proxy sessions when no FTP proxy
    "server-data-mode": "option",  # Determine mode of data session on FTP server side.
    "ssl": "option",  # Enable/disable the explicit FTPS proxy.
    "ssl-cert": "string",  # List of certificate names to use for SSL connections to this
    "ssl-dh-bits": "option",  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    "ssl-algorithm": "option",  # Relative strength of encryption algorithms accepted in negot
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable the explicit FTP proxy.",
    "incoming-port": "Accept incoming FTP requests on one or more ports.",
    "incoming-ip": "Accept incoming FTP requests from this IP address. An interface must have this IP address.",
    "outgoing-ip": "Outgoing FTP requests will leave from this IP address. An interface must have this IP address.",
    "sec-default-action": "Accept or deny explicit FTP proxy sessions when no FTP proxy firewall policy exists.",
    "server-data-mode": "Determine mode of data session on FTP server side.",
    "ssl": "Enable/disable the explicit FTPS proxy.",
    "ssl-cert": "List of certificate names to use for SSL connections to this server.",
    "ssl-dh-bits": "Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048).",
    "ssl-algorithm": "Relative strength of encryption algorithms accepted in negotiation.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
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
VALID_BODY_STATUS = [
    "enable",  # Enable the explicit FTP proxy.
    "disable",  # Disable the explicit FTP proxy.
]
VALID_BODY_SEC_DEFAULT_ACTION = [
    "accept",  # Accept requests. All explicit FTP proxy traffic is accepted whether there is an explicit FTP proxy policy or not
    "deny",  # Deny requests unless there is a matching explicit FTP proxy policy.
]
VALID_BODY_SERVER_DATA_MODE = [
    "client",  # Use the same transmission mode for client and server data sessions.
    "passive",  # Use passive mode on server data session.
]
VALID_BODY_SSL = [
    "enable",  # Enable the explicit FTPS proxy.
    "disable",  # Disable the explicit FTPS proxy.
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
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ftp_proxy_explicit_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for ftp_proxy/explicit."""
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
    """Validate required fields for ftp_proxy/explicit."""
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


def validate_ftp_proxy_explicit_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new ftp_proxy/explicit object."""
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
    if "sec-default-action" in payload:
        value = payload["sec-default-action"]
        if value not in VALID_BODY_SEC_DEFAULT_ACTION:
            desc = FIELD_DESCRIPTIONS.get("sec-default-action", "")
            error_msg = f"Invalid value for 'sec-default-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SEC_DEFAULT_ACTION)}"
            error_msg += f"\n  → Example: sec-default-action='{{ VALID_BODY_SEC_DEFAULT_ACTION[0] }}'"
            return (False, error_msg)
    if "server-data-mode" in payload:
        value = payload["server-data-mode"]
        if value not in VALID_BODY_SERVER_DATA_MODE:
            desc = FIELD_DESCRIPTIONS.get("server-data-mode", "")
            error_msg = f"Invalid value for 'server-data-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVER_DATA_MODE)}"
            error_msg += f"\n  → Example: server-data-mode='{{ VALID_BODY_SERVER_DATA_MODE[0] }}'"
            return (False, error_msg)
    if "ssl" in payload:
        value = payload["ssl"]
        if value not in VALID_BODY_SSL:
            desc = FIELD_DESCRIPTIONS.get("ssl", "")
            error_msg = f"Invalid value for 'ssl': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL)}"
            error_msg += f"\n  → Example: ssl='{{ VALID_BODY_SSL[0] }}'"
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ftp_proxy_explicit_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update ftp_proxy/explicit."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "sec-default-action" in payload:
        value = payload["sec-default-action"]
        if value not in VALID_BODY_SEC_DEFAULT_ACTION:
            return (
                False,
                f"Invalid value for 'sec-default-action'='{value}'. Must be one of: {', '.join(VALID_BODY_SEC_DEFAULT_ACTION)}",
            )
    if "server-data-mode" in payload:
        value = payload["server-data-mode"]
        if value not in VALID_BODY_SERVER_DATA_MODE:
            return (
                False,
                f"Invalid value for 'server-data-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_DATA_MODE)}",
            )
    if "ssl" in payload:
        value = payload["ssl"]
        if value not in VALID_BODY_SSL:
            return (
                False,
                f"Invalid value for 'ssl'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL)}",
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
    "endpoint": "ftp_proxy/explicit",
    "category": "cmdb",
    "api_path": "ftp-proxy/explicit",
    "help": "Configure explicit FTP proxy settings.",
    "total_fields": 10,
    "required_fields_count": 0,
    "fields_with_defaults_count": 9,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
