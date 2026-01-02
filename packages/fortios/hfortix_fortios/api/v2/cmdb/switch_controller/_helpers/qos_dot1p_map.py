"""
Validation helpers for switch-controller qos_dot1p_map endpoint.

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
    "egress-pri-tagging",  # Enable/disable egress priority-tag frame.
    "name",  # Dot1p map name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "egress-pri-tagging": "disable",
    "priority-0": "queue-0",
    "priority-1": "queue-0",
    "priority-2": "queue-0",
    "priority-3": "queue-0",
    "priority-4": "queue-0",
    "priority-5": "queue-0",
    "priority-6": "queue-0",
    "priority-7": "queue-0",
}


# Valid enum values from API documentation
VALID_BODY_EGRESS_PRI_TAGGING = ["disable", "enable"]
VALID_BODY_PRIORITY_0 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_1 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_2 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_3 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_4 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_5 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_6 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_7 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_qos_dot1p_map_get(
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
    Validate required fields for switch-controller_qos_dot1p-map.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "egress-pri-tagging": "value",
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


def validate_qos_dot1p_map_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - egress-pri-tagging: Enable/disable egress priority-tag frame.
      - name: Dot1p map name.

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
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate egress-pri-tagging if present
    if "egress-pri-tagging" in payload:
        value = payload.get("egress-pri-tagging")
        if value and value not in VALID_BODY_EGRESS_PRI_TAGGING:
            return (
                False,
                f"Invalid egress-pri-tagging '{value}'. Must be one of: {', '.join(VALID_BODY_EGRESS_PRI_TAGGING)}",
            )

    # Validate priority-0 if present
    if "priority-0" in payload:
        value = payload.get("priority-0")
        if value and value not in VALID_BODY_PRIORITY_0:
            return (
                False,
                f"Invalid priority-0 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_0)}",
            )

    # Validate priority-1 if present
    if "priority-1" in payload:
        value = payload.get("priority-1")
        if value and value not in VALID_BODY_PRIORITY_1:
            return (
                False,
                f"Invalid priority-1 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_1)}",
            )

    # Validate priority-2 if present
    if "priority-2" in payload:
        value = payload.get("priority-2")
        if value and value not in VALID_BODY_PRIORITY_2:
            return (
                False,
                f"Invalid priority-2 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_2)}",
            )

    # Validate priority-3 if present
    if "priority-3" in payload:
        value = payload.get("priority-3")
        if value and value not in VALID_BODY_PRIORITY_3:
            return (
                False,
                f"Invalid priority-3 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_3)}",
            )

    # Validate priority-4 if present
    if "priority-4" in payload:
        value = payload.get("priority-4")
        if value and value not in VALID_BODY_PRIORITY_4:
            return (
                False,
                f"Invalid priority-4 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_4)}",
            )

    # Validate priority-5 if present
    if "priority-5" in payload:
        value = payload.get("priority-5")
        if value and value not in VALID_BODY_PRIORITY_5:
            return (
                False,
                f"Invalid priority-5 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_5)}",
            )

    # Validate priority-6 if present
    if "priority-6" in payload:
        value = payload.get("priority-6")
        if value and value not in VALID_BODY_PRIORITY_6:
            return (
                False,
                f"Invalid priority-6 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_6)}",
            )

    # Validate priority-7 if present
    if "priority-7" in payload:
        value = payload.get("priority-7")
        if value and value not in VALID_BODY_PRIORITY_7:
            return (
                False,
                f"Invalid priority-7 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_7)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_qos_dot1p_map_put(
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
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate egress-pri-tagging if present
    if "egress-pri-tagging" in payload:
        value = payload.get("egress-pri-tagging")
        if value and value not in VALID_BODY_EGRESS_PRI_TAGGING:
            return (
                False,
                f"Invalid egress-pri-tagging '{value}'. Must be one of: {', '.join(VALID_BODY_EGRESS_PRI_TAGGING)}",
            )

    # Validate priority-0 if present
    if "priority-0" in payload:
        value = payload.get("priority-0")
        if value and value not in VALID_BODY_PRIORITY_0:
            return (
                False,
                f"Invalid priority-0 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_0)}",
            )

    # Validate priority-1 if present
    if "priority-1" in payload:
        value = payload.get("priority-1")
        if value and value not in VALID_BODY_PRIORITY_1:
            return (
                False,
                f"Invalid priority-1 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_1)}",
            )

    # Validate priority-2 if present
    if "priority-2" in payload:
        value = payload.get("priority-2")
        if value and value not in VALID_BODY_PRIORITY_2:
            return (
                False,
                f"Invalid priority-2 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_2)}",
            )

    # Validate priority-3 if present
    if "priority-3" in payload:
        value = payload.get("priority-3")
        if value and value not in VALID_BODY_PRIORITY_3:
            return (
                False,
                f"Invalid priority-3 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_3)}",
            )

    # Validate priority-4 if present
    if "priority-4" in payload:
        value = payload.get("priority-4")
        if value and value not in VALID_BODY_PRIORITY_4:
            return (
                False,
                f"Invalid priority-4 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_4)}",
            )

    # Validate priority-5 if present
    if "priority-5" in payload:
        value = payload.get("priority-5")
        if value and value not in VALID_BODY_PRIORITY_5:
            return (
                False,
                f"Invalid priority-5 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_5)}",
            )

    # Validate priority-6 if present
    if "priority-6" in payload:
        value = payload.get("priority-6")
        if value and value not in VALID_BODY_PRIORITY_6:
            return (
                False,
                f"Invalid priority-6 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_6)}",
            )

    # Validate priority-7 if present
    if "priority-7" in payload:
        value = payload.get("priority-7")
        if value and value not in VALID_BODY_PRIORITY_7:
            return (
                False,
                f"Invalid priority-7 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_7)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_qos_dot1p_map_delete(
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
