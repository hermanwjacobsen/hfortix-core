"""
Validation helpers for system device_upgrade endpoint.

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
    "device-type",  # Fortinet device type.
    "known-ha-members",  # Known members of the HA cluster. If a member is missing at u
    "maximum-minutes",  # Maximum number of minutes to allow for immediate upgrade pre
    "next-path-index",  # The index of the next image to upgrade to.
    "serial",  # Serial number of the node to include.
    "setup-time",  # Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC)
    "status",  # Current status of the upgrade.
    "time",  # Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UT
    "timing",  # Run immediately or at a scheduled time.
    "upgrade-path",  # Fortinet OS image versions to upgrade through in major-minor
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "allow-download": "enable",
    "device-type": "fortigate",
    "failure-reason": "none",
    "maximum-minutes": 15,
    "status": "disabled",
    "timing": "immediate",
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "disabled",
    "initialized",
    "downloading",
    "device-disconnected",
    "ready",
    "coordinating",
    "staging",
    "final-check",
    "upgrade-devices",
    "cancelled",
    "confirmed",
    "done",
    "dry-run-done",
    "failed",
]
VALID_BODY_TIMING = ["immediate", "scheduled"]
VALID_BODY_DEVICE_TYPE = [
    "fortigate",
    "fortiswitch",
    "fortiap",
    "fortiextender",
]
VALID_BODY_ALLOW_DOWNLOAD = ["enable", "disable"]
VALID_BODY_FAILURE_REASON = [
    "none",
    "internal",
    "timeout",
    "device-type-unsupported",
    "download-failed",
    "device-missing",
    "version-unavailable",
    "staging-failed",
    "reboot-failed",
    "device-not-reconnected",
    "node-not-ready",
    "no-final-confirmation",
    "no-confirmation-query",
    "config-error-log-nonempty",
    "csf-tree-not-supported",
    "firmware-changed",
    "node-failed",
    "image-missing",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_device_upgrade_get(
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
    Validate required fields for system_device-upgrade.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "device-type": "value",
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


def validate_device_upgrade_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - device-type: Fortinet device type.
      - known-ha-members: Known members of the HA cluster. If a member is missing at u
      - maximum-minutes: Maximum number of minutes to allow for immediate upgrade pre
      - next-path-index: The index of the next image to upgrade to.
      - serial: Serial number of the node to include.
      - setup-time: Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC)
      - status: Current status of the upgrade.
      - time: Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UT
      - timing: Run immediately or at a scheduled time.
      - upgrade-path: Fortinet OS image versions to upgrade through in major-minor

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
    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate ha-reboot-controller if present
    if "ha-reboot-controller" in payload:
        value = payload.get("ha-reboot-controller")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ha-reboot-controller cannot exceed 79 characters")

    # Validate next-path-index if present
    if "next-path-index" in payload:
        value = payload.get("next-path-index")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 10:
                    return (False, "next-path-index must be between 0 and 10")
            except (ValueError, TypeError):
                return (
                    False,
                    f"next-path-index must be numeric, got: {value}",
                )

    # Validate starter-admin if present
    if "starter-admin" in payload:
        value = payload.get("starter-admin")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "starter-admin cannot exceed 64 characters")

    # Validate serial if present
    if "serial" in payload:
        value = payload.get("serial")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "serial cannot exceed 79 characters")

    # Validate timing if present
    if "timing" in payload:
        value = payload.get("timing")
        if value and value not in VALID_BODY_TIMING:
            return (
                False,
                f"Invalid timing '{value}'. Must be one of: {', '.join(VALID_BODY_TIMING)}",
            )

    # Validate maximum-minutes if present
    if "maximum-minutes" in payload:
        value = payload.get("maximum-minutes")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 10080:
                    return (
                        False,
                        "maximum-minutes must be between 5 and 10080",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"maximum-minutes must be numeric, got: {value}",
                )

    # Validate device-type if present
    if "device-type" in payload:
        value = payload.get("device-type")
        if value and value not in VALID_BODY_DEVICE_TYPE:
            return (
                False,
                f"Invalid device-type '{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_TYPE)}",
            )

    # Validate allow-download if present
    if "allow-download" in payload:
        value = payload.get("allow-download")
        if value and value not in VALID_BODY_ALLOW_DOWNLOAD:
            return (
                False,
                f"Invalid allow-download '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_DOWNLOAD)}",
            )

    # Validate failure-reason if present
    if "failure-reason" in payload:
        value = payload.get("failure-reason")
        if value and value not in VALID_BODY_FAILURE_REASON:
            return (
                False,
                f"Invalid failure-reason '{value}'. Must be one of: {', '.join(VALID_BODY_FAILURE_REASON)}",
            )

    return (True, None)
