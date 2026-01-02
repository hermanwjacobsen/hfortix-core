"""
Validation helpers for wireless-controller hotspot20_h2qp_wan_metric endpoint.

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
    "name",  # WAN metric name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "downlink-speed": 2400,
    "link-at-capacity": "disable",
    "link-status": "up",
    "symmetric-wan-link": "asymmetric",
    "uplink-speed": 2400,
}


# Valid enum values from API documentation
VALID_BODY_LINK_STATUS = ["up", "down", "in-test"]
VALID_BODY_SYMMETRIC_WAN_LINK = ["symmetric", "asymmetric"]
VALID_BODY_LINK_AT_CAPACITY = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_hotspot20_h2qp_wan_metric_get(
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
    Validate required fields for wireless-controller_hotspot20_h2qp-wan-metric.

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


def validate_hotspot20_h2qp_wan_metric_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: WAN metric name.

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

    # Validate link-status if present
    if "link-status" in payload:
        value = payload.get("link-status")
        if value and value not in VALID_BODY_LINK_STATUS:
            return (
                False,
                f"Invalid link-status '{value}'. Must be one of: {', '.join(VALID_BODY_LINK_STATUS)}",
            )

    # Validate symmetric-wan-link if present
    if "symmetric-wan-link" in payload:
        value = payload.get("symmetric-wan-link")
        if value and value not in VALID_BODY_SYMMETRIC_WAN_LINK:
            return (
                False,
                f"Invalid symmetric-wan-link '{value}'. Must be one of: {', '.join(VALID_BODY_SYMMETRIC_WAN_LINK)}",
            )

    # Validate link-at-capacity if present
    if "link-at-capacity" in payload:
        value = payload.get("link-at-capacity")
        if value and value not in VALID_BODY_LINK_AT_CAPACITY:
            return (
                False,
                f"Invalid link-at-capacity '{value}'. Must be one of: {', '.join(VALID_BODY_LINK_AT_CAPACITY)}",
            )

    # Validate uplink-speed if present
    if "uplink-speed" in payload:
        value = payload.get("uplink-speed")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "uplink-speed must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"uplink-speed must be numeric, got: {value}")

    # Validate downlink-speed if present
    if "downlink-speed" in payload:
        value = payload.get("downlink-speed")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "downlink-speed must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"downlink-speed must be numeric, got: {value}")

    # Validate uplink-load if present
    if "uplink-load" in payload:
        value = payload.get("uplink-load")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "uplink-load must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"uplink-load must be numeric, got: {value}")

    # Validate downlink-load if present
    if "downlink-load" in payload:
        value = payload.get("downlink-load")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "downlink-load must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"downlink-load must be numeric, got: {value}")

    # Validate load-measurement-duration if present
    if "load-measurement-duration" in payload:
        value = payload.get("load-measurement-duration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "load-measurement-duration must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"load-measurement-duration must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_hotspot20_h2qp_wan_metric_put(
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

    # Validate link-status if present
    if "link-status" in payload:
        value = payload.get("link-status")
        if value and value not in VALID_BODY_LINK_STATUS:
            return (
                False,
                f"Invalid link-status '{value}'. Must be one of: {', '.join(VALID_BODY_LINK_STATUS)}",
            )

    # Validate symmetric-wan-link if present
    if "symmetric-wan-link" in payload:
        value = payload.get("symmetric-wan-link")
        if value and value not in VALID_BODY_SYMMETRIC_WAN_LINK:
            return (
                False,
                f"Invalid symmetric-wan-link '{value}'. Must be one of: {', '.join(VALID_BODY_SYMMETRIC_WAN_LINK)}",
            )

    # Validate link-at-capacity if present
    if "link-at-capacity" in payload:
        value = payload.get("link-at-capacity")
        if value and value not in VALID_BODY_LINK_AT_CAPACITY:
            return (
                False,
                f"Invalid link-at-capacity '{value}'. Must be one of: {', '.join(VALID_BODY_LINK_AT_CAPACITY)}",
            )

    # Validate uplink-speed if present
    if "uplink-speed" in payload:
        value = payload.get("uplink-speed")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "uplink-speed must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"uplink-speed must be numeric, got: {value}")

    # Validate downlink-speed if present
    if "downlink-speed" in payload:
        value = payload.get("downlink-speed")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "downlink-speed must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"downlink-speed must be numeric, got: {value}")

    # Validate uplink-load if present
    if "uplink-load" in payload:
        value = payload.get("uplink-load")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "uplink-load must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"uplink-load must be numeric, got: {value}")

    # Validate downlink-load if present
    if "downlink-load" in payload:
        value = payload.get("downlink-load")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "downlink-load must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"downlink-load must be numeric, got: {value}")

    # Validate load-measurement-duration if present
    if "load-measurement-duration" in payload:
        value = payload.get("load-measurement-duration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "load-measurement-duration must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"load-measurement-duration must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_hotspot20_h2qp_wan_metric_delete(
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
