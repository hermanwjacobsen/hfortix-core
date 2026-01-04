"""
Validation helpers for firewall/local_in_policy endpoint.

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
    "intf",  # Incoming interface name from available options.
    "srcaddr",  # Source address object from available options.
    "dstaddr",  # Destination address object from available options.
    "service",  # Service object from available options.
    "schedule",  # Schedule object from available options.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "policyid": 0,
    "uuid": "00000000-0000-0000-0000-000000000000",
    "ha-mgmt-intf-only": "disable",
    "srcaddr-negate": "disable",
    "internet-service-src": "disable",
    "dstaddr-negate": "disable",
    "action": "deny",
    "service-negate": "disable",
    "internet-service-src-negate": "disable",
    "schedule": "",
    "status": "enable",
    "virtual-patch": "disable",
    "logtraffic": "disable",
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
    "policyid": "integer",  # User defined local in policy ID.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "ha-mgmt-intf-only": "option",  # Enable/disable dedicating the HA management interface only f
    "intf": "string",  # Incoming interface name from available options.
    "srcaddr": "string",  # Source address object from available options.
    "srcaddr-negate": "option",  # When enabled srcaddr specifies what the source address must 
    "dstaddr": "string",  # Destination address object from available options.
    "internet-service-src": "option",  # Enable/disable use of Internet Services in source for this l
    "internet-service-src-name": "string",  # Internet Service source name.
    "internet-service-src-group": "string",  # Internet Service source group name.
    "internet-service-src-custom": "string",  # Custom Internet Service source name.
    "internet-service-src-custom-group": "string",  # Custom Internet Service source group name.
    "internet-service-src-fortiguard": "string",  # FortiGuard Internet Service source name.
    "dstaddr-negate": "option",  # When enabled dstaddr specifies what the destination address 
    "action": "option",  # Action performed on traffic matching the policy (default = d
    "service": "string",  # Service object from available options.
    "service-negate": "option",  # When enabled service specifies what the service must NOT be.
    "internet-service-src-negate": "option",  # When enabled internet-service-src specifies what the service
    "schedule": "string",  # Schedule object from available options.
    "status": "option",  # Enable/disable this local-in policy.
    "virtual-patch": "option",  # Enable/disable virtual patching.
    "logtraffic": "option",  # Enable/disable local-in traffic logging.
    "comments": "var-string",  # Comment.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "policyid": "User defined local in policy ID.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "ha-mgmt-intf-only": "Enable/disable dedicating the HA management interface only for local-in policy.",
    "intf": "Incoming interface name from available options.",
    "srcaddr": "Source address object from available options.",
    "srcaddr-negate": "When enabled srcaddr specifies what the source address must NOT be.",
    "dstaddr": "Destination address object from available options.",
    "internet-service-src": "Enable/disable use of Internet Services in source for this local-in policy. If enabled, source address is not used.",
    "internet-service-src-name": "Internet Service source name.",
    "internet-service-src-group": "Internet Service source group name.",
    "internet-service-src-custom": "Custom Internet Service source name.",
    "internet-service-src-custom-group": "Custom Internet Service source group name.",
    "internet-service-src-fortiguard": "FortiGuard Internet Service source name.",
    "dstaddr-negate": "When enabled dstaddr specifies what the destination address must NOT be.",
    "action": "Action performed on traffic matching the policy (default = deny).",
    "service": "Service object from available options.",
    "service-negate": "When enabled service specifies what the service must NOT be.",
    "internet-service-src-negate": "When enabled internet-service-src specifies what the service must NOT be.",
    "schedule": "Schedule object from available options.",
    "status": "Enable/disable this local-in policy.",
    "virtual-patch": "Enable/disable virtual patching.",
    "logtraffic": "Enable/disable local-in traffic logging.",
    "comments": "Comment.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "policyid": {"type": "integer", "min": 0, "max": 4294967295},
    "schedule": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "intf": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "srcaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dstaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-name": {
        "name": {
            "type": "string",
            "help": "Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-group": {
        "name": {
            "type": "string",
            "help": "Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-custom": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-fortiguard": {
        "name": {
            "type": "string",
            "help": "FortiGuard Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "service": {
        "name": {
            "type": "string",
            "help": "Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_HA_MGMT_INTF_ONLY = [
    "enable",
    "disable",
]
VALID_BODY_SRCADDR_NEGATE = [
    "enable",
    "disable",
]
VALID_BODY_INTERNET_SERVICE_SRC = [
    "enable",
    "disable",
]
VALID_BODY_DSTADDR_NEGATE = [
    "enable",
    "disable",
]
VALID_BODY_ACTION = [
    "accept",
    "deny",
]
VALID_BODY_SERVICE_NEGATE = [
    "enable",
    "disable",
]
VALID_BODY_INTERNET_SERVICE_SRC_NEGATE = [
    "enable",
    "disable",
]
VALID_BODY_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_VIRTUAL_PATCH = [
    "enable",
    "disable",
]
VALID_BODY_LOGTRAFFIC = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_local_in_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for firewall/local_in_policy.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_firewall_local_in_policy_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by policyid
        >>> is_valid, error = validate_firewall_local_in_policy_get(policyid="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_firewall_local_in_policy_get(
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
    Validate required fields for firewall/local_in_policy.

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


def validate_firewall_local_in_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new firewall/local_in_policy object.

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
        ...     "intf": True,  # Incoming interface name from available options.
        ...     "srcaddr": True,  # Source address object from available options.
        ... }
        >>> is_valid, error = validate_firewall_local_in_policy_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "intf": True,
        ...     "ha-mgmt-intf-only": "enable",  # Valid enum value
        ... }
        >>> is_valid, error = validate_firewall_local_in_policy_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["ha-mgmt-intf-only"] = "invalid-value"
        >>> is_valid, error = validate_firewall_local_in_policy_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_firewall_local_in_policy_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "ha-mgmt-intf-only" in payload:
        value = payload["ha-mgmt-intf-only"]
        if value not in VALID_BODY_HA_MGMT_INTF_ONLY:
            desc = FIELD_DESCRIPTIONS.get("ha-mgmt-intf-only", "")
            error_msg = f"Invalid value for 'ha-mgmt-intf-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HA_MGMT_INTF_ONLY)}"
            error_msg += f"\n  → Example: ha-mgmt-intf-only='{{ VALID_BODY_HA_MGMT_INTF_ONLY[0] }}'"
            return (False, error_msg)
    if "srcaddr-negate" in payload:
        value = payload["srcaddr-negate"]
        if value not in VALID_BODY_SRCADDR_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("srcaddr-negate", "")
            error_msg = f"Invalid value for 'srcaddr-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SRCADDR_NEGATE)}"
            error_msg += f"\n  → Example: srcaddr-negate='{{ VALID_BODY_SRCADDR_NEGATE[0] }}'"
            return (False, error_msg)
    if "internet-service-src" in payload:
        value = payload["internet-service-src"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC:
            desc = FIELD_DESCRIPTIONS.get("internet-service-src", "")
            error_msg = f"Invalid value for 'internet-service-src': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE_SRC)}"
            error_msg += f"\n  → Example: internet-service-src='{{ VALID_BODY_INTERNET_SERVICE_SRC[0] }}'"
            return (False, error_msg)
    if "dstaddr-negate" in payload:
        value = payload["dstaddr-negate"]
        if value not in VALID_BODY_DSTADDR_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("dstaddr-negate", "")
            error_msg = f"Invalid value for 'dstaddr-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DSTADDR_NEGATE)}"
            error_msg += f"\n  → Example: dstaddr-negate='{{ VALID_BODY_DSTADDR_NEGATE[0] }}'"
            return (False, error_msg)
    if "action" in payload:
        value = payload["action"]
        if value not in VALID_BODY_ACTION:
            desc = FIELD_DESCRIPTIONS.get("action", "")
            error_msg = f"Invalid value for 'action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACTION)}"
            error_msg += f"\n  → Example: action='{{ VALID_BODY_ACTION[0] }}'"
            return (False, error_msg)
    if "service-negate" in payload:
        value = payload["service-negate"]
        if value not in VALID_BODY_SERVICE_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("service-negate", "")
            error_msg = f"Invalid value for 'service-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVICE_NEGATE)}"
            error_msg += f"\n  → Example: service-negate='{{ VALID_BODY_SERVICE_NEGATE[0] }}'"
            return (False, error_msg)
    if "internet-service-src-negate" in payload:
        value = payload["internet-service-src-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("internet-service-src-negate", "")
            error_msg = f"Invalid value for 'internet-service-src-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE_SRC_NEGATE)}"
            error_msg += f"\n  → Example: internet-service-src-negate='{{ VALID_BODY_INTERNET_SERVICE_SRC_NEGATE[0] }}'"
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
    if "virtual-patch" in payload:
        value = payload["virtual-patch"]
        if value not in VALID_BODY_VIRTUAL_PATCH:
            desc = FIELD_DESCRIPTIONS.get("virtual-patch", "")
            error_msg = f"Invalid value for 'virtual-patch': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VIRTUAL_PATCH)}"
            error_msg += f"\n  → Example: virtual-patch='{{ VALID_BODY_VIRTUAL_PATCH[0] }}'"
            return (False, error_msg)
    if "logtraffic" in payload:
        value = payload["logtraffic"]
        if value not in VALID_BODY_LOGTRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("logtraffic", "")
            error_msg = f"Invalid value for 'logtraffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGTRAFFIC)}"
            error_msg += f"\n  → Example: logtraffic='{{ VALID_BODY_LOGTRAFFIC[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_local_in_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update firewall/local_in_policy.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_firewall_local_in_policy_put(payload)
    """
    # Step 1: Validate enum values
    if "ha-mgmt-intf-only" in payload:
        value = payload["ha-mgmt-intf-only"]
        if value not in VALID_BODY_HA_MGMT_INTF_ONLY:
            return (
                False,
                f"Invalid value for 'ha-mgmt-intf-only'='{value}'. Must be one of: {', '.join(VALID_BODY_HA_MGMT_INTF_ONLY)}",
            )
    if "srcaddr-negate" in payload:
        value = payload["srcaddr-negate"]
        if value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid value for 'srcaddr-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )
    if "internet-service-src" in payload:
        value = payload["internet-service-src"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid value for 'internet-service-src'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )
    if "dstaddr-negate" in payload:
        value = payload["dstaddr-negate"]
        if value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid value for 'dstaddr-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
            )
    if "action" in payload:
        value = payload["action"]
        if value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid value for 'action'='{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )
    if "service-negate" in payload:
        value = payload["service-negate"]
        if value not in VALID_BODY_SERVICE_NEGATE:
            return (
                False,
                f"Invalid value for 'service-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_NEGATE)}",
            )
    if "internet-service-src-negate" in payload:
        value = payload["internet-service-src-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC_NEGATE:
            return (
                False,
                f"Invalid value for 'internet-service-src-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC_NEGATE)}",
            )
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "virtual-patch" in payload:
        value = payload["virtual-patch"]
        if value not in VALID_BODY_VIRTUAL_PATCH:
            return (
                False,
                f"Invalid value for 'virtual-patch'='{value}'. Must be one of: {', '.join(VALID_BODY_VIRTUAL_PATCH)}",
            )
    if "logtraffic" in payload:
        value = payload["logtraffic"]
        if value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid value for 'logtraffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
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
    "endpoint": "firewall/local_in_policy",
    "category": "cmdb",
    "api_path": "firewall/local-in-policy",
    "mkey": "policyid",
    "mkey_type": "integer",
    "help": "Configure user defined IPv4 local-in policies.",
    "total_fields": 23,
    "required_fields_count": 5,
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
