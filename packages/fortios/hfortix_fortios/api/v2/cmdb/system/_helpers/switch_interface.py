"""
Validation helpers for system switch_interface endpoint.

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
    "name",  # Interface name (name cannot be in use by any other interface
    "vdom",  # VDOM that the software switch belongs to.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "intra-switch-policy": "implicit",
    "mac-ttl": 300,
    "span": "disable",
    "span-direction": "both",
    "type": "switch",
}


# Valid enum values from API documentation
VALID_BODY_TYPE = ["switch", "hub"]
VALID_BODY_INTRA_SWITCH_POLICY = ["implicit", "explicit"]
VALID_BODY_SPAN = ["disable", "enable"]
VALID_BODY_SPAN_DIRECTION = ["rx", "tx", "both"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_interface_get(
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
    Validate required fields for system_switch-interface.

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


def validate_switch_interface_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - name: Interface name (name cannot be in use by any other interface
      - vdom: VDOM that the software switch belongs to.

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
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate span-dest-port if present
    if "span-dest-port" in payload:
        value = payload.get("span-dest-port")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "span-dest-port cannot exceed 15 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate intra-switch-policy if present
    if "intra-switch-policy" in payload:
        value = payload.get("intra-switch-policy")
        if value and value not in VALID_BODY_INTRA_SWITCH_POLICY:
            return (
                False,
                f"Invalid intra-switch-policy '{value}'. Must be one of: {', '.join(VALID_BODY_INTRA_SWITCH_POLICY)}",
            )

    # Validate mac-ttl if present
    if "mac-ttl" in payload:
        value = payload.get("mac-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 8640000:
                    return (False, "mac-ttl must be between 300 and 8640000")
            except (ValueError, TypeError):
                return (False, f"mac-ttl must be numeric, got: {value}")

    # Validate span if present
    if "span" in payload:
        value = payload.get("span")
        if value and value not in VALID_BODY_SPAN:
            return (
                False,
                f"Invalid span '{value}'. Must be one of: {', '.join(VALID_BODY_SPAN)}",
            )

    # Validate span-direction if present
    if "span-direction" in payload:
        value = payload.get("span-direction")
        if value and value not in VALID_BODY_SPAN_DIRECTION:
            return (
                False,
                f"Invalid span-direction '{value}'. Must be one of: {', '.join(VALID_BODY_SPAN_DIRECTION)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_interface_put(
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
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate span-dest-port if present
    if "span-dest-port" in payload:
        value = payload.get("span-dest-port")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "span-dest-port cannot exceed 15 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate intra-switch-policy if present
    if "intra-switch-policy" in payload:
        value = payload.get("intra-switch-policy")
        if value and value not in VALID_BODY_INTRA_SWITCH_POLICY:
            return (
                False,
                f"Invalid intra-switch-policy '{value}'. Must be one of: {', '.join(VALID_BODY_INTRA_SWITCH_POLICY)}",
            )

    # Validate mac-ttl if present
    if "mac-ttl" in payload:
        value = payload.get("mac-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 8640000:
                    return (False, "mac-ttl must be between 300 and 8640000")
            except (ValueError, TypeError):
                return (False, f"mac-ttl must be numeric, got: {value}")

    # Validate span if present
    if "span" in payload:
        value = payload.get("span")
        if value and value not in VALID_BODY_SPAN:
            return (
                False,
                f"Invalid span '{value}'. Must be one of: {', '.join(VALID_BODY_SPAN)}",
            )

    # Validate span-direction if present
    if "span-direction" in payload:
        value = payload.get("span-direction")
        if value and value not in VALID_BODY_SPAN_DIRECTION:
            return (
                False,
                f"Invalid span-direction '{value}'. Must be one of: {', '.join(VALID_BODY_SPAN_DIRECTION)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_switch_interface_delete(
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
