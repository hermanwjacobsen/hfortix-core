"""Validation helpers for vpn/certificate/ca - Auto-generated"""

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
    "name",  # Name.
    "ca",  # CA certificate as a PEM file.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "ca": "",
    "range": "vdom",
    "source": "user",
    "ssl-inspection-trusted": "enable",
    "scep-url": "",
    "est-url": "",
    "auto-update-days": 0,
    "auto-update-days-warning": 0,
    "source-ip": "0.0.0.0",
    "ca-identifier": "",
    "obsolete": "disable",
    "fabric-ca": "disable",
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
    "name": "string",  # Name.
    "ca": "user",  # CA certificate as a PEM file.
    "range": "option",  # Either global or VDOM IP address range for the CA certificat
    "source": "option",  # CA certificate source type.
    "ssl-inspection-trusted": "option",  # Enable/disable this CA as a trusted CA for SSL inspection.
    "scep-url": "string",  # URL of the SCEP server.
    "est-url": "string",  # URL of the EST server.
    "auto-update-days": "integer",  # Number of days to wait before requesting an updated CA certi
    "auto-update-days-warning": "integer",  # Number of days before an expiry-warning message is generated
    "source-ip": "ipv4-address",  # Source IP address for communications to the SCEP server.
    "ca-identifier": "string",  # CA identifier of the SCEP server.
    "obsolete": "option",  # Enable/disable this CA as obsoleted.
    "fabric-ca": "option",  # Enable/disable synchronization of CA across Security Fabric.
    "details": "key",  # Print CA certificate detailed information.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Name.",
    "ca": "CA certificate as a PEM file.",
    "range": "Either global or VDOM IP address range for the CA certificate.",
    "source": "CA certificate source type.",
    "ssl-inspection-trusted": "Enable/disable this CA as a trusted CA for SSL inspection.",
    "scep-url": "URL of the SCEP server.",
    "est-url": "URL of the EST server.",
    "auto-update-days": "Number of days to wait before requesting an updated CA certificate (0 - 4294967295, 0 = disabled).",
    "auto-update-days-warning": "Number of days before an expiry-warning message is generated (0 - 4294967295, 0 = disabled).",
    "source-ip": "Source IP address for communications to the SCEP server.",
    "ca-identifier": "CA identifier of the SCEP server.",
    "obsolete": "Enable/disable this CA as obsoleted.",
    "fabric-ca": "Enable/disable synchronization of CA across Security Fabric.",
    "details": "Print CA certificate detailed information.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 79},
    "scep-url": {"type": "string", "max_length": 255},
    "est-url": {"type": "string", "max_length": 255},
    "auto-update-days": {"type": "integer", "min": 0, "max": 4294967295},
    "auto-update-days-warning": {"type": "integer", "min": 0, "max": 4294967295},
    "ca-identifier": {"type": "string", "max_length": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "details": {
        "<CA certficate name>": {
            "type": "value",
            "help": "CA certificate name.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_RANGE = [
    "global",  # Global range.
    "vdom",  # VDOM IP address range.
]
VALID_BODY_SOURCE = [
    "factory",  # Factory installed certificate.
    "user",  # User generated certificate.
    "bundle",  # Bundle file certificate.
]
VALID_BODY_SSL_INSPECTION_TRUSTED = [
    "enable",  # Trusted CA for SSL inspection.
    "disable",  # Untrusted CA for SSL inspection.
]
VALID_BODY_OBSOLETE = [
    "disable",  # Alive.
    "enable",  # Obsolete.
]
VALID_BODY_FABRIC_CA = [
    "disable",  # Disable synchronization of CA across Security Fabric.
    "enable",  # Enable synchronization of CA across Security Fabric.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vpn_certificate_ca_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for vpn/certificate/ca."""
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
    """Validate required fields for vpn/certificate/ca."""
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


def validate_vpn_certificate_ca_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new vpn/certificate/ca object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "range" in payload:
        value = payload["range"]
        if value not in VALID_BODY_RANGE:
            desc = FIELD_DESCRIPTIONS.get("range", "")
            error_msg = f"Invalid value for 'range': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RANGE)}"
            error_msg += f"\n  → Example: range='{{ VALID_BODY_RANGE[0] }}'"
            return (False, error_msg)
    if "source" in payload:
        value = payload["source"]
        if value not in VALID_BODY_SOURCE:
            desc = FIELD_DESCRIPTIONS.get("source", "")
            error_msg = f"Invalid value for 'source': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SOURCE)}"
            error_msg += f"\n  → Example: source='{{ VALID_BODY_SOURCE[0] }}'"
            return (False, error_msg)
    if "ssl-inspection-trusted" in payload:
        value = payload["ssl-inspection-trusted"]
        if value not in VALID_BODY_SSL_INSPECTION_TRUSTED:
            desc = FIELD_DESCRIPTIONS.get("ssl-inspection-trusted", "")
            error_msg = f"Invalid value for 'ssl-inspection-trusted': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_INSPECTION_TRUSTED)}"
            error_msg += f"\n  → Example: ssl-inspection-trusted='{{ VALID_BODY_SSL_INSPECTION_TRUSTED[0] }}'"
            return (False, error_msg)
    if "obsolete" in payload:
        value = payload["obsolete"]
        if value not in VALID_BODY_OBSOLETE:
            desc = FIELD_DESCRIPTIONS.get("obsolete", "")
            error_msg = f"Invalid value for 'obsolete': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OBSOLETE)}"
            error_msg += f"\n  → Example: obsolete='{{ VALID_BODY_OBSOLETE[0] }}'"
            return (False, error_msg)
    if "fabric-ca" in payload:
        value = payload["fabric-ca"]
        if value not in VALID_BODY_FABRIC_CA:
            desc = FIELD_DESCRIPTIONS.get("fabric-ca", "")
            error_msg = f"Invalid value for 'fabric-ca': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FABRIC_CA)}"
            error_msg += f"\n  → Example: fabric-ca='{{ VALID_BODY_FABRIC_CA[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_vpn_certificate_ca_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update vpn/certificate/ca."""
    # Step 1: Validate enum values
    if "range" in payload:
        value = payload["range"]
        if value not in VALID_BODY_RANGE:
            return (
                False,
                f"Invalid value for 'range'='{value}'. Must be one of: {', '.join(VALID_BODY_RANGE)}",
            )
    if "source" in payload:
        value = payload["source"]
        if value not in VALID_BODY_SOURCE:
            return (
                False,
                f"Invalid value for 'source'='{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE)}",
            )
    if "ssl-inspection-trusted" in payload:
        value = payload["ssl-inspection-trusted"]
        if value not in VALID_BODY_SSL_INSPECTION_TRUSTED:
            return (
                False,
                f"Invalid value for 'ssl-inspection-trusted'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_INSPECTION_TRUSTED)}",
            )
    if "obsolete" in payload:
        value = payload["obsolete"]
        if value not in VALID_BODY_OBSOLETE:
            return (
                False,
                f"Invalid value for 'obsolete'='{value}'. Must be one of: {', '.join(VALID_BODY_OBSOLETE)}",
            )
    if "fabric-ca" in payload:
        value = payload["fabric-ca"]
        if value not in VALID_BODY_FABRIC_CA:
            return (
                False,
                f"Invalid value for 'fabric-ca'='{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_CA)}",
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
    "endpoint": "vpn/certificate/ca",
    "category": "cmdb",
    "api_path": "vpn.certificate/ca",
    "mkey": "name",
    "mkey_type": "string",
    "help": "CA certificate.",
    "total_fields": 14,
    "required_fields_count": 2,
    "fields_with_defaults_count": 13,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
