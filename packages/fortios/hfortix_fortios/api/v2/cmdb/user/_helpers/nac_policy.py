"""
Validation helpers for user/nac_policy endpoint.

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
    "description": "",
    "category": "device",
    "status": "enable",
    "match-type": "dynamic",
    "match-period": 0,
    "match-remove": "default",
    "mac": "",
    "hw-vendor": "",
    "type": "",
    "family": "",
    "os": "",
    "hw-version": "",
    "sw-version": "",
    "host": "",
    "user": "",
    "src": "",
    "user-group": "",
    "ems-tag": "",
    "fortivoice-tag": "",
    "switch-fortilink": "",
    "switch-mac-policy": "",
    "firewall-address": "",
    "ssid-policy": "",
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
    "name": "string",  # NAC policy name.
    "description": "string",  # Description for the NAC policy matching pattern.
    "category": "option",  # Category of NAC policy.
    "status": "option",  # Enable/disable NAC policy.
    "match-type": "option",  # Match and retain the devices based on the type.
    "match-period": "integer",  # Number of days the matched devices will be retained (0 - alw
    "match-remove": "option",  # Options to remove the matched override devices.
    "mac": "string",  # NAC policy matching MAC address.
    "hw-vendor": "string",  # NAC policy matching hardware vendor.
    "type": "string",  # NAC policy matching type.
    "family": "string",  # NAC policy matching family.
    "os": "string",  # NAC policy matching operating system.
    "hw-version": "string",  # NAC policy matching hardware version.
    "sw-version": "string",  # NAC policy matching software version.
    "host": "string",  # NAC policy matching host.
    "user": "string",  # NAC policy matching user.
    "src": "string",  # NAC policy matching source.
    "user-group": "string",  # NAC policy matching user group.
    "ems-tag": "string",  # NAC policy matching EMS tag.
    "fortivoice-tag": "string",  # NAC policy matching FortiVoice tag.
    "severity": "string",  # NAC policy matching devices vulnerability severity lists.
    "switch-fortilink": "string",  # FortiLink interface for which this NAC policy belongs to.
    "switch-group": "string",  # List of managed FortiSwitch groups on which NAC policy can b
    "switch-mac-policy": "string",  # Switch MAC policy action to be applied on the matched NAC po
    "firewall-address": "string",  # Dynamic firewall address to associate MAC which match this p
    "ssid-policy": "string",  # SSID policy to be applied on the matched NAC policy.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "NAC policy name.",
    "description": "Description for the NAC policy matching pattern.",
    "category": "Category of NAC policy.",
    "status": "Enable/disable NAC policy.",
    "match-type": "Match and retain the devices based on the type.",
    "match-period": "Number of days the matched devices will be retained (0 - always retain)",
    "match-remove": "Options to remove the matched override devices.",
    "mac": "NAC policy matching MAC address.",
    "hw-vendor": "NAC policy matching hardware vendor.",
    "type": "NAC policy matching type.",
    "family": "NAC policy matching family.",
    "os": "NAC policy matching operating system.",
    "hw-version": "NAC policy matching hardware version.",
    "sw-version": "NAC policy matching software version.",
    "host": "NAC policy matching host.",
    "user": "NAC policy matching user.",
    "src": "NAC policy matching source.",
    "user-group": "NAC policy matching user group.",
    "ems-tag": "NAC policy matching EMS tag.",
    "fortivoice-tag": "NAC policy matching FortiVoice tag.",
    "severity": "NAC policy matching devices vulnerability severity lists.",
    "switch-fortilink": "FortiLink interface for which this NAC policy belongs to.",
    "switch-group": "List of managed FortiSwitch groups on which NAC policy can be applied.",
    "switch-mac-policy": "Switch MAC policy action to be applied on the matched NAC policy.",
    "firewall-address": "Dynamic firewall address to associate MAC which match this policy.",
    "ssid-policy": "SSID policy to be applied on the matched NAC policy.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
    "description": {"type": "string", "max_length": 63},
    "match-period": {"type": "integer", "min": 0, "max": 120},
    "mac": {"type": "string", "max_length": 17},
    "hw-vendor": {"type": "string", "max_length": 15},
    "type": {"type": "string", "max_length": 15},
    "family": {"type": "string", "max_length": 31},
    "os": {"type": "string", "max_length": 31},
    "hw-version": {"type": "string", "max_length": 15},
    "sw-version": {"type": "string", "max_length": 15},
    "host": {"type": "string", "max_length": 64},
    "user": {"type": "string", "max_length": 64},
    "src": {"type": "string", "max_length": 15},
    "user-group": {"type": "string", "max_length": 35},
    "ems-tag": {"type": "string", "max_length": 79},
    "fortivoice-tag": {"type": "string", "max_length": 79},
    "switch-fortilink": {"type": "string", "max_length": 15},
    "switch-mac-policy": {"type": "string", "max_length": 63},
    "firewall-address": {"type": "string", "max_length": 79},
    "ssid-policy": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "severity": {
        "severity-num": {
            "type": "integer",
            "help": "Enter multiple severity levels, where 0 = Info, 1 = Low, ..., 4 = Critical",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4,
        },
    },
    "switch-group": {
        "name": {
            "type": "string",
            "help": "Managed FortiSwitch group name from available options.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_CATEGORY = [
    "device",  # Device category.
    "firewall-user",  # Firewall user category.
    "ems-tag",  # EMS Tag category.
    "fortivoice-tag",  # FortiVoice Tag category.
    "vulnerability",  # Vulnerability category.
]
VALID_BODY_STATUS = [
    "enable",  # Enable NAC policy.
    "disable",  # Disable NAC policy.
]
VALID_BODY_MATCH_TYPE = [
    "dynamic",  # Matched devices will be removed on dynamic events like link-down,device-inactivity,switch-offline.
    "override",  # Matched devices will be retained until the match-period.
]
VALID_BODY_MATCH_REMOVE = [
    "default",  # Remove the matched override devices based on the match period.
    "link-down",  # Remove the matched override devices based on switch port link down event.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_nac_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for user/nac_policy.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_user_nac_policy_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_user_nac_policy_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_user_nac_policy_get(
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
    Validate required fields for user/nac_policy.

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


def validate_user_nac_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new user/nac_policy object.

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
        >>> is_valid, error = validate_user_nac_policy_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "category": "{'name': 'device', 'help': 'Device category.', 'label': 'Device', 'description': 'Device category'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_user_nac_policy_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["category"] = "invalid-value"
        >>> is_valid, error = validate_user_nac_policy_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_user_nac_policy_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "category" in payload:
        value = payload["category"]
        if value not in VALID_BODY_CATEGORY:
            desc = FIELD_DESCRIPTIONS.get("category", "")
            error_msg = f"Invalid value for 'category': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CATEGORY)}"
            error_msg += f"\n  → Example: category='{{ VALID_BODY_CATEGORY[0] }}'"
            return (False, error_msg)
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
    if "match-type" in payload:
        value = payload["match-type"]
        if value not in VALID_BODY_MATCH_TYPE:
            desc = FIELD_DESCRIPTIONS.get("match-type", "")
            error_msg = f"Invalid value for 'match-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MATCH_TYPE)}"
            error_msg += f"\n  → Example: match-type='{{ VALID_BODY_MATCH_TYPE[0] }}'"
            return (False, error_msg)
    if "match-remove" in payload:
        value = payload["match-remove"]
        if value not in VALID_BODY_MATCH_REMOVE:
            desc = FIELD_DESCRIPTIONS.get("match-remove", "")
            error_msg = f"Invalid value for 'match-remove': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MATCH_REMOVE)}"
            error_msg += f"\n  → Example: match-remove='{{ VALID_BODY_MATCH_REMOVE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_nac_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update user/nac_policy.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_user_nac_policy_put(payload)
    """
    # Step 1: Validate enum values
    if "category" in payload:
        value = payload["category"]
        if value not in VALID_BODY_CATEGORY:
            return (
                False,
                f"Invalid value for 'category'='{value}'. Must be one of: {', '.join(VALID_BODY_CATEGORY)}",
            )
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "match-type" in payload:
        value = payload["match-type"]
        if value not in VALID_BODY_MATCH_TYPE:
            return (
                False,
                f"Invalid value for 'match-type'='{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_TYPE)}",
            )
    if "match-remove" in payload:
        value = payload["match-remove"]
        if value not in VALID_BODY_MATCH_REMOVE:
            return (
                False,
                f"Invalid value for 'match-remove'='{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_REMOVE)}",
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
    "endpoint": "user/nac_policy",
    "category": "cmdb",
    "api_path": "user/nac-policy",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure NAC policy matching pattern to identify matching NAC devices.",
    "total_fields": 26,
    "required_fields_count": 0,
    "fields_with_defaults_count": 24,
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
