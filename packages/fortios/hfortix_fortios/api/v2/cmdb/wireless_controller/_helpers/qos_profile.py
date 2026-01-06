"""
Validation helpers for wireless_controller/qos_profile endpoint.

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
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "comment": "",
    "uplink": 0,
    "downlink": 0,
    "uplink-sta": 0,
    "downlink-sta": 0,
    "burst": "disable",
    "wmm": "enable",
    "wmm-uapsd": "enable",
    "call-admission-control": "disable",
    "call-capacity": 10,
    "bandwidth-admission-control": "disable",
    "bandwidth-capacity": 2000,
    "dscp-wmm-mapping": "disable",
    "wmm-dscp-marking": "disable",
    "wmm-vo-dscp": 48,
    "wmm-vi-dscp": 32,
    "wmm-be-dscp": 0,
    "wmm-bk-dscp": 8,
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
    "name": "string",  # WiFi QoS profile name.
    "comment": "string",  # Comment.
    "uplink": "integer",  # Maximum uplink bandwidth for Virtual Access Points (VAPs) (0
    "downlink": "integer",  # Maximum downlink bandwidth for Virtual Access Points (VAPs) 
    "uplink-sta": "integer",  # Maximum uplink bandwidth for clients (0 - 2097152 Kbps, defa
    "downlink-sta": "integer",  # Maximum downlink bandwidth for clients (0 - 2097152 Kbps, de
    "burst": "option",  # Enable/disable client rate burst.
    "wmm": "option",  # Enable/disable WiFi multi-media (WMM) control.
    "wmm-uapsd": "option",  # Enable/disable WMM Unscheduled Automatic Power Save Delivery
    "call-admission-control": "option",  # Enable/disable WMM call admission control.
    "call-capacity": "integer",  # Maximum number of Voice over WLAN (VoWLAN) phones allowed (0
    "bandwidth-admission-control": "option",  # Enable/disable WMM bandwidth admission control.
    "bandwidth-capacity": "integer",  # Maximum bandwidth capacity allowed (1 - 600000 Kbps, default
    "dscp-wmm-mapping": "option",  # Enable/disable Differentiated Services Code Point (DSCP) map
    "dscp-wmm-vo": "string",  # DSCP mapping for voice access (default = 48 56).
    "dscp-wmm-vi": "string",  # DSCP mapping for video access (default = 32 40).
    "dscp-wmm-be": "string",  # DSCP mapping for best effort access (default = 0 24).
    "dscp-wmm-bk": "string",  # DSCP mapping for background access (default = 8 16).
    "wmm-dscp-marking": "option",  # Enable/disable WMM Differentiated Services Code Point (DSCP)
    "wmm-vo-dscp": "integer",  # DSCP marking for voice access (default = 48).
    "wmm-vi-dscp": "integer",  # DSCP marking for video access (default = 32).
    "wmm-be-dscp": "integer",  # DSCP marking for best effort access (default = 0).
    "wmm-bk-dscp": "integer",  # DSCP marking for background access (default = 8).
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "WiFi QoS profile name.",
    "comment": "Comment.",
    "uplink": "Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).",
    "downlink": "Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).",
    "uplink-sta": "Maximum uplink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).",
    "downlink-sta": "Maximum downlink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).",
    "burst": "Enable/disable client rate burst.",
    "wmm": "Enable/disable WiFi multi-media (WMM) control.",
    "wmm-uapsd": "Enable/disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode.",
    "call-admission-control": "Enable/disable WMM call admission control.",
    "call-capacity": "Maximum number of Voice over WLAN (VoWLAN) phones allowed (0 - 60, default = 10).",
    "bandwidth-admission-control": "Enable/disable WMM bandwidth admission control.",
    "bandwidth-capacity": "Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).",
    "dscp-wmm-mapping": "Enable/disable Differentiated Services Code Point (DSCP) mapping.",
    "dscp-wmm-vo": "DSCP mapping for voice access (default = 48 56).",
    "dscp-wmm-vi": "DSCP mapping for video access (default = 32 40).",
    "dscp-wmm-be": "DSCP mapping for best effort access (default = 0 24).",
    "dscp-wmm-bk": "DSCP mapping for background access (default = 8 16).",
    "wmm-dscp-marking": "Enable/disable WMM Differentiated Services Code Point (DSCP) marking.",
    "wmm-vo-dscp": "DSCP marking for voice access (default = 48).",
    "wmm-vi-dscp": "DSCP marking for video access (default = 32).",
    "wmm-be-dscp": "DSCP marking for best effort access (default = 0).",
    "wmm-bk-dscp": "DSCP marking for background access (default = 8).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "comment": {"type": "string", "max_length": 63},
    "uplink": {"type": "integer", "min": 0, "max": 2097152},
    "downlink": {"type": "integer", "min": 0, "max": 2097152},
    "uplink-sta": {"type": "integer", "min": 0, "max": 2097152},
    "downlink-sta": {"type": "integer", "min": 0, "max": 2097152},
    "call-capacity": {"type": "integer", "min": 0, "max": 60},
    "bandwidth-capacity": {"type": "integer", "min": 1, "max": 600000},
    "wmm-vo-dscp": {"type": "integer", "min": 0, "max": 63},
    "wmm-vi-dscp": {"type": "integer", "min": 0, "max": 63},
    "wmm-be-dscp": {"type": "integer", "min": 0, "max": 63},
    "wmm-bk-dscp": {"type": "integer", "min": 0, "max": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "dscp-wmm-vo": {
        "id": {
            "type": "integer",
            "help": "DSCP WMM mapping numbers (0 - 63).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
    },
    "dscp-wmm-vi": {
        "id": {
            "type": "integer",
            "help": "DSCP WMM mapping numbers (0 - 63).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
    },
    "dscp-wmm-be": {
        "id": {
            "type": "integer",
            "help": "DSCP WMM mapping numbers (0 - 63).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
    },
    "dscp-wmm-bk": {
        "id": {
            "type": "integer",
            "help": "DSCP WMM mapping numbers (0 - 63).",
            "default": 0,
            "min_value": 0,
            "max_value": 63,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_BURST = [
    "enable",  # Enable client rate burst.
    "disable",  # Disable client rate burst.
]
VALID_BODY_WMM = [
    "enable",  # Enable WiFi multi-media (WMM) control.
    "disable",  # Disable WiFi multi-media (WMM) control.
]
VALID_BODY_WMM_UAPSD = [
    "enable",  # Enable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode.
    "disable",  # Disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode.
]
VALID_BODY_CALL_ADMISSION_CONTROL = [
    "enable",  # Enable WMM call admission control.
    "disable",  # Disable WMM call admission control.
]
VALID_BODY_BANDWIDTH_ADMISSION_CONTROL = [
    "enable",  # Enable WMM bandwidth admission control.
    "disable",  # Disable WMM bandwidth admission control.
]
VALID_BODY_DSCP_WMM_MAPPING = [
    "enable",  # Enable Differentiated Services Code Point (DSCP) mapping.
    "disable",  # Disable Differentiated Services Code Point (DSCP) mapping.
]
VALID_BODY_WMM_DSCP_MARKING = [
    "enable",  # Enable WMM Differentiated Services Code Point (DSCP) marking.
    "disable",  # Disable WMM Differentiated Services Code Point (DSCP) marking.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_qos_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for wireless_controller/qos_profile.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_wireless_controller_qos_profile_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_wireless_controller_qos_profile_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_wireless_controller_qos_profile_get(
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
    Validate required fields for wireless_controller/qos_profile.

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


def validate_wireless_controller_qos_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new wireless_controller/qos_profile object.

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
        ... }
        >>> is_valid, error = validate_wireless_controller_qos_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "burst": "{'name': 'enable', 'help': 'Enable client rate burst.', 'label': 'Enable', 'description': 'Enable client rate burst'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_wireless_controller_qos_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["burst"] = "invalid-value"
        >>> is_valid, error = validate_wireless_controller_qos_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_wireless_controller_qos_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "burst" in payload:
        value = payload["burst"]
        if value not in VALID_BODY_BURST:
            desc = FIELD_DESCRIPTIONS.get("burst", "")
            error_msg = f"Invalid value for 'burst': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BURST)}"
            error_msg += f"\n  → Example: burst='{{ VALID_BODY_BURST[0] }}'"
            return (False, error_msg)
    if "wmm" in payload:
        value = payload["wmm"]
        if value not in VALID_BODY_WMM:
            desc = FIELD_DESCRIPTIONS.get("wmm", "")
            error_msg = f"Invalid value for 'wmm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WMM)}"
            error_msg += f"\n  → Example: wmm='{{ VALID_BODY_WMM[0] }}'"
            return (False, error_msg)
    if "wmm-uapsd" in payload:
        value = payload["wmm-uapsd"]
        if value not in VALID_BODY_WMM_UAPSD:
            desc = FIELD_DESCRIPTIONS.get("wmm-uapsd", "")
            error_msg = f"Invalid value for 'wmm-uapsd': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WMM_UAPSD)}"
            error_msg += f"\n  → Example: wmm-uapsd='{{ VALID_BODY_WMM_UAPSD[0] }}'"
            return (False, error_msg)
    if "call-admission-control" in payload:
        value = payload["call-admission-control"]
        if value not in VALID_BODY_CALL_ADMISSION_CONTROL:
            desc = FIELD_DESCRIPTIONS.get("call-admission-control", "")
            error_msg = f"Invalid value for 'call-admission-control': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CALL_ADMISSION_CONTROL)}"
            error_msg += f"\n  → Example: call-admission-control='{{ VALID_BODY_CALL_ADMISSION_CONTROL[0] }}'"
            return (False, error_msg)
    if "bandwidth-admission-control" in payload:
        value = payload["bandwidth-admission-control"]
        if value not in VALID_BODY_BANDWIDTH_ADMISSION_CONTROL:
            desc = FIELD_DESCRIPTIONS.get("bandwidth-admission-control", "")
            error_msg = f"Invalid value for 'bandwidth-admission-control': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BANDWIDTH_ADMISSION_CONTROL)}"
            error_msg += f"\n  → Example: bandwidth-admission-control='{{ VALID_BODY_BANDWIDTH_ADMISSION_CONTROL[0] }}'"
            return (False, error_msg)
    if "dscp-wmm-mapping" in payload:
        value = payload["dscp-wmm-mapping"]
        if value not in VALID_BODY_DSCP_WMM_MAPPING:
            desc = FIELD_DESCRIPTIONS.get("dscp-wmm-mapping", "")
            error_msg = f"Invalid value for 'dscp-wmm-mapping': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DSCP_WMM_MAPPING)}"
            error_msg += f"\n  → Example: dscp-wmm-mapping='{{ VALID_BODY_DSCP_WMM_MAPPING[0] }}'"
            return (False, error_msg)
    if "wmm-dscp-marking" in payload:
        value = payload["wmm-dscp-marking"]
        if value not in VALID_BODY_WMM_DSCP_MARKING:
            desc = FIELD_DESCRIPTIONS.get("wmm-dscp-marking", "")
            error_msg = f"Invalid value for 'wmm-dscp-marking': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WMM_DSCP_MARKING)}"
            error_msg += f"\n  → Example: wmm-dscp-marking='{{ VALID_BODY_WMM_DSCP_MARKING[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_qos_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update wireless_controller/qos_profile.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_wireless_controller_qos_profile_put(payload)
    """
    # Step 1: Validate enum values
    if "burst" in payload:
        value = payload["burst"]
        if value not in VALID_BODY_BURST:
            return (
                False,
                f"Invalid value for 'burst'='{value}'. Must be one of: {', '.join(VALID_BODY_BURST)}",
            )
    if "wmm" in payload:
        value = payload["wmm"]
        if value not in VALID_BODY_WMM:
            return (
                False,
                f"Invalid value for 'wmm'='{value}'. Must be one of: {', '.join(VALID_BODY_WMM)}",
            )
    if "wmm-uapsd" in payload:
        value = payload["wmm-uapsd"]
        if value not in VALID_BODY_WMM_UAPSD:
            return (
                False,
                f"Invalid value for 'wmm-uapsd'='{value}'. Must be one of: {', '.join(VALID_BODY_WMM_UAPSD)}",
            )
    if "call-admission-control" in payload:
        value = payload["call-admission-control"]
        if value not in VALID_BODY_CALL_ADMISSION_CONTROL:
            return (
                False,
                f"Invalid value for 'call-admission-control'='{value}'. Must be one of: {', '.join(VALID_BODY_CALL_ADMISSION_CONTROL)}",
            )
    if "bandwidth-admission-control" in payload:
        value = payload["bandwidth-admission-control"]
        if value not in VALID_BODY_BANDWIDTH_ADMISSION_CONTROL:
            return (
                False,
                f"Invalid value for 'bandwidth-admission-control'='{value}'. Must be one of: {', '.join(VALID_BODY_BANDWIDTH_ADMISSION_CONTROL)}",
            )
    if "dscp-wmm-mapping" in payload:
        value = payload["dscp-wmm-mapping"]
        if value not in VALID_BODY_DSCP_WMM_MAPPING:
            return (
                False,
                f"Invalid value for 'dscp-wmm-mapping'='{value}'. Must be one of: {', '.join(VALID_BODY_DSCP_WMM_MAPPING)}",
            )
    if "wmm-dscp-marking" in payload:
        value = payload["wmm-dscp-marking"]
        if value not in VALID_BODY_WMM_DSCP_MARKING:
            return (
                False,
                f"Invalid value for 'wmm-dscp-marking'='{value}'. Must be one of: {', '.join(VALID_BODY_WMM_DSCP_MARKING)}",
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
    "endpoint": "wireless_controller/qos_profile",
    "category": "cmdb",
    "api_path": "wireless-controller/qos-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure WiFi quality of service (QoS) profiles.",
    "total_fields": 23,
    "required_fields_count": 0,
    "fields_with_defaults_count": 19,
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
