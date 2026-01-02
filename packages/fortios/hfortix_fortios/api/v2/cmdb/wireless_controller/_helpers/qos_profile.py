"""
Validation helpers for wireless-controller qos_profile endpoint.

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
    "name",  # WiFi QoS profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "bandwidth-admission-control": "disable",
    "bandwidth-capacity": 2000,
    "burst": "disable",
    "call-admission-control": "disable",
    "call-capacity": 10,
    "dscp-wmm-mapping": "disable",
    "wmm": "enable",
    "wmm-bk-dscp": 8,
    "wmm-dscp-marking": "disable",
    "wmm-uapsd": "enable",
    "wmm-vi-dscp": 32,
    "wmm-vo-dscp": 48,
}


# Valid enum values from API documentation
VALID_BODY_BURST = ["enable", "disable"]
VALID_BODY_WMM = ["enable", "disable"]
VALID_BODY_WMM_UAPSD = ["enable", "disable"]
VALID_BODY_CALL_ADMISSION_CONTROL = ["enable", "disable"]
VALID_BODY_BANDWIDTH_ADMISSION_CONTROL = ["enable", "disable"]
VALID_BODY_DSCP_WMM_MAPPING = ["enable", "disable"]
VALID_BODY_WMM_DSCP_MARKING = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_qos_profile_get(
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
    Validate required fields for wireless-controller_qos-profile.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "name": "value",
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


def validate_qos_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: WiFi QoS profile name.

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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "comment cannot exceed 63 characters")

    # Validate uplink if present
    if "uplink" in payload:
        value = payload.get("uplink")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097152:
                    return (False, "uplink must be between 0 and 2097152")
            except (ValueError, TypeError):
                return (False, f"uplink must be numeric, got: {value}")

    # Validate downlink if present
    if "downlink" in payload:
        value = payload.get("downlink")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097152:
                    return (False, "downlink must be between 0 and 2097152")
            except (ValueError, TypeError):
                return (False, f"downlink must be numeric, got: {value}")

    # Validate uplink-sta if present
    if "uplink-sta" in payload:
        value = payload.get("uplink-sta")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097152:
                    return (False, "uplink-sta must be between 0 and 2097152")
            except (ValueError, TypeError):
                return (False, f"uplink-sta must be numeric, got: {value}")

    # Validate downlink-sta if present
    if "downlink-sta" in payload:
        value = payload.get("downlink-sta")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097152:
                    return (
                        False,
                        "downlink-sta must be between 0 and 2097152",
                    )
            except (ValueError, TypeError):
                return (False, f"downlink-sta must be numeric, got: {value}")

    # Validate burst if present
    if "burst" in payload:
        value = payload.get("burst")
        if value and value not in VALID_BODY_BURST:
            return (
                False,
                f"Invalid burst '{value}'. Must be one of: {', '.join(VALID_BODY_BURST)}",
            )

    # Validate wmm if present
    if "wmm" in payload:
        value = payload.get("wmm")
        if value and value not in VALID_BODY_WMM:
            return (
                False,
                f"Invalid wmm '{value}'. Must be one of: {', '.join(VALID_BODY_WMM)}",
            )

    # Validate wmm-uapsd if present
    if "wmm-uapsd" in payload:
        value = payload.get("wmm-uapsd")
        if value and value not in VALID_BODY_WMM_UAPSD:
            return (
                False,
                f"Invalid wmm-uapsd '{value}'. Must be one of: {', '.join(VALID_BODY_WMM_UAPSD)}",
            )

    # Validate call-admission-control if present
    if "call-admission-control" in payload:
        value = payload.get("call-admission-control")
        if value and value not in VALID_BODY_CALL_ADMISSION_CONTROL:
            return (
                False,
                f"Invalid call-admission-control '{value}'. Must be one of: {', '.join(VALID_BODY_CALL_ADMISSION_CONTROL)}",
            )

    # Validate call-capacity if present
    if "call-capacity" in payload:
        value = payload.get("call-capacity")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 60:
                    return (False, "call-capacity must be between 0 and 60")
            except (ValueError, TypeError):
                return (False, f"call-capacity must be numeric, got: {value}")

    # Validate bandwidth-admission-control if present
    if "bandwidth-admission-control" in payload:
        value = payload.get("bandwidth-admission-control")
        if value and value not in VALID_BODY_BANDWIDTH_ADMISSION_CONTROL:
            return (
                False,
                f"Invalid bandwidth-admission-control '{value}'. Must be one of: {', '.join(VALID_BODY_BANDWIDTH_ADMISSION_CONTROL)}",
            )

    # Validate bandwidth-capacity if present
    if "bandwidth-capacity" in payload:
        value = payload.get("bandwidth-capacity")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 600000:
                    return (
                        False,
                        "bandwidth-capacity must be between 1 and 600000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bandwidth-capacity must be numeric, got: {value}",
                )

    # Validate dscp-wmm-mapping if present
    if "dscp-wmm-mapping" in payload:
        value = payload.get("dscp-wmm-mapping")
        if value and value not in VALID_BODY_DSCP_WMM_MAPPING:
            return (
                False,
                f"Invalid dscp-wmm-mapping '{value}'. Must be one of: {', '.join(VALID_BODY_DSCP_WMM_MAPPING)}",
            )

    # Validate wmm-dscp-marking if present
    if "wmm-dscp-marking" in payload:
        value = payload.get("wmm-dscp-marking")
        if value and value not in VALID_BODY_WMM_DSCP_MARKING:
            return (
                False,
                f"Invalid wmm-dscp-marking '{value}'. Must be one of: {', '.join(VALID_BODY_WMM_DSCP_MARKING)}",
            )

    # Validate wmm-vo-dscp if present
    if "wmm-vo-dscp" in payload:
        value = payload.get("wmm-vo-dscp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 63:
                    return (False, "wmm-vo-dscp must be between 0 and 63")
            except (ValueError, TypeError):
                return (False, f"wmm-vo-dscp must be numeric, got: {value}")

    # Validate wmm-vi-dscp if present
    if "wmm-vi-dscp" in payload:
        value = payload.get("wmm-vi-dscp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 63:
                    return (False, "wmm-vi-dscp must be between 0 and 63")
            except (ValueError, TypeError):
                return (False, f"wmm-vi-dscp must be numeric, got: {value}")

    # Validate wmm-be-dscp if present
    if "wmm-be-dscp" in payload:
        value = payload.get("wmm-be-dscp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 63:
                    return (False, "wmm-be-dscp must be between 0 and 63")
            except (ValueError, TypeError):
                return (False, f"wmm-be-dscp must be numeric, got: {value}")

    # Validate wmm-bk-dscp if present
    if "wmm-bk-dscp" in payload:
        value = payload.get("wmm-bk-dscp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 63:
                    return (False, "wmm-bk-dscp must be between 0 and 63")
            except (ValueError, TypeError):
                return (False, f"wmm-bk-dscp must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_qos_profile_put(
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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "comment cannot exceed 63 characters")

    # Validate uplink if present
    if "uplink" in payload:
        value = payload.get("uplink")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097152:
                    return (False, "uplink must be between 0 and 2097152")
            except (ValueError, TypeError):
                return (False, f"uplink must be numeric, got: {value}")

    # Validate downlink if present
    if "downlink" in payload:
        value = payload.get("downlink")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097152:
                    return (False, "downlink must be between 0 and 2097152")
            except (ValueError, TypeError):
                return (False, f"downlink must be numeric, got: {value}")

    # Validate uplink-sta if present
    if "uplink-sta" in payload:
        value = payload.get("uplink-sta")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097152:
                    return (False, "uplink-sta must be between 0 and 2097152")
            except (ValueError, TypeError):
                return (False, f"uplink-sta must be numeric, got: {value}")

    # Validate downlink-sta if present
    if "downlink-sta" in payload:
        value = payload.get("downlink-sta")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097152:
                    return (
                        False,
                        "downlink-sta must be between 0 and 2097152",
                    )
            except (ValueError, TypeError):
                return (False, f"downlink-sta must be numeric, got: {value}")

    # Validate burst if present
    if "burst" in payload:
        value = payload.get("burst")
        if value and value not in VALID_BODY_BURST:
            return (
                False,
                f"Invalid burst '{value}'. Must be one of: {', '.join(VALID_BODY_BURST)}",
            )

    # Validate wmm if present
    if "wmm" in payload:
        value = payload.get("wmm")
        if value and value not in VALID_BODY_WMM:
            return (
                False,
                f"Invalid wmm '{value}'. Must be one of: {', '.join(VALID_BODY_WMM)}",
            )

    # Validate wmm-uapsd if present
    if "wmm-uapsd" in payload:
        value = payload.get("wmm-uapsd")
        if value and value not in VALID_BODY_WMM_UAPSD:
            return (
                False,
                f"Invalid wmm-uapsd '{value}'. Must be one of: {', '.join(VALID_BODY_WMM_UAPSD)}",
            )

    # Validate call-admission-control if present
    if "call-admission-control" in payload:
        value = payload.get("call-admission-control")
        if value and value not in VALID_BODY_CALL_ADMISSION_CONTROL:
            return (
                False,
                f"Invalid call-admission-control '{value}'. Must be one of: {', '.join(VALID_BODY_CALL_ADMISSION_CONTROL)}",
            )

    # Validate call-capacity if present
    if "call-capacity" in payload:
        value = payload.get("call-capacity")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 60:
                    return (False, "call-capacity must be between 0 and 60")
            except (ValueError, TypeError):
                return (False, f"call-capacity must be numeric, got: {value}")

    # Validate bandwidth-admission-control if present
    if "bandwidth-admission-control" in payload:
        value = payload.get("bandwidth-admission-control")
        if value and value not in VALID_BODY_BANDWIDTH_ADMISSION_CONTROL:
            return (
                False,
                f"Invalid bandwidth-admission-control '{value}'. Must be one of: {', '.join(VALID_BODY_BANDWIDTH_ADMISSION_CONTROL)}",
            )

    # Validate bandwidth-capacity if present
    if "bandwidth-capacity" in payload:
        value = payload.get("bandwidth-capacity")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 600000:
                    return (
                        False,
                        "bandwidth-capacity must be between 1 and 600000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bandwidth-capacity must be numeric, got: {value}",
                )

    # Validate dscp-wmm-mapping if present
    if "dscp-wmm-mapping" in payload:
        value = payload.get("dscp-wmm-mapping")
        if value and value not in VALID_BODY_DSCP_WMM_MAPPING:
            return (
                False,
                f"Invalid dscp-wmm-mapping '{value}'. Must be one of: {', '.join(VALID_BODY_DSCP_WMM_MAPPING)}",
            )

    # Validate wmm-dscp-marking if present
    if "wmm-dscp-marking" in payload:
        value = payload.get("wmm-dscp-marking")
        if value and value not in VALID_BODY_WMM_DSCP_MARKING:
            return (
                False,
                f"Invalid wmm-dscp-marking '{value}'. Must be one of: {', '.join(VALID_BODY_WMM_DSCP_MARKING)}",
            )

    # Validate wmm-vo-dscp if present
    if "wmm-vo-dscp" in payload:
        value = payload.get("wmm-vo-dscp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 63:
                    return (False, "wmm-vo-dscp must be between 0 and 63")
            except (ValueError, TypeError):
                return (False, f"wmm-vo-dscp must be numeric, got: {value}")

    # Validate wmm-vi-dscp if present
    if "wmm-vi-dscp" in payload:
        value = payload.get("wmm-vi-dscp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 63:
                    return (False, "wmm-vi-dscp must be between 0 and 63")
            except (ValueError, TypeError):
                return (False, f"wmm-vi-dscp must be numeric, got: {value}")

    # Validate wmm-be-dscp if present
    if "wmm-be-dscp" in payload:
        value = payload.get("wmm-be-dscp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 63:
                    return (False, "wmm-be-dscp must be between 0 and 63")
            except (ValueError, TypeError):
                return (False, f"wmm-be-dscp must be numeric, got: {value}")

    # Validate wmm-bk-dscp if present
    if "wmm-bk-dscp" in payload:
        value = payload.get("wmm-bk-dscp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 63:
                    return (False, "wmm-bk-dscp must be between 0 and 63")
            except (ValueError, TypeError):
                return (False, f"wmm-bk-dscp must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_qos_profile_delete(
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
