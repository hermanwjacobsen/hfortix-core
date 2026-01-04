"""
Validation helpers for system/automation_trigger endpoint.

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
    "stitch-name",  # Triggering stitch name.
    "faz-event-name",  # FortiAnalyzer event handler name.
    "serial",  # Fabric connector serial number.
    "fabric-event-name",  # Fabric connector event handler name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "trigger-type": "event-based",
    "event-type": "ioc",
    "license-type": "forticare-support",
    "report-type": "posture",
    "stitch-name": "",
    "trigger-frequency": "daily",
    "trigger-weekday": "",
    "trigger-day": 1,
    "trigger-hour": 0,
    "trigger-minute": 0,
    "trigger-datetime": "0000-00-00 00:00:00",
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
    "name": "string",  # Name.
    "description": "var-string",  # Description.
    "trigger-type": "option",  # Trigger type.
    "event-type": "option",  # Event type.
    "vdom": "string",  # Virtual domain(s) that this trigger is valid for.
    "license-type": "option",  # License type.
    "report-type": "option",  # Security Rating report.
    "stitch-name": "string",  # Triggering stitch name.
    "logid": "string",  # Log IDs to trigger event.
    "trigger-frequency": "option",  # Scheduled trigger frequency (default = daily).
    "trigger-weekday": "option",  # Day of week for trigger.
    "trigger-day": "integer",  # Day within a month to trigger.
    "trigger-hour": "integer",  # Hour of the day on which to trigger (0 - 23, default = 1).
    "trigger-minute": "integer",  # Minute of the hour on which to trigger (0 - 59, default = 0)
    "trigger-datetime": "datetime",  # Trigger date and time (YYYY-MM-DD HH:MM:SS).
    "fields": "string",  # Customized trigger field settings.
    "faz-event-name": "var-string",  # FortiAnalyzer event handler name.
    "faz-event-severity": "var-string",  # FortiAnalyzer event severity.
    "faz-event-tags": "var-string",  # FortiAnalyzer event tags.
    "serial": "var-string",  # Fabric connector serial number.
    "fabric-event-name": "var-string",  # Fabric connector event handler name.
    "fabric-event-severity": "var-string",  # Fabric connector event severity.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Name.",
    "description": "Description.",
    "trigger-type": "Trigger type.",
    "event-type": "Event type.",
    "vdom": "Virtual domain(s) that this trigger is valid for.",
    "license-type": "License type.",
    "report-type": "Security Rating report.",
    "stitch-name": "Triggering stitch name.",
    "logid": "Log IDs to trigger event.",
    "trigger-frequency": "Scheduled trigger frequency (default = daily).",
    "trigger-weekday": "Day of week for trigger.",
    "trigger-day": "Day within a month to trigger.",
    "trigger-hour": "Hour of the day on which to trigger (0 - 23, default = 1).",
    "trigger-minute": "Minute of the hour on which to trigger (0 - 59, default = 0).",
    "trigger-datetime": "Trigger date and time (YYYY-MM-DD HH:MM:SS).",
    "fields": "Customized trigger field settings.",
    "faz-event-name": "FortiAnalyzer event handler name.",
    "faz-event-severity": "FortiAnalyzer event severity.",
    "faz-event-tags": "FortiAnalyzer event tags.",
    "serial": "Fabric connector serial number.",
    "fabric-event-name": "Fabric connector event handler name.",
    "fabric-event-severity": "Fabric connector event severity.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "stitch-name": {"type": "string", "max_length": 35},
    "trigger-day": {"type": "integer", "min": 1, "max": 31},
    "trigger-hour": {"type": "integer", "min": 0, "max": 23},
    "trigger-minute": {"type": "integer", "min": 0, "max": 59},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "vdom": {
        "name": {
            "type": "string",
            "help": "Virtual domain name.",
            "default": "",
            "max_length": 79,
        },
    },
    "logid": {
        "id": {
            "type": "integer",
            "help": "Log ID.",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 65535,
        },
    },
    "fields": {
        "id": {
            "type": "integer",
            "help": "Entry ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "name": {
            "type": "string",
            "help": "Name.",
            "default": "",
            "max_length": 35,
        },
        "value": {
            "type": "var-string",
            "help": "Value.",
            "max_length": 63,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_TRIGGER_TYPE = [
    "event-based",
    "scheduled",
]
VALID_BODY_EVENT_TYPE = [
    "ioc",
    "event-log",
    "reboot",
    "low-memory",
    "high-cpu",
    "license-near-expiry",
    "local-cert-near-expiry",
    "ha-failover",
    "config-change",
    "security-rating-summary",
    "virus-ips-db-updated",
    "faz-event",
    "incoming-webhook",
    "fabric-event",
    "ips-logs",
    "anomaly-logs",
    "virus-logs",
    "ssh-logs",
    "webfilter-violation",
    "traffic-violation",
    "stitch",
]
VALID_BODY_LICENSE_TYPE = [
    "forticare-support",
    "fortiguard-webfilter",
    "fortiguard-antispam",
    "fortiguard-antivirus",
    "fortiguard-ips",
    "fortiguard-management",
    "forticloud",
    "any",
]
VALID_BODY_REPORT_TYPE = [
    "posture",
    "coverage",
    "optimization",
    "any",
]
VALID_BODY_TRIGGER_FREQUENCY = [
    "hourly",
    "daily",
    "weekly",
    "monthly",
    "once",
]
VALID_BODY_TRIGGER_WEEKDAY = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_automation_trigger_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/automation_trigger.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_automation_trigger_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_system_automation_trigger_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_automation_trigger_get(
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
    Validate required fields for system/automation_trigger.

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


def validate_system_automation_trigger_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/automation_trigger object.

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
        ...     "stitch-name": True,  # Triggering stitch name.
        ...     "faz-event-name": True,  # FortiAnalyzer event handler name.
        ... }
        >>> is_valid, error = validate_system_automation_trigger_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "stitch-name": True,
        ...     "trigger-type": "event-based",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_automation_trigger_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["trigger-type"] = "invalid-value"
        >>> is_valid, error = validate_system_automation_trigger_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_automation_trigger_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "trigger-type" in payload:
        value = payload["trigger-type"]
        if value not in VALID_BODY_TRIGGER_TYPE:
            desc = FIELD_DESCRIPTIONS.get("trigger-type", "")
            error_msg = f"Invalid value for 'trigger-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRIGGER_TYPE)}"
            error_msg += f"\n  → Example: trigger-type='{{ VALID_BODY_TRIGGER_TYPE[0] }}'"
            return (False, error_msg)
    if "event-type" in payload:
        value = payload["event-type"]
        if value not in VALID_BODY_EVENT_TYPE:
            desc = FIELD_DESCRIPTIONS.get("event-type", "")
            error_msg = f"Invalid value for 'event-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EVENT_TYPE)}"
            error_msg += f"\n  → Example: event-type='{{ VALID_BODY_EVENT_TYPE[0] }}'"
            return (False, error_msg)
    if "license-type" in payload:
        value = payload["license-type"]
        if value not in VALID_BODY_LICENSE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("license-type", "")
            error_msg = f"Invalid value for 'license-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LICENSE_TYPE)}"
            error_msg += f"\n  → Example: license-type='{{ VALID_BODY_LICENSE_TYPE[0] }}'"
            return (False, error_msg)
    if "report-type" in payload:
        value = payload["report-type"]
        if value not in VALID_BODY_REPORT_TYPE:
            desc = FIELD_DESCRIPTIONS.get("report-type", "")
            error_msg = f"Invalid value for 'report-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REPORT_TYPE)}"
            error_msg += f"\n  → Example: report-type='{{ VALID_BODY_REPORT_TYPE[0] }}'"
            return (False, error_msg)
    if "trigger-frequency" in payload:
        value = payload["trigger-frequency"]
        if value not in VALID_BODY_TRIGGER_FREQUENCY:
            desc = FIELD_DESCRIPTIONS.get("trigger-frequency", "")
            error_msg = f"Invalid value for 'trigger-frequency': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRIGGER_FREQUENCY)}"
            error_msg += f"\n  → Example: trigger-frequency='{{ VALID_BODY_TRIGGER_FREQUENCY[0] }}'"
            return (False, error_msg)
    if "trigger-weekday" in payload:
        value = payload["trigger-weekday"]
        if value not in VALID_BODY_TRIGGER_WEEKDAY:
            desc = FIELD_DESCRIPTIONS.get("trigger-weekday", "")
            error_msg = f"Invalid value for 'trigger-weekday': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRIGGER_WEEKDAY)}"
            error_msg += f"\n  → Example: trigger-weekday='{{ VALID_BODY_TRIGGER_WEEKDAY[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_automation_trigger_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/automation_trigger.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_automation_trigger_put(payload)
    """
    # Step 1: Validate enum values
    if "trigger-type" in payload:
        value = payload["trigger-type"]
        if value not in VALID_BODY_TRIGGER_TYPE:
            return (
                False,
                f"Invalid value for 'trigger-type'='{value}'. Must be one of: {', '.join(VALID_BODY_TRIGGER_TYPE)}",
            )
    if "event-type" in payload:
        value = payload["event-type"]
        if value not in VALID_BODY_EVENT_TYPE:
            return (
                False,
                f"Invalid value for 'event-type'='{value}'. Must be one of: {', '.join(VALID_BODY_EVENT_TYPE)}",
            )
    if "license-type" in payload:
        value = payload["license-type"]
        if value not in VALID_BODY_LICENSE_TYPE:
            return (
                False,
                f"Invalid value for 'license-type'='{value}'. Must be one of: {', '.join(VALID_BODY_LICENSE_TYPE)}",
            )
    if "report-type" in payload:
        value = payload["report-type"]
        if value not in VALID_BODY_REPORT_TYPE:
            return (
                False,
                f"Invalid value for 'report-type'='{value}'. Must be one of: {', '.join(VALID_BODY_REPORT_TYPE)}",
            )
    if "trigger-frequency" in payload:
        value = payload["trigger-frequency"]
        if value not in VALID_BODY_TRIGGER_FREQUENCY:
            return (
                False,
                f"Invalid value for 'trigger-frequency'='{value}'. Must be one of: {', '.join(VALID_BODY_TRIGGER_FREQUENCY)}",
            )
    if "trigger-weekday" in payload:
        value = payload["trigger-weekday"]
        if value not in VALID_BODY_TRIGGER_WEEKDAY:
            return (
                False,
                f"Invalid value for 'trigger-weekday'='{value}'. Must be one of: {', '.join(VALID_BODY_TRIGGER_WEEKDAY)}",
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
    "endpoint": "system/automation_trigger",
    "category": "cmdb",
    "api_path": "system/automation-trigger",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Trigger for automation stitches.",
    "total_fields": 22,
    "required_fields_count": 4,
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
