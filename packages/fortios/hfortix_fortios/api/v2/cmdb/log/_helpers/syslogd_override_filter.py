"""
Validation helpers for log/syslogd_override_filter endpoint.

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
    "severity": "information",
    "forward-traffic": "enable",
    "local-traffic": "enable",
    "multicast-traffic": "enable",
    "sniffer-traffic": "enable",
    "ztna-traffic": "enable",
    "http-transaction": "enable",
    "anomaly": "enable",
    "voip": "enable",
    "gtp": "enable",
    "forti-switch": "enable",
    "debug": "disable",
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
    "severity": "option",  # Lowest severity level to log.
    "forward-traffic": "option",  # Enable/disable forward traffic logging.
    "local-traffic": "option",  # Enable/disable local in or out traffic logging.
    "multicast-traffic": "option",  # Enable/disable multicast traffic logging.
    "sniffer-traffic": "option",  # Enable/disable sniffer traffic logging.
    "ztna-traffic": "option",  # Enable/disable ztna traffic logging.
    "http-transaction": "option",  # Enable/disable log HTTP transaction messages.
    "anomaly": "option",  # Enable/disable anomaly logging.
    "voip": "option",  # Enable/disable VoIP logging.
    "gtp": "option",  # Enable/disable GTP messages logging.
    "forti-switch": "option",  # Enable/disable Forti-Switch logging.
    "debug": "option",  # Enable/disable debug logging.
    "free-style": "string",  # Free style filters.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "severity": "Lowest severity level to log.",
    "forward-traffic": "Enable/disable forward traffic logging.",
    "local-traffic": "Enable/disable local in or out traffic logging.",
    "multicast-traffic": "Enable/disable multicast traffic logging.",
    "sniffer-traffic": "Enable/disable sniffer traffic logging.",
    "ztna-traffic": "Enable/disable ztna traffic logging.",
    "http-transaction": "Enable/disable log HTTP transaction messages.",
    "anomaly": "Enable/disable anomaly logging.",
    "voip": "Enable/disable VoIP logging.",
    "gtp": "Enable/disable GTP messages logging.",
    "forti-switch": "Enable/disable Forti-Switch logging.",
    "debug": "Enable/disable debug logging.",
    "free-style": "Free style filters.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "free-style": {
        "id": {
            "type": "integer",
            "help": "Entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "category": {
            "type": "option",
            "help": "Log category.",
            "required": True,
            "default": "traffic",
            "options": ["traffic", "event", "virus", "webfilter", "attack", "spam", "anomaly", "voip", "dlp", "app-ctrl", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "virtual-patch", "debug"],
        },
        "filter": {
            "type": "string",
            "help": "Free style filter string.",
            "required": True,
            "default": "",
            "max_length": 1023,
        },
        "filter-type": {
            "type": "option",
            "help": "Include/exclude logs that match the filter.",
            "default": "include",
            "options": ["include", "exclude"],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_SEVERITY = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
VALID_BODY_FORWARD_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_LOCAL_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_MULTICAST_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_SNIFFER_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_ZTNA_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_HTTP_TRANSACTION = [
    "enable",
    "disable",
]
VALID_BODY_ANOMALY = [
    "enable",
    "disable",
]
VALID_BODY_VOIP = [
    "enable",
    "disable",
]
VALID_BODY_GTP = [
    "enable",
    "disable",
]
VALID_BODY_FORTI_SWITCH = [
    "enable",
    "disable",
]
VALID_BODY_DEBUG = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_log_syslogd_override_filter_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for log/syslogd_override_filter.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_log_syslogd_override_filter_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_log_syslogd_override_filter_get(
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
    Validate required fields for log/syslogd_override_filter.

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


def validate_log_syslogd_override_filter_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new log/syslogd_override_filter object.

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
        >>> is_valid, error = validate_log_syslogd_override_filter_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "severity": "emergency",  # Valid enum value
        ... }
        >>> is_valid, error = validate_log_syslogd_override_filter_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["severity"] = "invalid-value"
        >>> is_valid, error = validate_log_syslogd_override_filter_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_log_syslogd_override_filter_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "severity" in payload:
        value = payload["severity"]
        if value not in VALID_BODY_SEVERITY:
            desc = FIELD_DESCRIPTIONS.get("severity", "")
            error_msg = f"Invalid value for 'severity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SEVERITY)}"
            error_msg += f"\n  → Example: severity='{{ VALID_BODY_SEVERITY[0] }}'"
            return (False, error_msg)
    if "forward-traffic" in payload:
        value = payload["forward-traffic"]
        if value not in VALID_BODY_FORWARD_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("forward-traffic", "")
            error_msg = f"Invalid value for 'forward-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORWARD_TRAFFIC)}"
            error_msg += f"\n  → Example: forward-traffic='{{ VALID_BODY_FORWARD_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "local-traffic" in payload:
        value = payload["local-traffic"]
        if value not in VALID_BODY_LOCAL_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("local-traffic", "")
            error_msg = f"Invalid value for 'local-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_TRAFFIC)}"
            error_msg += f"\n  → Example: local-traffic='{{ VALID_BODY_LOCAL_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "multicast-traffic" in payload:
        value = payload["multicast-traffic"]
        if value not in VALID_BODY_MULTICAST_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("multicast-traffic", "")
            error_msg = f"Invalid value for 'multicast-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTICAST_TRAFFIC)}"
            error_msg += f"\n  → Example: multicast-traffic='{{ VALID_BODY_MULTICAST_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "sniffer-traffic" in payload:
        value = payload["sniffer-traffic"]
        if value not in VALID_BODY_SNIFFER_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("sniffer-traffic", "")
            error_msg = f"Invalid value for 'sniffer-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SNIFFER_TRAFFIC)}"
            error_msg += f"\n  → Example: sniffer-traffic='{{ VALID_BODY_SNIFFER_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "ztna-traffic" in payload:
        value = payload["ztna-traffic"]
        if value not in VALID_BODY_ZTNA_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("ztna-traffic", "")
            error_msg = f"Invalid value for 'ztna-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ZTNA_TRAFFIC)}"
            error_msg += f"\n  → Example: ztna-traffic='{{ VALID_BODY_ZTNA_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "http-transaction" in payload:
        value = payload["http-transaction"]
        if value not in VALID_BODY_HTTP_TRANSACTION:
            desc = FIELD_DESCRIPTIONS.get("http-transaction", "")
            error_msg = f"Invalid value for 'http-transaction': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_TRANSACTION)}"
            error_msg += f"\n  → Example: http-transaction='{{ VALID_BODY_HTTP_TRANSACTION[0] }}'"
            return (False, error_msg)
    if "anomaly" in payload:
        value = payload["anomaly"]
        if value not in VALID_BODY_ANOMALY:
            desc = FIELD_DESCRIPTIONS.get("anomaly", "")
            error_msg = f"Invalid value for 'anomaly': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ANOMALY)}"
            error_msg += f"\n  → Example: anomaly='{{ VALID_BODY_ANOMALY[0] }}'"
            return (False, error_msg)
    if "voip" in payload:
        value = payload["voip"]
        if value not in VALID_BODY_VOIP:
            desc = FIELD_DESCRIPTIONS.get("voip", "")
            error_msg = f"Invalid value for 'voip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VOIP)}"
            error_msg += f"\n  → Example: voip='{{ VALID_BODY_VOIP[0] }}'"
            return (False, error_msg)
    if "gtp" in payload:
        value = payload["gtp"]
        if value not in VALID_BODY_GTP:
            desc = FIELD_DESCRIPTIONS.get("gtp", "")
            error_msg = f"Invalid value for 'gtp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GTP)}"
            error_msg += f"\n  → Example: gtp='{{ VALID_BODY_GTP[0] }}'"
            return (False, error_msg)
    if "forti-switch" in payload:
        value = payload["forti-switch"]
        if value not in VALID_BODY_FORTI_SWITCH:
            desc = FIELD_DESCRIPTIONS.get("forti-switch", "")
            error_msg = f"Invalid value for 'forti-switch': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTI_SWITCH)}"
            error_msg += f"\n  → Example: forti-switch='{{ VALID_BODY_FORTI_SWITCH[0] }}'"
            return (False, error_msg)
    if "debug" in payload:
        value = payload["debug"]
        if value not in VALID_BODY_DEBUG:
            desc = FIELD_DESCRIPTIONS.get("debug", "")
            error_msg = f"Invalid value for 'debug': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEBUG)}"
            error_msg += f"\n  → Example: debug='{{ VALID_BODY_DEBUG[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_log_syslogd_override_filter_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update log/syslogd_override_filter.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_log_syslogd_override_filter_put(payload)
    """
    # Step 1: Validate enum values
    if "severity" in payload:
        value = payload["severity"]
        if value not in VALID_BODY_SEVERITY:
            return (
                False,
                f"Invalid value for 'severity'='{value}'. Must be one of: {', '.join(VALID_BODY_SEVERITY)}",
            )
    if "forward-traffic" in payload:
        value = payload["forward-traffic"]
        if value not in VALID_BODY_FORWARD_TRAFFIC:
            return (
                False,
                f"Invalid value for 'forward-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_FORWARD_TRAFFIC)}",
            )
    if "local-traffic" in payload:
        value = payload["local-traffic"]
        if value not in VALID_BODY_LOCAL_TRAFFIC:
            return (
                False,
                f"Invalid value for 'local-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_TRAFFIC)}",
            )
    if "multicast-traffic" in payload:
        value = payload["multicast-traffic"]
        if value not in VALID_BODY_MULTICAST_TRAFFIC:
            return (
                False,
                f"Invalid value for 'multicast-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_TRAFFIC)}",
            )
    if "sniffer-traffic" in payload:
        value = payload["sniffer-traffic"]
        if value not in VALID_BODY_SNIFFER_TRAFFIC:
            return (
                False,
                f"Invalid value for 'sniffer-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_SNIFFER_TRAFFIC)}",
            )
    if "ztna-traffic" in payload:
        value = payload["ztna-traffic"]
        if value not in VALID_BODY_ZTNA_TRAFFIC:
            return (
                False,
                f"Invalid value for 'ztna-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_TRAFFIC)}",
            )
    if "http-transaction" in payload:
        value = payload["http-transaction"]
        if value not in VALID_BODY_HTTP_TRANSACTION:
            return (
                False,
                f"Invalid value for 'http-transaction'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_TRANSACTION)}",
            )
    if "anomaly" in payload:
        value = payload["anomaly"]
        if value not in VALID_BODY_ANOMALY:
            return (
                False,
                f"Invalid value for 'anomaly'='{value}'. Must be one of: {', '.join(VALID_BODY_ANOMALY)}",
            )
    if "voip" in payload:
        value = payload["voip"]
        if value not in VALID_BODY_VOIP:
            return (
                False,
                f"Invalid value for 'voip'='{value}'. Must be one of: {', '.join(VALID_BODY_VOIP)}",
            )
    if "gtp" in payload:
        value = payload["gtp"]
        if value not in VALID_BODY_GTP:
            return (
                False,
                f"Invalid value for 'gtp'='{value}'. Must be one of: {', '.join(VALID_BODY_GTP)}",
            )
    if "forti-switch" in payload:
        value = payload["forti-switch"]
        if value not in VALID_BODY_FORTI_SWITCH:
            return (
                False,
                f"Invalid value for 'forti-switch'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTI_SWITCH)}",
            )
    if "debug" in payload:
        value = payload["debug"]
        if value not in VALID_BODY_DEBUG:
            return (
                False,
                f"Invalid value for 'debug'='{value}'. Must be one of: {', '.join(VALID_BODY_DEBUG)}",
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
    "endpoint": "log/syslogd_override_filter",
    "category": "cmdb",
    "api_path": "log.syslogd/override-filter",
    "help": "Override filters for remote system server.",
    "total_fields": 13,
    "required_fields_count": 0,
    "fields_with_defaults_count": 12,
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
