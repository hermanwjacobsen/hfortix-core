"""
Validation helpers for system/fabric_vpn endpoint.

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
    "psksecret",  # Pre-shared secret for ADVPN.
    "bgp-as",  # BGP Router AS number, asplain/asdot/asdot+ format.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "status": "disable",
    "sync-mode": "enable",
    "branch-name": "",
    "policy-rule": "health-check",
    "vpn-role": "hub",
    "loopback-address-block": "0.0.0.0 0.0.0.0",
    "loopback-interface": "",
    "loopback-advertised-subnet": 0,
    "bgp-as": "",
    "sdwan-zone": "",
    "health-checks": "",
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
    "status": "option",  # Enable/disable Fabric VPN.
    "sync-mode": "option",  # Setting synchronised by fabric or manual.
    "branch-name": "string",  # Branch name.
    "policy-rule": "option",  # Policy creation rule.
    "vpn-role": "option",  # Fabric VPN role.
    "overlays": "string",  # Local overlay interfaces table.
    "advertised-subnets": "string",  # Local advertised subnets.
    "loopback-address-block": "ipv4-classnet-host",  # IPv4 address and subnet mask for hub's loopback address, syn
    "loopback-interface": "string",  # Loopback interface.
    "loopback-advertised-subnet": "integer",  # Loopback advertised subnet reference.
    "psksecret": "password-3",  # Pre-shared secret for ADVPN.
    "bgp-as": "user",  # BGP Router AS number, asplain/asdot/asdot+ format.
    "sdwan-zone": "string",  # Reference to created SD-WAN zone.
    "health-checks": "string",  # Underlying health checks.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable Fabric VPN.",
    "sync-mode": "Setting synchronised by fabric or manual.",
    "branch-name": "Branch name.",
    "policy-rule": "Policy creation rule.",
    "vpn-role": "Fabric VPN role.",
    "overlays": "Local overlay interfaces table.",
    "advertised-subnets": "Local advertised subnets.",
    "loopback-address-block": "IPv4 address and subnet mask for hub's loopback address, syntax: X.X.X.X/24.",
    "loopback-interface": "Loopback interface.",
    "loopback-advertised-subnet": "Loopback advertised subnet reference.",
    "psksecret": "Pre-shared secret for ADVPN.",
    "bgp-as": "BGP Router AS number, asplain/asdot/asdot+ format.",
    "sdwan-zone": "Reference to created SD-WAN zone.",
    "health-checks": "Underlying health checks.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "branch-name": {"type": "string", "max_length": 35},
    "loopback-interface": {"type": "string", "max_length": 15},
    "loopback-advertised-subnet": {"type": "integer", "min": 0, "max": 4294967295},
    "sdwan-zone": {"type": "string", "max_length": 35},
    "health-checks": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "overlays": {
        "name": {
            "type": "string",
            "help": "Overlay name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
        "ipsec-network-id": {
            "type": "integer",
            "help": "VPN gateway network ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "overlay-tunnel-block": {
            "type": "ipv4-classnet-host",
            "help": "IPv4 address and subnet mask for the overlay tunnel , syntax: X.X.X.X/24.",
            "default": "0.0.0.0 0.0.0.0",
        },
        "remote-gw": {
            "type": "ipv4-address-any",
            "help": "IP address of the hub gateway (Set by hub).",
            "default": "0.0.0.0",
        },
        "interface": {
            "type": "string",
            "help": "Underlying interface name.",
            "default": "",
            "max_length": 15,
        },
        "bgp-neighbor": {
            "type": "string",
            "help": "Underlying BGP neighbor entry.",
            "default": "",
            "max_length": 45,
        },
        "overlay-policy": {
            "type": "integer",
            "help": "The overlay policy to allow ADVPN thru traffic.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "bgp-network": {
            "type": "integer",
            "help": "Underlying BGP network.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "route-policy": {
            "type": "integer",
            "help": "Underlying router policy.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "bgp-neighbor-group": {
            "type": "string",
            "help": "Underlying BGP neighbor group entry.",
            "default": "",
            "max_length": 45,
        },
        "bgp-neighbor-range": {
            "type": "integer",
            "help": "Underlying BGP neighbor range entry.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ipsec-phase1": {
            "type": "string",
            "help": "IPsec interface.",
            "default": "",
            "max_length": 35,
        },
        "sdwan-member": {
            "type": "integer",
            "help": "Reference to SD-WAN member entry.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "advertised-subnets": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967294,
        },
        "prefix": {
            "type": "ipv4-classnet",
            "help": "Network prefix.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "access": {
            "type": "option",
            "help": "Access policy direction.",
            "required": True,
            "default": "inbound",
            "options": ["inbound", "bidirectional"],
        },
        "bgp-network": {
            "type": "integer",
            "help": "Underlying BGP network.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "firewall-address": {
            "type": "string",
            "help": "Underlying firewall address.",
            "default": "",
            "max_length": 79,
        },
        "policies": {
            "type": "integer",
            "help": "Underlying policies.",
            "default": "",
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_SYNC_MODE = [
    "enable",
    "disable",
]
VALID_BODY_POLICY_RULE = [
    "health-check",
    "manual",
    "auto",
]
VALID_BODY_VPN_ROLE = [
    "hub",
    "spoke",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_fabric_vpn_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/fabric_vpn.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_fabric_vpn_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_fabric_vpn_get(
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
    Validate required fields for system/fabric_vpn.

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


def validate_system_fabric_vpn_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/fabric_vpn object.

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
        ...     "psksecret": True,  # Pre-shared secret for ADVPN.
        ...     "bgp-as": True,  # BGP Router AS number, asplain/asdot/asdot+ format.
        ... }
        >>> is_valid, error = validate_system_fabric_vpn_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "psksecret": True,
        ...     "status": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_fabric_vpn_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_system_fabric_vpn_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_fabric_vpn_post(payload)
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
    if "sync-mode" in payload:
        value = payload["sync-mode"]
        if value not in VALID_BODY_SYNC_MODE:
            desc = FIELD_DESCRIPTIONS.get("sync-mode", "")
            error_msg = f"Invalid value for 'sync-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYNC_MODE)}"
            error_msg += f"\n  → Example: sync-mode='{{ VALID_BODY_SYNC_MODE[0] }}'"
            return (False, error_msg)
    if "policy-rule" in payload:
        value = payload["policy-rule"]
        if value not in VALID_BODY_POLICY_RULE:
            desc = FIELD_DESCRIPTIONS.get("policy-rule", "")
            error_msg = f"Invalid value for 'policy-rule': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_POLICY_RULE)}"
            error_msg += f"\n  → Example: policy-rule='{{ VALID_BODY_POLICY_RULE[0] }}'"
            return (False, error_msg)
    if "vpn-role" in payload:
        value = payload["vpn-role"]
        if value not in VALID_BODY_VPN_ROLE:
            desc = FIELD_DESCRIPTIONS.get("vpn-role", "")
            error_msg = f"Invalid value for 'vpn-role': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VPN_ROLE)}"
            error_msg += f"\n  → Example: vpn-role='{{ VALID_BODY_VPN_ROLE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_fabric_vpn_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/fabric_vpn.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_fabric_vpn_put(payload)
    """
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "sync-mode" in payload:
        value = payload["sync-mode"]
        if value not in VALID_BODY_SYNC_MODE:
            return (
                False,
                f"Invalid value for 'sync-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SYNC_MODE)}",
            )
    if "policy-rule" in payload:
        value = payload["policy-rule"]
        if value not in VALID_BODY_POLICY_RULE:
            return (
                False,
                f"Invalid value for 'policy-rule'='{value}'. Must be one of: {', '.join(VALID_BODY_POLICY_RULE)}",
            )
    if "vpn-role" in payload:
        value = payload["vpn-role"]
        if value not in VALID_BODY_VPN_ROLE:
            return (
                False,
                f"Invalid value for 'vpn-role'='{value}'. Must be one of: {', '.join(VALID_BODY_VPN_ROLE)}",
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
    "endpoint": "system/fabric_vpn",
    "category": "cmdb",
    "api_path": "system/fabric-vpn",
    "help": "Setup for self orchestrated fabric auto discovery VPN.",
    "total_fields": 14,
    "required_fields_count": 2,
    "fields_with_defaults_count": 11,
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
