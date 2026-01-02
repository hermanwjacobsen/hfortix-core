"""
Validation helpers for extension-controller fortigate endpoint.

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
    "authorized",  # Enable/disable FortiGate administration.
    "id",  # FortiGate serial number.
    "name",  # FortiGate entry name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "authorized": "discovered",
    "device-id": 1026,
}


# Valid enum values from API documentation
VALID_BODY_AUTHORIZED = ["discovered", "disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fortigate_get(
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
    Validate required fields for extension-controller_fortigate.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "authorized": "value",
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


def validate_fortigate_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - authorized: Enable/disable FortiGate administration.
      - id: FortiGate serial number.
      - name: FortiGate entry name.

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
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "name cannot exceed 19 characters")

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "id cannot exceed 19 characters")

    # Validate authorized if present
    if "authorized" in payload:
        value = payload.get("authorized")
        if value and value not in VALID_BODY_AUTHORIZED:
            return (
                False,
                f"Invalid authorized '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORIZED)}",
            )

    # Validate hostname if present
    if "hostname" in payload:
        value = payload.get("hostname")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "hostname cannot exceed 31 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "vdom must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"vdom must be numeric, got: {value}")

    # Validate device-id if present
    if "device-id" in payload:
        value = payload.get("device-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "device-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"device-id must be numeric, got: {value}")

    # Validate profile if present
    if "profile" in payload:
        value = payload.get("profile")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "profile cannot exceed 31 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_fortigate_put(
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
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "name cannot exceed 19 characters")

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "id cannot exceed 19 characters")

    # Validate authorized if present
    if "authorized" in payload:
        value = payload.get("authorized")
        if value and value not in VALID_BODY_AUTHORIZED:
            return (
                False,
                f"Invalid authorized '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORIZED)}",
            )

    # Validate hostname if present
    if "hostname" in payload:
        value = payload.get("hostname")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "hostname cannot exceed 31 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "vdom must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"vdom must be numeric, got: {value}")

    # Validate device-id if present
    if "device-id" in payload:
        value = payload.get("device-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "device-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"device-id must be numeric, got: {value}")

    # Validate profile if present
    if "profile" in payload:
        value = payload.get("profile")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "profile cannot exceed 31 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_fortigate_delete(
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
