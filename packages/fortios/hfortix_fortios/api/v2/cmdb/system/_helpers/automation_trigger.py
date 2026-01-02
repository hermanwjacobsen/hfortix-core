"""
Validation helpers for system automation_trigger endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# ============================================================================
# Required Fields Validation
# Auto-generated from schema using required_fields_analyzer.py
# ============================================================================

# NOTE: The FortiOS schema has known bugs where some specialized optional
# features are incorrectly marked as required. See SCHEMA_FALSE_POSITIVES
# for fields that should be OPTIONAL despite being marked required in
# the schema. The REQUIRED_FIELDS list below reflects the ACTUAL
# requirements based on API testing and schema analysis.

# Always required fields (no alternatives)
REQUIRED_FIELDS = [
    "fabric-event-name",  # Fabric connector event handler name.
    "faz-event-name",  # FortiAnalyzer event handler name.
    "name",  # Name.
    "serial",  # Fabric connector serial number.
    "stitch-name",  # Triggering stitch name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "event-type": "ioc",
    "license-type": "forticare-support",
    "report-type": "posture",
    "trigger-datetime": "0000-00-00 00:00:00",
    "trigger-day": 1,
    "trigger-frequency": "daily",
    "trigger-type": "event-based",
    "trigger-weekday": "sunday",
}


# Valid enum values from API documentation
VALID_BODY_TRIGGER_TYPE = ["event-based", "scheduled"]
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
VALID_BODY_REPORT_TYPE = ["posture", "coverage", "optimization", "any"]
VALID_BODY_TRIGGER_FREQUENCY = ["hourly", "daily", "weekly", "monthly", "once"]
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


def validate_automation_trigger_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> # List all objects
        >>> is_valid, error = {func_name}()
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
    Validate required fields for system_automation-trigger.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "fabric-event-name": "value",
        ...     # ... other fields
        ... })
    """
    # Check always-required fields
    missing = []
    for field in REQUIRED_FIELDS:
        # Skip fields with defaults
        if field in FIELDS_WITH_DEFAULTS:
            continue
        if field not in payload or payload.get(field) is None:
            missing.append(field)

    if missing:
        return (False, f"Missing required fields: {', '.join(missing)}")

    return (True, None)


# ============================================================================
# Endpoint Validation (Enhanced with Required Fields)
# ============================================================================


def validate_automation_trigger_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - fabric-event-name: Fabric connector event handler name.
      - faz-event-name: FortiAnalyzer event handler name.
      - name: Name.
      - serial: Fabric connector serial number.
      - stitch-name: Triggering stitch name.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate payload exists
    if not payload:
        payload = {}

    # Validate payload exists
    if not payload:
        payload = {}

    # Validate payload exists
    if not payload:
        payload = {}

    # Validate payload exists
    if not payload:
        payload = {}

    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate field values (enums, ranges, etc.)
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate trigger-type if present
    if "trigger-type" in payload:
        value = payload.get("trigger-type")
        if value and value not in VALID_BODY_TRIGGER_TYPE:
            return (
                False,
                f"Invalid trigger-type '{value}'. Must be one of: {', '.join(VALID_BODY_TRIGGER_TYPE)}",
            )

    # Validate event-type if present
    if "event-type" in payload:
        value = payload.get("event-type")
        if value and value not in VALID_BODY_EVENT_TYPE:
            return (
                False,
                f"Invalid event-type '{value}'. Must be one of: {', '.join(VALID_BODY_EVENT_TYPE)}",
            )

    # Validate license-type if present
    if "license-type" in payload:
        value = payload.get("license-type")
        if value and value not in VALID_BODY_LICENSE_TYPE:
            return (
                False,
                f"Invalid license-type '{value}'. Must be one of: {', '.join(VALID_BODY_LICENSE_TYPE)}",
            )

    # Validate report-type if present
    if "report-type" in payload:
        value = payload.get("report-type")
        if value and value not in VALID_BODY_REPORT_TYPE:
            return (
                False,
                f"Invalid report-type '{value}'. Must be one of: {', '.join(VALID_BODY_REPORT_TYPE)}",
            )

    # Validate stitch-name if present
    if "stitch-name" in payload:
        value = payload.get("stitch-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "stitch-name cannot exceed 35 characters")

    # Validate trigger-frequency if present
    if "trigger-frequency" in payload:
        value = payload.get("trigger-frequency")
        if value and value not in VALID_BODY_TRIGGER_FREQUENCY:
            return (
                False,
                f"Invalid trigger-frequency '{value}'. Must be one of: {', '.join(VALID_BODY_TRIGGER_FREQUENCY)}",
            )

    # Validate trigger-weekday if present
    if "trigger-weekday" in payload:
        value = payload.get("trigger-weekday")
        if value and value not in VALID_BODY_TRIGGER_WEEKDAY:
            return (
                False,
                f"Invalid trigger-weekday '{value}'. Must be one of: {', '.join(VALID_BODY_TRIGGER_WEEKDAY)}",
            )

    # Validate trigger-day if present
    if "trigger-day" in payload:
        value = payload.get("trigger-day")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 31:
                    return (False, "trigger-day must be between 1 and 31")
            except (ValueError, TypeError):
                return (False, f"trigger-day must be numeric, got: {value}")

    # Validate trigger-hour if present
    if "trigger-hour" in payload:
        value = payload.get("trigger-hour")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 23:
                    return (False, "trigger-hour must be between 0 and 23")
            except (ValueError, TypeError):
                return (False, f"trigger-hour must be numeric, got: {value}")

    # Validate trigger-minute if present
    if "trigger-minute" in payload:
        value = payload.get("trigger-minute")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 59:
                    return (False, "trigger-minute must be between 0 and 59")
            except (ValueError, TypeError):
                return (False, f"trigger-minute must be numeric, got: {value}")

    # Validate faz-event-name if present
    if "faz-event-name" in payload:
        value = payload.get("faz-event-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "faz-event-name cannot exceed 255 characters")

    # Validate faz-event-severity if present
    if "faz-event-severity" in payload:
        value = payload.get("faz-event-severity")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "faz-event-severity cannot exceed 255 characters")

    # Validate faz-event-tags if present
    if "faz-event-tags" in payload:
        value = payload.get("faz-event-tags")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "faz-event-tags cannot exceed 255 characters")

    # Validate serial if present
    if "serial" in payload:
        value = payload.get("serial")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "serial cannot exceed 255 characters")

    # Validate fabric-event-name if present
    if "fabric-event-name" in payload:
        value = payload.get("fabric-event-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "fabric-event-name cannot exceed 255 characters")

    # Validate fabric-event-severity if present
    if "fabric-event-severity" in payload:
        value = payload.get("fabric-event-severity")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "fabric-event-severity cannot exceed 255 characters",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_automation_trigger_put(
    name: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        name: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # name is required for updates
    if not name:
        return (False, "name is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate trigger-type if present
    if "trigger-type" in payload:
        value = payload.get("trigger-type")
        if value and value not in VALID_BODY_TRIGGER_TYPE:
            return (
                False,
                f"Invalid trigger-type '{value}'. Must be one of: {', '.join(VALID_BODY_TRIGGER_TYPE)}",
            )

    # Validate event-type if present
    if "event-type" in payload:
        value = payload.get("event-type")
        if value and value not in VALID_BODY_EVENT_TYPE:
            return (
                False,
                f"Invalid event-type '{value}'. Must be one of: {', '.join(VALID_BODY_EVENT_TYPE)}",
            )

    # Validate license-type if present
    if "license-type" in payload:
        value = payload.get("license-type")
        if value and value not in VALID_BODY_LICENSE_TYPE:
            return (
                False,
                f"Invalid license-type '{value}'. Must be one of: {', '.join(VALID_BODY_LICENSE_TYPE)}",
            )

    # Validate report-type if present
    if "report-type" in payload:
        value = payload.get("report-type")
        if value and value not in VALID_BODY_REPORT_TYPE:
            return (
                False,
                f"Invalid report-type '{value}'. Must be one of: {', '.join(VALID_BODY_REPORT_TYPE)}",
            )

    # Validate stitch-name if present
    if "stitch-name" in payload:
        value = payload.get("stitch-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "stitch-name cannot exceed 35 characters")

    # Validate trigger-frequency if present
    if "trigger-frequency" in payload:
        value = payload.get("trigger-frequency")
        if value and value not in VALID_BODY_TRIGGER_FREQUENCY:
            return (
                False,
                f"Invalid trigger-frequency '{value}'. Must be one of: {', '.join(VALID_BODY_TRIGGER_FREQUENCY)}",
            )

    # Validate trigger-weekday if present
    if "trigger-weekday" in payload:
        value = payload.get("trigger-weekday")
        if value and value not in VALID_BODY_TRIGGER_WEEKDAY:
            return (
                False,
                f"Invalid trigger-weekday '{value}'. Must be one of: {', '.join(VALID_BODY_TRIGGER_WEEKDAY)}",
            )

    # Validate trigger-day if present
    if "trigger-day" in payload:
        value = payload.get("trigger-day")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 31:
                    return (False, "trigger-day must be between 1 and 31")
            except (ValueError, TypeError):
                return (False, f"trigger-day must be numeric, got: {value}")

    # Validate trigger-hour if present
    if "trigger-hour" in payload:
        value = payload.get("trigger-hour")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 23:
                    return (False, "trigger-hour must be between 0 and 23")
            except (ValueError, TypeError):
                return (False, f"trigger-hour must be numeric, got: {value}")

    # Validate trigger-minute if present
    if "trigger-minute" in payload:
        value = payload.get("trigger-minute")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 59:
                    return (False, "trigger-minute must be between 0 and 59")
            except (ValueError, TypeError):
                return (False, f"trigger-minute must be numeric, got: {value}")

    # Validate faz-event-name if present
    if "faz-event-name" in payload:
        value = payload.get("faz-event-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "faz-event-name cannot exceed 255 characters")

    # Validate faz-event-severity if present
    if "faz-event-severity" in payload:
        value = payload.get("faz-event-severity")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "faz-event-severity cannot exceed 255 characters")

    # Validate faz-event-tags if present
    if "faz-event-tags" in payload:
        value = payload.get("faz-event-tags")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "faz-event-tags cannot exceed 255 characters")

    # Validate serial if present
    if "serial" in payload:
        value = payload.get("serial")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "serial cannot exceed 255 characters")

    # Validate fabric-event-name if present
    if "fabric-event-name" in payload:
        value = payload.get("fabric-event-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "fabric-event-name cannot exceed 255 characters")

    # Validate fabric-event-severity if present
    if "fabric-event-severity" in payload:
        value = payload.get("fabric-event-severity")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "fabric-event-severity cannot exceed 255 characters",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_automation_trigger_delete(
    name: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        name: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not name:
        return (False, "name is required for DELETE operation")

    return (True, None)
