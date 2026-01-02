"""
Validation helpers for switch-controller traffic_policy endpoint.

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
    "name",  # Traffic policy name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "guaranteed-bandwidth": 10000,
    "guaranteed-burst": 45000,
    "maximum-burst": 67500,
    "policer-status": "enable",
    "type": "ingress",
}


# Valid enum values from API documentation
VALID_BODY_POLICER_STATUS = ["enable", "disable"]
VALID_BODY_TYPE = ["ingress", "egress"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_traffic_policy_get(
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
    Validate required fields for switch-controller_traffic-policy.

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


def validate_traffic_policy_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: Traffic policy name.

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

    # Validate policer-status if present
    if "policer-status" in payload:
        value = payload.get("policer-status")
        if value and value not in VALID_BODY_POLICER_STATUS:
            return (
                False,
                f"Invalid policer-status '{value}'. Must be one of: {', '.join(VALID_BODY_POLICER_STATUS)}",
            )

    # Validate guaranteed-bandwidth if present
    if "guaranteed-bandwidth" in payload:
        value = payload.get("guaranteed-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 524287000:
                    return (
                        False,
                        "guaranteed-bandwidth must be between 0 and 524287000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"guaranteed-bandwidth must be numeric, got: {value}",
                )

    # Validate guaranteed-burst if present
    if "guaranteed-burst" in payload:
        value = payload.get("guaranteed-burst")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "guaranteed-burst must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"guaranteed-burst must be numeric, got: {value}",
                )

    # Validate maximum-burst if present
    if "maximum-burst" in payload:
        value = payload.get("maximum-burst")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "maximum-burst must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"maximum-burst must be numeric, got: {value}")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate cos-queue if present
    if "cos-queue" in payload:
        value = payload.get("cos-queue")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 7:
                    return (False, "cos-queue must be between 0 and 7")
            except (ValueError, TypeError):
                return (False, f"cos-queue must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_traffic_policy_put(
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

    # Validate policer-status if present
    if "policer-status" in payload:
        value = payload.get("policer-status")
        if value and value not in VALID_BODY_POLICER_STATUS:
            return (
                False,
                f"Invalid policer-status '{value}'. Must be one of: {', '.join(VALID_BODY_POLICER_STATUS)}",
            )

    # Validate guaranteed-bandwidth if present
    if "guaranteed-bandwidth" in payload:
        value = payload.get("guaranteed-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 524287000:
                    return (
                        False,
                        "guaranteed-bandwidth must be between 0 and 524287000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"guaranteed-bandwidth must be numeric, got: {value}",
                )

    # Validate guaranteed-burst if present
    if "guaranteed-burst" in payload:
        value = payload.get("guaranteed-burst")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "guaranteed-burst must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"guaranteed-burst must be numeric, got: {value}",
                )

    # Validate maximum-burst if present
    if "maximum-burst" in payload:
        value = payload.get("maximum-burst")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "maximum-burst must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"maximum-burst must be numeric, got: {value}")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate cos-queue if present
    if "cos-queue" in payload:
        value = payload.get("cos-queue")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 7:
                    return (False, "cos-queue must be between 0 and 7")
            except (ValueError, TypeError):
                return (False, f"cos-queue must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_traffic_policy_delete(
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
