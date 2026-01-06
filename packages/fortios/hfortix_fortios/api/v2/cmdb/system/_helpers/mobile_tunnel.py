"""Validation helpers for system/mobile_tunnel - Auto-generated"""

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
    "roaming-interface",  # Select the associated interface name from available options.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "status": "enable",
    "roaming-interface": "",
    "home-agent": "0.0.0.0",
    "home-address": "0.0.0.0",
    "renew-interval": 60,
    "lifetime": 65535,
    "reg-interval": 5,
    "reg-retry": 3,
    "n-mhae-spi": 256,
    "n-mhae-key-type": "ascii",
    "hash-algorithm": "hmac-md5",
    "tunnel-mode": "gre",
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
    "name": "string",  # Tunnel name.
    "status": "option",  # Enable/disable this mobile tunnel.
    "roaming-interface": "string",  # Select the associated interface name from available options.
    "home-agent": "ipv4-address",  # IPv4 address of the NEMO HA (Format: xxx.xxx.xxx.xxx).
    "home-address": "ipv4-address",  # Home IP address (Format: xxx.xxx.xxx.xxx).
    "renew-interval": "integer",  # Time before lifetime expiration to send NMMO HA re-registrat
    "lifetime": "integer",  # NMMO HA registration request lifetime (180 - 65535 sec, defa
    "reg-interval": "integer",  # NMMO HA registration interval (5 - 300, default = 5).
    "reg-retry": "integer",  # Maximum number of NMMO HA registration retries (1 to 30, def
    "n-mhae-spi": "integer",  # NEMO authentication SPI (default: 256).
    "n-mhae-key-type": "option",  # NEMO authentication key type (ASCII or base64).
    "n-mhae-key": "password_aes256",  # NEMO authentication key.
    "hash-algorithm": "option",  # Hash Algorithm (Keyed MD5).
    "tunnel-mode": "option",  # NEMO tunnel mode (GRE tunnel).
    "network": "string",  # NEMO network configuration.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Tunnel name.",
    "status": "Enable/disable this mobile tunnel.",
    "roaming-interface": "Select the associated interface name from available options.",
    "home-agent": "IPv4 address of the NEMO HA (Format: xxx.xxx.xxx.xxx).",
    "home-address": "Home IP address (Format: xxx.xxx.xxx.xxx).",
    "renew-interval": "Time before lifetime expiration to send NMMO HA re-registration (5 - 60, default = 60).",
    "lifetime": "NMMO HA registration request lifetime (180 - 65535 sec, default = 65535).",
    "reg-interval": "NMMO HA registration interval (5 - 300, default = 5).",
    "reg-retry": "Maximum number of NMMO HA registration retries (1 to 30, default = 3).",
    "n-mhae-spi": "NEMO authentication SPI (default: 256).",
    "n-mhae-key-type": "NEMO authentication key type (ASCII or base64).",
    "n-mhae-key": "NEMO authentication key.",
    "hash-algorithm": "Hash Algorithm (Keyed MD5).",
    "tunnel-mode": "NEMO tunnel mode (GRE tunnel).",
    "network": "NEMO network configuration.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 15},
    "roaming-interface": {"type": "string", "max_length": 15},
    "renew-interval": {"type": "integer", "min": 5, "max": 60},
    "lifetime": {"type": "integer", "min": 180, "max": 65535},
    "reg-interval": {"type": "integer", "min": 5, "max": 300},
    "reg-retry": {"type": "integer", "min": 1, "max": 30},
    "n-mhae-spi": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "network": {
        "id": {
            "type": "integer",
            "help": "Network entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "interface": {
            "type": "string",
            "help": "Select the associated interface name from available options.",
            "default": "",
            "max_length": 15,
        },
        "prefix": {
            "type": "ipv4-classnet",
            "help": "Class IP and Netmask with correction (Format:xxx.xxx.xxx.xxx xxx.xxx.xxx.xxx or xxx.xxx.xxx.xxx/x).",
            "default": "0.0.0.0 0.0.0.0",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "disable",  # Disable this mobile tunnel.
    "enable",  # Enable this mobile tunnel.
]
VALID_BODY_N_MHAE_KEY_TYPE = [
    "ascii",  # The authentication key is an ASCII string.
    "base64",  # The authentication key is Base64 encoded.
]
VALID_BODY_HASH_ALGORITHM = [
    "hmac-md5",  # Keyed MD5.
]
VALID_BODY_TUNNEL_MODE = [
    "gre",  # GRE tunnel.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_mobile_tunnel_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/mobile_tunnel."""
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
    """Validate required fields for system/mobile_tunnel."""
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


def validate_system_mobile_tunnel_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/mobile_tunnel object."""
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
    if "n-mhae-key-type" in payload:
        value = payload["n-mhae-key-type"]
        if value not in VALID_BODY_N_MHAE_KEY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("n-mhae-key-type", "")
            error_msg = f"Invalid value for 'n-mhae-key-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_N_MHAE_KEY_TYPE)}"
            error_msg += f"\n  → Example: n-mhae-key-type='{{ VALID_BODY_N_MHAE_KEY_TYPE[0] }}'"
            return (False, error_msg)
    if "hash-algorithm" in payload:
        value = payload["hash-algorithm"]
        if value not in VALID_BODY_HASH_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("hash-algorithm", "")
            error_msg = f"Invalid value for 'hash-algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HASH_ALGORITHM)}"
            error_msg += f"\n  → Example: hash-algorithm='{{ VALID_BODY_HASH_ALGORITHM[0] }}'"
            return (False, error_msg)
    if "tunnel-mode" in payload:
        value = payload["tunnel-mode"]
        if value not in VALID_BODY_TUNNEL_MODE:
            desc = FIELD_DESCRIPTIONS.get("tunnel-mode", "")
            error_msg = f"Invalid value for 'tunnel-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TUNNEL_MODE)}"
            error_msg += f"\n  → Example: tunnel-mode='{{ VALID_BODY_TUNNEL_MODE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_mobile_tunnel_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/mobile_tunnel."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "n-mhae-key-type" in payload:
        value = payload["n-mhae-key-type"]
        if value not in VALID_BODY_N_MHAE_KEY_TYPE:
            return (
                False,
                f"Invalid value for 'n-mhae-key-type'='{value}'. Must be one of: {', '.join(VALID_BODY_N_MHAE_KEY_TYPE)}",
            )
    if "hash-algorithm" in payload:
        value = payload["hash-algorithm"]
        if value not in VALID_BODY_HASH_ALGORITHM:
            return (
                False,
                f"Invalid value for 'hash-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_HASH_ALGORITHM)}",
            )
    if "tunnel-mode" in payload:
        value = payload["tunnel-mode"]
        if value not in VALID_BODY_TUNNEL_MODE:
            return (
                False,
                f"Invalid value for 'tunnel-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_TUNNEL_MODE)}",
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
    "endpoint": "system/mobile_tunnel",
    "category": "cmdb",
    "api_path": "system/mobile-tunnel",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.",
    "total_fields": 15,
    "required_fields_count": 1,
    "fields_with_defaults_count": 13,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
