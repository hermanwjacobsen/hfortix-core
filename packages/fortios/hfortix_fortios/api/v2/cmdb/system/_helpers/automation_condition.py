"""
Validation helpers for system automation_condition endpoint.

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
    "cpu-usage-percent",  # CPU usage reaches specified percentage.
    "mem-usage-percent",  # Memory usage reaches specified percentage.
    "name",  # Name.
    "vdom",  # Virtual domain which the tunnel belongs to.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "condition-type": "cpu",
    "vdom": "root",
    "vpn-tunnel-state": "tunnel-up",
}

# Fields wrongly marked as required in schema (schema bugs)
# These are specialized features and should be OPTIONAL
SCHEMA_FALSE_POSITIVES = [
    "vpn-tunnel-name",  # VPN tunnel name.
]


# Valid enum values from API documentation
VALID_BODY_CONDITION_TYPE = ["cpu", "memory", "vpn"]
VALID_BODY_VPN_TUNNEL_STATE = ["tunnel-up", "tunnel-down"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_automation_condition_get(
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
    Validate required fields for system_automation-condition.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "cpu-usage-percent": "value",
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


def validate_automation_condition_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - cpu-usage-percent: CPU usage reaches specified percentage.
      - mem-usage-percent: Memory usage reaches specified percentage.
      - name: Name.
      - vdom: Virtual domain which the tunnel belongs to.

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

    # Validate condition-type if present
    if "condition-type" in payload:
        value = payload.get("condition-type")
        if value and value not in VALID_BODY_CONDITION_TYPE:
            return (
                False,
                f"Invalid condition-type '{value}'. Must be one of: {', '.join(VALID_BODY_CONDITION_TYPE)}",
            )

    # Validate cpu-usage-percent if present
    if "cpu-usage-percent" in payload:
        value = payload.get("cpu-usage-percent")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "cpu-usage-percent must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cpu-usage-percent must be numeric, got: {value}",
                )

    # Validate mem-usage-percent if present
    if "mem-usage-percent" in payload:
        value = payload.get("mem-usage-percent")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "mem-usage-percent must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"mem-usage-percent must be numeric, got: {value}",
                )

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate vpn-tunnel-name if present
    if "vpn-tunnel-name" in payload:
        value = payload.get("vpn-tunnel-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "vpn-tunnel-name cannot exceed 79 characters")

    # Validate vpn-tunnel-state if present
    if "vpn-tunnel-state" in payload:
        value = payload.get("vpn-tunnel-state")
        if value and value not in VALID_BODY_VPN_TUNNEL_STATE:
            return (
                False,
                f"Invalid vpn-tunnel-state '{value}'. Must be one of: {', '.join(VALID_BODY_VPN_TUNNEL_STATE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_automation_condition_put(
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

    # Validate condition-type if present
    if "condition-type" in payload:
        value = payload.get("condition-type")
        if value and value not in VALID_BODY_CONDITION_TYPE:
            return (
                False,
                f"Invalid condition-type '{value}'. Must be one of: {', '.join(VALID_BODY_CONDITION_TYPE)}",
            )

    # Validate cpu-usage-percent if present
    if "cpu-usage-percent" in payload:
        value = payload.get("cpu-usage-percent")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "cpu-usage-percent must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cpu-usage-percent must be numeric, got: {value}",
                )

    # Validate mem-usage-percent if present
    if "mem-usage-percent" in payload:
        value = payload.get("mem-usage-percent")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "mem-usage-percent must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"mem-usage-percent must be numeric, got: {value}",
                )

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate vpn-tunnel-name if present
    if "vpn-tunnel-name" in payload:
        value = payload.get("vpn-tunnel-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "vpn-tunnel-name cannot exceed 79 characters")

    # Validate vpn-tunnel-state if present
    if "vpn-tunnel-state" in payload:
        value = payload.get("vpn-tunnel-state")
        if value and value not in VALID_BODY_VPN_TUNNEL_STATE:
            return (
                False,
                f"Invalid vpn-tunnel-state '{value}'. Must be one of: {', '.join(VALID_BODY_VPN_TUNNEL_STATE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_automation_condition_delete(
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
