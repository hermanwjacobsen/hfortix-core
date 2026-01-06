"""Validation helpers for system/automation_trigger - Auto-generated"""

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
    "event-based",  # Event based trigger.
    "scheduled",  # Scheduled trigger.
]
VALID_BODY_EVENT_TYPE = [
    "ioc",  # Indicator of compromise detected.
    "event-log",  # Use log ID as trigger.
    "reboot",  # Device reboot.
    "low-memory",  # Conserve mode due to low memory.
    "high-cpu",  # High CPU usage.
    "license-near-expiry",  # License near expiration date.
    "local-cert-near-expiry",  # The local certificate near expiration date.
    "ha-failover",  # HA failover.
    "config-change",  # Configuration change.
    "security-rating-summary",  # Security rating summary.
    "virus-ips-db-updated",  # Virus and IPS database updated.
    "faz-event",  # FortiAnalyzer event.
    "incoming-webhook",  # Incoming webhook call.
    "fabric-event",  # Fabric connector event.
    "ips-logs",  # IPS logs.
    "anomaly-logs",  # Anomaly logs.
    "virus-logs",  # Virus logs.
    "ssh-logs",  # SSH logs.
    "webfilter-violation",  # Webfilter violation.
    "traffic-violation",  # Traffic violation.
    "stitch",  # Specified stitch has been triggered.
]
VALID_BODY_LICENSE_TYPE = [
    "forticare-support",  # FortiCare support license.
    "fortiguard-webfilter",  # FortiGuard web filter license.
    "fortiguard-antispam",  # FortiGuard antispam license.
    "fortiguard-antivirus",  # FortiGuard AntiVirus license.
    "fortiguard-ips",  # FortiGuard IPS license.
    "fortiguard-management",  # FortiGuard management service license.
    "forticloud",  # FortiCloud license.
    "any",  # Any license.
]
VALID_BODY_REPORT_TYPE = [
    "posture",  # Posture report.
    "coverage",  # Coverage report.
    "optimization",  # Optimization report
    "any",  # Any report.
]
VALID_BODY_TRIGGER_FREQUENCY = [
    "hourly",  # Run hourly.
    "daily",  # Run daily.
    "weekly",  # Run weekly.
    "monthly",  # Run monthly.
    "once",  # Run once at specified date time.
]
VALID_BODY_TRIGGER_WEEKDAY = [
    "sunday",  # Sunday.
    "monday",  # Monday.
    "tuesday",  # Tuesday.
    "wednesday",  # Wednesday.
    "thursday",  # Thursday.
    "friday",  # Friday.
    "saturday",  # Saturday.
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
    """Validate GET request parameters for system/automation_trigger."""
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
    """Validate required fields for system/automation_trigger."""
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
    """Validate POST request to create new system/automation_trigger object."""
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
    """Validate PUT request to update system/automation_trigger."""
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
# Imported from central module to avoid duplication across 1,062 files
# ============================================================================

from hfortix_fortios._helpers.metadata import (
    get_field_description as _get_field_description,
    get_field_type as _get_field_type,
    get_field_constraints as _get_field_constraints,
    get_field_default as _get_field_default,
    get_field_options as _get_field_options,
    get_nested_schema as _get_nested_schema,
    get_all_fields as _get_all_fields,
    get_field_metadata as _get_field_metadata,
    validate_field_value as _validate_field_value,
)

# Wrapper functions that bind module-specific data to central functions
def get_field_description(field_name: str) -> str | None:
    """Get description/help text for a field."""
    return _get_field_description(FIELD_DESCRIPTIONS, field_name)

def get_field_type(field_name: str) -> str | None:
    """Get the type of a field."""
    return _get_field_type(FIELD_TYPES, field_name)

def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """Get constraints for a field (min/max values, string length)."""
    return _get_field_constraints(FIELD_CONSTRAINTS, field_name)

def get_field_default(field_name: str) -> Any | None:
    """Get default value for a field."""
    return _get_field_default(FIELDS_WITH_DEFAULTS, field_name)

def get_field_options(field_name: str) -> list[str] | None:
    """Get valid enum options for a field."""
    return _get_field_options(globals(), field_name)

def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """Get schema for nested table/list fields."""
    return _get_nested_schema(NESTED_SCHEMAS, field_name)

def get_all_fields() -> list[str]:
    """Get list of all field names."""
    return _get_all_fields(FIELD_TYPES)

def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """Get complete metadata for a field (type, description, constraints, defaults, options)."""
    return _get_field_metadata(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS, REQUIRED_FIELDS, NESTED_SCHEMAS,
        globals(), field_name
    )

def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """Validate a single field value against its constraints."""
    return _validate_field_value(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        globals(), field_name, value
    )


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
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
