"""Validation helpers for vpn/ipsec/manualkey - Auto-generated"""

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
    "interface",  # Name of the physical, aggregate, or VLAN interface.
    "authkey",  # Hexadecimal authentication key in 16-digit (8-byte) segments separated by hyphens.
    "enckey",  # Hexadecimal encryption key in 16-digit (8-byte) segments separated by hyphens.
    "localspi",  # Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules.
    "remotespi",  # Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "interface": "",
    "remote-gw": "0.0.0.0",
    "local-gw": "0.0.0.0",
    "authentication": "null",
    "encryption": "null",
    "authkey": "",
    "enckey": "",
    "localspi": "",
    "remotespi": "",
    "npu-offload": "enable",
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
    "name": "string",  # IPsec tunnel name.
    "interface": "string",  # Name of the physical, aggregate, or VLAN interface.
    "remote-gw": "ipv4-address",  # Peer gateway.
    "local-gw": "ipv4-address-any",  # Local gateway.
    "authentication": "option",  # Authentication algorithm. Must be the same for both ends of 
    "encryption": "option",  # Encryption algorithm. Must be the same for both ends of the 
    "authkey": "user",  # Hexadecimal authentication key in 16-digit (8-byte) segments
    "enckey": "user",  # Hexadecimal encryption key in 16-digit (8-byte) segments sep
    "localspi": "user",  # Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns betw
    "remotespi": "user",  # Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns bet
    "npu-offload": "option",  # Enable/disable NPU offloading.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "IPsec tunnel name.",
    "interface": "Name of the physical, aggregate, or VLAN interface.",
    "remote-gw": "Peer gateway.",
    "local-gw": "Local gateway.",
    "authentication": "Authentication algorithm. Must be the same for both ends of the tunnel.",
    "encryption": "Encryption algorithm. Must be the same for both ends of the tunnel.",
    "authkey": "Hexadecimal authentication key in 16-digit (8-byte) segments separated by hyphens.",
    "enckey": "Hexadecimal encryption key in 16-digit (8-byte) segments separated by hyphens.",
    "localspi": "Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules.",
    "remotespi": "Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules.",
    "npu-offload": "Enable/disable NPU offloading.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "interface": {"type": "string", "max_length": 15},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_AUTHENTICATION = [
    "null",  # Null.
    "md5",  # MD5.
    "sha1",  # SHA1.
    "sha256",  # SHA256.
    "sha384",  # SHA384.
    "sha512",  # SHA512.
]
VALID_BODY_ENCRYPTION = [
    "null",  # Null.
    "des",  # DES.
    "3des",  # 3DES.
    "aes128",  # AES128.
    "aes192",  # AES192.
    "aes256",  # AES256.
    "aria128",  # ARIA128.
    "aria192",  # ARIA192.
    "aria256",  # ARIA256.
    "seed",  # Seed.
]
VALID_BODY_NPU_OFFLOAD = [
    "enable",  # Enable NPU offloading.
    "disable",  # Disable NPU offloading.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vpn_ipsec_manualkey_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for vpn/ipsec/manualkey."""
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
    """Validate required fields for vpn/ipsec/manualkey."""
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


def validate_vpn_ipsec_manualkey_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new vpn/ipsec/manualkey object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "authentication" in payload:
        value = payload["authentication"]
        if value not in VALID_BODY_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("authentication", "")
            error_msg = f"Invalid value for 'authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHENTICATION)}"
            error_msg += f"\n  → Example: authentication='{{ VALID_BODY_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "encryption" in payload:
        value = payload["encryption"]
        if value not in VALID_BODY_ENCRYPTION:
            desc = FIELD_DESCRIPTIONS.get("encryption", "")
            error_msg = f"Invalid value for 'encryption': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENCRYPTION)}"
            error_msg += f"\n  → Example: encryption='{{ VALID_BODY_ENCRYPTION[0] }}'"
            return (False, error_msg)
    if "npu-offload" in payload:
        value = payload["npu-offload"]
        if value not in VALID_BODY_NPU_OFFLOAD:
            desc = FIELD_DESCRIPTIONS.get("npu-offload", "")
            error_msg = f"Invalid value for 'npu-offload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NPU_OFFLOAD)}"
            error_msg += f"\n  → Example: npu-offload='{{ VALID_BODY_NPU_OFFLOAD[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_vpn_ipsec_manualkey_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update vpn/ipsec/manualkey."""
    # Step 1: Validate enum values
    if "authentication" in payload:
        value = payload["authentication"]
        if value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )
    if "encryption" in payload:
        value = payload["encryption"]
        if value not in VALID_BODY_ENCRYPTION:
            return (
                False,
                f"Invalid value for 'encryption'='{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPTION)}",
            )
    if "npu-offload" in payload:
        value = payload["npu-offload"]
        if value not in VALID_BODY_NPU_OFFLOAD:
            return (
                False,
                f"Invalid value for 'npu-offload'='{value}'. Must be one of: {', '.join(VALID_BODY_NPU_OFFLOAD)}",
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
    "endpoint": "vpn/ipsec/manualkey",
    "category": "cmdb",
    "api_path": "vpn.ipsec/manualkey",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure IPsec manual keys.",
    "total_fields": 11,
    "required_fields_count": 5,
    "fields_with_defaults_count": 11,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
