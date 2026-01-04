"""
Validation helpers for firewall/central_snat_map endpoint.

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
    "srcintf",  # Source interface name from available interfaces.
    "dstintf",  # Destination interface name from available interfaces.
    "orig-addr",  # IPv4 Original address.
    "orig-addr6",  # IPv6 Original address.
    "dst-addr",  # IPv4 Destination address.
    "dst-addr6",  # IPv6 Destination address.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "policyid": 0,
    "uuid": "00000000-0000-0000-0000-000000000000",
    "status": "enable",
    "type": "ipv4",
    "protocol": 0,
    "orig-port": "",
    "nat": "enable",
    "nat46": "disable",
    "nat64": "disable",
    "port-preserve": "enable",
    "port-random": "disable",
    "nat-port": "",
    "dst-port": "",
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
    "policyid": "integer",  # Policy ID.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "status": "option",  # Enable/disable the active status of this policy.
    "type": "option",  # IPv4/IPv6 source NAT.
    "srcintf": "string",  # Source interface name from available interfaces.
    "dstintf": "string",  # Destination interface name from available interfaces.
    "orig-addr": "string",  # IPv4 Original address.
    "orig-addr6": "string",  # IPv6 Original address.
    "dst-addr": "string",  # IPv4 Destination address.
    "dst-addr6": "string",  # IPv6 Destination address.
    "protocol": "integer",  # Integer value for the protocol type (0 - 255).
    "orig-port": "user",  # Original TCP port (1 to 65535, 0 means any port).
    "nat": "option",  # Enable/disable source NAT.
    "nat46": "option",  # Enable/disable NAT46.
    "nat64": "option",  # Enable/disable NAT64.
    "nat-ippool": "string",  # Name of the IP pools to be used to translate addresses from 
    "nat-ippool6": "string",  # IPv6 pools to be used for source NAT.
    "port-preserve": "option",  # Enable/disable preservation of the original source port from
    "port-random": "option",  # Enable/disable random source port selection for source NAT.
    "nat-port": "user",  # Translated port or port range (1 to 65535, 0 means any port)
    "dst-port": "user",  # Destination port or port range (1 to 65535, 0 means any port
    "comments": "var-string",  # Comment.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "policyid": "Policy ID.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "status": "Enable/disable the active status of this policy.",
    "type": "IPv4/IPv6 source NAT.",
    "srcintf": "Source interface name from available interfaces.",
    "dstintf": "Destination interface name from available interfaces.",
    "orig-addr": "IPv4 Original address.",
    "orig-addr6": "IPv6 Original address.",
    "dst-addr": "IPv4 Destination address.",
    "dst-addr6": "IPv6 Destination address.",
    "protocol": "Integer value for the protocol type (0 - 255).",
    "orig-port": "Original TCP port (1 to 65535, 0 means any port).",
    "nat": "Enable/disable source NAT.",
    "nat46": "Enable/disable NAT46.",
    "nat64": "Enable/disable NAT64.",
    "nat-ippool": "Name of the IP pools to be used to translate addresses from available IP Pools.",
    "nat-ippool6": "IPv6 pools to be used for source NAT.",
    "port-preserve": "Enable/disable preservation of the original source port from source NAT if it has not been used.",
    "port-random": "Enable/disable random source port selection for source NAT.",
    "nat-port": "Translated port or port range (1 to 65535, 0 means any port).",
    "dst-port": "Destination port or port range (1 to 65535, 0 means any port).",
    "comments": "Comment.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "policyid": {"type": "integer", "min": 0, "max": 4294967295},
    "protocol": {"type": "integer", "min": 0, "max": 255},
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
    "dstintf": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "orig-addr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "orig-addr6": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "default": "",
            "max_length": 79,
        },
    },
    "dst-addr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dst-addr6": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "default": "",
            "max_length": 79,
        },
    },
    "nat-ippool": {
        "name": {
            "type": "string",
            "help": "IP pool name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "nat-ippool6": {
        "name": {
            "type": "string",
            "help": "IPv6 pool name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_TYPE = [
    "ipv4",
    "ipv6",
]
VALID_BODY_NAT = [
    "disable",
    "enable",
]
VALID_BODY_NAT46 = [
    "enable",
    "disable",
]
VALID_BODY_NAT64 = [
    "enable",
    "disable",
]
VALID_BODY_PORT_PRESERVE = [
    "enable",
    "disable",
]
VALID_BODY_PORT_RANDOM = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_central_snat_map_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for firewall/central_snat_map.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_firewall_central_snat_map_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by policyid
        >>> is_valid, error = validate_firewall_central_snat_map_get(policyid="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_firewall_central_snat_map_get(
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
    Validate required fields for firewall/central_snat_map.

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


def validate_firewall_central_snat_map_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new firewall/central_snat_map object.

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
        ...     "srcintf": True,  # Source interface name from available interfaces.
        ...     "dstintf": True,  # Destination interface name from available interfac
        ... }
        >>> is_valid, error = validate_firewall_central_snat_map_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "srcintf": True,
        ...     "status": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_firewall_central_snat_map_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_firewall_central_snat_map_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_firewall_central_snat_map_post(payload)
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
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "nat" in payload:
        value = payload["nat"]
        if value not in VALID_BODY_NAT:
            desc = FIELD_DESCRIPTIONS.get("nat", "")
            error_msg = f"Invalid value for 'nat': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT)}"
            error_msg += f"\n  → Example: nat='{{ VALID_BODY_NAT[0] }}'"
            return (False, error_msg)
    if "nat46" in payload:
        value = payload["nat46"]
        if value not in VALID_BODY_NAT46:
            desc = FIELD_DESCRIPTIONS.get("nat46", "")
            error_msg = f"Invalid value for 'nat46': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT46)}"
            error_msg += f"\n  → Example: nat46='{{ VALID_BODY_NAT46[0] }}'"
            return (False, error_msg)
    if "nat64" in payload:
        value = payload["nat64"]
        if value not in VALID_BODY_NAT64:
            desc = FIELD_DESCRIPTIONS.get("nat64", "")
            error_msg = f"Invalid value for 'nat64': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT64)}"
            error_msg += f"\n  → Example: nat64='{{ VALID_BODY_NAT64[0] }}'"
            return (False, error_msg)
    if "port-preserve" in payload:
        value = payload["port-preserve"]
        if value not in VALID_BODY_PORT_PRESERVE:
            desc = FIELD_DESCRIPTIONS.get("port-preserve", "")
            error_msg = f"Invalid value for 'port-preserve': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORT_PRESERVE)}"
            error_msg += f"\n  → Example: port-preserve='{{ VALID_BODY_PORT_PRESERVE[0] }}'"
            return (False, error_msg)
    if "port-random" in payload:
        value = payload["port-random"]
        if value not in VALID_BODY_PORT_RANDOM:
            desc = FIELD_DESCRIPTIONS.get("port-random", "")
            error_msg = f"Invalid value for 'port-random': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORT_RANDOM)}"
            error_msg += f"\n  → Example: port-random='{{ VALID_BODY_PORT_RANDOM[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_central_snat_map_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update firewall/central_snat_map.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_firewall_central_snat_map_put(payload)
    """
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "nat" in payload:
        value = payload["nat"]
        if value not in VALID_BODY_NAT:
            return (
                False,
                f"Invalid value for 'nat'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT)}",
            )
    if "nat46" in payload:
        value = payload["nat46"]
        if value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid value for 'nat46'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )
    if "nat64" in payload:
        value = payload["nat64"]
        if value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid value for 'nat64'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )
    if "port-preserve" in payload:
        value = payload["port-preserve"]
        if value not in VALID_BODY_PORT_PRESERVE:
            return (
                False,
                f"Invalid value for 'port-preserve'='{value}'. Must be one of: {', '.join(VALID_BODY_PORT_PRESERVE)}",
            )
    if "port-random" in payload:
        value = payload["port-random"]
        if value not in VALID_BODY_PORT_RANDOM:
            return (
                False,
                f"Invalid value for 'port-random'='{value}'. Must be one of: {', '.join(VALID_BODY_PORT_RANDOM)}",
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
    "endpoint": "firewall/central_snat_map",
    "category": "cmdb",
    "api_path": "firewall/central-snat-map",
    "mkey": "policyid",
    "mkey_type": "integer",
    "help": "Configure IPv4 and IPv6 central SNAT policies.",
    "total_fields": 22,
    "required_fields_count": 6,
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
