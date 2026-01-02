"""
Validation helpers for firewall shaper_traffic_shaper endpoint.

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
    "name",  # Traffic shaper name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "bandwidth-unit": "kbps",
    "cos-marking": "disable",
    "cos-marking-method": "static",
    "diffserv": "disable",
    "dscp-marking-method": "static",
    "per-policy": "disable",
    "priority": "high",
}


# Valid enum values from API documentation
VALID_BODY_BANDWIDTH_UNIT = ["kbps", "mbps", "gbps"]
VALID_BODY_PRIORITY = ["low", "medium", "high"]
VALID_BODY_PER_POLICY = ["disable", "enable"]
VALID_BODY_DIFFSERV = ["enable", "disable"]
VALID_BODY_DSCP_MARKING_METHOD = ["multi-stage", "static"]
VALID_BODY_COS_MARKING = ["enable", "disable"]
VALID_BODY_COS_MARKING_METHOD = ["multi-stage", "static"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_shaper_traffic_shaper_get(
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
    Validate required fields for firewall_shaper_traffic-shaper.

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


def validate_shaper_traffic_shaper_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: Traffic shaper name.

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

    # Validate guaranteed-bandwidth if present
    if "guaranteed-bandwidth" in payload:
        value = payload.get("guaranteed-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "guaranteed-bandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"guaranteed-bandwidth must be numeric, got: {value}",
                )

    # Validate maximum-bandwidth if present
    if "maximum-bandwidth" in payload:
        value = payload.get("maximum-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "maximum-bandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"maximum-bandwidth must be numeric, got: {value}",
                )

    # Validate bandwidth-unit if present
    if "bandwidth-unit" in payload:
        value = payload.get("bandwidth-unit")
        if value and value not in VALID_BODY_BANDWIDTH_UNIT:
            return (
                False,
                f"Invalid bandwidth-unit '{value}'. Must be one of: {', '.join(VALID_BODY_BANDWIDTH_UNIT)}",
            )

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value and value not in VALID_BODY_PRIORITY:
            return (
                False,
                f"Invalid priority '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY)}",
            )

    # Validate per-policy if present
    if "per-policy" in payload:
        value = payload.get("per-policy")
        if value and value not in VALID_BODY_PER_POLICY:
            return (
                False,
                f"Invalid per-policy '{value}'. Must be one of: {', '.join(VALID_BODY_PER_POLICY)}",
            )

    # Validate diffserv if present
    if "diffserv" in payload:
        value = payload.get("diffserv")
        if value and value not in VALID_BODY_DIFFSERV:
            return (
                False,
                f"Invalid diffserv '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV)}",
            )

    # Validate dscp-marking-method if present
    if "dscp-marking-method" in payload:
        value = payload.get("dscp-marking-method")
        if value and value not in VALID_BODY_DSCP_MARKING_METHOD:
            return (
                False,
                f"Invalid dscp-marking-method '{value}'. Must be one of: {', '.join(VALID_BODY_DSCP_MARKING_METHOD)}",
            )

    # Validate exceed-bandwidth if present
    if "exceed-bandwidth" in payload:
        value = payload.get("exceed-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "exceed-bandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"exceed-bandwidth must be numeric, got: {value}",
                )

    # Validate cos-marking if present
    if "cos-marking" in payload:
        value = payload.get("cos-marking")
        if value and value not in VALID_BODY_COS_MARKING:
            return (
                False,
                f"Invalid cos-marking '{value}'. Must be one of: {', '.join(VALID_BODY_COS_MARKING)}",
            )

    # Validate cos-marking-method if present
    if "cos-marking-method" in payload:
        value = payload.get("cos-marking-method")
        if value and value not in VALID_BODY_COS_MARKING_METHOD:
            return (
                False,
                f"Invalid cos-marking-method '{value}'. Must be one of: {', '.join(VALID_BODY_COS_MARKING_METHOD)}",
            )

    # Validate overhead if present
    if "overhead" in payload:
        value = payload.get("overhead")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (False, "overhead must be between 0 and 100")
            except (ValueError, TypeError):
                return (False, f"overhead must be numeric, got: {value}")

    # Validate exceed-class-id if present
    if "exceed-class-id" in payload:
        value = payload.get("exceed-class-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "exceed-class-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"exceed-class-id must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_shaper_traffic_shaper_put(
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

    # Validate guaranteed-bandwidth if present
    if "guaranteed-bandwidth" in payload:
        value = payload.get("guaranteed-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "guaranteed-bandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"guaranteed-bandwidth must be numeric, got: {value}",
                )

    # Validate maximum-bandwidth if present
    if "maximum-bandwidth" in payload:
        value = payload.get("maximum-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "maximum-bandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"maximum-bandwidth must be numeric, got: {value}",
                )

    # Validate bandwidth-unit if present
    if "bandwidth-unit" in payload:
        value = payload.get("bandwidth-unit")
        if value and value not in VALID_BODY_BANDWIDTH_UNIT:
            return (
                False,
                f"Invalid bandwidth-unit '{value}'. Must be one of: {', '.join(VALID_BODY_BANDWIDTH_UNIT)}",
            )

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value and value not in VALID_BODY_PRIORITY:
            return (
                False,
                f"Invalid priority '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY)}",
            )

    # Validate per-policy if present
    if "per-policy" in payload:
        value = payload.get("per-policy")
        if value and value not in VALID_BODY_PER_POLICY:
            return (
                False,
                f"Invalid per-policy '{value}'. Must be one of: {', '.join(VALID_BODY_PER_POLICY)}",
            )

    # Validate diffserv if present
    if "diffserv" in payload:
        value = payload.get("diffserv")
        if value and value not in VALID_BODY_DIFFSERV:
            return (
                False,
                f"Invalid diffserv '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV)}",
            )

    # Validate dscp-marking-method if present
    if "dscp-marking-method" in payload:
        value = payload.get("dscp-marking-method")
        if value and value not in VALID_BODY_DSCP_MARKING_METHOD:
            return (
                False,
                f"Invalid dscp-marking-method '{value}'. Must be one of: {', '.join(VALID_BODY_DSCP_MARKING_METHOD)}",
            )

    # Validate exceed-bandwidth if present
    if "exceed-bandwidth" in payload:
        value = payload.get("exceed-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "exceed-bandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"exceed-bandwidth must be numeric, got: {value}",
                )

    # Validate cos-marking if present
    if "cos-marking" in payload:
        value = payload.get("cos-marking")
        if value and value not in VALID_BODY_COS_MARKING:
            return (
                False,
                f"Invalid cos-marking '{value}'. Must be one of: {', '.join(VALID_BODY_COS_MARKING)}",
            )

    # Validate cos-marking-method if present
    if "cos-marking-method" in payload:
        value = payload.get("cos-marking-method")
        if value and value not in VALID_BODY_COS_MARKING_METHOD:
            return (
                False,
                f"Invalid cos-marking-method '{value}'. Must be one of: {', '.join(VALID_BODY_COS_MARKING_METHOD)}",
            )

    # Validate overhead if present
    if "overhead" in payload:
        value = payload.get("overhead")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (False, "overhead must be between 0 and 100")
            except (ValueError, TypeError):
                return (False, f"overhead must be numeric, got: {value}")

    # Validate exceed-class-id if present
    if "exceed-class-id" in payload:
        value = payload.get("exceed-class-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "exceed-class-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"exceed-class-id must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_shaper_traffic_shaper_delete(
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
