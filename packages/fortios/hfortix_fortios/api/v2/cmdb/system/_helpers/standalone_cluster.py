"""
Validation helpers for system/standalone_cluster endpoint.

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
    "psksecret",  # Pre-shared secret for session synchronization (ASCII string or hexadecimal encoded with a leading 0x).
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "standalone-group-id": 0,
    "group-member-id": 0,
    "layer2-connection": "unavailable",
    "session-sync-dev": "",
    "encryption": "disable",
    "asymmetric-traffic-control": "cps-preferred",
    "helper-traffic-bounce": "enable",
    "utm-traffic-bounce": "enable",
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
    "standalone-group-id": "integer",  # Cluster group ID (0 - 255). Must be the same for all members
    "group-member-id": "integer",  # Cluster member ID (0 - 15).
    "layer2-connection": "option",  # Indicate whether layer 2 connections are present among FGSP 
    "session-sync-dev": "user",  # Offload session-sync process to kernel and sync sessions usi
    "encryption": "option",  # Enable/disable encryption when synchronizing sessions.
    "psksecret": "password-3",  # Pre-shared secret for session synchronization (ASCII string 
    "asymmetric-traffic-control": "option",  # Asymmetric traffic control mode.
    "cluster-peer": "string",  # Configure FortiGate Session Life Support Protocol (FGSP) ses
    "monitor-interface": "string",  # Configure a list of interfaces on which to monitor itself. M
    "pingsvr-monitor-interface": "string",  # List of pingsvr monitor interface to check for remote IP mon
    "monitor-prefix": "string",  # Configure a list of routing prefixes to monitor.
    "helper-traffic-bounce": "option",  # Enable/disable helper related traffic bounce.
    "utm-traffic-bounce": "option",  # Enable/disable UTM related traffic bounce.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "standalone-group-id": "Cluster group ID (0 - 255). Must be the same for all members.",
    "group-member-id": "Cluster member ID (0 - 15).",
    "layer2-connection": "Indicate whether layer 2 connections are present among FGSP members.",
    "session-sync-dev": "Offload session-sync process to kernel and sync sessions using connected interface(s) directly.",
    "encryption": "Enable/disable encryption when synchronizing sessions.",
    "psksecret": "Pre-shared secret for session synchronization (ASCII string or hexadecimal encoded with a leading 0x).",
    "asymmetric-traffic-control": "Asymmetric traffic control mode.",
    "cluster-peer": "Configure FortiGate Session Life Support Protocol (FGSP) session synchronization.",
    "monitor-interface": "Configure a list of interfaces on which to monitor itself. Monitoring is performed on the status of the interface.",
    "pingsvr-monitor-interface": "List of pingsvr monitor interface to check for remote IP monitoring.",
    "monitor-prefix": "Configure a list of routing prefixes to monitor.",
    "helper-traffic-bounce": "Enable/disable helper related traffic bounce.",
    "utm-traffic-bounce": "Enable/disable UTM related traffic bounce.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "standalone-group-id": {"type": "integer", "min": 0, "max": 255},
    "group-member-id": {"type": "integer", "min": 0, "max": 15},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "cluster-peer": {
        "sync-id": {
            "type": "integer",
            "help": "Sync ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "peervd": {
            "type": "string",
            "help": "VDOM that contains the session synchronization link interface on the peer unit. Usually both peers would have the same peervd.",
            "default": "root",
            "max_length": 31,
        },
        "peerip": {
            "type": "ipv4-address",
            "help": "IP address of the interface on the peer unit that is used for the session synchronization link.",
            "default": "0.0.0.0",
        },
        "syncvd": {
            "type": "string",
            "help": "Sessions from these VDOMs are synchronized using this session synchronization configuration.",
        },
        "down-intfs-before-sess-sync": {
            "type": "string",
            "help": "List of interfaces to be turned down before session synchronization is complete.",
        },
        "hb-interval": {
            "type": "integer",
            "help": "Heartbeat interval (1 - 20 (100*ms). Increase to reduce false positives.",
            "default": 2,
            "min_value": 1,
            "max_value": 20,
        },
        "hb-lost-threshold": {
            "type": "integer",
            "help": "Lost heartbeat threshold (1 - 60). Increase to reduce false positives.",
            "default": 10,
            "min_value": 1,
            "max_value": 60,
        },
        "ipsec-tunnel-sync": {
            "type": "option",
            "help": "Enable/disable IPsec tunnel synchronization.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "secondary-add-ipsec-routes": {
            "type": "option",
            "help": "Enable/disable IKE route announcement on the backup unit.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "session-sync-filter": {
            "type": "string",
            "help": "Add one or more filters if you only want to synchronize some sessions. Use the filter to configure the types of sessions to synchronize.",
        },
    },
    "monitor-interface": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "pingsvr-monitor-interface": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "monitor-prefix": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "vdom": {
            "type": "string",
            "help": "VDOM name.",
            "required": True,
            "default": "",
            "max_length": 31,
        },
        "vrf": {
            "type": "integer",
            "help": "VRF ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 511,
        },
        "prefix": {
            "type": "ipv4-classnet-any",
            "help": "Prefix.",
            "default": "0.0.0.0 0.0.0.0",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_LAYER2_CONNECTION = [
    "available",
    "unavailable",
]
VALID_BODY_ENCRYPTION = [
    "enable",
    "disable",
]
VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL = [
    "cps-preferred",
    "strict-anti-replay",
]
VALID_BODY_HELPER_TRAFFIC_BOUNCE = [
    "enable",
    "disable",
]
VALID_BODY_UTM_TRAFFIC_BOUNCE = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_standalone_cluster_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/standalone_cluster.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_standalone_cluster_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_standalone_cluster_get(
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
    Validate required fields for system/standalone_cluster.

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


def validate_system_standalone_cluster_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/standalone_cluster object.

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
        ...     "psksecret": True,  # Pre-shared secret for session synchronization (ASC
        ... }
        >>> is_valid, error = validate_system_standalone_cluster_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "psksecret": True,
        ...     "layer2-connection": "available",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_standalone_cluster_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["layer2-connection"] = "invalid-value"
        >>> is_valid, error = validate_system_standalone_cluster_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_standalone_cluster_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "layer2-connection" in payload:
        value = payload["layer2-connection"]
        if value not in VALID_BODY_LAYER2_CONNECTION:
            desc = FIELD_DESCRIPTIONS.get("layer2-connection", "")
            error_msg = f"Invalid value for 'layer2-connection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LAYER2_CONNECTION)}"
            error_msg += f"\n  → Example: layer2-connection='{{ VALID_BODY_LAYER2_CONNECTION[0] }}'"
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
    if "asymmetric-traffic-control" in payload:
        value = payload["asymmetric-traffic-control"]
        if value not in VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL:
            desc = FIELD_DESCRIPTIONS.get("asymmetric-traffic-control", "")
            error_msg = f"Invalid value for 'asymmetric-traffic-control': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL)}"
            error_msg += f"\n  → Example: asymmetric-traffic-control='{{ VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL[0] }}'"
            return (False, error_msg)
    if "helper-traffic-bounce" in payload:
        value = payload["helper-traffic-bounce"]
        if value not in VALID_BODY_HELPER_TRAFFIC_BOUNCE:
            desc = FIELD_DESCRIPTIONS.get("helper-traffic-bounce", "")
            error_msg = f"Invalid value for 'helper-traffic-bounce': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HELPER_TRAFFIC_BOUNCE)}"
            error_msg += f"\n  → Example: helper-traffic-bounce='{{ VALID_BODY_HELPER_TRAFFIC_BOUNCE[0] }}'"
            return (False, error_msg)
    if "utm-traffic-bounce" in payload:
        value = payload["utm-traffic-bounce"]
        if value not in VALID_BODY_UTM_TRAFFIC_BOUNCE:
            desc = FIELD_DESCRIPTIONS.get("utm-traffic-bounce", "")
            error_msg = f"Invalid value for 'utm-traffic-bounce': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UTM_TRAFFIC_BOUNCE)}"
            error_msg += f"\n  → Example: utm-traffic-bounce='{{ VALID_BODY_UTM_TRAFFIC_BOUNCE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_standalone_cluster_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/standalone_cluster.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_standalone_cluster_put(payload)
    """
    # Step 1: Validate enum values
    if "layer2-connection" in payload:
        value = payload["layer2-connection"]
        if value not in VALID_BODY_LAYER2_CONNECTION:
            return (
                False,
                f"Invalid value for 'layer2-connection'='{value}'. Must be one of: {', '.join(VALID_BODY_LAYER2_CONNECTION)}",
            )
    if "encryption" in payload:
        value = payload["encryption"]
        if value not in VALID_BODY_ENCRYPTION:
            return (
                False,
                f"Invalid value for 'encryption'='{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPTION)}",
            )
    if "asymmetric-traffic-control" in payload:
        value = payload["asymmetric-traffic-control"]
        if value not in VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL:
            return (
                False,
                f"Invalid value for 'asymmetric-traffic-control'='{value}'. Must be one of: {', '.join(VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL)}",
            )
    if "helper-traffic-bounce" in payload:
        value = payload["helper-traffic-bounce"]
        if value not in VALID_BODY_HELPER_TRAFFIC_BOUNCE:
            return (
                False,
                f"Invalid value for 'helper-traffic-bounce'='{value}'. Must be one of: {', '.join(VALID_BODY_HELPER_TRAFFIC_BOUNCE)}",
            )
    if "utm-traffic-bounce" in payload:
        value = payload["utm-traffic-bounce"]
        if value not in VALID_BODY_UTM_TRAFFIC_BOUNCE:
            return (
                False,
                f"Invalid value for 'utm-traffic-bounce'='{value}'. Must be one of: {', '.join(VALID_BODY_UTM_TRAFFIC_BOUNCE)}",
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
    "endpoint": "system/standalone_cluster",
    "category": "cmdb",
    "api_path": "system/standalone-cluster",
    "help": "Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.",
    "total_fields": 13,
    "required_fields_count": 1,
    "fields_with_defaults_count": 8,
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
