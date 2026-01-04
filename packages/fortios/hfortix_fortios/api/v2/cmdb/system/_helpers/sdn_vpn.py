"""
Validation helpers for system/sdn_vpn endpoint.

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
    "sdn",  # SDN connector name.
    "vgw-id",  # Virtual private gateway id.
    "tgw-id",  # Transit gateway id.
    "tunnel-interface",  # Tunnel interface with public IP.
    "internal-interface",  # Internal interface with local subnet.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "sdn": "",
    "remote-type": "vgw",
    "routing-type": "dynamic",
    "vgw-id": "",
    "tgw-id": "",
    "subnet-id": "",
    "bgp-as": 65000,
    "cgw-gateway": "0.0.0.0",
    "nat-traversal": "enable",
    "tunnel-interface": "",
    "internal-interface": "",
    "local-cidr": "0.0.0.0 0.0.0.0",
    "remote-cidr": "0.0.0.0 0.0.0.0",
    "cgw-name": "",
    "type": 0,
    "status": 0,
    "code": 0,
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
    "name": "string",  # Public cloud VPN name.
    "sdn": "string",  # SDN connector name.
    "remote-type": "option",  # Type of remote device.
    "routing-type": "option",  # Type of routing.
    "vgw-id": "string",  # Virtual private gateway id.
    "tgw-id": "string",  # Transit gateway id.
    "subnet-id": "string",  # AWS subnet id for TGW route propagation.
    "bgp-as": "integer",  # BGP Router AS number.
    "cgw-gateway": "ipv4-address-any",  # Public IP address of the customer gateway.
    "nat-traversal": "option",  # Enable/disable use for NAT traversal. Please enable if your 
    "tunnel-interface": "string",  # Tunnel interface with public IP.
    "internal-interface": "string",  # Internal interface with local subnet.
    "local-cidr": "ipv4-classnet",  # Local subnet address and subnet mask.
    "remote-cidr": "ipv4-classnet",  # Remote subnet address and subnet mask.
    "cgw-name": "string",  # AWS customer gateway name to be created.
    "psksecret": "password-3",  # Pre-shared secret for PSK authentication. Auto-generated if 
    "type": "integer",  # SDN VPN type.
    "status": "integer",  # SDN VPN status.
    "code": "integer",  # SDN VPN error code.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Public cloud VPN name.",
    "sdn": "SDN connector name.",
    "remote-type": "Type of remote device.",
    "routing-type": "Type of routing.",
    "vgw-id": "Virtual private gateway id.",
    "tgw-id": "Transit gateway id.",
    "subnet-id": "AWS subnet id for TGW route propagation.",
    "bgp-as": "BGP Router AS number.",
    "cgw-gateway": "Public IP address of the customer gateway.",
    "nat-traversal": "Enable/disable use for NAT traversal. Please enable if your FortiGate device is behind a NAT/PAT device.",
    "tunnel-interface": "Tunnel interface with public IP.",
    "internal-interface": "Internal interface with local subnet.",
    "local-cidr": "Local subnet address and subnet mask.",
    "remote-cidr": "Remote subnet address and subnet mask.",
    "cgw-name": "AWS customer gateway name to be created.",
    "psksecret": "Pre-shared secret for PSK authentication. Auto-generated if not specified",
    "type": "SDN VPN type.",
    "status": "SDN VPN status.",
    "code": "SDN VPN error code.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "sdn": {"type": "string", "max_length": 35},
    "vgw-id": {"type": "string", "max_length": 63},
    "tgw-id": {"type": "string", "max_length": 63},
    "subnet-id": {"type": "string", "max_length": 63},
    "bgp-as": {"type": "integer", "min": 1, "max": 4294967295},
    "tunnel-interface": {"type": "string", "max_length": 15},
    "internal-interface": {"type": "string", "max_length": 15},
    "cgw-name": {"type": "string", "max_length": 35},
    "type": {"type": "integer", "min": 0, "max": 65535},
    "status": {"type": "integer", "min": 0, "max": 255},
    "code": {"type": "integer", "min": 0, "max": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_REMOTE_TYPE = [
    "vgw",
    "tgw",
]
VALID_BODY_ROUTING_TYPE = [
    "static",
    "dynamic",
]
VALID_BODY_NAT_TRAVERSAL = [
    "disable",
    "enable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_sdn_vpn_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/sdn_vpn.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_sdn_vpn_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_system_sdn_vpn_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_sdn_vpn_get(
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
    Validate required fields for system/sdn_vpn.

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


def validate_system_sdn_vpn_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/sdn_vpn object.

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
        ...     "sdn": True,  # SDN connector name.
        ...     "vgw-id": True,  # Virtual private gateway id.
        ... }
        >>> is_valid, error = validate_system_sdn_vpn_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "sdn": True,
        ...     "remote-type": "vgw",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_sdn_vpn_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["remote-type"] = "invalid-value"
        >>> is_valid, error = validate_system_sdn_vpn_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_sdn_vpn_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "remote-type" in payload:
        value = payload["remote-type"]
        if value not in VALID_BODY_REMOTE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("remote-type", "")
            error_msg = f"Invalid value for 'remote-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REMOTE_TYPE)}"
            error_msg += f"\n  → Example: remote-type='{{ VALID_BODY_REMOTE_TYPE[0] }}'"
            return (False, error_msg)
    if "routing-type" in payload:
        value = payload["routing-type"]
        if value not in VALID_BODY_ROUTING_TYPE:
            desc = FIELD_DESCRIPTIONS.get("routing-type", "")
            error_msg = f"Invalid value for 'routing-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROUTING_TYPE)}"
            error_msg += f"\n  → Example: routing-type='{{ VALID_BODY_ROUTING_TYPE[0] }}'"
            return (False, error_msg)
    if "nat-traversal" in payload:
        value = payload["nat-traversal"]
        if value not in VALID_BODY_NAT_TRAVERSAL:
            desc = FIELD_DESCRIPTIONS.get("nat-traversal", "")
            error_msg = f"Invalid value for 'nat-traversal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT_TRAVERSAL)}"
            error_msg += f"\n  → Example: nat-traversal='{{ VALID_BODY_NAT_TRAVERSAL[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_sdn_vpn_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/sdn_vpn.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_sdn_vpn_put(payload)
    """
    # Step 1: Validate enum values
    if "remote-type" in payload:
        value = payload["remote-type"]
        if value not in VALID_BODY_REMOTE_TYPE:
            return (
                False,
                f"Invalid value for 'remote-type'='{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_TYPE)}",
            )
    if "routing-type" in payload:
        value = payload["routing-type"]
        if value not in VALID_BODY_ROUTING_TYPE:
            return (
                False,
                f"Invalid value for 'routing-type'='{value}'. Must be one of: {', '.join(VALID_BODY_ROUTING_TYPE)}",
            )
    if "nat-traversal" in payload:
        value = payload["nat-traversal"]
        if value not in VALID_BODY_NAT_TRAVERSAL:
            return (
                False,
                f"Invalid value for 'nat-traversal'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT_TRAVERSAL)}",
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
    constant_name = f"VALID_BODY_{field_name.replace('-', '_').upper()}"
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
    "endpoint": "system/sdn_vpn",
    "category": "cmdb",
    "api_path": "system/sdn-vpn",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure public cloud VPN service.",
    "total_fields": 19,
    "required_fields_count": 5,
    "fields_with_defaults_count": 18,
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
