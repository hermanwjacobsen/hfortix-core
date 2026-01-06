"""
Validation helpers for system/mobile_tunnel endpoint.

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
    """
    Validate GET request parameters for system/mobile_tunnel.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_mobile_tunnel_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_system_mobile_tunnel_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_mobile_tunnel_get(
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
    Validate required fields for system/mobile_tunnel.

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


def validate_system_mobile_tunnel_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/mobile_tunnel object.

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
        ...     "roaming-interface": True,  # Select the associated interface name from availabl
        ... }
        >>> is_valid, error = validate_system_mobile_tunnel_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "roaming-interface": True,
        ...     "status": "{'name': 'disable', 'help': 'Disable this mobile tunnel.', 'label': 'Disable', 'description': 'Disable this mobile tunnel'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_mobile_tunnel_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_system_mobile_tunnel_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_mobile_tunnel_post(payload)
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
    """
    Validate PUT request to update system/mobile_tunnel.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_mobile_tunnel_put(payload)
    """
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
